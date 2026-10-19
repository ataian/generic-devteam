# Originalquellen und Bezugsvertrag

## Stand und Verwendung

Dies ist die Quellen- und Rezeptzuordnung des T5-Lieferstands. Der [geführte Setupweg](setup.md), die [allgemeinen Integrationsrezepte](integrations.md) und beide [Codeanalysealternativen](code-analysis.md) sind enthalten; ihre Manifestverweise stehen auf `documented`. G2/A01-CBM bleibt ausdrücklich offen. Die Einträge behaupten keine erfolgreiche Installation. Vor Zielbezug den geeigneten Originalstand neu auflösen, Version/Revision, vollständige Assetmenge und Lizenz-/Noticepflichten dokumentieren; erst im bestätigten Zielscope einrichten und prüfen. Vorhandene geeignete Distributionen wiederverwenden.

Das [Manifest](../manifest.json) ordnet die Quellen maschinenlesbar zu. `hermes: coder` bedeutet Coding-Orchestrator; `codex: team-codex` bedeutet den getrennten Teamzustand. Rollen sind Funktionen, keine vorhandenen Profilnamen. Für beide Analysealternativen gilt dieselbe Rollenmatrix; beim Setup wird genau ein Weg gewählt.

## Eigene Fähigkeiten: enthaltene T2-Fassungen

Alle folgenden Fähigkeiten sind vollständig enthalten. [NOTICE](../NOTICE.md) beschreibt G3: Screenshot wird unverändert übernommen, die übrigen fünf Fähigkeiten sind neu aus bestätigten Regeln formuliert. Jede Neufassung enthält ihre eigene vollständige MIT-Lizenz und Herkunftsnotice. Private Quellpfade bleiben außerhalb des Exports; die öffentlichen Screenshot-Dateihashes dienen dem portablen Integritätscheck.

<a id="own-workflow"></a>
### devteam-workflow

Fachliche Vorläufer: historische Planhandoff-, Phasenfortführungs-, Review-Handoff- und Routingregeln. Neue eigene Anleitung aus dem bestätigten Gesamtprozess: Planannahme, reale Bindungen, geordnete Ticketkette, Codex-Auftrag, nativer Handoff/Rückweg und Planner-Wake. Keine alten operativen Helper übernommen. Der [installierbare Workflow](../templates/skills/devteam-workflow/SKILL.md.template) enthält seine eigene native Referenz; die [Makerreferenz](native-workflow.md) besitzt nur Einrichtung und Bindungsprüfung. Ziel: alle drei Hermes-Rollen; Codex erhält Arbeitsgrenzen im Auftrag, keine direkte Skillinstallation.

<a id="own-planning"></a>
### brownfield-feature-planning

Fachlicher gemeinsamer Kern aus `brownfield-feature-planning` und `codebase-update-planning`: Regeln und Bestand, Definitionen/Aufrufer/Datenpfade, Wiederverwendung, Annahmen, Datei-/Abhängigkeitsmatrix und prüfbare Phasen. Neu aus bestätigten Anforderungen formuliert; spezialisierte historische Verfahren sind Vergleichsquellen, keine zweite exportierte Methodik. Ziel: Hermes-Planner.

<a id="own-minimal"></a>
### minimal-change-engineering

Portable Sammlungsversion als fachliche Grundlage; Quellangabe `Max (drafted) + Joi`, MIT-Identifier, fehlender separater ursprünglicher Lizenztext. Historische Texte wurden nicht übernommen; die bestätigten Regeln sind eigenständig neu formuliert. Inhaltliche Anpassungen: vorhandene Projektprüfungen und Fixtures verwenden, Schutz-/Verifikationspflichten erhalten, lokale Zustandsannahmen entfernen und Rollenverteilung klarstellen. Ziel: Hermes-Planner und -Reviewer; Ponytail ist gesonderte Coder-/Codex-Ausstattung.

<a id="own-plan-versioning"></a>
### plan-versioning-semver

Historische gleichnamige Konvention ohne belegte ursprüngliche Lizenz. Eigenständig aus bestätigten Regeln formuliert: eigene Plan-SemVer, historische Fassungen erhalten, gültige Index-/Ticketreferenzen, bekannte JIRA-Verweise ohne Integration. Produktgebundene Version-API- und Changelogvorgaben entfallen. Ziel: Hermes-Planner.

