"""Isolated updater contracts. No live Hermes calls or profile writes."""
from typing import Any
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import update_team as u


class UpdaterTests(unittest.TestCase):
    def setUp(self):
        # The fixture uses real local files and a real Git repository.
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / 'maker'
        self.repo.mkdir()
        original = Path(__file__).resolve().parents[1]
        for name in ['templates', 'skills', 'references']:
            shutil.copytree(original / name, self.repo / name, ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy(original / 'manifest.json', self.repo)
        shutil.copy(original / 'SKILL.md', self.repo)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.commit('fixture baseline')
        self.base = self.git('rev-parse', 'HEAD').strip()
        self.roles = {}
        for role in ['planner', 'coder', 'reviewer', 'team-codex']:
            home = (self.root / 'coder/devteam/user-home' if role == 'team-codex'
                    else self.root / role)
            home.mkdir(mode=0o700, parents=True)
            self.roles[role] = {'id': 'fixture-' + role, 'home': str(home)}
        self.home = Path(self.roles['planner']['home'])
        self.state = self.home / 'devteam'
        self.state.mkdir(mode=0o700)
        values = {key: 'medium' if 'REASONING' in key else 'sample' for key in [
            'PLANER_NAME', 'CODER_NAME', 'REVIEWER_NAME', 'PROJECT_NAME',
            'HINDSIGHT_BANK_NAME', 'KANBAN_BOARD_NAME', 'CODER_PROFILE', 'REVIEWER_PROFILE',
            'CODEX_REASONING_DEFAULT', 'CODEX_REASONING_MAX', 'ROLE_REASONING_DEFAULT', 'ROLE_REASONING_HIGH']}
        values['PLANNER_PROFILE'] = self.roles['planner']['id']
        values['PROJECT_DIR'] = "/synthetic/client's workspace"
        values['REPOSITORY_ROOTS'] = "Planning: /synthetic/plans; implementation: /synthetic/client's workspace/code"
        values['CODER_PROFILE'] = self.roles['coder']['id']
        values['REVIEWER_PROFILE'] = self.roles['reviewer']['id']
        values['CODEX_BINARY'] = '/synthetic/bin/codex'
        values['CODEX_PROCESS_HOME'] = self.roles['team-codex']['home']
        values['CODEX_HOME'] = str(Path(self.roles['coder']['home']) / 'devteam/codex-home')
        # Synthetic demonstration password; never a real credential.
        values['DEMO_PASSWORD'] = 'Synthetic-Demo-Passphrase-9'
        self.bindings = {'board': 'sample', 'roles': self.roles, 'triage_recovery': {
            'python': '/synthetic/python',
            'script': str(self.home / 'skills/brownfield-feature-planning/scripts/recover_triage.py'),
            'db': str(self.root / "board with 'quotes'.db"),
            'planner_profile': self.roles['planner']['id']}}
        record = {'confirmed_values': values, 'confirmed_bindings': self.bindings}
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(record) + '\n```\n')
        (self.state / 'setup.md').chmod(0o600)
        for entry in u.desired(self.repo, self.base, self.roles, values, bindings=self.bindings):
            path = Path(entry['target'])
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(entry['content'])
            path.chmod(entry['mode'])

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], text=True)

    def commit(self, message):
        self.git('add', '.')
        self.git('commit', '-qm', message)

    def initialize(self, legacy=False):
        return u.initialize(self.repo, self.home, 'fixture-team', self.roles, legacy=legacy)

    def change(self, relative='skills/brownfield-feature-planning/SKILL.md', text='\nNew upstream instruction.\n'):
        path = self.repo / relative
        path.write_text(path.read_text() + text)
        self.commit('new upstream')

    def proposal(self):
        return u.prepare(self.repo, self.home, 'HEAD')

    def test_keep_plan_apply_and_followup(self):
        self.initialize()
        targets = [self.home / 'skills/brownfield-feature-planning/SKILL.md', self.home / 'SOUL.md']
        self.change()
        local = {}
        for target in targets:
            local[str(target)] = target.read_bytes() + b'\nLocal team rule.\n'
            target.write_bytes(local[str(target)])

        def cli(*args):
            result = subprocess.run([sys.executable, '-B', u.__file__, '--repo', str(self.repo), *args],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)

        first = cli('plan', '--home', str(self.home))
        self.assertEqual(first.get('keep'), [])
        self.assertEqual({a['path'] for a in first['adaptations']}, set(local))
        second = cli('plan', '--home', str(self.home), '--keep', str(targets[0]), '--keep', str(targets[1]))
        self.assertNotEqual(first['proposal'], second['proposal'])
        proposal = json.loads(Path(second['proposal']).read_text())
        self.assertEqual(proposal['keep'], sorted(local))
        pristine = {}
        for entry in proposal['entries']:
            if entry['target'] in local:
                self.assertEqual(u.decoded(entry['merged']), local[entry['target']])
                pristine[entry['target']] = u.decoded(entry['new_base'])
        inodes = {p: Path(p).stat().st_ino for p in local}
        result = cli('apply', '--home', str(self.home), '--proposal', second['proposal'],
                     '--activity-decision', 'proceed', '--semantic-review', 'Keep both local rules')
        journal = json.loads((Path(result['run']) / 'result.json').read_text())
        self.assertEqual({f['target'] for f in journal['files'] if f['kept']}, set(local))
        _, _, record = u.load_record(self.home)
        self.assertNotIn('keep', record)
        for entry in record['managed']:
            p = entry['target']
            if p in local:
                self.assertEqual((Path(p).read_bytes(), Path(p).stat().st_ino), (local[p], inodes[p]))
                self.assertEqual(entry['installed_hash'], u.digest(pristine[p]))
                self.assertEqual((self.state / 'baselines' / entry['baseline']).read_bytes(), pristine[p])
        following = cli('plan', '--home', str(self.home))
        self.assertEqual(following['keep'], [])
        self.assertEqual({a['path'] for a in following['adaptations']}, set(local))

    def test_keep_rejects_unmodified_target(self):
        self.initialize()
        with self.assertRaisesRegex(ValueError, 'adaptation'):
            u.prepare(self.repo, self.home, keep=[str(self.home / 'SOUL.md')])

    def test_apply_rejects_settings_type_drift(self):
        self.initialize()
        path = self.proposal()
        proposal = json.loads(path.read_text())
        proposal['settings']['planner']['kanban.auto_subscribe_on_create'] = 0
        path.write_text(json.dumps(proposal))
        with self.assertRaisesRegex(ValueError, 'drift'):
            u.apply(self.home, path, decision='proceed', review='checked')

    def test_settings_required_only_in_target_manifest(self):
        path = self.repo / 'manifest.json'
        manifest = json.loads(path.read_text())
        manifest.pop('settings', None)
        path.write_text(json.dumps(manifest))
        self.commit('old manifest without settings')
        self.initialize()
        with self.assertRaisesRegex(ValueError, 'settings'):
            self.proposal()
        manifest['settings'] = {'planner': {'kanban.auto_subscribe_on_create': False}}
        path.write_text(json.dumps(manifest))
        self.commit('target settings')
        self.assertEqual(json.loads(self.proposal().read_text())['settings'], manifest['settings'])

    def deassigned_reviewer_skill(self, name='screenshot-to-code'):
        """Install one Maker skill into the Reviewer home, then deassign it."""
        manifest_path = self.repo / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        manifest['own_skills'][name]['targets']['hermes'].append('reviewer')
        manifest_path.write_text(json.dumps(manifest))
        self.commit('fixture old reviewer equipment')
        setup = u.setup_data(self.state)
        installed = {}
        for entry in u.desired(self.repo, 'HEAD', self.roles, setup['confirmed_values'], bindings=self.bindings):
            if entry['role'] == 'reviewer' and entry['source'].startswith('skills/' + name + '/'):
                target = Path(entry['target'])
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(entry['content'])
                target.chmod(entry['mode'])
                installed[str(target)] = target.read_bytes()
        self.assertTrue(installed)
        self.initialize()
        manifest['own_skills'][name]['targets']['hermes'].remove('reviewer')
        manifest_path.write_text(json.dumps(manifest))
        self.commit('fixture deassign reviewer skill')
        return installed

    def test_setup_scalars_survive_initialize_discovery_and_update(self):
        setup = u.setup_data(self.state)
        scalars = {'CREATE_BANK': True, 'CREATE_BOARD': False, 'WATCHER': True,
                   'OPTIONAL_VALUE': None, 'INTEGER_VALUE': 7, 'NUMBER_VALUE': 1.5,
                   'STRING_VALUE': 'confirmed'}
        setup['confirmed_values'].update(scalars)
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(setup) + '\n```\n')
        self.initialize()
        _, _, record = u.load_record(self.home)
        for key, value in scalars.items():
            with self.subTest(key=key):
                self.assertEqual(record['confirmed_values'][key], value)
                self.assertIs(type(record['confirmed_values'][key]), type(value))
        self.assertEqual(u.discover([{'home': str(self.home)}])[0]['status'], 'recorded')
        self.change()
        result = u.apply(self.home, self.proposal(), decision='proceed', review='checked scalar preservation')
        self.assertEqual(result['status'], 'applied')
        _, _, updated = u.load_record(self.home)
        self.assertEqual(updated['confirmed_values'], setup['confirmed_values'])
        for key, value in scalars.items():
            self.assertIs(type(updated['confirmed_values'][key]), type(value))

    def test_setup_values_reject_structures_and_non_json_numbers(self):
        record = self.initialize()
        marker = self.state / 'installation.json'
        for value in ([], {}, ['nested'], {'nested': True}, float('nan'), float('inf'), -float('inf')):
            with self.subTest(value=value):
                values = dict(record['confirmed_values'], INVALID=value)
                marker.write_text(json.dumps(dict(record, confirmed_values=values)))
                with self.assertRaisesRegex(ValueError, 'Invalid installation setup data'):
                    u.load_record(self.home)
                self.assertEqual(u.discover([{'home': str(self.home)}])[0]['status'], 'failed')

    def test_setup_record_template_preserves_update_round_trip(self):
        import bind_recovery as b

        setup = u.setup_data(self.state)
        setup['confirmed_values'].update(CODEX_MODEL='native-model-id',
                                         PLANNER_REASONING='high', CODER_REASONING='medium')
        template = (self.repo / 'templates/setup-record.md').read_text()
        self.assertEqual(template.count('```json\n'), 1)
        head, block = template.split('```json\n', 1)
        _, tail = block.split('\n```', 1)
        setup_path = self.state / 'setup.md'
        setup_path.write_text(head + '```json\n' + json.dumps(setup, ensure_ascii=True, indent=2) + '\n```' + tail)
        setup_path.chmod(0o600)
        self.assertEqual(u.setup_data(self.state), setup)
        launcher = b.install(self.home)
        self.assertEqual(launcher, self.home / b.SOURCE)
        self.assertEqual(launcher.read_bytes(), b.render_launcher(
            (self.repo / b.SOURCE).read_bytes(), self.bindings['triage_recovery'], self.roles))
        self.assertEqual(u.file_mode(launcher), 0o700)

        record = u.initialize(self.repo, self.home, 'fixture-team')
        self.assertEqual(record['maker_version'], u.package_version(self.repo, self.base))
        self.assertEqual(record['maker_commit'], self.base)
        self.assertEqual(record['roles'], self.roles)
        self.assertEqual(record['confirmed_values'], setup['confirmed_values'])
        self.assertEqual(record['confirmed_bindings'], setup['confirmed_bindings'])
        self.assertEqual(record['provenance'], 'verified-initial-file-readback')
        self.assertTrue(record['historical_installation_verified'])
        expected = u.desired(self.repo, self.base, self.roles, setup['confirmed_values'], bindings=self.bindings)
        self.assertEqual(record['managed'], [
            {key: entry[key] for key in ('role', 'source', 'target', 'transform')} |
            {'baseline': u.digest(entry['content']), 'installed_hash': u.digest(entry['content'])}
            for entry in expected])
        process_home = Path(self.roles['team-codex']['home'])
        self.assertEqual(process_home, Path(self.roles['coder']['home']) / 'devteam/user-home')
        codex_entries = [entry for entry in expected if entry['role'] == 'team-codex']
        self.assertTrue(codex_entries)
        for entry in codex_entries:
            self.assertTrue(Path(entry['target']).is_relative_to(process_home / '.agents/skills'))
        for entry in expected:
            self.assertEqual((self.state / 'baselines' / u.digest(entry['content'])).read_bytes(), entry['content'])

        marker = self.state / 'installation.json'
        before_metadata = marker.read_bytes()
        target = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        target.write_bytes(b'Local heading\n' + target.read_bytes())
        target.chmod(0o640)
        before_targets = {entry['target']: (Path(entry['target']).read_bytes(), u.file_mode(entry['target']))
                          for entry in expected}
        self.change()
        plan = self.proposal()
        proposal = json.loads(plan.read_text())
        self.assertFalse(proposal['conflicts'])
        self.assertIn(str(target), {item['path'] for item in proposal['adaptations']})
        self.assertEqual(marker.read_bytes(), before_metadata)
        result = u.apply(self.home, plan, decision='proceed', review='Checked template record round trip',
                         dependency_review='Reviewed operational changes; no runtime migration authorized')
        self.assertEqual(result['status'], 'applied')
        updated = json.loads(marker.read_text())
        self.assertEqual(updated['maker_commit'], self.git('rev-parse', 'HEAD').strip())
        self.assertEqual(updated['maker_version'], proposal['maker_version'])
        self.assertEqual(updated['roles'], self.roles)
        self.assertEqual(updated['confirmed_values'], setup['confirmed_values'])
        self.assertEqual(updated['confirmed_bindings'], setup['confirmed_bindings'])
        self.assertEqual(updated['last_run'], result['run'])
        for entry in proposal['entries']:
            self.assertEqual(Path(entry['target']).read_bytes(), u.decoded(entry['merged']))
            self.assertEqual(u.file_mode(entry['target']), entry['mode'])
        new_expected = u.desired(self.repo, updated['maker_commit'], self.roles,
                                 setup['confirmed_values'], bindings=self.bindings)
        for entry in new_expected:
            managed = next(item for item in updated['managed'] if item['target'] == entry['target'])
            self.assertEqual({key: managed[key] for key in ('role', 'source', 'target', 'transform')},
                             {key: entry[key] for key in ('role', 'source', 'target', 'transform')})
            self.assertEqual(managed['installed_hash'], u.digest(Path(entry['target']).read_bytes()))
            self.assertEqual(managed['baseline'], u.digest(entry['content']))
            self.assertEqual((self.state / 'baselines' / managed['baseline']).read_bytes(), entry['content'])
        new_file = next(entry for entry in new_expected
                        if entry['source'] == 'skills/brownfield-feature-planning/SKILL.md')
        self.assertEqual(target.read_bytes(), new_file['content'])
        self.assertFalse(target.read_text().startswith('Local heading'))
        self.assertEqual(json.loads((Path(result['run']) / 'result.json').read_text())['status'], 'applied')
        self.assertEqual(u.rollback(self.home, Path(result['run']), decision='proceed')['status'], 'rolled-back')
        self.assertEqual(marker.read_bytes(), before_metadata)
        for path, (content, mode) in before_targets.items():
            self.assertEqual(Path(path).read_bytes(), content)
            self.assertEqual(u.file_mode(path), mode)
        self.assertEqual(u.setup_data(self.state), setup)
        self.assertFalse(self.state.is_relative_to(self.repo))
        for path in [self.state, *self.state.rglob('*')]:
            self.assertEqual(u.file_mode(path), 0o700 if path.is_dir() else 0o600, str(path))

    def historical_installation(self, commit, legacy=False):
        original = Path(__file__).resolve().parents[1]
        self.git('fetch', '-q', str(original), commit)
        setup_path = self.state / 'setup.md'
        setup = u.setup_data(self.state)
        old_values = {key: value for key, value in setup['confirmed_values'].items()
                      if key not in ('PROJECT_DIR', 'REPOSITORY_ROOTS', 'PLANNER_PROFILE',
                                     'CODEX_BINARY', 'CODEX_PROCESS_HOME', 'CODEX_HOME')}
        setup_path.write_text('```json\n' + json.dumps(dict(setup, confirmed_values=old_values)) + '\n```\n')
        historical_renderer = {}
        exec(u.blob(self.repo, commit, 'references/render_text.py'), historical_renderer)
        for entry in u.desired(self.repo, commit, self.roles, old_values, souls_only=legacy, bindings=self.bindings):
            content = entry['content']
            if entry['transform'] == 'render-role-v1':
                role = entry['role']
                template = u.blob(self.repo, commit, entry['source']).decode()
                fields = historical_renderer['role_fields'](template, role)
                raw = dict(old_values, ROLE_NAME=old_values[u.ROLE_NAMES[role]])
                content = historical_renderer['render_role'](template, {key: raw[key] for key in fields}, role).encode()
                self.assertEqual(entry['content'], content, 'Current renderer must reproduce exact historical output')
            target = Path(entry['target'])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        if legacy:
            self.initialize(legacy=True)
        else:
            u.initialize(self.repo, self.home, 'fixture-team', self.roles, base_commit=commit,
                         basis_evidence='Synthetic exact source installation')
        return setup

    def check_historical_binding_upgrade(self, commit, legacy=False):
        setup = self.historical_installation(commit, legacy)
        # Existing confirmed evidence is supplied by the operator, not the role.
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(setup) + '\n```\n')
        target = self.home / 'SOUL.md'
        target.write_text('Local team note\n' + target.read_text())
        plan = self.proposal()
        self.assertFalse(json.loads(plan.read_text())['conflicts'])
        result = u.apply(self.home, plan, decision='proceed', review='Checked bindings and local note',
                         dependency_review='Approved file-only migration')
        self.assertEqual(result['status'], 'applied')
        self.assertFalse(target.read_text().startswith('Local team note\n'))
        self.assertIn(str(target), {item['path'] for item in json.loads(plan.read_text())['adaptations']})
        self.assertIn("`/synthetic/client's workspace`", target.read_text())
        self.assertIn("`Planning: /synthetic/plans; implementation: /synthetic/client's workspace/code`", target.read_text())
        coder = (Path(self.roles['coder']['home']) / 'SOUL.md').read_text()
        self.assertIn('kanban_block(kind="needs_input", reason=...)', coder)
        self.assertIn('keep card and assignment', coder)
        self.assertIn('confirm the existing subscription wakes `fixture-planner`', coder)
        self.assertIn('one TIMER request to fixture-planner through `kanban_create`', coder)
        record = json.loads((self.state / 'installation.json').read_text())
        self.assertEqual(record['confirmed_values']['PROJECT_DIR'], setup['confirmed_values']['PROJECT_DIR'])
        self.assertEqual(record['confirmed_values']['REPOSITORY_ROOTS'], setup['confirmed_values']['REPOSITORY_ROOTS'])
        self.assertEqual(record['confirmed_values']['PLANNER_PROFILE'], 'fixture-planner')
        (self.state / 'setup.md').rename(self.state / 'audit-only.md')
        self.assertFalse(json.loads(self.proposal().read_text())['conflicts'])

    def test_pre290_installation_adopts_confirmed_codex_paths(self):
        original = Path(__file__).resolve().parents[1]
        commit = 'f0040ce5c748c4aa83d94c77c0be2af928a83a0a'
        self.git('fetch', '-q', str(original), commit)
        setup = u.setup_data(self.state)
        paths = {key: setup['confirmed_values'][key]
                 for key in ('CODEX_BINARY', 'CODEX_PROCESS_HOME', 'CODEX_HOME')}
        old = dict(setup, confirmed_values={key: value for key, value in setup['confirmed_values'].items()
                                          if key not in paths})
        setup_path = self.state / 'setup.md'
        setup_path.write_text('```json\n' + json.dumps(old) + '\n```\n')
        for entry in u.desired(self.repo, commit, self.roles, old['confirmed_values'], bindings=self.bindings):
            target = Path(entry['target'])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(entry['content'])
        u.initialize(self.repo, self.home, 'fixture-team', self.roles, base_commit=commit,
                     basis_evidence='Exact synthetic 2.8.18 installation')
        before = (self.state / 'installation.json').read_bytes()
        coder = Path(self.roles['coder']['home']) / 'SOUL.md'
        before_coder = coder.read_bytes()
        with self.assertRaisesRegex(ValueError, 'Missing confirmed role bindings'):
            self.proposal()
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)
        self.assertEqual(coder.read_bytes(), before_coder)
        setup_path.write_text('```json\n' + json.dumps(setup) + '\n```\n')
        coder.write_text('Local retained rule.\n' + coder.read_text())
        plan = self.proposal()
        result = u.apply(self.home, plan, decision='proceed',
                         review='Checked bound invocation and replaced local rule',
                         dependency_review='Confirmed Codex paths; file-only fixture update')
        self.assertEqual(result['status'], 'applied')
        self.assertFalse(coder.read_text().startswith('Local retained rule.\n'))
        self.assertIn(str(coder), {item['path'] for item in json.loads(plan.read_text())['adaptations']})
        self.assertIn(paths['CODEX_HOME'] + '/config.toml', coder.read_text())
        self.assertIn('Check `ok: true` and `status: \"review\"`', coder.read_text())
        record = u.load_record(self.home)[2]
        for key, value in paths.items():
            self.assertEqual(record['confirmed_values'][key], value)
        setup_path.rename(self.state / 'audit-only.md')
        proposal = json.loads(self.proposal().read_text())
        self.assertFalse(proposal['conflicts'])
        for entry in proposal['entries']:
            self.assertEqual(u.digest(u.decoded(entry['merged'])), entry['before_hash'])

    def test_codex_process_home_conflict_is_rejected(self):
        values = dict(u.setup_data(self.state)['confirmed_values'], CODEX_PROCESS_HOME='/other/home')
        with self.assertRaisesRegex(ValueError, 'Codex process HOME differs'):
            u.desired(self.repo, self.base, self.roles, values, bindings=self.bindings)

    def test_fresh_team_renders_demonstration_password_only_into_the_three_souls(self):
        record = self.initialize()
        self.assertEqual(record['confirmed_values']['DEMO_PASSWORD'], 'Synthetic-Demo-Passphrase-9')
        for role in ('planner', 'coder', 'reviewer'):
            with self.subTest(role=role):
                text = (Path(self.roles[role]['home']) / 'SOUL.md').read_text()
                self.assertEqual(text.count('`Synthetic-Demo-Passphrase-9`'), 1)
                self.assertNotIn('{{DEMO_PASSWORD}}', text)
        for entry in record['managed']:
            if entry['source'].startswith('skills/'):
                with self.subTest(source=entry['source'], role=entry['role']):
                    self.assertNotIn(b'Synthetic-Demo-Passphrase-9', Path(entry['target']).read_bytes())

    def test_missing_or_unsafe_demonstration_password_blocks_fresh_role_output(self):
        setup = u.setup_data(self.state)
        path = self.state / 'setup.md'
        absent = dict(setup['confirmed_values'])
        absent.pop('DEMO_PASSWORD')
        path.write_text('```json\n' + json.dumps(dict(setup, confirmed_values=absent)) + '\n```\n')
        with self.assertRaisesRegex(ValueError, 'DEMO_PASSWORD'):
            u.initialize(self.repo, self.home, 'fresh-team', self.roles)
        for value in ('', '   ', 'two\nlines', 'tick`value', 'back\\slash', 'tilde~value', '{{DEMO_PASSWORD}}'):
            values = dict(setup['confirmed_values'], DEMO_PASSWORD=value)
            path.write_text('```json\n' + json.dumps(dict(setup, confirmed_values=values)) + '\n```\n')
            with self.subTest(value=value), self.assertRaises(ValueError):
                u.initialize(self.repo, self.home, 'fresh-team', self.roles)
            self.assertFalse((self.state / 'installation.json').exists())

    def pre2140_installation(self):
        """Exact 2.13.1 source fixture: the last Maker without DEMO_PASSWORD."""
        original = Path(__file__).resolve().parents[1]
        commit = '675e05180b4277d78206d63beb2ff71cee2f4f73'
        self.git('fetch', '-q', str(original), commit)
        self.assertEqual(u.package_version(self.repo, commit), '2.13.1')
        setup = u.setup_data(self.state)
        old = dict(setup, confirmed_values={key: value for key, value in setup['confirmed_values'].items()
                                            if key != 'DEMO_PASSWORD'})
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(old) + '\n```\n')
        for entry in u.desired(self.repo, commit, self.roles, old['confirmed_values'], bindings=self.bindings):
            target = Path(entry['target'])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(entry['content'])
            target.chmod(entry['mode'])
        return u.initialize(self.repo, self.home, 'fixture-team', self.roles, base_commit=commit,
                            basis_evidence='Synthetic exact 2.13.1 installation without DEMO_PASSWORD')

    def test_pre2140_team_adopts_demonstration_password_only_after_verified_apply(self):
        self.pre2140_installation()
        marker = self.state / 'installation.json'
        before_marker = marker.read_bytes()
        coder = Path(self.roles['coder']['home']) / 'SOUL.md'
        before_coder = coder.read_bytes()
        with self.assertRaisesRegex(ValueError, 'DEMO_PASSWORD'):
            self.proposal()
        self.assertEqual(marker.read_bytes(), before_marker)
        self.assertEqual(coder.read_bytes(), before_coder)

        setup = u.setup_data(self.state)
        setup['confirmed_values']['DEMO_PASSWORD'] = 'Synthetic-Pre214-Pass-1'
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(setup) + '\n```\n')
        plan = self.proposal()
        proposal = json.loads(plan.read_text())
        self.assertFalse(proposal['conflicts'])
        # Adoption is not persisted before the verified target write.
        self.assertNotIn('DEMO_PASSWORD', json.loads(marker.read_text())['confirmed_values'])
        self.assertNotIn(b'Synthetic-Pre214-Pass-1', coder.read_bytes())

        result = u.apply(self.home, plan, decision='proceed',
                         review='Checked demo lifecycle, teardown verb and literal password in all three SOULs',
                         dependency_review='Reviewed operational recipe change; file-only fixture update')
        self.assertEqual(result['status'], 'applied')
        record = u.load_record(self.home)[2]
        self.assertEqual(record['confirmed_values']['DEMO_PASSWORD'], 'Synthetic-Pre214-Pass-1')
        for role in ('planner', 'coder', 'reviewer'):
            with self.subTest(role=role):
                text = (Path(self.roles[role]['home']) / 'SOUL.md').read_text()
                self.assertEqual(text.count('`Synthetic-Pre214-Pass-1`'), 1)
        self.assertIn('a demonstration runtime is not permanent',
                      (Path(self.roles['reviewer']['home']) / 'SOUL.md').read_text())
        self.assertNotIn('a demonstration runtime is not permanent', coder.read_text())
        handover = Path(self.roles['coder']['home']) / 'skills' / 'demo-handover' / 'SKILL.md'
        self.assertTrue(handover.is_file(), handover)
        self.assertEqual(handover.read_bytes(),
                         (Path(__file__).resolve().parents[1] / 'skills/demo-handover/SKILL.md').read_bytes())
        self.assertIn('`demo.sh retire`', handover.read_text())
        self.assertIn('`demo.sh user`', handover.read_text())
        self.assertNotIn('demo.sh retire', coder.read_text())
        self.assertIn('read the `demo-handover` skill', coder.read_text())
        self.assertIn('recorded login works on the running system',
                      (Path(self.roles['reviewer']['home']) / 'SOUL.md').read_text())

        # A later update reuses the recorded value without reading setup.md again.
        (self.state / 'setup.md').rename(self.state / 'audit-only.md')
        later = json.loads(self.proposal().read_text())
        self.assertFalse(later['conflicts'])
        self.assertEqual(later['confirmed_values']['DEMO_PASSWORD'], 'Synthetic-Pre214-Pass-1')
        for entry in later['entries']:
            self.assertEqual(u.digest(u.decoded(entry['merged'])), entry['before_hash'])

    def test_cli_output_redacts_the_demonstration_password(self):
        script = Path(__file__).with_name('update_team.py')
        roles = self.root / 'native-roles.json'
        roles.write_text(json.dumps(self.roles))

        def cli(*arguments):
            result = subprocess.run([sys.executable, '-B', str(script), '--repo', str(self.repo), *arguments],
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            return result.stdout

        printed = cli('init', '--home', str(self.home), '--team-id', 'cli-demo', '--roles', str(roles))
        self.assertNotIn('Synthetic-Demo-Passphrase-9', printed)
        self.assertEqual(json.loads(printed)['confirmed_values']['DEMO_PASSWORD'], '{{DEMO_PASSWORD}}')
        self.change()
        printed = cli('plan', '--home', str(self.home))
        self.assertNotIn('Synthetic-Demo-Passphrase-9', printed)
        proposal = json.loads(printed)
        self.assertEqual(proposal['confirmed_values']['DEMO_PASSWORD'], '{{DEMO_PASSWORD}}')
        for entry in proposal['entries']:
            payload = u.decoded(entry['new_base'])
            self.assertNotIn(b'Synthetic-Demo-Passphrase-9', payload)
            if entry['target'].endswith('/SOUL.md'):
                self.assertIn(b'`{{DEMO_PASSWORD}}`', payload)
        # The private proposal keeps the exact bytes the helper applies.
        stored = json.loads(Path(proposal['proposal']).read_text())
        souls = [entry for entry in stored['entries'] if entry['target'].endswith('/SOUL.md')]
        self.assertTrue(souls)
        for entry in souls:
            self.assertIn(b'Synthetic-Demo-Passphrase-9', u.decoded(entry['new_base']))

    def test_cli_redaction_swaps_only_the_rendered_literal(self):
        secret = 'Synthetic-Demo-Passphrase-9'
        masked = u.redacted({'merged': u.encoded(b'password `' + secret.encode() + b'` in demonstration text\n'),
                             'new_base': u.encoded(b'no secret here\n'),
                             'confirmed_values': {'DEMO_PASSWORD': secret, 'PROJECT_NAME': 'keep'}}, secret)
        self.assertIsInstance(masked, dict)
        assert isinstance(masked, dict)
        self.assertEqual(u.decoded(masked['merged']), b'password `{{DEMO_PASSWORD}}` in demonstration text\n')
        self.assertEqual(u.decoded(masked['new_base']), b'no secret here\n')
        self.assertEqual(masked['confirmed_values'], {'DEMO_PASSWORD': '{{DEMO_PASSWORD}}', 'PROJECT_NAME': 'keep'})
        stray = u.redacted({'merged': u.encoded(secret.encode() + b' outside code\n')}, secret)
        self.assertIsInstance(stray, dict)
        assert isinstance(stray, dict)
        self.assertEqual(stray['merged'], u.WITHHELD)
        self.assertEqual(u.redacted({'a': ['b', {'DEMO_PASSWORD': secret}]}, secret),
                         {'a': ['b', {'DEMO_PASSWORD': '{{DEMO_PASSWORD}}'}]})

    def pre200_installation(self):
        """Exact local source fixture, not an inferred package-version baseline."""
        original = Path(__file__).resolve().parents[1]
        commit = 'bd7664b531250c5583dec58d21570de1cace1120'
        self.git('fetch', '-q', str(original), commit)
        setup = u.setup_data(self.state)
        self.assertEqual(u.package_version(self.repo, commit), '1.1.22')
        for entry in u.desired(self.repo, commit, self.roles, setup['confirmed_values'], bindings=self.bindings):
            target = Path(entry['target'])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(entry['content'])
            target.chmod(entry['mode'])
        return u.initialize(self.repo, self.home, 'fixture-team', self.roles, base_commit=commit,
                            basis_evidence='Synthetic exact 1.1.22 source and complete managed-tree installation')

    def test_pre200_update_reports_and_replaces_local_text(self):
        target_version = json.loads((self.repo / 'manifest.json').read_text())['version']
        record = self.pre200_installation()
        self.assertEqual(record['maker_version'], '1.1.22')
        coder = Path(self.roles['coder']['home']) / 'SOUL.md'
        local = 'Local approved resource cap: 40 EUR; no deployment permission.\n\n'
        coder.write_text(local + coder.read_text())
        setup = self.state / 'setup.md'
        setup.write_text(setup.read_text() + '\nWorkflow migration 2.0.0: pending; old-card ownership unresolved.\n')
        before_setup = setup.read_bytes()
        plan = self.proposal()
        proposal = json.loads(plan.read_text())
        self.assertEqual(proposal['maker_version'], target_version)
        self.assertFalse(proposal['conflicts'])
        result = u.apply(self.home, plan, decision='proceed',
                         review='Checked local cap preservation; card migration and loading remain pending',
                         dependency_review='Authorized fixture file-only changes; no live transition or runtime change')
        self.assertEqual(result['status'], 'applied')
        updated = u.load_record(self.home)[2]
        self.assertEqual(updated['maker_version'], target_version)
        self.assertEqual(updated['roles'], self.roles)
        self.assertEqual(updated['confirmed_bindings'], self.bindings)
        self.assertFalse(coder.read_text().startswith(local))
        self.assertIn(str(coder), {item['path'] for item in proposal['adaptations']})
        self.assertIn('kanban_block(kind="needs_input", reason=...)', coder.read_text())
        self.assertNotIn('through native `kanban_request_review`', coder.read_text())
        reviewer = (Path(self.roles['reviewer']['home']) / 'SOUL.md').read_text()
        self.assertIn('only the Coder escalates it through the Planner.', reviewer)
        self.assertEqual(setup.read_bytes(), before_setup)

    def test_pre200_local_planner_route_is_reported_and_replaced(self):
        self.pre200_installation()
        coder = Path(self.roles['coder']['home']) / 'SOUL.md'
        old = 'Route the same task to `fixture-planner` through native `kanban_request_review`.'
        self.assertIn(old, coder.read_text())
        coder.write_text(coder.read_text().replace(old, 'Local binding mandate: route all decisions to Planner review.'))
        plan = self.proposal()
        proposal = json.loads(plan.read_text())
        self.assertFalse(proposal['conflicts'])
        self.assertIn(str(coder), {item['path'] for item in proposal['adaptations']})
        u.apply(self.home, plan, decision='proceed',
                review='Reported local route deviation; Maker text authoritative',
                dependency_review='Fixture file-only migration; runtime unchanged')
        self.assertNotIn('Local binding mandate', coder.read_text())
        self.assertIn('confirm the existing subscription wakes `fixture-planner`', coder.read_text())

    def test_113_installation_adopts_confirmed_role_bindings(self):
        self.check_historical_binding_upgrade('da11a12710aace9a0522c88fd8fb3ef378711d0c')

    def test_100_soul_baseline_adopts_confirmed_role_bindings(self):
        self.check_historical_binding_upgrade(u.LEGACY_COMMIT, legacy=True)

    def test_old_installation_missing_path_binding_stops_without_writes(self):
        setup = self.historical_installation('da11a12710aace9a0522c88fd8fb3ef378711d0c')
        marker = (self.state / 'installation.json').read_bytes()
        before = (self.home / 'SOUL.md').read_bytes()
        for field in ('PROJECT_DIR', 'REPOSITORY_ROOTS'):
            values = dict(setup['confirmed_values'])
            del values[field]
            (self.state / 'setup.md').write_text('```json\n' + json.dumps(dict(setup, confirmed_values=values)) + '\n```\n')
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'Missing confirmed.*' + field):
                self.proposal()
            self.assertEqual((self.home / 'SOUL.md').read_bytes(), before)
            self.assertEqual((self.state / 'installation.json').read_bytes(), marker)
        (self.state / 'setup.md').rename(self.state / 'audit-only.md')
        with self.assertRaisesRegex(ValueError, 'Missing confirmed.*operator'):
            self.proposal()
        self.assertEqual((self.state / 'installation.json').read_bytes(), marker)

    def test_old_installation_rejects_conflicting_planner_id(self):
        setup = self.historical_installation('da11a12710aace9a0522c88fd8fb3ef378711d0c')
        setup['confirmed_values']['PLANNER_PROFILE'] = 'wrong-planner'
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(setup) + '\n```\n')
        with self.assertRaisesRegex(ValueError, 'profile ID'):
            self.proposal()

    def test_bound_launcher_is_regenerated_and_binding_survives_updates(self):
        source = 'skills/brownfield-feature-planning/scripts/recover-triage'
        entries = u.desired(self.repo, self.base, self.roles,
                            json.loads((self.state / 'setup.md').read_text().split('```json\n')[1].split('\n```')[0])['confirmed_values'],
                            bindings=self.bindings)
        launcher = next((entry for entry in entries if entry['source'] == source), None)
        self.assertIsNotNone(launcher, 'Bound launcher must be delivered with the complete skill')
        self.assertEqual(launcher['transform'], 'bound-recovery-v1')
        target = Path(launcher['target'])
        target.write_bytes(launcher['content'])
        target.chmod(0o700)
        self.initialize()
        (self.state / 'setup.md').rename(self.state / 'audit-only.md')
        self.change(source, '\n# New launcher revision\n')
        plan = self.proposal()
        self.assertFalse(json.loads(plan.read_text())['conflicts'])
        result = u.apply(self.home, plan, decision='proceed', review='Checked bound launcher')
        self.assertEqual(result['status'], 'applied')
        self.assertTrue(target.read_text().endswith('# New launcher revision\n'))

        self.assertIn('/synthetic/python', target.read_text())
        self.assertEqual(target.stat().st_mode & 0o777, 0o700)
        record = json.loads((self.state / 'installation.json').read_text())
        self.assertEqual(record['confirmed_bindings'], self.bindings)
        entry = next(x for x in record['managed'] if x['source'] == source)
        self.assertEqual(entry['transform'], 'bound-recovery-v1')
        self.assertEqual((self.state / 'baselines' / entry['baseline']).read_bytes(), target.read_bytes())
        self.change(source, '# Another revision\n')
        self.assertFalse(json.loads(self.proposal().read_text())['conflicts'])

    def test_old_copy_installation_adopts_bound_launcher_from_maker_setup(self):
        source = 'skills/brownfield-feature-planning/scripts/recover-triage'
        template = (self.repo / source).read_bytes()
        manifest = json.loads((self.repo / 'manifest.json').read_text())
        del manifest['recovery_launcher']
        (self.repo / 'manifest.json').write_text(json.dumps(manifest))
        self.git('rm', source)
        self.commit('old generic copy installation')
        (self.home / source).unlink()
        setup = json.loads((self.state / 'setup.md').read_text().split('```json\n')[1].split('\n```')[0])
        del setup['confirmed_bindings']['triage_recovery']
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(setup) + '\n```\n')
        self.initialize()
        setup['confirmed_bindings']['triage_recovery'] = self.bindings['triage_recovery']
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(setup) + '\n```\n')
        manifest['recovery_launcher'] = source
        (self.repo / 'manifest.json').write_text(json.dumps(manifest))
        (self.repo / source).write_bytes(template)
        self.commit('add bound launcher')
        plan = self.proposal()
        result = u.apply(self.home, plan, decision='proceed', review='Checked Maker binding adoption')
        self.assertEqual(result['status'], 'applied')
        record = json.loads((self.state / 'installation.json').read_text())
        self.assertEqual(record['confirmed_bindings']['triage_recovery'], self.bindings['triage_recovery'])
        self.assertIn('/synthetic/python', (self.home / source).read_text())
        self.assertEqual((self.home / source).stat().st_mode & 0o777, 0o700)
        (self.state / 'setup.md').rename(self.state / 'audit-only.md')
        self.assertFalse(json.loads(self.proposal().read_text())['conflicts'])

    def test_legacy_safepoint_reports_user_provenance_not_history(self):
        original = Path(__file__).resolve().parents[1]
        result = u.legacy_baseline(original)
        self.assertEqual(result['maker_commit'], '21cae6551c03b6ab84d004f41fc81c921e3e9837')
        self.assertEqual(result['maker_version'], '1.0.0')
        self.assertEqual(result['provenance'], 'user-defined-1.0.0-safepoint')
        self.assertFalse(result['historical_installation_verified'])

    def test_complete_skill_tree_and_personalized_baseline(self):
        record = self.initialize()
        mapped = {(x['role'], x['source']) for x in record['managed']}
        self.assertIn(('planner', 'skills/brownfield-feature-planning/references/kanban-triage-recovery.md'), mapped)
        manifest = json.loads((self.repo / 'manifest.json').read_text())
        expected_skills = set()
        for name, skill in manifest['own_skills'].items():
            for harness, roles in skill['targets'].items():
                for role in roles:
                    for path in (self.repo / 'skills' / name).rglob('*'):
                        if path.is_file():
                            expected_skills.add((role, path.relative_to(self.repo).as_posix()))
        self.assertEqual({(x['role'], x['source']) for x in record['managed']
                          if x['source'].startswith('skills/')}, expected_skills)
        launcher = next(x for x in record['managed'] if x['source'].endswith('/recover-triage'))
        self.assertEqual(launcher['transform'], 'bound-recovery-v1')
        self.assertNotEqual(Path(launcher['target']).read_bytes(), (self.repo / launcher['source']).read_bytes())
        script_source = 'skills/brownfield-feature-planning/scripts/recover_triage.py'
        script = next(x for x in record['managed'] if x['source'] == script_source)
        self.assertEqual(script['role'], 'planner')
        self.assertEqual(script['transform'], 'copy-v1')
        self.assertEqual(Path(script['target']).read_bytes(), (self.repo / script_source).read_bytes())
        self.assertIn(('team-codex', 'skills/screenshot-to-code/LICENSE'), mapped)
        codex_entry = next(x for x in record['managed'] if x['role'] == 'team-codex' and x['source'] == 'skills/screenshot-to-code/LICENSE')
        self.assertEqual(codex_entry['target'], str(Path(self.roles['team-codex']['home']) / '.agents/skills/screenshot-to-code/LICENSE'))
        self.assertEqual(record['maker_commit'], self.base)
        self.assertEqual((self.state / 'installation.json').stat().st_mode & 0o777, 0o600)
        soul = next(x for x in record['managed'] if x['role'] == 'planner' and x['target'].endswith('/SOUL.md'))
        self.assertNotIn(b'{{', (self.state / 'baselines' / soul['baseline']).read_bytes())

    def test_new_recovery_script_is_delivered_by_existing_updater(self):
        source = 'skills/brownfield-feature-planning/scripts/recover_triage.py'
        original = (self.repo / source).read_bytes()
        target = self.home / source
        self.git('rm', source)
        self.commit('fixture before script extraction')
        target.unlink()
        self.initialize()
        (self.repo / source).parent.mkdir(parents=True, exist_ok=True)
        (self.repo / source).write_bytes(original)
        self.commit('ship reusable recovery script')
        plan = self.proposal()
        result = u.apply(self.home, plan, decision='proceed', review='Reviewed recovery extraction and preserved gates')
        self.assertEqual(result['status'], 'applied')
        self.assertEqual(target.read_bytes(), original)
        record = json.loads((self.state / 'installation.json').read_text())
        entry = next(x for x in record['managed'] if x['source'] == source)
        self.assertEqual(entry['transform'], 'copy-v1')
        self.assertEqual((self.state / 'baselines' / entry['baseline']).read_bytes(), original)
        self.assertEqual(record['maker_commit'], self.git('rev-parse', 'HEAD').strip())

    def test_dev_environment_complete_tree_delivery_and_local_update(self):
        record = self.initialize()
        entries = [e for e in record['managed'] if e['source'].startswith('skills/dev-environment/')]
        self.assertEqual({e['source'] for e in entries}, {'skills/dev-environment/SKILL.md'})
        self.assertEqual({e['role'] for e in entries}, {'planner'})
        for entry in entries:
            self.assertEqual(entry['target'], str(self.home / entry['source']))
            self.assertEqual(entry['transform'], 'copy-v1')
            self.assertEqual(Path(entry['target']).read_bytes(), (self.repo / entry['source']).read_bytes())
        for role in ('coder', 'reviewer', 'team-codex'):
            self.assertFalse((Path(self.roles[role]['home']) / 'skills/dev-environment').exists())
        main = self.home / 'skills/dev-environment/SKILL.md'
        main.write_bytes(b'Approved local environment note\n' + main.read_bytes())
        self.change('skills/dev-environment/SKILL.md', '\nUpdated environment instruction.\n')
        plan = self.proposal()
        self.assertIn(str(main), {item['path'] for item in json.loads(plan.read_text())['adaptations']})
        u.apply(self.home, plan, decision='proceed', review='Fixture environment update reviewed')
        self.assertFalse(main.read_bytes().startswith(b'Approved local environment note\n'))
        self.assertTrue(main.read_bytes().endswith(b'Updated environment instruction.\n'))

    def test_new_dev_environment_collision_addition_and_guarded_rollback(self):
        path = self.repo / 'manifest.json'
        manifest = json.loads(path.read_text())
        self.assertIn('dev-environment', manifest['own_skills'])
        entry = manifest['own_skills'].pop('dev-environment')
        relative = 'skills/dev-environment/SKILL.md'
        content = (self.repo / relative).read_bytes()
        self.git('rm', '-r', 'skills/dev-environment')
        path.write_text(json.dumps(manifest))
        self.commit('fixture before environment assignment')
        target = self.home / 'skills/dev-environment'
        shutil.rmtree(target)
        self.initialize()
        before = (self.state / 'installation.json').read_bytes()
        manifest['own_skills']['dev-environment'] = entry
        path.write_text(json.dumps(manifest))
        (self.repo / relative).parent.mkdir()
        (self.repo / relative).write_bytes(content)
        self.commit('fixture add Planner environment skill')
        target.mkdir()
        main = target / 'SKILL.md'
        main.write_bytes(b'Unrelated local skill.\n')
        plan = self.proposal()
        self.assertIn(str(main), json.loads(plan.read_text())['conflicts'])
        with self.assertRaisesRegex(ValueError, 'Text conflicts'):
            u.apply(self.home, plan, decision='proceed', review='Fixture unresolved collision')
        self.assertEqual(main.read_bytes(), b'Unrelated local skill.\n')
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)
        main.unlink()  # Resolve only this disposable fixture collision.
        plan = self.proposal()
        entries = [e for e in json.loads(plan.read_text())['entries'] if e['source'] == relative]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]['role'], 'planner')
        result = u.apply(self.home, plan, decision='proceed', review='Fixture environment addition reviewed')
        self.assertEqual(main.read_bytes(), content)
        restored = u.rollback(self.home, Path(result['run']), decision='proceed')
        self.assertEqual(set(restored['retained_additions']), {str(main)})
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)

    def test_prototype_complete_tree_maps_only_to_planner(self):
        record = self.initialize()
        entries = [e for e in record['managed'] if e['source'].startswith('skills/prototype/')]
        source = self.repo / 'skills/prototype'
        self.assertEqual({e['source'] for e in entries},
                         {p.relative_to(self.repo).as_posix() for p in source.rglob('*') if p.is_file()})
        self.assertEqual({e['role'] for e in entries}, {'planner'})
        for e in entries:
            self.assertEqual(e['target'], str(self.home / e['source']))
            self.assertEqual(e['transform'], 'copy-v1')
            self.assertEqual(Path(e['target']).read_bytes(), (self.repo / e['source']).read_bytes())
        main = self.home / 'skills/prototype/SKILL.md'
        main.write_bytes(b'Approved local planning note\n' + main.read_bytes())
        self.change('skills/prototype/SKILL.md', '\nUpdated prototype clarification instruction.\n')
        plan = self.proposal()
        self.assertIn(str(main), {item['path'] for item in json.loads(plan.read_text())['adaptations']})
        u.apply(self.home, plan, decision='proceed', review='Fixture prototype update reviewed')
        self.assertFalse(main.read_bytes().startswith(b'Approved local planning note\n'))
        self.assertTrue(main.read_bytes().endswith(b'Updated prototype clarification instruction.\n'))

    def test_new_prototype_tree_collision_and_guarded_rollback(self):
        path = self.repo / 'manifest.json'
        manifest = json.loads(path.read_text())
        entry = manifest['own_skills'].pop('prototype')
        files = {p.relative_to(self.repo).as_posix(): p.read_bytes()
                 for p in (self.repo / 'skills/prototype').rglob('*') if p.is_file()}
        self.git('rm', '-r', 'skills/prototype')
        path.write_text(json.dumps(manifest))
        self.commit('fixture before prototype assignment')
        target = self.home / 'skills/prototype'
        shutil.rmtree(target)
        self.initialize()
        before = (self.state / 'installation.json').read_bytes()
        manifest['own_skills']['prototype'] = entry
        path.write_text(json.dumps(manifest))
        for relative, content in files.items():
            p = self.repo / relative
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(content)
        self.commit('fixture add Planner-only prototype')
        target.mkdir()
        main = target / 'SKILL.md'
        main.write_bytes(b'Unrelated local skill.\n')
        plan = self.proposal()
        self.assertIn(str(main), json.loads(plan.read_text())['conflicts'])
        with self.assertRaisesRegex(ValueError, 'Text conflicts'):
            u.apply(self.home, plan, decision='proceed', review='Fixture unresolved collision')
        self.assertEqual(main.read_bytes(), b'Unrelated local skill.\n')
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)
        main.unlink()  # Fixture-only reconciliation, not a live retirement policy.
        plan = self.proposal()
        entries = [e for e in json.loads(plan.read_text())['entries'] if e['source'] in files]
        self.assertEqual({e['source'] for e in entries}, set(files))
        self.assertEqual({e['role'] for e in entries}, {'planner'})
        result = u.apply(self.home, plan, decision='proceed', review='Fixture prototype addition reviewed')
        for e in entries:
            self.assertEqual(Path(e['target']).read_bytes(), files[e['source']])
        restored = u.rollback(self.home, Path(result['run']), decision='proceed')
        self.assertEqual(set(restored['retained_additions']), {e['target'] for e in entries})
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)

    def diagnosis_added_to_existing_team(self):
        """Synthetic prior install without this owned skill; no live discovery."""
        path = self.repo / 'manifest.json'
        manifest = json.loads(path.read_text())
        self.assertIn('diagnosing-bugs', manifest['own_skills'], 'Missing owned diagnosis delivery')
        source = self.repo / 'skills/diagnosing-bugs'
        files = {p.relative_to(self.repo).as_posix(): p.read_bytes() for p in source.rglob('*') if p.is_file()}
        self.assertEqual(set(files), {'skills/diagnosing-bugs/' + name for name in
                                     ('SKILL.md', 'README.md', 'LICENSE', 'NOTICE.md', 'references/method.md')})
        entry = manifest['own_skills'].pop('diagnosing-bugs')
        self.git('rm', '-r', 'skills/diagnosing-bugs')
        path.write_text(json.dumps(manifest))
        self.commit('fixture prior installation without diagnosis')
        target = Path(self.roles['team-codex']['home']) / '.agents/skills/diagnosing-bugs'
        shutil.rmtree(target)
        self.initialize()
        before = (self.state / 'installation.json').read_bytes()
        manifest['own_skills']['diagnosing-bugs'] = entry
        path.write_text(json.dumps(manifest))
        for relative, content in files.items():
            p = self.repo / relative
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(content)
        self.commit('fixture newly assigned whole diagnosis tree at same package version')
        return files, target, before

    def test_new_owned_diagnosis_tree_maps_only_to_codex_and_retains_rollback_additions(self):
        files, target, before = self.diagnosis_added_to_existing_team()
        unaffected = {str(p): p.read_bytes() for role in ('planner', 'coder', 'reviewer')
                      for p in Path(self.roles[role]['home']).glob('SOUL.md')}
        # A real operational recipe change retains the existing dependency gate.
        self.change('references/setup.md', '\nDiagnosis delivery recipe fixture update.\n')
        plan = self.proposal()
        proposal = json.loads(plan.read_text())
        self.assertIn('references/setup.md', proposal['dependencies'])
        entries = [e for e in proposal['entries'] if e['source'] in files]
        self.assertEqual({e['source'] for e in entries}, set(files))
        self.assertEqual({e['role'] for e in entries}, {'team-codex'})
        for e in entries:
            self.assertEqual(e['target'], str(target / Path(e['source']).relative_to('skills/diagnosing-bugs')))
            self.assertEqual(e['transform'], 'copy-v1')
            self.assertIsNone(e['before_hash'])
            self.assertEqual(u.decoded(e['merged']), files[e['source']])
        with self.assertRaisesRegex(ValueError, 'Operational dependency changes'):
            u.apply(self.home, plan, decision='proceed', review='Fixture static review')
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)
        self.assertFalse(target.exists())
        result = u.apply(self.home, plan, decision='proceed', review='Fixture static review',
                         dependency_review='Approved synthetic file-only scope; no native activation')
        self.assertEqual(result['status'], 'applied')
        record = u.load_record(self.home)[2]
        for e in entries:
            self.assertEqual(Path(e['target']).read_bytes(), files[e['source']])
            managed = next(x for x in record['managed'] if x['target'] == e['target'])
            self.assertEqual((self.state / 'baselines' / managed['baseline']).read_bytes(), files[e['source']])
        for p, content in unaffected.items():
            self.assertEqual(Path(p).read_bytes(), content)
        restored = u.rollback(self.home, Path(result['run']), decision='proceed')
        self.assertEqual(set(restored['retained_additions']), {e['target'] for e in entries})
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)

    def test_new_owned_diagnosis_collision_withholds_and_existing_local_edits_survive(self):
        files, target, before = self.diagnosis_added_to_existing_team()
        target.mkdir(parents=True)
        main = target / 'SKILL.md'
        main.write_bytes(b'Unrelated same-name local skill.\n')
        plan = self.proposal()
        self.assertIn(str(main), json.loads(plan.read_text())['conflicts'])
        with self.assertRaisesRegex(ValueError, 'Text conflicts'):
            u.apply(self.home, plan, decision='proceed', review='Collision unresolved')
        self.assertEqual(main.read_bytes(), b'Unrelated same-name local skill.\n')
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)
        # Fixture-only reconciliation; real use requires the existing user decision.
        main.unlink()
        u.apply(self.home, self.proposal(), decision='proceed', review='Fixture collision reconciled')
        main.write_bytes(b'Local approved note\n' + main.read_bytes())
        main.chmod(0o640)
        self.change('skills/diagnosing-bugs/SKILL.md', '\nNew diagnosis instruction.\n')
        plan = self.proposal()
        self.assertIn(str(main), {item['path'] for item in json.loads(plan.read_text())['adaptations']})
        u.apply(self.home, plan, decision='proceed', review='Fixture local adaptation reported and replaced')
        self.assertFalse(main.read_bytes().startswith(b'Local approved note\n'))
        self.assertTrue(main.read_bytes().endswith(b'New diagnosis instruction.\n'))
        self.assertEqual(u.file_mode(main), 0o640)

    def test_legacy_souls_preserve_drift_and_do_not_adopt_skills(self):
        original = Path(__file__).resolve().parents[1]
        # Fetch only from the local source repository into the isolated fixture.
        self.git('fetch', '-q', str(original), u.LEGACY_COMMIT)
        target = self.home / 'SOUL.md'
        target.write_text('Local team note\n' + target.read_text())
        record = self.initialize(legacy=True)
        self.assertEqual(record['maker_commit'], '21cae6551c03b6ab84d004f41fc81c921e3e9837')
        self.assertFalse(record['historical_installation_verified'])
        self.assertEqual(len(record['managed']), 3)
        self.assertTrue(record['legacy_skills_unknown'])
        self.change()
        plan = self.proposal()
        self.assertIn('legacy skills: baseline unknown; withheld', json.loads(plan.read_text())['notices'])
        result = u.apply(self.home, plan, decision='proceed', review='Agent reviewed local drift',
                         dependency_review='User approved file-only migration; no runtime change')
        self.assertEqual(result['status'], 'applied')
        self.assertFalse(target.read_text().startswith('Local team note'))
        self.assertIn(str(target), {item['path'] for item in json.loads(plan.read_text())['adaptations']})
        skill = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        self.assertNotIn('New upstream instruction.', skill.read_text())

    def test_reviewer_investigation_reaches_existing_soul_and_replaces_local_policy(self):
        """Actual old/new SOUL delivery; no runtime activation or model call."""
        source = self.repo / 'templates/roles/reviewer.SOUL.md.template'
        candidate = source.read_text()
        heading = '## Proportional investigation\n'
        self.assertIn(heading, candidate)
        body = candidate.split(heading, 1)[1].split('\n## ', 1)[0]
        source.write_text(candidate.replace(heading + body + '\n', '', 1))
        self.commit('synthetic prior reviewer without investigation method')
        self.base = self.git('rev-parse', 'HEAD').strip()
        target = Path(self.roles['reviewer']['home']) / 'SOUL.md'
        setup = u.setup_data(self.state)
        old = next(e for e in u.desired(self.repo, self.base, self.roles,
                                       setup['confirmed_values'], bindings=self.bindings)
                   if e['role'] == 'reviewer' and e['transform'] == 'render-role-v1')
        target.write_bytes(old['content'])
        self.initialize()
        local = '\nLocal customer resource cap remains binding.\n'
        target.write_text(target.read_text() + local)
        neighbors = {r: (Path(self.roles[r]['home']) / 'SOUL.md').read_bytes()
                     for r in ('planner', 'coder')}
        source.write_text(candidate)
        self.commit('deliver candidate investigation through existing SOUL mapping')
        proposal = self.proposal()
        self.assertIn(str(target), {item['path'] for item in json.loads(proposal.read_text())['adaptations']})
        result = u.apply(self.home, proposal, decision='proceed', review='Static candidate and local-cap replacement')
        self.assertEqual(result['status'], 'applied')
        self.assertIn(heading, target.read_text())
        self.assertIn('Spec / requirement fidelity', target.read_text())
        self.assertIn('Technical quality / standards', target.read_text())
        self.assertFalse(target.read_text().endswith(local))
        _, _, record = u.load_record(self.home)
        managed = next(e for e in record['managed'] if e['target'] == str(target))
        baseline = (self.state / 'baselines' / managed['baseline']).read_bytes()
        self.assertEqual(target.read_bytes(), baseline)
        self.assertEqual(managed['transform'], 'render-role-v1')
        self.assertEqual(managed['installed_hash'], u.digest(target.read_bytes()))
        for role, before in neighbors.items():
            self.assertEqual((Path(self.roles[role]['home']) / 'SOUL.md').read_bytes(), before)
        self.assertEqual(u.rollback(self.home, Path(result['run']), decision='proceed')['status'], 'rolled-back')
        self.assertEqual(target.read_bytes(), old['content'] + local.encode())

    def test_reviewer_investigation_local_text_is_reported_and_replaced(self):
        self.initialize()
        source = self.repo / 'templates/roles/reviewer.SOUL.md.template'
        target = Path(self.roles['reviewer']['home']) / 'SOUL.md'
        clause = 'Review small, clearly bounded corrections directly'
        self.assertIn(clause, source.read_text())
        target.write_text(target.read_text().replace(clause, 'Locally amended small-correction policy'))
        source.write_text(source.read_text().replace(clause, 'Revised upstream small-correction policy'))
        self.commit('synthetic reviewer policy revision')
        proposal = self.proposal()
        data = json.loads(proposal.read_text())
        self.assertFalse(data['conflicts'])
        self.assertIn(str(target), {item['path'] for item in data['adaptations']})
        u.apply(self.home, proposal, decision='proceed', review='Reported local policy replacement')
        self.assertIn('Revised upstream small-correction policy', target.read_text())
        self.assertNotIn('Locally amended small-correction policy', target.read_text())

    def test_local_edit_is_replaced_and_new_baseline_is_pristine(self):
        self.initialize()
        target = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        target.write_text('Local heading\n' + target.read_text())
        self.change()
        plan = self.proposal()
        self.assertIn(str(target), {item['path'] for item in json.loads(plan.read_text())['adaptations']})
        result = u.apply(self.home, plan, decision='proceed', review='Agent checked all changed context files')
        self.assertEqual(result['status'], 'applied')
        self.assertFalse(target.read_text().startswith('Local heading\n'))
        self.assertTrue(target.read_text().endswith('New upstream instruction.\n'))
        record = json.loads((self.state / 'installation.json').read_text())
        entry = next(x for x in record['managed'] if x['target'] == str(target))
        self.assertFalse((self.state / 'baselines' / entry['baseline']).read_text().startswith('Local heading'))
        self.assertEqual(record['maker_commit'], self.git('rev-parse', 'HEAD').strip())
        self.assertEqual(u.rollback(self.home, Path(result['run']), decision='proceed')['status'], 'rolled-back')
        self.assertEqual(target.read_text().splitlines()[0], 'Local heading')
        self.assertNotIn('New upstream instruction.', target.read_text())
        self.assertEqual(json.loads((self.state / 'installation.json').read_text())['maker_commit'], self.base)

    def test_build_evidence_and_grant_rules_reach_fresh_and_existing_teams(self):
        record = self.initialize()
        sources = {entry['source'] for entry in record['managed']}
        self.assertIn('skills/build-evidence/SKILL.md', sources)
        self.assertIn('skills/build-evidence/references/production-build-selectors.md', sources)
        for role, subpath in (('reviewer', 'skills'), ('team-codex', '.agents/skills')):
            target = Path(self.roles[role]['home']) / subpath / 'build-evidence/SKILL.md'
            self.assertTrue(target.is_file(), (role, target))
        self.assertFalse((Path(self.roles['coder']['home']) / 'skills/build-evidence/SKILL.md').exists())
        coder = Path(self.roles['coder']['home']) / 'SOUL.md'
        reviewer = Path(self.roles['reviewer']['home']) / 'SOUL.md'
        self.assertNotIn('$build-evidence', coder.read_text())
        self.assertIn('never change your own `command_allowlist`', coder.read_text())
        self.assertIn('never change this profile\'s `command_allowlist`', reviewer.read_text())

        target = Path(self.roles['reviewer']['home']) / 'skills/build-evidence/references/jfr-observer.md'
        local = b'\nLocal build note.\n'
        target.write_bytes(target.read_bytes() + local)
        self.change('skills/build-evidence/SKILL.md', '\nNew build evidence rule.\n')
        plan = self.proposal()
        adaptations = {item['path']: item for item in json.loads(plan.read_text())['adaptations']}
        self.assertEqual(adaptations[str(target)]['version'], record['maker_version'])
        result = u.apply(self.home, plan, decision='proceed', review='Reported and replaced local build note')
        self.assertFalse(target.read_bytes().endswith(local))
        self.assertEqual(u.rollback(self.home, Path(result['run']), decision='proceed')['status'], 'rolled-back')
        self.assertTrue(target.read_bytes().endswith(local))

    def test_local_managed_text_replacement_precedes_both_sides(self):
        self.initialize()
        target = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        target.write_text(target.read_text().replace('name:', 'local-name:', 1))
        source = self.repo / 'skills/brownfield-feature-planning/SKILL.md'
        source.write_text(source.read_text().replace('name:', 'upstream-name:', 1))
        self.commit('local and upstream text change')
        plan = self.proposal()
        data = json.loads(plan.read_text())
        self.assertFalse(data['conflicts'])
        self.assertIn(str(target), {item['path'] for item in data['adaptations']})
        u.apply(self.home, plan, decision='proceed', review='Reported local text replacement')
        self.assertIn('upstream-name:', target.read_text())
        self.assertNotIn('local-name:', target.read_text())

    def test_activity_and_semantic_review_gates_and_skip(self):
        self.initialize()
        self.change()
        plan = self.proposal()
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, review='checked')
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed')
        self.assertEqual(u.apply(self.home, plan, decision='skip')['status'], 'skipped')
        self.assertEqual(json.loads((self.state / 'installation.json').read_text())['maker_commit'], self.base)

    def test_stale_target_and_metadata_are_rejected(self):
        self.initialize()
        self.change()
        plan = self.proposal()
        target = self.home / 'SOUL.md'
        target.write_text(target.read_text() + '\nConcurrent edit\n')
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertTrue(target.read_text().endswith('Concurrent edit\n'))

    def test_symlink_and_traversal_rejected(self):
        self.initialize()
        self.change()
        target = self.home / 'SOUL.md'
        outside = self.root / 'outside'
        outside.write_text('untouched')
        target.unlink()
        target.symlink_to(outside)
        with self.assertRaises(ValueError):
            self.proposal()
        self.assertEqual(outside.read_text(), 'untouched')
        with self.assertRaises(ValueError):
            u.safe_relative('../outside')

    def test_operational_changes_require_explicit_user_decision(self):
        self.initialize()
        self.change('references/integrations.md')
        plan = self.proposal()
        self.assertTrue(json.loads(plan.read_text())['dependencies'])
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed', review='checked')
        result = u.apply(self.home, plan, decision='proceed', review='checked', dependency_review='User approved file-only changes; runtime remains unchanged')
        self.assertEqual(result['status'], 'applied')

    def test_voltagent_revision_change_requires_decision_without_writing_agent_files(self):
        """Pinned metadata gates file updates; external TOMLs stay operator-owned."""
        self.initialize()
        agents = self.root / 'coder/devteam/codex-home/agents'
        agents.mkdir(parents=True)
        original = b'name = "reviewer"\nmodel = "local-model"\n'
        target = agents / 'reviewer.toml'
        target.write_bytes(original)
        target.chmod(0o600)
        manifest_path = self.repo / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        # Synthetic commit identifier; this offline fixture never fetches upstream.
        manifest['upstream_components']['codex-custom-agents']['source_revision'] = 'a' * 40
        manifest_path.write_text(json.dumps(manifest))
        self.commit('fixture change pinned VoltAgent revision')
        plan = self.proposal()
        self.assertIn('manifest.json:upstream_components', json.loads(plan.read_text())['dependencies'])
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed', review='checked')
        result = u.apply(self.home, plan, decision='proceed', review='checked',
                         dependency_review='Approved file-only update; VoltAgent companion update pending')
        self.assertEqual(result['status'], 'applied')
        self.assertEqual(target.read_bytes(), original)
        self.assertEqual(target.stat().st_mode & 0o777, 0o600)
        self.assertNotIn(str(target), {entry['target'] for entry in u.load_record(self.home)[2]['managed']})

    def test_domain_tree_addition_gates_files_without_installing_upstream(self):
        """The existing file-only updater gates a missing upstream dependency."""
        manifest_path = self.repo / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        domain = 'skills/engineering/domain-modeling'
        self.assertIn(domain, manifest['upstream_components']['grill-me']['subpaths'])
        manifest['upstream_components']['grill-me']['subpaths'].remove(domain)
        manifest_path.write_text(json.dumps(manifest))
        self.commit('fixture before domain assignment')
        self.initialize()
        manifest['upstream_components']['grill-me']['subpaths'].insert(-1, domain)
        manifest_path.write_text(json.dumps(manifest))
        self.commit('fixture add domain assignment at same revision and version')
        plan = self.proposal()
        proposal = json.loads(plan.read_text())
        self.assertIn('manifest.json:upstream_components', proposal['dependencies'])
        marker = (self.state / 'installation.json').read_bytes()
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual((self.state / 'installation.json').read_bytes(), marker)
        for role in ('planner', 'coder', 'reviewer'):
            self.assertFalse((Path(self.roles[role]['home']) / 'skills/domain-modeling').exists())
        self.assertFalse(any('domain-modeling' in entry['target']
                             for entry in u.load_record(self.home)[2]['managed']))

    def test_questionnaire_addition_gates_files_without_installing_upstream(self):
        """A new Matt subtree needs the approved upstream companion path."""
        path = self.repo / 'manifest.json'
        manifest = json.loads(path.read_text())
        skill = 'skills/productivity/to-questionnaire'
        manifest['upstream_components']['grill-me']['subpaths'].remove(skill)
        path.write_text(json.dumps(manifest))
        self.commit('fixture before questionnaire assignment')
        self.initialize()
        manifest['upstream_components']['grill-me']['subpaths'].insert(-1, skill)
        path.write_text(json.dumps(manifest))
        self.commit('fixture add questionnaire at same Matt revision and Maker version')
        plan = self.proposal()
        self.assertIn('manifest.json:upstream_components', json.loads(plan.read_text())['dependencies'])
        marker = (self.state / 'installation.json').read_bytes()
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual((self.state / 'installation.json').read_bytes(), marker)
        for role in ('planner', 'coder', 'reviewer'):
            self.assertFalse((Path(self.roles[role]['home']) / 'skills/to-questionnaire').exists())
        self.assertFalse(any('to-questionnaire' in entry['target']
                             for entry in u.load_record(self.home)[2]['managed']))

    def test_all_asset_pin_changes_gate_same_version_without_companion_writes(self):
        """Offline helper characterization; prose companion execution stays separate."""
        self.initialize()
        setup = self.state / 'setup.md'
        setup.write_text(setup.read_text() + '\nUpstream companion update: pending; provenance unknown.\n')
        before_setup = setup.read_bytes()
        manifest_path = self.repo / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        version = manifest['version']
        external = {}
        for relative in ('coder/devteam/codex-home/agents/reviewer.toml',
                         'planner/plugins/superpowers/local.txt',
                         'coder/skills/graphify/SKILL.md'):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b'Local upstream asset; preserve edits.\n')
            external[str(target)] = target.read_bytes()
        names = ('codex-cli', 'superpowers', 'grill-me', 'hindsight', 'ponytail',
                 'find-skills', 'codex-custom-agents', 'codebase-memory', 'graphify')
        for index, name in enumerate(names):
            with self.subTest(component=name):
                item = manifest['upstream_components'][name]
                self.assertRegex(item.get('source_revision', ''), r'^[0-9a-f]{40}$')
                # Synthetic identifiers, never fetched or presented as upstream evidence.
                item['source_revision'] = f'{index + 1:040x}'
                manifest_path.write_text(json.dumps(manifest))
                self.commit('fixture change asset pin ' + name)
                plan = self.proposal()
                proposal = json.loads(plan.read_text())
                self.assertEqual(proposal['maker_version'], version)
                self.assertIn('manifest.json:upstream_components', proposal['dependencies'])
                marker = (self.state / 'installation.json').read_bytes()
                with self.assertRaises(ValueError):
                    u.apply(self.home, plan, decision='proceed', review='checked')
                self.assertEqual((self.state / 'installation.json').read_bytes(), marker)
                result = u.apply(self.home, plan, decision='proceed', review='checked',
                                 dependency_review='Approved file-only fixture; companion remains pending')
                self.assertEqual(result['status'], 'applied')
                self.assertEqual(setup.read_bytes(), before_setup)
                managed = {x['target'] for x in u.load_record(self.home)[2]['managed']}
                for target, original in external.items():
                    self.assertNotIn(target, managed)
                    self.assertEqual(Path(target).read_bytes(), original)

    def test_cac_recipe_orders_staging_files_retirement_and_readbacks(self):
        """Static checks of the required operator order, with no native execution."""
        recipe = (self.repo / 'references/update.md').read_text()
        heading = '## CAC migration\n'
        self.assertIn(heading, recipe.splitlines(keepends=True))
        section = recipe.split(heading, 1)[1].split('\n## ', 1)[0]
        ordered = ('1. **Inspect**', '2. **Approve and back up**', '3. **Stage CAC**',
                   '4. **Apply files, then retire legacy bindings**', '5. **Verify and resume**',
                   '6. **Roll back**')
        positions = [section.index(step) for step in ordered]
        self.assertEqual(positions, sorted(positions))
        for start, end, clauses in (
            (0, 1, ('pre-update manifest', 'absence from the target manifest',
                    'CODEX_PROCESS_HOME', 'CODEX_HOME', 'AGENTS.override.md', 'nested project', 'truncation')),
            (1, 2, ('`pending`', 'outside all discovery roots', 'complete inventories, hashes, ownership, modes',
                    'activity decision')),
            (2, 3, ('`$CODEX_HOME/AGENTS.md`', 'preserve local text', 'withhold dependent file application')),
            (3, 4, ('After successful file application', 'concurrent drift', '`skills.auto_load`',
                    'only proven, pristine, authorized team-owned trees', 'foreign, shared, edited',
                    'without deleting, masking, or overwriting')),
            (4, 5, ('`complete` only', 'fresh native discovery', 'task and resume', 'Ponytail registration in the Team-Codex context',
                    'PONYTAIL_DEFAULT_MODE=full', 'even after installation metadata advances',
                    'Repeat the file proposal and companion checks', 'files updated; team update incomplete')),
        ):
            for clause in clauses:
                with self.subTest(step=ordered[start], clause=clause):
                    self.assertIn(clause, section[positions[start]:positions[end]])
        apply = section[positions[3]:positions[4]]
        self.assertLess(apply.index('After successful file application'), apply.index('reconcile `skills.auto_load`'))
        self.assertLess(apply.index('reconcile `skills.auto_load`'), apply.index('Retire only proven'))
        rollback = section[positions[-1]:]
        for clause in ('file-helper rollback', 'later edits', 'only recorded, authorized changes',
                       'native readbacks', 'renewed `pending`'):
            self.assertIn(clause, rollback)
        self.assertLess(rollback.index('Restore required legacy trees'),
                        rollback.index('Restore the prior Codex home instruction after reverting dependent SOULs'))
        for heading in ('Prepare and review one team', 'Activity and application', 'Verify and hand off'):
            body = recipe.split(f'## {heading}\n', 1)[1].split('\n## ', 1)[0]
            self.assertIn('(#cac-migration)', body)
        companion = recipe.split('## Required upstream companion update\n', 1)[1].split('\n## ', 1)[0]
        self.assertNotIn('Caveman, caveman-review', companion)
        self.assertNotIn('integrations.md#caveman', companion)

    def test_cac_recipe_requires_fresh_native_checks_and_journaled_recovery(self):
        recipe = (self.repo / 'references/update.md').read_text()
        cac = recipe.split('## CAC migration\n', 1)[1].split('\n## ', 1)[0]
        approval = cac.split('2. **Approve and back up**', 1)[1].split('3. **Stage CAC**', 1)[0]
        self.assertIn('Generic upstream approval alone does not authorize CAC writes', approval)
        companion = recipe.split('## Required upstream companion update\n', 1)[1].split('\n## ', 1)[0]
        self.assertIn('Route existing-team Team-Codex instruction writes and legacy Caveman reconciliation '
                      'through [CAC migration](#cac-migration)', companion)
        for action in ('staging', 'dependent file application', 'each retirement mutation',
                       'each rollback mutation'):
            self.assertIn('immediately before ' + action, cac)
        for evidence in ('`current_run_id`', '`claim_lock`', '`ended_at`', 'worker, dispatcher, and session',
                         'defer affected writes', 'read-only'):
            self.assertIn(evidence, cac)
        retirement = cac.split('4. **Apply files, then retire legacy bindings**', 1)[1]
        self.assertLess(retirement.index('Persist and read back the intent'), retirement.index('mv --no-copy'))
        for recovery in ('original present and quarantine absent', 'original absent and quarantine present',
                         'both paths present', 'both paths absent', 'no copy/delete fallback'):
            self.assertIn(recovery, cac.lower())
        rollback = cac.split('6. **Roll back**', 1)[1]
        self.assertLess(rollback.index('before restoring either'), rollback.index('Restore required legacy trees'))
        self.assertLess(rollback.index('Restore required legacy trees'), rollback.index('run the file-helper rollback'))
        self.assertLess(rollback.index('run the file-helper rollback'),
                        rollback.index('Restore the prior Codex home instruction'))

    def cac_rename(self, source, destination):
        """Run the documented stock command on disposable paths."""
        recipe = (self.repo / 'references/update.md').read_text()
        commands = [line.strip() for line in recipe.splitlines() if line.lstrip().startswith('mv --no-copy ')]
        self.assertEqual(len(commands), 1, 'CAC recipe must provide a rename-only command')
        help_text = subprocess.run(['mv', '--help'], capture_output=True, text=True, timeout=10).stdout
        if '--no-copy' not in help_text:
            self.skipTest('GNU mv with --no-copy is required for the documented rename command')
        return subprocess.run(['sh', '-c', commands[0]], capture_output=True, text=True, timeout=10,
                              env=dict(os.environ, SOURCE=str(source), DESTINATION=str(destination)))

    def test_cac_quarantine_interruptions_and_coordinated_rollback(self):
        before = self.cac_revisions()
        coder = Path(self.roles['coder']['home'])
        soul = coder / 'SOUL.md'
        old_soul = soul.read_bytes()
        instruction = Path(before['confirmed_values']['CODEX_HOME']) / 'AGENTS.md'
        local = b'# Local instructions\n'
        staged = local + b'# Fixture CAC instruction\n'
        u.atomic(instruction, local, None)
        u.atomic(instruction, staged, u.digest(local))

        original = coder / 'skills/caveman'
        legacy = {'SKILL.md': (b'# Legacy writing skill\n', 0o640),
                  'legal/LICENSE': (b'License fixture\n', 0o600)}
        original.mkdir(mode=0o750)
        for name, (data, mode) in legacy.items():
            u.atomic(original / name, data, None, mode)
        inode = original.stat().st_ino
        config = coder / 'config.yaml'
        old_config = b'skills:\n  auto_load: [local-skill, caveman, ponytail]\n'
        retired_config = b'skills:\n  auto_load: [local-skill, ponytail]\n'
        u.atomic(config, old_config, None)
        private = u.private_dir(self.state / 'cac-quarantine')
        quarantine = private / 'coder caveman'
        backup = private / 'verified backup'
        shutil.copytree(original, backup)

        result = u.apply(self.home, self.proposal(), decision='proceed', review='Fixture stage readback',
                         dependency_review='Approved CAC fixture scope')
        run = Path(result['run'])
        new_soul = soul.read_bytes()
        self.assertIn(b'Fixture legacy requirement: load caveman', old_soul)
        self.assertNotIn(b'Fixture legacy requirement: load caveman', new_soul)
        u.atomic(config, retired_config, u.digest(old_config))
        setup = self.state / 'setup.md'
        intent = (f'\nCAC pending: retire {original} into {quarantine}; '
                  f'backup {backup}; dependent file run {run}; inode {inode}.\n').encode()
        u.atomic(setup, setup.read_bytes() + intent, u.fingerprint(setup))

        # Interruption after intent, before rename. The pending source still holds the whole tree.
        self.assertIn(intent, setup.read_bytes())
        self.assertEqual(original.stat().st_ino, inode)
        self.assertFalse(os.path.lexists(quarantine))
        moved = self.cac_rename(original, quarantine)
        self.assertEqual(moved.returncode, 0, moved.stderr)
        # Interruption after rename, before receipt. Reopen the same intent and read both paths.
        self.assertIn(intent, setup.read_bytes())
        self.assertFalse(os.path.lexists(original))
        self.assertEqual(quarantine.stat().st_ino, inode)
        self.assertEqual(quarantine.stat().st_mode & 0o777, 0o750)
        for name, (data, mode) in legacy.items():
            self.assertEqual((quarantine / name).read_bytes(), data)
            self.assertEqual(u.file_mode(quarantine / name), mode)
            self.assertEqual((backup / name).read_bytes(), data)

        # Restore the tree and autoload before the actual file-helper rollback restores its consumers.
        restoring = f'\nCAC pending: restore {quarantine} to {original}.\n'.encode()
        u.atomic(setup, setup.read_bytes() + restoring, u.fingerprint(setup))
        moved = self.cac_rename(quarantine, original)
        self.assertEqual(moved.returncode, 0, moved.stderr)
        self.assertIn(restoring, setup.read_bytes())
        self.assertEqual(original.stat().st_ino, inode)
        self.assertFalse(os.path.lexists(quarantine))
        u.atomic(config, old_config, u.digest(retired_config))
        self.assertEqual(soul.read_bytes(), new_soul)
        self.assertEqual(instruction.read_bytes(), staged)
        self.assertEqual(u.rollback(self.home, run, decision='proceed')['status'], 'rolled-back')
        self.assertEqual(config.read_bytes(), old_config)
        self.assertEqual(soul.read_bytes(), old_soul)
        self.assertEqual(instruction.read_bytes(), staged)
        u.atomic(instruction, local, u.digest(staged))
        self.assertEqual(instruction.read_bytes(), local)
        self.assertEqual(u.load_record(self.home)[2], before)

    def test_cac_quarantine_exposes_drift_and_preserves_occupied_shared_targets(self):
        original = self.home / 'skills/caveman'
        original.mkdir()
        skill = original / 'SKILL.md'
        u.atomic(skill, b'pristine\n', None)
        pristine = u.fingerprint(skill)
        private = u.private_dir(self.state / 'cac-quarantine')
        quarantine = private / 'planner caveman'

        # A local edit and a second consumer's hard link invalidate pristine/exclusive ownership.
        other = Path(self.roles['reviewer']['home']) / 'shared-skill.md'
        os.link(skill, other)
        with self.assertRaisesRegex(ValueError, 'regular file'):
            u.fingerprint(skill)
        skill.write_bytes(b'local edit\n')
        self.assertNotEqual(u.digest(skill.read_bytes()), pristine)
        self.assertEqual(skill.stat().st_nlink, 2)
        self.assertEqual(other.read_bytes(), b'local edit\n')
        self.assertFalse(os.path.lexists(quarantine))

        # Use an independently pristine tree for retirement, then recreate the discovery path.
        original = Path(self.roles['reviewer']['home']) / 'skills/caveman-review'
        original.mkdir(parents=True)
        u.atomic(original / 'SKILL.md', b'pristine\n', None)
        moved = self.cac_rename(original, quarantine)
        self.assertEqual(moved.returncode, 0, moved.stderr)
        (quarantine / 'SKILL.md').write_bytes(b'later quarantine edit\n')
        self.assertNotEqual(u.fingerprint(quarantine / 'SKILL.md'), pristine)
        original.mkdir()
        occupied = original.stat().st_ino
        self.cac_rename(quarantine, original)
        self.assertEqual(original.stat().st_ino, occupied)
        self.assertEqual(list(original.iterdir()), [])
        original.rmdir()
        shared = self.home / 'skills'
        original.symlink_to(shared, target_is_directory=True)
        self.cac_rename(quarantine, original)
        self.assertEqual(original.readlink(), shared)
        self.assertEqual((quarantine / 'SKILL.md').read_bytes(), b'later quarantine edit\n')
        self.assertEqual(other.read_bytes(), b'local edit\n')

    def test_cac_native_recheck_detects_new_claim_without_file_drift(self):
        import sqlite3
        try:
            from hermes_cli import kanban_db as native
        except ImportError:
            self.skipTest('Installed Hermes Python required for the native claim readback')

        board = self.root / 'fixture-board.db'
        coder = self.roles['coder']
        soul = Path(coder['home']) / 'SOUL.md'
        before = (u.fingerprint(soul), u.file_mode(soul))
        writer = sqlite3.connect(board)
        self.addCleanup(writer.close)
        with writer:
            writer.executescript(native.SCHEMA_SQL)
            writer.execute("INSERT INTO tasks(id,title,assignee,status,created_at) VALUES "
                           "('fixture-task','Fixture task',?,'ready',1)", (coder['id'],))
        reader = sqlite3.connect(board.as_uri() + '?mode=ro', uri=True)
        self.addCleanup(reader.close)
        reader.row_factory = sqlite3.Row
        with reader:
            reader.execute('BEGIN')
            self.assertIsNone(native.list_tasks(reader)[0].claim_lock)
            self.assertEqual(native.list_runs(reader, 'fixture-task'), [])
        with writer:
            writer.execute("INSERT INTO task_runs(id,task_id,profile,status,claim_lock,started_at) "
                           "VALUES (1,'fixture-task',?,'running','fixture-claim',2)", (coder['id'],))
            writer.execute("UPDATE tasks SET status='running',claim_lock='fixture-claim',current_run_id=1")
        worker = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'],
                                  env=dict(os.environ, HERMES_HOME=coder['home']))
        try:
            with reader:
                reader.execute('BEGIN')
                task, = native.list_tasks(reader)
                run, = native.list_runs(reader, task.id)
                self.assertEqual((task.current_run_id, task.claim_lock), (run.id, 'fixture-claim'))
                self.assertEqual(run.profile, coder['id'])
                self.assertIsNone(run.ended_at)
            self.assertIn(worker.pid, u.activity(self.roles)['visible_pids'])
            self.assertEqual((u.fingerprint(soul), u.file_mode(soul)), before)
        finally:
            worker.terminate()
            worker.wait(timeout=5)

    def cac_revisions(self):
        """Build synthetic old/new Maker revisions without acquiring upstream trees."""
        manifest_path = self.repo / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        components = manifest['upstream_components']
        components['caveman'] = {'source_revision': 'a' * 40, 'targets': {
            'hermes': ['planner', 'coder', 'reviewer'], 'codex': ['team-codex']}}
        components['caveman-review'] = {'source_component': 'caveman', 'targets': {'hermes': ['reviewer']}}
        manifest_path.write_text(json.dumps(manifest))
        coder = self.repo / 'templates/roles/coder.SOUL.md.template'
        coder_template = coder.read_text()
        legacy_clause = '\nFixture legacy requirement: load caveman.\n'
        coder.write_text(coder_template + legacy_clause)
        installed_coder = Path(self.roles['coder']['home']) / 'SOUL.md'
        installed_coder.write_bytes(installed_coder.read_bytes() + legacy_clause.encode())
        self.commit('fixture legacy upstream assignments')
        before = self.initialize()

        for name in ('caveman', 'caveman-review'):
            del components[name]
        source = 'templates/team-codex-AGENTS.md'
        (self.repo / source).write_text('# Fixture CAC instruction\n')
        manifest['files'] = sorted(set(manifest['files']) | {source})
        major, minor, _ = map(int, before['maker_version'].split('.'))
        manifest['version'] = f'{major}.{minor + 1}.0'
        manifest_path.write_text(json.dumps(manifest))
        skill = self.repo / 'SKILL.md'
        skill.write_text(skill.read_text().replace(f"version: {before['maker_version']}\n",
                                                  f"version: {manifest['version']}\n", 1))
        coder.write_text(coder_template)
        self.change('templates/roles/coder.SOUL.md.template', '\nUse the compact task and resume form.\n')
        return before

    def test_cac_file_only_update_leaves_legacy_companions_pending_on_repeat(self):
        before = self.cac_revisions()
        setup = self.state / 'setup.md'
        setup.write_text(setup.read_text() + f"\nCAC migration: pending; exact base {before['maker_commit']}.\n"
                         'Fixture interruption: staged CAC; retirement and effective loading unverified.\n')
        values = u.setup_data(self.state)['confirmed_values']
        code_home = Path(values['CODEX_HOME'])
        process_home = Path(values['CODEX_PROCESS_HOME'])
        coder = Path(self.roles['coder']['home']) / 'SOUL.md'
        coder.write_text('Local rule: keep the approved resource cap.\n\n' + coder.read_text())
        plan = self.proposal()
        external = {
            code_home / 'AGENTS.md': b'# Local rules and staged CAC\nKeep the local review boundary.\n',
            code_home / 'AGENTS.override.md': b'# Local override\nKeep the local escalation rule.\n',
            code_home / 'config.toml': b'model = "fixture-model"\n[plugins."ponytail@team-ponytail"]\nenabled = true\n',
            self.root / 'workspace/nested/AGENTS.md': b'# Project rules\nPreserve local scope.\n',
            self.root / 'workspace/.agents/skills/caveman/SKILL.md': b'# Foreign project copy\n',
            self.root / 'coder/plugins/ponytail/plugin.yaml': b'name: ponytail\n',
            process_home / '.agents/skills/caveman/SKILL.md': b'# Legacy Codex copy\n',
        }
        for role in ('planner', 'coder', 'reviewer'):
            home = Path(self.roles[role]['home'])
            external[home / 'config.yaml'] = b'skills:\n  auto_load: [local-skill, caveman]\n'
            external[home / 'skills/caveman/SKILL.md'] = b'# Legacy Hermes copy\n'
        external[self.root / 'reviewer/skills/caveman-review/SKILL.md'] = b'# Locally edited review copy\n'
        for path, contents in external.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(contents)
            path.chmod(0o640)
        saved_setup = setup.read_bytes()

        proposal = json.loads(plan.read_text())
        self.assertIn('manifest.json:upstream_components', proposal['dependencies'])
        self.assertFalse(proposal['obsolete'])
        with self.assertRaisesRegex(ValueError, 'Operational dependency changes'):
            u.apply(self.home, plan, decision='proceed', review='Checked fixture scope')
        result = u.apply(self.home, plan, decision='proceed', review='Checked local rule preservation',
                         dependency_review='Fixture file-only decision; companion collision remains open')
        self.assertEqual(result['status'], 'applied')
        updated = u.load_record(self.home)[2]
        self.assertNotEqual(updated['maker_version'], before['maker_version'])
        self.assertEqual(updated['maker_commit'], proposal['maker_commit'])
        self.assertFalse(coder.read_text().startswith('Local rule: keep the approved resource cap.\n'))
        self.assertIn(str(coder), {item['path'] for item in proposal['adaptations']})
        repeat = json.loads(self.proposal().read_text())
        self.assertFalse(repeat['dependencies'] or repeat['conflicts'] or repeat['obsolete'])
        self.assertTrue(all(u.digest(u.decoded(entry['merged'])) == entry['before_hash']
                            for entry in repeat['entries']))
        self.assertEqual(setup.read_bytes(), saved_setup)
        self.assertIn('CAC migration: pending', setup.read_text())
        for path, contents in external.items():
            with self.subTest(path=path):
                self.assertNotIn(str(path), {entry['target'] for entry in updated['managed']})
                self.assertEqual(path.read_bytes(), contents)
                self.assertEqual(path.stat().st_mode & 0o777, 0o640)

    def test_cac_file_rollback_leaves_simulated_companion_changes_for_operator(self):
        """A clean Codex home starts without AGENTS.md; only fixture writes stage it."""
        before = self.cac_revisions()
        plan = self.proposal()
        code_home = Path(before['confirmed_values']['CODEX_HOME'])
        instruction = code_home / 'AGENTS.md'
        coder = Path(self.roles['coder']['home']) / 'SOUL.md'
        old_soul = coder.read_bytes()
        self.assertFalse(instruction.exists())
        self.assertEqual(u.apply(self.home, plan, decision='skip')['status'], 'skipped')
        self.assertEqual(coder.read_bytes(), old_soul)
        self.assertFalse(instruction.exists())
        code_home.mkdir(parents=True)
        instruction.write_bytes(b'# Staged CAC fixture\n')
        result = u.apply(self.home, plan, decision='proceed', review='Checked fixture SOUL change',
                         dependency_review='Approved fixture file-only scope')
        run = Path(result['run'])
        self.assertNotEqual(coder.read_bytes(), old_soul)
        self.assertEqual(instruction.read_bytes(), b'# Staged CAC fixture\n')
        instruction.write_bytes(b'# Later local work in team AGENTS.md\n')
        rolled_back = u.rollback(self.home, run, decision='proceed')
        self.assertEqual(rolled_back['status'], 'rolled-back')
        self.assertEqual(coder.read_bytes(), old_soul)
        self.assertEqual(u.load_record(self.home)[2], before)
        self.assertEqual(instruction.read_bytes(), b'# Later local work in team AGENTS.md\n')
        self.assertNotIn(str(instruction), rolled_back['retained_additions'])

    def test_obsolete_file_is_retained_and_classified(self):
        self.initialize()
        relative = 'skills/brownfield-feature-planning/references/project-retrospectives.md'
        (self.repo / relative).unlink()
        self.commit('remove source')
        plan = self.proposal()
        data = json.loads(plan.read_text())
        target = str(self.home / relative)
        record = next(item for item in data['obsolete'] if target in item['targets'])
        self.assertEqual(record['kind'], 'file')
        self.assertEqual(record['role'], 'planner')
        self.assertEqual(record['skill'], 'brownfield-feature-planning')
        self.assertEqual(record['root'], str(self.home / 'skills/brownfield-feature-planning'))
        self.assertEqual(record['state'], 'pristine')
        self.assertEqual(record['findings'], [])
        result = u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual(result['status'], 'applied')
        self.assertTrue((self.home / relative).exists())
        self.assertIn(target, result['retained_obsolete'])

    def test_pristine_obsolete_tree_is_classified_without_deletion(self):
        installed = self.deassigned_reviewer_skill()
        plan = self.proposal()
        proposal = json.loads(plan.read_text())
        trees = [item for item in proposal['obsolete'] if item['kind'] == 'tree']
        self.assertEqual(len(trees), 1)
        tree = trees[0]
        self.assertEqual(tree['role'], 'reviewer')
        self.assertEqual(tree['skill'], 'screenshot-to-code')
        self.assertEqual(tree['root'], str(Path(self.roles['reviewer']['home']) / 'skills/screenshot-to-code'))
        self.assertEqual(tree['targets'], sorted(installed))
        self.assertEqual(tree['state'], 'pristine')
        self.assertEqual(tree['findings'], [])
        result = u.apply(self.home, plan, decision='proceed', review='checked pristine reviewer candidate')
        self.assertEqual(result['status'], 'applied')
        self.assertEqual(result['retained_obsolete'], sorted(installed))
        _, _, record = u.load_record(self.home)
        self.assertEqual(record['retained_obsolete'], sorted(installed))
        for target, content in installed.items():
            self.assertEqual(Path(target).read_bytes(), content)

    def test_obsolete_classification_is_stable_across_preparations(self):
        self.deassigned_reviewer_skill()
        first = json.loads(self.proposal().read_text())['obsolete']
        second = json.loads(self.proposal().read_text())['obsolete']
        self.assertTrue(first)
        self.assertEqual(first, second)

    def test_local_edit_after_approval_invalidates_proposal(self):
        installed = self.deassigned_reviewer_skill()
        plan = self.proposal()
        target = Path(sorted(installed)[0])
        target.write_bytes(target.read_bytes() + b'\nLate local edit.\n')
        with self.assertRaisesRegex(ValueError, 'drift'):
            u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual(Path(target).read_bytes(), installed[str(target)] + b'\nLate local edit.\n')

    def test_symlink_in_obsolete_tree_is_indeterminate(self):
        self.deassigned_reviewer_skill()
        root = Path(self.roles['reviewer']['home']) / 'skills/screenshot-to-code'
        (root / 'references/linked.md').symlink_to('/etc/hostname')
        proposal = json.loads(self.proposal().read_text())
        tree = next(item for item in proposal['obsolete'] if item['kind'] == 'tree')
        self.assertEqual(tree['state'], 'indeterminate')
        self.assertTrue(any('linked.md' in finding for finding in tree['findings']), tree['findings'])

    def test_partially_missing_obsolete_tree_is_locally_modified(self):
        installed = self.deassigned_reviewer_skill()
        gone = sorted(installed)[0]
        Path(gone).unlink()
        proposal = json.loads(self.proposal().read_text())
        tree = next(item for item in proposal['obsolete'] if item['kind'] == 'tree')
        self.assertEqual(tree['state'], 'locally-modified')
        self.assertIn('missing: ' + gone, tree['findings'])

    def test_obsolete_mapping_outside_skill_roots_is_refused(self):
        soul = {'role': 'reviewer', 'source': 'templates/roles/reviewer.SOUL.md.template',
                'target': str(Path(self.roles['reviewer']['home']) / 'SOUL.md'), 'installed_hash': '0' * 64}
        with self.assertRaisesRegex(ValueError, 'outside a skill tree'):
            u.skill_placement(soul, self.roles)
        stray = {'role': 'reviewer', 'source': 'skills/demo/SKILL.md',
                 'target': '/synthetic/elsewhere/SKILL.md', 'installed_hash': '0' * 64}
        with self.assertRaisesRegex(ValueError, 'outside its recorded skill root'):
            u.skill_placement(stray, self.roles)
        candidates = u.obsolete_candidates({soul['target']: soul, stray['target']: stray},
                                           [soul['target'], stray['target']], self.roles)
        self.assertEqual([item['state'] for item in candidates], ['indeterminate'] * 2)
        self.assertEqual(u.obsolete_targets(candidates), sorted([soul['target'], stray['target']]))

    def test_fully_removed_obsolete_tree_is_absent(self):
        installed = self.deassigned_reviewer_skill()
        root = Path(self.roles['reviewer']['home']) / 'skills/screenshot-to-code'
        shutil.rmtree(root)
        plan = self.proposal()
        tree = next(item for item in json.loads(plan.read_text())['obsolete'] if item['kind'] == 'tree')
        self.assertEqual(tree['state'], 'absent')
        self.assertEqual(tree['targets'], sorted(installed))
        result = u.apply(self.home, plan, decision='proceed', review='checked absent candidate')
        self.assertEqual(result['status'], 'applied')
        self.assertFalse(root.exists())

    def test_reviewer_deassignment_retains_installed_skills(self):
        """The file helper retains trees; the required prose poststep is separate."""
        manifest_path = self.repo / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        names = ('minimal-change-engineering', 'screenshot-to-code')
        self.assertNotIn('project-lib-versioning', manifest['own_skills'])
        for name in names:
            manifest['own_skills'][name]['targets']['hermes'].append('reviewer')
        manifest_path.write_text(json.dumps(manifest))
        self.commit('fixture old reviewer equipment')
        setup = u.setup_data(self.state)
        previous = {}
        for entry in u.desired(self.repo, 'HEAD', self.roles, setup['confirmed_values'], bindings=self.bindings):
            if entry['role'] == 'reviewer' and entry['source'].startswith('skills/'):
                target = Path(entry['target'])
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(entry['content'])
                target.chmod(entry['mode'])
                previous[str(target)] = target.read_bytes()
        self.assertTrue(previous)
        self.initialize()
        # Local changes and untracked learned/reference files survive file apply.
        reviewer = Path(self.roles['reviewer']['home'])
        for name in names:
            main = reviewer / 'skills' / name / 'SKILL.md'
            main.write_bytes(main.read_bytes() + b'\nLocal adaptation.\n')
            learned = main.parent / 'references/local-learning.md'
            learned.parent.mkdir(exist_ok=True)
            learned.write_bytes(b'Learned local rule.\n')
            previous[str(main)] = main.read_bytes()
            previous[str(learned)] = learned.read_bytes()
        # These upstream trees are outside the file helper's managed mappings.
        for name in ('graphify', 'codebase-memory'):
            main = reviewer / 'skills' / name / 'SKILL.md'
            main.parent.mkdir(parents=True)
            main.write_bytes(b'Locally adapted upstream fixture.\n')
            previous[str(main)] = main.read_bytes()
        managed_previous = {
            item['target'] for item in u.load_record(self.home)[2]['managed']
            if item['role'] == 'reviewer' and any(item['source'].startswith(f'skills/{name}/') for name in names)}
        unaffected = {
            str(path): path.read_bytes()
            for role in ('planner', 'coder', 'team-codex')
            for path in (Path(self.roles[role]['home']) /
                         ('.agents/skills' if role == 'team-codex' else 'skills')).rglob('*') if path.is_file()}
        setup_path = self.state / 'setup.md'
        pending = '\nReviewer retirement 1.1.22: pending; pre-update evidence retained.\n'
        setup_path.write_text(setup_path.read_text() + pending)
        setup_before = setup_path.read_bytes()
        for name in names:
            manifest['own_skills'][name]['targets']['hermes'].remove('reviewer')
        manifest_path.write_text(json.dumps(manifest))
        self.commit('fixture deassign reviewer skills without deletion')
        plan = self.proposal()
        proposal = json.loads(plan.read_text())
        self.assertEqual(set(u.obsolete_targets(proposal['obsolete'])), managed_previous)
        trees = {item['skill']: item for item in proposal['obsolete'] if item['kind'] == 'tree'}
        self.assertEqual(set(trees), set(names))
        for name, item in trees.items():
            with self.subTest(name=name):
                self.assertEqual(item['state'], 'locally-modified')
                self.assertTrue(any(finding.startswith('modified:') for finding in item['findings']))
                self.assertTrue(any(finding.startswith('extra:') for finding in item['findings']))
        self.assertFalse(proposal['conflicts'])
        result = u.apply(self.home, plan, decision='proceed', review='Checked retained reviewer equipment')
        self.assertEqual(result['status'], 'applied')
        _, _, record = u.load_record(self.home)
        self.assertEqual(set(record['retained_obsolete']), managed_previous)
        self.assertFalse(managed_previous & {item['target'] for item in record['managed']})
        for target, content in previous.items():
            self.assertEqual(Path(target).read_bytes(), content)
        for target, content in unaffected.items():
            self.assertEqual(Path(target).read_bytes(), content)
        self.assertEqual(setup_path.read_bytes(), setup_before)

    def test_initial_record_rejects_profile_id_drift(self):
        path = self.state / 'setup.md'
        path.write_text(path.read_text().replace('"CODER_PROFILE": "fixture-coder"', '"CODER_PROFILE": "wrong-profile"'))
        with self.assertRaisesRegex(ValueError, 'profile ID'):
            self.initialize()

    def test_version_sources_must_agree(self):
        manifest = self.repo / 'manifest.json'
        data = json.loads(manifest.read_text())
        data['version'] = '9.9.9'
        manifest.write_text(json.dumps(data))
        self.commit('inconsistent release')
        with self.assertRaisesRegex(ValueError, 'version'):
            self.initialize()

    def test_renderer_change_is_withheld_not_executed(self):
        self.initialize()
        self.change('references/render_text.py')
        with self.assertRaisesRegex(ValueError, 'renderer'):
            self.proposal()

    def test_apply_rejects_tampered_payload(self):
        self.initialize()
        self.change()
        plan = self.proposal()
        data = json.loads(plan.read_text())
        data['entries'][0]['merged'] = 'RXZpbAo='
        plan.write_text(json.dumps(data))
        before = (self.home / 'SOUL.md').read_bytes()
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual((self.home / 'SOUL.md').read_bytes(), before)

    def test_baseline_corruption_and_mapping_injection_stop_plan(self):
        record = self.initialize()
        baseline = self.state / 'baselines' / record['managed'][0]['baseline']
        baseline.write_bytes(b'corrupted')
        with self.assertRaisesRegex(ValueError, 'baseline'):
            self.proposal()
        installation = self.state / 'installation.json'
        record['managed'][0]['target'] = str(self.root / 'outside')
        installation.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, 'mapping'):
            self.proposal()

    def test_partial_write_failure_keeps_revision_and_can_rollback(self):
        from unittest.mock import patch
        self.initialize()
        self.change()
        self.change('skills/minimal-change-engineering/SKILL.md')
        plan = self.proposal()
        before = (self.state / 'installation.json').read_bytes()
        real_atomic = u.atomic
        first = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        failing = self.home / 'skills/minimal-change-engineering/SKILL.md'

        def disk_failure(path, *args, **kwargs):
            if Path(path) == failing:
                raise OSError('simulated disk failure at second changed target')
            return real_atomic(path, *args, **kwargs)

        with patch.object(u, 'atomic', side_effect=disk_failure):
            with self.assertRaises(OSError):
                u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)
        self.assertIn('New upstream instruction.', first.read_text())
        runs = list((self.state / 'runs').iterdir())
        self.assertEqual(len(runs), 1)
        result = json.loads((runs[0] / 'result.json').read_text())
        self.assertEqual(result['status'], 'failed')
        self.assertEqual((runs[0] / 'installation.before.json').read_bytes(), before)
        self.assertEqual(u.rollback(self.home, runs[0], decision='proceed')['status'], 'rolled-back')
        self.assertNotIn('New upstream instruction.', first.read_text())

    def test_additions_are_copied_but_not_deleted_on_rollback(self):
        self.initialize()
        source = self.repo / 'skills/brownfield-feature-planning/references/new.py'
        source.write_text('print("new")\n')
        self.commit('add skill script')
        plan = self.proposal()
        result = u.apply(self.home, plan, decision='proceed', review='checked')
        target = self.home / 'skills/brownfield-feature-planning/references/new.py'
        self.assertEqual(target.read_text(), 'print("new")\n')
        rollback = u.rollback(self.home, Path(result['run']), decision='proceed')
        self.assertEqual(rollback['retained_additions'], [str(target)])
        self.assertTrue(target.exists())

    def test_rollback_refuses_edits_made_after_update(self):
        self.initialize()
        self.change()
        result = u.apply(self.home, self.proposal(), decision='proceed', review='checked')
        target = self.home / 'SOUL.md'
        target.write_text('New local work\n' + target.read_text())
        with self.assertRaisesRegex(ValueError, 'changed since update'):
            u.rollback(self.home, Path(result['run']), decision='proceed')
        self.assertTrue(target.read_text().startswith('New local work'))

    def test_active_process_is_observed_without_stopping_it(self):
        import sys
        process = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'],
                                   env=dict(os.environ, HERMES_HOME=str(self.home)))
        self.addCleanup(process.wait)
        self.addCleanup(process.terminate)
        observed = u.activity(self.roles)
        self.assertEqual(observed['state'], 'active')
        self.assertIn(process.pid, observed['visible_pids'])
        self.assertIsNone(process.poll())

    def test_unknown_activity_is_not_reported_as_idle(self):
        self.assertEqual(u.activity(self.roles)['state'], 'unknown')

    def test_duplicate_homes_and_hardlinks_are_rejected(self):
        duplicated = dict(self.roles)
        duplicated['coder'] = dict(self.roles['coder'], home=str(self.home))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            u.initialize(self.repo, self.home, 'fixture-team', duplicated)
        self.initialize()
        target = self.home / 'SOUL.md'
        os.link(target, self.root / 'soul-hardlink')
        with self.assertRaisesRegex(ValueError, 'regular file'):
            self.proposal()

    def test_delivered_package_versions_agree(self):
        root = Path(__file__).resolve().parents[1]
        manifest = json.loads((root / 'manifest.json').read_text())
        import re
        match = re.search(r'^version: (.+)$', (root / 'SKILL.md').read_text(), re.MULTILINE)
        assert match is not None
        version = match[1]
        self.assertRegex(version, r'^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$')
        self.assertEqual(version, manifest['version'])

    def test_documented_exact_base_keeps_existing_local_changes(self):
        target = self.home / 'SOUL.md'
        target.write_text('Existing local note\n' + target.read_text())
        record = u.initialize(self.repo, self.home, 'fixture-team', self.roles,
                              base_commit=self.base, basis_evidence='Existing setup proves this exact commit and all own skill copies')
        self.assertEqual(record['maker_commit'], self.base)
        self.assertEqual(record['provenance'], 'documented-setup-baseline')
        self.assertTrue(target.read_text().startswith('Existing local note'))
        with self.assertRaises(ValueError):
            u.initialize(self.repo, self.home, 'other-team', self.roles, base_commit='HEAD')

    def test_final_receipt_failure_does_not_advance_metadata(self):
        from unittest.mock import patch
        self.initialize()
        self.change()
        plan = self.proposal()
        before = (self.state / 'installation.json').read_bytes()
        real_atomic = u.atomic
        failed = False

        def receipt_failure(path, data, *args, **kwargs):
            nonlocal failed
            if Path(path).name == 'result.json' and json.loads(data)['status'] == 'applied' and not failed:
                failed = True
                raise OSError('simulated receipt disk failure')
            return real_atomic(path, data, *args, **kwargs)

        with patch.object(u, 'atomic', side_effect=receipt_failure):
            with self.assertRaises(OSError):
                u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)
        run = next((self.state / 'runs').iterdir())
        self.assertEqual(json.loads((run / 'result.json').read_text())['status'], 'failed')
        self.assertEqual(u.rollback(self.home, run, decision='proceed')['status'], 'rolled-back')

    def test_cli_end_to_end_with_readback(self):
        import sys
        script = Path(__file__).with_name('update_team.py')
        roles = self.root / 'native-roles.json'
        roles.write_text(json.dumps(self.roles))

        def cli(*arguments, success=True) -> Any:
            result = subprocess.run([sys.executable, '-B', str(script), '--repo', str(self.repo), *arguments],
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, 0 if success else 1, result.stderr)
            return json.loads(result.stdout) if success else result.stderr

        record = cli('init', '--home', str(self.home), '--team-id', 'cli-team', '--roles', str(roles))
        self.assertEqual(record['maker_commit'], self.base)
        self.change()
        plan = cli('plan', '--home', str(self.home))
        self.assertEqual(plan['maker_commit'], self.git('rev-parse', 'HEAD').strip())
        error = cli('apply', '--home', str(self.home), '--proposal', plan['proposal'], success=False)
        self.assertIn('explicit proceed/skip decision', error)
        result = cli('apply', '--home', str(self.home), '--proposal', plan['proposal'],
                     '--activity-decision', 'proceed', '--semantic-review', 'Agent reviewed changed skill instructions')
        self.assertEqual(result['status'], 'applied')
        self.assertEqual(json.loads((Path(result['run']) / 'result.json').read_text())['status'], 'applied')
        restored = cli('rollback', '--home', str(self.home), '--run', result['run'], '--activity-decision', 'proceed')
        self.assertEqual(restored['status'], 'rolled-back')
        self.assertEqual(json.loads((self.state / 'installation.json').read_text())['maker_commit'], self.base)
        inventory = self.root / 'native-homes.json'
        inventory.write_text(json.dumps([{'id': 'native-resolved-planner', 'home': str(self.home)}]))
        discovered = cli('discover', '--homes', str(inventory))
        self.assertEqual(discovered[0]['team_id'], 'cli-team')

    def test_missing_proposal_stops_with_clear_error(self):
        self.initialize()
        with self.assertRaisesRegex(ValueError, 'Missing required file'):
            u.apply(self.home, self.state / 'proposals/missing.json', decision='proceed', review='checked')

    def test_discovery_failure_does_not_hide_independent_team(self):
        self.initialize()
        link = self.root / 'linked-native-home'
        link.symlink_to(self.home, target_is_directory=True)
        found = u.discover([{'id': 'bad-home', 'home': str(link)}, {'id': 'actual-planner', 'home': str(self.home)}])
        self.assertEqual([item['status'] for item in found], ['failed', 'recorded'])
        self.assertEqual(found[1]['team_id'], 'fixture-team')

    def test_nested_coder_codex_home_supports_init_plan_apply(self):
        nested = Path(self.roles['coder']['home']) / 'devteam/user-home'
        self.assertEqual(self.roles['team-codex']['home'], str(nested))
        self.initialize()
        self.change('skills/screenshot-to-code/SKILL.md')
        result = u.apply(self.home, self.proposal(), decision='proceed', review='checked nested layout')
        self.assertEqual(result['status'], 'applied')
        self.assertIn('New upstream instruction.', (nested / '.agents/skills/screenshot-to-code/SKILL.md').read_text())

    def test_nested_codex_home_cannot_overlap_managed_skill_area(self):
        nested = Path(self.roles['coder']['home']) / 'skills/codex-home'
        nested.mkdir(parents=True)
        self.roles['team-codex']['home'] = str(nested)
        with self.assertRaisesRegex(ValueError, 'collid|overlap|Overlapping'):
            self.initialize()

    def test_missing_managed_files_block_apply_without_advancing_record(self):
        self.initialize()
        before = (self.state / 'installation.json').read_bytes()
        self.change('skills/minimal-change-engineering/SKILL.md')
        for relative in ('SOUL.md', 'skills/brownfield-feature-planning/SKILL.md'):
            with self.subTest(relative=relative):
                target = self.home / relative
                saved = target.read_bytes()
                target.unlink()
                plan = self.proposal()
                self.assertIn(str(target), json.loads(plan.read_text())['conflicts'])
                with self.assertRaises(ValueError):
                    u.apply(self.home, plan, decision='proceed', review='checked')
                self.assertFalse(target.exists())
                self.assertEqual((self.state / 'installation.json').read_bytes(), before)
                target.write_bytes(saved)

    def test_present_empty_file_is_replaced_as_a_local_deviation(self):
        self.initialize()
        target = self.home / 'SOUL.md'
        before = target.read_bytes()
        target.write_bytes(b'')
        self.change()
        plan = self.proposal()
        data = json.loads(plan.read_text())
        self.assertNotIn(str(target), data['conflicts'])
        self.assertIn(str(target), {item['path'] for item in data['adaptations']})
        result = u.apply(self.home, plan, decision='proceed', review='checked deliberate empty local file')
        self.assertEqual(target.read_bytes(), before)
        self.assertEqual(u.rollback(self.home, Path(result['run']), decision='proceed')['status'], 'rolled-back')
        self.assertEqual(target.read_bytes(), b'')

    def test_updates_preserve_local_modes_and_private_state(self):
        self.initialize()
        target = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        target.chmod(0o640)
        self.change()
        plan = self.proposal()
        result = u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual(target.stat().st_mode & 0o7777, 0o640)
        for path in self.state.rglob('*'):
            if path.is_file() and path.name != 'setup.md':
                self.assertEqual(path.stat().st_mode & 0o7777, 0o600, str(path))
        u.rollback(self.home, Path(result['run']), decision='proceed')
        self.assertEqual(target.stat().st_mode & 0o7777, 0o640)
        self.assertNotIn('New upstream instruction.', target.read_text())

    def test_new_executable_helper_uses_owner_only_mode_and_runs(self):
        self.initialize()
        source = self.repo / 'skills/brownfield-feature-planning/references/new.sh'
        source.write_text('#!/bin/sh\nprintf "helper-ok\\n"\n')
        source.chmod(0o755)
        plain = source.with_name('new.txt')
        plain.write_text('plain\n')
        self.commit('add executable helper')
        result = u.apply(self.home, self.proposal(), decision='proceed', review='checked helper')
        target = self.home / source.relative_to(self.repo)
        self.assertEqual(target.stat().st_mode & 0o7777, 0o700)
        self.assertEqual(target.with_name('new.txt').stat().st_mode & 0o7777, 0o600)
        self.assertEqual(subprocess.check_output([str(target)], text=True), 'helper-ok\n')
        restored = u.rollback(self.home, Path(result['run']), decision='proceed')
        self.assertIn(str(target), restored['retained_additions'])
        self.assertEqual(target.stat().st_mode & 0o7777, 0o700)

    def test_mode_drift_after_plan_blocks_apply(self):
        self.initialize()
        self.change()
        plan = self.proposal()
        target = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        target.chmod(0o711)
        before = (self.state / 'installation.json').read_bytes()
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual(target.stat().st_mode & 0o7777, 0o711)
        self.assertEqual((self.state / 'installation.json').read_bytes(), before)

    def test_rollback_refuses_mode_changes_after_update(self):
        self.initialize()
        self.change()
        result = u.apply(self.home, self.proposal(), decision='proceed', review='checked')
        target = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        target.chmod(0o711)
        with self.assertRaisesRegex(ValueError, 'changed since update'):
            u.rollback(self.home, Path(result['run']), decision='proceed')
        self.assertEqual(target.stat().st_mode & 0o7777, 0o711)

    def test_malformed_records_fail_per_home_and_discovery_continues(self):
        record = self.initialize()
        marker = self.state / 'installation.json'
        other = Path(self.roles['reviewer']['home'])
        (other / 'devteam').mkdir(mode=0o700)
        (other / 'devteam/setup.md').write_text('existing setup marker')
        invalid = [[], None, 'record', {}, dict(record, roles=[]),
                   dict(record, roles=dict(self.roles, coder=[])),
                   dict(record, roles=dict(self.roles, coder={'id': [], 'home': 7})),
                   dict(record, managed={}), dict(record, managed=[None]),
                   dict(record, managed=[dict(record['managed'][0], baseline=[])]),
                   dict(record, confirmed_values=[]), dict(record, maker_commit=[])]
        for value in invalid:
            with self.subTest(record=value):
                marker.write_text(json.dumps(value))
                found = u.discover([{'home': str(self.home)}, {'home': str(other)}])
                self.assertEqual([item['status'] for item in found], ['failed', 'unrecorded'])
                self.assertEqual(found[0]['home'], str(self.home))
                self.assertTrue(found[0]['error'])
                with self.assertRaises(ValueError):
                    u.load_record(self.home)

    def test_malformed_inventory_entries_do_not_hide_valid_team(self):
        self.initialize()
        for item in (None, [], 'home', {}, {'home': None}, {'home': []}, {'home': 7}):
            with self.subTest(item=item):
                found = u.discover([item, {'home': str(self.home)}])
                self.assertEqual([entry['status'] for entry in found], ['failed', 'recorded'])
        for inventory in (None, {}, 'homes'):
            with self.subTest(inventory=inventory), self.assertRaises(ValueError):
                u.discover(inventory)

    def test_discovery_uses_supplied_native_homes_not_names(self):
        self.initialize()
        found = u.discover([{'id': 'unexpected', 'home': str(self.home)}, {'id': 'coder', 'home': self.roles['coder']['home']}])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]['team_id'], 'fixture-team')


if __name__ == '__main__':
    unittest.main()
