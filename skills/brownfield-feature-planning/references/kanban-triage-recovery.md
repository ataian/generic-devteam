# Safe Kanban resumption and triage recovery

Trigger: resolved blocker or interrupted run. Use additional checks below for internal triage recovery. Recovery grants no new permission.

- Preserve card, authorized scope, history, valid dependencies, review provenance, counters, and native counter semantics, including legitimate transition resets.
- Preserve assigned implementation/review owners, native guards, and runtime policies. Leave dispatch to the dispatcher.
- Triage means blocked work in this team. Never deliberately send work there.
- Screen a real Coder escalation for an overlooked in-scope solution before involving the customer. If found, record the correction and resume the Coder without a customer round. Otherwise coordinate permitted recovery or obtain the missing decision in Mattermost.
- For a missing worker credential with an explicitly authorized local source, verify source accessibility and an unambiguous match without emitting the value. Give the worker only the source and injection procedure. Scope the value to the consuming process, with tracing off; never pass it in argument vectors, tickets, tool results, or logs. Verify the injection prerequisite before releasing a retry.
- Record a sufficient customer answer and its scope on the existing ticket. Amend the versioned plan and affected ticket bindings before release when required. Post with `kanban_comment(task_id=..., body=...)` and read back the decision before resuming. A sufficient answer needs no further start request.
- A Mattermost wake carries no active Reviewer authority. Use ordinary unblock or guarded triage recovery. Reserve request-changes for active review.
- Keep capability failures and verified quota pauses blocked until their actual cause is resolved. Verify quota reset before authorized native one-time resumption.

## Resume after a blocker or interrupted run

1. Read exact task, full blocker/decision thread, parents, children, latest runs, and claim. Match answer scope to blocker and run. An old answer must not clear a newer blocker. Leave active/completed tasks unchanged.
2. If the failure boundary is unclear, use [status inspection](kanban-status-inspection.md). Verify blocker resolution, authority for the next operation, and artifacts/results against original task/run records. Verify returning-context capabilities and permissions. Keep each session's capability and approval evidence separate.
3. Keep unresolved work blocked and descendants gated. Coordinate existing claims/retries through their owner's thread. Require an ended previous writer and no parallel repository writer before continuing.
4. Inspect HEAD, `git status --short`, and `git diff --check` before defining remaining work. Preserve completed commits, partial changes, unrelated files, and historical observations.
5. Record on the existing card: repaired boundary and evidence, intended owner, remaining file/verification/commit/review work, unchanged exclusions, and reusable completed prerequisites/final results. For handoff/reporting only, exclude reimplementation and duplicate commits. Clarify ambiguous assignments without repeating completed coordination.
6. Replace contradictory active body text through the supported edit. Read back body and resumption comment before release.
7. Once blocker is resolved, parents satisfied, and target runs ended, use `kanban_unblock(task_id=..., board=...)` from the authorized orchestrator.
8. Read back recipient, source phase, valid parents, and later phases still gated without runs. Verify baseline adoption independently of queue/start status. Report `ready` until a new intended-profile dispatcher claim. Use the native transition as release evidence. Add any missing readback evidence to the same card and verify the comment. Report continuation. Execution repair and acceptance require their own evidence.

