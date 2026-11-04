# Private setup record

Fill this template only for an authorized target setup.
Store it at `<actual planner home>/devteam/setup.md`, outside the project, Git, and exports.
Use mode 0700 for the owner directory and 0600 for this file.
Store no tokens, passwords, authentication codes, or unredacted configuration dumps.
Record only secret locations and access-check status.
Native profiles, board, and service objects remain authoritative for current state.
This record is evidence, not permission for rollout or operation.

## Authorizations and readiness

- Approved local installations, exact change scope, and bootstrap/PM/activation effects: pending.
- Separate secret, shared-configuration, service, model, and external-identity authorizations: pending.
- Preserved protection settings, ownership/collision checks, and shared objects affected: pending.
- Complete upfront dataset readiness: pending.

Before installation, resolve all foreseeable choices for project/workspace and repository boundaries,
role names and IDs, models/providers and reasoning, Codex access and Git identity, bank/board,
analysis choice, communication identity/targets/authorized users, and change scope.
Use the existing pre-profile dataset and handoff until the Planner home exists.
Keep raw confirmed values only in the JSON block below.
Record readiness and evidence references here without repeating those values.
Disclose any login, native approval, or `/sethome` action that technically requires a created target.
Record its reason and execution point; do not treat other unresolved choices as deferred actions.

- Disclosed technically deferred actions and completion evidence: pending.

## Confirmed data

Write every nonsecret confirmed raw value in this single JSON block.
Use `json.dumps` and the `json.loads` readback in [Setup](../references/setup.md).
Preserve existing keys, types, and confirmed overrides on resume and update.
Empty objects mean that values have not been recorded.

Store names, project, bank, board, profile IDs, models, and reasoning in `confirmed_values`.
Keep the canonical absolute workspace as `PROJECT_DIR`.
Keep `REPOSITORY_ROOTS` as single-line repository text with separate planning and implementation assignments, or confirmed absence.
Preserve `PLANER_NAME`, `CODER_NAME`, `REVIEWER_NAME`, `PROJECT_NAME`, `HINDSIGHT_BANK_NAME`,
`KANBAN_BOARD_NAME`, `PLANNER_PROFILE`, `CODER_PROFILE`, `REVIEWER_PROFILE`, `CODEX_MODEL`,
`PLANNER_REASONING`, `CODER_REASONING`, `CODEX_REASONING_DEFAULT`, `CODEX_REASONING_MAX`,
`ROLE_REASONING_DEFAULT`, and `ROLE_REASONING_HIGH` when confirmed.
Keep fixed Planner/Hermes-Coder reasoning and the Codex model ID for native configuration only.
Do not add role-render fields for these native settings.

Store resolved technical bindings in `confirmed_bindings`.
Under `roles`, retain `planner`, `coder`, `reviewer`, and `team-codex`, each with `id` and canonical `home`.
Use the actual process HOME for `team-codex`, not `CODEX_HOME`.
Under `triage_recovery`, retain `python`, `script`, `db`, and `planner_profile`.
Use the verified dispatcher interpreter, installed planner script path, confirmed board DB resolved by the dispatcher,
and confirmed technical Planner profile ID.

```json
{
  "confirmed_values": {},
  "confirmed_bindings": {}
}
```

## Setup targets and readbacks

Record actual targets and evidence references without duplicating raw confirmed values.
For each setup item, record its native identity or exact file path, configuration source,
previous state/hash, delivered revision/hash, mode, and actual readback result.
Report availability, configuration, file delivery, and unverified behavior separately.
Do not infer live behavior from configuration or file checks.

- Native profiles, personalized SOUL targets and byte comparisons, complete assigned skills and discovery: pending.
- Required shared dependency availability and established interface readbacks: pending.
- Per-role model/provider/reasoning settings, effective overrides, and native configuration readbacks: pending.
- Team-Codex process HOME, separate CODEX_HOME, binary, protected access location/status, and Git identity configuration readbacks: pending.
- Board/workspace, bank ownership and per-role memory bindings, selected analysis integration and target paths: pending.
- Planner communication identity, authorized users/channels, subscriptions, dispatcher/notifier ownership, and activation state: pending.
- Component source repository/subpath, exact revision, license, complete file inventory/hashes, actual target, and discovery/configuration readbacks for each assigned component: pending.

Generate the recovery launcher with `references/bind_recovery.py` after copying the complete skill tree.
Keep its task ID as the only runtime argument.
The installed launcher must not depend on this record at runtime.
Binding evidence does not authorize operation or prove semantic API behavior.

- Recovery board/dispatcher binding readback, script byte comparison, launcher hash and mode 0700, deterministic output comparison, and shell-quoted installed invocation path: pending.

## Progress and recovery

- Latest completed and verified step, created objects/files, and evidence: pending.
- Incomplete step, exact blocker or missing prerequisite, next action, required authorization, and success signal: pending.
- Previous own file/configuration state and targeted recovery path: pending.

On resume, read the JSON and relevant actual targets, then continue only the first incomplete setup step.
Confirm missing input before using it.
Resolve actual target drift before rendering or writing.
Correct stale descriptive prose from readbacks without repeating confirmed choices or successful creates.
Preserve local edits and unrelated profiles, skills, subscriptions, shared binaries/PM runtime,
personal Codex assets, project files/AGENTS, service/bank/channel contents, and graph caches.
Limit recovery to recorded own objects and entries.
Obtain separate authorization for data deletion.

## Installation and update evidence

Initialize only after complete delivery, configuration/file readbacks, and recovery binding.
Follow [Team updates](../references/update.md) for initialization, existing-team baselines, and authorized updates.
Keep `installation.json` and pristine personalized `baselines/<sha256>` under the Planner's private `devteam/` directory.
Keep package SemVer and exact Maker commit distinct from the record schema.
Preserve baseline provenance, role bindings, managed source/target mappings, transform identifiers, and hashes.
Never use a locally edited target as a pristine Maker baseline.
Keep private state directories at 0700 and files at 0600.

- Package SemVer, exact Maker commit, installation marker, provenance, and baseline readbacks: pending.
- Update proposal, activity finding and explicit proceed/skip decision, semantic review, and operational dependency decision: pending when an update is authorized.
- Backup run, result journal, verified targets, per-team result, guarded rollback receipt, and retained additions/obsolete files: pending when an update is authorized.

Advance installation metadata only after successful target verification.
Preserve the three-way comparison, local-edit/conflict safeguards, conservative legacy handling, and guarded rollback.
Report setup completion as **Team configured; setup outputs verified** only when required setup readbacks and the versioned installation baseline are complete.
Report remaining setup blockers precisely.
Do not leave excluded research or behavioral experiments as pending setup gates.
