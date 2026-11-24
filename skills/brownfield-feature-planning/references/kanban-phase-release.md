# Verified Kanban phase release

Prerequisite: explicit acceptance of a dependency-ordered implementation plan. Only the planning section below runs before acceptance. The authorized coordinator orchestrates. Plan acceptance grants the Planner neither implementation nor manual worker-spawn authority.

## Expand–Migrate–Contract

During planning only, use for broad mechanical changes that cannot safely land as ordinary independent vertical slices.

1. Expand: add the new form alongside the old. Verify coexistence and compatibility.
2. Migrate: move callers in bounded, reviewable batches, each dependent on expansion. Keep every intermediate state working and verified, with required checks green.
3. Contract: depend on every migration batch. Confirm no callers remain before retiring the old form.

Carry outcomes, dependencies, and verification into the accepted plan, phases, and native tickets through the release procedure below. Advance only when each prerequisite's existing independent review gate reaches DONE. Use existing implementation tickets and Reviewer gates for integrated acceptance. Keep the Planner's final report separate.

## 1. Read-only preflight

1. Read specification and plan at approved Git revisions. Inspect current HEAD, branch, and working tree. Record accepted revisions separately from later documentation-only commits.
2. Select the project board explicitly on every call. On rejection, inspect native help. Setup established the surface.
3. Get the notification destination from project rules and reuse the verified gateway origin for the participant and `chat_type`. Match the gateway's literal type: a private Mattermost channel can be reported as `group`, so do not infer `channel` from its display label. Re-derive only if the binding changed or the relevant origin fields were not established. Old subscriptions and the current desktop conversation are not sources for the destination.
4. Reuse setup facts for gateway, dispatcher, adapter ownership, routing, and file identity. Skip per-release rechecks.
5. When the planned change repairs the demo teardown command itself, check before plan acceptance whether the existing approved teardown can satisfy the pre-release gate. If not, escalate the circular prerequisite to the operator and keep the release blocked. Do not propose applying and reverting the same product fix simply to get through the gate.

## 2. Create blocked cards and persist progress

1. Write one concise actor-behaviour-benefit story in the title. For a technical prerequisite, use the real beneficiary and enabling story. Do not invent user actions or benefits or use a technical task label. Surface incompatible native title limits without truncating user meaning. Apply the Planner's vocabulary and accepted-ADR rules to title and body at the accepted baseline.
2. Write a self-contained body with short bullets. Use the authoritative accepted plan for excerpts. Leave implementation discretion with the Coder.
   - Goal/context: outcome and necessary context beyond the title.
   - Acceptance criteria: observable success conditions.
   - Technical implementation: necessary interfaces, affected areas, binding constraints, and accepted task-specific exceptions. Label suggestions separately.
   - Verification: state the checks needed to establish these criteria, including relevant failure cases.
   - Dependencies and binding: planned story/prerequisite identity, blockers, absolute accepted plan/phase paths, exact Git commits, phase identifier, and planning repository root. Bind separate phase plans or specifications by absolute path and exact Git commit.
   - Keep criteria and implementation context concise. Leave standard procedures in role rules and omit whole-plan copies and successful-test catalogues.
3. Set native assignee and workspace, `--initial-status blocked`, idempotency key, explicit completion contract, explicit customer limits, and required runtime/retry fields. Set no `skills`: role skills come from setup. Do not invent discretionary attempt budgets. Give every Coder card `--max-runtime 8h`; it caps the whole worker run for dispatcher recovery, not the work budget. Check `--max-retries` semantics before setting a consecutive-failure limit. The breaker threshold counts failures, not extra attempts.
4. Read back each returned exact card before further writes. Compare ticket/phase identity, title, approved references, body, and native limits against approved-revision files. Use the persisted card as the creation checkpoint.
5. Bind the verified notification destination. Read `notify-list --json`. Compare platform, channel, chat type, participant, notifier profile, and delivery mode literally.
   Subscribe on the project board: `hermes -p <planner-profile> kanban --board <board> notify-subscribe <task> ...`, then read the same board and task back. A subscription created without the board binds to the wrong installation.

Existing card: development decisions, consequential failures and remedies, blockers, concise outcomes, and review verdicts. Attribute evidence to its executor and checked code state. Native run outputs remain available evidence, not an authored run-log duty. Keep product and test/start documentation in its owning repository.

### Resume a partial batch

