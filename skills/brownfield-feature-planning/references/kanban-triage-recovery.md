# Safe Kanban resumption and triage recovery

Use this reference after a resolved blocker or interrupted run.
Use the internal triage fallback only under its additional checks below.
Recovery grants no new execution permission.
Preserve the existing card, authorized scope, history, valid dependencies, review provenance and counters.
Leave implementation and independent review with their assigned owners.
Do not bypass guards, weaken runtime policies or manually dispatch workers.

## Resume after a blocker or interrupted run

1. Read the exact task, full blocker/decision thread, parents, children, latest runs and claim.
2. Use [status inspection](kanban-status-inspection.md) if the failure boundary remains unclear.
3. Require resolution of the actual blocker and approval covering the next operation.
4. Verify required artifacts and results against original task/run records.
5. Verify that the next execution context can perform its remaining operations.
6. Do not transfer capability or approval evidence from another session.
7. Keep the task blocked and descendants gated while a prerequisite remains unresolved.
8. If another session owns a claim or retry, coordinate through its thread instead of racing it.
9. Require an ended previous writer and no parallel repository writer before continuation.
10. Inspect HEAD, `git status --short` and `git diff --check` before defining remaining work.
11. Preserve completed commits, partial changes, unrelated files and historical observations.
12. Record the repaired boundary, evidence, intended owner, remaining file/verification/commit/review work and unchanged exclusions on the existing card.
13. If only handoff or reporting is missing, exclude reimplementation and duplicate commits explicitly.
14. Replace contradictory active body instructions through the supported edit operation.
15. If an ambiguous instruction caused the block, clarify that assignment instead of rebuilding completed coordination work.
16. Reference completed prerequisite cards and final results for reuse by the returning worker.
17. Read back the body and resumption comment before release.
18. From the authorized orchestrator context, use `kanban_unblock(task_id=..., board=...)` only after the blocker is resolved, required parents are satisfied and no active target run remains.
19. Read back the target, unchanged valid parents and still-gated later phases without active runs.
20. Distinguish returned `ready` from a later dispatcher claim with a new intended-profile run.
21. Use the native transition as the release record.
22. Add missing readback evidence to the same card and verify the comment.
23. Report continuation as progress, not proof of repaired execution or completed acceptance.

