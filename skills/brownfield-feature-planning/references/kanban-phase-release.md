# Verified Kanban phase release

Use this procedure after explicit acceptance of a dependency-ordered implementation plan, except the conditional planning section below.
Keep orchestration with the authorized coordinator.
Do not treat plan acceptance as permission for the planner to implement or manually spawn workers.

## Expand–Migrate–Contract

Use during planning only for broad mechanical changes that cannot safely land as ordinary independent vertical slices.

1. Expand: add the new form alongside the old; verify coexistence and compatibility.
2. Migrate: move callers in reviewable bounded batches; make each batch depend on expansion.
   Keep every intermediate state working and verified, with required checks green.
3. Contract: retire the old form only after every migration batch and confirmed absence of remaining callers.
   Make contraction depend on every migration batch.

Bind these outcomes, dependencies, and verification to the accepted plan, phases, and native tickets through the release procedure below.
Advance only after each prerequisite's existing independent review gate reaches DONE.
Use existing implementation tickets and Reviewer gates for integrated acceptance; keep the Planner's final report separate.

## 1. Read-only preflight

1. Read the accepted specification and plan at their approved Git revisions.
2. Inspect the current repository HEAD, branch and working tree.
3. Record the accepted revision separately from later documentation-only commits.
4. Select the project board explicitly on every call.
5. Inspect current native schemas or CLI help for creation, title constraints, reads, subscriptions, links and release.
6. Verify the running gateway's configuration context, dispatcher/review routing, assigned profiles and concurrency cap.
7. Read only the required non-secret settings.
8. Resolve the notification destination and authorized participant from project rules, session origin and current authorization settings.
9. Do not infer the destination from an old subscription or the current desktop conversation.
10. Verify the required skill and reference-file identities at each consuming runtime.
11. Do not assume that one role's skill load transfers to another role or coding harness.

## 2. Create blocked cards and persist progress

1. Identify each planned story or prerequisite ticket and its phase in the body by approved plan path, plan commit, phase identifier and planning repository root.
2. Reference separate phase plans or specifications by absolute path and exact Git commit.
3. Write a concise actor-behaviour-benefit title, not a technical task label.
   Apply the Planner's vocabulary and accepted-ADR rules to ticket titles and descriptions at the accepted baseline.
   For a technical prerequisite, name its real beneficiary and enabling story; do not invent user actions or benefits.
   Surface incompatible native title constraints instead of truncating user meaning.
   Structure the body with short statements and concrete bullets:
   - Goal/context: state the outcome and necessary context.
   - Acceptance criteria: list concrete observable success conditions.
   - Technical implementation: include necessary interfaces, affected areas, and constraints; label suggestions separately.
   - Verification: state the checks needed to establish these criteria, including relevant failure cases.
   - Dependencies and binding: name blockers, absolute accepted plan/phase paths, exact Git commits, phase identifier, and planning repository root.
   Keep criteria and implementation context concise; align excerpts with the authoritative accepted plan.
   Make the card understandable without opening the full plan; leave implementation discretion with the Coder.
   Do not repeat the whole plan, routine team procedures, or successful-test catalogues.
4. Keep task-specific accepted exceptions in the body. Keep standard team procedures in role rules.
5. Create each card with the intended assignee/workspace, `--initial-status blocked`, an idempotency key, required skill and explicit completion contract.
6. Set explicit customer limits and required native runtime/retry fields without inventing discretionary attempt budgets.
7. Check `--max-retries` semantics before setting a consecutive-failure limit.
8. Do not interpret the failure number that trips a breaker as the number of extra attempts.
9. Read each returned exact card before further writes.
10. Verify its planned ticket and phase identity, title, approved references, body and native limits against the files at the approved revision.
11. Use the persisted card as the creation checkpoint.
12. Bind the verified notification destination.
13. Read `notify-list --json` and compare platform, channel, chat type, participant, notifier profile and delivery mode literally.

Keep development decisions, consequential failures and remedies, blockers, concise outcomes, and review verdicts on the existing card.
Attribute evidence to its executor and checked code state.
Native run outputs remain available evidence, not an authored run-log duty.
Keep product and test/start documentation in its owning repository.

### Resume a partial batch

