"""Deterministic project demo password setting, MIT.

Writes `<project>/demo/settings.json` for the disposable-demo skill: one
`password` policy (`shared` with a value, or `random`), file mode 0600, owned by
the invoking operator, excluded from Git with a narrow rule, unrelated keys and
an existing choice preserved. Validates everything before mutating; malformed
settings, a tracked destination, a world-writable demo directory or an
unsafe/unwritable target block the write. A Git-managed destination stages the
secret in the Git directory, never in the work tree.

No network, Docker, profile or privilege access. The value never appears in an
argument or output; the CLI reads a shared value from stdin only.
"""
import argparse
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
from typing import NoReturn

FILE_MODE = 0o600
DIR_MODE = 0o700
IGNORE_LINE = "/settings.json"
SETTINGS = ("demo", "settings.json")


class SettingsError(ValueError):
    """The destination or the requested policy cannot be written safely."""


def _fail(message) -> NoReturn:
    raise SettingsError(message)


def _project(path):
    if not isinstance(path, str) or not path or not os.path.isabs(path):
        _fail("Project root must be an absolute path")
    if os.path.normpath(path) != path:
        _fail("Project root must be a canonical absolute path")
    if os.path.realpath(path) != path:
        _fail("Project root must not contain a symlink component")
    try:
        info = os.lstat(path)
    except OSError:
        _fail("Project root is missing or unreadable")
    if not stat.S_ISDIR(info.st_mode):
        _fail("Project root must be a directory")
    return path


def _policy(value):
    """Accept exactly the two documented policies; never coerce or repair."""
    if not isinstance(value, dict) or "mode" not in value:
        _fail("Invalid password policy")
    mode = value["mode"]
    if mode == "shared":
        if set(value) != {"mode", "value"}:
            _fail("Invalid shared password policy")
        secret = value["value"]
        if (not isinstance(secret, str) or not secret or any(c in secret for c in "\x00\r\n")):
            _fail("Expected a single-line shared password")
        return {"mode": "shared", "value": secret}
    if mode == "random":
        if set(value) != {"mode"}:
            _fail("Invalid random password policy")
        return {"mode": "random"}
    _fail("Invalid password policy")


def _object(raw):
    def unique(pairs):
        seen = {}
        for key, item in pairs:
            if key in seen:
                raise SettingsError("Duplicate key in settings.json")
            seen[key] = item
        return seen
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=unique)
    except (UnicodeDecodeError, ValueError) as error:
        raise SettingsError("Invalid settings.json") from error
    if not isinstance(value, dict):
        raise SettingsError("settings.json must contain a JSON object")
    return value


def _private_bytes(path):
    try:
        handle = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except OSError as error:
        raise SettingsError("Cannot read settings.json safely") from error
    with os.fdopen(handle, "rb") as stream:
        info = os.fstat(stream.fileno())
        if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid()
                or stat.S_IMODE(info.st_mode) != FILE_MODE or info.st_nlink != 1):
            raise SettingsError("settings.json must be an operator-owned private file (0600)")
        return stream.read()


def _demo_dir(project):
    demo = os.path.join(project, *SETTINGS[:-1])
    try:
        info = os.lstat(demo)
    except FileNotFoundError:
        return demo, False
    except OSError as error:
        raise SettingsError("Cannot inspect the demo directory") from error
    if (stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode)
            or info.st_uid != os.getuid()
            or stat.S_IMODE(info.st_mode) & 0o002):
        raise SettingsError("demo directory must be an operator-owned real directory "
                            "that is not world-writable")
    return demo, True


def _git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def _repo_root(project):
    result = _git(project, "rev-parse", "--show-toplevel")
    if result.returncode == 0:
        return result.stdout.decode().strip() or None
    if b"not a git repository" in result.stderr:
        return None
    raise SettingsError("Git state could not be verified; refusing the settings write")


def _target_relative(repo, settings):
    try:
        return os.path.relpath(settings, repo)
    except ValueError as error:
        raise SettingsError("Settings path is outside its Git work tree") from error


def _git_state(project, settings):
    repo = _repo_root(project)
    if repo is None:
        return None
    return repo, _target_relative(repo, settings)


def _git_dir(project):
    result = _git(project, "rev-parse", "--absolute-git-dir")
    path = result.stdout.decode().strip() if result.returncode == 0 else ""
    if not path or not os.path.isabs(path):
        raise SettingsError("Git directory could not be verified; refusing the settings write")
    return path


def _check_tracked(repo, relative):
    result = _git(repo, "ls-files", "--error-unmatch", "--", relative)
    if result.returncode == 0:
        raise SettingsError("Destination is already tracked by Git")
    if result.returncode != 1:
        raise SettingsError("Git tracked state could not be verified")


def _check_ignored(repo, relative):
    result = _git(repo, "check-ignore", "-q", "--", relative)
    if result.returncode == 0:
        return True
    if result.returncode == 1:
        return False
    raise SettingsError("Git ignore state could not be verified")