If ordinary release refuses an automatically triaged card, use the fallback below.
If scope or graph changes are needed, use [approved phase changes](kanban-phase-release.md#amend-an-approved-graph).
Do not recreate tasks or reclassify unresolved capability/security blocks to enable release.

### Resume a blocked card after coordinator acknowledgment

Use this branch only after the existing acknowledgment completes and resolves the original blocker.
Do not treat an active acknowledgment or unresolved execution/security denial as clearance.

1. Read its complete report, original completed run and terminal event.
2. Require the intended owner and fulfilled result contract.
3. Do not make the returning worker gain coordinator privileges or repeat completed subscription/graph probes.
4. Verify process exit separately from `ended_at` or board `done`.
5. Obtain PID and process-start identity from the exact original spawn record.
6. Inspect `ps -p <verified-pid> -o pid,ppid,stat,etime,comm` and relevant children with `ps --ppid <verified-pid> -o pid,ppid,stat,etime,comm`.
7. If PID reuse is possible, compare the recorded start identity before identifying the worker.
8. If handoff requires termination, use only a supported bounded foreground process check.
9. Do not kill or reclaim completed work to end its epilogue.
10. Do not manufacture polling of delegated work whose result requires ending the turn.
11. Re-read the final report after exit to include late completion-event evidence.
12. Verify the exact task, run, checked artifact and result against those final records.
13. Apply the ordinary resumption checks before releasing the existing target.

## Decision before transition

Use this triage branch when repeated blocking moved a specified card to `triage` and ordinary `unblock` or `promote` refuses it.
Treat automatic triage as an error state, not a normal planning step.
Do not request specifications, decomposition, replacement tickets or approval solely because of triage.
Obtain missing approval for the actual next operation.

1. Identify `block_loop_detected`, its `kind` and recurrence count in the complete current thread.
2. Distinguish automatic triage from intentionally unspecific work awaiting planning.
3. Inspect relevant dependencies under the ordinary resumption checks.
4. Resolve routine technical decisions within the planner's existing mandate.
5. Do not attribute planner decisions to customer approval.
6. Confirm no active worker or claim owns the card.
7. Do not reclaim or kill a worker merely to qualify for recovery.
8. Verify the dispatcher's actual installation, interpreter, profile home and board database.
9. Check inherited `HERMES_KANBAN_DB` because a board name alone does not establish database identity.
10. Do not access another team's database or copy private data outside scope.
11. Re-read task and relevant graph immediately before transition to detect concurrent changes.
12. Inspect auto-generated children and their claims, runs and dependencies before acting.
13. Route unsafe graph reconciliation to the authorized operator rather than deleting protective gates.

Report any unresolved permission, cause, ownership or identity gap specifically.
Do not declare triage unfixable or require the owner to drag a card merely because common CLI verbs refuse it.

## Supported transition, then internal fallback

Inspect installed native tools and CLI help first.
Prefer a public operation that preserves specification and dependency gates.
Do not equate CLI `specify` with the deterministic fallback because it may invoke an auxiliary LLM and rewrite the assignment.
Do not run `decompose` to recover specified work.

If no suitable public transition is usable, inspect installed source before using `specify_triage_task(conn, task_id, author=planner_profile)`.
Require the exact parameter order, kinds and defaults represented by `specify_triage_task(conn, task_id, *, title=None, body=None, assignee=None, author=None)`.
Inspect `recompute_ready` semantics because signature equality alone is insufficient.
Stop if installed behavior differs from the contract below.
Do not patch Hermes, invent APIs, issue raw SQL updates or install another Hermes for recovery.

Call the fallback without `title`, `body` or `assignee` overrides.
It changes `triage` to `todo` and invokes native dependency recomputation.
Recomputation scans eligible board cards and can advance other already-unblocked dependency waits.
The operation records `specified` without creating cards, invoking an LLM or clearing failure/block counters.
Inspect relevant board state before and after transition.
If it returns `False`, re-read the card rather than forcing a write because it is no longer in triage.

### Concrete invocation after the checks above

Run the installed [bound launcher](../scripts/recover-triage) from the installed skill directory.
Pass the exact task ID as the only argument.
Process one card at a time.

```sh
./scripts/recover-triage "$TASK_ID"
```

The launcher invokes the shipped [recovery script](../scripts/recover_triage.py) with fixed team bindings.
It needs no setup record or runtime configuration file.
If missing or unbound, report the installation failure to the Maker/operator.
Do not collect binding variables or generate configuration during recovery.
Complete operation, identity and installed-source checks before invocation.
The script rejects signature drift but does not prove semantic equivalence.
Its `mode=rw` prevents creating an empty database at a wrong path.
Its SQL only reads; mutation uses the native transition.
Arrange one recovery owner because the preliminary read is not a cross-session lock.
Recheck state immediately and rely on the native status guard.
Do not claim an atomic multi-condition capability boundary.
Read `specified` and actual `task` state from the JSON output.
Treat exit code 0 as transition success, not worker startup or completion.

## Read back the actual landing state

- If the card is `todo`, inspect unsatisfied parents without removing valid gates.
- If the card is `ready`, report queued work rather than running work.
- If the card is `review`, inspect the last `review_requested` implementer/reviewer and latest verdict.
- If the card is `running` or newly claimed, stop recovery writes.
- Leave a newly claimed card with its current owner.

### Review-provenance special case

If an active review run owns the card, leave normal `kanban_request_changes` to that owner for a changes-requested verdict or answered planner question.
Do not let a wake session compete with the reviewer.
Without an active review run, request-changes can refuse with `not in an active review run`.
Before reopening, confirm prior handoff and required rework/continuation rather than pending review acceptance.
Inspect local help before using `hermes kanban --board <board> reopen-review <task>` to return the card to `ready`/`todo`.
If no equivalent public operation is usable, use `reopen_review_task(conn, task_id)` only after the same version/identity checks.
Read back the implementer restored from `review_requested`, which may be the coder or planner/operator.
Do not hardcode a coder or bypass an unresolved `CHANGES_REQUESTED` verdict.
Do not reopen pending review merely to execute code.

## Preserved circuit breaker and verification

Another same-kind block can immediately return the card to triage.
Fix the cause instead of looping retries, faking completion, resetting counters, rotating block kinds or replacing cards.
Treat `auto_decompose: false` as preventing fan-out, not entry into triage.
Do not change central gateway configuration during recovery.
Do not silently delete auto-generated children or count them done.
Read back specification, assignee, parents, children and transition events.
Verify that descendants remain gated.
Do not treat a transition as review approval or completed implementation.
Leave startup to the gateway dispatcher without a new watcher, restart or parallel worker.
Require claim/run evidence before reporting `running`.
If a guard denies database access or execution, report that capability failure.
Keep customer approval, board transition, low-level execution approval and verified outcome distinct.
