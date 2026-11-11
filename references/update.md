# User-triggered team file updates

## Scope and boundaries

Use this procedure if the user asks to check and apply Maker changes to existing teams.
Do not repeat the setup interview.
Reuse `confirmed_values` and `confirmed_bindings` from the single JSON block in each private `devteam/setup.md`.
Keep that block as the sole raw-value source; descriptive record sections contain evidence references.
Distinguish missing confirmed input from actual target drift and stale descriptive prose.
Resolve missing required input or actual drift before the affected write.
Correct stale prose from readbacks without repeating confirmed choices or successful creates.
Do not rewrite existing teams' private records merely to adopt the simplified template.
Resolve missing or contradictory bindings before writing that team's files.
Do not create a cron job or watcher.
Do not stop workers or restart sessions.
Do not change models, plugins, integrations, configuration, or external services through the file helper.
The required prose [Reviewer skill retirement](#required-reviewer-skill-retirement-1122) is the narrow post-file-update exception for approved removal and Reviewer-specific obsolete bindings.
Do not run a new setup or pipeline test card as part of a file update.

Use Python 3.11 or later and local Git for this helper.
Use the existing package SemVer as the release identifier.
Use the exact Git commit as the source revision.
The record `schema` identifies a data format, not another package version.
Keep the source repository and its Git history available for future comparison and rollback review.
An exported skill tree without Git history cannot resolve old source revisions.

## Discover teams

First check your own wrapper or a local adaptation under [Maker wrapper](main-agent-wrapper.md).

1. Inspect the native profile inventory and actual resolved profile homes.
2. Check the installed CLI help before invoking a native inventory command.
3. Save the native results as a private JSON array of `{"id": "actual-id", "home": "/actual/profile/home"}` objects.
4. Include every native profile home in the inventory, including custom and default homes.
5. Run discovery with that inventory.

```sh
python3 -B references/update_team.py discover --homes /private/native-homes.json
```

The helper checks `devteam/installation.json` and `devteam/setup.md` inside the supplied homes.
It does not derive homes from profile names.
It reports invalid records per home without marking other teams as failed.
If an old team has no marker but has a separately known setup record, inspect that record and its native role bindings.
Do not claim that discovery found an unmarked team without such evidence.
Do not add a central team registry.

## Record a new team

Complete setup delivery and configuration/file readbacks before recording a new installation.
Generate the bound recovery launcher through `references/bind_recovery.py` before `init`.
Save the actual role IDs and canonical homes under `confirmed_bindings.roles` in the setup JSON.
Use `planner`, `coder`, `reviewer`, and `team-codex` as role keys.
Use `id` and `home` as the two fields in each role object.
For `team-codex`, use the actual process HOME, not `CODEX_HOME`.
The updater maps its own Codex skill trees to `<process HOME>/.agents/skills/`.
It maps Hermes skill trees to `<role home>/skills/`.

```json
{
  "planner": {"id": "planner-id", "home": "/actual/planner-home"},
  "coder": {"id": "coder-id", "home": "/actual/coder-home"},
  "reviewer": {"id": "reviewer-id", "home": "/actual/reviewer-home"},
  "team-codex": {"id": "team-codex-id", "home": "/actual/codex-process-home"}
}
```

This object is the value of `confirmed_bindings.roles`, not a second setup record.
You can pass the same verified object through `--roles /private/roles.json` if the existing setup uses another binding layout.
Keep IDs distinct from display names.
Keep secrets out of all setup JSON and updater arguments.

Inspect `git status --porcelain` before selecting the source revision.
Use a clean, reviewed Maker checkout.
Record the installed files against its committed `HEAD`.

```sh
python3 -B references/update_team.py init --home /actual/planner-home --team-id actual-team-id
```

`init` does not write role or skill files.
For a new team, it requires exact target readbacks of all personalized SOULs and complete manifest-owned skill trees.
It stores `installation.json` with package version, full commit, role IDs/homes, nonsecret setup values, explicit mappings, transform names, baseline hashes, and installed hashes.
It stores pristine personalized Maker output separately in `baselines/<sha256>`.
It does not use the locally modified target as the Maker baseline.
The private directories use mode 0700.
The private records, proposals, baselines, and backups use mode 0600.
Content updates preserve existing local target modes; they do not migrate permissions.
New regular target files use mode 0600.
New skill helpers with Git mode `100755` use mode 0700, without group or other access.
The proposal binds target modes as well as bytes.
Application and rollback check both before advancing the installation record.

## Record an existing team

Read the existing setup evidence before choosing a baseline.
If the setup proves an exact source revision and coverage of all managed skill copies, use that commit and cite the evidence.
Do not infer an exact revision from a package version alone.

```sh
python3 -B references/update_team.py init --home /actual/planner-home --team-id actual-team-id \
  --base-commit FULL_40_CHARACTER_COMMIT \
  --basis-evidence 'Setup record section and original copy/hash evidence for all managed files'
```

This path preserves existing local changes.
It labels provenance as `documented-setup-baseline`.
The helper records the evidence; it does not authenticate the historical claim.
If the evidence does not cover the skill copies, do not use this full-tree path.

For a team without a version or installation record, use the explicit user-defined SOUL safepoint:

- Package release: `1.0.0`.
- Source revision: `21cae6551c03b6ab84d004f41fc81c921e3e9837` (28 October 2026).
- Provenance: `user-defined-1.0.0-safepoint`.
- Historical installation verification: `false`.

```sh
python3 -B references/update_team.py legacy-baseline
python3 -B references/update_team.py init --home /actual/planner-home --team-id actual-team-id --legacy-souls
```

Do not substitute the updater's introduction commit for this safepoint.
Do not apply this SOUL baseline to old skills.
The legacy path manages only the three SOULs.
It reports old skills as `baseline unknown; withheld` on every update.
Keep those skills outside automatic updates until their own source evidence or a specific reconciliation is approved.
Preserve local SOUL drift through the same three-way comparison as a recorded installation.

## Prepare and review one team

```sh
python3 -B references/update_team.py plan --home /actual/planner-home --target HEAD
```

The helper saves a private proposal and prints its path and contents.
It compares the old pristine baseline, current target, and new personalized Maker output.
It merges nonconflicting text changes with `git merge-file`.
It stops application on text conflicts, missing local files, or incompatible source mappings.
New files in a managed skill tree are included automatically.
The manifest's `recovery_launcher` uses `bound-recovery-v1` instead of `copy-v1`.
The updater renders both source baselines with the team's recorded `confirmed_bindings.triage_recovery`.
It preserves that binding when it renews the launcher from a new template.
It compares local launcher edits against the bound baseline, not the generic template.
If an older marker lacks the binding, the Maker/operator resolves it from confirmed setup and dispatcher evidence before preparing the update.
Save that binding under `confirmed_bindings.triage_recovery` in the existing private setup JSON.
Keep `confirmed_bindings.roles` equal to the recorded team roles.
The updater adopts the missing recovery binding into its reviewed proposal and installation record.
If the marker already has the binding, the updater preserves it without reading `setup.md`.
Do not assign that reconciliation to the planner.
Do not replace unknown local launcher edits with a generic copy.
The file helper lists removed source files and deassigned managed skill copies as `obsolete` and retains them on disk.
Complete the [required Reviewer skill retirement](#required-reviewer-skill-retirement-1122) after file application for affected teams.
Outside this explicit retirement, retain generic obsolete files and local adaptations.
The file helper does not manage upstream Graphify/CBM integrations, MCP configuration, hooks, or indices.
The helper accepts the reviewed pre-1.1.4 renderer by its exact source hash.
That compatibility case adds role fields without changing substitution of old fields.
The helper still verifies each old personalized baseline against the stored bytes.
Other renderer changes remain withheld until transform compatibility is reviewed.

For pre-1.1.4 teams, transfer the already confirmed workspace into `confirmed_values.PROJECT_DIR` in the existing setup JSON.
Transfer the confirmed repository boundaries into `confirmed_values.REPOSITORY_ROOTS` there.
Keep planning and implementation assignments separate in that single-line text.
Preserve multiple repositories and nested checkouts.
If no repository exists yet, record that confirmed fact instead of inventing a root.
Do not infer missing paths from the project name or a current working directory.
Do not repeat the setup interview.
If confirmed evidence is missing, report the unresolved binding to the operator before preparing the update.
The updater adopts only missing role-binding values from that setup JSON.
It reuses the recorded Planner role ID if `PLANNER_PROFILE` is absent.
It rejects a conflicting Planner ID.
It preserves values already present in the installation record.
It saves adopted values only after successful target verification.
Later updates use those recorded values without reading `setup.md`.
Do not assign this reconciliation to the Planner or Coder.

Read the proposal and the changed SOULs and skill files.
Decode the proposal's `new_base` and `merged` fields as base64 if you inspect their bytes programmatically.
Compare the candidate against neighboring instructions and local role rules.
Record a concrete semantic review finding.
Do not treat a clean text merge as proof of semantic compatibility.
If a conflict exists, preserve the proposal and resolve the affected local sections against the exact source revisions within the approved mandate.
Prepare and review a new proposal after that resolution.
Do not edit proposal payloads to bypass a conflict.

If operational recipes or upstream component metadata changed, report their effect and recommendation.
Ask the user to approve or defer the dependent file changes.
Keep the whole team proposal withheld until that decision is recorded.
Use `--dependency-decision` only to record that decision.
It does not authorize runtime configuration or integration changes.
For the Planner skill-maintenance policy, report the separate configuration step in [Setup](setup.md#3-frische-profile-bestätigte-modelle).
The file updater delivers the Planner template change but does not set `skills.creation_nudge_interval`.
Obtain separate authorization to set and read back `skills.creation_nudge_interval=0` in the existing Planner profile.

If the helper recipe changed, report the required Team-Codex model and helper reasoning assignments from [the recipe](integrations.md#codex-agents).
The file updater does not manage the six upstream agent TOMLs.
Obtain separate authorization before adapting installed helper files.
Reuse the team's confirmed `CODEX_MODEL`, `CODEX_REASONING_DEFAULT`, and `CODEX_REASONING_MAX`; preserve other fields and local edits.
If the required runtime capability is absent, defer the dependent proposal.

For Caveman changes, inspect each assigned consumer under [the writing-skill recipe](integrations.md#caveman).
The file updater does not install Caveman skills or change `skills.auto_load`.
Include the exact skill targets, source revision, autoload changes, backups, and readbacks in the explicit team-update authorization.
Preserve local adaptations and historical tickets.
Defer the dependent SOUL changes until the required skills and loading bindings are verified.
Read back each delivered scope clause and the Coder's per-task propagation after file application.
Record subsequent-context loading separately; do not restart sessions or claim that running contexts adopted the change.

## Workflow migration (2.0.0)

Use this procedure during an explicitly authorized team update from a pre-update version below `2.0.0` to a target at or above `2.0.0`.
Resume an unfinished migration even after installation metadata advances.
Resolve unknown legacy provenance instead of assuming completion.
Keep migration progress in the existing private setup/update record.
The file helper does not migrate cards or certify loaded instructions.

1. **Inspect before authority changes:** Read affected cards, actual phase/assignment, current runs and claims, latest `review_requested` provenance, blockers, decisions, and parent gates.
   Record the pre-update package version, exact Maker commit, affected card IDs, and unfinished migration steps in the existing update record.
2. **Settle active old-contract work:** Let active workers finish under their existing contract or obtain a separately scoped transition decision.
   Do not mix old and new loaded roles on one active handoff.
   For an active legacy Planner review run, let that owner use the established native `kanban_request_changes` return to its original Coder.
   This is a migration-only completion, not the route for new questions.
   A wake session cannot take over that run or reopen an active card.
3. **Resolve parked legacy cards:** Require no active run or competing claim.
   Resolve the actual blocker and use ordinary unblock or guarded triage recovery to restore its source phase first.
   If clarification is complete and Coder continuation is required, use the guarded review-reopen procedure in [Review-provenance special case](../skills/brownfield-feature-planning/references/kanban-triage-recovery.md#review-provenance-special-case).
   Inspect installed public help and native source semantics before using that procedure.
   Preserve pending independent review and unresolved `CHANGES_REQUESTED` findings.
   Do not reopen pending review indiscriminately.
4. **Reconcile local authority:** Reconcile old Planner-review clarification routes and fixed discretionary retry approvals within the approved update mandate.
   Preserve explicit customer financial/resource caps, operational permissions, native guards, and unrelated local adaptations.
   Do not silently transfer or enlarge a separate customer-approved mandate.
   Obtain a customer decision only for genuinely conflicting explicit mandates.
5. **Review and apply files:** Prepare the normal three-way proposal and review changed instructions with neighboring local rules.
   Recheck current runs and claims immediately before application; defer if the settled state changed.
   Use the existing activity decision, semantic review, backups, and exact-target verification below.
   Complete the fixed `1.1.22` retirement procedure when applicable; this workflow migration does not replace it.
6. **Read back the same cards:** Verify card identity, recorded decisions, implementation owner, review provenance, counters, parent gates, and actual phase.
   Keep the same card and its history.
   Update contradictory active instructions and affected baseline bindings through supported operations within the approved scope.
   For the next Coder handoff, bind the independent Reviewer explicitly; retain historical Planner provenance.
   New customer-decision questions use Reviewer → Coder → needs-input → Planner/Mattermost → Coder → Reviewer.
7. **Verify subsequent instruction loading:** Verify effective loading in subsequent execution contexts separately from saved file bytes.
   Confirm the applicable plan and role baseline before the next handoff.
   Do not restart a gateway or session merely because files changed.
   Report file application, card migration, and effective-loading evidence separately.
   Keep unresolved steps open instead of inferring completion from a package version or queued run.

## Activity and application

The helper scans visible process environments for exact bound role homes.
A matching process yields `active`.
No match yields `unknown`, not `inactive`.
The helper cannot prove dispatcher or session inactivity from `/proc`.
Check the native board, worker, dispatcher, and session evidence available to the operator.
Warn the user if the team is active or activity remains unknown.
Obtain an explicit proceed or skip decision for that team.
The CLI conservatively requires this decision for every application and rollback.
Do not fabricate an inactivity result to avoid the question.
Before file application, complete the pre-apply record and approval steps in [required Reviewer skill retirement](#required-reviewer-skill-retirement-1122).
Before applying workflow authority changes, complete steps 1–4 of [Workflow migration](#workflow-migration-200).

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

Use `--activity-decision skip` to leave the team unchanged.
Record that team as skipped and open.
Do not schedule a later retry.
Process other independent teams even if one team is skipped or fails.
Report each team's actual result instead of a global current-version claim.

Application rebuilds the proposal from its exact Git revision before writing.
It rechecks target hashes and modes, installation metadata, and visible activity before the write batch.
It backs up every target and the old installation record before the first target write.
It verifies exact target bytes and modes before advancing installation metadata.
Metadata replacement is atomic per file.
The whole update is not an atomic multi-file transaction or an external process lock.
An active external writer can still race between checks and replacement.
Private per-team state is trusted operator input, not a hostile same-UID security boundary.

## Required Reviewer skill retirement (1.1.22)

This is a mandatory Maker prose poststep, not automatic deletion by `update_team.py`.
Apply it when an existing team crosses from a pre-update version below `1.1.22` to a target version at or above `1.1.22`.
This includes teams on `1.1.21` whose earlier deassignment retained installed skills.
Keep this introduction release fixed on later Maker releases.
Resume a pending retirement on later updates even if `installation.json` already reports `1.1.22` or a later version.
Never infer migration completion from version alone.
For a team created at or above `1.1.22`, use original setup and discovery evidence to establish that this crossing migration is not applicable.
For an older team already reporting a newer version without completion evidence, resolve its pre-update evidence or reconcile the exact scope below.
For legacy or unknown versions, resolve the source evidence or explicitly reconcile these five identities within the approved scope.
Do not silently skip an unknown version.

The only removal targets are these exact Reviewer skill identities and their complete local trees:

| Native skill identity | Recipe path to resolve, not a guessed deletion target |
|---|---|
| `minimal-change-engineering` | `<reviewer home>/skills/minimal-change-engineering/` |
| `project-lib-versioning` | `<reviewer home>/skills/project-lib-versioning/` |
| `screenshot-to-code` | `<reviewer home>/skills/screenshot-to-code/` |
| `graphify` | `<reviewer home>/skills/graphify/` |
| `codebase-memory` | `<reviewer home>/skills/codebase-memory/` |

Confirm identities and recipe paths against the [manifest](../manifest.json), [own-skill recipe](setup.md#6-eigene-skills-rollen-und-textpersonalisierung), and [analysis recipes](code-analysis.md).
This migration overrides local-adaptation preservation only for these five Reviewer skill trees.
Include learned files, references, hidden files, and local additions.
Do not copy retired methods into SOUL or other skills.
Keep the native `sdlc-review` skill and its automatic integration unchanged.
Preserve all other adaptations and all Planner, Coder and Team-Codex assets.
Preserve shared runtimes, caches, indices, MCP entries, hooks, and unrelated integrations.
Skill retirement does not authorize general integration or runtime cleanup.

1. **Before file application:** Read the existing private setup/update record and any pending retirement evidence.
   Before invoking `apply`, capture the installed package version and exact Maker commit from the installation record and available setup evidence.
   Save the pre-update version, target release/commit, and retirement status `pending` in the existing private `devteam/setup.md` progress/update section.
   Keep the original pre-update evidence on resume; do not replace it with advanced installation metadata.
   For missing provenance, record the unresolved evidence for the exact reconciliation scope below.
   Read back this private record before file application.
   Do not create a central registry or change the file-helper record schema.
2. **Read-only discovery:** Resolve the exact Reviewer home from confirmed bindings and native profile inventory.
   Keep this discovery strictly read-only.
   Do not remove trees or change exclusions or bindings during discovery.
   Inspect native discovery roots and every resolved source path for the five exact skill identities.
   Record source ownership, aliases, symlinks, and shared/external sources before selecting any removal path.
   Do not delete guessed paths or follow links into shared assets.
   If a shared or external source serves other roles, determine the supported Reviewer-specific exclusion or unbinding from the installed interface without applying it.
   If no supported isolation is available, stop this reconciliation with a concrete blocker.
   Report each concrete retained instruction or autoload reference that would recreate or require a retired skill.
   Record the concrete Reviewer-specific obsolete bindings for scope approval.
   Do not remove unrelated bindings or expand into general MCP/hook cleanup.
3. **Approve the full update scope once:** Include these exact removals and the local-adaptation override once in the target update scope and approval.
   Include complete-tree backups, native readbacks, and the concrete paths and Reviewer-specific exclusions/unbindings found during read-only discovery.
   Include the concrete Reviewer-specific obsolete bindings from that inventory.
   For missing provenance, add the approved exact reconciliation scope to the existing private record before file application.
   This authoring procedure grants no live deletion permission.
   Within that approved update, retirement is mandatory, not an optional second choice.
   If the scope is withheld, record the incomplete step instead of claiming a complete team update.
4. **After successful file application:** Run the pending retirement after successful file application and before reporting a complete team update.
   Save the complete discovered local trees and affected Reviewer-specific bindings to a protected external backup outside all native discovery roots, including inherited and project roots.
   Preserve modes, link metadata, and the full file inventory without dereferencing links into shared assets.
   Compare the complete backup inventory and file bytes/hashes with the source before removal.
   Save backup location, source inventory, verification, and unaffected-role inventories in the existing private record.
   Continue only if file application, the complete backup, and backup comparison succeeded.
   Recheck the inspected source bytes and bindings immediately before any removal, exclusion, or binding change; stop on concurrent drift.
   Remove only the verified Reviewer-local trees from discovery, without following links or deleting shared sources.
   Apply only the inspected, supported Reviewer-specific exclusions/unbindings for shared sources and obsolete references.
   Reconcile only the inventoried Reviewer-specific obsolete bindings within the approved update scope.
   Treat already absent skills as successful no-ops after native readback.
5. **Verify and persist the result:** Verify absence of all five identities through native Reviewer discovery and source resolution.
   Use an established fresh discovery/readback interface; stale session catalogs and missing files alone do not establish absence.
   Verify preservation of unaffected roles and assets against the pre-removal inventory.
   Read back affected Reviewer-specific bindings and the preserved native `sdlc-review` source/integration.
   Mark retirement `complete` only after these readbacks pass, with exact paths, backup evidence, and file-update run/revision.
   Read back the saved completion evidence.
   Keep failed or interrupted retirement `pending`, with the concrete blocker and next action.
   If retirement is withheld or fails, report `files updated; team update incomplete`.
   On resume, read pending state, backup, journal, and actual discovery before continuing only unfinished work.

The file-updater rollback does not restore this prose poststep's removed trees or bindings.
For an authorized restoration, first check current targets for later edits and review the saved backup and binding scope.
Restore complete trees, modes, and Reviewer-specific bindings from the external backup without overwriting later work or shared assets.
Verify restored bytes and native discovery separately from the guarded file-helper rollback below.
Record restoration and renewed `pending` status in the existing private record; do not retain a completion claim for restored skills.
Do not restart workers or sessions, or claim that running contexts unloaded these skills.

## Failure and rollback

Inspect `<planner home>/devteam/runs/<run>/result.json` after application.
Read `status`, review evidence, target hashes, and the retained-file lists.
If a target write fails, the installation revision remains at the previous verified state.
Some target files can already contain new bytes.
Do not report the team as updated after such a failure.
Use the retained backup and journal to recover before preparing another update.
If a process or power failure interrupts the run, inspect its `prepared` journal before continuing.
A successful per-file `fsync` does not guarantee power-loss durability for the whole update.

```sh
python3 -B references/update_team.py rollback --home /actual/planner-home \
  --run /actual/planner-home/devteam/runs/RUN --activity-decision proceed
```

Rollback checks the exact recorded before/after hashes and modes.
It refuses to overwrite work made after the update.
It restores backed-up bytes and modes before restoring the old installation record.
It reads the restored files back.
It retains newly added files and lists them as `retained_additions`.
The restored metadata does not claim those retained additions as managed files.
Obtain separate deletion approval if those files need removal.
Do not prune backups or obsolete files automatically.
A rollback receipt proves file restoration, not reloaded agent behavior.

## Verify and hand off

Package regression belongs to explicit Maker development/review, not each file update or initialization.
Do not repeat removed behavioral experiments or treat them as pending setup gates.
Preserve the operational dependency-decision gate when recipes or component metadata change, including changes that remove tests.

For an authorized target update, read back the exact installation record, result journal, and changed targets.
Read back the required retirement status and native evidence for affected teams before claiming the team update is complete.
Read back workflow migration progress and subsequent-context loading evidence for affected teams; report missing evidence as an open step.
Report package version and commit separately.
Report `applied`, `skipped`, `failed`, unknown legacy skill baselines, retained files, and remaining runtime checks per team.
Do not claim that running sessions loaded the new context.
Do not restart them to obtain that claim.
