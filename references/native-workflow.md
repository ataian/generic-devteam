# Set up and verify role bindings

Use with [Setup](setup.md) to bind confirmed values and personalize roles.
Role SOULs own workflow, reasoning escalation and compact exchanges. Installed skills own domain instructions.

## 1. Copy complete skills and bind the recovery launcher

1. Use the [source matrix](upstream-sources.md#bundled-components) to map complete skill trees to `<actually resolved role home>/skills/<Skillname>/` or `<CODEX_PROCESS_HOME>/.agents/skills/<Skillname>/`. Check ownership and local changes before copying. Stop on conflicts.
2. Copy from `skills/`. Keep filenames and bytes, including `SKILL.md`, references, scripts and legal files. Bind only `brownfield-feature-planning/scripts/recover-triage` through [Setup](setup.md#bind-the-planner-recovery-invocation). Deliver the callable launcher in the Planner skill tree. Use the delivery recipes for [`diagnosing-bugs`](integrations.md#diagnosing-bugs) (Team-Codex only) and [`prototype`](integrations.md#prototype) (Planner only). Keep installed skills independent of the Maker package and setup record. Add no runtime config file or workflow skill.
3. Compare full file sets and bytes, using the bound Maker output for the launcher, then verify discovery and loading in each target harness.

## 2. Personalize role SOULs

Render the [Planner](../templates/roles/planner.SOUL.md.template), [Coder](../templates/roles/coder.SOUL.md.template) and [Reviewer](../templates/roles/reviewer.SOUL.md.template) placeholders using the [manifest](../manifest.json) `render_fields` for each role.

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

- **Bind.** Use the same confirmed record for every occurrence. Keep display names separate from technical IDs. Use the role's own display name for `ROLE_NAME`.
- **Render.** The pure [text renderer](render_text.py) validates the field set and substitutes once. Reject missing, extra or damaged fields. Require nonempty single-line names and valid technical IDs and project name under their syntax and path rules. Preserve values and every non-placeholder byte without truncation or normalization. Apply context-specific Markdown escaping and shell-quote Codex paths in shell fences. Keep code values raw. Append no persona or rules.
- **Deliver.** Compare rendered output against the personalization accepted in preparation. Write only `SOUL.md` in each confirmed role home. Preserve foreign or concurrently changed files. Ask again only for a newly observed conflict or scope change.
- **Read back.** Compare complete saved bytes with generated output and use the native interface to verify full loading. The Reviewer SOUL owns proportional investigation and conditional critical-invariant helper credit. Keep native `sdlc-review` preloaded. Deliver no separate method reference or helper profile.
- **Check call policy.** After SOUL delivery, verify the explicit diagnosis call in the Team-Codex instructions and the Planner's direct clarification exception.

## 3. Bind technical values to actual targets

| Value | Target/readback |
|---|---|
| Role identity | Native registration, canonical home, personalized SOUL |
| Workspace/repositories | Confirmed workspace, `terminal.cwd`, board default workspace and Planner repository-boundary fields |
| Board | Native board ID, explicit board selection and dispatcher DB |
| Bank | Effective provider/bank and exact per-role tags/match settings |
| Models/reasoning | Native configuration and effective overrides; existing role default/max fields |
| Team-Codex | Actual binary, separate process/config homes, access and identity under [Integrations](integrations.md#team-codex), plus [effective home instructions](integrations.md#team-codex-instructions) |
| Analysis | Planner, Reviewer and Team-Codex: exactly the confirmed branch, complete assets and native connection/configuration readbacks |
| Communication | Planner-only bot, exact authorized user/channel/DM IDs and genuine Home binding; later task subscriptions remain operational |

- **Workspace.** Bind Planner `PROJECT_DIR`, native `terminal.cwd` and board default workspace to the confirmed workspace. Bind `REPOSITORY_ROOTS` to confirmed boundaries with separate planning and implementation assignments. Preserve nested or distinct roots. Record confirmed repository absence. Keep Planner's Git-root, cwd, board and ticket checks.
- **Identity and tasks.** Match confirmed technical `PLANNER_PROFILE` to native registration and render it into the Coder SOUL for Planner wake and TIMER. Derive only new profile IDs using setup normalization. Preserve confirmed IDs and use actual paths independent of display names. Reuse confirmed values. Resolve conflicting bindings before writing role files. Keep branch, plan revision and ticket/run/event IDs task-specific.
- **Routing.** For a missing customer decision, Coder keeps assignment and blocks the same card with `kind="needs_input"`. The existing subscription wakes Planner for Mattermost coordination. After recording a sufficient answer, Planner uses ordinary unblock or guarded triage recovery. Route `kanban_request_review` only to the independent Reviewer.
- **Reasoning.** Keep fixed Planner/Hermes-Coder reasoning in native config. Keep Reviewer/Team-Codex defaults and maxima in current role fields. Resolve native model IDs, supported levels and limits during preparation. Read back actual config and overrides without model probes. Treat role maxima as policy. Verify unchanged VoltAgent TOMLs and original model/reasoning availability through [their recipe](integrations.md#codex-agents).
- **Access and record.** Keep communication access and channels with Planner. Use protected native access for secrets. Record values, targets and evidence in the private [setup record](../templates/setup-record.md). Add no runtime binding file.

## 4. Setup readbacks and resume

Compare profiles, board/workspace, bank, actual homes, effective model configuration, complete skill trees, full SOUL and Team-Codex instruction loading, recovery output and modes against confirmed bindings.
Use established discovery/configuration readbacks. Skip synthetic handoff, wake and worker experiments.
Reuse preparation acceptance for role personalization; compare exact rendered output with that scope before writing.
A concrete mismatch needs resolution before the affected write or activation.
On resume, read the single setup JSON and actual targets; continue only the incomplete step.
Correct stale descriptive prose without repeating confirmed decisions or creates.

Execute only for explicitly commissioned target setup. Package edits grant no activation authority.
