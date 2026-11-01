# Maker setup scope — design specification

## Status and authority

- Date: 2026-11-01.
- Repository: `/home/joi/projects/generic-devteam`.
- Inspected source: `a44d15e3aad77b891fa5c95ebeba49a780e4525e`, branch `develop`, Maker package `1.1.4`.
- Max approved the design direction in the planning conversation: preserve the generated team's capabilities and quality; remove development research and behavioral qualification from ordinary team setup.
- Max explicitly requires useful setup records and the existing versioned installation/update mechanism to remain intact.
- This document records that direction for review. Approval of this written specification and a subsequent implementation plan are still separate gates.
- No implementation, team rollout, profile change, push, release, or deployment is authorized by this document.

## 1. Outcome

Keep the same equipped Planner, Coder/Codex, and independent Reviewer team.
Reduce the Maker's ordinary job to setting up that team on an available system basis.
Verify the Maker's own configuration and file delivery.
Do not make the setup prove that the platform or agents behave correctly in a development scenario.

Use this completion statement: **Team configured; setup outputs verified.**
Do not claim end-to-end team behavior, learning quality, or project readiness from setup readbacks.
Do not leave a completed setup pending merely because excluded development tests were not run.
Report a real missing prerequisite or failed binding as an incomplete setup item.

## 2. Preserved product and safety requirements

Preserve:

- Three native profiles with the existing role responsibilities and independent review boundary.
- Personalized SOULs and complete assigned skill, script, and helper packages.
- Confirmed model/provider choices and reasoning limits.
- Team-Codex process/configuration homes, access configuration, and Git identity.
- The selected code-analysis integration for its assigned consumers.
- Shared Hindsight bank creation or authorized reuse and each role's memory binding.
- Planner communication identity, authorized user/channel configuration, and native board/workspace bindings.
- The bound recovery launcher and its recorded team values.
- Collision checks, ownership checks, secret protection, local-edit preservation, and separate approval for shared-system changes.
- Useful setup progress and exact installed-version evidence for later updates.

Do not simplify role quality requirements to reduce setup work.
Do not remove a component solely because its current setup recipe contains excessive tests.
Keep role templates, skill payloads, render transforms, and helper behavior unchanged unless a concrete setup-scope conflict requires a targeted correction.
Do not turn this revision into a general rewrite of the team's working methods.

## 3. Responsibility boundary

| Area | Ordinary Maker setup | Outside ordinary setup |
|---|---|---|
| Shared dependencies | Identify the existing required component and check availability through its established interface | Install, upgrade, repair, or requalify the shared platform |
| Profile integration | Install/activate required profile-local assets and configure their concrete targets through the established recipe | Research adapter internals or invent a replacement integration |
| Hindsight | Check service availability; create/bind the confirmed bank; verify role/provider/bank settings | Retain/recall/reflect experiments, consolidation tests, SDK research, synthetic conversation matrices |
| Codex and helpers | Bind homes, access, identity, model limits, and intended helper files; check their effective configuration | Real delegation to every helper, reasoning-boundary experiments, retry/resume and HIGH+HIGH behavior matrices |
| Code analysis | Bind the selected existing runtime, skills, MCP/hooks and team-specific paths as required | Index/query/update experiments in a fabricated project |
| Communication and Kanban | Configure identities, permissions, board/workspace, dispatcher ownership, and the established routing recipe | Synthetic coding/review cards, interview tests, reply-behavior matrices, experimental wake chains |
| Target project | Resolve the intended workspace and repository boundaries for team binding | Install project build dependencies, qualify its toolchain, or begin project onboarding |
| Maker helpers | Deliver correct files and generated team bindings | Run renderer/updater/recovery development suites on every team creation |

Profile-local installation is not the same as reinstalling a shared service.
Preserve necessary profile-local integration work.
Use concrete supported recipes instead of asking the setup agent to discover how a dependency works.
Use the established available source rather than requiring a search for the newest upstream version on every setup.
If the recipe is incompatible or incomplete, report that specific limitation.
Resolve recipe gaps during Maker development, not through open-ended research in each setup.
Do not introduce a prerequisite certification pipeline, new registry, installer framework, or verification service.

