"""User-triggered Maker file updates. Standard library + local Git only (MIT).

No Hermes bootstrap, networking, worker control, configuration writes or deletion.
Activity evidence is deliberately conservative: absence of visible processes does
not establish an idle dispatcher. The operator must resolve unknown activity.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import tempfile
import uuid
from datetime import datetime, timezone

from render_text import ROLE_NAMES, render_role, role_fields

LEGACY_COMMIT = '21cae6551c03b6ab84d004f41fc81c921e3e9837'
LEGACY_VERSION = '1.0.0'
SCHEMA = 1
OPERATIONAL = ('references/integrations.md', 'references/setup.md',
               'references/code-analysis.md', 'references/native-workflow.md',
               'references/kanban-block-triage-escalation.md', 'references/render_text.py')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(data):
    return base64.b64encode(data).decode('ascii')


def decoded(data):
    return base64.b64decode(data, validate=True)


def json_bytes(data):
    return (json.dumps(data, ensure_ascii=True, indent=2, sort_keys=True) + '\n').encode()


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.PIPE)


def revision(repo, ref):
    if not isinstance(ref, str) or ref.startswith('-'):
        raise ValueError('Invalid revision')
    return git(repo, 'rev-parse', '--verify', ref + '^{commit}').decode().strip()


def package_version(repo, commit):
    """Use existing package SemVer; the schema is only a record format."""
    version = json.loads(blob(repo, commit, 'manifest.json'))['version']
    frontmatter = blob(repo, commit, 'SKILL.md').decode().split('---', 2)[1]
    match = re.search(r'^version: ([^\n]+)$', frontmatter, re.MULTILINE)
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', version) or not match or match[1] != version:
        raise ValueError('Package version must be matching SemVer in SKILL.md and manifest.json')
    return version


def legacy_baseline(repo):
    commit = revision(repo, LEGACY_COMMIT)
    if package_version(repo, commit) != LEGACY_VERSION:
        raise ValueError('User-defined legacy safepoint version mismatch')
    return {'maker_commit': commit, 'maker_version': LEGACY_VERSION,
            'provenance': 'user-defined-1.0.0-safepoint',
            'historical_installation_verified': False,
            'scope': 'SOULs only; legacy skill baseline remains unknown'}


def safe_relative(value):
    if not isinstance(value, str):
        raise ValueError('Expected relative path string')
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(x in ('', '.', '..') for x in value.split('/')) or '\\' in value:
        raise ValueError('Unsafe relative path: ' + str(value))
    return path


def guarded(path):
    path = Path(path)
    if not path.is_absolute() or '..' in path.parts:
        raise ValueError('Expected absolute canonical path: ' + str(path))
    for parent in [*reversed(path.parents), path]:
        if parent.is_symlink():
            raise ValueError('Symlink rejected: ' + str(parent))
        if parent.exists() and parent != path and not parent.is_dir():
            raise ValueError('Non-directory ancestor: ' + str(parent))
    if path.exists() and not (path.is_file() or path.is_dir()):
        raise ValueError('Non-regular path: ' + str(path))
    return path


def read(path):
    path = guarded(path)
    if not path.exists():
        return None
    if not path.is_file() or path.stat().st_nlink != 1:
        raise ValueError('Expected unlinked regular file: ' + str(path))
    return path.read_bytes()


def required_read(path):
    data = read(path)
    if data is None:
        raise ValueError('Missing required file: ' + str(path))
    return data


def fingerprint(path):
    data = read(path)
    return digest(data) if data is not None else None


def file_mode(path):
    path = guarded(path)
    return stat.S_IMODE(path.stat().st_mode) if path.exists() else None


def private_dir(path):
    path = guarded(path)
    if not path.exists():
        private_dir(path.parent)
        path.mkdir(mode=0o700)
        path.chmod(0o700)
    if not path.is_dir() or path.stat().st_uid != os.getuid() or path.stat().st_mode & 0o077:
        raise ValueError('Private owner-only directory required: ' + str(path))
    return path


def state_dir(home):
    home = guarded(home)
    if not home.is_dir() or home.stat().st_uid != os.getuid():
        raise ValueError('Existing owned profile home required')
    return private_dir(home / 'devteam')


def atomic(path, data, expected, mode=0o600):
    """Recheck before replace; not a lock against an active external writer."""
    path = guarded(path)
    if not path.parent.exists():
        # Only create directories within an already validated profile mapping.
        missing = []
        parent = path.parent
        while not parent.exists():
            missing.append(parent)
            parent = parent.parent
        for directory in reversed(missing):
            guarded(directory).mkdir(mode=0o700)
            directory.chmod(0o700)
    if fingerprint(path) != expected:
        raise ValueError('Concurrent change: ' + str(path))
    fd, temporary = tempfile.mkstemp(prefix='.maker-', dir=path.parent)
    try:
        os.fchmod(fd, mode)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        guarded(path)
        if fingerprint(path) != expected:
            raise ValueError('Concurrent change: ' + str(path))
        os.replace(temporary, path)
        if read(path) != data or stat.S_IMODE(path.stat().st_mode) != mode:
            raise ValueError('Exact readback failed: ' + str(path))
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)  # Only this invocation's temporary file.


def source_mode(repo, commit, source):
    safe_relative(source)
    mode = git(repo, 'ls-tree', commit, '--', source).decode().split(' ', 1)[0]
    if mode not in ('100644', '100755'):
        raise ValueError('Source is missing, symlink or non-regular: ' + source)
    return 0o700 if mode == '100755' else 0o600


def blob(repo, commit, source):
    source_mode(repo, commit, source)
    return git(repo, 'show', commit + ':' + source)


def check_roles(roles, home=None):
    if not isinstance(roles, dict) or not {'planner', 'coder', 'reviewer'} <= set(roles) or set(roles) - {'planner', 'coder', 'reviewer', 'team-codex'}:
        raise ValueError('Expected actual role IDs and homes')
    homes, ids = set(), set()
    for role, item in roles.items():
        if (not isinstance(item, dict) or set(item) != {'id', 'home'}
                or not isinstance(item['id'], str) or not isinstance(item['home'], str)
                or not re.fullmatch(r'[a-z0-9][a-z0-9_-]{0,63}', item['id'])):
            raise ValueError('Invalid role binding: ' + role)
        path = guarded(item['home'])
        if str(path) != item['home'] or not path.is_dir() or path.stat().st_uid != os.getuid():
            raise ValueError('Actual canonical owned home required: ' + role)
        if path in homes or item['id'] in ids:
            raise ValueError('Duplicate role ID/home')
        homes.add(path)
        ids.add(item['id'])
    for role, item in roles.items():
        a = Path(item['home'])
        for other, binding in roles.items():
            b = Path(binding['home'])
            if a in b.parents and (role, other) != ('coder', 'team-codex'):
                raise ValueError('Overlapping role homes')
    # The regular Codex HOME is inside coder/devteam/user-home. Compare
    # managed areas, not the whole homes, before allowing that nesting.
    areas = []
    for role, item in roles.items():
        root = Path(item['home'])
        areas.extend([root / '.agents/skills'] if role == 'team-codex'
                     else [root / 'SOUL.md', root / 'skills'])
    for index, a in enumerate(areas):
        for b in areas[index + 1:]:
            if a == b or a in b.parents or b in a.parents:
                raise ValueError('Managed target areas collide/overlap')
    if home is not None and str(home) != roles['planner']['home']:
        raise ValueError('Planner home mismatch')


def desired(repo, commit, roles, values, souls_only=False):
    check_roles(roles)
    manifest = json.loads(blob(repo, commit, 'manifest.json'))
    result = []
    for role in ROLE_NAMES:
        source = manifest['role_templates'][role]['template_path']
        if source != f'templates/roles/{role}.SOUL.md.template':
            raise ValueError('Unsupported role template mapping')
        template = blob(repo, commit, source).decode()
        fields = role_fields(template, role)
        raw = dict(values, ROLE_NAME=values[ROLE_NAMES[role]])
        content = render_role(template, {key: raw[key] for key in fields}, role).encode()
        result.append({'role': role, 'source': source, 'target': str(Path(roles[role]['home']) / 'SOUL.md'),
                       'transform': 'render-role-v1', 'content': content, 'mode': 0o600})
    if not souls_only:
        for name, skill in manifest['own_skills'].items():
            safe_relative(name)
            if '/' in name or skill['skill_path'] != f'skills/{name}/SKILL.md':
                raise ValueError('Unsupported skill root')
            root = f'skills/{name}/'
            sources = git(repo, 'ls-tree', '-r', '--name-only', commit, '--', root).decode().splitlines()
            if root + 'SKILL.md' not in sources:
                raise ValueError('Skill has no entry point: ' + name)
            for harness, targets in skill['targets'].items():
                for role in targets:
                    if role not in roles or (harness == 'codex' and role != 'team-codex'):
                        raise ValueError('Missing actual skill target home: ' + role)
                    for source in sources:
                        target = Path(roles[role]['home']) / ('.agents' if harness == 'codex' else '') / source
                        result.append({'role': role, 'source': source, 'target': str(target),
                                       'transform': 'copy-v1', 'content': blob(repo, commit, source),
                                       'mode': source_mode(repo, commit, source)})
    targets = [entry['target'] for entry in result]
    if len(targets) != len(set(targets)):
        raise ValueError('Duplicate managed target')
    for entry in result:
        guarded(entry['target'])
    return result


def store_baseline(state, content):
    directory = private_dir(state / 'baselines')
    name = digest(content)
    path = directory / name
    previous = read(path)
    if previous is not None and previous != content:
        raise ValueError('Corrupt baseline')
    if previous is None:
        atomic(path, content, None)
    return name


def setup_data(state):
    path = state / 'setup.md'
    if path.stat().st_mode & 0o077:
        raise ValueError('setup.md must be private (0600)')
    text = required_read(path).decode()
    if text.count('```json\n') != 1:
        raise ValueError('Expected one setup JSON block')
    data = json.loads(text.split('```json\n', 1)[1].split('\n```', 1)[0])
    if (not isinstance(data, dict) or not isinstance(data.get('confirmed_values'), dict)
            or not isinstance(data.get('confirmed_bindings'), dict)):
        raise ValueError('Missing confirmed setup data')
    return data


def initialize(repo, home, team_id, roles=None, legacy=False, base_commit=None, basis_evidence=None):
    if base_commit is not None and (legacy or not re.fullmatch(r'[0-9a-f]{40}', base_commit) or not basis_evidence):
        raise ValueError('Documented full base commit and evidence required; do not combine with legacy safepoint')
    if basis_evidence and base_commit is None:
        raise ValueError('Evidence needs an exact base commit')
    state = state_dir(home)
    if read(state / 'installation.json') is not None:
        raise ValueError('Installation record already exists; do not overwrite')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,119}', team_id):
        raise ValueError('Invalid team ID')
    setup = setup_data(state)
    roles = roles if roles is not None else setup['confirmed_bindings']['roles']
    check_roles(roles, home)
    # The setup record remains the input authority. Do not save secrets here.
    for role in ROLE_NAMES:
        key = role.upper() + '_PROFILE'
        if key in setup['confirmed_values'] and setup['confirmed_values'][key] != roles[role]['id']:
            raise ValueError('Confirmed profile ID differs from actual role binding: ' + role)
    commit = legacy_baseline(repo)['maker_commit'] if legacy else revision(repo, base_commit or 'HEAD')
    version = package_version(repo, commit)
    entries = desired(repo, commit, roles, setup['confirmed_values'], souls_only=legacy)
    for entry in entries:
        actual = read(entry['target'])
        if actual is None or (not legacy and base_commit is None and actual != entry['content']):
            raise ValueError('Initial target does not match verified Maker output: ' + entry['target'])
    record = {'schema': SCHEMA, 'team_id': team_id, 'maker_commit': commit,
              'maker_version': version,
              'roles': roles, **setup, 'legacy_skills_unknown': legacy,
              'historical_installation_verified': not legacy and base_commit is None,
              'basis_evidence': basis_evidence,
              'provenance': ('user-defined-1.0.0-safepoint' if legacy else
                             'documented-setup-baseline' if base_commit else 'verified-initial-file-readback'),
              'managed': []}
    for entry in entries:
        content = entry.pop('content')
        entry.pop('mode')  # Delivery policy is not the installed local mode.
        record['managed'].append(dict(entry, baseline=store_baseline(state, content), installed_hash=fingerprint(entry['target'])))
    atomic(state / 'installation.json', json_bytes(record), None)
    return record


def load_record(home):
    state = state_dir(home)
    path = state / 'installation.json'
    raw = read(path)
    if raw is None or path.stat().st_mode & 0o077:
        raise ValueError('Private installation record required')
    record = json.loads(raw)
    if not isinstance(record, dict):
        raise ValueError('Installation record must be an object')
    if type(record.get('schema')) is not int or record['schema'] != SCHEMA:
        raise ValueError('Unsupported installation schema')
    for key, pattern in (('team_id', r'[A-Za-z0-9][A-Za-z0-9_.-]{0,119}'),
                         ('maker_commit', r'[0-9a-f]{40}'),
                         ('maker_version', r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)')):
        if not isinstance(record.get(key), str) or not re.fullmatch(pattern, record[key]):
            raise ValueError('Invalid installation field: ' + key)
    check_roles(record.get('roles'), home)
    if (not isinstance(record.get('confirmed_values'), dict)
            or not all(isinstance(value, str) for value in record['confirmed_values'].values())
            or not isinstance(record.get('confirmed_bindings'), dict)
            or type(record.get('legacy_skills_unknown')) is not bool):
        raise ValueError('Invalid installation setup data')
    if not isinstance(record.get('managed'), list):
        raise ValueError('Invalid managed inventory: expected array')
    for entry in record['managed']:
        fields = ('role', 'source', 'target', 'transform', 'baseline', 'installed_hash')
        if not isinstance(entry, dict) or not all(isinstance(entry.get(key), str) for key in fields):
            raise ValueError('Invalid managed inventory entry')
        if (entry['role'] not in record['roles'] or entry['transform'] not in ('render-role-v1', 'copy-v1')
                or not re.fullmatch(r'[0-9a-f]{64}', entry['baseline'])
                or not re.fullmatch(r'[0-9a-f]{64}', entry['installed_hash'])):
            raise ValueError('Invalid managed inventory binding/hash')
        safe_relative(entry['source'])
        guarded(entry['target'])
    return state, raw, record


def discover(native_homes):
    """Consume native profile-home output, never infer a home from an ID."""
    if not isinstance(native_homes, list):
        raise ValueError('Native home inventory must be an array')
    results, seen = [], set()
    for item in native_homes:
        try:
            if not isinstance(item, dict) or not isinstance(item.get('home'), str):
                raise ValueError('Native home entry must be an object with a home string')
            home = guarded(item['home'])
        except (ValueError, KeyError, OSError) as error:
            results.append({'home': item.get('home') if isinstance(item, dict) else None,
                            'status': 'failed', 'error': str(error)})
            continue
        marker = home / 'devteam/installation.json'
        if home in seen:
            continue
        seen.add(home)
        if marker.exists() or marker.is_symlink():
            try:
                _, _, record = load_record(home)
                results.append({'home': str(home), 'team_id': record['team_id'], 'maker_commit': record['maker_commit'], 'status': 'recorded'})
            except (ValueError, KeyError, OSError) as error:
                results.append({'home': str(home), 'status': 'failed', 'error': str(error)})
        elif (home / 'devteam/setup.md').exists():
            results.append({'home': str(home), 'status': 'unrecorded', 'action': 'inspect setup role bindings; use explicit user-defined 1.0.0 SOUL safepoint, not verified history'})
    return results


def merge(base, local, new):
    if local is None:
        return None, True
    if local == base or local == new:
        return new, False
    if new == base:
        return local, False
    if base is None:
        return local, True
    if any(b'\0' in data for data in (base, local, new)):
        return local, True
    with tempfile.TemporaryDirectory(prefix='maker-merge-') as directory:
        paths = [Path(directory) / name for name in ('local', 'base', 'new')]
        for path, data in zip(paths, (local, base, new)):
            path.write_bytes(data)
        result = subprocess.run(['git', 'merge-file', '-p', *map(str, paths)], capture_output=True)
    if result.returncode < 0 or result.returncode > 127:
        raise ValueError('git merge-file failed: ' + result.stderr.decode(errors='replace'))
    return result.stdout, result.returncode != 0


def activity(roles):
    """Visible relevant processes are active; invisible activity remains unknown."""
    matches = []
    homes = {item['home'].encode() for item in roles.values()}
    try:
        for process in Path('/proc').iterdir():
            if not process.name.isdigit() or int(process.name) == os.getpid():
                continue
            try:
                env = (process / 'environ').read_bytes().split(b'\0')
                bound = any(field.split(b'=', 1)[-1] in homes for field in env
                            if field.startswith((b'HERMES_HOME=', b'CODEX_HOME=', b'HOME=')))
                if bound:
                    matches.append(int(process.name))
            except (OSError, ProcessLookupError):
                continue
    except OSError:
        pass
    return {'state': 'active' if matches else 'unknown', 'visible_pids': matches,
            'observed_at': datetime.now(timezone.utc).isoformat(),
            'limit': 'No process match does not prove an idle team; dispatcher/session activity may be invisible.'}


def prepare(repo, home, ref='HEAD'):
    state, raw, old = load_record(home)
    commit = revision(repo, ref)
    version = package_version(repo, commit)
    if old['maker_version'] != package_version(repo, old['maker_commit']):
        raise ValueError('Recorded package version mismatch')
    renderer = Path(__file__).with_name('render_text.py').read_bytes()
    if any(blob(repo, rev, 'references/render_text.py') != renderer for rev in (old['maker_commit'], commit)):
        raise ValueError('Changed renderer: withhold rendered files and review transform compatibility before migration')
    old_entries = desired(repo, old['maker_commit'], old['roles'], old['confirmed_values'], old['legacy_skills_unknown'])
    expected = {entry['target']: entry for entry in old_entries}
    stored = {entry['target']: entry for entry in old['managed']}
    if len(stored) != len(old['managed']) or set(stored) != set(expected):
        raise ValueError('Invalid recorded mapping set')
    for target, entry in stored.items():
        origin = expected[target]
        if any(entry[key] != origin[key] for key in ('role', 'source', 'transform')) or entry['baseline'] != digest(origin['content']):
            raise ValueError('Mapping/baseline does not match exact old Maker source: ' + target)
        baseline = read(state / 'baselines' / entry['baseline'])
        if baseline != origin['content']:
            raise ValueError('Missing or corrupt pristine baseline')
    new_entries = desired(repo, commit, old['roles'], old['confirmed_values'], old['legacy_skills_unknown'])
    new_targets = {entry['target'] for entry in new_entries}
    dependencies = []
    for source in OPERATIONAL:
        try:
            if blob(repo, old['maker_commit'], source) != blob(repo, commit, source):
                dependencies.append(source)
        except ValueError:
            dependencies.append(source)
    old_manifest = json.loads(blob(repo, old['maker_commit'], 'manifest.json'))
    new_manifest = json.loads(blob(repo, commit, 'manifest.json'))
    if old_manifest.get('upstream_components') != new_manifest.get('upstream_components'):
        dependencies.append('manifest.json:upstream_components')
    entries, conflicts = [], []
    for entry in new_entries:
        target = entry['target']
        previous = stored.get(target)
        base = read(state / 'baselines' / previous['baseline']) if previous else None
        local = read(target)
        before_mode = file_mode(target)
        if before_mode is not None:
            entry['mode'] = before_mode
        new = entry.pop('content')
        if previous is None:
            merged, conflict = (new, False) if local is None or local == new else (local, True)
        else:
            merged, conflict = merge(base, local, new)
        if conflict:
            conflicts.append(target)
        entries.append(dict(entry, before_hash=digest(local) if local is not None else None, before_mode=before_mode,
                            baseline=digest(new), new_base=encoded(new), merged=encoded(merged or b''), conflict=conflict))
    obsolete = sorted(set(stored) - new_targets)
    proposal = {'schema': SCHEMA, 'team_id': old['team_id'], 'home': str(home), 'repo': str(Path(repo).resolve()),
                'record_hash': digest(raw), 'maker_commit': commit, 'maker_version': version,
                'entries': entries, 'obsolete': obsolete, 'conflicts': conflicts, 'dependencies': dependencies,
                'notices': ['legacy skills: baseline unknown; withheld'] if old['legacy_skills_unknown'] else [],
                'activity': activity(old['roles']), 'semantic_review_required': True}
    directory = private_dir(state / 'proposals')
    path = directory / (uuid.uuid4().hex + '.json')
    atomic(path, json_bytes(proposal), None)
    return path


def require_decision(roles, decision):
    observed = activity(roles)  # Fresh observation immediately before writes.
    if decision not in ('proceed', 'skip'):
        raise ValueError('Team activity ' + observed['state'] + ': warn user and record explicit proceed/skip decision')
    return observed


def apply(home, proposal_path, decision=None, review=None, dependency_review=None):
    state, raw, old = load_record(home)
    path = guarded(proposal_path)
    if path.parent != state / 'proposals':
        raise ValueError('Proposal must belong to this team')
    proposal_raw = required_read(path)
    proposal = json.loads(proposal_raw)
    if proposal['schema'] != SCHEMA or proposal['home'] != str(home) or proposal['team_id'] != old['team_id'] or proposal['record_hash'] != digest(raw):
        raise ValueError('Stale or foreign proposal')
    observed = require_decision(old['roles'], decision)
    if decision == 'skip':
        return {'status': 'skipped', 'team_id': old['team_id'], 'activity': observed}
    if proposal['conflicts'] or any(x['conflict'] for x in proposal['entries']):
        raise ValueError('Text conflicts: obtain concrete agent decision and create a new proposal; do not edit the proposal')
    if not isinstance(review, str) or not review.strip():
        raise ValueError('Agent semantic review of SOULs/skills required; text merge cannot prove semantic compatibility')
    if proposal['dependencies'] and (not isinstance(dependency_review, str) or not dependency_review.strip()):
        raise ValueError('Operational dependency changes: report effect/recommendation, obtain user decision, withhold dependent files')
    # Rebuild from exact Git commits and current files. Never trust proposal target
    # paths or merged bytes as an arbitrary write payload.
    fresh_path = prepare(proposal['repo'], home, proposal['maker_commit'])
    fresh = json.loads(required_read(fresh_path))
    for key in ('entries', 'obsolete', 'dependencies', 'maker_version', 'notices'):
        if fresh[key] != proposal[key]:
            raise ValueError('Proposal/source/target drift; prepare and review again')
    if fingerprint(state / 'installation.json') != proposal['record_hash'] or read(path) != proposal_raw:
        raise ValueError('Metadata/proposal changed during preflight')
    run = private_dir(private_dir(state / 'runs') / uuid.uuid4().hex)
    backup = private_dir(run / 'backup')
    journal = {'schema': SCHEMA, 'status': 'prepared', 'team_id': old['team_id'], 'home': str(home),
               'record_before': encoded(raw), 'record_after': None, 'activity': observed,
               'decision': decision, 'semantic_review': review, 'dependency_review': dependency_review,
               'proposal': str(path), 'files': [], 'retained_obsolete': proposal['obsolete']}
    # Back up all targets before the first target write. Back up metadata too.
    atomic(run / 'installation.before.json', raw, None)
    for index, entry in enumerate(proposal['entries']):
        before = read(entry['target'])
        if ((digest(before) if before is not None else None) != entry['before_hash']
                or file_mode(entry['target']) != entry['before_mode']):
            raise ValueError('Target changed during backup: ' + entry['target'])
        if before is not None:
            atomic(backup / str(index), before, None)
        journal['files'].append({'target': entry['target'], 'before_hash': entry['before_hash'],
                                 'after_hash': digest(decoded(entry['merged'])), 'backup': str(index),
                                 'mode': entry['before_mode'], 'after_mode': entry['mode']})
    atomic(run / 'result.json', json_bytes(journal), None)
    try:
        observed = require_decision(old['roles'], decision)
        journal['activity_before_write'] = observed
        if fingerprint(state / 'installation.json') != proposal['record_hash']:
            raise ValueError('Installation changed before write')
        for entry in proposal['entries']:
            if fingerprint(entry['target']) != entry['before_hash'] or file_mode(entry['target']) != entry['before_mode']:
                raise ValueError('Target changed before write: ' + entry['target'])
        managed = []
        for entry in proposal['entries']:
            merged, new = decoded(entry['merged']), decoded(entry['new_base'])
            if digest(new) != entry['baseline']:
                raise ValueError('New baseline checksum mismatch')
            if digest(merged) != entry['before_hash']:
                atomic(entry['target'], merged, entry['before_hash'], entry['mode'])
            baseline = store_baseline(state, new)
            managed.append({key: entry[key] for key in ('role', 'source', 'target', 'transform')} |
                           {'baseline': baseline, 'installed_hash': digest(merged)})
        for entry in proposal['entries']:
            if fingerprint(entry['target']) != digest(decoded(entry['merged'])) or file_mode(entry['target']) != entry['mode']:
                raise ValueError('Final target readback mismatch: ' + entry['target'])
        updated = dict(old, maker_commit=proposal['maker_commit'], maker_version=proposal['maker_version'],
                       managed=managed, last_run=str(run), retained_obsolete=proposal['obsolete'])
        updated_raw = json_bytes(updated)
        journal['record_after'] = encoded(updated_raw)
        # Persist recovery information before the metadata commit point.
        atomic(run / 'result.json', json_bytes(journal), fingerprint(run / 'result.json'))
        atomic(state / 'installation.json', updated_raw, proposal['record_hash'])
        journal['status'] = 'applied'
        atomic(run / 'result.json', json_bytes(journal), fingerprint(run / 'result.json'))
    except Exception as error:
        journal['status'] = 'failed'
        journal['error'] = str(error)
        # If the metadata replace occurred but verification failed, restore only
        # our exact candidate, never overwrite another writer's record.
        current = read(state / 'installation.json')
        if journal['record_after'] is not None and current == decoded(journal['record_after']):
            atomic(state / 'installation.json', raw, digest(current))
        try:
            atomic(run / 'result.json', json_bytes(journal), fingerprint(run / 'result.json'))
        except OSError as receipt_error:
            error.add_note('Could not persist failure receipt: ' + str(receipt_error))
        error.args = (str(error) + '; recovery run: ' + str(run),)
        raise
    return {'status': 'applied', 'team_id': old['team_id'], 'run': str(run),
            'retained_obsolete': proposal['obsolete'], 'notices': proposal['notices']}


def rollback(home, run, decision=None):
    state, current_raw, current = load_record(home)
    run = guarded(run)
    if run.parent != state / 'runs':
        raise ValueError('Rollback run must belong to this team')
    journal = json.loads(required_read(run / 'result.json'))
    if journal['home'] != str(home) or journal['team_id'] != current['team_id'] or journal['status'] not in ('applied', 'failed', 'prepared'):
        raise ValueError('Invalid rollback journal')
    before = decoded(journal['record_before'])
    after = decoded(journal['record_after']) if journal['record_after'] else None
    if current_raw not in (before, after):
        raise ValueError('Installation changed since this run')
    observed = require_decision(current['roles'], decision)
    if decision == 'skip':
        return {'status': 'skipped', 'team_id': current['team_id']}
    # Validate journal targets against the immutable proposal, not arbitrary paths.
    proposal = json.loads(required_read(guarded(journal['proposal'])))
    allowed = {entry['target']: entry for entry in proposal['entries']}
    if len(allowed) != len(journal['files']) or {entry['target'] for entry in journal['files']} != set(allowed):
        raise ValueError('Rollback mapping mismatch')
    retained = []
    for entry in journal['files']:
        target = entry['target']
        role = allowed[target]['role']
        root = Path(current['roles'][role]['home'])
        relative = Path(target).relative_to(root).as_posix()
        safe_relative(relative)
        allowed_root = '.agents/skills/' if role == 'team-codex' else 'skills/'
        if not (relative == 'SOUL.md' and role != 'team-codex') and not relative.startswith(allowed_root):
            raise ValueError('Invalid rollback target')
        safe_relative(entry['backup'])
        actual = fingerprint(target)
        if (actual, file_mode(target)) not in ((entry['before_hash'], entry['mode'] if entry['before_hash'] is not None else None),
                                             (entry['after_hash'], entry.get('after_mode', entry['mode']))):
            raise ValueError('Target changed since update: ' + target)
        if entry['before_hash'] is not None and fingerprint(run / 'backup' / entry['backup']) != entry['before_hash']:
            raise ValueError('Corrupt rollback backup')
    if read(state / 'installation.json') != current_raw:
        raise ValueError('Installation changed during rollback preflight')
    require_decision(current['roles'], decision)
    for entry in journal['files']:
        target = entry['target']
        actual = fingerprint(target)
        if (actual, file_mode(target)) not in ((entry['before_hash'], entry['mode'] if entry['before_hash'] is not None else None),
                                             (entry['after_hash'], entry.get('after_mode', entry['mode']))):
            raise ValueError('Target changed before rollback: ' + target)
        if entry['before_hash'] is None:
            if actual is not None:
                retained.append(target)  # Do not delete additions without separate approval.
        elif actual != entry['before_hash'] or file_mode(target) != entry['mode']:
            atomic(target, read(run / 'backup' / entry['backup']), actual, entry['mode'])
        if entry['before_hash'] is not None and (fingerprint(target) != entry['before_hash'] or file_mode(target) != entry['mode']):
            raise ValueError('Rollback readback failed: ' + target)
    atomic(state / 'installation.json', before, digest(current_raw))
    result = {'status': 'rolled-back', 'team_id': current['team_id'], 'retained_additions': retained, 'activity': observed}
    atomic(run / 'rollback.json', json_bytes(result), None)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('legacy-baseline')
    discovery = commands.add_parser('discover')
    discovery.add_argument('--homes', type=Path, required=True, help='JSON array of native {id, home} results')
    init = commands.add_parser('init')
    init.add_argument('--home', type=Path, required=True)
    init.add_argument('--team-id', required=True)
    init.add_argument('--roles', type=Path, help='Verified role/home JSON; default: setup confirmed_bindings.roles')
    init.add_argument('--legacy-souls', action='store_true')
    init.add_argument('--base-commit', help='Exact documented 40-character setup revision; all managed files need evidence')
    init.add_argument('--basis-evidence', help='Nonsecret provenance for the exact old baseline and mapping coverage')
    plan = commands.add_parser('plan')
    plan.add_argument('--home', type=Path, required=True)
    plan.add_argument('--target', default='HEAD')
    for name, option in [('apply', '--proposal'), ('rollback', '--run')]:
        command = commands.add_parser(name)
        command.add_argument('--home', type=Path, required=True)
        command.add_argument(option, type=Path, required=True)
        command.add_argument('--activity-decision', choices=['proceed', 'skip'])
        if name == 'apply':
            command.add_argument('--semantic-review', help='Agent finding after reading all changed SOULs/skills')
            command.add_argument('--dependency-decision', help='User decision with scope/effect; never authorization to change runtime')
    args = parser.parse_args()
    try:
        if args.command == 'legacy-baseline':
            output = legacy_baseline(args.repo)
        elif args.command == 'discover':
            output = discover(json.loads(required_read(args.homes)))
            for item in output:
                if item['status'] == 'unrecorded':
                    item['legacy_baseline'] = legacy_baseline(args.repo)
        elif args.command == 'init':
            output = initialize(args.repo, args.home, args.team_id,
                                json.loads(required_read(args.roles)) if args.roles else None, args.legacy_souls,
                                args.base_commit, args.basis_evidence)
        elif args.command == 'plan':
            path = prepare(args.repo, args.home, args.target)
            output = {'proposal': str(path), **json.loads(required_read(path))}
        elif args.command == 'apply':
            output = apply(args.home, args.proposal, args.activity_decision, args.semantic_review, args.dependency_decision)
        else:
            output = rollback(args.home, args.run, args.activity_decision)
        print(json.dumps(output, ensure_ascii=True, indent=2))
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, 'Updater stopped: ' + str(error) + '\n')


if __name__ == '__main__':
    main()