If automatic-triage release is refused, use the fallback below. For scope/graph changes, use [approved phase changes](kanban-phase-release.md#amend-an-approved-graph). Preserve cards and unresolved capability/security block kinds.

### Resume a blocked card after coordinator acknowledgment

Prerequisite: completed acknowledgment resolves the original blocker. Keep unresolved execution/security denials blocked.

1. Read complete report, original run, and terminal event. Verify owner and fulfillment of the result contract. Preserve worker privileges and completed subscription/graph checks.
2. Verify process exit separately from `ended_at` or board `done`. Get PID and process-start identity from the exact original spawn record. Inspect `ps -p <verified-pid> -o pid,ppid,stat,etime,comm` and relevant children with `ps --ppid <verified-pid> -o pid,ppid,stat,etime,comm`. Check start identity for PID reuse.
3. If handoff requires exit, use a supported bounded foreground check. Never kill or reclaim completed work to end its epilogue. End the turn for delegated results instead of polling.
4. After exit, re-read the final report for late events. Verify task, run, artifact, and result against final records. Apply ordinary resumption checks before release.

## Decision before transition

Trigger: repeated-block `triage` refuses ordinary `unblock` or `promote`. Triage alone requires no further specification, decomposition, replacement ticket, or approval.

1. Read the complete current thread for `block_loop_detected`, `kind`, and recurrence count. Match the answer to the current blocker, including distinct same-kind questions. Inspect dependencies under ordinary resumption checks. Screen the escalation as above and attribute the correction/answer to its actual source.
2. Confirm no active worker or claim owns the card. Do not reclaim or kill a worker to qualify for recovery.
3. Verify dispatcher installation, interpreter, profile home, and database. Check inherited `HERMES_KANBAN_DB`. Board names cannot identify a database. Exclude other teams' databases and private data.
4. Immediately before transition, re-read task and graph for concurrent changes. Inspect generated children, claims, runs, and dependencies. Route unsafe graph changes to the operator. Preserve protective gates.

Report unresolved permission, cause, ownership, or identity gaps. Inspect recovery options before declaring triage unfixable or requesting a manual drag.

## Supported transition, then internal fallback

1. Inspect installed native tools and CLI help. Prefer public transitions preserving specification and dependencies. CLI `specify` can call an auxiliary LLM and rewrite the assignment. Do not run `decompose` to recover specified work.
2. If no suitable public transition is usable, inspect installed source before using `specify_triage_task(conn, task_id, author=planner_profile)`. Require `specify_triage_task(conn, task_id, *, title=None, body=None, assignee=None, author=None)` with exact parameter order, kinds, and defaults. Inspect `recompute_ready` behavior as well as signatures. Stop on drift. Do not patch Hermes, invent APIs, issue raw SQL updates, or install another Hermes.
3. Inspect relevant board state before and after the fallback. Omit `title`, `body`, and `assignee` overrides. The call moves `triage` to `todo`, invokes native dependency recomputation, and records `specified`. Other eligible dependency waits may advance. It creates no cards, invokes no LLM, and clears no failure/block counters.
4. On `False`, re-read state. Do not force a write.

### Concrete invocation after the checks above

After operation, identity, and source checks, run the installed [bound launcher](../scripts/recover-triage) from the installed skill directory. Pass one exact task ID as the only argument.

```sh
./scripts/recover-triage "$TASK_ID"
```

- The launcher invokes the shipped [recovery script](../scripts/recover_triage.py) with fixed team bindings. It needs no setup record/runtime configuration file. Report missing/unbound launchers to the Maker/operator. Do not generate bindings.
- The script rejects signature drift but does not prove semantic equivalence. Its `mode=rw` prevents wrong-path database creation. SQL only reads. Native transitions mutate.
- Assign one recovery owner. The preliminary read is no cross-session lock. Recheck state immediately under the native status guard. It does not provide an atomic multi-condition boundary.
- Read `specified` and actual `task` state from JSON output. Exit code 0 proves transition only.

## Read back the actual landing state

- `todo`: inspect unsatisfied parents and preserve valid gates.
- `ready`: report queued.
- `review`: inspect the last `review_requested` implementer/reviewer and latest verdict.
- `running` or newly claimed: stop recovery writes and leave the claim with its owner.

### Review-provenance special case

1. Technical interruption during review: restore unfinished review with existing provenance. Use a Coder return only for substantive findings, questions, or required implementation continuation.
2. Reserve `kanban_request_changes` for the active Reviewer returning findings/questions to the original implementer. Wake sessions must not compete with review. Without active review, request-changes can refuse with `not in an active review run`.
3. Before reopening, verify prior handoff and required continuation. Leave pending review acceptance with the Reviewer. Never reopen pending review to execute code or bypass unresolved `CHANGES_REQUESTED`.
4. For a card in `review`, inspect local help before `hermes kanban --board <board> reopen-review <task>` to return it to `ready`/`todo`. If no usable public equivalent exists, apply the same version/identity checks before `reopen_review_task(conn, task_id)`.
5. For a card still `blocked` from an ended review that now needs explicitly approved implementation changes, verify the installed transition semantics: ordinary `unblock` can restore `review` and race the dispatcher. When native `promote --dry-run --json` confirms that the card can return directly to `ready` with dependencies enforced, read back the approved baseline, restore the original implementer while the card is still blocked, then promote the same card with the audit reason. Require no active claim or unresolved capability blocker; leave dependent gates and the next independent review intact. Read back the native transition and actual claim separately.
6. Resolve the implementer from the last `review_requested` event, including planner/operator origins. Do not hardcode a coder.

## Preserved circuit breaker and verification

- Another same-kind block can immediately return the card to triage. Fix the cause. Do not loop retries, fake completion, reset counters, rotate block kinds, or replace cards.
- `auto_decompose: false` prevents fan-out. Triage can still occur. Leave central gateway configuration unchanged. Do not silently delete auto-generated children or count them done.
- Read back specification, assignee, graph, and events. Verify descendant gates. Keep transition, review approval, and implementation completion distinct.
- Leave startup to the gateway dispatcher. No new watchers, restarts, or parallel workers. Require claim/run evidence for `running`.
- Report guard-denied database access or execution as capability failure. Distinguish customer approval, board transition, execution approval, and verified outcome.
