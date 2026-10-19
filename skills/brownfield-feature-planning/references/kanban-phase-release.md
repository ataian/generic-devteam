*** VON GORDON ANFANG***
# Verified Kanban phase release

Use after explicit acceptance of a dependency-ordered implementation plan. This is orchestration, not permission for the planner to implement or manually spawn workers.

## 1. Read-only preflight

- Read the accepted plan/specification and inspect current repository HEAD, branch and working tree. Record the accepted revision separately from later documentation-only commits.
- Inspect live CLI help for `create`, `show`, `attach`, `attachments`, `notify-subscribe`, `notify-list`, `link` and `unblock`; use schemas/help, not remembered options. Explicitly select the project board on every call.
- Verify the running gateway's configuration context, dispatcher/review settings, assigned profiles and concurrency cap. Read only the non-secret settings needed; avoid broad config commands that print credential fields.
- Resolve the required notification channel and authorized participant from project rules, session origin and current authorization settings. An old subscription alone is insufficient; do not assume the current desktop conversation is the destination channel session.
- Verify required skill availability and loaded package identity at each consuming runtime. Check needed reference files as well as SKILL.md; one role loading a skill does not transfer it to another role or coding harness.

## 2. Create blocked cards and persist progress

1. Prepare each body from the accepted common constraints plus that phase's files, interfaces, tests, gate, dependency and commit boundary. Include absolute source paths, explicit approval provenance, implementer-only harness instructions and the independent reviewer handoff.
2. Create each card with the correct assignee/workspace, `--initial-status blocked`, an idempotency key, required skill, explicit completion contract and approved runtime/retry settings. For native consecutive-failure limits, inspect `--max-retries` semantics: it can mean the failure number that trips the breaker, not the number of extra attempts.
3. Immediately persist the returned real ID in a durable manifest before attachments or further calls. Store approved document hashes and limits alongside it; recover a partial batch from this manifest rather than starting creation over.
4. Attach the accepted plan and specification as real files, not comment links. Read `attachments --json` and compare the stored files' hashes with the accepted originals; upload success alone does not prove document identity.
5. Bind the verified notification destination, then read `notify-list --json` and compare platform, channel, chat type, participant, notifier profile and delivery mode literally.

## 3. Verify the complete blocked graph

Only after every card exists, link consecutive phases. Read each exact card using `show --json`; parse complete stdout within the executing process and print a reduced summary, avoiding truncation of large bodies.

Require:
- Every card is still blocked and has the intended assignee, workspace, skill, runtime/retry fields and completion contract.
- Phase one has no parent, the final phase no child, and every intermediate phase exactly the intended predecessor/successor.
- Every body contains its gate, commit boundary, approved scope and reviewer handoff.
- Every attachment and notification binding matches the verified target.

Do not repeat a successful write merely because parsing failed; re-read the recorded exact ID. Preserve incomplete progress and stop release on any unresolved mismatch.

## 4. Release without racing the dispatcher

1. Persist the verified graph checkpoint and any authorized repository manifest commit before release. Avoid leaving planner metadata edits uncommitted in a directory workspace that a worker can immediately start modifying.
2. Unblock descendants in reverse order and phase one last. Read each transition back: descendants remain `todo` while their parents are incomplete; phase one becomes `ready` or may already be claimed as `running`.
3. Store the live release receipt outside the shared implementation workspace, or use board comments/events, so post-release bookkeeping does not dirty the worker's checkout. Keep the committed manifest clearly labeled as a pre-release checkpoint rather than falsely claiming it is live status.
4. Read the whole project board once more. Report `ready` until a real claim/start is observed; do not wait or manually dispatch just to turn an honest ready status into a running claim. Leave later phase advancement to the dispatcher and independent review gates.

The release handoff is not completion of the app, a guarantee of provider availability or customer acceptance of the result.
*** VON GORDON ENDE ***