<a id="own-lib-versioning"></a>
### project-lib-versioning

Fachliche Vorläufer sind generische und projektgebundene Bibliotheksversionsregeln; Auditverweis der abgeleiteten Vorlage ist nicht belegt. Neue technologieunabhängige Formulierung der bestätigten Regeln zu Verträgen, rekursiven Verbrauchern, Versionsauflösung und Build-/Testnachweisen. Ziel: alle drei Hermes-Rollen mit eigener Zuständigkeit; Codex erhält konkrete Arbeitsvorgaben, keine zusätzliche direkte Skillinstallation.

<a id="own-screenshot"></a>
### screenshot-to-code

Kanonisches eigenständiges Paket `screenshot-to-code` 1.0.0; Autorenfeld `Max, Mariko (Hermes Agent)`, MIT, Notice `Copyright (c) 2026 screenshot-to-code contributors`. Portabler Quellumfang: `SKILL.md`, `LICENSE`, `references/offline-export.md`, `references/runtime-usage.md`, `references/source-and-assets.md`, `references/visual-check.md`. Es wird kein öffentliches Ursprungsrepository behauptet. Diese sechs Dateien sind inhaltlich unverändert enthalten; ausschließlich der Einstieg wird für den Transport in `SKILL.md.template` umbenannt. Der rückbenannte Baum wurde intern bytegenau gegen die kanonische Quelle geprüft; das Manifest führt die vollständigen kanonischen SHA-256-Identitäten für öffentliche Integritätsprüfungen. Ziel: alle drei Hermes-Rollen und Team-Codex. Die vollständige quelleneigene Lizenz ist innerhalb des Skillpakets mitgeliefert.

<a id="own-roles"></a>
## Eigene Rollen-SOULs: quellnahe aktuelle Fassungen

[Planner](../templates/roles/planner.SOUL.md.template) und
[Coder](../templates/roles/coder.SOUL.md.template) sind im ausdrücklich bestätigten
Auftrag quellnah aus den vorhandenen Rollen-SOULs abgeleitet: Struktur, Methodik,
Berichtswege und die genehmigte portable Plannerregel bis zu drei
Budgeterweiterungen bleiben erhalten. Persönliche Projekt-/Teambindungen werden
durch erklärte Felder ersetzt; Modellrouten stammen aus aktueller bestätigter
Policy und Konfiguration, nicht aus SOUL-Pins. Keine aktiven Profile werden exportiert.
Der [Reviewer](../templates/roles/reviewer.SOUL.md.template) ist die vom Nutzer
überarbeitete maßgebliche Vorlage und wird bei der Makerintegration nicht geändert.
Die frühere T3-Neufassung und ihre Integration sind historischer Lieferstand,
keine Beschreibung dieser aktuellen Rollen. Es gibt keinen erzwungenen bytegleichen
neunstufigen Prozess. Herkunft und Grenzen stehen in der [Notice](../NOTICE.md);
die private Vergleichsquelle ist weder Paketbestandteil noch Testabhängigkeit.

`role_templates` ordnet jede Vorlage genau einem Hermes-Rollenprofil zu. Keine
Rollen-SOUL wird als Codex-Profil installiert: Codex bekommt Arbeitsgrenzen im
Auftrag. Der [Render-/Kontextvertrag](native-workflow.md) erklärt alle Namen,
Projekt-/Bank-/Boardfelder und technischen Profilwerte; Anzeigenamen sind
keine technischen IDs. Nur tatsächlich vorkommende Felder werden übergeben,
Mehrfachvorkommen ersetzt und alle anderen Bytes erhalten. Keine Persona-Abfrage.
Der [reine Textweg](render_text.py) wird im [Setupweg](setup.md) verbindlich genutzt,
mit bestätigten Rohwerten aus dem privaten Record auch bei Wiederaufnahme.
Das ist kein operativer Setuphelfer und kein Nachweis effektiver Promptaufnahme.

## Fremdkomponenten: Originalquelle und Zielrezepte

<a id="hermes-core"></a>
### Hermes-Basis — T4-Rezept dokumentiert

