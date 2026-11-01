"""Recover one triage card after the reference's approval and API checks."""
import argparse
import inspect
import json
from pathlib import Path
import sqlite3


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', required=True, type=Path, help='Confirmed existing board DB')
    parser.add_argument('--task-id', required=True, help='Exact runtime card ID')
    parser.add_argument('--planner-profile', required=True, help='Confirmed technical planner profile ID')
    args = parser.parse_args(argv)
    if not args.task_id.strip() or not args.planner_profile.strip():
        parser.error('Task ID and planner profile cannot be blank')

    from hermes_cli.kanban_db import specify_triage_task

    # A matching signature does not prove semantics. Inspect the installed source
    # and recompute_ready as required by the reference before using this fallback.
    parameters = list(inspect.signature(specify_triage_task).parameters.values())
    expected = [('conn', inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.empty),
                ('task_id', inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.empty)]
    expected += [(name, inspect.Parameter.KEYWORD_ONLY, None)
                 for name in ('title', 'body', 'assignee', 'author')]
    if [(p.name, p.kind, p.default) for p in parameters] != expected:
        raise RuntimeError('Native API signature changed; inspect the installed implementation')

    board_db = args.db.resolve(strict=True)
    conn = sqlite3.connect(board_db.as_uri() + '?mode=rw', uri=True)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            'SELECT id, status, current_run_id FROM tasks WHERE id = ?',
            (args.task_id,),
        ).fetchone()
        if row is None or row['status'] != 'triage' or row['current_run_id'] is not None:
            raise RuntimeError('Reinspect state/claim before recovery')
        changed = specify_triage_task(conn, args.task_id, author=args.planner_profile)
        actual = conn.execute(
            'SELECT id, status, assignee, current_run_id FROM tasks WHERE id = ?',
            (args.task_id,),
        ).fetchone()
        print(json.dumps({'specified': changed, 'task': dict(actual) if actual else None}))
        return 0 if changed else 1
    finally:
        conn.close()


if __name__ == '__main__':
    raise SystemExit(main())
