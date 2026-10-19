# Operator script acceptance

Use this checklist when a feature already exists but operators lack a reliable setup or activation path. These are planning and acceptance requirements, not a claim that any particular installation recipe has been implemented or tested.

## 1. Establish the boundary

Record whether the request is to produce artifacts, verify them in isolation, or apply them to a live deployment. Do not seek a production host as a blocker for artifact-only work. Inventory operator-runtime prerequisites separately from developer/build prerequisites before choosing the entrypoint. Under a Docker-only production contract, host-side Java, Maven, Python installation, backend source checkout and image compilation are not acceptable setup instructions. Select a Docker-and-shell entrypoint and an already-built executable/runtime artifact; verify the package contents and availability rather than treating a candidate container recipe as tested. Keep builds on the development/build side. Include all required compiled classes, schema resources and DB-client dependencies in the delivered artifact; shipping sources that compile only when the operator invokes the command merely relocates the development requirement.

For instruction-to-script work, read the maintained instruction and existing executable/importer first, and map only its required actions to the acceptance path. Read deployment definitions and image/startup metadata only when those actions require them. Apply later activation, upgrade, UI and lifecycle checks only when those functions are explicitly in scope; this checklist must not turn a database-import script into an application-management package.

When deployment is in scope, read the maintained deployment definition and its current Git state. If the user identifies a refreshed checkout as the deployed baseline, record that provenance separately from a direct live-system inspection. Never describe the latter as performed when only repository inspection occurred.

## 2. Trace the complete operator path

For every required action, specify who performs it, the process/container boundary, permissions, inputs and an observable success condition:

| Boundary | Required planning evidence |
| --- | --- |
| Deployment selection | Explicit directory, ordered config files and project identity; reject ambiguous targets before mutation. |
| Container access | Resolve the existing project's container rather than choosing a convenient fixed name or creating a second installation. |
| Database administration | Test actual administrative access; do not assume a default role or leave authentication to manual container editing. |
| Bulk import | Reuse the existing importer; specify how its executable, dependencies, inputs and network reachability are supplied. |
| Runtime configuration | Trace settings into the actual application process; writing an unused environment file has no effect. |
| Artifact availability | Specify how operator-host images arrive; a developer's local build is not automatically present on the deployment host. |
| Activation | Confirm only intended app services restart; preserve database and unrelated dependency containers. |
| Verification | Assert exact status values and a meaningful operation, not merely successful process exit. |

### Specify configuration and noninterference before promising one-command operation

1. Trace each credential from the authorized input file or secret source to the DB client and application process. Inspect the actual variable names and selected deployment configuration; do not guess a default administrator or claim a dotenv file supplies credentials just because Compose references it. Read only the required fields, never print values or execute the file with shell `source`.
2. Name the operator-owned configuration file, required keys and exact invocation. Add a separate module config only for genuinely separate settings; do not introduce a second password store or copy existing secrets merely to simplify an example. State clearly whether the executable reads an existing config, prompts or accepts process-environment values. Document existing behavior separately from a proposed new reader.
3. Check application enablement independently of image freshness and successful data import. Trace flag and DB settings into the running process; writing a new unused env file cannot activate the feature. If the running process lacks them, disclose the needed configuration/recreation boundary and obtain approval for any changed functionality rather than silently adding restart or reconfiguration actions.
4. Limit mutations to the optional module's data and invocation-owned temporary resources. Do not restart/recreate existing app or DB services, change their credentials, alter the primary database or publish ports to satisfy an import-only path. Bound tool-container resource use on shared infrastructure; a separate database does not imply zero shared-resource risk. Check that optional datastore failure is contained by the application instead of promising noninterference from packaging alone.
5. Explain acceptance in operator terms: the documented command against a running instance, verified imported records and relevant failure/repeat checks. An isolated copy without sibling source repos proves packaging independence only; do not present it as the customer's installation workflow or as evidence of real DB execution.

### Bound preparation and acceptance before artifact checks

