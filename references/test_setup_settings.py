"""Temp-dir contracts for the project demo password setting; synthetic values only.

Covers the §2 write path: private mode, operator ownership, narrow Git exclusion,
preserved unrelated keys and existing choices, and blocking of malformed or
unsafe destinations before any mutation. No real secret, Docker or profile.
"""
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import setup_settings  # noqa: E402
from setup_settings import SettingsError, write_choice  # noqa: E402

SYNTHETIC = "Synthetic-Shared-Value-1"


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class SettingsWriteTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="maker-settings-"))
        self.project = self.root / "project"
        self.project.mkdir()
        # TMPDIR can sit inside an unrelated repository; stop Git discovery here
        # so "outside Git" fixtures are independent of the host checkout.
        self.saved_ceiling = os.environ.get("GIT_CEILING_DIRECTORIES")
        os.environ["GIT_CEILING_DIRECTORIES"] = str(self.root)

    def tearDown(self):
        if self.saved_ceiling is None:
            os.environ.pop("GIT_CEILING_DIRECTORIES", None)
        else:
            os.environ["GIT_CEILING_DIRECTORIES"] = self.saved_ceiling
        for path in self.root.rglob("*"):
            try:
                path.chmod(0o700)
            except OSError:
                pass
        shutil.rmtree(self.root)

    @property
    def demo(self):
        return self.project / "demo"

    @property
    def settings(self):
        return self.demo / "settings.json"

    def read(self):
        return json.loads(self.settings.read_text())

    def init_repo(self, root=None):
        target = root or self.project
        result = git(target, "init", "-q")
        self.assertEqual(result.returncode, 0, result.stderr)
        return target

    def test_shared_choice_creates_a_private_operator_file(self):
        summary = write_choice(str(self.project), {"mode": "shared", "value": SYNTHETIC})
        self.assertEqual(summary["status"], "written")
        self.assertEqual(summary["path"], str(self.settings))
        self.assertEqual(summary["choice"], "shared")
        self.assertEqual(self.read(), {"password": {"mode": "shared", "value": SYNTHETIC}})
        info = os.lstat(self.settings)
        self.assertTrue(stat.S_ISREG(info.st_mode))
        self.assertEqual(stat.S_IMODE(info.st_mode), 0o600)
        self.assertEqual(info.st_uid, os.getuid())

    def test_random_choice_stores_the_mode_without_a_value(self):
        summary = write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(summary["status"], "written")
        self.assertEqual(self.read(), {"password": {"mode": "random"}})

    def test_skip_writes_no_file_and_no_directory(self):
        summary = write_choice(str(self.project), None)
        self.assertEqual(summary["status"], "skipped")
        self.assertFalse(self.demo.exists())
        self.assertFalse(self.settings.exists())

    def test_skip_keeps_an_existing_choice_untouched(self):
        self.demo.mkdir()
        self.settings.write_text(json.dumps({"password": {"mode": "random"}}))
        self.settings.chmod(0o600)
        before = self.settings.read_bytes()
        summary = write_choice(str(self.project), None)
        self.assertEqual(summary["status"], "existing")
        self.assertEqual(self.settings.read_bytes(), before)

    def test_unrelated_keys_are_preserved_on_write(self):
        self.demo.mkdir()
        self.settings.write_text(json.dumps({"note": "keep-me", "count": 2}))
        self.settings.chmod(0o600)
        write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(self.read(), {"note": "keep-me", "count": 2,
                                       "password": {"mode": "random"}})

    def test_existing_choice_wins_on_resume(self):
        write_choice(str(self.project), {"mode": "shared", "value": SYNTHETIC})
        summary = write_choice(str(self.project), {"mode": "shared", "value": "Other-Synthetic-2"})
        self.assertEqual(summary["status"], "existing")
        self.assertEqual(self.read()["password"]["value"], SYNTHETIC)

    def test_later_operator_choice_is_not_overwritten(self):
        write_choice(str(self.project), {"mode": "shared", "value": SYNTHETIC})
        changed = {"password": {"mode": "shared", "value": "Later-Synthetic-3"}}
        self.settings.write_text(json.dumps(changed))
        summary = write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(summary["status"], "existing")
        self.assertEqual(self.read(), changed)

    def test_existing_secret_in_a_tracked_file_blocks(self):
        self.init_repo()
        self.demo.mkdir()
        self.settings.write_text(json.dumps({"password": {"mode": "random"}}))
        self.settings.chmod(0o600)
        self.assertEqual(git(self.project, "add", "demo/settings.json").returncode, 0)
        with self.assertRaises(SettingsError):
            write_choice(str(self.project), None)
        self.assertEqual(self.read(), {"password": {"mode": "random"}})

    def test_existing_secret_adds_the_narrow_rule_without_changing_the_choice(self):
        self.init_repo()
        self.demo.mkdir()
        raw = json.dumps({"password": {"mode": "random"}, "note": "keep-me"})
        self.settings.write_text(raw)
        self.settings.chmod(0o600)
        before = self.settings.read_bytes()
        summary = write_choice(str(self.project), None)
        self.assertEqual(summary["status"], "existing")
        self.assertEqual(summary["ignore"], "added")
        self.assertEqual(self.settings.read_bytes(), before)
        self.assertEqual((self.demo / ".gitignore").read_text(), "/settings.json\n")

    def test_malformed_settings_block_before_mutation(self):
        self.demo.mkdir()
        for raw in ("{not json", "[]", '{"password": "plain"}',
                    '{"password": {"mode": "random", "value": "x"}}',
                    '{"password": {"mode": "shared", "value": ""}}',
                    '{"password": {"mode": "shared"}}'):
            with self.subTest(raw=raw):
                self.settings.write_text(raw)
                self.settings.chmod(0o600)
                with self.assertRaises(SettingsError):
                    write_choice(str(self.project), {"mode": "random"})
                self.assertEqual(self.settings.read_text(), raw)

    def test_duplicate_json_keys_block(self):
        self.demo.mkdir()
        raw = '{"password": {"mode": "random"}, "password": {"mode": "random"}}'
        self.settings.write_text(raw)
        self.settings.chmod(0o600)
        with self.assertRaises(SettingsError):
            write_choice(str(self.project), None)

    def test_non_private_existing_file_blocks(self):
        self.demo.mkdir()
        self.settings.write_text("{}")
        self.settings.chmod(0o644)
        with self.assertRaises(SettingsError):
            write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(stat.S_IMODE(os.lstat(self.settings).st_mode), 0o644)

    def test_symlinked_settings_file_blocks(self):
        self.demo.mkdir()
        foreign = self.root / "foreign.json"
        foreign.write_text("{}")
        self.settings.symlink_to(foreign)
        with self.assertRaises(SettingsError):
            write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(foreign.read_text(), "{}")

    def test_symlinked_demo_directory_blocks(self):
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        self.demo.symlink_to(elsewhere, target_is_directory=True)
        with self.assertRaises(SettingsError):
            write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_relative_or_missing_project_blocks(self):
        for bad in ("project", "", str(self.project / "missing"), str(self.settings)):
            with self.subTest(bad=bad):
                with self.assertRaises(SettingsError):
                    write_choice(bad, {"mode": "random"})
        self.assertFalse(self.demo.exists())

    def test_invalid_choice_blocks_before_creating_anything(self):
        for bad in ({"mode": "plain"}, {"mode": "shared"},
                    {"mode": "shared", "value": ""},
                    {"mode": "shared", "value": "broken\x00value"},
                    {"mode": "random", "value": "x"},
                    {"mode": "shared", "value": SYNTHETIC, "extra": 1},
                    "shared"):
            with self.subTest(bad=bad):
                with self.assertRaises(SettingsError):
                    write_choice(str(self.project), bad)
                self.assertFalse(self.demo.exists())

    def test_tracked_destination_blocks_the_write(self):
        self.init_repo()
        self.demo.mkdir()
        self.settings.write_text("{}\n")
        self.settings.chmod(0o600)
        self.assertEqual(git(self.project, "add", "demo/settings.json").returncode, 0)
        with self.assertRaises(SettingsError):
            write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(self.read(), {})

    def test_git_root_writes_a_narrow_ignore_rule_and_verifies_it(self):
        self.init_repo()
        summary = write_choice(str(self.project), {"mode": "shared", "value": SYNTHETIC})
        self.assertEqual(summary["ignore"], "added")
        self.assertEqual((self.demo / ".gitignore").read_text(), "/settings.json\n")
        rel = "demo/settings.json"
        self.assertEqual(git(self.project, "check-ignore", "-q", "--", rel).returncode, 0,
                         "the settings path must be ignored before the secret is written")
        self.assertEqual(git(self.project, "ls-files", "--error-unmatch", "--", rel).returncode, 1)
        self.assertEqual(self.read()["password"]["value"], SYNTHETIC)

    def test_existing_project_ignore_rules_are_preserved_and_rule_added_once(self):
        self.init_repo()
        self.demo.mkdir()
        ignore = self.demo / ".gitignore"
        ignore.write_text("runtime/\n# keep this comment\n")
        write_choice(str(self.project), {"mode": "random"})
        first = ignore.read_text()
        self.assertTrue(first.startswith("runtime/\n# keep this comment\n"))
        self.assertEqual(first.count("/settings.json"), 1)
        write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(ignore.read_text(), first)

    def test_already_ignored_destination_needs_no_rule(self):
        self.init_repo()
        self.demo.mkdir()
        (self.project / ".gitignore").write_text("demo/\n")
        summary = write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(summary["ignore"], "unchanged")
        self.assertFalse((self.demo / ".gitignore").exists())

    def test_secret_staging_stays_outside_the_git_work_tree(self):
        self.init_repo()
        seen = []
        real_mkstemp = tempfile.mkstemp

        def spy(*args, **kwargs):
            seen.append((kwargs.get("dir"), kwargs.get("prefix")))
            return real_mkstemp(*args, **kwargs)

        with mock.patch.object(setup_settings.tempfile, "mkstemp", side_effect=spy):
            write_choice(str(self.project), {"mode": "shared", "value": SYNTHETIC})
        gitdir = Path(git(self.project, "rev-parse", "--absolute-git-dir")
                      .stdout.decode().strip()).resolve()
        staged = [Path(directory).resolve() for directory, prefix in seen
                  if prefix == ".settings-"]
        self.assertTrue(staged, "the write must stage the secret in a private file")
        for directory in staged:
            self.assertEqual(directory, gitdir,
                             "the secret staging file must not be inside the Git work tree")

    def test_outside_git_writes_no_repository_and_no_ignore_file(self):
        summary = write_choice(str(self.project), {"mode": "random"})
        self.assertEqual(summary["ignore"], "not-in-git")
        self.assertFalse((self.project / ".git").exists())
        self.assertFalse((self.demo / ".gitignore").exists())
        self.assertTrue(self.settings.is_file())

    @unittest.skipIf(os.geteuid() == 0, "root ignores directory permissions")
    def test_unwritable_demo_directory_blocks_before_the_secret(self):
        self.demo.mkdir()
        self.demo.chmod(0o500)
        with self.assertRaises(SettingsError):
            write_choice(str(self.project), {"mode": "shared", "value": SYNTHETIC})
        self.assertFalse(self.settings.exists())

    @unittest.skipIf(os.geteuid() == 0, "root ignores directory permissions")
    def test_unwritable_destination_leaves_the_ignore_file_unchanged(self):
        self.init_repo()
        self.demo.mkdir()
        ignore = self.demo / ".gitignore"
        ignore.write_text("runtime/\n")
        self.demo.chmod(0o500)
        with self.assertRaises(SettingsError):
            write_choice(str(self.project), {"mode": "shared", "value": SYNTHETIC})
        self.assertEqual(ignore.read_text(), "runtime/\n")
        self.assertFalse(self.settings.exists())

    def test_world_writable_demo_directory_blocks(self):
        self.demo.mkdir()
        for mode in (0o777, 0o707, 0o702):
            with self.subTest(mode=oct(mode)):
                self.demo.chmod(mode)
                with self.assertRaises(SettingsError):
                    write_choice(str(self.project), {"mode": "random"})
                self.assertFalse(self.settings.exists())

    def test_summary_never_contains_the_value(self):
        summary = write_choice(str(self.project), {"mode": "shared", "value": SYNTHETIC})
        self.assertNotIn(SYNTHETIC, json.dumps(summary))


class SettingsCliTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="maker-settings-cli-"))
        self.project = self.root / "project"
        self.project.mkdir()
        self.script = Path(__file__).resolve().parent / "setup_settings.py"
        self.saved_ceiling = os.environ.get("GIT_CEILING_DIRECTORIES")
        os.environ["GIT_CEILING_DIRECTORIES"] = str(self.root)

    def tearDown(self):
        if self.saved_ceiling is None:
            os.environ.pop("GIT_CEILING_DIRECTORIES", None)
        else:
            os.environ["GIT_CEILING_DIRECTORIES"] = self.saved_ceiling
        shutil.rmtree(self.root)

    def run_cli(self, *args, stdin=b""):
        return subprocess.run([sys.executable, "-B", str(self.script), "--project",
                               str(self.project), *args], input=stdin,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def test_shared_value_is_read_from_stdin_only(self):
        result = self.run_cli("--mode", "shared", stdin=(SYNTHETIC + "\n").encode())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn(SYNTHETIC.encode(), result.stdout + result.stderr)
        stored = json.loads((self.project / "demo/settings.json").read_text())
        self.assertEqual(stored["password"]["value"], SYNTHETIC)

    def test_random_mode_needs_no_stdin(self):
        result = self.run_cli("--mode", "random")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "written")

    def test_empty_or_multiline_stdin_is_refused_without_a_file(self):
        for stdin in (b"", b"\n", b"\n\n", b"value\x00byte\n"):
            with self.subTest(stdin=stdin):
                result = self.run_cli("--mode", "shared", stdin=stdin)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.project / "demo/settings.json").exists())

    def test_a_password_argument_is_not_accepted(self):
        result = self.run_cli("--mode", "shared", "--value", SYNTHETIC, stdin=b"unused\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.project / "demo/settings.json").exists())

    def test_an_unknown_argument_never_echoes_a_supplied_value(self):
        result = self.run_cli("--mode", "shared", "--value", SYNTHETIC, stdin=b"unused\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(SYNTHETIC.encode(), result.stdout + result.stderr)
        self.assertFalse((self.project / "demo/settings.json").exists())

    def test_refusal_message_never_echoes_the_value(self):
        (self.project / "demo").mkdir()
        settings = self.project / "demo/settings.json"
        settings.write_text("{broken")
        settings.chmod(0o600)
        result = self.run_cli("--mode", "shared", stdin=(SYNTHETIC + "\n").encode())
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(SYNTHETIC.encode(), result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
