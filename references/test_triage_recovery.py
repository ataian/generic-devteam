"""One-card recovery contracts using synthetic SQLite boards only."""
import contextlib
import importlib.util
import inspect
from typing import Any
import io
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

try:
    from hermes_cli import kanban_db as installed_native
    native: Any = installed_native
except ImportError:
    native = None

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/brownfield-feature-planning/scripts/recover_triage.py'


@unittest.skipIf(native is None, 'Installed Hermes Python required for native recovery tests')
class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.is_file(), 'Ship the reusable recovery script')
        assert native is not None
        spec = importlib.util.spec_from_file_location('recover_triage', SCRIPT)
        assert spec is not None and spec.loader is not None
        self.recovery = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.recovery)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name) / 'synthetic.db'
        self.conn = sqlite3.connect(self.db)
        self.conn.row_factory = sqlite3.Row
        self.addCleanup(self.conn.close)
        self.conn.executescript(native.SCHEMA_SQL)
        self.card('target', 'triage')
        self.card('child', 'todo')
        self.conn.execute('INSERT INTO task_links VALUES (?, ?)', ('target', 'child'))
        self.conn.commit()

    def card(self, task, status, run=None):
        self.conn.execute('INSERT INTO tasks (id, title, body, assignee, status, created_at, '
                          'current_run_id, consecutive_failures, block_kind, block_recurrences) '
                          'VALUES (?, ?, ?, ?, ?, 1, ?, 3, ?, 2)',
                          (task, 'Exact title', 'Exact body', 'fixture-coder', status, run, 'capability'))
        self.conn.commit()

    def row(self, task='target'):
        return dict(self.conn.execute('SELECT * FROM tasks WHERE id = ?', (task,)).fetchone())

    def run_recovery(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = self.recovery.main(['--db', str(self.db), '--task-id', 'target',
                                         '--planner-profile', 'fixture-planner'])
        return result, json.loads(output.getvalue())

    def require_native_mutation(self):
        try:
            native._assert_not_delegated_child_mutation(self.db)
        except PermissionError as error:
            self.skipTest(str(error))

    def test_native_transition_preserves_spec_counters_and_child_gate(self):
        self.require_native_mutation()
        before = self.row()
        code, output = self.run_recovery()
        self.assertEqual(code, 0)
        self.assertTrue(output['specified'])
        self.assertEqual(output['task'], {'id': 'target', 'status': 'ready',
                                          'assignee': 'fixture-coder', 'current_run_id': None})
        after = self.row()
        self.assertEqual(after, dict(before, status='ready'))
        self.assertEqual(self.row('child')['status'], 'todo')
        self.assertEqual(self.conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0], 2)
        self.assertEqual(self.conn.execute('SELECT COUNT(*) FROM task_runs').fetchone()[0], 0)
        self.assertEqual(self.conn.execute('SELECT COUNT(*) FROM task_events WHERE kind = ?',
                                           ('specified',)).fetchone()[0], 1)

    def test_parent_keeps_recovered_card_in_todo(self):
        self.require_native_mutation()
        self.card('parent', 'blocked')
        self.conn.execute('INSERT INTO task_links VALUES (?, ?)', ('parent', 'target'))
        self.conn.commit()
        self.assertEqual(self.run_recovery()[1]['task']['status'], 'todo')

    def test_review_provenance_is_read_back_without_reopening(self):
        self.require_native_mutation()
        self.conn.execute('INSERT INTO task_events (task_id, kind, payload, created_at) VALUES (?, ?, ?, 1)',
                          ('target', 'block_loop_detected', '{"resume_status":"review"}'))
        self.conn.commit()
        self.assertEqual(self.run_recovery()[1]['task']['status'], 'review')
        self.assertEqual(self.row()['assignee'], 'fixture-coder')

    def test_recomputation_can_advance_other_eligible_cards(self):
        self.require_native_mutation()
        self.card('other', 'todo')
        self.run_recovery()
        self.assertEqual(self.row('other')['status'], 'ready')

    def test_missing_nontriage_and_active_run_refuse_without_mutation(self):
        for status, run in [('ready', None), ('triage', 7)]:
            with self.subTest(status=status, run=run):
                self.conn.execute('UPDATE tasks SET status = ?, current_run_id = ? WHERE id = ?',
                                  (status, run, 'target'))
                self.conn.commit()
                before = self.conn.iterdump()
                before = list(before)
                with self.assertRaisesRegex(RuntimeError, 'Reinspect'):
                    self.run_recovery()
                self.assertEqual(list(self.conn.iterdump()), before)
        self.conn.execute('DELETE FROM tasks WHERE id = ?', ('target',))
        self.conn.commit()
        with self.assertRaisesRegex(RuntimeError, 'Reinspect'):
            self.run_recovery()

    def test_wrong_path_does_not_create_database(self):
        self.db = self.db.parent / 'missing.db'
        with self.assertRaises(FileNotFoundError):
            self.run_recovery()
        self.assertFalse(self.db.exists())

    def test_native_denial_propagates_without_sql_fallback(self):
        before = self.row()
        signature = inspect.signature(native.specify_triage_task)
        with patch.object(native, 'specify_triage_task', side_effect=PermissionError('guard denied')) as denied:
            # Keep the actual signature when simulating an execution guard.
            denied.__signature__ = signature
            with self.assertRaisesRegex(PermissionError, 'guard denied'):
                self.run_recovery()
        self.assertEqual(self.row(), before)

    def test_delegation_guard_denial_leaves_synthetic_board_unchanged(self):
        try:
            native._assert_not_delegated_child_mutation(self.db)
        except PermissionError:
            before = list(self.conn.iterdump())
            with self.assertRaisesRegex(PermissionError, 'delegate_task child contexts'):
                self.run_recovery()
            self.assertEqual(list(self.conn.iterdump()), before)
        else:
            self.skipTest('No delegation fence in this process')

    def test_signature_drift_refuses_before_transition(self):
        def incompatible(conn, task_id, *, force=False):
            raise AssertionError('Do not call a changed API')
        with patch.object(native, 'specify_triage_task', incompatible):
            with self.assertRaisesRegex(RuntimeError, 'signature'):
                self.run_recovery()
        self.assertEqual(self.row()['status'], 'triage')

    def test_cli_uses_explicit_db_despite_inherited_board_override(self):
        self.require_native_mutation()
        import os
        wrong = self.db.parent / 'wrong.db'
        result = subprocess.run([sys.executable, '-B', str(SCRIPT), '--db', str(self.db),
                                 '--task-id', 'target', '--planner-profile', 'fixture-planner'],
                                env=dict(os.environ, HERMES_KANBAN_DB=str(wrong)),
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['task']['status'], 'ready')
        self.assertFalse(wrong.exists())


if __name__ == '__main__':
    unittest.main()