1. Extract the finite operator journey and safety/failure gates from the accepted plan. For each check record the user-visible outcome, expected result and the requirement or changed-code risk it proves; discard redundant proof work rather than inventing another acceptance phase. Preserve required backup, noninterference, recovery and independent-review gates.
2. List the setup artifacts needed to execute that journey: owned isolated deployment, authentic app/dependency images, input catalog, synthetic credentials and safe negative-test contexts. Assign preparation to the implementation or operator role as appropriate. Missing fixtures or target builds are unfinished team work, not automatically customer-supplied prerequisites; do not hand off a document that requires a fully prepared environment without specifying who prepares it and how.
3. Inspect the actual setup commands for conflicts with the test order's restrictions, including implicit downloads or builds. Resolve an accidental scope contradiction in the authoritative existing order; preserve genuine user restrictions and runtime approvals, and seek narrowly bounded authorization when a necessary operation exceeds them. Do not fabricate offline flags, prepared manifests or successful provisioning, and do not silently bypass a denied operation.
4. Execute the documented journey on the final tested state and return the actual results. Attribute reused evidence to its original executor and commit. Explain any remaining gap in product terms and route the specific unfinished deliverable, not an open-ended investigation.

### Artifact provenance and startup-contract preflight

1. Inventory baseline, target and dependency artifacts before promising an integrated acceptance run. Use `docker image ls` to establish local availability and narrowly formatted `docker image inspect --format '{{.Id}} {{json .RepoDigests}}' IMAGE` to identify candidates. For independently verifying an operator handoff, inspect each exact digest-pinned reference on the verified worker engine, require that reference in the actual RepoDigests and compare the separately reported Image-ID with the live Image-ID. Do not assume `.Id` equals the manifest or index digest: these describe different content objects. Record selected platform identity when applicable. Record how authorized artifacts are acquired or transferred and who supplies them. A tag, historical source checkout or locally rebuilt JAR alone does not prove the deployed baseline's image content. Treat an unauthenticated registry response as an access-boundary result, not evidence that the artifact is absent; request an authorized artifact path without putting credentials in tickets or chat.
2. Require genuine pre-feature application artifacts and functional dependency services for an upgrade-from-existing-installation gate. Keep smaller fixtures for unit/component tests, but label their limits; removing feature classes from the target build or using idle dependency containers cannot establish authentic baseline compatibility.
3. Compare the actual starter guard against the maintained and baseline build definitions (`git show BASELINE:path/to/Dockerfile`) and, when available, effective container metadata. Trace the complete `Entrypoint + Cmd`, `WorkingDir`, relevant mounts and inspected artifact path. Do not infer runtime equivalence from command spelling alone, or infer a schema-changing upgrade solely from a relative-versus-absolute path mismatch.
4. Reproduce a suspected guard mismatch against the unchanged predicate before prescribing a fix. If importing the module would execute orchestration, inspect it first and use a scratch-only probe of the relevant method with synthetic metadata and explicit dependencies; AST extraction of a reviewed method is one option. Prevent external calls, assert the exact rejection, and use a comparison case that reaches the next guard. Report this as predicate-level evidence, not container, database or end-to-end success.
5. Separate the missing-artifact boundary from the compatibility-code boundary. Record both on the existing task. If correcting a runtime guard exceeds a test/documentation-only phase, propose one narrowly scoped, independently reviewed prerequisite and obtain amendment approval before creating it. Preserve artifact, configuration and migration safety checks; do not change fixtures or build files merely to hide the production mismatch. Leave any remaining real-image compatibility checks explicitly unresolved.

### Standalone commands packaged in an application image

Use this inspection and decision procedure when a deployment wrapper should call existing backend code. It is not evidence that a proposed container invocation has already worked.

1. Locate the producer's packaging configuration and Dockerfile, then inspect the built artifact on the development side. For a Spring Boot executable JAR, a bounded inspection can use:

   ```sh
   unzip -l application.jar \
     'BOOT-INF/classes/com/example/ImportCommand.class' \
     'BOOT-INF/classes/catalog/schema.sql' \
     'org/springframework/boot/loader/launch/PropertiesLauncher.class' \
     'BOOT-INF/lib/postgresql-*.jar'
   ```

   Substitute the real class/resource names. Confirm the exact entries and bundled dependency version. A command class, resource and driver in a local JAR prove package contents, not their presence in the running deployment or a working entrypoint. Do not add a live driver download or compiler merely because an older developer instruction used one.
