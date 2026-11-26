# Operator script acceptance

Trigger: accepted operator setup, import, or activation path. This procedure grants no deployment authority and supplies no execution evidence by itself.

## Establish the execution boundary

1. Separate artifact creation, isolated verification, and live application. Record approved test targets and deployment exclusions in plan and phase cards. Artifact-only work needs no production host. Historical host permissions do not carry forward.
2. Read maintained instructions and existing importer first. Map required actions to actors, inputs, resources, and observable results. Inspect only relevant deployment/startup wiring. Do not expand import automation into application-lifecycle management. Distinguish user-confirmed deployed checkout from direct live inspection.
3. Docker-only operator host: require only Docker and ordinary shell facilities. Keep language runtimes, source checkout, compilation, and image builds on the development side. Put entrypoint and short README in the deployment repository.
4. Invoke the producing module's packaged business logic. Do not copy sources or add a parser. Name the chain: host script → producing artifact → command process/container → database. Identify exact repositories, services, images, and paths as existing, proposed, or execution-verified.

## Configuration and process boundaries

1. Resolve deployment directory, ordered config files, project identity, and existing container. Reject ambiguous targets before mutation. Verify administrative access. Do not assume a default role.
2. Name operator configuration, required keys, and normal invocation. Trace authorized credentials/settings into DB client and app process. Read only necessary fields. Do not print secrets or execute dotenv files with shell `source`. Avoid duplicate password stores. Distinguish existing readers from proposed behavior.
3. Inspect producer packaging, built command, resources, and dependencies. Verify command-only launch with a harmless help/argument check in the built image. Image contents alone prove no deployment availability or execution. Do not add obsolete developer-recipe compilation/downloads to the live path.
4. Choose placement by isolation needs. In-app container processes share its limits and can starve the app. Temporary containers can have separate limits but share host/database capacity. Override the temporary server entrypoint to run only the utility. Require no permanent service or bespoke image without need.
5. Temporary jobs: resolve actual local image ID and existing DB network. Mount only required inputs/config read-only. Exclude app data mounts, published ports, privileges, and Docker socket. DB access on the container network needs no host port. Verify command availability before mutation. Treat outdated images as update prerequisites, with no implied live builds, pulls, or restarts.
6. Deliver producer packaging before its wrapper. Retire old entrypoint only after a successful real data-operation check. Include container access, authentication, and verification in the executable path. Document and test unavoidable manual preparation.

