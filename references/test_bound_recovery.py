"""Maker binding and installed launcher contracts in isolated file fixtures."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'skills/brownfield-feature-planning/scripts/recover-triage'


class BoundRecoveryTests(unittest.TestCase):
    def test_maker_installs_callable_binding_without_runtime_setup(self):
        # Catch missing generation, unsafe shell quoting and runtime setup reads.
        self.assertTrue((ROOT / 'references/bind_recovery.py').is_file(), 'Maker binder missing')
        import bind_recovery as b
        with tempfile.TemporaryDirectory(prefix="bound ' fixture ") as directory:
            root = Path(directory)
            home = root / 'planner home'
            state = home / 'devteam'
            state.mkdir(parents=True, mode=0o700)
            script = home / 'skills/brownfield-feature-planning/scripts/recover_triage.py'
            script.parent.mkdir(parents=True)
            # An argv recorder isolates launcher execution from native mutations.
            script.write_text('import json,sys\nprint(json.dumps(sys.argv[1:]))\n')
            interpreter = root / "python ' executable"
            interpreter.symlink_to(sys.executable)
            binding = {'python': str(interpreter), 'script': str(script),
                       'db': str(root / "board ' ; $(false).db"), 'planner_profile': 'fixture-planner'}
            record = {'confirmed_values': {}, 'confirmed_bindings': {
                'roles': {'planner': {'id': 'fixture-planner', 'home': str(home)}},
                'triage_recovery': binding}}
            setup = state / 'setup.md'
            setup.write_text('```json\n' + json.dumps(record) + '\n```\n')
            setup.chmod(0o600)
            launcher = b.install(home)
            self.assertEqual(launcher, home / SOURCE)
            self.assertEqual(launcher.stat().st_mode & 0o777, 0o700)
            setup.rename(state / 'audit-only.md')
            for task in ['exact task ID', "-x'; $(touch NEVER)"]:
                result = subprocess.run([str(launcher), task], cwd=root, text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout), ['--db', binding['db'],
                    '--planner-profile', 'fixture-planner', '--task-id=' + task])
            for args in [[], ['one', 'two'], ['']]:
                result = subprocess.run([str(launcher), *args], cwd=root, text=True, capture_output=True)
                self.assertNotEqual(result.returncode, 0)
            self.assertFalse((root / 'NEVER').exists())

    def test_binding_rejects_wrong_profile_and_script(self):
        self.assertTrue((ROOT / 'references/bind_recovery.py').is_file(), 'Maker binder missing')
        import bind_recovery as b
        roles = {'planner': {'id': 'fixture-planner', 'home': '/synthetic/planner'}}
        binding = {'python': '/synthetic/python', 'db': '/synthetic/board.db',
                   'script': '/synthetic/planner/skills/brownfield-feature-planning/scripts/recover_triage.py',
                   'planner_profile': 'fixture-planner'}
        template = (ROOT / SOURCE).read_bytes()
        for bad in [dict(binding, planner_profile='other-team'), dict(binding, script='/other/script'),
                    dict(binding, python='relative'), dict(binding, db='/bad\npath')]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                b.render_launcher(template, bad, roles)


if __name__ == '__main__':
    unittest.main()
