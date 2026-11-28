# Private setup record

- Scope: authorized target setup only. Use `<actual planner home>/devteam/setup.md` outside project, Git and exports. Owner directory 0700, file 0600.
- Secrets: record credential locations and access-check status only. The demo password choice lives only in `<project>/demo/settings.json` (mode 0600, excluded from Git); record its mode, location and Git-exclusion status, never the value.
- Authority: native profiles, board and service objects establish current state. This record grants no rollout or operation permission.

## Authorizations and readiness

Before installation resolve all foreseeable choices: project/workspace, repositories, role names/IDs, models/providers/reasoning, Codex access/Git identity, bank/board, analysis, communication identities/targets/authorized users and change scope. Until Planner home exists, use the existing pre-profile dataset and handoff. Record raw values only in the JSON below. Here record readiness and evidence references.

- Approved local installs, exact change scope, bootstrap/PM/activation effects: pending.
- Separate secret, shared-configuration, service, model and external-identity approvals: pending.
- Preserved protection settings, ownership/collision checks, affected shared objects: pending.
- Upfront dataset complete: pending.
- Technically deferred login, native approval or `/sethome` requiring a created target: pending. Record disclosed reason, execution point and completion evidence. Resolve other choices upfront.

## Confirmed data

Store all confirmed raw data in the single JSON block. Use [Setup](../references/setup.md) for `json.dumps` and `json.loads` readback. Preserve existing keys, types and confirmed overrides on resume/update. Empty objects mean unrecorded values. A new record has no demo password value; a historical record may retain the retired `DEMO_PASSWORD` key only until its 4.0.0 adoption removes it, and the project settings file owns every fresh choice.

- `confirmed_values`: names, project, bank, board, profile IDs, models and reasoning. Preserve confirmed `PLANER_NAME`, `CODER_NAME`, `REVIEWER_NAME`, `PROJECT_NAME`, `HINDSIGHT_BANK_NAME`, `KANBAN_BOARD_NAME`, `PLANNER_PROFILE`, `CODER_PROFILE`, `REVIEWER_PROFILE`, `CODEX_MODEL`, `PLANNER_REASONING`, `CODER_REASONING`, `CODEX_REASONING_DEFAULT`, `CODEX_REASONING_MAX`, `ROLE_REASONING_DEFAULT`, `ROLE_REASONING_HIGH`.
- Workspace: `PROJECT_DIR` is canonical and absolute. `REPOSITORY_ROOTS` is one line with separate planning and implementation assignments or confirmed absence.
- Native configuration only: fixed Planner/Hermes-Coder reasoning and Codex model ID. Add no role-render fields for them.
- Coder render paths: verified absolute `CODEX_BINARY` entrypoint, process home `CODEX_PROCESS_HOME`, config home `CODEX_HOME`. Use raw paths without shell quoting. Match process HOME to `confirmed_bindings.roles.team-codex.home`.
- `confirmed_bindings.roles`: `planner`, `coder`, `reviewer` and `team-codex`, each with actual `id` and canonical `home`. Use actual process HOME for `team-codex`.
- `confirmed_bindings.command_allowlists`: map `planner`, `coder` and `reviewer` to their verified native arrays of command strings. A missing role key is unknown; `[]` is a verified empty list.
- `confirmed_bindings.triage_recovery`: `python` from verified dispatcher interpreter, `script` from installed Planner skill, `db` from dispatcher resolution of confirmed board DB, `planner_profile` from confirmed technical Planner ID.

```json
{
  "confirmed_values": {},
  "confirmed_bindings": {}
}
```

## Setup targets and readbacks

Per target, record actual native identity or exact path, configuration source, previous state/hash, delivered revision/hash, mode and readback. Reference JSON values without duplicating them. Separate availability, configuration, file delivery and unverified live behavior.

- Native profiles, three SOULs (bytes, effective loading, compact exchanges, Coder task/resume/delegation and Reviewer procedure), skill inventories and discovery: pending.
- Required shared dependency availability and established interface readbacks: pending.
- Per-role model/provider/reasoning settings, effective overrides, and native configuration readbacks: pending.
- Docker grants: the `docker`, `docker *`, `docker-compose` and `docker-compose *` entries in all three profiles cover all operations on any daemon accessible to the CLI, including an alternate context or remote daemon. They are not project-scoped, can affect other workloads, and do not override existing deny rules. Record the native readback.
- Project demo settings: `<project>/demo/settings.json` path, choice mode (`shared`, `random` or absent), file mode 0600, Git-exclusion and untracked readback, and completion: pending. Never the value.
- Team-Codex process HOME, separate CODEX_HOME, binary, protected access location/status, and Git identity configuration readbacks: pending.
- Team-Codex instructions: source template path/hash and Maker SemVer/commit, confirmed homes/cwd, target path, previous and installed hashes/modes, backup location, effective instruction sources in order, override/limit and full-content results: pending.
- Board/workspace, bank ownership and per-role memory bindings, selected analysis integration and target paths for Planner, Reviewer and Team-Codex: pending.
- Planner communication identity, authorized users/channels, subscriptions, dispatcher/notifier ownership, and activation state: pending.
- Component source repository/subpath, exact revision, license, complete file inventory/hashes, actual target, and discovery/configuration readbacks for each assigned component: pending.

