# Bezugsquellen

Diese Übersicht nennt Quellen, benötigten Umfang und Zielrollen. Die Einrichtung
steht in [setup.md](setup.md) und [integrations.md](integrations.md).
„Coder“ bezeichnet den Hermes-Coding-Orchestrator, „Team-Codex“ dessen getrennten
Codex-Arbeitskontext; „alle Hermes-Rollen“ meint Planner, Coder und Reviewer.

## Mitgelieferte Bausteine

Die eigenen Skills sind fertige Pakete: den jeweiligen vollständigen Baum aus
`skills/` unverändert kopieren, einschließlich Begleitdateien. Keine
Template-Verarbeitung und keine Umbenennung ihrer `SKILL.md`.

| Skill / lokale Quelle | Ziel |
|---|---|
| <a id="own-planning"></a>[brownfield-feature-planning](../skills/brownfield-feature-planning/SKILL.md) | Hermes-Planner |
| <a id="own-minimal"></a>[minimal-change-engineering](../skills/minimal-change-engineering/SKILL.md) | Hermes-Planner und -Reviewer |
| <a id="own-plan-versioning"></a>[plan-versioning-semver](../skills/plan-versioning-semver/SKILL.md) | Hermes-Planner |
| <a id="own-lib-versioning"></a>[project-lib-versioning](../skills/project-lib-versioning/SKILL.md) | Alle Hermes-Rollen |
| <a id="own-screenshot"></a>[screenshot-to-code](../skills/screenshot-to-code/SKILL.md) | Alle Hermes-Rollen und Team-Codex |

<a id="own-roles"></a>
Die SOUL-Vorlagen für [Planner](../templates/roles/planner.SOUL.md.template),
[Coder](../templates/roles/coder.SOUL.md.template) und
[Reviewer](../templates/roles/reviewer.SOUL.md.template) gehören jeweils zum
entsprechenden Hermes-Profil. Nur die vorgesehenen Platzhalter durch bestätigte
Werte ersetzen; den übrigen Inhalt erhalten.

## Fremdkomponenten

Geeignete vorhandene Installationen wiederverwenden. Bei neuem Bezug den konkreten
Originalstand und dessen Dateiumfang prüfen und Version/Revision im Setup-Protokoll
festhalten. Die folgenden Repositorypfade benennen die Bezugsstellen, keine fest
vorgeschriebenen Versionen oder bereits nachgewiesenen Installationen.

Vollständige Skill-/Pluginpakete samt benötigten Begleitdateien übernehmen, nicht
nur einzelne Einstiegstexte. Die zum Bezugsstand gehörenden Lizenz- und
Notice-Dateien erhalten, auch wenn sie oberhalb eines ausgewählten Unterbaums liegen.

| Komponente | Originalquelle | Benötigter Umfang | Ziel |
|---|---|---|---|
| <a id="hermes-core"></a>Hermes-Basis | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), [Dokumentation](https://hermes-agent.nousresearch.com/docs/) | Vorhandene funktionsfähige Hermes-Installation | Alle Hermes-Rollen |
| <a id="hermes-codex"></a>Hermes-codex | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Vollständiges `skills/autonomous-ai-agents/codex` | Hermes-Coder |
| <a id="hermes-review"></a>sdlc-review | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Vollständiges `skills/devops/sdlc-review` | Hermes-Reviewer |
| <a id="codex-cli"></a>Codex CLI | [openai/codex](https://github.com/openai/codex) | Geeignete vorhandene Binary oder offizielles Release für das Zielsystem | Team-Codex |
| <a id="superpowers"></a>Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Vollständiges Pluginrepository einschließlich `.hermes-plugin/plugin.yaml`, `__init__.py` und `skills/` | Hermes-Planner |
| <a id="grill-me"></a>grill-me / grilling | [mattpocock/skills](https://github.com/mattpocock/skills) | Vollständige Bäume `skills/productivity/grill-me` und `skills/productivity/grilling` einschließlich `agents/`, benötigter Referenzen und MIT-`LICENSE` aus dem Repositoryroot | Hermes-Planner |
| <a id="hindsight"></a>Hindsight-Integration | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Vollständiges `hindsight-integrations/hermes`; vorhandenen Hindsight-Dienst anbinden | Alle Hermes-Rollen |
| <a id="ponytail"></a>Ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Vollständiges Repository mit Hermes-Plugin, `.codex-plugin/plugin.json`, Skills und Hooks | Hermes-Coder und Team-Codex |
| <a id="caveman"></a>Caveman | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Vollständiges `skills/caveman` für den Chatstil, nicht das zusätzliche CLI-/Proxyprodukt | Hermes-Coder, Hermes-Reviewer und Team-Codex |
| <a id="find-skills"></a>find-skills | [vercel-labs/skills](https://github.com/vercel-labs/skills) | Vollständiges `skills/find-skills` | Team-Codex |
| <a id="codex-agents"></a>Codex-Custom-Agents | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | Die unten aufgeführten Originaldateien | Team-Codex |

### Codex-Custom-Agents: Originaldateien

- `categories/04-quality-security/test-automator.toml`
- `categories/04-quality-security/security-auditor.toml`
- `categories/04-quality-security/reviewer.toml`
- `categories/04-quality-security/anti-ui-slop-reviewer.toml`
- `categories/01-core-development/ui-fixer.toml`
- `categories/03-infrastructure/docker-expert.toml`

Original-Modell- und Reasoning-Pins erhalten. Fehlende Modellverfügbarkeit als
Blocker melden. Der Codex-Agent `reviewer` ersetzt nicht die Hermes-Reviewrolle.

## Codeanalyse: genau eine Alternative

| Komponente | Originalquelle | Benötigter Umfang | Ziel |
|---|---|---|---|
| <a id="codebase-memory"></a>Codebase-memory | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Passendes offizielles Release und vollständige native Hermes-/Codex-Integration: Originalskill, MCP, Hooks sowie die zu CBM gehörenden Codex-Unteragenten; `LICENSE` und Release-`THIRD_PARTY_NOTICES.md` erhalten. | Alle Hermes-Rollen und Team-Codex |
| <a id="graphify"></a>Graphify | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Runtime; für Hermes `graphify/skill-claw.md` und vollständiges `graphify/skills/claw/references/`, für Codex `graphify/skill-codex.md` und vollständiges `graphify/skills/codex/references/`; `LICENSE`, `LICENSE-MIT` und `NOTICE` erhalten. | Alle Hermes-Rollen und Team-Codex |

Auswahl und Einrichtung stehen in [code-analysis.md](code-analysis.md). Diese Quellenübersicht ersetzt weder
das jeweilige Integrationsrezept noch die Funktionsprüfung im Zielkontext.
