# Codeanalyse einrichten

Configure the **Graphify or CBM** alternative confirmed in [Setup](setup.md) for Planner, Coder and Team-Codex.
Reviewer receives neither integration by default. Preserve existing local Reviewer adaptations; this recipe does not remove them.
Sources and licenses are listed in [Sources](upstream-sources.md#codeanalyse-genau-eine-alternative).
Execute this recipe only during authorized target setup, not Maker authoring.

## Gemeinsame Vorbereitung

1. Check the selected existing runtime, version, skills and integration availability through established interfaces.
   If the common runtime is missing/incompatible, report the prerequisite; do not install or repair it.
2. Reuse confirmed absolute role homes, `CODEX_HOME`, `CODEX_PROCESS_HOME` and target ownership from preparation.
   Preserve symlinks/local edits and back up affected own configuration before authorized changes.
3. Consume the confirmed repository/corpus scope, roots, cache/output locations and optional watcher decision.
   Keep multiple repositories separate. Do not index secrets or project content during setup.
4. Use the agreed profile-local installation and activation scope.
   Disclose target-dependent hook approval during preparation; execute it only after final configuration.
   Do not create a test workspace or run index/query/update experiments.

Die folgenden Pfade und Optionen beim Zielsetup mit der gewählten Version abgleichen.
Vorhandene Projektregeln, fremde Profile und persönliche Codex-Konfiguration bleiben
außerhalb der Team-Einrichtung. Konflikte mit bestehenden Dateien vor dem Schreiben
klären; bei Teilfehlern den tatsächlichen Zustand lesen statt blind erneut installieren.

<a id="graphify"></a>
## Graphify

### 1. Runtime und vollständige Skills bereitstellen

Use the compatible existing Graphify runtime and its actual Python interpreter.
If unavailable, report `graphifyy` and the required compatible runtime as prerequisites.
Do not run `uv tool install` or qualify a shared runtime during setup.

Runtime und Skilldateien müssen zusammenpassen. Aus demselben Bezugsstand die
vollständigen Originalbäume nach folgender Zuordnung kopieren:

| Verbraucher | Originalhauptdatei → `SKILL.md` | Referenzen → `references/` | Zielverzeichnis |
|---|---|---|---|
| Planner and Coder | `graphify/skill-claw.md` | `graphify/skills/claw/references/` vollständig | `<ROLE_HOME>/skills/graphify/` |
| Team-Codex | `graphify/skill-codex.md` | `graphify/skills/codex/references/` vollständig | `<CODEX_PROCESS_HOME>/.agents/skills/graphify/` |

Die zum Paket gehörenden `LICENSE`, `LICENSE-MIT` und `NOTICE` beilegen. Ganze
Dateimengen und Inhalte mit der Quelle vergleichen; keine eigene Skillfassung bauen.
Die Hermes-Zuordnung zur claw-Variante ergibt sich aus Graphifys `graphify/install.py`.
Dessen allgemeiner Installer kann persönliche Standardhomes und Projektanweisungen
beschreiben; für diese profilbezogene Skillablage deshalb die expliziten Ziele nutzen.

### 2. Bind and read back

Verify native discovery/loading of the original `graphify` skill in each assigned harness.
Bind the confirmed output CWD, corpus and runtime interpreter without generating a graph.
For multiple repositories retain separate output locations.
No additional MCP service is required for the normal skill/CLI route.
Do not add a watcher unless its need and effects were confirmed during preparation.
Keep the complete original query, update, export, hook and merge references for later operational tasks.
Later `/graphify <CORPUS>`, `graphify query ...`, and `/graphify <CORPUS> --update` belong to an explicitly authorized project task.
Semantic document/image processing requires its own approved data/provider scope.

<a id="codebase-memory"></a>
## Codebase-memory-mcp (CBM)

### 1. Gemeinsame Runtime bereitstellen

Use the compatible existing original binary and record its exact path/version.
If unavailable, report the missing runtime to the operator; do not download/install/repair it.
Retain its `LICENSE` and `THIRD_PARTY_NOTICES.md` provenance and use the existing runtime for profile-local client integration.

CBM verwendet einen accountweit koordinierten Daemon. Vorhandenen Build, Cache und
Rendezvousbereich berücksichtigen; ein anderes `HOME` oder `CODEX_HOME` isoliert
keinen eigenen CBM-Daemon. Alle Verbraucher müssen denselben kompatiblen Runtime-
und Cachekontext erreichen. Bestehende gemeinsame Runtime nicht beiläufig aktualisieren.

Ein abweichendes Prozess-`HOME` ändert den **abgeleiteten** Default-Cache: mit dem
Team-Codex-`HOME` leitet der Client `<team-home>/.cache/codebase-memory-mcp` ab,
während der laufende Account-Daemon `<owner-home>/.cache/codebase-memory-mcp` nutzt.
Der Start bricht dann für jedes Tool mit
`… the active account daemon uses a different cache directory (active cache <hash>;
requested cache <hash>)` ab (Exit 1), obwohl derselbe Aufruf im Elternkontext
funktioniert. Die beiden Kennungen im Fehlertext sind die SHA256 der jeweiligen Pfade —
damit lässt sich die Wurzel belegen statt raten.

Bind the cache in the Team-Codex configuration, not in per-call environment overrides.
Team-Codex has its own `devteam/codex-home/config.toml`.
Declare the MCP server and canonical account cache there as a static literal:

```toml
[mcp_servers.codebase-memory-mcp]
command = "…/codebase-memory-mcp"
args = []

[mcp_servers.codebase-memory-mcp.env]
CBM_CACHE_DIR = "<Cacheverzeichnis des Account-Daemons>"
```

`env` trägt Literalwerte (genau so schreibt `codex mcp add --env KEY=VALUE` sie); `env_vars`
reicht dagegen nur durch, was der Aufrufer in seiner Umgebung hat, und gehört deshalb **nicht**
in diesen Eintrag: eine deklarierte, aber nirgends gesetzte Variable bleibt leer und erzeugt in
`codex doctor` eine MCP-Warnung, die wie ein Defekt aussieht. Beide Schlüssel sind Geschwister
im selben Eintrag, falls später doch ein Wert aus der Laufumgebung kommen soll; für CBM kommt
heute keiner daher — der Daemon-Socket liegt uid-basiert unter `/tmp/cbm-daemon-<uid>`, nicht
unter `HOME`, und braucht keine Bindung. `CBM_CACHE_DIR` gehört ausschließlich in `env` — die
Vorrangregel bei Doppelung ist nicht belegt, also nicht darauf bauen. Die Konfigurationsdatei
wird über `CODEX_HOME` gefunden, nicht über `HOME`: die Bindung gilt damit **pro Team/Rolle**,
unabhängig davon, unter welchem Prozess-`HOME` der Lauf startet. Alle Teams binden **dieselbe**
Wurzel; es gibt genau einen Account-Daemon, also auch nur eine richtige. Damit braucht kein
Coder-Lauf die Zeile im `env`-Präfix.

**Reihenfolge:** den Eintrag schreiben, **bevor** die Hook-Zustimmung erteilt wird. Die
`[hooks.state.…]`-Vertrauenshashes binden auf den Dateiinhalt; ein nachträglich geändertes
`config.toml` macht sie ungültig und erzwingt eine erneute Bestätigung über `/hooks`.

Fällt die Bindung in einem Lauf trotzdem aus (fremde oder unvollständige Konfiguration), ist
ein prozesslokales `CBM_CACHE_DIR` im `env`-Präfix ein Notbehelf für diesen einen Lauf — keine
Einrichtung und kein Ersatz für den Eintrag. Kein Daemonstopp/-restart, kein zweiter Cache,
keine Cache-/Indexlöschung, keine Rechteänderung, kein globaler `export`. Die Warnung
`daemon.private_dir_group_writable_ancestor mode=0775` erscheint auch in funktionierenden
Kontexten und ist nicht die Ursache.

### 2. Offizielle Clientintegration ausführen

Die vollständige Originalintegration verwenden, **einschließlich der CBM-eigenen
Codex-Unteragenten**. Sie ergänzen die VoltAgent-Helfer innerhalb von Codex und
ändern nicht die Hermes-Teamrollen.

Vor den folgenden Aufrufen müssen die Rollenhomes und das Team-Codex-Home bereits
existieren. `ROLE_HOME`, `CODEX_HOME`, `CODEX_PROCESS_HOME` und `CBM_BIN_DIR` sind
bestätigte absolute Pfade. Unter `CBM_BIN_DIR` liegt die tatsächlich verwendete
Originalbinary `codebase-memory-mcp`.

```sh
# Run for Planner and Coder with their respective ROLE_HOME.
HERMES_HOME="$ROLE_HOME" \
  "$CBM_BIN_DIR/codebase-memory-mcp" install \
  --clients=hermes --skip-binary --dir="$CBM_BIN_DIR"

# Einmal für den getrennten Team-Codex-Kontext ausführen.
HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" \
  "$CBM_BIN_DIR/codebase-memory-mcp" install \
  --clients=codex --skip-binary --dir="$CBM_BIN_DIR"
```

`--clients=…` begrenzt die erkannten Clients; es erzeugt deren Homes nicht.
`--dir` bezeichnet das Binaryverzeichnis, nicht das Profil oder Repository.
Dieselbe Binary aus demselben Verzeichnis aufrufen: `--skip-binary` allein verhindert
nicht jeden Zielbinarykonflikt. Ohne pauschales `--force` arbeiten; vorhandene
angepasste Skill-/Agentdateien vergleichen und Konflikte gezielt klären.

**Direkt danach den kanonischen CBM-Cache in die erzeugte Team-`config.toml` schreiben**
— als Pflichtteil der Einrichtung, nicht als Nachtrag, und **vor** der Hook-Zustimmung
(Begründung in Abschnitt 1):

```toml
[mcp_servers.codebase-memory-mcp]
command = "<CBM_BIN_DIR>/codebase-memory-mcp"
args = []

[mcp_servers.codebase-memory-mcp.env]
CBM_CACHE_DIR = "<Cacheverzeichnis des Account-Daemons>"
```

Ohne diesen Literalwert leitet der Client den Cache aus dem abweichenden Team-`HOME`
ab und verweigert jeden Aufruf. Alle Teams tragen **dieselbe** Wurzel — den einen
accountweiten Cache. Keine `env_vars`-Zeile ergänzen: sie bliebe leer und würde in
`codex doctor` als MCP-Warnung erscheinen.

Die Aufrufform ist am offiziellen CBM-Stand
[v0.12.1, `src/cli/cli.c`](https://github.com/DeusData/codebase-memory-mcp/blob/v0.12.1/src/cli/cli.c)
quellseitig geprüft, kein Versionszwang. Bei anderer Zielversion Optionen und
Zielauflösung vor Ausführung abgleichen.

### 3. Ergebnis, Arbeitskontext und Hooks prüfen

| Kontext | Erwartete Originalintegration |
|---|---|
| Planner and Coder | `skills/codebase-memory/SKILL.md`, MCP-Eintrag in `config.yaml`, Shellhook `hooks.pre_llm_call` |
| Team-Codex | MCP in `config.toml`, Aktivierungszeiger in `AGENTS.md`, `skills/codebase-memory/SKILL.md` |
| Team-Codex-Unteragenten | `agents/codebase-memory-scout.toml`, `agents/codebase-memory.toml` (Verify), `agents/codebase-memory-auditor.toml` |
| Team-Codex-Hooks | `SessionStart` und `SubagentStart`; vorhandene `hooks.json`, sonst native TOML-Ablage |

- Installerausgabe und Dateien zurücklesen; Exitstatus allein genügt nicht.
  Andere MCP-Einträge, Hooks, Anweisungen und die VoltAgent-Helfer müssen erhalten sein.
- Tatsächlichen Session-/MCP-CWD auf das jeweilige Repository binden. Der Installer
  legt mit Profilhome und Binarypfad noch keinen Analyse-Root fest.
- Read back the `CBM_CACHE_DIR` literal in the team TOML `[mcp_servers.codebase-memory-mcp.env]` for MCP and hook configuration.
  Do not rely on caller environment inheritance. Bind Hermes MCP `env` too if its derived default differs from the shared account cache.
  Read back actual native connection/configuration status in the bound context through the established non-indexing interface.
  Do not create projects or run index/query/update experiments.
- Erforderliche Zielanpassungen über die unterstützte native Konfiguration vornehmen;
  siehe [Hermes MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
  und [Shellhooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#shell-hooks).
  Original-Hookkommandos beibehalten; keine eigenen Indexierungshooks ergänzen.
- Obtain the disclosed native hook approval in the selected target context; Codex uses `/hooks`.
  Read back approval and configuration state after the final cache/configuration write.
  Do not start a worker to test hook behavior; definitions and approval do not prove execution.

### 4. Later project operation

Deliver the complete original `codebase-memory` skill and its references.
Later authorized project tasks use its native `list_projects`, `index_repository`, `index_status`, query and watcher/update paths.
Do not require indexing, graph relationships, incremental updates or watcher experiments to complete setup.
Do not add repeated reindexing on each call, message, commit, or review handoff.

<a id="funktionspruefung"></a>
## Setup output boundary

Read back the chosen integration, complete file set, native discovery, runtime/MCP command,
CWD/roots, cache literal, hooks and approval state.
A readback proves configuration/delivery, not graph accuracy or live hook behavior.
Report an actual failed binding precisely; do not silently switch alternatives.

## Wiederaufnahme, Updates und Rückweg

Bei Wiederaufnahme zuerst den protokollierten Zielzustand abgleichen. Werkzeugupdates
von normalen Indexaktualisierungen unterscheiden; neue Versionen samt Auswirkungen
auf gemeinsame Runtime, Skilldateien und Hookzustimmung prüfen. Für einen Rückbau
nur die dokumentierten eigenen Einträge gezielt zurücknehmen und gesicherte Werte
wiederherstellen. Gemeinsame Binaries, fremde Konfiguration und Indizes erhalten;
Datenlöschung separat freigeben.
