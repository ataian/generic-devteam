# Setup-output verification

Use this checklist for an authorized team setup after delivery and configuration.
Reuse exact evidence captured by each setup step; do not repeat successful steps as a test campaign.
Read only the selected analysis branch and preserve confirmed values.

## Evidence output

Apply the [tool output contract](../SKILL.md#tool-output) to each readback below.
Compare complete file inventories, bytes, mappings, and required native-loaded content without printing successful full payloads.
Use the native interface's documented normalization when comparing loaded text.
For skill discovery/loading, return success, the resolved source path, and required reference coverage in the actual consumer context.
For SOUL loading, return the full-content comparison result and concrete differences if it fails.
For file baselines, return the number checked, source revision, and every missing or mismatched target.
Keep the complete comparison evidence in the existing private setup area.
For configuration and access checks, return the required nonsecret values and their effective management sources.
Report unverified items separately from successful checks.

## Required outputs

- Profiles: compare actual native IDs, ownership, canonical homes, workspace/board bindings and personalized SOUL bytes with the confirmed dataset and rendered output. Read back full SOUL loading through the established interface; file existence alone is insufficient.
- Skills/components: compare complete assigned trees, companion/legal files and bytes with the selected recorded source/revision. Verify native discovery/loading through established interfaces. Reject multiple active paths for the same skill, even if their bytes match and loading succeeds. Keep all own skill bytes unchanged except the bound recovery launcher.
- Upstream pins: resolve each independent component's manifest `source_revision` or inherited `source_component`. Compare complete original file sets and bytes, including hidden manifests, plugin packages, skill companions, all six VoltAgent TOMLs and legal files. Record required/observed revisions separately; a version label or successful native install does not prove a pin match.
- Planner domain modelling: verify complete original `domain-modeling` companions and legal files under [the skill recipe](integrations.md#grill-me). Read back its conditional load and planning-document authority after role delivery; keep Coder/Reviewer as accepted-definition consumers.
- Planner questionnaire: compare the complete original `to-questionnaire` tree, `agents/openai.yaml`, and root MIT license with the pinned source. Verify unambiguous native discovery and full loading under [the same recipe](integrations.md#grill-me), without generating or sending a questionnaire.
- Planner prototypes: verify the complete Planner-only owned tree, branch/legal bytes, native discovery/loading, and direct clarification exception through [its recipe](integrations.md#prototype). Check delivery only; do not generate a demo during setup.
- Runtime boundary: record actual CBM/Graphify and Team-Codex binary paths, versions, shared consumers, compatibility/reuse decisions and approved changes separately from asset hashes. Do not force existing runtimes to asset pins or infer permission from a pin. Keep Hermes/distribution skills native-managed and the Hindsight service untouched.
- Writing skills: verify pinned original `caveman` for all Hermes roles and Team-Codex, plus `caveman-review` for Reviewer. Read back Hermes autoload, each SOUL's use and persisted-prose scope, Reviewer format/procedure separation, and Coder propagation to every task/resume under [Caveman](integrations.md#caveman). File presence alone does not establish activation.
- Models: read back actual native model/provider IDs, fixed Planner/Hermes-Coder reasoning, Reviewer/Team-Codex main-process default/max policy, and effective overrides. Compare all six VoltAgent TOMLs byte-for-byte with the manifest revision, including original model/reasoning settings. Verify discovery without same-name shadowing and supported levels/access availability without model calls. Do not silently switch model/provider.
- Team-Codex: read back actual binary, separate process HOME and CODEX_HOME, config/skill roots, protected access status, Ponytail binding and Caveman per-task clause. Verify the own regular mode-0600 `.gitconfig`, source and effective author/committer identity under the bound process environment using [the concrete recipe](integrations.md#team-codex). Do not create artifacts or commits.
- Reviewer investigation: read back the rendered SOUL's direct/parallel selection, sole coverage/verdict ownership, exact helper binding and limits, and conditional HIGH critical-invariant pass credit under [Role bindings](native-workflow.md#2-rollen-souls-personalisieren). Preserve original native `sdlc-review` loading. Verify delivered policy and full loading, not helper behavior; do not run model experiments.
- Diagnosis: verify the complete Team-Codex-only `diagnosing-bugs` tree, legal/reference bytes, unambiguous native discovery/loading, and Coder task/resume invocation and result-validation clauses through [the owned-skill recipe](integrations.md#diagnosing-bugs). Check saved bytes, discovery, explicit call policy, and actual behavior as distinct claims; do not run a bug experiment during setup.
- Hindsight: check existing service availability, confirmed bank identity/ownership and effective provider, per-role profile JSON, tags/match semantics and override sources under [Hindsight](integrations.md#hindsight). Do not create synthetic memories or test consolidation.
- Analysis: read back exactly one complete integration for Planner, Coder, Reviewer and Team-Codex under [Code analysis](code-analysis.md). For CBM include all native subagents and the account cache literal in TOML `env` before hook approval. For Graphify include both complete supporting reference bundles. Verify established connection/configuration status without index/query/update experiments.
- Communication: read back Planner-only bot/team/channel membership, exact human/channel/DM IDs, effective permission settings and activation/adapter ownership under [Mattermost](integrations.md#mattermost). Perform the disclosed genuine DM `/sethome` and read back the exact DM Home without an extra Home thread. Do not require reply or authorization-event matrices.
- Board: compare actual board ID/default workspace/DB and dispatcher/notifier ownership. Use the [known resolver](kanban-block-triage-escalation.md) with the active gateway PM interpreter for effective `kanban.auto_decompose=false`. Accept a correct central value; do not repair graphs or create test cards. Retain the later operational subscription recipe without creating a subscription to an invented task.
- Protection: verify effective `security.protected_instruction_files=false` and its management source for each selected role. Accept a correct centrally managed value without a duplicate override. Report real restrictions without bypassing them.
- Planner skill maintenance: read back effective `skills.creation_nudge_interval=0` in the Planner profile.
- Recovery: compare installed generic script bytes and generated launcher bytes against `bind_recovery.render_launcher`, mode 0700, interpreter, DB, script and Planner ID. Keep task ID as the sole runtime argument; do not invoke a recovery transition.

## Baseline and completion

Follow [Record a new team](update.md#record-a-new-team) only after all required outputs and recovery binding pass.
Read back and validate locally the private single setup JSON, `installation.json`, complete managed mappings, transform identifiers and pristine personalized `baselines/<sha256>` bytes under the [tool output contract](../SKILL.md#tool-output).
Record package SemVer and exact Maker commit separately, with baseline provenance and actual role homes.
Use the real process HOME for `team-codex`.
Keep private state directories at 0700 and files at 0600.
Keep proposals, backups and journals when the actual update operation requires them.

Use **Team configured; setup outputs verified** only after required outputs and the baseline are complete.
Otherwise state the exact incomplete binding, preserved progress, next action and required authorization.
A missing shared prerequisite is not an automatic install/repair task; use only the disclosed first-installation or separately approved change scope in [Integrations](integrations.md).
On resume, reconcile saved setup data with relevant native objects; continue only the incomplete step.
Correct stale prose without repeating confirmed choices or creates.

Setup verifies configuration, availability and delivered outputs. It does not qualify live agent behavior or project readiness.
Do not retain excluded source/SDK research, behavioral experiments, or general timeout/retry/rate-limit investigations as pending setup gates.
For a requested file update, preserve the [update contract](update.md), including semantic review, activity/dependency decisions, local edits, legacy unknown baselines, journals and guarded rollback.
Report `applied`, `skipped`, `failed` and retained files per team; a file update does not prove runtime reload.
For each requested team update, read back the [mandatory upstream companion status](update.md#required-upstream-companion-update), even when the Maker version is unchanged.
Deferred required assets or loading keep the team update incomplete; report them separately from successful file application.
