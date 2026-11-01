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
            home = self.root / role
            home.mkdir(mode=0o700)
            self.roles[role] = {'id': 'fixture-' + role, 'home': str(home)}
        self.home = Path(self.roles['planner']['home'])
        self.state = self.home / 'devteam'
        self.state.mkdir(mode=0o700)
        values = {key: 'medium' if 'REASONING' in key else 'sample' for key in [
            'PLANER_NAME', 'CODER_NAME', 'REVIEWER_NAME', 'PROJECT_NAME',
            'HINDSIGHT_BANK_NAME', 'KANBAN_BOARD_NAME', 'CODER_PROFILE', 'REVIEWER_PROFILE',
            'CODEX_REASONING_DEFAULT', 'CODEX_REASONING_MAX', 'ROLE_REASONING_DEFAULT', 'ROLE_REASONING_HIGH']}
        values['CODER_PROFILE'] = self.roles['coder']['id']
        values['REVIEWER_PROFILE'] = self.roles['reviewer']['id']
        record = {'confirmed_values': values, 'confirmed_bindings': {'board': 'sample'}}
        (self.state / 'setup.md').write_text('```json\n' + json.dumps(record) + '\n```\n')
        (self.state / 'setup.md').chmod(0o600)
        for entry in u.desired(self.repo, self.base, self.roles, values):
            path = Path(entry['target'])
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(entry['content'])

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
        self.assertIn(('team-codex', 'skills/screenshot-to-code/LICENSE'), mapped)
        codex_entry = next(x for x in record['managed'] if x['role'] == 'team-codex' and x['source'].endswith('/LICENSE'))
        self.assertEqual(codex_entry['target'], str(Path(self.roles['team-codex']['home']) / '.agents/skills/screenshot-to-code/LICENSE'))
        self.assertEqual(record['maker_commit'], self.base)
        self.assertEqual((self.state / 'installation.json').stat().st_mode & 0o777, 0o600)
        soul = next(x for x in record['managed'] if x['role'] == 'planner' and x['target'].endswith('/SOUL.md'))
        self.assertNotIn(b'{{', (self.state / 'baselines' / soul['baseline']).read_bytes())

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

    def test_discovery_uses_supplied_native_homes_not_names(self):
        self.initialize()
        found = u.discover([{'id': 'unexpected', 'home': str(self.home)}, {'id': 'coder', 'home': self.roles['coder']['home']}])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]['team_id'], 'fixture-team')


if __name__ == '__main__':
    unittest.main()
