# Safe Kanban resumption and triage recovery

Use after a resolved blocker or interrupted run.
Apply the additional checks below before internal triage recovery.
Recovery grants no new permission.
Preserve the existing card, authorized scope, history, valid dependencies, review provenance and counters.
Preserve native counter semantics, including resets performed by legitimate native transitions.
Keep assigned implementation/review owners and native guards/runtime policies.
Leave dispatch to the dispatcher.

Triage means blocked work in this team; never deliberately send work there.
Check an actual Coder escalation for an overlooked in-scope solution before involving the customer.
Record the correction and resume the Coder without a customer round.
Otherwise coordinate permitted recovery or obtain the missing decision in Mattermost.
Record a sufficient customer answer and its scope on the existing ticket.
Amend the versioned plan and affected ticket bindings before release when required.
Use `kanban_comment(task_id=..., body=...)` and read back the posted decision before resumption.
Resume on a sufficient answer without another start request.
A Mattermost wake is not an active Reviewer run; use ordinary unblock or guarded triage recovery instead of request-changes.
Keep capability failures and verified quota pauses blocked until their actual cause is resolved.
Verify quota reset information before authorized native one-time resumption.

## Resume after a blocker or interrupted run

1. Read the exact task, full blocker/decision thread, parents, children, latest runs and claim.
   Match answer scope, blocker, and run. An old answer must not clear a newer blocker.
   Leave an already-active or completed task unchanged.
2. Use [status inspection](kanban-status-inspection.md) for an unclear failure boundary.
3. Require blocker resolution and authority for the next operation.
4. Verify artifacts and results against original task/run records.
5. Verify the returning context's capabilities and permissions.
6. Keep session-specific capability and approval evidence separate.
7. Keep unresolved work blocked and descendants gated.
8. Coordinate existing claims/retries through their owner's thread.
9. Require an ended previous writer and no parallel repository writer before continuation.
10. Inspect HEAD, `git status --short` and `git diff --check` before defining remaining work.
11. Preserve completed commits, partial changes, unrelated files and historical observations.
12. Record the repaired boundary, evidence, intended owner, remaining file/verification/commit/review work and unchanged exclusions on the existing card.
13. For handoff/reporting-only work, exclude reimplementation and duplicate commits.
14. Replace contradictory active body instructions through the supported edit operation.
15. Clarify ambiguous assignments instead of repeating completed coordination.
16. Reference completed prerequisites and final results for reuse.
17. Read back the body and resumption comment before release.
18. Use `kanban_unblock(task_id=..., board=...)` from the authorized orchestrator after resolution, satisfied parents, and ended target runs.
19. Read back recipient, source phase, valid parents, and gated later phases without runs.
    Verify baseline adoption separately from queued or started status.
20. Report `ready` until a new intended-profile dispatcher claim.
21. Use the native transition as the release record.
22. Add missing readback evidence to the same card and verify the comment.
23. Report continuation, not repaired execution or acceptance.

