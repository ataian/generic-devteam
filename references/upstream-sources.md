# Sources

Use this inventory with [Setup](setup.md) and [Integrations](integrations.md). Coder is the Hermes orchestrator and Team-Codex is its separate Codex work context. All Hermes roles are Planner, Coder and Reviewer.

## Bundled components

Copy each complete skill tree from `skills/`, including companion files.
Keep all skill names and bytes unchanged except `brownfield-feature-planning/scripts/recover-triage`.
Bind that launcher through the Maker's [recovery binding step](setup.md#bind-the-planner-recovery-invocation).

| Skill / local source | Target |
|---|---|
| <a id="own-planning"></a>[brownfield-feature-planning](../skills/brownfield-feature-planning/SKILL.md) | Hermes Planner |
| <a id="own-build-evidence"></a>[build-evidence](../skills/build-evidence/SKILL.md) | Reviewer and Team-Codex |
| <a id="own-demo-handover"></a>[demo-handover](../skills/demo-handover/SKILL.md) | Hermes Coder |
| <a id="own-dev-environment"></a>[dev-environment](../skills/dev-environment/SKILL.md) | Hermes Planner |
| <a id="own-diagnosis"></a>[diagnosing-bugs](../skills/diagnosing-bugs/SKILL.md) | Team-Codex |
| <a id="own-minimal"></a>[minimal-change-engineering](../skills/minimal-change-engineering/SKILL.md) | Hermes Planner |
| <a id="own-plan-versioning"></a>[plan-versioning-semver](../skills/plan-versioning-semver/SKILL.md) | Planner and Team-Codex |
| <a id="own-prototype"></a>[prototype](../skills/prototype/SKILL.md) | Hermes Planner |
| <a id="own-retro"></a>[retro](../skills/retro/SKILL.md) | Hermes Planner |
| <a id="own-devteam-cleanup"></a>[devteam-cleanup](../skills/devteam-cleanup/SKILL.md) | Hermes Planner |
| <a id="own-screenshot"></a>[screenshot-to-code](../skills/screenshot-to-code/SKILL.md) | Planner and Team-Codex |

Use the owned-skill setup/update path for these trees.