Original: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), Repositoryroot `.`. Ziel: alle drei Hermes-Rollen. Vorhandene Distribution auf native Profile, Board, Dispatcher, Gateway, Review und Wake prüfen. Referenz für spätere native Rezepte: [offizielle Dokumentation](https://hermes-agent.nousresearch.com/docs/). Kein Coreexport und kein eigener Ersatzdienst. Zielversion, unterstützte Schnittstellen und native Funktionsnachweise gehören zum Setup; insbesondere bleibt die Garantie begrenzter automatischer Rate-Limit-Wiederholungen ein gesondertes Kompatibilitätsgate.

<a id="hermes-codex"></a>
### Hermes-codex — T4-Rezept dokumentiert

Original: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), vollständiges Verzeichnis `skills/autonomous-ai-agents/codex`. Ziel: Hermes-Coding-Orchestrator. Vorhandenen Basisskill und seine Begleitdateien/Notices verwenden; Auflösung und echten Codex-Arbeitsweg im Teamkontext später belegen.

<a id="hermes-review"></a>
### sdlc-review — T4-Rezept dokumentiert

Original: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), vollständiges Verzeichnis `skills/devops/sdlc-review`. Ziel: Hermes-Reviewer. Fachliche Reviewfähigkeit bleibt eigenständig neben dem eigenen Ablaufskill. Später Skillauflösung und unabhängigen nativen Review am selben Ticket belegen.

<a id="codex-cli"></a>
### Codex CLI — T4-Rezept dokumentiert