2. Determine the command-only launch supported by that packaging and loader version. Invoke the intended standalone main explicitly, not the application main or the image's default server entrypoint. Require a harmless help/argument check in the built image before calling the launch verified; packaged class presence alone is insufficient. Keep any necessary CLI/config-reader change small and reuse the existing business method.
3. Choose the process boundary from the noninterference requirement:

   | Placement | Mechanism and trade-off |
   | --- | --- |
   | Existing application container | `docker exec` starts another process, not another backend instance. Ordinary command failure is separate, but memory/CPU limits are shared and an OOM condition can affect the backend. |
   | Temporary container from the existing application image | Override the server entrypoint and run only the utility. Apply independent resource limits and a smaller runtime heap; no additional permanent service or bespoke tool image is inherently required. Shared host/database capacity still matters. |

   Describe this trade-off briefly rather than telling the operator another backend must start. Record the chosen contract, not a blanket rule that every utility requires a new container.
4. For a temporary job, resolve the intended application's actual local image ID and the target deployment's existing database network. Bind only required inputs/configuration read-only; do not inherit application data mounts, published ports, privileged settings or a Docker socket. No host PostgreSQL port is needed merely to reach the DB over its existing container network. Verify the required command is present before database mutation; an outdated image should produce an explicit normal-update prerequisite, not an automatic live build, pull or application restart.
5. Order producer packaging before the deployment wrapper, and retire an obsolete operator entrypoint only after the replacement has a real successful data-operation check. Keep shell-side orchestration, packaged business logic and application activation separate; do not treat an import transaction as proof that the running application received new settings.

### Authenticated registry metadata and acquisition handoff

Use after the owner confirms candidate image references and explicitly authorizes a credential source. A successful metadata check resolves the access boundary, not local image availability or compatibility.

1. Resolve the authorized profile or secret source and read only the required variables machine-side. For an explicitly supplied dotenv file, use `dotenv_values(path, interpolate=False)` rather than shell `source`; print only presence booleans. Do not display/copy the complete file, log credential values, or pass them to a coding-model prompt. Scope worker authorization to registry authentication rather than implicitly granting access to unrelated application or profile secrets.
2. Validate the registry origin before sending authentication: require the approved HTTPS hostname and port, reject URL userinfo, and disable credential-forwarding redirects. In a read-only Python probe, `urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())` supports a direct connection with redirects rejected; use it when no proxy is required. Keep authorization headers in memory, not shell arguments or diagnostic output. Select Basic or token authentication from the registry's actual challenge instead of assuming all registries behave alike.
3. Request `/v2/<repository>/manifests/<reference>` with Docker v2/manifest-list and OCI manifest/index Accept types. Bound request time and response size. Report only the approved reference, HTTP status, validated schema/media type and a syntactically valid `Docker-Content-Digest`; do not dump headers, response bodies or exception objects that could contain credentials. A metadata probe can use `GET` to validate the manifest JSON rather than accepting status alone.
4. Record source confirmation separately from technical evidence: owner-confirmed baseline, authenticated manifest availability and captured digest are distinct facts. Pin the resulting immutable reference in the plan and worker handoff. Recheck on acquisition; stop on identity drift instead of silently following a changed mutable tag.
5. Delegate actual acquisition and verification to the execution role. Use a private temporary Docker configuration outside repositories and build contexts so authentication cannot overwrite an existing user login. Supply the password machine-side through stdin, never argv; remove only owned temporary authentication files. For digest-pinned acquisition, use `docker --config CONFIG_DIR pull REGISTRY/REPOSITORY@DIGEST`, then narrowly inspect IDs/RepoDigests. Record local acquisition separately from the earlier metadata check.
6. Preserve the authentic baseline before building targets. Give feature builds distinct local names and retain baseline IDs/digests; building under the same mutable tag can destroy the very starting point the upgrade test must exercise. For manifest indexes, record the selected platform and acquired platform-image identity as well as the index digest.
7. Report the strongest completed boundary only: manifest access is not a pull, a pull is not startup compatibility, and compatibility is not end-to-end or authenticated UI acceptance. Release an approved prerequisite through the existing graph only after its next execution context and supported handoff satisfy their own entry gates; access verification alone does not resolve command-approval or ownership boundaries. Keep the successor dependency-gated and retain all remaining safety checks.

