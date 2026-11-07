"""Isolated updater contracts. No live Hermes imports or profile writes."""
from typing import Any
import json
import os
from pathlib import Path
import shutil
import subprocess
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
        self.assertEqual(target.read_bytes(), before_targets[str(target)][0] + b'\nNew upstream instruction.\n')
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
                      if key not in ('PROJECT_DIR', 'REPOSITORY_ROOTS', 'PLANNER_PROFILE')}
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
        self.assertTrue(target.read_text().startswith('Local team note\n'))
        self.assertIn("`/synthetic/client's workspace`", target.read_text())
        self.assertIn("`Planning: /synthetic/plans; implementation: /synthetic/client's workspace/code`", target.read_text())
        coder = (Path(self.roles['coder']['home']) / 'SOUL.md').read_text()
        self.assertIn('Route the same task to `fixture-planner`', coder)
        self.assertIn('Send one TIMER request to `fixture-planner`', coder)
        record = json.loads((self.state / 'installation.json').read_text())
        self.assertEqual(record['confirmed_values']['PROJECT_DIR'], setup['confirmed_values']['PROJECT_DIR'])
        self.assertEqual(record['confirmed_values']['REPOSITORY_ROOTS'], setup['confirmed_values']['REPOSITORY_ROOTS'])
        self.assertEqual(record['confirmed_values']['PLANNER_PROFILE'], 'fixture-planner')
        (self.state / 'setup.md').rename(self.state / 'audit-only.md')
        self.assertFalse(json.loads(self.proposal().read_text())['conflicts'])

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
        codex_entry = next(x for x in record['managed'] if x['role'] == 'team-codex' and x['source'].endswith('/LICENSE'))
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
        self.assertTrue(target.read_text().startswith('Local team note'))
        skill = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        self.assertNotIn('New upstream instruction.', skill.read_text())

    def test_three_way_keeps_local_edits_and_pristine_new_baseline(self):
        self.initialize()
        target = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        target.write_text('Local heading\n' + target.read_text())
        self.change()
        plan = self.proposal()
        result = u.apply(self.home, plan, decision='proceed', review='Agent checked all changed context files')
        self.assertEqual(result['status'], 'applied')
        self.assertTrue(target.read_text().startswith('Local heading\n'))
        self.assertTrue(target.read_text().endswith('New upstream instruction.\n'))
        record = json.loads((self.state / 'installation.json').read_text())
        entry = next(x for x in record['managed'] if x['target'] == str(target))
        self.assertFalse((self.state / 'baselines' / entry['baseline']).read_text().startswith('Local heading'))
        self.assertEqual(record['maker_commit'], self.git('rev-parse', 'HEAD').strip())
        self.assertEqual(u.rollback(self.home, Path(result['run']), decision='proceed')['status'], 'rolled-back')
        self.assertEqual(target.read_text().splitlines()[0], 'Local heading')
        self.assertNotIn('New upstream instruction.', target.read_text())
        self.assertEqual(json.loads((self.state / 'installation.json').read_text())['maker_commit'], self.base)

    def test_conflict_stops_without_target_writes(self):
        self.initialize()
        target = self.home / 'skills/brownfield-feature-planning/SKILL.md'
        target.write_text(target.read_text().replace('name:', 'local-name:', 1))
        source = self.repo / 'skills/brownfield-feature-planning/SKILL.md'
        source.write_text(source.read_text().replace('name:', 'upstream-name:', 1))
        self.commit('conflict')
        before = target.read_bytes()
        plan = self.proposal()
        self.assertTrue(json.loads(plan.read_text())['conflicts'])
        with self.assertRaises(ValueError):
            u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual(target.read_bytes(), before)

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

    def test_obsolete_file_is_retained_and_reported(self):
        self.initialize()
        relative = 'skills/brownfield-feature-planning/references/project-retrospectives.md'
        (self.repo / relative).unlink()
        self.commit('remove source')
        plan = self.proposal()
        data = json.loads(plan.read_text())
        self.assertTrue(data['obsolete'])
        result = u.apply(self.home, plan, decision='proceed', review='checked')
        self.assertEqual(result['status'], 'applied')
        self.assertTrue((self.home / relative).exists())

    def test_reviewer_deassignment_retains_installed_skills(self):
        """The file helper retains trees; the required prose poststep is separate."""
        manifest_path = self.repo / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        names = ('minimal-change-engineering', 'project-lib-versioning', 'screenshot-to-code')
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
            if item['role'] == 'reviewer' and item['source'].startswith('skills/')}
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
        self.assertEqual(set(proposal['obsolete']), managed_previous)
        self.assertFalse(proposal['conflicts'])
        result = u.apply(self.home, plan, decision='proceed', review='Checked retained reviewer equipment')
        self.assertEqual(result['status'], 'applied')
        _, _, record = u.load_record(self.home)
        self.assertEqual(set(record['retained_obsolete']), managed_previous)
        self.assertFalse(set(previous) & {item['target'] for item in record['managed']})
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

    def test_present_empty_file_is_not_a_missing_file(self):
        self.initialize()
        target = self.home / 'SOUL.md'
        target.write_bytes(b'')
        self.change()
        plan = self.proposal()
        self.assertNotIn(str(target), json.loads(plan.read_text())['conflicts'])
        u.apply(self.home, plan, decision='proceed', review='checked deliberate empty local file')
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
