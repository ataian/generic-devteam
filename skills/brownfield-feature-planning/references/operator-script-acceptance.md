# Operator script acceptance

Use for an accepted operator setup, import, or activation path.
These rules neither authorize deployment nor prove that a recipe has run.

## Establish the execution boundary

Separate artifact creation, isolated verification, and live application.
Record approved test targets and deployment exclusions in the plan and phase cards.
Do not require a production host for artifact-only work or inherit historical host permissions.

Read the maintained instruction and existing importer first.
Map required actions to actors, inputs, resources, and observable results.
Inspect deployment/startup wiring only as needed for that path.
Do not expand import automation into application-lifecycle management.
Distinguish a user-confirmed deployed checkout from direct live inspection.

Under a Docker-only contract, require only Docker and ordinary shell facilities on the operator host.
Keep language-runtime installation, source checkout, compilation, and image builds on the development side.
Place the entrypoint and short README in the deployment repository.
Invoke packaged business logic from its producing module; do not copy sources or create another parser.
Name the chain: host script → producing artifact → command process/container → database.
Identify exact repositories, services, images, and paths as existing, proposed, or execution-verified.

## Configuration and process boundaries

1. Resolve the deployment directory, ordered config files, project identity, and existing container.
   Reject ambiguous targets before mutation.
   Verify administrative access rather than assuming a default role.
2. Name the operator configuration, required keys, and normal invocation.
   Trace credentials/settings from authorized sources into the DB client and app process.
   Read only needed fields without printing secrets or executing dotenv files with shell `source`.
   Avoid duplicate password stores.
   Distinguish existing readers from proposed configuration behavior.
3. Inspect producer packaging and the built command, resources, and dependencies.
   Verify command-only launch with a harmless help/argument check in the built image.
   Contents alone prove neither deployment availability nor entrypoint execution.
   Do not add live compilation or dependency downloads from obsolete developer recipes.
4. Choose placement from the isolation requirement.
   A process inside the existing container shares its resource limits and can affect the app through exhaustion.
   A temporary container can have separate limits but still shares host/database capacity.
   Override its server entrypoint to run only the utility.
   Do not require a permanent service or bespoke image without need.
5. For temporary jobs, resolve the actual local image ID and existing DB network.
   Mount only required inputs/configuration read-only.
   Exclude app data mounts, published ports, privileges, and the Docker socket.
   Container-network DB access does not require a host DB port.
   Verify command availability before mutation.
   Treat outdated images as explicit update prerequisites, not permission for live builds, pulls, or restarts.
6. Deliver producer packaging before its wrapper.
   Retire the old entrypoint only after a successful real data-operation check.
   Include required container access, authentication, and verification in the executable path.
   Document and test any unavoidable manual preparation.

