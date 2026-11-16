# Set up and verify role bindings

This reference complements the [setup flow](setup.md): it assigns confirmed values
to their targets and describes the personalization of the roles. The running
work process and the reasoning escalation stand in the role SOULs; domain
instructions stay in the respectively installed skills.

## 1. Copy complete skills and bind the recovery launcher

The [source overview](upstream-sources.md#bundled-components) names the
bundled skill trees and their target roles. For each target, copy the complete tree from
`skills/` including references, scripts and existing license/notice files.
`SKILL.md` stays `SKILL.md`.
Bind only `brownfield-feature-planning/scripts/recover-triage` through the Maker's [recovery binding step](setup.md#bind-the-planner-recovery-invocation).
Keep all other skill bytes unchanged.

- Hermes: `<actually resolved role home>/skills/<Skillname>/`.
- Team-Codex: `<CODEX_PROCESS_HOME>/.agents/skills/<Skillname>/` per the role matrix.
- Check existing targets for ownership and changes; stop on conflicts.
- Compare the complete file set and bytes, using the bound Maker output for the recovery launcher.
- Check discovery and loading in the target harness after the comparison.

Keep installed skills usable without the Maker package or setup record.
Deliver `diagnosing-bugs` only to Team-Codex through [its owned-skill recipe](integrations.md#diagnosing-bugs); verify the Coder's explicit call policy after SOUL delivery.
Deliver `prototype` only to the Planner through [its owned-skill recipe](integrations.md#prototype); verify the direct clarification exception after SOUL delivery.
Deliver the bound callable launcher inside the existing planner skill tree.
Do not add a separate runtime configuration file or workflow skill.

## 2. Personalize role SOULs

The templates for [Planner](../templates/roles/planner.SOUL.md.template),
[Coder](../templates/roles/coder.SOUL.md.template) and
[Reviewer](../templates/roles/reviewer.SOUL.md.template) are changed only at the
provided placeholders. The [manifest](../manifest.json) describes
the `render_fields` actually occurring per role.

| Field | Confirmed value |
|---|---|
| `ROLE_NAME` | Own display name of the respective role |
| `PLANER_NAME` | Planner display name; spelling with one N |
| `CODER_NAME` | Coder display name |
| `REVIEWER_NAME` | Reviewer display name |
| `PROJECT_NAME` | Project identifier as a single segment; does not determine the workspace |
| `PROJECT_DIR` | Confirmed canonical absolute workspace; Planner only |
| `REPOSITORY_ROOTS` | Confirmed repository boundaries as single-line text with separate planning and implementation assignments; Planner only |
| `PLANNER_PROFILE` | Confirmed technical Planner profile ID; Coder only |
| `HINDSIGHT_BANK_NAME` | Actually assigned shared project bank |
| `KANBAN_BOARD_NAME` | Native board identifier, not the display title |
| `CODER_PROFILE` | Technical Coder profile identifier, as far as present in the template |
| `REVIEWER_PROFILE` | Technical Reviewer profile identifier, as far as present in the template |
| `CODEX_BINARY` | Verified absolute Codex entrypoint, not its version-specific release target; Coder only |
| `CODEX_PROCESS_HOME` / `CODEX_HOME` | Verified absolute process/config homes; process HOME matches `confirmed_bindings.roles.team-codex.home`; Coder only |
| `CODEX_REASONING_DEFAULT` / `CODEX_REASONING_MAX` | Confirmed Team-Codex default and permitted upper limit; Coder template only |
| `ROLE_REASONING_DEFAULT` / `ROLE_REASONING_HIGH` | Confirmed Reviewer default and highest permitted review level; Reviewer template only |

Keep display names and technical identifiers separate. Replace all multiple occurrences
from the same confirmed record. The own display name supplies
`ROLE_NAME`; append neither an additional persona nor new role rules.

The pure [text renderer](render_text.py) validates the role-related field set
and replaces in one pass. Missing, additional or damaged fields
are errors. Values stay unchanged: no silent truncation or normalization.
Names are non-empty single-line plain text; technical identifiers and project name
must additionally pass the respective syntax and path checks. Markdown is
masked context-appropriately; technical values in code contexts stay unaltered except Codex paths in shell fences, which receive shell quoting.
All non-placeholder bytes of the confirmed template are preserved.

Use the role personalization accepted during preparation.
Compare the rendered output with that scope before writing only `SOUL.md` in each confirmed role home.
Read back complete bytes against the generated output and check effective full loading through the established native interface.
The rendered Reviewer SOUL carries the proportional investigation method and conditional critical-invariant helper credit.
No separate method reference or helper profile needs delivery; preserve the native `sdlc-review` preload.
Do not overwrite foreign or concurrently changed files.
Ask again only for a newly observed conflict or scope change.

## 3. Bind technical values to actual targets

| Value | Target/readback |
|---|---|
| Role identity | Native registration, canonical home, personalized SOUL |
| Workspace/repositories | Confirmed workspace, `terminal.cwd`, board default workspace and Planner repository-boundary fields |
| Board | Native board ID, explicit board selection and dispatcher DB |
| Bank | Effective provider/bank and exact per-role tags/match settings |
| Models/reasoning | Native configuration and effective overrides; existing role default/max fields |
| Team-Codex | Actual binary, separate process/config homes, access and identity under [Integrations](integrations.md#team-codex) |
| Analysis | Planner, Coder, Reviewer and Team-Codex: exactly the confirmed branch, complete assets and native connection/configuration readbacks |
| Communication | Planner-only bot, exact authorized user/channel/DM IDs and genuine Home binding; later task subscriptions remain operational |

Reuse the confirmed workspace as `PROJECT_DIR` in the Planner SOUL.
Reuse the confirmed repository boundaries as `REPOSITORY_ROOTS` in the Planner SOUL.
Keep planning and implementation assignments separate in that value.
Preserve nested checkouts and roots that differ from the workspace.
If no repository exists yet, record that confirmed fact instead of inventing a root.
Bind the workspace natively as `terminal.cwd` and the board default workspace.
Keep the current Git-root, cwd, board, and ticket checks in the Planner workflow.
Render the confirmed technical `PLANNER_PROFILE` directly into the Coder SOUL.
Check that ID against the native profile registration.
Use that bound ID for the existing Planner wake and TIMER routes.
For a missing customer decision, the Coder keeps assignment and blocks the same card with `kind="needs_input"`.
The existing subscription wakes the Planner for Mattermost coordination.
After recording the sufficient answer, the Planner uses ordinary unblock or guarded triage recovery.
Keep `kanban_request_review` bound to the independent Reviewer, not customer clarification.
Do not derive paths from display names. Derive only new profile IDs under the setup normalization rule; preserve confirmed IDs.
Do not ask the user to repeat confirmed values.
If bindings conflict, resolve the conflict before writing role files.
Keep branch, plan revision, and ticket/run/event IDs specific to the current task.
Do not generate a second runtime binding file.

Keep fixed Planner/Hermes-Coder reasoning in native configuration.
Keep Reviewer/Team-Codex default and maximum in the existing role fields.
Resolve native model IDs, supported levels, and limits during preparation.
For the six VoltAgent specialists, verify unchanged TOMLs and original model/reasoning availability through [their recipe](integrations.md#codex-agents).
Read back actual configuration and overrides; do not probe reasoning boundaries with model calls.
A role maximum is a policy rule, not a technical execution barrier.

Communication accesses and channel bindings stay with the Planner. Secrets belong
in protected native access paths. The private [setup record](../templates/setup-record.md)
documents values, targets and evidence; it is not an additional runtime configuration.

## 4. Setup readbacks and resume

Compare profiles, board/workspace, bank, actual homes, effective model configuration, complete skill trees,
full SOUL loading, recovery output and modes with confirmed values.
Use established discovery/configuration readbacks, not synthetic handoff, wake, or worker experiments.
Reuse preparation acceptance for role personalization; compare exact rendered output with that scope before writing.
A concrete mismatch needs resolution before the affected write or activation.
On resume, read the single setup JSON and actual targets; continue only the incomplete step.
Correct stale descriptive prose without repeating confirmed decisions or creates.

These steps belong to the target setup explicitly commissioned later. Editing
this package activates no profiles, services or agents.