1. Read the project board, including archived cards, before continuing creation.
2. Match persisted cards to the planned ticket identity, approved plan path, plan commit and phase identifier.
3. Resolve missing identity fields or ambiguous matches before further writes.
4. Reuse exact matching cards and create only missing planned tickets.
5. Compare existing preparation with the complete accepted ticket-to-phase mapping.
6. Complete missing bindings on blocked cards before graph verification.
7. If a card was already released, reconcile its current run and dependencies without repeating its release.
8. If a later operational blocker interrupted work, use [safe resumption](kanban-triage-recovery.md#resume-after-a-blocker-or-interrupted-run).

## 3. Verify the complete graph

1. Link missing approved ticket dependencies only after every card exists.
2. Read each exact card to verify the complete graph.
3. Use [bounded extraction](kanban-status-inspection.md#read-and-reduce-before-output-truncation) only if native reads cannot supply the required evidence.
4. Before the first release, require every card to be blocked.
5. On partial release, verify current runs and dependency gates for already released cards.
6. Preserve completed release transitions.
7. Verify each card's assignee, workspace, skill, runtime/retry fields and completion contract.
8. Check each story, criterion, technical constraint and exception against its phase scope, gate, commit boundary and reviewer binding.
9. Verify that every plan reference resolves to its approved revision.
10. Verify every notification binding against the intended destination.
11. Verify that the first ticket has no parent and the final ticket has no child in the approved chain.
12. Verify each intermediate ticket's intended predecessor and successor.
13. If a write succeeds but parsing fails, re-read its recorded exact ID instead of repeating the write.
14. Stop release on any unresolved mismatch while preserving partial progress.

## 4. Release without racing the dispatcher

1. Verify the complete graph before release. Use native card/link state as the checkpoint; omit routine progress comments.
2. Finish authorized planning commits before release.
3. Do not leave planner metadata edits uncommitted in a directory workspace that a worker can immediately modify.
4. Unblock descendants in reverse order and the first ticket last.
5. On resume, apply this order only to pending initial releases.
6. Read back each transition to verify that descendants remain `todo` while parents are incomplete.
7. Read the first ticket as `ready` unless a real dispatcher claim already makes it `running`.
8. Use native board events as the release record.
9. Record consequential discrepancies on the relevant card and verify each posted comment.
10. Keep the historical pre-release checkpoint distinct from current task status.
11. Read the whole project board again after release.
12. Leave later advancement to the dispatcher and independent review gates.
13. Do not wait or manually dispatch merely to report `running` instead of `ready`.

A release handoff proves neither completed implementation nor customer acceptance.
It does not guarantee execution-service availability.

## Narrow scope without stopping the accepted delivery

Use this section when the owner rejects expanded side work but still requests the accepted delivery.
Do not use scope narrowing to resume cancelled work, add functionality, bypass a denial or weaken a safety gate.

1. Read the exact coding card, current board, run, repository state and relevant writer processes.
2. Report whether work is running, ready or idle and whether input is genuinely missing.
3. If newer documentation obscured the agreed instructions, recover their accepted baseline.
4. Map the remaining instructions to existing implementation rather than rewriting working code or building a new test platform.
5. Bind the accepted bounded scope on the existing card. Record the narrowing decision and exceptions missing from the plan.
6. Park obsolete runnable successors with the supported `assign <obsolete-task> none` operation before release.
7. Replace their active body instructions with an explicit hold and historical-reference status.
8. Do not falsely complete parked work.
9. Temporarily unassign the coding card if dispatch could race the graph edits.
10. Update its body through the supported `edit <coding-task> --body <body-text>` operation.
11. Reference the approved plan revision and explicitly supersede obsolete instructions and historical attachments.
12. Use `unlink <obsolete-parent> <coding-task>` only for a prerequisite belonging to the abandoned scope.
13. Preserve dependencies that still protect the requested mutation.
14. Do not claim that removing an obsolete prerequisite proves its checks passed.
15. Read back the body, remaining parents, parked successors and notification route.
16. Require fulfilled necessary parents and an ended previous writer before restoring the intended coding assignee.
17. Release the existing card with `kanban_unblock(task_id=..., board=...)` from the authorized orchestrator context.
18. Do not reset counters, reclassify capability failures or manually claim/dispatch.
19. Check pickup with a bounded native `kanban_list` filtered by assignee and status.
20. Report `ready` until an actual intended-profile claim supplies a new run identity.
21. Keep resumed coding, independent review and verified product results distinct.

## Amend an approved graph

1. Reconcile overlapping proposals into one authoritative amendment with file scope, commit boundary, gate and dependency order.
2. Obtain explicit amendment approval before creating or releasing additional coding work.
3. Mark superseded proposals as historical rather than treating another needs-input notification as new approval.
4. Keep the successor blocked while creating and binding the approved reviewed prerequisite.
5. Preserve still-valid parent edges.
6. Update both bodies to reference the exact approved amended plan revision.
7. Verify parent sets, notification routing and plan references before release.
8. Return the successor to dependency-gated `todo` before releasing the new prerequisite.
9. Read back both states to exclude premature successor execution.