Limit import-only mutations to module data and invocation-owned resources.
Do not recreate app/DB services, change credentials, alter primary data, or publish ports for that path.
If activation is contracted, verify flags and DB settings in the running process.
An edited environment file or fresh image does not prove enablement.
Disclose required restarts/recreation and obtain approval for changed functionality.
Preserve unrelated services and dependencies.
For optional-data failure containment, load [External-data discovery](data-discovery.md#optional-data-features).

## Artifact provenance and startup-contract preflight

Inventory baseline, target, and dependency artifacts before integrated acceptance.
Assign acquisition or transfer to an authorized role.
Inspect exact immutable references on the verified worker engine.
Require their actual `RepoDigests` and compare reported versus live Image-IDs separately.
Distinguish image, manifest, and index digests.
Record selected platform and acquired platform-image identity when relevant.
Tags, source checkouts, and local builds do not prove deployed image content.

For upgrade acceptance, require authentic pre-feature artifacts and functional dependencies.
Do not substitute stripped target builds or idle placeholder services.
Label smaller component fixtures by their actual scope.
Preserve baseline identities and use distinct target-build names to prevent tag overwrite.

Compare startup guards with maintained and baseline build definitions using `git show BASELINE:path`.
Trace `Entrypoint + Cmd`, `WorkingDir`, mounts, and artifact paths.
Path spelling alone proves neither incompatibility nor a schema-changing upgrade.
Reproduce suspected mismatches against the unchanged predicate before proposing fixes.
If imports start orchestration, use an inspected scratch-only predicate probe with synthetic inputs.
Prevent external calls and include a control that reaches the next guard.
Report predicate evidence separately from container/database execution.

Record artifact-access and compatibility-code blockers separately on the existing card.
Obtain amendment approval for out-of-phase fixes with independent review.
Do not change fixtures/build definitions to hide production mismatches.
Keep outstanding real-image checks explicit.

### Authenticated registry metadata and acquisition handoff

Use after owner confirmation of candidate references and authorization of the credential source.

1. Read required credentials machine-side without dotenv execution or interpolation.
   Limit access to registry credentials, not unrelated profile/application secrets.
   Keep values out of prompts, argv, reports, and diagnostics.
2. Validate the approved HTTPS origin/port before authentication.
   Reject URL userinfo and credential-forwarding redirects.
   Follow the actual authentication challenge and keep headers in memory.
   Bound request time and response size.
3. Request `/v2/<repository>/manifests/<reference>` with Docker/OCI manifest/index Accept types.
   Validate schema/media type and `Docker-Content-Digest` syntax.
   Report only approved reference, status, type, and digest.
   Do not dump bodies, headers, or secret-bearing exceptions.
   An unauthenticated response proves an access boundary, not artifact absence.
4. Separate owner confirmation, authenticated availability, and digest capture.
   Pin immutable references in the plan/handoff and stop on acquisition-time identity drift.
5. Assign acquisition to the execution role.
   Use private temporary Docker authentication outside repositories/build contexts.
   Pass passwords through stdin and preserve existing logins.
   Pull pinned references and verify local IDs, RepoDigests, engine, and platform.
   Remove only owned temporary authentication files.
6. Distinguish metadata access, acquisition, compatibility, and end-to-end acceptance.
   Provisioning elsewhere does not prove the next worker's command-approval capability.
   Keep successors gated until their execution context and handoff meet entry conditions.

## Safe mutation and recovery

Perform read-only preflight and acquire artifacts before interrupting services.
Preserve environment values, Compose override order, mounts, dependencies, and later-start configuration.
Empty-directory initialization SQL does not provision an existing volume.
Provide the required existing-instance provisioning path.

Back up affected data and verify restoration, not only dump creation.
Require backup before catalog replacement, including direct importer calls.
Record original configuration/image identity and detect operator edits before rewriting or restoring files.
Serialize conflicting operations and bound external calls.
Return clear nonzero failures and clean only authorized invocation-owned resources.
Separate disablement from deletion and image rollback from database rollback.
Route out-of-scope main-schema changes to a separate upgrade decision.

### Version-control protection for generated state

1. Locate generated credentials, config snapshots, complete dumps, and partial backups in every affected repository.
   Include nested deployments; directory permissions do not prevent Git staging.
2. Add targeted versioned ignore rules in each owning repository.
   Use directory-only unanchored patterns when generated directories occur at multiple depths.
   Avoid broad extension rules that hide legitimate fixtures.
3. Test synthetic root/nested paths with `git check-ignore --no-index -v`.
   Require the intended versioned `.gitignore`, not global or machine-local excludes.
   Include normal source/documentation paths as negative controls.
   Inspect `git ls-files` names for tracked state without reading secrets.
   Escalate matches rather than deleting data or rewriting history.
4. Explain limits: ignore rules exclude neither tracked files nor `git add -f`.
   Sibling repositories need their own rules.
   Replace obsolete manual-exclusion instructions when versioned protection is delivered.
5. If authorized file scope cannot meet the gate, obtain approval for the missing repository prerequisite.
   Retain independent review; do not weaken the gate or substitute machine-local exclusions.

## Real operator acceptance

Define a finite journey from accepted outcomes and safety gates.
Tie each check to a requirement or concrete changed-code risk.
Assign bounded fixture/artifact preparation to the appropriate team role, not implicitly to the user.
Inspect setup commands for hidden builds/downloads and order contradictions.
Correct accidental contradictions in the authoritative order without bypassing real restrictions.

Link a short README beside the entrypoint from the operator's usual starting point.
Lead with required keys, credential sourcing, one complete invocation, results, and failure/repeat behavior.
Include maintenance, activation, UI, and lifecycle only when contracted.
Keep architecture/history outside the normal path.

Execute those commands against a safely owned running target.
For import-only work, verify records, relevant target/input/backup failures, and repeat behavior.
Prove primary data and existing services unchanged.
Require populated full-app fixtures and authenticated UI/lifecycle checks only for contracted functions.
A source-independent package copy proves packaging independence, not DB execution.

Before fixture creation, re-inventory Docker endpoint, capacity, containers, networks, volumes, mounts, and listeners.
Replace fixed names, tags, ports, and host paths with owned test resources.
Compose project naming alone is not isolation.
Prefer no published ports; otherwise use free loopback-only bindings.
Use synthetic credentials and bounded CPU/RAM.
Prove isolation before startup and preserve resources without established cleanup ownership.
Do not use host networking, privileges, production binds, or broad prune/down commands as shortcuts.

Separate syntax checks, CLI parsing, intercepted examples, isolated execution, and UI acceptance.
Assert exact status and meaningful results, not process exit alone.
Attribute reused evidence to its executor and checked state.
Run integrated acceptance on the final committed tree after startup, capability, or safety changes.
A prior full run plus narrow final regressions does not close that gate.
If the reviewer supplies the final run, keep the gap open until execution evidence exists.
Verify reported commit identities against final Git state.

## Operator-executed verification contract

Use only for an accepted, bounded responsibility amendment.
Separate plan approval, role assignment, source access, runtime approval, and product acceptance.
This contract provides neither native pause/resume support nor permission to bypass denials.

### Roles and transitions

1. Read the complete proposal, authoritative plan, exact task/parents/runs, and relevant Git state.
   Attribute approval to the current owner decision, not a proposal label.
   Give the bounded decision and distinguish it from operational release.
2. Preserve SOUL-defined roles.
   The implementer owns product changes, test orders, assessment, and commits through the mandated coding path.
   The independent reviewer chooses/assesses separate rechecks and owns the verdict.
   The operator executes authorized orders and reports original observations.
   The planner coordinates board state, routing, receipt, and release rather than taking over lifecycle tests.
   Shared execution does not permit shared test judgment.
3. Amend the versioned plan before the authoritative task body.
   Bind the card to exact plan and phase-plan Git revisions.
   Identify superseded responsibilities and unchanged gates.
   Preserve history without contradictory active instructions.
   Read back the exact body, references, status, parents, and run ownership.
4. Specify supported state/ownership during the operator interval, repository write authority,
   receipt owner, and implementation/review return.
   Verify delivery and acknowledgment before release.
   Do not invent pause/claim support, reuse run IDs, create parallel writers, or use repeated blocks as waiting.
   Preserve protective parents and never falsely complete redundant work.
5. Limit the amendment to its named phase.
   Require separate approval for infrastructure, new watchers, or additional product changes.
   Preserve denials and their real boundary.
   An unsuitable command form does not bar an otherwise authorized native read.
   Do not reassign a denied operation to bypass its guard.

Use [Kanban phase release](kanban-phase-release.md) for graph changes.
Use [Kanban triage recovery](kanban-triage-recovery.md) for blocked-card resumption and process-end checks.
An operator can close only its own card under the accepted bounded-result contract.
That closure cannot replace product review or deployment approval.

### Test orders, source freeze, and evidence

Keep orders, results, and assessments on existing Kanban cards; use native run logs for detailed output.
Require the implementer's order and the reviewer's independently chosen recheck order.
Each identifies:

- Repository, exact commit or reproducibly identified provisional diff, and test files.
- Immutable artifacts, local engine, prerequisites, commands, and expected results.
- Owned resources, limits, current preflight, and authorized cleanup.

Freeze the tested tree during each operator run and refresh resource inventory before mutation.
After provisional checks and the product commit, repeat all mandated checks on the exact final commit.
Invalidate affected evidence after changes and rerun those gates.
A frozen implementation commit can precede authorized external tests; it is not reviewed completion.

Return evidence to the ordering role.
Record ordering role/operator, timestamp, source state, actual commands, exits, and relevant original output.
Include image IDs/RepoDigests, platform, engine, isolation, and resource ownership.
State denials, errors, untested points, and exact cleanup.
Separate operator observations from implementer assessment and independent reviewer verdict.
Exclude secrets and restricted source identities from orders, board artifacts, and model prompts.

### Receipt without taking another worker's claim

Confirm the responsible planner's receipt before each role transition.
A posted comment, configured subscription, or cursor alone is not acknowledgment.

1. Read the operator card, complete result, original runs/events, and existing acknowledgment card.
   Compare exact task, run profile, claim/spawn provenance, and parent direction.
   A display name or shared profile grants no ownership of another session's claim.
2. Inspect `hermes kanban --board <board> notify-list <operator-task> --json`.
   Match platform/chat/thread/user/profile/mode and actual event-selection/wake behavior.
   Correlate cursor/ping with the terminal event received in the current conversation.
   Separate subscription, event cursor, ping, delivery, and explicit assessment.
   Claim receipt only at the observed destination.
3. If required event IDs are absent, use an authorized read-only exact-task lookup.
   Query parameterized `task_events` rows for verified task and claimed/spawned/completed events.
   Do not infer IDs, load write handlers, or repair projections with DB writes.
   If unavailable, retain the observed kind/time/run/payload association and state the limitation.
4. If canonical session evidence is required, inspect only verified session/message metadata
   and a boolean exact-task/status match through a parameterized read-only query.
   Verify routing separately without dumping chat contents or inventing IDs/foreign keys.
   Distinguish task-event ID, notification-row ID, gateway session, external post ID, and agent acceptance.
   Mark missing external post IDs unavailable; this does not negate observed internal receipt.
5. Append actual receipt and explicit assessment to the existing acknowledgment card.
   Include event/run/session association, exact result read, bounded acceptance, gaps, and next step.
   Preserve the earlier pending-receipt observation and read back the new comment.
6. Leave an active acknowledgment run/report with its owner.
   Do not complete, reclaim, redispatch, or overwrite it.
   Separate accepted operator results from the acknowledgment card's actual status.
   Keep later coding, review, and deployment gates pending.

Receipt proves neither reviewer return, runtime approval capability, nor product acceptance.
Use the recovery reference before resuming after acknowledgment completion.
Keep unsupported handoffs explicit rather than promising automatic continuation or adding watchers.
