# Bezugsquellen

Diese Übersicht nennt Quellen, benötigten Umfang und Zielrollen. Die Einrichtung
steht in [setup.md](setup.md) und [integrations.md](integrations.md).
„Coder“ bezeichnet den Hermes-Coding-Orchestrator, „Team-Codex“ dessen getrennten
Codex-Arbeitskontext; „alle Hermes-Rollen“ meint Planner, Coder und Reviewer.

## Mitgelieferte Bausteine

Copy each complete skill tree from `skills/`, including companion files.
Keep all skill names and bytes unchanged except `brownfield-feature-planning/scripts/recover-triage`.
Bind that launcher through the Maker's [recovery binding step](setup.md#bind-the-planner-recovery-invocation).

| Skill / lokale Quelle | Ziel |
|---|---|
| <a id="own-planning"></a>[brownfield-feature-planning](../skills/brownfield-feature-planning/SKILL.md) | Hermes-Planner |
| <a id="own-minimal"></a>[minimal-change-engineering](../skills/minimal-change-engineering/SKILL.md) | Hermes-Planner |
| <a id="own-plan-versioning"></a>[plan-versioning-semver](../skills/plan-versioning-semver/SKILL.md) | Hermes-Planner |
| <a id="own-lib-versioning"></a>[project-lib-versioning](../skills/project-lib-versioning/SKILL.md) | Planner and Coder |
| <a id="own-retro"></a>[retro](../skills/retro/SKILL.md) | Hermes-Planner |
| <a id="own-screenshot"></a>[screenshot-to-code](../skills/screenshot-to-code/SKILL.md) | Planner, Coder and Team-Codex |

The owned `retro` adapts Matt Pocock's method; retain its complete [NOTICE](../skills/retro/NOTICE.md), [MIT license](../skills/retro/LICENSE), and method reference.
It is not an upstream runtime component. Copy its complete tree through the normal own-skill setup/update path.
Before installing or updating it, check the target's native command registry and all resolved skill candidates for `retro` collisions.
Reuse the same managed skill through the normal update comparison; resolve any unrelated same-name skill or built-in command with the user before writing, rather than silently renaming or shadowing it.
Read back one unambiguous owned `retro` and its complete reference through native discovery/loading; distinguish slash-command availability from an existing conversation's cached catalog.
Do not execute a retrospective as an installation test. Invocation requires an explicit user request, such as `/retro` or a natural-language retrospective request.

<a id="own-roles"></a>
Die SOUL-Vorlagen für [Planner](../templates/roles/planner.SOUL.md.template),
[Coder](../templates/roles/coder.SOUL.md.template) und
[Reviewer](../templates/roles/reviewer.SOUL.md.template) gehören jeweils zum
entsprechenden Hermes-Profil. Nur die vorgesehenen Platzhalter durch bestätigte
Werte ersetzen; den übrigen Inhalt erhalten.

<a id="tas"></a>
## TAS authoring upstream

