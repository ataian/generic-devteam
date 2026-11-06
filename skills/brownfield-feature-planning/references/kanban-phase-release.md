# Verified Kanban phase release

Use after explicit acceptance of a dependency-ordered implementation plan. This is orchestration, not permission for the planner to implement or manually spawn workers.

## 1. Read-only preflight

- Read the accepted plan/specification and inspect current repository HEAD, branch and working tree. Record the accepted revision separately from later documentation-only commits.
- Inspect live CLI help for `create`, `list`, `show`, `notify-subscribe`, `notify-list`, `link` and `unblock`; use schemas/help, not remembered options. Explicitly select the project board on every call.
- Verify the running gateway's configuration context, dispatcher/review settings, assigned profiles and concurrency cap. Read only the non-secret settings needed; avoid broad config commands that print credential fields.
- Resolve the required notification channel and authorized participant from project rules, session origin and current authorization settings. An old subscription alone is insufficient; do not assume the current desktop conversation is the destination channel session.
- Verify required skill availability and loaded package identity at each consuming runtime. Check needed reference files as well as SKILL.md; one role loading a skill does not transfer it to another role or coding harness.

## 2. Create blocked cards and persist progress

1. Identify each phase by the approved plan path, plan commit, and phase identifier in its task body. Include the planning repository root. Prepare each body from the accepted common constraints plus that phase's files, interfaces, tests, gate, dependency and commit boundary. Include absolute source paths, explicit approval provenance, implementer-only harness instructions and the independent reviewer handoff.
2. Create each card with the correct assignee/workspace, `--initial-status blocked`, an idempotency key, required skill, explicit completion contract and approved runtime/retry settings. For native consecutive-failure limits, inspect `--max-retries` semantics: it can mean the failure number that trips the breaker, not the number of extra attempts.
3. Read each returned exact card before further writes. Verify its phase identity, approved document references, and native limits. Use the persisted card as the creation checkpoint.
4. Reference the accepted plan and phase plan by absolute path and exact Git commit. Include the accepted specification reference if it is separate. Read the referenced files at the approved Git revision in the planning repository. Verify that their requirements match the task body.
5. Bind the verified notification destination, then read `notify-list --json` and compare platform, channel, chat type, participant, notifier profile and delivery mode literally.

### Resume a partial batch

Read the project board, including archived cards, before continuing ticket creation.
Match persisted task bodies to the approved plan path, plan commit, and phase identifier.
Reuse the exact matching cards.
Resolve missing identity fields or ambiguous matches before further writes.
Check existing cards against the accepted phase list to identify incomplete preparation.
Create only missing phases.
Continue missing bindings on blocked cards and verify the complete graph before release.
If a card was already released, reconcile its current run and dependencies before continuing.

## 3. Verify the complete graph

Only after every card exists, link missing consecutive phase dependencies. Read each exact card using `show --json`; parse complete stdout within the executing process and print a reduced summary, avoiding truncation of large bodies.

Before the first release, require every card to be blocked.
On resume, verify current runs and dependency gates for already released cards.
Preserve their completed release transitions.
Treat a later operational blocker under the existing blocker workflow, not as an unfinished initial release.

Require:
- Every card has the intended assignee, workspace, skill, runtime/retry fields and completion contract.
- Phase one has no parent, the final phase no child, and every intermediate phase exactly the intended predecessor/successor.
- Every body contains its gate, commit boundary, approved scope and reviewer handoff.
- Every plan reference resolves to the approved revision.
- Every notification binding matches the verified target.

Do not repeat a successful write merely because parsing failed; re-read the recorded exact ID. Preserve incomplete progress and stop release on any unresolved mismatch.

## 4. Release without racing the dispatcher

1. Record the verified graph checkpoint on the first phase card and read it back. Finish any authorized planning commits before release. Avoid leaving planner metadata edits uncommitted in a directory workspace that a worker can immediately start modifying.
2. Unblock descendants in reverse order and phase one last. Apply this order only to pending initial releases on resume. Read each transition back: descendants remain `todo` while their parents are incomplete; phase one becomes `ready` or may already be claimed as `running`.
3. Use native board events as the release record. Record required readback findings in task comments if the events do not contain them. Read back each posted comment. Keep the pre-release checkpoint distinct from current task status.
4. Read the whole project board once more. Report `ready` until a real claim/start is observed; do not wait or manually dispatch just to turn an honest ready status into a running claim. Leave later phase advancement to the dispatcher and independent review gates.

The release handoff is not completion of the app, a guarantee of provider availability or customer acceptance of the result.