def _append_rule(demo, ignore_path):
    info = None
    try:
        info = os.lstat(ignore_path)
    except FileNotFoundError:
        pass
    except OSError as error:
        raise SettingsError("Cannot inspect demo/.gitignore") from error
    if info is not None and (stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode)):
        raise SettingsError("demo/.gitignore must be a regular file")
    try:
        handle = os.open(ignore_path, os.O_WRONLY | os.O_APPEND | os.O_CREAT
                         | os.O_NOFOLLOW, 0o644)
    except OSError as error:
        raise SettingsError("Cannot update demo/.gitignore") from error
    with os.fdopen(handle, "ab") as stream:
        current = b""
        if info is not None:
            with open(ignore_path, "rb") as existing:
                current = existing.read()
        prefix = current and not current.endswith(b"\n") and b"\n" or b""
        stream.write(prefix + IGNORE_LINE.encode() + b"\n")


def _exclude(project, demo, settings, state=None):
    """Return the ignore status; must prove the path untracked and ignored."""
    if state is None:
        state = _git_state(project, settings)
    if state is None:
        return "not-in-git"
    repo, relative = state
    _check_tracked(repo, relative)
    if _check_ignored(repo, relative):
        return "unchanged"
    _append_rule(demo, os.path.join(demo, ".gitignore"))
    if not _check_ignored(repo, relative):
        raise SettingsError("Settings path is still not ignored; refusing the write")
    return "added"


def _writable(demo):
    """Prove the destination is writable before any ignore-file mutation."""
    try:
        descriptor, probe = tempfile.mkstemp(dir=demo, prefix=".settings-probe-")
    except OSError as error:
        raise SettingsError("Settings destination is not writable") from error
    os.close(descriptor)
    try:
        os.unlink(probe)
    except OSError:
        pass


def _write_private(settings, data, staging):
    content = (json.dumps(data, ensure_ascii=True, indent=2) + "\n").encode()
    try:
        descriptor, temporary = tempfile.mkstemp(dir=staging, prefix=".settings-")
    except OSError as error:
        raise SettingsError("Settings destination is not writable") from error
    try:
        with os.fdopen(descriptor, "wb") as stream:
            os.fchmod(stream.fileno(), FILE_MODE)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, settings)
    except OSError as error:
        raise SettingsError("Settings write failed") from error
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
    if _object(_private_bytes(settings)) != data:
        raise SettingsError("Settings readback differs from the requested value")


def write_choice(project, choice=None):
    """Write or preserve the demo password policy; return metadata without a value.

    ``choice`` is ``None`` (skip), ``{"mode": "random"}`` or
    ``{"mode": "shared", "value": "..."}``.
    """
    project = _project(project)
    requested = None if choice is None else _policy(choice)
    demo, exists = _demo_dir(project)
    settings = os.path.join(demo, SETTINGS[-1])
    data = {}
    if exists:
        try:
            os.lstat(settings)
        except FileNotFoundError:
            pass
        except OSError as error:
            raise SettingsError("Cannot inspect settings.json") from error
        else:
            data = _object(_private_bytes(settings))
            if "password" in data:
                _policy(data["password"])
                state = _git_state(project, settings)
                ignore = _exclude(project, demo, settings, state)
                return {"status": "existing", "path": settings,
                        "choice": data["password"]["mode"], "ignore": ignore}
    if requested is None:
        return {"status": "skipped", "path": settings, "choice": "default",
                "ignore": "unchanged"}
    if not exists:
        try:
            os.mkdir(demo, DIR_MODE)
        except OSError as error:
            raise SettingsError("Cannot create the demo directory") from error
    _writable(demo)
    state = _git_state(project, settings)
    staging = _git_dir(project) if state is not None else demo
    if staging != demo:
        _writable(staging)
        try:
            same_device = os.stat(staging).st_dev == os.stat(demo).st_dev
        except OSError as error:
            raise SettingsError("Settings staging path could not be verified") from error
        if not same_device:
            raise SettingsError("Settings destination and Git directory are on different filesystems")
    ignore = _exclude(project, demo, settings, state)
    updated = dict(data)
    updated["password"] = requested
    _write_private(settings, updated, staging)
    return {"status": "written", "path": settings, "choice": requested["mode"],
            "ignore": ignore}


class _Parser(argparse.ArgumentParser):
    """Refuse invalid arguments without echoing raw argv values."""

    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, "Blocked: invalid command arguments\n")


def main(argv=None):
    parser = _Parser(description="Write the project demo password policy.")
    parser.add_argument("--project", required=True, help="Canonical absolute project root")
    parser.add_argument("--mode", required=True, choices=("shared", "random"))
    arguments = parser.parse_args(argv)
    choice = {"mode": "random"}
    if arguments.mode == "shared":
        raw = sys.stdin.buffer.read()
        if raw.endswith(b"\n"):
            raw = raw[:-1]
        try:
            value = raw.decode("utf-8")
        except UnicodeDecodeError:
            parser.error("Shared password must be UTF-8 text on stdin")
        choice = {"mode": "shared", "value": value}
    try:
        summary = write_choice(arguments.project, choice)
    except SettingsError as error:
        print(f"Blocked: {error}", file=sys.stderr)
        return 1
    print(json.dumps(summary, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