- Import-only: mutate only module data and invocation-owned resources. Do not recreate app/DB services, change credentials, alter primary data, or publish ports.
- Contracted activation: verify flags and DB settings in the running process. Edited env files or fresh images alone prove no enablement. Disclose restarts/recreation and obtain approval for changed functionality. Preserve unrelated services/dependencies.
- Optional-data failure containment: load [External-data discovery](data-discovery.md#optional-data-features).

## Artifact provenance and startup-contract preflight

1. Before integrated acceptance, inventory baseline, target, and dependency artifacts. Assign acquisition/transfer to an authorized role. Inspect exact immutable references on the verified worker engine. Require actual `RepoDigests`. Compare reported and live Image-IDs separately. Distinguish image, manifest, and index digests. Record selected platform and acquired platform-image identity where relevant. Tags, checkouts, and local builds do not prove deployed content.
2. Upgrade acceptance needs authentic pre-feature artifacts and functional dependencies. Do not substitute stripped target builds or idle placeholder services. Label component fixtures by actual scope. Preserve baseline identity and use distinct target-build names to prevent tag overwrite.
3. Compare startup guards with maintained and baseline build definitions via `git show BASELINE:path`. Trace `Entrypoint + Cmd`, `WorkingDir`, mounts, and artifact paths. Path spelling does not prove incompatibility or a schema-changing upgrade.
4. Before proposing fixes, reproduce suspected mismatch against the unchanged predicate. If imports start orchestration, use an inspected scratch-only predicate probe with synthetic inputs. Prevent external calls. Include a control that reaches the next guard. Report predicate evidence separately from container/database execution.
5. On the existing card, distinguish artifact-access blockers, compatibility-code blockers, and outstanding real-image checks. Obtain amendment approval and independent review for out-of-phase fixes. Do not hide production mismatches through fixture/build-definition changes.

### Authenticated registry metadata and acquisition handoff

Prerequisites: owner-confirmed candidate references and authorized credential source.

1. Read only needed registry credentials machine-side, without dotenv execution or interpolation. Exclude unrelated secrets and keep credential values out of prompts, argv, reports, and diagnostics.
2. Validate approved HTTPS origin/port before authentication. Reject URL userinfo and credential-forwarding redirects. Follow actual authentication challenge. Keep headers in memory. Bound time and response size.
3. Request `/v2/<repository>/manifests/<reference>` with Docker/OCI manifest/index Accept types. Validate schema/media type and `Docker-Content-Digest` syntax. Report only approved reference, status, type, and digest. Do not dump bodies, headers, or secret-bearing exceptions. An unauthenticated response establishes an access boundary only.
4. Distinguish owner confirmation, authenticated availability, and digest capture. Pin immutable references in plan/handoff. Stop if identity drifts at acquisition.
5. Execution role: use private temporary Docker authentication outside repositories/build contexts. Pass passwords on stdin. Preserve existing logins. Pull pinned references and verify local IDs, RepoDigests, engine, and platform. Remove only owned temporary auth files.
6. Distinguish metadata access, acquisition, compatibility, and end-to-end acceptance. Provisioning elsewhere does not establish the next worker's command-approval capability. Keep successors gated until execution context and handoff meet entry conditions.

## Safe mutation and recovery

1. Before interrupting services, complete read-only preflight and acquire artifacts. For an irreversible replacement, also confirm the authorized credential delivery path for provisioning and authenticated acceptance in the actual executing context before retiring the old instance. Check only presence, never values; an interactive login or a successful disposable run does not establish delivery to a managed worker. Preserve environment values, Compose override order, mounts, dependencies, and later-start configuration. Provide existing-instance provisioning. Empty-directory initialization SQL does not provision existing volumes.
2. Back up affected data and verify restoration. Require backup before catalog replacement, including direct importer calls. Record original configuration/image identity and check for operator edits before rewriting or restoring files.
3. Serialize conflicting operations and bound external calls. Return clear nonzero failures. Clean only authorized invocation-owned resources.
4. Keep disablement separate from deletion and image rollback separate from DB rollback. Route out-of-scope main-schema changes to a separate upgrade decision.

### Version-control protection for generated state

1. Inventory generated credentials, config snapshots, complete dumps, and partial backups in every affected repository, including nested deployments. Directory permissions alone cannot prevent staging.
2. Add targeted versioned ignore rules per owning repository. Use unanchored directory-only patterns at multiple depths. Avoid broad extension rules that hide legitimate fixtures.
3. Test synthetic root/nested paths with `git check-ignore --no-index -v`. Require matches from the intended versioned `.gitignore`. Global/local excludes cannot satisfy the gate. Include normal source/docs paths as negative controls. Inspect `git ls-files` names without reading secrets. Escalate tracked matches without deleting data or rewriting history.
4. Explain that ignores cannot protect tracked files or paths staged with `git add -f`. Sibling repositories need their own rules. Replace obsolete manual exclusions when versioned protection is delivered.
5. If approved file scope cannot satisfy the gate, obtain approval for the missing repository prerequisite. Retain independent review and the gate. Machine-local excludes cannot substitute.

## Real operator acceptance

1. Define a finite journey from accepted outcomes and safety gates. Bind each check to a requirement or concrete changed-code risk. Assign bounded fixture/artifact prep to the appropriate team role. Inspect setup commands for hidden builds/downloads and contradictory order. Correct accidental contradictions in the authoritative order without bypassing restrictions.
2. Link a short README beside the entrypoint from the operator's usual starting point. Lead with required keys, credential sourcing, one complete invocation, results, and failure/repeat behavior. Include maintenance, activation, UI, and lifecycle only when contracted. Keep architecture/history outside the normal path.
3. Before fixture creation, re-inventory Docker endpoint, capacity, containers, networks, volumes, mounts, and listeners. Replace fixed names, tags, ports, and host paths with owned test resources. Verify isolation beyond Compose project naming. Prefer no published ports. Otherwise use free loopback-only bindings. Use synthetic credentials and bounded CPU/RAM. Prove isolation before startup and preserve resources without established cleanup ownership. Do not use host networking, privileges, production binds, or broad prune/down commands as shortcuts.
4. Run the documented commands against a safely owned running target. For import-only, verify records, relevant target/input/backup failures, and repeat behavior. Prove primary data and existing services unchanged. Require populated full-app fixtures and authenticated UI/lifecycle checks only for contracted functions. A source-independent package copy proves packaging independence only.
5. Separate syntax, CLI parsing, intercepted examples, isolated execution, and UI acceptance. Assert exact status and meaningful results beyond exit alone. Attribute reused evidence to executor and checked state. After startup, capability, or safety changes, run integrated acceptance on the final committed tree. A prior full run with narrow final regressions leaves the gate open. If reviewer supplies the final run, wait for execution evidence. Verify reported commits against final Git state.

## Operator-executed verification contract

Prerequisite: accepted bounded responsibility amendment. Separate plan approval, role assignment, source access, runtime approval, and product acceptance. This contract grants neither native pause/resume nor a denial bypass.

### Roles and transitions

1. Read complete proposal, authoritative plan, exact task/parents/runs, and Git state. Attribute approval to the current owner's decision, never a proposal label. State the bounded decision separately from operational release.
2. Preserve SOUL-defined roles and independent judgment:
   - Implementer: product changes, test orders, assessment, and commits through the mandated coding path.
   - Independent reviewer: choose and assess separate rechecks, own verdict.
   - Operator: execute authorized orders, report original observations.
   - Planner: coordinate board state, routing, receipt, and release. Leave lifecycle tests with their owner. Shared execution does not authorize shared judgment.
3. Amend versioned plan before authoritative task body. Bind exact plan and phase-plan Git revisions. State superseded duties and unchanged gates. Preserve history without conflicting active instructions. Read back exact body, references, status, parents, and run ownership.
4. Specify supported state/ownership during operator interval, repository write authority, receipt owner, and implementation/review return. Verify delivery and acknowledgment before release. Do not invent pause/claim support, reuse run IDs, create parallel writers, wait through repeated blocks, or falsely complete redundant work. Keep protective parents.
5. Limit amendment to named phase. Obtain separate approval for infrastructure, new watchers, or additional product work. Preserve denials and their actual boundaries. If only the command form is unsuitable, use an otherwise authorized native read. Do not reassign a denied operation to bypass its guard.

Use [Kanban phase release](kanban-phase-release.md) for graph changes and [Kanban triage recovery](kanban-triage-recovery.md) for blocked-card resumption and process-end checks. An operator may close only their own card under the accepted bounded-result contract. Product review and deployment approval remain separate.

### Test orders, source freeze, and evidence

- Existing cards hold orders, results, and assessments. Use native run logs for detail. Require the implementer's order and the reviewer's independently chosen recheck order.
- Each order: repository, exact commit or reproducibly identified provisional diff, test files, immutable artifacts, local engine, prerequisites, commands, expected results, owned resources, limits, current preflight, and authorized cleanup.
- Freeze the tested tree during each operator run. Refresh resource inventory before mutation. After provisional checks and product commit, repeat all mandated checks on the exact final commit. Invalidate affected evidence after changes and rerun those gates. A frozen commit can precede authorized external tests. Reviewed completion still needs a verdict.
- Return evidence to ordering role: ordering role/operator, timestamp, source state, actual commands/exits, relevant original output, image IDs/RepoDigests, platform, engine, isolation, and resource ownership. Include denials, errors, untested points, and exact cleanup. Distinguish operator observations, implementer assessment, and reviewer verdict.
- Keep secrets and restricted source identities out of orders, board artifacts, and model prompts.

### Receipt without taking another worker's claim

Prerequisite to each role transition: confirmed receipt by the responsible Planner. Comment, subscription, or cursor alone cannot establish acknowledgment.

1. Read operator card, complete result, original runs/events, and existing acknowledgment card. Compare exact task, run profile, claim/spawn provenance, and parent direction. A shared profile or display name grants no ownership of another session's claim.
2. Read `hermes kanban --board <board> notify-list <operator-task> --json`. Match platform/chat/thread/user/profile/mode and actual event-selection/wake behavior. Correlate cursor/ping with terminal event received in this conversation. Distinguish subscription, event cursor, ping, delivery, and explicit assessment. Claim receipt only at the observed destination.
3. Missing required event IDs: use authorized read-only exact-task lookup. Query parameterized `task_events` rows for verified task and claimed/spawned/completed events. Do not infer IDs, load write handlers, or repair projections with writes. If unavailable, retain observed kind/time/run/payload association and state the limitation.
4. Required canonical session evidence: query only verified session/message metadata and a boolean exact-task/status match, using parameterized read-only lookup. Verify routing separately. Do not dump chat or invent IDs/foreign keys. Distinguish task-event ID, notification-row ID, gateway session, external post ID, and agent acceptance. Mark missing external post IDs unavailable. Preserve observed internal receipt.
5. Append receipt and explicit assessment to existing acknowledgment card: event/run/session association, exact result read, bounded acceptance, gaps, and next step. Preserve earlier pending-receipt observation. Read back the new comment.
6. Leave active acknowledgment run/report with its owner. Do not complete, reclaim, redispatch, or overwrite it. Keep accepted operator results separate from actual acknowledgment-card status. Keep later coding, review, and deployment gates pending.

Receipt establishes neither reviewer return, runtime approval capability, nor product acceptance. Load the recovery reference before resuming after acknowledgment completes. Report unsupported handoffs without promising automatic continuation or adding watchers.