Reject an operator step that depends on an undocumented manual intervention. If a prerequisite genuinely cannot be automated, name it precisely, document the concrete preparation procedure and test that procedure.

### Operator-executed verification contract

Use only when the bounded change of verification responsibility is accepted. These are prerequisites and evidence requirements, not a tested native pause/resume recipe.

1. Preserve the original task as the shared reference. Re-read it with `hermes kanban --board BOARD show TASK --json`; check the body, actual schema, parent set and run ownership before any edit. Prepend an explicit authoritative amendment using the supported `edit TASK --body` command, preserving the still-valid original requirements below it. Read back that same task and verify body plus unchanged status/parents/runs; do not infer release from a successful edit.
2. Specify the transition contract before releasing work: who produces the test order, which supported task state and owner cover the operator interval, who may change the repository, who confirms receipt, and how implementation or review resumes. Do not fill an unresolved transition with a guessed command sequence. Preserve existing dependency protection while that contract is unresolved; waiting is not a new capability-failure retry.
3. Require a test order from the responsible implementer, and a separate recheck order from the independent reviewer. Each names the exact source commit or reproducibly identified provisional diff, test files, complete immutable image references, local engine target, commands, prerequisites, expected results, owned resource names, resource limits and authorized cleanup. Re-inventory resources immediately before mutation rather than relying on a prior snapshot.
4. Freeze the tested tree during each operator run. After provisional checks and the required product commit, repeat all mandated checks on the exact final commit. If later code changes, invalidate affected evidence and rerun the corresponding gates; do not merge pre-commit success into a final-commit acceptance claim.
5. Return the operator's evidence to the ordering role for assessment. For review checks, preserve the reviewer's independently chosen scope and own verdict; common operator execution must not become common test judgment. Confirm Delenn's receipt before each role transition through the verified communication path; a ticket comment alone is not acknowledgment and does not authorize an unrequested watcher.

| Evidence field | Required content |
| --- | --- |
| Provenance | Ordering role, operator, timestamp, repository and exact commit or reproducibly identified provisional state. |
| Execution | Actual commands, exit status, relevant original output and comparison with expected results. |
| Artifact identity | Actual image IDs, RepoDigests, platform identity when relevant and explicit local engine target. |
| Noninterference | Preflight inventory, isolation outcome and ownership of affected containers, networks, volumes, mounts and ports. |
| Limits | Preserved gates, errors, denied operations, untested points and exact authorized cleanup performed. |
| Assessment | Ordering implementer's interpretation or independent reviewer's own recheck assessment; distinguish it from the operator's execution report. |

Keep secrets out of test orders, evidence, model prompts and board artifacts. Record a denied operation as a stop with its actual boundary; do not substitute another tool or rewrite the command to bypass the approval. Separate method approval, artifact availability, operator execution, final-commit verification and independent reviewer acceptance in every handoff.

## 3. Design safe mutation and recovery

Require read-only preflight before mutation and obtain artifacts before interrupting service. Preserve existing environment-file values, Compose override ordering, mounts and service dependencies. Maintain one effective configuration across installation, status checks and later operator starts; otherwise a successful setup can disappear at the next restart.

Identify whether initialization runs only for empty data directories; adding initialization SQL does not repair an already deployed volume. Use an explicit existing-instance provisioning path for optional databases.

Scope backups to the data that will change and verify restoration, not just dump creation. Require successful backup before replacing an existing catalog, including direct import calls that bypass an install orchestrator. Separate disabling a feature from deleting its data.