## 4. Ordinary setup flow

1. Reuse confirmed team values. Ask only for missing consequential choices. Identify required available dependencies and target collisions.
2. Confirm the concrete change and activation scope. Retain separate authorization for secrets, shared configuration, and external identity actions where required.
3. Create/configure profiles. Deliver personalized roles and complete required assets. Bind Codex, code analysis, board/workspace, communication, and Hindsight according to the existing recipes.
4. Read back the created objects, effective settings, delivered files, modes, and generated bindings. Reuse evidence from the setup step; do not repeat it as a separate general test campaign.
5. Save the versioned installation baseline through the existing updater initialization path. Record verified completion or exact remaining setup blockers.

Do not add a coding task, agent conversation, synthetic memory content, or test repository to this flow.
Keep genuine initial communication binding actions if the established interface needs them; do not expand them into agent-behavior tests.
Check loader/discovery/configuration through an available established readback when needed to establish delivery. Do not inspect loader implementations anew.
Treat an effective centrally managed setting as satisfied when it meets the required behavior. Do not require a duplicate profile entry or override an administrative restriction for formal compliance.

## 5. Setup record and update compatibility

### 5.1 Keep the existing data contract

Keep the private `devteam/setup.md` record and its single parseable fenced JSON block.
Preserve `confirmed_values` and `confirmed_bindings` with their existing names and meanings.
Preserve actual role IDs and canonical homes under `confirmed_bindings.roles`.
Use the real process HOME for `team-codex`, not `CODEX_HOME`.
Preserve `confirmed_bindings.triage_recovery` and the role-render values needed by current or supported older installations.
Keep native objects authoritative for current runtime state.

Simplify duplicate prose tables and research-result checklists.
Do not remove machine-consumed values or replace them with free-form summaries.
Record the latest completed step, created targets, unresolved blocker, and next required action briefly.
On resume, compare the relevant actual state and continue at the first incomplete setup step.
Do not repeat successful setup or ask again for confirmed values because an old descriptive table is stale.
Do not rewrite existing teams' private records as part of this Maker revision.

### 5.2 Preserve versioned installation evidence

Keep the existing `devteam/installation.json` and pristine personalized `baselines/<sha256>` files.
These are required updater state, not redundant research evidence.
Preserve package SemVer, exact Maker commit, role bindings, managed source/target mappings, transform identifiers, hashes, and baseline provenance.
Preserve the existing private directory/file permissions and mode checks.
Keep backups, proposals, result journals, and rollback evidence when the existing update operation needs them.
Do not add another version system or central team database.

Keep package version and exact Git source revision distinct.
Keep record `schema` distinct from the package version.
Keep the historical Git objects needed to reconstruct earlier Maker outputs.
A package version alone does not prove an exact historical installation baseline.

### 5.3 Preserve update behavior and limits

Keep the three-way comparison of old pristine output, current local output, and new personalized output.
Preserve local edits and stop on unresolved conflicts.
Advance installation metadata only after successful target verification.
Preserve the current guarded rollback and retained-file behavior.
Preserve conservative treatment of legacy teams with unknown skill baselines.
Do not repeat setup interviews or run test cards during file updates.

The existing updater updates managed role/skill files. It does not update runtime configuration, integrations, models, external services, or running contexts.
Do not promise that every future Maker change can be applied automatically to an existing team.
Report changed operational recipes through the existing dependency-decision path. Do not bypass that path merely because this revision removes setup tests.
Keep any runtime migration separate from file-update permission.

## 6. Change surface and document ownership

- `SKILL.md`, `README.md`, `NOTICE.md`: align entry, supported outcome, and completion claims with setup-only responsibility.
- `references/setup.md`, `references/native-workflow.md`: retain concrete creation/binding/readback recipes; remove recurring platform investigation and behavioral test obligations.
- `references/integrations.md`, `references/code-analysis.md`, `references/kanban-block-triage-escalation.md`: separate necessary configuration from component research, operation, and test scenarios.
- `references/verification.md`: make ordinary setup checks explicit. Keep useful Maker development checks in a separately triggered development reference, not a mandatory setup reference.
- `templates/setup-record.md`: simplify human-maintained evidence while preserving the JSON/update contract.
- `references/update.md`: keep update guarantees; correct only references or scope wording affected by this revision.
- `manifest.json`: preserve component assignments and transforms; align file references and stage wording with actual evidence. Do not label unperformed runtime acceptance as passed.
- `references/test_*.py`: retain existing development tests; add only a focused missing regression for a changed contract.
- `templates/roles/` and `skills/`: audit setup backlinks. Do not broadly rewrite role instructions or copy test duties into generated teams.