Original: [openai/codex](https://github.com/openai/codex), Repositoryroot `.` für Releaseherkunft. Ziel: Team-Codex. Geeignete vorhandene Binary wiederverwenden; teambezogene Konfiguration und effektive Skillablagen getrennt binden. Native Anmeldung durch den Nutzer, Discovery und echter Aufruf sind spätere Nachweise; Hermes-Login beweist keinen Codex-Zugang.

<a id="superpowers"></a>
### Superpowers — T4-Rezept dokumentiert

Original: [obra/superpowers](https://github.com/obra/superpowers), vollständiges Repository `.` mit Hermes-Einstieg `.hermes-plugin/plugin.yaml`, `__init__.py` und vollständigen `skills/`. Ziel: Hermes-Planner. Native Pluginauflösung, Aktivierung und tatsächlich geladene Regeln prüfen; eine Skilltextkopie allein ersetzt das Plugin nicht.

<a id="hindsight"></a>
### Hindsight-Integration — T4-Rezept dokumentiert

Original: [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight), vollständiger Unterbaum `hindsight-integrations/hermes` mit Begleitdateien und benötigten übergeordneten Rechtshinweisen. Ziel: alle drei Hermes-Rollen. Vorhandenen Dienst verwenden, neue gemeinsame Projektbank und Rollenfilter bestätigen. Konfiguration, tatsächliche Requestfilter und Speicherung getrennt belegen; Reflect einschließlich Prefetch setzt nachgewiesene Filterweitergabe voraus.

<a id="ponytail"></a>
### Ponytail — T4-Rezept dokumentiert

Original: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), vollständiges Repository `.`; Hermes `plugin.yaml`/`__init__.py`, Codex `.codex-plugin/plugin.json`, Skill- und Hookbegleitdateien. Ziel: Hermes-Coder und Team-Codex. Native Wege je Harness getrennt ausarbeiten, dauerhaften Modus `full` und wirksamen Hookkontext später nachweisen. Notwendige Fremdpluginänderungen sind ein Blocker, keine Forkfreigabe.

<a id="caveman"></a>
### Caveman — T4-Rezept dokumentiert

Original: [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), vollständiger Hauptskill `skills/caveman` plus Lizenz-/Notice-Dateien des Bezugsstands. Ziel: Hermes-Coder, Hermes-Reviewer und Team-Codex. Umfang ist Chatstil, nicht das zusätzliche CLI-/Proxyprodukt. Die recherchierte Abbildung von `full` auf `caveman` beim Zielstand bestätigen; persistente Aktivierung und geladenen Originaltext je Harness prüfen. Code, Dokumentation, Commits, Memory und Sicherheitswarnungen bleiben verständlich und unkomprimiert.

<a id="find-skills"></a>
### find-skills — T4-Rezept dokumentiert

Original: [vercel-labs/skills](https://github.com/vercel-labs/skills), vollständiger Unterbaum `skills/find-skills` plus geltende Rechtshinweise. Ziel: Team-Codex. Skillauflösung und Suche später prüfen. Ein Suchergebnis oder Vorschlag ist keine Freigabe zur Nachinstallation.

<a id="codex-agents"></a>
### Sechs Codex-Custom-Agents — T4-Rezept dokumentiert

Original: [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents). Ziel: Team-Codex, gesteuert durch den Coding-Orchestrator. Genau diese vollständigen Originaldateien beziehen:

- `categories/04-quality-security/test-automator.toml`
- `categories/04-quality-security/security-auditor.toml`
- `categories/04-quality-security/reviewer.toml`
- `categories/04-quality-security/anti-ui-slop-reviewer.toml`
- `categories/01-core-development/ui-fixer.toml`
- `categories/03-infrastructure/docker-expert.toml`

Original-Modell-/Reasoning-Pins erhalten, Revision und Lizenz separat dokumentieren. Bei fehlender Modellverfügbarkeit den Blocker melden. Später Discovery und je einen begrenzten echten Delegationsaufruf belegen; der Codex-Helfer `reviewer` ersetzt nicht die unabhängige Hermes-Reviewrolle.

<a id="codebase-memory"></a>
### Codebase-memory — T5-Rezept dokumentiert, G2/A01-CBM offen

Original: [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp).
[Rezept, Dateimenge und Vergleichsgate](code-analysis.md#codebase-memory) für alle
drei Hermes-Rollen und Team-Codex. Frisch gelesener Release v0.12.1, Commit
`a7158ac2f48ca646b4527341b76f930f2aeff87e`; HEAD
`354ccecbe612a9fdb624396a6738fa87f2617434` separat, CLIbytes identisch.
Originalinterfaces: `src/cli/cli.c` (Skill, Zielresolver, Clients, Hooks),
`src/cli/agent_profiles.c`, `src/cli/config_toml_edit.c`, `src/cli/hook_augment.c`,
`src/mcp/mcp.c`. Linuxarchive/Integrität über Release, `scripts/package-release.sh`
und `scripts/gen-third-party-notices.sh` nachvollziehen. MIT-LICENSE und erzeugte
Release-THIRD_PARTY_NOTICES unverändert erhalten; keine Root-Noticedatei erfinden.
Manifest führt statische Skill-/Pointerhashes, Zielpfade und drei ausgeschlossene
Agent-TOMLs. Keine Originalausgabe ausgeführt: `--plan` liefert keine Assetbytes
und bindet Auswahl/skip-binary nicht verlässlich; [G2](code-analysis.md#g2) nennt
den konkreten Folgeauftrag. Kein Originalinstallerlauf, keine geprüften Archive
oder Liveintegration behauptet.

<a id="graphify"></a>
### Graphify — T5-Rezept dokumentiert

Original: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify),
frisch gelesene Revision `86c57be8204673c2a1b9849a3292a7dd3ab373d8`,
Manifest/Release 0.9.92, Python >=3.10.
[Vollständiges Rezept](code-analysis.md#graphify) für alle drei Hermes-Rollen
und Team-Codex. `graphify/install.py` ordnet Hermes `graphify/skill-claw.md`
plus `graphify/skills/claw/references/` zu, Codex `graphify/skill-codex.md`
plus `graphify/skills/codex/references/`. Beide Hauptdateien und sämtliche
Referenzen (je acht) frisch aus der Originalrevision gelesen; das Manifest
enthält vollständige Quelle→Zielabbildungen und SHA-256 der unveränderten Bytes.
Laufzeit aus `pyproject.toml`, Apache-2.0-`LICENSE`, `LICENSE-MIT` und `NOTICE`
erhalten. Keine eigenen Mischskills, kein pauschaler Installer gegen vermutete
Homevariablen; bestehende Projektanweisungen bleiben erhalten. Discovery und
Index-/Query-/Updatenachweise sind trotz vollständiger Quellenprüfung offen.