Record original app configuration and image identity before changes. Detect operator edits before rewriting or restoring managed files. Limit cleanup to resources owned by the invocation. Bound external calls, serialize conflicting installs, and require clear nonzero failure results.

Do not promise image rollback as database rollback. If a proposed app replacement requires main-schema changes outside the accepted feature scope, stop and route a separate upgrade decision rather than silently widening the installer.

### Version-control protection for generated state

1. Trace where runtime state is actually written relative to each independent repository, including nested deployment directories. Cover credentials, configuration snapshots, completed dumps and partial backups; directory permissions do not prevent an accidental Git add.
2. Plan a targeted versioned ignore rule in every affected repository. Use a directory-only pattern without a root anchor when the same generated directory can appear beneath nested deployments; avoid broad `*.env` or `*.dump` rules that could hide legitimate project fixtures. One repository's `.gitignore` does not apply to a sibling repository.
3. Verify synthetic paths using `git check-ignore --no-index -v <root-state-path> <nested-state-path>` and check that the reported rule comes from the intended versioned `.gitignore`, not a global exclude or `.git/info/exclude`. Include negative controls for normal source/documentation paths. Use `git ls-files` filtered by path names to detect already tracked state without reading secret contents; escalate any match rather than automatically deleting files or rewriting history.
4. State the limits in the adjacent operator documentation: ignore rules protect untracked files from ordinary adds, not already tracked files or `git add -f`; external deployment repositories require their own rules. Update any temporary manual-exclusion wording when the versioned protection is delivered.
5. If the accepted phase permits changes in only one repository but its gate requires protection in several, stop before coding. Obtain approval for a small reviewed prerequisite in the missing repository, then link it before the existing phase; do not weaken the gate or use machine-local excludes as the delivered fix.

## 4. Make documentation testable

Put a short README next to the executable in the deployment repository and link it from the operator's usual entrypoint. Lead with only the necessary configuration file/keys, how credentials are obtained, one complete normal invocation and its result. Include real operator obligations and failure/repeat behavior, not development prerequisites or hypothetical password-management tasks. Explain maintenance windows, later starts, recovery and UI only when those operations are in the accepted contract. Keep detailed architecture and historical procedures separate so the operator need not read them to run the command.

Execute the accepted path against a safely owned running instance and record actual artifact identities and limits. For import-only work, verify the documented invocation, resulting records, relevant target/input/backup failures and repeat behavior, with targeted evidence that primary data and existing services remain unchanged. Build a full populated application fixture and exercise activation, UI or lifecycle transitions only when those functions are explicitly contracted; do not make them prerequisites for a database import.

Distinguish Bash syntax checks, real CLI parsing, intercepted mutation examples and live isolated execution in each handoff; a documentation verifier that intercepts actions proves syntax/argument handling, not operator success. API/container checks and GUI artifact inspection do not prove an authenticated UI workflow. Carry those remaining gates into the agreed end-to-end phase rather than silently treating them as covered.

Run the integrated acceptance path on the final committed tree after changes to startup, capability or safety gates; a previous full run plus narrow final regression tests can miss interactions. If the full run is deferred to the independent reviewer, name that exact gap in the handoff and keep it unresolved until the reviewer supplies execution evidence. Verify source/commit identifiers against the final repository state rather than copying a pre-amend evidence document's hash.

For Compose tests, re-inventory all existing containers, network/volume ownership and host listeners before fixture creation; an earlier port listing is not a reservation. Override every fixed container name, published port and persistent host path with owned test resources; project naming alone is insufficient. Prefer no published ports, otherwise use free loopback-only bindings. Use synthetic credentials/configuration, bound CPU/RAM use, and prove isolation before starting the fixture. Preserve pre-existing services and even earlier test resources unless ownership and cleanup authorization are established; never use host networking, privileged containers, production bind paths or broad prune/down commands as a shortcut. Free RAM/disk and available images establish prerequisites, not noninterference or successful lifecycle execution.
