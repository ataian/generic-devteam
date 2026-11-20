# User-triggered team file updates

## Scope and boundaries

- **Trigger:** The user asks to check and apply Maker changes to existing teams. Do not repeat setup, run a new setup or pipeline test card, or recreate a team.
- **Inputs:** Use the single JSON block in each private `devteam/setup.md` as the sole raw-value source for `confirmed_values` and `confirmed_bindings`. Descriptive sections hold evidence references. Resolve missing or contradictory required bindings and actual target drift before affected writes. Correct stale prose from readbacks without repeating confirmed choices or successful creates. Do not rewrite private records just to adopt the simplified template.
- **Source:** Python 3.11 or later, local Git, and the Maker repository with history. Use package SemVer for the release and the exact Git commit for the source revision. The record `schema` identifies the data format. An exported skill tree without Git history cannot resolve old revisions for comparison or rollback.
- **Authority:** The file helper changes managed files only. It does not change models, plugins, integrations, configuration, or external services. Use separate approved steps for [Planner Kanban binding](#planner-kanban-tools), [upstream companion update](#required-upstream-companion-update), [CAC migration](#cac-migration), and [skill retirement](#required-skill-retirement).
- **Limits:** No cron job, watcher, worker stop, or session restart.
- **Order:** Discover → record if needed → recover interrupted work → inspect companions and migration → propose and inspect retirement → approve scope and activity → satisfy prerequisites → apply → retire → verify per team.

## Discover teams

- **Prerequisite:** Check your own wrapper or a local adaptation under [Maker wrapper](main-agent-wrapper.md).

1. **Resolve homes.** Check installed CLI help before invoking a native inventory command. Inspect native profiles and actual resolved homes.
2. **Save inventory.** Write a private JSON array of `{"id": "actual-id", "home": "/actual/profile/home"}` objects. Include all native profile homes, including custom and default homes.
3. **Discover and resolve.** Run:

   ```sh
   python3 -B references/update_team.py discover --homes /private/native-homes.json
   ```

   The helper checks `devteam/installation.json` and `devteam/setup.md` in supplied homes, without deriving paths from profile names. It reports invalid records per home so other teams can proceed. For an unmarked team with a separately known setup record, inspect that record and its native role bindings before claiming discovery. Keep no central registry.

## Record a new team

- **Prerequisites:** Completed setup delivery and configuration/file readbacks. Generate the bound recovery launcher through `references/bind_recovery.py` before `init`.

1. **Confirm role mappings.** Save actual role IDs and canonical homes under `confirmed_bindings.roles` in the setup JSON. Use keys `planner`, `coder`, `reviewer`, and `team-codex` with fields `id` and `home`. Keep IDs distinct from display names. For `team-codex`, bind the actual process HOME separately from `CODEX_HOME`. Owned Codex skills map to `<process HOME>/.agents/skills/`; Hermes skills map to `<role home>/skills/`.

   ```json
   {
     "planner": {"id": "planner-id", "home": "/actual/planner-home"},
     "coder": {"id": "coder-id", "home": "/actual/coder-home"},
     "reviewer": {"id": "reviewer-id", "home": "/actual/reviewer-home"},
     "team-codex": {"id": "team-codex-id", "home": "/actual/codex-process-home"}
   }
   ```

   This object is the value of `confirmed_bindings.roles`. If existing setup uses another binding layout, pass the same verified object through `--roles /private/roles.json`. Keep secrets out of setup JSON and updater arguments.
2. **Bind the revision.** Inspect `git status --porcelain` before selecting the source. Require a clean, reviewed Maker checkout. Use its committed `HEAD` and exact target readbacks of all personalized SOULs and complete manifest-owned skill trees. Run:

   ```sh
   python3 -B references/update_team.py init --home /actual/planner-home --team-id actual-team-id
   ```

3. **Read the baseline.** `init` writes baseline metadata only. Check `installation.json` for package version, full commit, role IDs/homes, nonsecret setup values, explicit mappings, transform names, baseline hashes, and installed hashes. Pristine personalized Maker output lives separately in `baselines/<sha256>`; local target edits never become the Maker baseline.
4. **Check modes.** Private directories use mode 0700. Private records, proposals, baselines, and backups use mode 0600. Content updates preserve existing local target modes. New regular targets use mode 0600. New skill helpers with Git mode `100755` use mode 0700, without group or other access. Application and rollback verify proposal-bound bytes and modes before advancing the record.

## Record an existing team

- **Prerequisite:** Read the existing setup evidence before choosing a baseline.

1. **Documented full-tree baseline.** If setup proves an exact source revision and covers all managed skill copies, use that commit and cite the evidence. A package version alone cannot prove an exact revision. If skill coverage is missing, withhold this path.

   ```sh
   python3 -B references/update_team.py init --home /actual/planner-home --team-id actual-team-id \
     --base-commit FULL_40_CHARACTER_COMMIT \
     --basis-evidence 'Setup record section and original copy/hash evidence for all managed files'
   ```

   This path preserves local changes and records provenance as `documented-setup-baseline`. The helper records the evidence without authenticating the historical claim.
2. **Unrecorded legacy team.** For a team without a version or installation record, use the explicit user-defined SOUL safepoint:

   - Package release: `1.0.0`.
   - Source revision: `21cae6551c03b6ab84d004f41fc81c921e3e9837` (28 October 2026).
   - Provenance: `user-defined-1.0.0-safepoint`.
   - Historical installation verification: `false`.

   ```sh
   python3 -B references/update_team.py legacy-baseline
   python3 -B references/update_team.py init --home /actual/planner-home --team-id actual-team-id --legacy-souls
   ```

   Use this safepoint even if the updater's introduction commit differs. The legacy path manages only the three SOULs and preserves their local drift through the normal three-way comparison. It reports old skills as `baseline unknown; withheld` on every update. Keep them outside automatic updates until their own source evidence or a specific reconciliation is approved.

## Prepare and review one team

- **Prerequisites:** Confirm team bindings and an exact target. Check recorded pending work first. On an interrupted run, use [Failure and rollback](#failure-and-rollback) before preparing another update. A verified file result can remain in place while pending companions resume.

1. **Inspect the full scope.**
   - Inspect all assigned assets under [Required upstream companion update](#required-upstream-companion-update). Inspect [Planner Kanban tools](#planner-kanban-tools) before approval. Compare even for a same-version or no-op file proposal.
   - For CAC targets, inspect [CAC migration](#cac-migration), including pending work. When [Workflow migration](#workflow-migration-200) applies, include its card inspection in scope. Settle old-contract work, parked cards, and local authority within the approved migration before changing workflow authority.
   - For Planner-only `prototype`, use [its delivery recipe](integrations.md#prototype) for collisions, complete-tree loading, dependent SOUL clauses, and local-rule reconciliation.
   - For `diagnosing-bugs`, inspect collisions through [the owned-skill recipe](integrations.md#diagnosing-bugs) before the normal proposal. Include its complete tree and dependent Coder call clause in the same approval. Resolve missing bindings or local conflicts before application. The legacy SOUL-only path still withholds unknown-baseline skills. Reconcile required diagnosis delivery in scope before applying dependent policy. Withhold dependent outputs until delivery and native loading are verified, even if metadata advanced. Read back its complete saved tree, unambiguous Codex discovery, and the Coder's explicit call policy separately. Saved files and discovery do not establish actual diagnosis behavior.
2. **Resolve missing legacy bindings before planning.** The Maker/operator uses confirmed evidence, without repeating setup. Withhold the affected proposal if required evidence remains missing.

   | Trigger | Confirmed values and guards |
   |---|---|
   | Pre-`1.1.4` role fields | Transfer the confirmed workspace and repository boundaries into `confirmed_values.PROJECT_DIR` and `confirmed_values.REPOSITORY_ROOTS` in the existing setup JSON. Keep planning and implementation assignments separate in its single-line text. Preserve multiple repositories and nested checkouts. Record confirmed absence if no repository exists. Never derive paths from project name or current working directory. Report unresolved bindings to the operator. Do not assign reconciliation to the Planner or Coder. |
   | Pre-`2.9.0` Codex paths | Transfer the verified absolute stable entrypoint and process/config homes into `CODEX_BINARY`, `CODEX_PROCESS_HOME`, and `CODEX_HOME` in `confirmed_values`. Use existing setup evidence and configuration readbacks. Keep the stable entrypoint even when it resolves to a version-specific release target. Match process HOME to `confirmed_bindings.roles.team-codex.home`. Resolve missing or conflicting paths before planning. |
   | Missing recovery binding | Resolve from confirmed setup and dispatcher evidence. Save `confirmed_bindings.triage_recovery` in the existing private setup JSON and keep `confirmed_bindings.roles` equal to the recorded roles. Do not assign this to the Planner or replace unknown local launcher edits with a generic copy. The helper adopts the missing binding into the proposal and installation record. With a recorded binding, it preserves it without reading `setup.md`. |

   Role-value adoption fills only missing fields from the setup JSON. The updater reuses the recorded Planner ID when `PLANNER_PROFILE` is absent and rejects a conflicting ID. It preserves recorded values, saves adopted ones only after successful target verification, and uses them on later updates without reading `setup.md`.
3. **Generate and inspect the proposal.**

   ```sh
   python3 -B references/update_team.py plan --home /actual/planner-home --target HEAD
   ```

   - **Comparison:** The helper saves a private proposal and prints its path and contents. It uses the old pristine baseline, current target, and new personalized output. It merges nonconflicting text with `git merge-file`. Text conflict, missing local files, or incompatible source mappings stop application.
   - **Mappings:** New files in managed trees enter automatically. New owned skills use the same existing whole-tree mapping from `own_skills.targets`, including Team-Codex's process-HOME `.agents/skills/`. The helper does not manage upstream Graphify/CBM integrations, MCP configuration, hooks, or indices.
   - **Launcher:** The manifest's `recovery_launcher` uses `bound-recovery-v1` instead of `copy-v1`. The updater renders both baselines with recorded `confirmed_bindings.triage_recovery`, keeps it on template renewal, and compares local changes to the bound baseline.
   - **Renderer:** Accept the exact reviewed pre-1.1.4 renderer by source hash. It adds role fields without changing old substitutions. The helper still verifies each old personalized baseline against stored bytes. It also accepts the exact reviewed pre-2.9.0 renderer, with shell quoting limited to new Codex path fields. Withhold other renderer changes pending transform compatibility review.
   - **Obsolete:** The helper lists removed source files and deassigned managed skill copies as `obsolete` with role, identity, resolved root, and local state. It deletes nothing. Inspect and scope [required skill retirement](#required-skill-retirement) before applying, then finish it afterward. Retain obsolete files that are not managed skill copies, and retain local adaptations.
4. **Review semantics.**
   - Read the proposal and changed SOULs and skills alongside neighboring instructions and local rules. Decode `new_base` and `merged` as base64 for programmatic byte checks. Record a concrete semantic review finding. A clean text merge cannot establish compatibility.
   - For Reviewer proportional investigation, inspect direct/parallel selection, helper limits, exact code/plan binding, and conditional critical-invariant pass credit in the rendered SOUL. Preserve confirmed local model/reasoning and resource policies. This method adds no skill tree, helper profile, runtime setting, or companion installation. Preserve native `sdlc-review` management and preload. After application, read back the full SOUL and subsequent-context loading under [Verification](verification.md). Saved files cannot establish live helper behavior.
   - If a conflict remains, preserve the proposal and resolve affected local sections against exact source revisions within the approved mandate. Prepare and review a new proposal. Never edit proposal payloads to bypass conflict.
5. **Record scope decisions.**
   - If operational recipes or upstream component metadata changed, tell the user the effect and recommendation. Obtain their approve/defer decision for dependent files. Withhold the whole team proposal until recorded. Use `--dependency-decision` only to record that decision. Runtime configuration and integration changes need their applicable authorization.
   - For Planner skill maintenance, report the separate configuration step in [Setup](setup.md#3-fresh-profiles-confirmed-models). The updater delivers the Planner template change. Obtain separate authorization to set and read back `skills.creation_nudge_interval=0` in the existing Planner profile.

## Planner Kanban tools

- **Trigger:** Check availability on every requested team update, including same-version and no-op file updates.
- **Interface:** Use native scope, commands and complete readbacks in [Planner Kanban tools](setup.md#planner-kanban-tools). The file helper does not enable tools or change native configuration. Installation metadata cannot certify the binding.

1. **Inspect and approve.** Include missing Planner tool selections in the complete update scope before approval. Obtain authorization before changing native configuration. `--dependency-decision` alone does not grant it.
2. **Back up and enable.** Back up the affected configuration and native tool selections in the existing private update area. Preserve unrelated enabled and disabled tools, global suppression entries, and MCP bindings under the setup recipe. Recheck for concurrent drift before enabling only the missing authorized selections through the native commands.
3. **Verify and record.** Read back all three platform selections and compare preservation against captured state. Save and read back completion evidence in the existing private setup/update record. Keep the binding `pending` if authorization, availability, or preservation remains unresolved, even after the Maker version advances. Report `files updated; team update incomplete` while it remains pending. Configuration readbacks cannot establish adoption by running sessions.

## Required upstream companion update

- **Trigger:** Compare every assigned upstream asset on every requested team update, even when the Maker version is unchanged.
- **Inventory:** Independently delivered skills, all six VoltAgent TOMLs, complete plugins, and selected analysis assets. Include Superpowers, grill-me/grilling/domain-modeling/to-questionnaire, Hindsight adapter, Ponytail in both harnesses, find-skills, and the selected CBM or Graphify integration. Assess Team-Codex CLI target/reuse separately from asset replacement.
- **Source:** Read `source_revision` or inherited `source_component`, `subpaths`, legal files, mappings, and hashes from the target Maker manifest. Use exact commits without a fresh latest-version search. For the Planner's domain tree include `GLOSSARY-FORMAT.md`, `ADR-FORMAT.md`, `agents/openai.yaml`, and all legal files. Include the complete original `to-questionnaire` tree, its `agents/openai.yaml`, and root MIT license. Use the Planner-only [complete-tree recipe](integrations.md#grill-me) for both.
- **Authority:** Pins are source targets, not operational permission. Keep Hermes core and its distribution skills native-managed and outside Maker updates. Keep the Hindsight service untouched. Role templates and `own_skills` use the file helper. Route existing-team Team-Codex instruction writes and legacy Caveman reconciliation through [CAC migration](#cac-migration), including approval and activity checks. Use the integration recipe there for delivery and readback.
- **Record:** Use pending/completed evidence in the team's existing private `devteam/setup.md` progress/update sections. Keep no separate registry or helper schema.

1. **Inspect:**
   - **Consumers:** Resolve every assigned consumer, native registration/discovery root, and actual source and target before any write. For the selected CBM or Graphify branch, inspect Planner, Coder, Reviewer and Team-Codex even when installation metadata is already current. Include previously retired Reviewer analysis assets and missing MCP/CLI, cache, CWD, hook or discovery bindings in the concrete companion scope. Preserve the confirmed alternative and nonselected assets; do not silently re-select.
   - **Assets:** Compare installed assets to exact required commits and complete file/byte inventories, including hidden files, companions, legal files, and local additions. Neither name, version nor earlier review establishes a match. Check native loading, duplicate/shadowed paths, ownership, modes, symlinks, and shared consumers.
   - **Runtime:** Read CBM/Graphify runtime and Team-Codex binary paths, versions, and shared use separately. Preserve compatible runtimes and avoid automatic version changes to enforce pins. Do not blindly upgrade or downgrade a reused matching/newer CLI. If a capability is unavailable, name the runtime/asset mismatch and required update/defer decision.
   - **Evidence:** Record missing historical provenance as unknown; never invent an installed revision or pristine baseline. Verified current bytes can serve as a pre-change backup. Before file application, record pre-update Maker version/commit and per-component required/observed sources, differences, proposed actions, and `pending`. Preserve earlier pending evidence if metadata advanced.
2. **Approve:**
   - Present full file and companion scope with concrete paths, source/target versions, local-edit decisions, and native binding changes. Obtain advance explicit approval once for the complete concrete plugin/runtime/CLI change set.
   - Include any full Superpowers, Ponytail, or Hindsight-adapter update even for apparently profile/team-local changes. Disclose dependency resolution, shared Hermes PM generations, and other affected consumers. Include proposed CBM/Graphify runtime and Team-Codex CLI changes with actual paths, versions and shared effects, plus required autoload, hooks, MCP, and old team-owned registration replacements.
   - Preserve local edits unless exact reconciliation is approved. One approval covers the approved batch. Record approval or deferral before mutations. `--dependency-decision` records the dependent-file decision only.
3. **Back up:**
   - Save complete affected installed trees and native bindings outside all discovery roots. Preserve bytes/hashes, inventories, ownership, modes, link metadata and original provenance evidence, and track runtime state separately. Compare complete backup inventories and bytes to inspected targets. Record verified backup paths and supported restoration route before replacement.
4. **Apply:**
   - Recheck targets and bindings for concurrent drift immediately before writes. Stop on any difference. Apply only approved changes via [Integrations](integrations.md) and the selected [analysis recipe](code-analysis.md).
   - Restore missing selected Reviewer assets and native bindings through the selected analysis recipe within the approved companion scope. Keep complete upstream bytes unchanged, including model/reasoning fields, plugin manifests, and skill instructions. Limit shared runtime/PM mutations to the concrete approved scope. Do not bootstrap or repair Hermes as a prerequisite.
   - Complete required assets and native loading before applying dependent role/skill file changes. If an asset, approval or compatible runtime is unavailable, withhold dependent outputs and keep the companion `pending`. After file application, read back personalized scope/use clauses through existing recipes.
5. **Verify:**
   - Compare every delivered source/target path and byte to the required commit, including complete file sets and legal files. Read back native registration, actual loaded source paths, required main/reference content, and affected configuration/hooks for each consumer. Verify unaffected roles/shared consumers against the pre-change inventory.
   - Distinguish exact asset matches, compatible runtime reuse, unresolved provenance, and unverified running-context loading. Mark each companion `complete` only after required readbacks pass. Save and read back the evidence. Keep selected-analysis work pending until required Reviewer assets, configuration and native discovery readbacks pass.
   - Resume from the backup, prior pending evidence, and actual native state even after the Maker version advances. Report `files updated; team update incomplete` while required companion work is pending or deferred.
6. **Rollback:**
   - The file-helper rollback does not restore companion assets or native bindings. Obtain restoration scope and inspect current bytes/bindings for later edits before restoring from the verified backup. Restore only recorded affected trees, modes and native registrations/configuration. Preserve later work and shared assets. Restore runtime or PM generations only through supported routes with explicit shared-effect approval.
   - Read back restored files, native registration/loading and unaffected consumers separately from helper rollback. Record restoration and renewed `pending`. Deletion and service/session restarts require separate authorization.

### VoltAgent original files

- **Prerequisites:** Use [the original-file recipe](integrations.md#codex-agents). Read the target Maker manifest's `codex-custom-agents.source_revision`, `subpaths`, and `legal_files` for the inventory. The file updater does not manage the six upstream TOMLs.

1. **Compare and approve.** Compare all six installed files with the required revision at every update. Include replacement of old Maker model/reasoning overrides with unchanged originals in explicit team-update approval. Resolve other local edits or conflicting customer rules before replacement. Preserve unresolved files. If required runtime capability is absent, defer the dependent proposal.
2. **Back up and replace.** Back up all six installed files and record their paths, bytes/hashes, modes, and source provenance before authorized replacement. Recheck drift before writing and preserve ownership and modes.
3. **Verify or resume.** Keep the companion update pending until all six files match the pinned originals and native discovery/access readbacks pass. Record revision, matching hashes, and completion in the existing private update record. Resume pending work on later updates.
4. **Restore if authorized.** Check drift, restore the verified backup, and read back restored files.

### Historical Caveman targets

- **Trigger:** Only an explicitly selected pre-CAC Maker target whose manifest assigns legacy Caveman skills. For CAC targets, use [CAC migration](#cac-migration).

1. **Inspect and approve.** Check each assigned consumer using the `caveman` anchor in the exact historical target's `references/integrations.md`. Include exact skill targets, source revision, autoload changes, backups, and readbacks in explicit team-update authorization. Use the companion guards above. Preserve local adaptations and historical tickets.
2. **Deliver and verify.** Use that historical recipe outside the file helper. Defer dependent SOUL changes until required skills and loading bindings are verified. After application, read back each delivered scope clause and the Coder's per-task propagation. Record subsequent-context loading separately. Do not restart sessions or claim that running contexts adopted the change.

## CAC migration

- **Trigger:** A target that delivers CAC. Check every requested update, including same-version and no-op file proposals.
- **Authority:** Use the approved team-update scope for CAC delivery and legacy retirement. The file updater does not install Caveman skills, change `skills.auto_load`, write Codex home instructions, or retire external trees. Use the approved companion route for those actions.
- **Fresh activity evidence:** Use an established read-only projection of the confirmed board and dispatcher. Read actual runs and claims, including `current_run_id`, `claim_lock`, run profile and `ended_at`. If needed and permitted, check the installed `hermes_cli.kanban_db.list_tasks` and `list_runs` read path for side effects before using it in one read transaction on the bound SQLite DB opened with `mode=ro`. The CLI `kanban list` can recompute readiness.
- **Activity guard:** Check actual worker, dispatcher, and session activity for all affected roles and Team-Codex contexts, including work outside the board. Record board, runs, claims, contexts, and observation times. If a context still needs the affected contract, a new claim has unresolved ownership or loading, or material activity evidence is unresolved, defer affected writes and keep them pending. A missing projection, inaccessible state, or no visible PID cannot establish inactivity. Approval-time evidence expires before each mutation. Readbacks cannot lock the dispatcher or other writers.

1. **Inspect**
   - **Bindings:** Confirm Planner, Coder, Reviewer, `CODEX_HOME`, and separate `CODEX_PROCESS_HOME` bindings. Resolve discrepancies before writes. Read the private setup/update record.
   - **Legacy ownership:** For detected bindings or pending retirement, use the exact pre-update manifest for each legacy source revision and assigned path. Establish team ownership and a pristine baseline from recorded installation evidence and complete source comparisons. The absence from the target manifest proves neither.
   - **Legacy inventory:** Check `skills/caveman/` in all three Hermes homes, `skills/caveman-review/` in the Reviewer home, and `.agents/skills/caveman/` in Codex process HOME. Inventory autoload, instruction and prompt bindings, links, unmanaged contents, and shadow copies in other effective roots.
   - **Codex reach:** Use the [Team-Codex instruction recipe](integrations.md#team-codex-instructions) to inspect `$CODEX_HOME/AGENTS.md`, `AGENTS.override.md`, inherited sources, and ancestor and nested project instructions for each affected working directory. Check precedence and truncation. Record conflicts and missing evidence before approval.
2. **Approve and back up**
   - **Approval:** Include exact instruction, autoload entries, original/quarantine paths, and restoration scope in the existing team-update approval. Generic upstream approval alone does not authorize CAC writes. Use the Team-Codex recipe after this approval, including entry through the generic companion link. Review candidate SOULs and local rules, inspect native activity, and record the existing team activity decision. A `skip` leaves the affected team unchanged.
   - **Evidence and backup:** Record exact homes, base and target Maker versions and commits, approval, pre-existing configuration, complete inventories, hashes, ownership, modes, links, and actual source paths. Save and verify restorable backups outside all discovery roots. Record originally absent targets and backup paths.
   - **Quarantine:** Choose an unused path in a protected owner-only directory on the original tree's filesystem, outside every native discovery root including inherited and project roots. Check canonical paths and parents for links or shared access. Keep the backup separate.
   - **Write-ahead record:** For every companion action, persist and read back `pending`, step, exact before and approved after states, and restoration evidence in the existing private `devteam/setup.md` update record before the write. Replace the record atomically and flush the record and its parent directory. On resume preserve original base, historical tickets, and prior evidence.
3. **Stage CAC**
   - **Guard:** Journal the approved write and check inspected targets and bindings for drift. Recheck native activity and claims immediately before staging.
   - **Write:** Use `templates/team-codex-AGENTS.md` and the approved Team-Codex recipe at the confirmed team-specific `$CODEX_HOME/AGENTS.md`. Follow the approved reconciliation to preserve local text, including any CBM pointer.
   - **Verify:** Read back saved bytes and mode. Resolve effective loading through the bound CLI without a model call. If an override, project instruction, truncation, or unresolved edit prevents safe delivery or effective reach, report the specific blocker and withhold dependent file application. Preserve customer files and precedence. Keep the old bindings until CAC is staged and verified.
4. **Apply files, then retire legacy bindings**
   - **Files:** Use the reviewed file proposal and approved retirement scope. Verify the staged instruction and affected bindings, journal the exact proposal, then recheck native activity and claims immediately before dependent file application. After successful file application, record its run and read back all three personalized SOULs. Verify the Reviewer's findings rule, the Coder's CAC task and resume requirements, and absence of any requirement for legacy writing skills.
   - **Retirement guard:** Recheck backed-up trees and native bindings for concurrent drift. Stop affected changes on any difference. Validate the journaled intent against current paths and bindings, then recheck native activity and claims immediately before each retirement mutation, including every autoload write and rename.
   - **Autoload:** For Planner, Coder, and Reviewer, reconcile `skills.auto_load` through the native config interface. Read with `hermes -p "$PROFILE" config get skills.auto_load`. Remove only entries linked to approved obsolete team bindings. Preserve unrelated entries and their order. If changed, apply with `hermes -p "$PROFILE" config set skills.auto_load "$AUTO_LOAD_JSON"` and read back the whole list.
   - **Eligibility:** Retire only proven, pristine, authorized team-owned trees at inventoried paths. Compare the complete tree with the verified inventory and backup, including directory and file modes, ownership, links, hidden entries and legal files. Stop for symlinks, multiply linked files, mount points, or shared consumers. Report foreign, shared, edited, or unproven copies and remaining bindings without deleting, masking, or overwriting them. Keep unresolved retirement pending. An originally absent target needs no move after native discovery confirms absence.
   - **Rename intent:** Persist and read back the intent for each tree. Record original/quarantine paths, tree and both parent device/inode identities, verified inventory, expected destination absence, backup reference, and file run. Recheck identities, inventory, destination absence including dangling links, same filesystem, and applicable bindings before the fresh activity check.
   - **Move and verify:** Rename the entire tree atomically into quarantine. Set `SOURCE` and `DESTINATION` to the journaled paths. On GNU `mv` with the required options, use:

     ```sh
     mv --no-copy --no-clobber --no-target-directory -- "$SOURCE" "$DESTINATION"
     ```

     Keep the step pending if a supported same-filesystem rename is unavailable or fails. There is no copy/delete fallback. Check both paths regardless of exit status. Verify the exact tree at quarantine and absence at the original path, flush both parent directories, and record the readback before continuing. Retain quarantine and backup for recovery.
5. **Verify and resume**
   - **Readbacks:** Check saved instructions, tree inventories, autoload lists, fresh native discovery and source resolution, and Coder task and resume prompts. Verify actual bound HOME and `CODEX_HOME`, Ponytail in both harnesses, `PONYTAIL_DEFAULT_MODE=full`, and preservation of unrelated settings and local text against the pre-change record.
   - **Completion:** Save file run/revision, exact readbacks, and blockers. Mark `complete` only after CAC loading, legacy retirement and preservation checks pass. Read back the private record. Distinguish saved files and fresh readbacks from running-context loading. Do not restart workers or sessions to force adoption.
   - **Failure:** Report what changed, what still loads, and the next action. Keep unfinished work `pending`. If files applied, report `files updated; team update incomplete`. On resume use original pre-change evidence, backup, journal, and current native state even after installation metadata advances. Match each interrupted action to its recorded before state or approved result. Continue only unfinished approved work. Stop on drift.
   - **Interrupted retirement rename:** With the exact recorded tree and unchanged parent identities, original present and quarantine absent means the rename has yet to run. Original absent and quarantine present means it ran. In the latter case, flush pending rename metadata, record the verified result, and check fresh native discovery without renaming again. Both paths present, both paths absent, a partial or edited tree, changed parent, or unexpected link means drift. Preserve both paths as found and report the blocker. An unjournaled partial removal needs separate reconciliation.
   - **Interrupted file application:** Identify the exact helper run from the journaled proposal and team. Inspect its receipt, metadata, and target readbacks under [Failure and rollback](#failure-and-rollback). Recover a partial batch before retirement and keep the original run for rollback. Do not reapply a verified file result to resume the companion. Repeat the file proposal and companion checks. Report a complete no-op only if neither path needs changes and required readbacks pass.
6. **Roll back**
   - **Preflight both sides:** Require approved restoration scope and the existing activity decision. File-helper rollback restores managed files only. Check both managed and companion state for later edits against recorded before/after states before restoring either. Include original/quarantine trees, verified backups, autoload, instruction state, the helper run's installation record, targets/backups, and dependent consumers. On drift, withhold the affected restoration sequence and report the blocker.
   - **Before each write:** Restore only recorded, authorized changes. Journal each inverse companion change before writing. Recheck relevant state and native activity and claims immediately before each rollback mutation. Resume in the following order:
     1. Restore required legacy trees by inverse journaled rename to absent original paths with step 4's identity, inventory, filesystem, no-clobber and flush guards. In a resumed inverse rename, exact tree at quarantine with original absent is the before state. Exact tree at original with quarantine absent is the restored state. Verify and record a completed restore without replay. Read back restored trees and native discovery before advancing.
     2. Restore only affected autoload entries in their recorded positions, and verify the complete lists.
     3. Once legacy prerequisites are verified, run the file-helper rollback if dependent application started. Use the exact run and read back the SOULs. If a rollback was interrupted, check that run's rollback receipt and restored targets against recorded hashes and modes before advancing. If application never started, verify the original SOULs.
     4. Restore the prior Codex home instruction after reverting dependent SOULs, using the verified backup. Remove a newly added instruction only if its bytes and mode still match the record and removal is authorized. Preserve unrelated entries, local text, ownership, modes, and Ponytail. Stop on ambiguous state or drift. Leave the staged CAC instruction in place while any dependent SOUL still requires it.
   - **Verify and record:** Compare restored files, bindings, and preserved settings with native readbacks separately from the file-helper receipt. Record restoration and renewed `pending` in the same private record. Keep interrupted restoration open and report actual files and effective sources.

## Workflow migration (2.0.0)

- **Trigger:** Explicitly authorized update from a pre-update version below `2.0.0` to a target at or above `2.0.0`.
- **Resume:** Resume an unfinished migration even after installation metadata advances. Resolve unknown legacy provenance instead of assuming completion.
- **Record:** Use the existing private setup/update record. The file helper does not migrate cards or certify loaded instructions.

1. **Inspect before authority changes:**
   - **Readbacks:** Affected cards, actual phase/assignment, current runs and claims, latest `review_requested` provenance, blockers, decisions, and parent gates.
   - **Record:** Pre-update version, exact Maker commit, affected card IDs, and unfinished steps.
2. **Settle active old-contract work:**
   - Let active workers finish under their existing contract or obtain a separately scoped transition decision. Do not mix old and new loaded roles on one active handoff.
   - For an active legacy Planner review run, let that owner use the established native `kanban_request_changes` return to its original Coder. This is a migration-only completion, not the route for new questions. A wake session cannot take over that run or reopen an active card.
3. **Resolve parked legacy cards:**
   - Require no active run or competing claim. Resolve the actual blocker and use ordinary unblock or guarded triage recovery to restore its source phase first.
   - If clarification is complete and Coder continuation is required, use the guarded review-reopen procedure in [Review-provenance special case](../skills/brownfield-feature-planning/references/kanban-triage-recovery.md#review-provenance-special-case). Inspect installed public help and native source semantics first. Preserve pending independent review and unresolved `CHANGES_REQUESTED` findings. Do not reopen pending review indiscriminately.
4. **Reconcile local authority:**
   - Reconcile old Planner-review clarification routes and fixed discretionary retry approvals within the approved update mandate.
   - Preserve explicit customer financial/resource caps, operational permissions, native guards, and unrelated local adaptations. Do not silently transfer or enlarge a separate customer-approved mandate. Obtain a customer decision only for genuinely conflicting explicit mandates.
5. **Review and apply files:**
   - Prepare the normal three-way proposal and review neighboring local rules. Recheck current runs and claims immediately before application; defer if the settled state changed.
   - Use the existing activity decision, semantic review, backups, and exact-target verification below. Complete [required skill retirement](#required-skill-retirement) independently of workflow migration.
6. **Read back the same cards:**
   - Verify card identity, decisions, implementation owner, review provenance, counters, parent gates, and actual phase. Keep the same card and its history.
   - Update contradictory active instructions and affected baseline bindings through supported operations within approved scope. For the next Coder handoff, bind the independent Reviewer explicitly; retain historical Planner provenance.
   - **New customer questions:** Reviewer → Coder → needs-input → Planner/Mattermost → Coder → Reviewer.
7. **Verify subsequent instruction loading:**
   - Verify effective loading in subsequent execution contexts separately from saved file bytes. Confirm the applicable plan and role baseline before the next handoff. Do not restart a gateway or session merely because files changed.
   - Report file application, card migration, and effective loading separately. Keep unresolved steps open regardless of package version or queued runs.

## Activity and application

- **Decision:** The helper requires explicit `proceed` or `skip` for application and rollback. It scans visible process environments for exact bound role homes. A match yields `active`; no match yields `unknown`. Inspect native board, worker, dispatcher, and session evidence. The helper cannot prove dispatcher or session inactivity from `/proc`. If active or still unknown, warn the user. Obtain and record their decision per team. Do not fabricate inactivity.
- **Approved scope:** Review the exact proposal and dependent-file decision. Before file application, complete the pre-apply record and approval steps in [required skill retirement](#required-skill-retirement). Before applying workflow authority changes, complete steps 1–4 of [Workflow migration](#workflow-migration-200). Complete approved asset/loading requirements in [Required upstream companion update](#required-upstream-companion-update) before dependent files. For a CAC target, complete steps 1–3 of [CAC migration](#cac-migration) and perform step 4's immediate native activity and claims check before dependent application.
- **Skip:** Use `--activity-decision skip` to leave the team unchanged. Record it as skipped and open. Do not schedule a later retry. Continue other independent teams if one skips or fails.

1. **Apply the reviewed proposal.** With the guards satisfied and decision `proceed`, run:

   ```sh
   python3 -B references/update_team.py apply --home /actual/planner-home \
     --proposal /actual/planner-home/devteam/proposals/PROPOSAL.json \
     --activity-decision proceed \
     --semantic-review 'Reviewed changed files and neighboring role rules; no unresolved semantic conflict'
   ```

   If the proposal reports dependencies, add the concrete user decision:

   ```sh
   python3 -B references/update_team.py apply --home /actual/planner-home \
     --proposal /actual/planner-home/devteam/proposals/PROPOSAL.json \
     --activity-decision proceed \
     --semantic-review 'Reviewed changed files and neighboring role rules' \
     --dependency-decision 'User approved the file-only scope; required runtime capability already verified at the cited setup evidence'
   ```

2. **Check the file transaction.** The helper rebuilds the proposal from its exact Git revision and rechecks target hashes/modes, installation metadata, and visible activity. It backs up every target and the old installation record before the first target write. It verifies exact target bytes and modes before advancing metadata. Replacement is atomic per file only. External writers can race between checks and replacement. Private team state is trusted operator input and cannot isolate hostile same-UID processes.
3. **Continue by result.** Inspect the run under [Failure and rollback](#failure-and-rollback). After success, finish CAC steps 4–5 when applicable, required skill retirement, and workflow readbacks before claiming completion. Report each team's actual result.

## Required skill retirement

- **Trigger:** The reviewed proposal lists `obsolete` skill copies the target no longer produces, or the private record shows pending retirement. Run once per team update. Preserve local work unless the user explicitly approves its reconciliation.
- **Scope:** `update_team.py` deletes nothing. It reports every candidate in the reviewed proposal with its role, identity, resolved root, managed targets, and local state. A skill the team created itself is never a candidate, and neither is a file the Maker does not manage. A candidate is one retired skill tree, or one retired file inside a tree that stays assigned. Use separate [CAC migration](#cac-migration) ownership evidence for external Caveman copies.
- **Evidence:** Resolve each identity against the [manifest](../manifest.json) or its recorded source mapping when the target manifest omits it. A retired identity without a managed installation baseline stays unknown. Retain it, report it, and never remove it from a guess.
- **History:** The retirement introduced in `1.1.22` for `minimal-change-engineering` and `screenshot-to-code` in Reviewer homes is the first instance of this rule, not a separate mechanism; a pending one resumes as an ordinary candidate.
- **Preservation:** Keep the native `sdlc-review` skill and its automatic integration unchanged. Preserve CBM/Graphify skills and bindings; restore the selected Reviewer integration through the approved upstream companion update. Keep every other adaptation and every Planner, Coder and Team-Codex asset. Preserve shared runtimes, caches, indices, MCP entries, hooks, and unrelated integrations; do not copy retired methods into SOUL or other skills.

| State | Evidence | Approved handling |
|---|---|---|
| `pristine` | Every managed file matches its installation hash and the tree contains no unmanaged file | back up outside all native discovery roots, then remove |
| `locally-modified` | A managed file differs or part of the tree is missing | retain and report findings; removal needs a separate decision for that exact candidate |
| `extra-files` | The tree contains an unmanaged file | retain and report findings; removal needs a separate decision for that exact tree |
| `indeterminate` | Unsafe resolution: symlink, hard link, shared source, unreadable path, or outside recorded skill roots | retain and report the blocker |
| `absent` | All managed files are gone | successful no-op after native readback |

1. **Before file application:**
   - Read the private setup/update record and pending retirement evidence. Before invoking `apply`, capture the installed package version and exact Maker commit from the installation record and available setup evidence.
   - Save the pre-update version, target release/commit, and retirement status `pending` in existing private `devteam/setup.md` progress/update sections. Preserve original pre-update evidence on resume even if installation metadata advanced. Record missing provenance against the exact candidate. Read back this private record before file application. Keep no central registry or helper schema change.
2. **Read-only discovery:**
   - Read the proposal's obsolete entries and resolve each candidate's root, managed targets, state, and findings against confirmed role homes and native profile inventory. Keep this discovery strictly read-only. Do not remove trees or change exclusions or bindings during discovery.
   - Inspect all native discovery roots and resolved sources for ownership, aliases, symlinks, and shared/external sources. Record every unmanaged file in a candidate tree and every candidate the record does not manage. Do not follow links into shared assets.
   - If a shared or external source serves other roles, determine the supported role-specific exclusion or unbinding from the installed interface without applying it. If no supported isolation is available, stop this reconciliation with a concrete blocker.
   - Report each concrete retained instruction or autoload reference that would recreate or require a retired skill. Record the concrete role-specific obsolete bindings for scope approval. Leave unrelated bindings and general MCP/hooks outside scope.
3. **Approve the full update scope once:**
   - Include the exact `pristine` candidates, their resolved paths and backup destinations, retained candidates and findings, and inspected role-specific exclusions/unbindings. Include the complete-tree backups, native readbacks, and the concrete role-specific obsolete bindings from that inventory.
   - For missing provenance, add the approved exact reconciliation scope to the existing private record before file application. This authoring procedure grants no live deletion permission. Within that approved update, retiring every `pristine` candidate is mandatory, not an optional second choice. Retained `locally-modified`, `extra-files`, `indeterminate`, and unknown-baseline candidates are reported. Any additional reconciliation needs separate authority. If scope is withheld, record the incomplete step.
4. **After successful file application:**
   - Run the pending retirement after successful file application and before reporting a complete team update.
   - Save every candidate's complete local tree and affected role-specific bindings to a protected external backup outside all native discovery roots, including inherited and project roots. Preserve modes, link metadata, and full inventory without dereferencing links into shared assets. Compare the complete backup inventory and file bytes/hashes with the source before removal. Save backup location, source inventory, verification, and unaffected-role inventories in the existing private record.
   - Continue only if file application, the complete backup, and backup comparison succeeded.
   - Recheck the inspected source bytes and bindings immediately before any removal, exclusion, or binding change; stop on concurrent drift.
     Remove only the verified `pristine` candidates, without following links or deleting shared sources. Apply only the inspected, supported role-specific exclusions/unbindings for shared sources and obsolete references. Reconcile only the inventoried role-specific obsolete bindings within the approved update scope. Treat already absent skills as successful no-ops after native readback.
5. **Verify and persist the result:**
   - Verify absence of every removed candidate through native discovery and source resolution. Use established fresh discovery/readback. Stale session catalogs and missing files alone cannot establish absence. Verify preservation of unaffected roles and assets against the pre-removal inventory. Read back affected role-specific bindings and the preserved native `sdlc-review` source/integration.
   - Mark retirement `complete` only after these readbacks pass. Save exact paths, backup evidence, and file-update run/revision. Read back saved evidence. A `pristine` candidate still present or an `absent` candidate without native readback keeps retirement incomplete.
   - Keep failed or interrupted retirement `pending`, with the concrete blocker and next action. If retirement is withheld or fails, report `files updated; team update incomplete`. On resume read pending state, backup, journal, and actual discovery before continuing only unfinished work.

The file-updater rollback does not restore this prose poststep's removed trees or bindings.

- **Restoration gate:** Obtain authorization, check current targets for later edits, and review saved backup and binding scope.
- **Restore:** Restore complete trees, modes, and role-specific bindings from the external backup without overwriting later work or shared assets.
- **Verify:** Verify restored bytes and native discovery separately from guarded file-helper rollback. Record restoration and renewed `pending` in the existing private record. Do not restart workers or sessions or claim that running contexts unloaded these skills.

## Failure and rollback

- **Prerequisites:** Exact team, proposal, run, installation record, journal, and retained backup. Inspect and recover interrupted work before preparing another update. For started CAC companion writes, use step 6 of [CAC migration](#cac-migration) to coordinate the file rollback. Other approved companion or retirement restoration uses its own procedure.
- **Limits:** File operations and metadata replacements are atomic per file. Successful per-file `fsync` cannot guarantee whole-update power-loss durability. Preserve original journal and backup.

1. **Identify and read the run.** Inspect `<planner home>/devteam/runs/<run>/result.json` after application. Match team, home, proposal and run. Read `status`, review evidence, recorded hashes/modes, and retained-file lists. Compare the installation record, targets, and backups to the recorded states. If a process or power failure interrupts the run, inspect its `prepared` journal before continuing.
2. **Choose the recovery path.**
   - **Verified application:** If the journal reports `applied`, verify the recorded after metadata and every target. If the final receipt was interrupted at `prepared` but exact recorded after metadata and all target hashes/modes match, record that verified result with the interrupted receipt still identified. Keep the exact run for rollback. Resume only pending companion steps. Do not write a new successful helper receipt or reapply verified files.
   - **Failed or partial:** A failed target write leaves the installation revision at the previous verified state, but some files can already contain new bytes. Do not report the team as updated. If the record and targets each match a recorded before or after state and application failed or remains partial, use guarded rollback before new application or dependent retirement. Recheck dependencies and companion recovery after rollback.
   - **Unresolved:** If a run cannot be authenticated, a backup is corrupt, state matches neither recorded side, or evidence is otherwise ambiguous, stop affected writes and report the discrepancy. If no journal was reached, establish from verified evidence that no managed write began before resuming preparation.
3. **Run guarded file rollback.** Confirm authorized restoration, exact run and activity decision under [Activity and application](#activity-and-application). For CAC use this command only at the file-rollback step of coordinated restoration.

   ```sh
   python3 -B references/update_team.py rollback --home /actual/planner-home \
     --run /actual/planner-home/devteam/runs/RUN --activity-decision proceed
   ```

   The helper checks recorded before/after hashes and modes, rejects later work, restores backed-up bytes and modes, and reads restored targets back before restoring the old installation record. It retains newly added files as `retained_additions`. Restored metadata does not claim those additions. Obtain separate deletion approval if needed. Never prune backups or obsolete files automatically.
4. **Verify or resume rollback.** Check `rollback.json`, the restored installation record, hashes and modes, and any retained additions against the same run. If the receipt and readbacks verify rollback, record it without replay. If no receipt exists, rerun guarded rollback for the same run only if its backups, targets, metadata, scope and activity still pass preflight. Stop on drift or contradictory evidence. A receipt proves file restoration only. Verify native bindings and later instruction loading separately.

## Verify and hand off

- **Scope:** Package regression belongs to explicit Maker development/review. Do not repeat removed behavioral experiments or treat them as pending setup gates. Operational dependency decisions still apply when recipes or component metadata change, including changes that remove tests.

1. **Verify saved state.** Read back the exact installation record, result journal, and changed targets. Report package version and commit separately. Confirm each changed instruction from its exact installed passage. If a managed file's bytes match no committed revision, report uncommitted drift and keep it out of the claimed role state.
2. **Verify prerequisites and companions.** Read back [Planner Kanban tools](#planner-kanban-tools), including unchanged-version checks and preservation evidence, and all required upstream companion statuses and native evidence, including unchanged-version comparisons. For a CAC target, read back [CAC migration](#cac-migration) evidence for instruction loading and legacy retirement. For affected teams, read back required skill retirement and workflow migration progress, native evidence, and subsequent-context loading. Missing evidence keeps the relevant step open.
3. **Report per team.** Include `applied`, `skipped`, or `failed`, unknown legacy skill baselines, retained files, remaining runtime checks and any open companion or migration work. Distinguish saved files, native readbacks, and running-context adoption. Do not claim that running sessions loaded the new context or restart them to obtain that claim.
