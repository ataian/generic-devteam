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
- Models: read back actual native model/provider IDs, fixed Planner/Hermes-Coder reasoning, Reviewer/Team-Codex default/max policy, effective overrides and six helper model/reasoning bindings to the confirmed Team-Codex policy. Confirm supported levels/access availability without model calls. Do not silently switch model/provider.
- Team-Codex: read back actual binary, separate process HOME and CODEX_HOME, config/skill roots, protected access status, Ponytail binding and Caveman per-task clause. Verify the own regular mode-0600 `.gitconfig`, source and effective author/committer identity under the bound process environment using [the concrete recipe](integrations.md#team-codex). Do not create artifacts or commits.
- Hindsight: check existing service availability, confirmed bank identity/ownership and effective provider, per-role profile JSON, tags/match semantics and override sources under [Hindsight](integrations.md#hindsight). Do not create synthetic memories or test consolidation.
- Analysis: read back exactly one complete integration for Planner, Coder and Team-Codex under [Code analysis](code-analysis.md). Reviewer has no default analysis delivery/discovery gate; preserve existing local adaptations. For CBM include all native subagents and the account cache literal in TOML `env` before hook approval. For Graphify include both complete supporting reference bundles. Verify established connection/configuration status without index/query/update experiments.
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
A missing shared prerequisite is an operator issue, not an automatic install/repair task.
On resume, reconcile saved setup data with relevant native objects; continue only the incomplete step.
Correct stale prose without repeating confirmed choices or creates.

Setup verifies configuration, availability and delivered outputs. It does not qualify live agent behavior or project readiness.
Do not retain excluded source/SDK research, behavioral experiments, or general timeout/retry/rate-limit investigations as pending setup gates.
For a requested file update, preserve the [update contract](update.md), including semantic review, activity/dependency decisions, local edits, legacy unknown baselines, journals and guarded rollback.
Report `applied`, `skipped`, `failed` and retained files per team; a file update does not prove runtime reload.