1. Read the project board, including archived cards. Match persisted cards by planned ticket identity, approved plan path, plan commit and phase identifier. Resolve missing fields or ambiguous matches before writing.
2. Reuse exact matches. Create only missing planned tickets. Compare existing preparation against the complete accepted ticket-to-phase mapping. Complete missing bindings on blocked cards before graph verification.
3. For released cards, reconcile current runs and dependencies without repeating the release. If a later operational blocker interrupted work, use [safe resumption](kanban-triage-recovery.md#resume-after-a-blocker-or-interrupted-run).

## 3. Verify the complete graph

1. Wait until all cards exist before linking missing approved dependencies. Read each exact card. Use [bounded extraction](kanban-status-inspection.md#read-and-reduce-before-output-truncation) only when native reads lack required evidence.
2. Before first release, require every card blocked. On partial release, preserve completed transitions and verify current runs and dependency gates on released cards.
3. Check assignee, workspace, runtime/retry fields, and completion contract. Check each story, criterion, technical constraint, and exception against phase scope, gate, commit boundary, and reviewer binding.
4. Resolve each plan reference to its approved revision. Verify every notification binding against the intended destination. Verify the first ticket has no parent and the final ticket has no child in the approved chain. Preserve valid links to follow-up tickets outside the chain. Verify each intermediate ticket's intended predecessor and successor.
5. If parsing fails after a successful write, re-read the recorded exact ID. Do not repeat the write. Stop release on unresolved mismatches. Preserve partial progress.

## 4. Release without racing the dispatcher

1. Verify the full graph before release. Use native card/link state as the checkpoint. Omit routine progress comments.
2. Finish authorized planning commits. Leave no uncommitted Planner metadata in a directory workspace a worker can immediately modify.
3. Unblock descendants in reverse order and the first ticket last. On resume, apply the order only to pending initial releases.
4. Read back each transition. Descendants remain `todo` while parents are incomplete. The first ticket is `ready` until a real dispatcher claim makes it `running`.
5. Use native board events as release evidence. Record consequential discrepancies on the relevant card and verify posted comments. Distinguish the historical pre-release checkpoint from current status.
6. Read the whole project board again. Leave later advancement to the dispatcher and independent review gates. Do not wait or dispatch manually merely to replace a `ready` report with `running`.

Report verified release. Implementation completion, customer acceptance, and execution-service availability require separate evidence.

Send handoff and closing report with `hermes send --to mattermost:<channel-id> --json` and read the returned message ID back. Use the project binding for the channel ID. `--list mattermost` finds no channels without a channel directory and cannot serve as a probe.

## Narrow scope without stopping the accepted delivery

Trigger: the owner rejects expanded side work and still requests accepted delivery. Scope narrowing grants no authority to resume cancelled work, add functionality, bypass a denial, or weaken a safety gate.

1. Read the exact coding card, board, run, repository state, and relevant writer processes. Report running, ready, or idle and whether input is genuinely missing.
2. If newer docs obscure the agreed instructions, recover the accepted baseline. Map remaining instructions to existing implementation. Preserve working code and avoid a new test platform.
3. Bind bounded scope to the existing card. Record the narrowing decision and exceptions missing from the plan.
4. Before release, park obsolete runnable successors with `assign <obsolete-task> none`. Replace active body instructions with an explicit hold and historical-reference status. Do not mark parked work falsely complete.
5. If dispatch can race graph edits, temporarily unassign the coding card. Update its body with `edit <coding-task> --body <body-text>`. Reference the approved plan revision and explicitly supersede obsolete instructions and historical attachments.
6. Use `unlink <obsolete-parent> <coding-task>` only for an abandoned-scope prerequisite. Preserve dependencies protecting the requested mutation. Removing an obsolete prerequisite proves no checks passed.
7. Read back body, remaining parents, parked successors, and notification route. Restore the intended coding assignee only after required parents are fulfilled and the previous writer has ended.
8. Release the existing card with `kanban_unblock(task_id=..., board=...)` in the authorized orchestrator context. Preserve counters and capability-failure classifications. Leave claims and dispatch native.
9. Check pickup with bounded native `kanban_list` filtered by assignee and status. Report `ready` until an actual intended-profile claim supplies a new run identity. Distinguish resumed coding, independent review, and verified product results.

## Amend an approved graph

1. Reconcile overlapping proposals into an authoritative amendment: file scope, commit boundary, gate, and dependency order. Obtain explicit amendment approval before creating or releasing additional coding work.
2. Mark superseded proposals historical. A new needs-input notification grants no approval.
3. Keep the successor blocked while creating and binding the approved reviewed prerequisite. Preserve valid parent edges. Update both bodies to reference the exact approved amended plan revision.
4. Verify parent sets, notification routing, and plan references before release. Return the successor to dependency-gated `todo` before releasing the new prerequisite. Read back both states to rule out premature successor execution.
