# Recover an existing Kanban card from automatic triage

Use when a planner has resolved a repeated block but `unblock` / `promote`
refuse the existing `triage` card. This is operational recovery, not a request
for a new specification, decomposition, replacement ticket or new approval.

## Decision before transition

1. Read the exact board/card, full latest blocker and decision thread, parents,
   children, latest runs and claim. Identify `block_loop_detected`, its `kind`
   and recurrence count. Distinguish automatic triage from intentionally
   unspecific work awaiting planning. Inspect only the relevant dependencies.
2. Establish that the concrete cause is resolved and required approval actually
   covers the next operation. Make routine technical decisions within the
   planner's existing mandate. Do not claim that a customer approved something
   that only the planner decided. Recovery grants no new execution permission.
3. Preserve the same card, scope, history, valid dependencies and review verdict.
   Record the resolution, supporting evidence, remaining work and intended next
   owner as a comment. Explicitly supersede contradictory old instructions;
   update an actively contradictory body through the supported edit operation.
4. Confirm no active worker/claim owns this card. If another session is handling
   it, coordinate through its comment thread instead of racing its transition.
   Do not reclaim or kill a worker merely to make this procedure applicable.
5. Confirm the exact installation/interpreter, profile home and board DB used
   by the actual dispatcher. An inherited `HERMES_KANBAN_DB` can pin another
   board even when a board name is supplied. A board name alone is insufficient
   evidence. Do not access another team's DB or copy private data without scope.

If permission, cause, graph ownership or board identity remains unresolved,
report that specific gap. Do not report triage itself as an unfixable state or
make the customer drag the card merely because the common CLI verbs refuse it.

## Supported transition, then internal fallback

Inspect the installed CLI help / native tools first. Prefer a supported public
operation that preserves the existing spec and dependency gates. The CLI
`specify` may invoke an auxiliary LLM and rewrite the assignment; it is NOT the
same operation as the deterministic internal function below. Do not run
`decompose` to recover a fully specified card.

In the verified Hermes implementation, the fallback is:

```python
from hermes_cli.kanban_db import specify_triage_task
changed = specify_triage_task(conn, task_id, author=planner_profile)
```

Use **no** `title`, `body` or `assignee` overrides. This changes `triage -> todo`
and calls native dependency recomputation. Recompute scans eligible cards on
that board, not just this card; other already-unblocked dependency waits may
advance as they would on the next dispatcher tick. Inspect the relevant board
state before and after the operation. It records `specified`; it does not
create a card, invoke an LLM or clear failure/block counters. `False` means the
card is no longer in triage: reread it, do not force a write.

This is an internal, version-sensitive API, not a stable public command.
Before use inspect its current signature/source and `recompute_ready` behavior
in the actual installed Hermes. Stop if semantics differ; never patch Hermes,
invent a function, issue raw SQL UPDATEs or install another Hermes to get it.

### Concrete invocation after the checks above

Use the verified Hermes Python, not an unrelated system Python. Replace these
three values with the confirmed DB path, exact task ID and planner profile.
The following is a one-card operation, not a bulk recovery loop:

```python
import sqlite3
from pathlib import Path
from hermes_cli.kanban_db import specify_triage_task

board_db = Path('/confirmed/board/kanban.db').resolve(strict=True)
task_id = 't_exact_id'
planner_profile = 'actual-planner-profile'
conn = sqlite3.connect(board_db.as_uri() + '?mode=rw', uri=True)
conn.row_factory = sqlite3.Row
try:
    row = conn.execute(
        'SELECT id, status, current_run_id FROM tasks WHERE id = ?',
        (task_id,),
    ).fetchone()
    if row is None or row['status'] != 'triage' or row['current_run_id'] is not None:
        raise RuntimeError('Reinspect state/claim before recovery')
    changed = specify_triage_task(conn, task_id, author=planner_profile)
    print('specified:', changed)
    print(dict(conn.execute(
        'SELECT id, status, assignee, current_run_id FROM tasks WHERE id = ?',
        (task_id,),
    ).fetchone()))
finally:
    conn.close()
```

`mode=rw` prevents silently creating an empty DB at a wrong path. SQL here is
read-only inspection; mutation is exclusively through the native transition.
The preliminary read is not a cross-session lock: arrange a single recovery
owner, recheck state immediately and rely on the native status guard. Do not
advertise the example as an atomic multi-condition capability boundary.

## Read back the actual landing state

- `todo`: check unsatisfied parents; do not remove valid gates.
- `ready`: queued for the normal gateway dispatcher, NOT running yet.
- `review`: dependency recomputation can restore prior review provenance. Read
  the last `review_requested` implementer/reviewer and latest verdict before
  choosing a next step. A review verdict must never be bypassed.
- `running` or a new active claim: another owner already took over; stop recovery
  writes and let that owner continue.

### Review-provenance special case

If a genuine active review run owns the card, its owner uses normal
`kanban_request_changes` for a changes-requested verdict or answered planner
question. A wake session must not compete with it.

If the card has landed in `review` **without an active review run**, the ordinary
request-changes operation can refuse with `not in an active review run`. After
checking the prior handoff and confirming rework/continuation rather than pending
review acceptance, the native public `hermes kanban --board <board>
reopen-review <task>` returns it to `ready`/`todo`. Inspect local help first.
The corresponding internal function is `reopen_review_task(conn, task_id)`;
use it only with the same version/identity checks if no equivalent public
operation is usable. It restores the implementer from `review_requested`, which
may be the coder OR the planner/operator, not necessarily the current assignee.
Read back that assignee. Never hardcode a coder or route past an unresolved
CHANGES_REQUESTED verdict. Do not reopen a pending review simply to execute code.

## Preserved circuit breaker and verification

- Recurrence accounting and consecutive failures remain. Another same-kind block
  can immediately return the card to triage. Fix the cause; no retries in a loop,
  fake completion, reset counter, block-kind rotation or replacement card to evade it.
- `auto_decompose: false` prevents automatic fan-out, NOT entry into triage. Do
  not change central gateway configuration as part of this recovery. Existing
  auto-generated children must be inspected, not silently removed or counted done.
- Read back spec/assignee, parents/children and transition events. Verify descendants
  stay gated. A transition is neither review approval nor completed implementation.
- Leave startup to the gateway dispatcher: no manual `dispatch`, new watcher,
  restart or parallel worker. Claim/run evidence is required before saying running.
- If a guard denies DB access/execution, report that capability failure; this API
  is not permission to bypass the guard. Keep customer approval, board transition,
  low-level execution approval and verified outcome distinct.

## Package versus live rollout

The Maker ships this file inside the planner's complete
`brownfield-feature-planning` skill tree. Existing planners do not update merely
because the Maker changed. Inventory the actual team/version/skill edits and
obtain a scoped rollout instruction before modifying existing profile copies or
SOULs. No kernel patch or SOUL expansion is needed to teach this technique.
