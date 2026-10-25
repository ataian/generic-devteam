# Codeanalyse einrichten

Richte die im [Setup](setup.md) bestätigte Auswahl **Graphify oder CBM** für
Planner, Coder, Reviewer und Team-Codex ein. Bezugsquellen und Lizenzen stehen in
[upstream-sources.md](upstream-sources.md#codeanalyse-genau-eine-alternative).
Diese Anleitung wird beim beauftragten Zielsetup ausgeführt, nicht beim Bearbeiten
des Makerpakets.

## Gemeinsame Vorbereitung

1. Vorhandene Runtime, Version, Skills und Integrationen prüfen; passenden Bestand
   wiederverwenden. Bei neuem Bezug einen konkreten offiziellen Release-/Quellstand
   wählen, Integrität prüfen und im privaten Setup-Protokoll festhalten.
2. Absolute Hermes-Rollenhomes sowie `CODEX_HOME` und `CODEX_PROCESS_HOME` aus dem
   [Team-Codex-Rezept](integrations.md#team-codex) übernehmen. Symlinks und vorhandene
   Zieldateien prüfen; betroffene Konfiguration vor Änderungen sichern.
3. Repositoryroots, erlaubten Analyseumfang und Index-/Ausgabeorte festlegen.
   Ein Workspace mit mehreren Repositories ist nicht automatisch ein gemeinsamer
   Index. Geheimnisse und fachliche Daten gehören nicht in den Analyseumfang.
4. Installations- und Aktivierungsumfang bestätigen. Zunächst einen separaten
   Testworkspace verwenden; Session-CWD und gegebenenfalls MCP-CWD vor Aktivierung
   darauf binden. Produktrepositories erst beim späteren Projektauftrag aktivieren.

Die folgenden Pfade und Optionen beim Zielsetup mit der gewählten Version abgleichen.
Vorhandene Projektregeln, fremde Profile und persönliche Codex-Konfiguration bleiben
außerhalb der Team-Einrichtung. Konflikte mit bestehenden Dateien vor dem Schreiben
klären; bei Teilfehlern den tatsächlichen Zustand lesen statt blind erneut installieren.

<a id="graphify"></a>
## Graphify

### 1. Runtime und vollständige Skills bereitstellen

Passende vorhandene Graphify-Runtime und ihren Python-Interpreter verwenden. Fehlt
sie, das offizielle Paket `graphifyy` nach Freigabe installieren; dessen Manifest
bestimmt Python-Version und Abhängigkeiten. Beispiel mit vorhandenem `uv` und der
zuvor geprüften Version in `GRAPHIFY_VERSION`:

```sh
uv tool install "graphifyy==$GRAPHIFY_VERSION"
```

Runtime und Skilldateien müssen zusammenpassen. Aus demselben Bezugsstand die
vollständigen Originalbäume nach folgender Zuordnung kopieren:

| Verbraucher | Originalhauptdatei → `SKILL.md` | Referenzen → `references/` | Zielverzeichnis |
|---|---|---|---|
| Jede Hermes-Rolle | `graphify/skill-claw.md` | `graphify/skills/claw/references/` vollständig | `<ROLE_HOME>/skills/graphify/` |
| Team-Codex | `graphify/skill-codex.md` | `graphify/skills/codex/references/` vollständig | `<CODEX_PROCESS_HOME>/.agents/skills/graphify/` |

Die zum Paket gehörenden `LICENSE`, `LICENSE-MIT` und `NOTICE` beilegen. Ganze
Dateimengen und Inhalte mit der Quelle vergleichen; keine eigene Skillfassung bauen.
Die Hermes-Zuordnung zur claw-Variante ergibt sich aus Graphifys `graphify/install.py`.
Dessen allgemeiner Installer kann persönliche Standardhomes und Projektanweisungen
beschreiben; für diese profilbezogene Skillablage deshalb die expliziten Ziele nutzen.

### 2. Aktivieren und verwenden

- In jeder Hermes-Rolle den installierten Skill `graphify` laden, in Team-Codex
  `$graphify` verwenden. Auch nach Resume muss der richtige Skillbaum aufgelöst werden.
- Die vorhandenen Rollen-/Skillanweisungen nutzen; keine zusätzliche Modellpolicy
  oder parallele Rollenregel für die Codeanalyse anlegen.
- Aufbau als Auftrag an den geladenen Originalskill: `/graphify <CORPUS>`.
  Das ist eine Skillanweisung, kein gleichnamiger Shellbefehl.
- Danach gemäß installierter `references/query.md` abfragen, beispielsweise
  `graphify query "<vorhandenes Symbol oder Aufrufbeziehung>"`.
- Änderungen über `/graphify <CORPUS> --update` und die installierte
  `references/update.md` nachführen. Vorhandene aktuelle Ergebnisse wiederverwenden;
  erneutes Clustering allein ersetzt keine Aktualisierung des Quellbestands.

Ausgabe-CWD, Corpus und Interpreter müssen zusammengehören. Bei mehreren Repositories
getrennte Graphausgaben führen; Zusammenführung und erneute Aktualisierung gemäß
`references/github-and-merge.md`. Watcher nur bei vereinbartem Bedarf nach
`references/add-watch.md` einrichten. Für den normalen Skill-/CLI-Weg ist kein
zusätzlicher MCP-Dienst erforderlich. Semantische Dokument-/Bildanalyse kann
Modellverarbeitung auslösen; deren Datenumfang und Anbieter müssen freigegeben sein.

<a id="codebase-memory"></a>
## Codebase-memory-mcp (CBM)

### 1. Gemeinsame Runtime bereitstellen

Eine geeignete vorhandene Originalbinary wiederverwenden. Fehlt sie, das passende
offizielle Linux-Releasearchiv für Architektur und System beziehen, Prüfsumme und
verfügbare Herkunftsnachweise prüfen und nach Freigabe die Binary im vereinbarten
Benutzer-Binverzeichnis bereitstellen. `LICENSE` und `THIRD_PARTY_NOTICES.md` aus
dem Releasearchiv aufbewahren. Der Runtimebezug und die folgende Clientkonfiguration
sind getrennte Schritte; ein ungeprüfter Shellinstaller ist dafür nicht nötig.

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

**Dauerhaft richtig ist die Bindung in der Team-Codex-Konfiguration, nicht im Aufruf.**
Jede Rolle hat ihr eigenes `devteam/codex-home/config.toml`; dort wird der MCP-Server
deklariert, und dort gehört der kanonische Cache **statisch** hinein — als Literal, nicht
als Durchreichen aus der Prozessumgebung:

```toml
[mcp_servers.codebase-memory-mcp]
command = "…/codebase-memory-mcp"
args = []
env_vars = ["CBM_RUNTIME_DIR"]

[mcp_servers.codebase-memory-mcp.env]
CBM_CACHE_DIR = "<Cacheverzeichnis des Account-Daemons>"
```

`env` trägt Literalwerte (genau so schreibt `codex mcp add --env KEY=VALUE` sie), `env_vars`
reicht nur durch, was der Aufrufer in seiner Umgebung hat; beide sind Geschwister im selben
Eintrag und stehen nebeneinander. `CBM_CACHE_DIR` gehört nur in `env` und nicht zusätzlich in
`env_vars` — die Vorrangregel bei Doppelung ist nicht belegt, also nicht darauf bauen. Die
Konfigurationsdatei wird über `CODEX_HOME` gefunden, nicht über `HOME`: die Bindung gilt damit
**pro Team/Rolle**, unabhängig davon, unter welchem Prozess-`HOME` der Lauf startet. Alle Teams
binden **dieselbe** Wurzel; es gibt genau einen Account-Daemon, also auch nur eine richtige.
Damit braucht kein Coder-Lauf die Zeile im `env`-Präfix.

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
# Je Hermes-Rolle mit deren ROLE_HOME ausführen.
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

Die Aufrufform ist am offiziellen CBM-Stand
[v0.12.1, `src/cli/cli.c`](https://github.com/DeusData/codebase-memory-mcp/blob/v0.12.1/src/cli/cli.c)
quellseitig geprüft, kein Versionszwang. Bei anderer Zielversion Optionen und
Zielauflösung vor Ausführung abgleichen.

### 3. Ergebnis, Arbeitskontext und Hooks prüfen

| Kontext | Erwartete Originalintegration |
|---|---|
| Jede Hermes-Rolle | `skills/codebase-memory/SKILL.md`, MCP-Eintrag in `config.yaml`, Shellhook `hooks.pre_llm_call` |
| Team-Codex | MCP in `config.toml`, Aktivierungszeiger in `AGENTS.md`, `skills/codebase-memory/SKILL.md` |
| Team-Codex-Unteragenten | `agents/codebase-memory-scout.toml`, `agents/codebase-memory.toml` (Verify), `agents/codebase-memory-auditor.toml` |
| Team-Codex-Hooks | `SessionStart` und `SubagentStart`; vorhandene `hooks.json`, sonst native TOML-Ablage |

- Installerausgabe und Dateien zurücklesen; Exitstatus allein genügt nicht.
  Andere MCP-Einträge, Hooks, Anweisungen und die VoltAgent-Helfer müssen erhalten sein.
- Tatsächlichen Session-/MCP-CWD auf das jeweilige Repository binden. Der Installer
  legt mit Profilhome und Binarypfad noch keinen Analyse-Root fest.
- `CBM_CACHE_DIR` ist ein Pflichtprüfpunkt der Team-Codex-Konfiguration: er muss als
  Literal in `[mcp_servers.….env]` stehen (Abschnitt 1), nicht nur in `env_vars`
  durchgereicht werden. Fehlt er, leitet der Client ihn aus dem abweichenden Team-`HOME`
  ab und verweigert den Start. Bei MCP **und** Hooks prüfen; Hermes braucht bei
  abweichenden Defaults eine passende MCP-`env`-Bindung. Den tatsächlichen Client
  prüfen, nicht nur die Umgebung des Installationsbefehls: belegt ist die Bindung erst,
  wenn `list_projects` und `index_status` **im echten Client-Kontext** selbst Exit 0
  liefern — ein erfolgreicher Lauf im Elternkontext beweist sie nicht.
- Erforderliche Zielanpassungen über die unterstützte native Konfiguration vornehmen;
  siehe [Hermes MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
  und [Shellhooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#shell-hooks).
  Original-Hookkommandos beibehalten; keine eigenen Indexierungshooks ergänzen.
- Native Hookzustimmung im jeweiligen Zielkontext einholen; bei Codex über `/hooks`.
  Anschließend tatsächliche Kontextaufnahme prüfen. Installierte Definitionen sind
  noch kein ausgeführter Hook.

### 4. Index aufbauen und aktuell halten

Den installierten Originalskill `codebase-memory` in Hermes bzw. `$codebase-memory`
in Team-Codex laden. Über `list_projects` die tatsächliche Rootzuordnung ermitteln;
fehlenden Index mit `index_repository` für den freigegebenen Repositoryroot aufbauen.
Asynchrone Arbeit begrenzt bis zum Endstatus verfolgen. Mit `index_status` Bereitschaft,
Root, Indexstand und Watcherzustand prüfen, dann mit dem aktuellen Toolschema abfragen.

Der native Watcher führt Änderungen für registrierte aktive MCP-Projektsitzungen
nach. Einen aktuellen Index weiterverwenden; keine zusätzlichen Reindex-Aufträge
pro Codex-Aufruf, Nachricht, Commit oder Reviewübergabe einbauen. Nach Änderungen
bzw. Branchwechseln Aktualität prüfen und nur bei tatsächlichem Bedarf den nativen
Updateweg nutzen. Bei mehreren Repositories jede Root separat zuordnen und ihre
Beobachtung prüfen. Ein einmaliger Indexlauf beweist keinen dauerhaft aktiven Watcher.

<a id="funktionspruefung"></a>
## Kurze Funktionsprüfung im Zielsetup

Nach der Setup-Aktivierungsfreigabe ein kleines Repository im separaten
Testworkspace verwenden. Beispielinhalt für `probe.py`:

```python
def probe_leaf():
    return 1


def probe_entry():
    return probe_leaf()
```

1. In allen drei Hermes-Rollen und im echten Team-Codex-Kontext den ausgewählten
   Originalskill laden und die jeweilige Runtime bzw. MCP-Verbindung nachweisen.
   Bei CBM zusätzlich Hooks und Discovery der CBM-Unteragenten prüfen.
2. Testrepository indexieren und die Beziehung `probe_entry` → `probe_leaf`
   tatsächlich abfragen, nicht nur beide Symbolnamen suchen.
3. Eine Funktion `probe_added` ergänzen und von `probe_entry` aufrufen lassen.
   Graphify nativ aktualisieren bzw. bei CBM die automatische Nachführung prüfen;
   anschließend auch diese neue Aufrufbeziehung abfragen.
4. Root, geprüften Dateistand, Ergebnis und etwaige Coverage-Lücken im Setup-Protokoll
   festhalten. Fremde Konfigurationen mit dem Vorherzustand vergleichen.

Fehlende Graphbeziehungen beweisen keine fehlenden Abhängigkeiten. Wichtige Befunde
am Quelltext prüfen. Bei Fehlern die konkrete betroffene Fähigkeit offenlassen;
keinen stillen Wechsel zur anderen Analysealternative vornehmen.

## Wiederaufnahme, Updates und Rückweg

Bei Wiederaufnahme zuerst den protokollierten Zielzustand abgleichen. Werkzeugupdates
von normalen Indexaktualisierungen unterscheiden; neue Versionen samt Auswirkungen
auf gemeinsame Runtime, Skilldateien und Hookzustimmung prüfen. Für einen Rückbau
nur die dokumentierten eigenen Einträge gezielt zurücknehmen und gesicherte Werte
wiederherstellen. Gemeinsame Binaries, fremde Konfiguration und Indizes erhalten;
Datenlöschung separat freigeben.