TAS is maintained only in [ataian/tas](https://github.com/ataian/tas), not in this Maker.
For Maker instruction authoring/review, read the selected TAS `SKILL.md` completely and follow all required references before drafting.
Resolve its references against that TAS entrypoint, not the Maker checkout.
Use the sibling `../tas/SKILL.md` relative to the Maker root when that checkout is the commissioned TAS working tree; verify its Git origin and record its HEAD plus local changes.
Otherwise use a complete checkout of `upstream_components.tas.original_repo` at its manifest `source_revision`, outside active discovery.
Reuse a verified checkout or obtain it only within the authorized file-work scope; reading these instructions does not authorize installation or checkout replacement.
If the source or a required reference is missing or unreadable, report the exact path and stop the affected authoring step.
Keep `SKILL.md`, `references/`, provenance, and all legal files together; maintain normative wording upstream rather than copying it back here.

The manifest pin identifies published TAS `1.1.0`, including the writing-for-agents adaptation.
Pin maintenance requires verification of the actual published commit before advancing `source_revision`.
Record local working-tree changes separately from that published identity.
TAS has no team-role targets and is not installed into Planner, Coder, Reviewer, or Team-Codex by setup or team updates.
Their existing SOUL and Caveman contracts remain unchanged; ordinary team setup does not load this authoring branch.

## Fremdkomponenten

Read `upstream_components` in the [manifest](../manifest.json) as the required source inventory.
The TAS entry is an authoring dependency with empty `targets`; use its separate branch above, not the target-installation recipes.
For independent assets, use `original_repo`, exact `source_revision`, complete `subpaths`, `legal_files`, and assigned `targets`.
Resolve `source_component` before acquisition; `caveman-review` inherits the Caveman commit.
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

Maintenance provenance, checked 11 November 2026: Superpowers `v7.0.2`, Caveman `v4.1.0`, CBM `v0.12.1`, Graphify `v0.9.106` and Codex `rust-v0.167.1` resolve to the manifest commits.
Graphify's default branch is `v8`, not `main`.
Ponytail, Matt Pocock's selected skills, the Hindsight adapter and find-skills use the inspected default-branch commits.
Ponytail's plugin manifests identify `5.3.3`; the Hindsight adapter manifests identify `1.2.4`, independently of the service release.
The six VoltAgent files retain the existing manifest commit, which matched upstream HEAD.
Caveman's selected skill/legal bytes match the newer HEAD; retain the release commit.
Graphify's bundle hashes now derive from the selected release, replacing the historical `86c57be8204673c2a1b9849a3292a7dd3ab373d8` evidence.
CBM's existing static asset evidence derives from its selected `v0.12.1` source; it is not installer-output or live-runtime evidence.

| Komponente | Originalquelle | Benötigter Umfang | Ziel |
|---|---|---|---|
| TAS | [ataian/tas](https://github.com/ataian/tas) | Complete standalone root skill tree, provenance and all `third_party/` legal files; see [authoring branch](#tas) | Maker authoring/review only; no team-role installation |
| <a id="hermes-core"></a>Hermes-Basis | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), [Dokumentation](https://hermes-agent.nousresearch.com/docs/) | Vorhandene funktionsfähige Hermes-Installation | Alle Hermes-Rollen |
| <a id="hermes-codex"></a>Hermes-codex | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Vollständiges `skills/autonomous-ai-agents/codex` | Hermes-Coder |
| <a id="hermes-review"></a>sdlc-review | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Vollständiges `skills/devops/sdlc-review` | Hermes-Reviewer |
| <a id="codex-cli"></a>Codex CLI | [openai/codex](https://github.com/openai/codex) | Geeignete vorhandene Binary oder offizielles Release für das Zielsystem | Team-Codex |
| <a id="superpowers"></a>Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Vollständiges Pluginrepository einschließlich `.hermes-plugin/plugin.yaml`, `__init__.py` und `skills/` | Hermes-Planner |
| <a id="grill-me"></a>grill-me / grilling / domain-modeling / to-questionnaire | [mattpocock/skills](https://github.com/mattpocock/skills) | Complete `skills/productivity/grill-me`, `skills/productivity/grilling`, `skills/engineering/domain-modeling`, and `skills/productivity/to-questionnaire` trees, including `GLOSSARY-FORMAT.md`, `ADR-FORMAT.md`, `agents/openai.yaml`, and applicable legal files including root MIT `LICENSE`; same manifest revision | Hermes-Planner |
| <a id="hindsight"></a>Hindsight-Integration | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Vollständiges `hindsight-integrations/hermes`; vorhandenen Hindsight-Dienst anbinden | Alle Hermes-Rollen |
| <a id="ponytail"></a>Ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Vollständiges Repository mit Hermes-Plugin, `.codex-plugin/plugin.json`, Skills und Hooks | Hermes-Coder und Team-Codex |
| <a id="caveman"></a>Caveman | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Complete `skills/caveman`, root `LICENSE`, `LICENSE-MIT`, `NOTICE`; writing only | All Hermes roles and Team-Codex |
| <a id="caveman-review"></a>Caveman Review | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Complete `skills/caveman-review` and the same legal files and revision; finding format only | Hermes-Reviewer |
| <a id="find-skills"></a>find-skills | [vercel-labs/skills](https://github.com/vercel-labs/skills) | Vollständiges `skills/find-skills` | Team-Codex |
| <a id="codex-agents"></a>Codex-Custom-Agents | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | Die unten aufgeführten Originaldateien | Team-Codex |

### Codex-Custom-Agents: Originaldateien

The [manifest](../manifest.json) is the version inventory for this component.
Read `upstream_components.codex-custom-agents`: `original_repo`, `source_revision`, `subpaths`, and `legal_files`.
Setup and updates use that exact revision, not a moving branch or the historical research anchor.

- `categories/04-quality-security/test-automator.toml`
- `categories/04-quality-security/security-auditor.toml`
- `categories/04-quality-security/reviewer.toml`
- `categories/04-quality-security/anti-ui-slop-reviewer.toml`
- `categories/01-core-development/ui-fixer.toml`
- `categories/03-infrastructure/docker-expert.toml`

Keep all six TOMLs byte-identical to that revision through [the helper recipe](integrations.md#codex-agents).
Use their original model and reasoning settings, separately from the Team-Codex main-process policy.
The Codex agent `reviewer` does not replace the independent Hermes Reviewer.

## Codeanalyse: genau eine Alternative

| Komponente | Originalquelle | Benötigter Umfang | Ziel |
|---|---|---|---|
| <a id="codebase-memory"></a>Codebase-memory | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Passendes offizielles Release und vollständige native Hermes-/Codex-Integration: Originalskill, MCP, Hooks sowie die zu CBM gehörenden Codex-Unteragenten; `LICENSE` und Release-`THIRD_PARTY_NOTICES.md` erhalten. | Planner, Coder, Reviewer and Team-Codex |
| <a id="graphify"></a>Graphify | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Runtime; für Hermes `graphify/skill-claw.md` und vollständiges `graphify/skills/claw/references/`, für Codex `graphify/skill-codex.md` und vollständiges `graphify/skills/codex/references/`; `LICENSE`, `LICENSE-MIT` und `NOTICE` erhalten. | Planner, Coder, Reviewer and Team-Codex |

Use only the selected branch in [Code analysis](code-analysis.md).
This source inventory does not replace its concrete setup recipe.
Verify availability and setup outputs without behavioral qualification.