- **`retro`.** Matt Pocock method adaptation with [NOTICE](../skills/retro/NOTICE.md), [MIT license](../skills/retro/LICENSE) and method reference. Check the native command registry and all resolved skill candidates for collisions before delivery. Reuse the managed skill through normal update comparison and resolve any unrelated same-name skill or built-in command with the user before writing. Preserve names and precedence. Read back one unambiguous owned `retro` and its complete reference through native discovery/loading. Track slash-command availability separately from cached conversation catalogs. Invoke only on explicit request, including `/retro` or natural language. Do not execute a retrospective as an installation test.
- **`dev-environment`.** Requested Docker development-environment creation, adoption and revision, including a project database when needed. Check name collisions and native loading without constructing an environment. The generated repository guide supplies routine commands to all roles. The construction skill stays Planner-only. Its requested-demo reference is loaded only after plan acceptance for a requested demo.
- **`build-evidence`.** Build-, browser- and process-dependent test evidence: production-build selectors, portless test containers, and the JFR socket observer. Deliver the complete tree to Reviewer and Team-Codex. Team-Codex passes the literal `$build-evidence` cue for the affected mode. The reference complements the Team-Codex skill block; it adds no product or release permission.
- **`demo-handover`.** Demo runtime procedure for a released demo handover card: start at the reviewed commit, create the demonstration user, seed data, record the card facts. Coder only, copied unchanged; the password stays in the role instructions. [Delivery recipe](integrations.md#demo-handover).
- **`devteam-cleanup`.** Customer-invoked outside delivery, with no automatic trigger or separate upstream source, license or NOTICE. Invoke only on explicit request, including `/devteam-cleanup` or natural language. Skip test cleanup.
- **`diagnosing-bugs`.** Matt Pocock method adaptation with evidence-based direct fix or full diagnosis. Include the method reference, [NOTICE](../skills/diagnosing-bugs/NOTICE.md) and original [MIT license](../skills/diagnosing-bugs/LICENSE). Team-Codex owns routing, invocation and validation of the method. [Delivery recipe](integrations.md#diagnosing-bugs).
- **`prototype`.** Matt Pocock logic/UI adaptation for direct clarification during grilling. Deliver the full tree and legal files only to Planner. [Delivery recipe](integrations.md#prototype).

<a id="own-roles"></a>
Render only confirmed placeholders and preserve all other bytes. Deliver [Planner](../templates/roles/planner.SOUL.md.template), [Coder](../templates/roles/coder.SOUL.md.template) and [Reviewer](../templates/roles/reviewer.SOUL.md.template) to their respective Hermes profiles through [Role bindings](native-workflow.md#2-personalize-role-souls).
The Reviewer SOUL owns proportional Spec/technical-quality investigation. Keep native `sdlc-review` as the review lifecycle prerequisite. Deliver no separate `code-review` skill or method file. [Exact Matt source and adaptation](../NOTICE.md#bounded-review-adaptation-code-review).

<a id="tas"></a>
<a id="tas-authoring-upstream"></a>
## TAS attribution

[TAS 1.2.0](https://github.com/ataian/tas) at `fe3a7d251518b793fedaec3041558c2840b4c796` was the Maker authoring baseline, including writing-for-agents and addition reconciliation.
Its complete standalone entrypoint, `references/`, provenance and `third_party/` legal files remain upstream.
For current Maker instruction authoring and review, read [Compact Artifact Contract](cac-authoring.md).

<a id="caveman"></a>
<a id="caveman-review"></a>
## Caveman attribution

Previous Maker manifests used [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) `v4.1.0` at `1e91f1306d602d4ca23618701b1185575ae1869b`.
`skills/caveman` supplied writing guidance to all Hermes roles and Team-Codex. `skills/caveman-review` supplied finding format to Reviewer.
Both used the same revision and original `LICENSE`, `LICENSE-MIT`, and `NOTICE`.
For existing teams, use [CAC migration](update.md#cac-migration) and recorded provenance.

## Third-party components

Read `upstream_components` in the [manifest](../manifest.json) as the required source inventory.
For independent assets, use `original_repo`, exact `source_revision`, complete `subpaths`, `legal_files`, and assigned `targets`.
Resolve any `source_component` before acquisition.
Acquire those commits outside active discovery without searching for a newer version during setup or team updates.
Compare complete file inventories and original bytes, including hidden files, companions, and applicable legal files above selected subtrees.
For `subpaths: ["."]`, retain the complete plugin repository, not only its skills or entry manifest.
Preserve native runtime state separately from immutable upstream package files.
Record required source, observed installed source, hashes, targets and native readbacks separately in the existing private setup/update record.
Unknown installed provenance stays unknown until resolved; matching current bytes do not prove an earlier pristine baseline.

Hermes core, `hermes-codex` and `sdlc-review` are native-managed prerequisites without Maker pins.
Maker does not install, upgrade, downgrade or repair Hermes or its distribution skills.
The Hindsight pin covers only `hindsight-integrations/hermes` and legal files; its service remains outside Maker updates.
Codex CLI has a release/source target, not an automatic shared-binary replacement instruction.
CBM and Graphify asset pins do not force installed runtimes to that revision.
Inspect existing/shared installations and compatibility before setup; preserve compatible installations.
Use [Integrations](integrations.md) for initial-installation scope and [Team updates](update.md#required-upstream-companion-update) for advance update approval.

### Pin maintenance

Select latest appropriate upstream sources only during deliberate Maker maintenance.
Resolve release tags to full commit IDs, including annotated-tag peeling.
Prefer official releases for release-coupled assets; use current default-branch commits for independently shipped skill/plugin trees when appropriate.
Verify selected paths, native manifests, complete bundles, legal files and any recorded hashes at that exact commit.
Keep upstream bytes unchanged, including models, reasoning and skill metadata.
Update pins, affected recipes and coupled hash evidence coherently through the normal Maker patch release.
Do not infer individual skill or adapter versions from a repository release number.
Pins are required source targets, not approval for operational changes.

On 11 November 2026, Superpowers `v7.0.2`, Caveman `v4.1.0`, CBM `v0.12.1`, Graphify `v0.9.106` and Codex `rust-v0.167.1` resolved to their then-current manifest commits.
Graphify's default branch is `v8`, not `main`.
Ponytail, Matt Pocock's selected skills, the Hindsight adapter and find-skills use the inspected default-branch commits.
Ponytail's plugin manifests identify `5.3.3`; the Hindsight adapter manifests identify `1.2.4`, independently of the service release.
The six VoltAgent files retain the existing manifest commit, which matched upstream HEAD.
Caveman's selected skill and legal bytes matched the newer HEAD. The historical pin used the release commit.
Graphify's bundle hashes now derive from the selected release, replacing the historical `86c57be8204673c2a1b9849a3292a7dd3ab373d8` evidence.
CBM's existing static asset evidence derives from its selected `v0.12.1` source; it is not installer-output or live-runtime evidence.

| Component | Original source | Required scope | Target |
|---|---|---|---|
| <a id="hermes-core"></a>Hermes base | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), [documentation](https://hermes-agent.nousresearch.com/docs/) | Existing functional Hermes installation | All Hermes roles |
| <a id="hermes-codex"></a>Hermes-codex | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Complete `skills/autonomous-ai-agents/codex` | Hermes Coder |
| <a id="hermes-review"></a>sdlc-review | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Complete `skills/devops/sdlc-review` | Hermes Reviewer |
| <a id="codex-cli"></a>Codex CLI | [openai/codex](https://github.com/openai/codex) | Suitable existing binary or official release for the target system | Team-Codex |
| <a id="superpowers"></a>Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Complete plugin repository including `.hermes-plugin/plugin.yaml`, `__init__.py` and `skills/` | Hermes Planner |
| <a id="grill-me"></a>grill-me / grilling / domain-modeling / to-questionnaire | [mattpocock/skills](https://github.com/mattpocock/skills) | Complete `skills/productivity/grill-me`, `skills/productivity/grilling`, `skills/engineering/domain-modeling`, and `skills/productivity/to-questionnaire` trees, including `GLOSSARY-FORMAT.md`, `ADR-FORMAT.md`, `agents/openai.yaml`, and applicable legal files including root MIT `LICENSE`; same manifest revision | Hermes Planner |
| <a id="hindsight"></a>Hindsight integration | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Complete `hindsight-integrations/hermes`; connect the existing Hindsight service | All Hermes roles |
| <a id="ponytail"></a>Ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Complete repository with `.codex-plugin/plugin.json`, skills and hooks | Team-Codex |
| <a id="find-skills"></a>find-skills | [vercel-labs/skills](https://github.com/vercel-labs/skills) | Complete `skills/find-skills` | Team-Codex |
| <a id="codex-agents"></a>Codex-Custom-Agents | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | The original files listed below | Team-Codex |

### Codex custom agents: original files

For setup and updates use `original_repo`, exact `source_revision`, `subpaths` and `legal_files` from [`upstream_components.codex-custom-agents`](../manifest.json).

- `categories/04-quality-security/test-automator.toml`
- `categories/04-quality-security/security-auditor.toml`
- `categories/04-quality-security/reviewer.toml`
- `categories/04-quality-security/anti-ui-slop-reviewer.toml`
- `categories/01-core-development/ui-fixer.toml`
- `categories/03-infrastructure/docker-expert.toml`

Keep all six TOMLs byte-identical to that revision through [the helper recipe](integrations.md#codex-agents).
Use their original model and reasoning settings, separately from the Team-Codex main-process policy.
The Codex agent `reviewer` does not replace the independent Hermes Reviewer.

## Code analysis: exactly one alternative

| Component | Original source | Required scope | Target |
|---|---|---|---|
| <a id="codebase-memory"></a>Codebase-memory | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Suitable official release and complete native Hermes/Codex integration: original skill, MCP, hooks and the Codex subagents belonging to CBM; preserve `LICENSE` and release `THIRD_PARTY_NOTICES.md`. | Planner, Reviewer and Team-Codex |
| <a id="graphify"></a>Graphify | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Runtime; for Hermes `graphify/skill-claw.md` and complete `graphify/skills/claw/references/`, for Codex `graphify/skill-codex.md` and complete `graphify/skills/codex/references/`; preserve `LICENSE`, `LICENSE-MIT` and `NOTICE`. | Planner, Reviewer and Team-Codex |

Follow the selected [Code analysis](code-analysis.md) recipe. Verify availability and setup outputs. Reserve behavioral qualification for separate authorization.