For refused automatic-triage release, use the fallback below.
Use [approved phase changes](kanban-phase-release.md#amend-an-approved-graph) for scope/graph changes.
Preserve cards and unresolved capability/security block kinds.

### Resume a blocked card after coordinator acknowledgment

Require completed acknowledgment that resolves the original blocker.
Keep unresolved execution/security denials blocked.

1. Read the complete report, original run, and terminal event.
2. Verify owner and fulfilled result contract.
3. Preserve worker privileges and completed subscription/graph checks.
4. Verify process exit separately from `ended_at` or board `done`.
5. Obtain PID and process-start identity from the exact original spawn record.
6. Inspect `ps -p <verified-pid> -o pid,ppid,stat,etime,comm` and relevant children with `ps --ppid <verified-pid> -o pid,ppid,stat,etime,comm`.
7. Check recorded start identity against possible PID reuse.
8. For exit-dependent handoff, use a supported bounded foreground check.
9. Do not kill or reclaim completed work to end its epilogue.
10. End the turn for delegated results instead of polling.
11. Re-read the final report after exit for late events.
12. Verify task, run, artifact, and result against final records.
13. Apply ordinary resumption checks before release.

## Decision before transition

Use this branch for repeated-block `triage` when ordinary `unblock` or `promote` refuses it.
Do not request specifications, decomposition, replacement tickets or approval solely because of triage.

1. Identify `block_loop_detected`, its `kind` and recurrence count in the complete current thread.
2. Match the current answer to the blocker, including distinct same-kind questions.
3. Inspect relevant dependencies under the ordinary resumption checks.
4. Screen the escalation as described above.
5. Attribute the correction or customer answer to its actual source.
6. Confirm no active worker or claim owns the card.
7. Do not reclaim or kill a worker merely to qualify for recovery.
8. Verify dispatcher installation, interpreter, profile home, and database.
9. Check inherited `HERMES_KANBAN_DB`; board names do not prove database identity.
10. Keep other teams' databases and private data outside scope.
11. Re-read the task and graph immediately before transition for concurrent changes.
12. Inspect generated children, claims, runs, and dependencies.
13. Route unsafe graph changes to the operator; preserve protective gates.

Report unresolved permission, cause, ownership, or identity gaps.
Inspect recovery options before declaring triage unfixable or requesting a manual drag.

## Supported transition, then internal fallback

Inspect installed native tools and CLI help first.
Prefer public operations that preserve specification and dependencies.
CLI `specify` can invoke an auxiliary LLM and rewrite the assignment; distinguish it from this deterministic fallback.
Do not run `decompose` to recover specified work.

If no suitable public transition is usable, inspect installed source before using `specify_triage_task(conn, task_id, author=planner_profile)`.
Require the exact parameter order, kinds and defaults represented by `specify_triage_task(conn, task_id, *, title=None, body=None, assignee=None, author=None)`.
Inspect `recompute_ready` semantics; matching signatures are insufficient.
Stop on behavior drift from this contract.
Do not patch Hermes, invent APIs, issue raw SQL updates or install another Hermes for recovery.

Call the fallback without `title`, `body` or `assignee` overrides.
It changes `triage` to `todo` and invokes native dependency recomputation.
Recomputation can advance other eligible board dependency waits.
The operation records `specified` without creating cards, invoking an LLM or clearing failure/block counters.
Inspect relevant board state before and after transition.
On `False`, re-read state instead of forcing a write.

### Concrete invocation after the checks above

Run the installed [bound launcher](../scripts/recover-triage) from the installed skill directory.
Pass one exact task ID as the only argument.

```sh
./scripts/recover-triage "$TASK_ID"
```

The launcher calls the shipped [recovery script](../scripts/recover_triage.py) with fixed team bindings.
It requires no setup record or runtime configuration file.
Report missing/unbound launchers to the Maker/operator; do not generate recovery bindings.
Complete operation, identity, and source checks first.
The script rejects signature drift but does not prove semantic equivalence.
Its `mode=rw` prevents wrong-path database creation.
SQL only reads; native transitions mutate.
Assign one recovery owner; the preliminary read is no cross-session lock.
Recheck state immediately under the native status guard, not an atomic multi-condition boundary.
Read `specified` and actual `task` state from the JSON output.
Exit code 0 proves transition, not startup or completion.

## Read back the actual landing state

- If the card is `todo`, inspect unsatisfied parents without removing valid gates.
- If the card is `ready`, report queued work rather than running work.
- If the card is `review`, inspect the last `review_requested` implementer/reviewer and latest verdict.
- If the card is `running` or newly claimed, stop recovery writes.
- Leave a newly claimed card with its current owner.

### Review-provenance special case

For a technical interruption during review, restore unfinished review with its existing provenance.
Use a Coder return only for substantive findings, questions, or required implementation continuation.
Leave `kanban_request_changes` to the active Reviewer for findings/questions returned to the original implementer.
Do not let a wake session compete with the reviewer.
Without active review, request-changes can refuse with `not in an active review run`.
Before reopening, verify prior handoff and required continuation, not pending review acceptance.
Inspect local help before using `hermes kanban --board <board> reopen-review <task>` to return the card to `ready`/`todo`.
Without a usable public equivalent, apply the same version/identity checks before `reopen_review_task(conn, task_id)`.
Read back the `review_requested` implementer, including planner/operator origins.
Do not hardcode a coder or bypass an unresolved `CHANGES_REQUESTED` verdict.
Do not reopen pending review merely to execute code.

## Preserved circuit breaker and verification

Another same-kind block can immediately return the card to triage.
Fix the cause instead of looping retries, faking completion, resetting counters, rotating block kinds or replacing cards.
`auto_decompose: false` prevents fan-out, not triage.
Do not change central gateway configuration during recovery.
Do not silently delete auto-generated children or count them done.
Read back specification, assignee, graph, and events; verify descendant gates.
Distinguish transition, review approval, and implementation completion.
Leave startup to the gateway dispatcher without new watchers, restarts, or parallel workers.
Require claim/run evidence for `running`.
Report guard-denied database access or execution as capability failure.
Distinguish customer approval, board transition, execution approval, and verified outcome.