- Component pin evidence: per independent component, required manifest `source_revision` or inherited `source_component` and observed installed provenance. Compare full plugin/skill trees, hidden files, companions, six VoltAgent TOMLs and legal files. Record native registration and complete main/reference loading per assigned consumer. Unknown historical provenance stays unknown. A local backup cannot prove a pristine upstream baseline.
- Runtime evidence: actual Codex/CBM/Graphify paths, versions, shared consumers and compatibility/reuse decisions, separate from asset pins. Approve first installs in upfront setup scope. Preserve existing/shared installations unless explicitly approved for concrete change. For updates, retain advance explicit approval of each concrete plugin/runtime/CLI change batch and shared PM effects. Keep Hermes/distribution skills native-managed and the Hindsight service untouched.
- Recovery launcher: after copying the full skill tree, generate with `references/bind_recovery.py`. Task ID is the sole runtime argument. No runtime dependency on this record. Binding evidence proves neither operation authority nor semantic API behavior.
- Recovery board/dispatcher readback, script bytes, launcher hash and mode 0700, deterministic output comparison and shell-quoted installed invocation path: pending.

## Progress and recovery

- Latest completed and verified step, created objects/files, and evidence: pending.
- Incomplete step, exact blocker or missing prerequisite, next action, required authorization, and success signal: pending.
- Previous own file/configuration state and targeted recovery path: pending.

1. On resume compare saved JSON with relevant actual targets. Confirm missing input and resolve target drift before render/write. Update stale prose from readbacks without repeating confirmed choices or successful creates. Resume the first incomplete step.
2. Recover only recorded own objects/entries. Preserve local edits, unrelated profiles/skills/subscriptions, shared binaries/PM, personal Codex assets, project files/AGENTS, service/bank/channel contents and graph caches. Obtain separate data-deletion approval.

## Installation and update evidence

- Baseline: initialize only after complete delivery, configuration/file readbacks and recovery binding. Follow [Team updates](../references/update.md) for initialization, existing-team baselines and authorized updates. Save `installation.json` and pristine personalized `baselines/<sha256>` under private Planner `devteam/` (directories 0700, files 0600). Record package SemVer and exact Maker commit separately from schema. Preserve provenance, role bindings, managed mappings, transforms and hashes. Exclude locally edited targets from pristine baselines.
- Skill retirement: before file application, record pre-update version and `pending` under [required skill retirement](../references/update.md#required-skill-retirement). Keep approval, external backup, native readbacks and pending/completed poststep evidence in progress and update sections.
- Companions: follow [required upstream update](../references/update.md#required-upstream-companion-update) on every requested update, even at the same Maker version. Before file application record pre-update Maker version/commit, required/observed asset sources, exact targets, differences, decisions and per-component `pending`. Include missing selected Reviewer analysis assets and native bindings, including previously retired assets, plus approved restoration/readbacks. Keep full backup inventories/bytes, modes, ownership, binding readbacks and guarded companion restoration evidence.
- [CAC migration](../references/update.md#cac-migration): before the first companion write record base/target SemVer and commit, stage and `pending`. Keep exact [Team-Codex template](../references/integrations.md#team-codex-instructions) and approved merge evidence. Record effective loading, legacy reconciliation and `complete` separately from file application.
- Companion completion: mark `complete` only after exact pinned asset byte comparisons and required native readbacks pass. Read back saved evidence. Resume pending work even if metadata advanced. Restore companion assets/bindings through guarded companion rollback. File-helper rollback alone leaves them in place. Report `files updated; team update incomplete` while required companion work is pending or deferred.

- Package SemVer, exact Maker commit, installation marker, provenance, and baseline readbacks: pending.
- Update proposal, activity finding and explicit proceed/skip decision, semantic review, and operational dependency decision: pending when an update is authorized.
- Backup run, result journal, verified targets, per-team result, guarded rollback receipt, and retained additions/obsolete files: pending when an update is authorized.

- Advance metadata only after successful target verification. Apply the managed-file, conflict and rollback rules in [Team updates](../references/update.md).
- Use **Team configured; setup outputs verified** only after required outputs and versioned baseline pass. Report exact blockers. Research and behavioral experiments stay outside setup gates.
