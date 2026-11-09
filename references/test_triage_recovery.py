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
        try:
            native._assert_not_delegated_child_mutation(self.db)
        except PermissionError:
            # Denial tests need only the base fixture, not fenced migrations.
            pass
        else:
            native.init_db(self.db)
        self.conn = sqlite3.connect(self.db)
        self.conn.row_factory = sqlite3.Row
        self.addCleanup(self.conn.close)
        self.conn.executescript(native.SCHEMA_SQL)
        # Isolate optional external lifecycle hooks, never the native DB guard.
        hooks = patch.object(native, '_fire_kanban_lifecycle_hook')
        hooks.start()
        self.addCleanup(hooks.stop)
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

    def execution_fixture(self):
        """Initial synthetic state only; recovery itself always uses native APIs."""
        self.conn.execute('UPDATE tasks SET status = ?, block_kind = NULL, '
                          "block_recurrences = 0, consecutive_failures = 0, "
                          "completion_contract = 'local-only' WHERE id = ?",
                          ('ready', 'target'))
        self.conn.commit()

    def enter_review(self, reviewer='fixture-reviewer'):
        self.execution_fixture()
        coder = native.claim_task(self.conn, 'target', claimer='fixture-coder')
        self.assertIsNotNone(coder)
        self.assertTrue(native.request_review(self.conn, 'target', summary='Candidate checked',
                                              reviewer=reviewer,
                                              expected_run_id=coder.current_run_id))
        claimed = native.claim_review_task(self.conn, 'target', claimer=reviewer)
        self.assertIsNotNone(claimed)
        return claimed.current_run_id

    def test_legacy_active_planner_review_returns_through_its_current_owner(self):
        self.require_native_mutation()
        run = self.enter_review('fixture-planner')
        native.add_comment(self.conn, 'target', 'fixture-planner', 'Legacy clarification answered; Coder continues')
        before = self.row()
        snapshot = list(self.conn.iterdump())
        # A migration/wake context must not reopen the active owner's card.
        self.assertFalse(native.reopen_review_task(self.conn, 'target'))
        self.assertEqual(list(self.conn.iterdump()), snapshot)
        self.assertEqual(native.request_changes(self.conn, 'target', reason='Legacy answer recorded',
                                                expected_run_id=run), (True, 'fixture-coder'))
        after = self.row()
        self.assertEqual(after['status'], 'ready')
        self.assertEqual(after['assignee'], 'fixture-coder')
        self.assertEqual(after['block_recurrences'], before['block_recurrences'])
        self.assertEqual(after['consecutive_failures'], before['consecutive_failures'])
        returned = json.loads(self.conn.execute(
            "SELECT payload FROM task_events WHERE kind = 'changes_requested' ORDER BY id DESC LIMIT 1").fetchone()[0])
        self.assertEqual(returned['reviewer'], 'fixture-planner')
        self.assertEqual(returned['implementer'], 'fixture-coder')
        self.assertEqual(self.row('child')['status'], 'todo')
        self.assertEqual(self.conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0], 2)

    def check_legacy_parked_review_migration(self, triaged):
        self.require_native_mutation()
        run = self.enter_review('fixture-planner')
        handoff = self.conn.execute(
            "SELECT payload FROM task_events WHERE kind = 'review_requested' ORDER BY id DESC LIMIT 1").fetchone()[0]
        attempts = native.BLOCK_RECURRENCE_LIMIT if triaged else 1
        for number in range(1, attempts + 1):
            self.assertTrue(native.block_task(self.conn, 'target', kind='needs_input',
                                             reason=f'Legacy customer question {number}', expected_run_id=run))
            native.add_comment(self.conn, 'target', 'fixture-planner', f'Scoped answer {number}; continue Coder')
            self.assertIsNone(self.row()['current_run_id'])
            if number == native.BLOCK_RECURRENCE_LIMIT:
                self.assertTrue(self.run_recovery()[1]['specified'])
            else:
                self.assertTrue(native.unblock_task(self.conn, 'target'))
            self.assertEqual(self.row()['status'], 'review')
            self.assertEqual(self.row()['assignee'], 'fixture-planner')
            if number < attempts:
                run = native.claim_review_task(self.conn, 'target', claimer='fixture-planner').current_run_id
        # Clarification is resolved and implementation continuation is required.
        # Reopen is not the operation for a still-pending independent verdict.
        before = self.row()
        if triaged:
            self.card('parent', 'blocked')
            self.conn.execute('INSERT INTO task_links VALUES (?, ?)', ('parent', 'target'))
            self.conn.commit()
        self.assertTrue(native.reopen_review_task(self.conn, 'target'))
        after = self.row()
        self.assertEqual(after['status'], 'todo' if triaged else 'ready')
        self.assertEqual(after['assignee'], 'fixture-coder')
        self.assertEqual(after['block_recurrences'], before['block_recurrences'])
        self.assertEqual(after['consecutive_failures'], before['consecutive_failures'])
        self.assertEqual(self.conn.execute(
            "SELECT payload FROM task_events WHERE kind = 'review_requested' ORDER BY id DESC LIMIT 1").fetchone()[0], handoff)
        self.assertEqual(self.row('child')['status'], 'todo')
        comments = [r[0] for r in self.conn.execute('SELECT body FROM task_comments WHERE task_id = ?', ('target',))]
        self.assertIn(f'Scoped answer {attempts}; continue Coder', comments)
        snapshot = list(self.conn.iterdump())
        self.assertFalse(native.reopen_review_task(self.conn, 'target'))
        self.assertEqual(list(self.conn.iterdump()), snapshot)
        if triaged:
            self.assertIsNone(native.claim_task(self.conn, 'target', claimer='fixture-coder'))
        else:
            coder = native.claim_task(self.conn, 'target', claimer='fixture-coder')
            self.assertTrue(native.request_review(self.conn, 'target', summary='Candidate after legacy clarification',
                                                 reviewer='fixture-reviewer', expected_run_id=coder.current_run_id))
            self.assertEqual(self.row()['assignee'], 'fixture-reviewer')
            self.assertEqual(self.row()['status'], 'review')

    def test_legacy_parked_blocked_review_reopens_original_coder_then_independent_reviewer(self):
        self.check_legacy_parked_review_migration(False)

    def test_legacy_parked_triage_review_restores_source_phase_before_gated_reopen(self):
        self.check_legacy_parked_review_migration(True)

    def test_distinct_needs_input_questions_recur_to_same_card_triage(self):
        self.require_native_mutation()
        self.execution_fixture()
        # The native limit is protection, not a discretionary work budget.
        for number in range(1, native.BLOCK_RECURRENCE_LIMIT + 1):
            question = f'Distinct customer decision {number}'
            native.add_comment(self.conn, 'target', 'fixture-coder', question)
            self.assertTrue(native.block_task(self.conn, 'target', kind='needs_input', reason=question))
            row = self.row()
            self.assertEqual(row['block_recurrences'], number)
            self.assertEqual(row['assignee'], 'fixture-coder')
            self.assertEqual(row['status'], 'triage' if number == native.BLOCK_RECURRENCE_LIMIT else 'blocked')
            native.add_comment(self.conn, 'target', 'fixture-planner', f'Answer to decision {number}')
            if row['status'] == 'blocked':
                self.assertTrue(native.unblock_task(self.conn, 'target'))
        before = self.row()
        self.assertFalse(native.unblock_task(self.conn, 'target'))
        self.assertTrue(self.run_recovery()[1]['specified'])
        self.assertEqual(self.row(), dict(before, status='ready'))
        self.assertEqual(self.row('child')['status'], 'todo')
        self.assertEqual(self.conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0], 2)
        comments = [r['body'] for r in self.conn.execute('SELECT body FROM task_comments WHERE task_id = ? ORDER BY id', ('target',))]
        self.assertIn('Distinct customer decision 1', comments)
        self.assertIn(f'Answer to decision {native.BLOCK_RECURRENCE_LIMIT}', comments)
        snapshot = list(self.conn.iterdump())
        with self.assertRaisesRegex(RuntimeError, 'Reinspect'):
            self.run_recovery()
        self.assertEqual(list(self.conn.iterdump()), snapshot)

    def test_reviewer_question_customer_answer_returns_coder_then_review(self):
        self.require_native_mutation()
        review_run = self.enter_review()
        native.add_comment(self.conn, 'target', 'fixture-reviewer', 'Clarify accepted behavior; not a proven defect')
        self.assertEqual(native.request_changes(self.conn, 'target', reason='Question on accepted behavior',
                                                expected_run_id=review_run), (True, 'fixture-coder'))
        coder = native.claim_task(self.conn, 'target', claimer='fixture-coder')
        self.assertIsNotNone(coder)
        self.assertTrue(native.block_task(self.conn, 'target', kind='needs_input', reason='Customer choice',
                                         expected_run_id=coder.current_run_id))
        native.add_comment(self.conn, 'target', 'fixture-planner', 'Sufficient scoped answer; continue')
        self.assertEqual(self.row()['assignee'], 'fixture-coder')
        self.assertTrue(native.unblock_task(self.conn, 'target'))
        self.assertEqual(self.row()['status'], 'ready')
        coder = native.claim_task(self.conn, 'target', claimer='fixture-coder')
        self.assertIsNotNone(coder)
        self.assertTrue(native.request_review(self.conn, 'target', summary='Explanation resolves question; same candidate',
                                             expected_run_id=coder.current_run_id))
        self.assertEqual(self.row()['status'], 'review')
        self.assertEqual(self.row()['assignee'], 'fixture-reviewer')
        self.assertEqual(self.row('child')['status'], 'todo')
        self.assertEqual(self.conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0], 2)

    def test_request_changes_reapplies_parent_gate_and_rejects_stale_owner(self):
        self.require_native_mutation()
        review_run = self.enter_review()
        snapshot = list(self.conn.iterdump())
        ok, reason = native.request_changes(self.conn, 'target', reason='Question', expected_run_id=review_run + 1)
        self.assertFalse(ok)
        self.assertIn('run_id mismatch', reason)
        self.assertEqual(list(self.conn.iterdump()), snapshot)
        # New upstream prerequisite is fixture input, not recovery bypass.
        self.card('parent', 'blocked')
        self.conn.execute('INSERT INTO task_links VALUES (?, ?)', ('parent', 'target'))
        self.conn.commit()
        self.assertEqual(native.request_changes(self.conn, 'target', reason='Question', expected_run_id=review_run),
                         (True, 'fixture-coder'))
        self.assertEqual(self.row()['status'], 'todo')
        self.assertIsNone(native.claim_task(self.conn, 'target', claimer='fixture-coder'))

    def test_ordinary_unblock_preserves_block_counter_and_native_failure_reset(self):
        self.require_native_mutation()
        self.execution_fixture()
        self.assertTrue(native.block_task(self.conn, 'target', kind='needs_input', reason='Actual question'))
        # Synthetic preexisting failure evidence; unblock owns the reset.
        self.conn.execute('UPDATE tasks SET consecutive_failures = 3 WHERE id = ?', ('target',))
        self.conn.commit()
        before = self.row()
        self.assertTrue(native.unblock_task(self.conn, 'target'))
        after = self.row()
        self.assertEqual(after['consecutive_failures'], 0)
        self.assertEqual(after['block_recurrences'], before['block_recurrences'])
        self.assertEqual(after['block_kind'], 'needs_input')
        self.assertEqual(after['assignee'], 'fixture-coder')

    def test_ordinary_unblock_respects_parent_and_duplicate_transition(self):
        self.require_native_mutation()
        self.execution_fixture()
        self.assertTrue(native.block_task(self.conn, 'target', kind='needs_input', reason='Question'))
        self.card('parent', 'blocked')
        self.conn.execute('INSERT INTO task_links VALUES (?, ?)', ('parent', 'target'))
        self.conn.commit()
        self.assertTrue(native.unblock_task(self.conn, 'target'))
        self.assertEqual(self.row()['status'], 'todo')
        snapshot = list(self.conn.iterdump())
        self.assertFalse(native.unblock_task(self.conn, 'target'))
        self.assertEqual(list(self.conn.iterdump()), snapshot)

    def check_review_interruption(self, recover_triage):
        self.require_native_mutation()
        review_run = self.enter_review()
        attempts = native.BLOCK_RECURRENCE_LIMIT if recover_triage else 1
        for number in range(1, attempts + 1):
            self.assertTrue(native.block_task(self.conn, 'target', kind='capability',
                                             reason=f'Review capability interruption {number}',
                                             expected_run_id=review_run))
            if self.row()['status'] == 'triage':
                self.assertTrue(self.run_recovery()[1]['specified'])
            else:
                self.assertTrue(native.unblock_task(self.conn, 'target'))
            self.assertEqual(self.row()['status'], 'review')
            self.assertEqual(self.row()['assignee'], 'fixture-reviewer')
            resumed = native.claim_review_task(self.conn, 'target', claimer='fixture-reviewer')
            self.assertIsNotNone(resumed)
            review_run = resumed.current_run_id
        handoff = json.loads(self.conn.execute(
            'SELECT payload FROM task_events WHERE task_id = ? AND kind = ? ORDER BY id DESC LIMIT 1',
            ('target', 'review_requested')).fetchone()[0])
        self.assertEqual(handoff['implementer'], 'fixture-coder')
        self.assertEqual(handoff['reviewer'], 'fixture-reviewer')
        self.assertEqual(self.conn.execute('SELECT COUNT(*) FROM task_events WHERE kind = ?',
                                           ('changes_requested',)).fetchone()[0], 0)

    def test_technical_review_interruption_restores_review_and_provenance(self):
        self.check_review_interruption(False)

    def test_triaged_review_interruption_restores_review_and_provenance(self):
        self.check_review_interruption(True)

    def test_active_claim_and_done_are_not_recovered_again(self):
        self.require_native_mutation()
        review_run = self.enter_review()
        snapshot = list(self.conn.iterdump())
        with self.assertRaisesRegex(RuntimeError, 'Reinspect'):
            self.run_recovery()
        self.assertFalse(native.unblock_task(self.conn, 'target'))
        self.assertEqual(list(self.conn.iterdump()), snapshot)
        metadata = {'review_outcome': 'approved', 'reviewer_checks': ['synthetic state checks'],
                    'reviewed_commit': 'a' * 40}
        self.assertTrue(native.complete_task(self.conn, 'target', summary='Exact candidate approved',
                                            metadata=metadata, expected_run_id=review_run))
        self.assertEqual(self.row()['status'], 'done')
        self.assertEqual(self.row('child')['status'], 'ready')
        run = self.conn.execute('SELECT metadata FROM task_runs WHERE id = ?', (review_run,)).fetchone()
        self.assertEqual(json.loads(run[0]), metadata)
        snapshot = list(self.conn.iterdump())
        with self.assertRaisesRegex(RuntimeError, 'Reinspect'):
            self.run_recovery()
        self.assertFalse(native.unblock_task(self.conn, 'target'))
        self.assertIsNone(native.claim_task(self.conn, 'target', claimer='fixture-coder'))
        self.assertEqual(list(self.conn.iterdump()), snapshot)


if __name__ == '__main__':
    unittest.main()