Classify affected instructions as KEEP, MOVE, MERGE, REMOVE, or REVIEW under the repository TAS standard.
Apply this classification during development; do not add a per-installation classification ledger.
Do not make a moved development reference mandatory through another setup link.
Do not impose a fixed document-length target at the expense of necessary recipes.

The installed launcher `/home/joi/.hermes/skills/devops/generic-devteam/SKILL.md` contains additional operative instructions outside this repository.
Review its entry contract against the revised Maker before claiming that the actual installed entry is aligned.
Keep any launcher replacement narrowly scoped and separately authorized for that profile. Do not edit other profile instructions or configurations.
A repository-only result must state that an unchanged installed launcher can still impose older obligations.

## 7. Development acceptance for this revision

These checks belong to Maker revision work, not to each future team setup.

1. Trace the normal entry and required references. No mandatory platform-source investigation, artificial team task, Hindsight experiment, helper-call matrix, or code-analysis test project remains reachable as a setup duty.
2. Compare the component/role assignments with the inspected baseline. Preserve all required team assets and safety/role boundaries.
3. Verify that the revised record remains readable by the existing `setup_data` consumer. Verify initialization, baseline creation, update planning/application, local-edit preservation, and rollback with the existing synthetic fixtures. Add a small fixture only if the changed template is not covered.
4. Run the repository's existing offline suite: `python3 -B -m unittest discover -s references -p 'test_*.py'`. Run `git diff --check`. Report skipped checks and failures accurately.
5. Review normal setup, missing dependency, collision, interrupted setup, and existing-team update against the revised instructions. Ensure each has a bounded next action rather than an automatic research/repair expansion.
6. Check links, manifest consistency, and TAS for changed instructions. Keep package tests separate from claims about installed live teams.

Do not add a benchmark platform or an arbitrary promised setup duration.
Any separately authorized practical Maker trial is one-time revision evidence. Do not turn it into a standard future setup gate.

## 8. Versioning and authorization

This planning document and `HERMES.md` do not change the delivered Maker package or its manifest.
Keep package version `1.1.4` unchanged during this design step.
For the implementation changeset, apply the repository's existing SemVer rules and update `SKILL.md` and `manifest.json` together.
Do not introduce a record-schema migration solely to shorten setup prose.
If implementation discovery requires a genuine incompatible data or role change, stop and revise this design before proceeding.

After written-spec acceptance, prepare the versioned implementation plan with file scope, acceptance, commit boundaries, and predecessors.
Obtain Max's explicit plan approval before creating Scotty implementation tasks.
Julia remains the independent reviewer of implemented changes.
Resolve the project board and communication routing before task creation.
Do not apply this revision to existing teams, update the installed launcher, or publish the repository without the corresponding authorization.

## 9. Evidence and interpretation limits

- User context: session `20261101_182710_26b6d5` and the subsequent Kirk planning conversation.
- Investigation input: `/home/joi/projects/devteam-profiling/MAKER_OVERLOAD_FINDINGS_UND_EMPFEHLUNGEN.md`.
- The later confirmed setup-only boundary supersedes that investigation document's recommendation for a mandatory small team trial. Keep the historical investigation unchanged.
- Current repository evidence: `references/integrations.md` Hindsight/helper sections; `references/verification.md` behavior and pipeline checks; `references/setup.md` preflight/resume/baseline sections; `templates/setup-record.md`; `references/update.md`.
- Code evidence: `references/update_team.py` functions `setup_data`, `initialize`, and `prepare`; existing updater, renderer, and recovery tests.
- No live team configuration was inspected or modified for this specification.
- This specification does not claim that the proposed simplification has been implemented or that a new team has passed setup.
