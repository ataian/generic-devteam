# Codeanalyse: zwei Originalwege, eine Auswahl

Diese Anleitung ist ein statisches Einrichtungsrezept, keine Installation oder
Funktionsabnahme. [Setup](setup.md) bestimmt Freigaben und Reihenfolge,
[Manifest](../../manifest.json) die Rollenmatrix und geprüften Dateimengen,
[Herkunft](upstream-sources.md) die Bezugsquellen. Fremdassets werden beim späteren
Zielsetup vollständig aus der gewählten Originalrevision bezogen, nicht aus
privaten Profilen. Dieses Makerpaket enthält Rezepte, keine Graphify-/CBM-Runtime.

## Gemeinsamer Vertrag

Bei einem Setup genau einen gewählten Analyseweg einrichten; bei Fehlern anhalten, nicht still wechseln oder beide installieren.
Passenden Bestand wiederverwenden; fehlenden Runtimebedarf aus dem Originalmanifest ableiten und gesondert genehmigen lassen.
Erster Index-/Query-Nachweis ausschließlich im später genehmigten separaten Testworkspace; Produktanalyse erst nach Projektauftrag.

1. Auswahl `graphify` oder `codebase-memory` im privaten Setuprecord festhalten.
   Für **Planner, Coder, Reviewer und Team-Codex** denselben gewählten Weg
   bereitstellen; Binaryverfügbarkeit ist nicht Skill-/MCP-Verfügbarkeit.
2. Version/Releasecommit, Ursprung, Quell- und Zieldateimenge samt SHA-256,
   Rechtshinweise, tatsächliche Runtime/Binary/Interpreter und Terminalbackend
   erfassen. Am Ziel geeignete aktuelle Version neu auflösen; die folgenden
   Rechercheanker vom 18.10.2026 sind keine dauerhafte Versions-Allowlist.
   Produktstack aus AGENTS/Manifesten/Lockfiles, keine universellen DevHours-Pins.
3. Absolute Rollenhomes aus nativer Profilauflösung verwenden. Team-Codex bindet
   ausschließlich im eigenen Prozess `HOME=CODEX_PROCESS_HOME` und `CODEX_HOME`
   gemäß [Team-Codex](integrations.md#team-codex). Keine globale Env-Änderung.
   Symlinks, fremde Dateien und gleiche Skillnamen vor Schreibzugriff prüfen.
4. Skills und Lizenzen vollständig kopieren, außerhalb aktiver Discovery
   vorbereiten; nur bestätigte eigene Ziele beschreiben. Vorherige eigene Fassung
   außerhalb Discovery sichern; keine Quellinstallation ändern. Quelle→Zielmenge
   und Bytes zurücklesen, keine zweite gleichnamige Skillkopie erzeugen.
5. Analyseauswahl, Ladeauftrag und Nachführung in den **Codeanalyseabschnitt** der
   lokal installierten [Modell-/Auftragspolicy](../templates/model-policy.md)
   schreiben. Alle Rollen erreichen diese über `MODEL_POLICY_REF` des installierten
   Workflows; der Coder trägt die gewählte Regel in jeden Codexauftrag. Keine
   Abhängigkeit des Alltags vom Makerbaum und keine neue Rolle/Bridge.
6. Root, CWD, Corpusgrenzen/Ausschlüsse und Ausgabe-/Cacheort pro Repository
   festlegen. Der Teamworkspace ist nicht automatisch ein Repo oder ein Index.
   Für mehrere Repos eigene Root-/Commitzuordnung führen. Analyseartefakte und
   ggf. semantische Verarbeitung benötigen einen freigegebenen Corpus.

Vor relevanten Queries Corpus und Arbeitsbaum gegen den letzten erfolgreichen Indexstand prüfen; bei Änderung zuerst den Original-Updateweg ausführen.
Stale/fehlende/teilweise Indizes offenlegen. Eine Original-Suche mit anschließendem
gezieltem Quellenlesen ist kein heimlicher Wechsel zur anderen Analyseinstallation.
Discovery, Aktivierung, Indexstatus, Query und Update getrennt nachweisen.

Vor MCP-Aufnahme, Hook-Consent oder Skill-Aufbau den tatsächlichen Session-/Tool-CWD und die MCP-Wurzel auf den freigegebenen Testworkspace binden; nicht auf das Produktprojekt.
Das gilt auch bei bereits hot-admittierten Rollen: Aktivierungs-/Autoload-/
Watcherwirkungen nicht durch voreilige Konfiguration auslösen. Bis zur Freigabe
und wirksamen Testbindung nur Assets/Rezept außerhalb aktiver Integration
vorbereiten. Den Team-Startworkspace nicht dauerhaft umdefinieren: Testaufrufe
explizit im Testroot, MCP-cwd für die Abnahme ebenfalls dort binden. Wenn der
native Zielweg diese Trennung nicht gewährleisten kann, vor Aufnahme anhalten.
Produktroots erst beim späteren Projektauftrag ausdrücklich registrieren/aktivieren.

<a id="graphify"></a>
## Graphify

### Originalstand und Runtime

[Originalmanifest](https://github.com/Graphify-Labs/graphify/blob/86c57be8204673c2a1b9849a3292a7dd3ab373d8/pyproject.toml):
`graphifyy` **0.9.92**, Python **>=3.10**, Revision
`86c57be8204673c2a1b9849a3292a7dd3ab373d8`. Der normale CLI-/Skillweg braucht
kein MCP-Extra. Manifestabhängigkeiten durch den offiziellen Paketresolver
auflösen, nicht in eine zweite eigene Abhängigkeitsliste übersetzen. Beispielsweise
nach Bestandsprüfung und Bezugsfreigabe `uv tool install graphifyy`; im Setup
aufgelöste Paketversion/Integrität festhalten. Kein automatisches Upgrade eines
passenden Bestands. Die Skillvariante muss zur verwendeten Runtime passen.

Strukturelle AST-Codeanalyse ist modellfrei; semantische Dokument-/Bildarbeit kann
der aktive Hostagent übernehmen. Kein zusätzlicher Modellanbieter erforderlich.
Vorhandene optionale Backend-Env kann den Originalskill zu externer Verarbeitung
lenken: Zielpolicy und Corpusfreigabe prüfen, keine Secrets ausgeben und keinen
neuen Providerzwang erzeugen. Extras wie `watch` (`watchdog`) oder `mcp`
(`mcp>=1,<3`, `starlette>=1.3.1,<2` an diesem Stand) nur bei bewusst gewähltem
Zusatzbetrieb. Kein automatisch angelegter Watcher oder zusätzlicher Dienst.

### Vollständige Originaldateimengen und Ziele

[Originalmapping](https://github.com/Graphify-Labs/graphify/blob/86c57be8204673c2a1b9849a3292a7dd3ab373d8/graphify/install.py):
`PLATFORMS` verwendet für Hermes ausdrücklich die **claw**-Variante.

| Zielharness | Originalhauptdatei → `SKILL.md` | Vollständiger Referenzunterbaum | Aufgelöstes Ziel |
|---|---|---|---|
| Hermes, jede der drei Rollen | `graphify/skill-claw.md` | `graphify/skills/claw/references/` | `<ROLE_HOME>/skills/graphify/` |
| Team-Codex | `graphify/skill-codex.md` | `graphify/skills/codex/references/` | `<CODEX_PROCESS_HOME>/.agents/skills/graphify/` |

**Jeder** Referenzbaum enthält an der geprüften Revision genau diese acht Dateien;
alle müssen unter `references/` desselben Zielskills liegen:

- `add-watch.md`
- `exports.md`
- `extraction-spec.md`
- `github-and-merge.md`
- `hooks.md`
- `query.md`
- `transcribe.md`
- `update.md`

Damit neun Skilldateien je Variante; im Manifest stehen beide vollständigen
Quelle→Zielabbildungen und frisch aus Originalbytes berechnete Hashes. Bei einem
neueren Bezugsstand rekursive Dateimenge neu erheben, nicht auf acht beschneiden.
Zusätzlich Root-`LICENSE` (Apache-2.0), `LICENSE-MIT` und `NOTICE` unverändert je
übernommenem Baum beilegen. NOTICE erhält Safi Shamsi und Graphify contributors
sowie die MIT-Vorgeschichte. Diese Texte nicht unter die eigene MIT-Lizenz stellen.

**Nicht `graphify install` pauschal verwenden:** Der Linux-Hermesresolver nutzt
`Path.home()/.hermes/skills`, nicht zuverlässig `HERMES_HOME`; Codexmapping nutzt
`.codex/skills`, nicht ausschließlich `CODEX_HOME`. Explizite obige Zielablage
verhindert falsche persönliche/Profile-Roots. `_agents_install`/Projektinstaller
können außerdem `AGENTS.md` und `.codex/hooks.json` ändern. Diese Wege sind für
unseren Skill-/CLIweg unnötig; Projekt-AGENTS und vorhandene Hooks unverändert lassen.

### Aktivierung, Nachführung und mehrere Repos

In jedem neuen Analyseauftrag und nach Resume den installierten Originalskill laden: Hermes `skill_view(name="graphify")`, Team-Codex ausdrücklich `$graphify`.
Je Rolle Hauptskill und benötigte Referenzen aus genau dem bestätigten Zielbaum
auflösen; native Katalog-/Ladenachweise später im echten Worker gewinnen. Die
Auftragspolicy trägt diese Ladepflicht dauerhaft, nicht nur der Setupdialog.
Hermes-Autoload ist möglich, ersetzt aber nicht die Prüfung effektiver Aufnahme.

- Aufbau über den geladenen Originalskill `/graphify <CORPUS>`; vorhandener Graph
  unter `graphify-out/graph.json` → `references/query.md`, Vokabularauswahl und
  `graphify query "<wirklich vorhandene Symbolbegriffe>"`. Quellenstellen zitieren;
  leere Treffer oder Coverageprobleme nicht als vollständigen Negativbeweis nutzen.
- Änderungen → `/graphify <CORPUS> --update` mit vollständig geladener
  `references/update.md`. Kein `--cluster-only` als Ersatz für Neu-Extraktion.
  Gelöschte Dateien, semantische Änderungen und Fehler der Shrink-/Leergraphguards
  beachten; keine stillen `--force`-Umgehungen. Output-CWD und `.graphify_root`
  sowie Interpreterzuordnung festhalten, nicht in einem anderen CWD weitermachen.
- Ein ausdrücklich genehmigter Watcher folgt `references/add-watch.md`. Er
  aktualisiert Code strukturell; Dokumente/Bilder erzeugen `needs_update` und
  benötigen semantisches Update. Skillkopie beweist weder laufenden Watcher noch
  aktuelle Daten. Kein Systemdienst als Makernebenwirkung.
- Mehrere Repos gemäß `references/github-and-merge.md`: getrennte Ausgaben pro
  Repo, danach `graphify merge-graphs <graph1> <graph2> --out graphify-out/graph.json`
  am vereinbarten kanonischen Queryort. Bei lokalen Teilbäumen nutzt die
  Originalreferenz `graphify extract <subdir>` für getrennte Ausgabewurzeln;
  wiederholte Skillpipeline im gleichen CWD würde sonst Ausgaben überschreiben.
  Erst Teilgraphen aktualisieren, dann erneut mergen; Herkunft je Repo erhalten.
  Keine Klone/Netzwerkzugriffe nur aufgrund eines vorhandenen Merge-Rezepts.

## Graphify-Funktionsprüfung (später)

Im separaten genehmigten Testworkspace das unten beschriebene synthetische Repo
anlegen. Hauptskill, Query- und Updatereferenz im echten jeweiligen Harness laden.
Aufbau abschließen, `graph.json`/Report und Corpuszuordnung prüfen, `t5_entry` und
`t5_leaf` mit ihrer tatsächlichen Aufrufrelation abfragen. Danach Änderung mit
`t5_added`, Originalupdate und neue Relationsquery. Bei Multi-Repo-Nutzung zusätzlich
Teilgraph-/Mergezuordnung prüfen. Die gespeicherte Revision des Prüfprotokolls
samt indexierter Dateihashes und relevantem Arbeitsbaum muss zum Graphlauf passen;
ein gerade gelesenes Git-HEAD allein ist kein Beleg des Indexstands. Keine native
Commitmetadaten im Graphformat erfinden, wenn der konkrete Stand sie nicht liefert.

<a id="codebase-memory"></a>
## Codebase-memory-mcp (CBM)

### Release, Linuxarchitektur und gemeinsamer Runtimekontext

[Release v0.12.1](https://github.com/DeusData/codebase-memory-mcp/releases/tag/v0.12.1)
zeigt auf `a7158ac2f48ca646b4527341b76f930f2aeff87e`; separat gelesener HEAD
`354ccecbe612a9fdb624396a6738fa87f2617434` hat bytegleiches `src/cli/cli.c`.
Am Ziel geeignete Releaseidentität neu prüfen, nicht HEAD und Release gleichsetzen.

Offizielle Linuxarchive: `codebase-memory-mcp-linux-amd64.tar.gz`,
`codebase-memory-mcp-linux-arm64.tar.gz` und jeweils die `-portable.tar.gz`-Variante.
Zielarchitektur/ABI/CPUanforderungen gegen Release/Bestand prüfen (`x86_64` → `amd64`,
`aarch64` → `arm64`), nicht die Autorenmaschine zur Vorgabe machen. Passende
Originalbinary wiederverwenden. Fehlt sie, Download, Prüfsummen-/Signaturprüfung
(`checksums.txt`, zugehörige `.bundle`-Nachweise) und Runtimeaufnahme gesondert
genehmigen. Kein ungeprüftes `curl | sh`, kein UI-Pack erforderlich.

Der [Releasepackager](https://github.com/DeusData/codebase-memory-mcp/blob/a7158ac2f48ca646b4527341b76f930f2aeff87e/scripts/package-release.sh)
verpackt für Linux genau `codebase-memory-mcp`, `LICENSE`, `install.sh`,
`THIRD_PARTY_NOTICES.md`. Lizenz ist MIT; Notices bündeln zusätzliche
Fremdlizenzen. `THIRD_PARTY_NOTICES.md` wird beim Releasebau erzeugt, liegt **nicht**
als gleichnamige Rootdatei im Gitbaum: Generator `scripts/gen-third-party-notices.sh`
liest `THIRD_PARTY.md`, Grammarmanifest und vendorte Lizenz-/Noticetexte. Deshalb
vollständige Notices aus dem verifizierten Releasearchiv erhalten, nicht durch
Root-LICENSE ersetzen. Archive wurden beim Paketbau nicht heruntergeladen/geprüft;
Dateimenge ist Packagerableitung, keine behauptete Archivprüfung. `install.sh`
nicht automatisch ausführen. Original-`--skip-config` überspringt nur die
Agentkonfiguration, nicht Binary-/PATH-/Aktivierungswirkungen.

CBM nutzt einen accountweit koordinierten Originaldaemon. Buildkompatibilität,
gemeinsamen Cache und Rendezvous (`CBM_CACHE_DIR`, `CBM_RUNTIME_DIR`) vor Aktivierung
prüfen. Ein anderer HOME isoliert diesen Daemon nicht automatisch. Keine bestehende
gemeinsame Runtime eigenmächtig ersetzen, drainen oder stoppen. Strukturqueries
brauchen keinen Hosted-Modellanbieter; kein neuer Wrapper oder Ersatzdienst.

### Vollständige Integrationsmenge je Harness

Autorität ist [src/cli/cli.c](https://github.com/DeusData/codebase-memory-mcp/blob/a7158ac2f48ca646b4527341b76f930f2aeff87e/src/cli/cli.c),
nicht eine nachgeschriebene README. `cbm_codex_config_dir` respektiert CODEX_HOME,
`cbm_hermes_home_dir_for` HERMES_HOME. `install_agent_skill` schreibt genau
`skill_content` nach `skills/codebase-memory/SKILL.md`; **keine** Referenzen oder
separaten Hookskripte gehören zu diesem Skill. Alle Harnesses erhalten dieselben
Originalskillbytes. Tiernamen Scout/Verify/Auditor im Skill bleiben unverändert:
sie sind Evidenzstufen, keine Anweisung, zusätzliche Agentdateien zu installieren.

| Kontext | Originalziel / selektiver Umgang |
|---|---|
| Jede Hermes-Rolle | `<ROLE_HOME>/skills/codebase-memory/SKILL.md`; `<ROLE_HOME>/config.yaml` enthält MCP plus `hooks.pre_llm_call` |
| Team-Codex Skill | `<CODEX_HOME>/skills/codebase-memory/SKILL.md`, aktuell nativer Kompatibilitätspfad; nicht zusätzlich unter Prozess-HOME duplizieren |
| Team-Codex Aktivierung | `<CODEX_HOME>/AGENTS.md`: Originalpointer gezielt ergänzen, übrigen Inhalt erhalten; **kein** Projekt-AGENTS |
| Team-Codex MCP | `<CODEX_HOME>/config.toml`: eigene native MCP-Tabelle gezielt mergen |
| Team-Codex Hooks | Wenn `hooks.json` vorhanden: dort beide Originalhooks; sonst im `config.toml`. Keine doppelte CBM-Hookablage |
| Nicht übernehmen | `agents/codebase-memory-scout.toml`, `agents/codebase-memory.toml` (Verify), `agents/codebase-memory-auditor.toml` |

Die drei CBM-Agentdateien nicht übernehmen; die sechs bestätigten VoltAgent-Originalagenten bleiben die einzige zusätzliche Helfermenge.
`install_cli_agent_configs` ruft zwingend `install_tiered_agent_profiles` auf;
kein geprüfter `--no-agents`-Schalter. Keine nachträgliche Löschung fremder Agenten.
Bei schon vorhandenen Helfern Konflikt klären, keine automatische Bereinigung.
Original-LICENSE und Release-THIRD_PARTY_NOTICES separat zur Herkunft aufbewahren
und bei Übernahme beilegen. Keine selbst umgeschriebenen Skill-/Hookersatztexte.

### Native MCP-/Hookkonfiguration und Aktivierung

Nach Originaloutput-Gate unten die Originalwerte über unterstützte Zielkonfiguration
mergen. Für Hermes profilbezogen `hermes -p "$PROFILE" config set/get` gemäß
[Hermes-MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
und [Shellhooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#shell-hooks)
verwenden, nicht ganze YAML-Dateien ersetzen. Bestehende Hooklisten zuerst lesen,
nur eigenen Eintrag ergänzen. Inhaltliche Form, keine bytegleiche Installerdatei:

```yaml
mcp_servers:
  codebase-memory-mcp:
    command: "<absoluter Originalbinarypfad>"
    args: []
    cwd: "<bestätigte Workspacewurzel>"
    env:
      CBM_CACHE_DIR: "<gemeinsamer bestätigter Cache>"
      CBM_RUNTIME_DIR: "<gemeinsamer bestätigter Rendezvousbereich>"
hooks:
  pre_llm_call:
    - id: "codebase-memory-mcp"
      type: "command"
      command: "'<absoluter Originalbinarypfad>' hook-augment --dialect hermes"
```

`cwd`/`env` sind bewusste native Zielbindung, nicht behaupteter Originalinstalleroutput.
Env nur setzen, wenn diese Werte im tatsächlichen gemeinsamen Runtimekontext
verwendet werden; sonst konsistente native Defaults nachweisen. Auch Hookprozess
und MCP müssen denselben Kontext treffen. Pfade shell-/YAML-sicher kodieren,
insbesondere Apostrophe nicht per naiver Stringeinfügung. `id`/`type` dienen dem
CBM-Merger; Hermes nutzt den Command. Kein Gateway-`HOOK.yaml`, Plugin oder separates
Hookskript. Native Freigabe pro Ereignis/Command und echte Kontextinjektion prüfen.
Je Rolle Originalskill ausdrücklich laden (`skill_view(name="codebase-memory")`).

Codex nutzt den dokumentierten nativen
[TOML-MCP-Weg](https://developers.openai.com/codex/mcp.md), mit beiden Teamhomes:

```toml
[mcp_servers.codebase-memory-mcp]
command = "<absoluter Originalbinarypfad>"
args = []
env_vars = ["CBM_CACHE_DIR", "CBM_RUNTIME_DIR"]
```

Kein `serve`-Argument. `env_vars` reicht vorhandene Variablen weiter, erzeugt keine
Werte; reale Workerumgebung prüfen. Den tatsächlichen Session-/MCP-CWD gegen den
Repo-Root prüfen, bei Bedarf dokumentiertes `cwd` bewusst binden. Ein fester
Workspace darf andere Repos nicht still unter dem falschen Root analysieren.
Aktivierungszeile (`codex_instructions_content`, abschließendes LF) lautet:

```text
For structural codebase exploration, use the installed `codebase-memory` skill.
```

Zusätzlich im jeweiligen Codexauftrag `$codebase-memory` laden lassen. Die
[Codex-Hooks](https://developers.openai.com/codex/hooks.md) verwenden folgende
Originalsemantik, in **einer** Repräsentation pro Layer:

```toml
[[hooks.SessionStart]]
matcher = "startup|resume|clear|compact"
[[hooks.SessionStart.hooks]]
type = "command"
command = "<shell-quotierter absoluter Binarypfad> hook-augment"
command_windows = "& <PowerShell-quotierter absoluter Binarypfad> hook-augment"
timeout = 5

[[hooks.SubagentStart]]
matcher = "*"
[[hooks.SubagentStart.hooks]]
type = "command"
command = "<shell-quotierter absoluter Binarypfad> hook-augment"
command_windows = "& <PowerShell-quotierter absoluter Binarypfad> hook-augment"
timeout = 5
```

Quelle: `cbm_build_augment_command`, `cbm_build_augment_command_windows`,
`src/cli/config_toml_edit.c` und `cbm_upsert_paired_lifecycle_hooks_json`. Im
JSON-Fall dieselben Ereignisse/Matcher und `hooks`-Listen verwenden. Originale
Managed-Marker (`# >>> codebase-memory-mcp SessionStart >>>` / Endmarker; MCP
entsprechend) erhalten. Andere Hook-/MCP-Einträge bewahren; eigene alte doppelte
CBM-Definition nur nach Eigentumsprüfung entfernen. `command_windows` nicht still
weglassen. `/hooks` muss **exakte** Definition freigeben, Änderungen brauchen
erneuten Trust. Kein Trustbypass. Originalmatcher umfasst nicht `fork`; keine
Forkabdeckung versprechen. Ein erfolgreicher MCP-Call beweist keinen Hooklauf.

<a id="g2"></a>
### G2: statischer Befund und ausführbares späteres Vergleichsverfahren

G2 ist ungelöst; A01-CBM bleibt offen, bis echte Originalausgabe, selektiver Transfer und Bytevergleich im genehmigten Prüfbereich vorliegen.

Die Option `install --clients=codex --skip-binary --plan` wurde **nur gelesen**.
Der `--plan`-Rücksprung (cli.c 11325–11337) erfolgt **vor**
`g_client_selection = requested_clients` (11346). `skip_binary` wird dem
Planbuilder nicht übergeben, dieser verwendet `bin_target` statt der späteren
Selbstbinary. Der Plan liefert Pfade, **keine Assetbytes**; `--clients` filtert
nur erkannte Clients, erzwingt keine Detektion. Deshalb weder Plan noch
`next_safe_command` als codex-exklusive Scopefreigabe oder Originaloutput ausgeben.

Statische C-Literaldekodierung ohne Compiler/Import ergab am Releasecommit:
`skill_content` 5571 UTF-8-Bytes, SHA-256
`8199b92faf89ab7b33bd5f2d7d1f8e967b53741cb357735219c049218a09c1b1`;
Pointer 80 Bytes, SHA-256
`11901ae6aa7431aac51f75d580f1f42955993704cc3ac22d6e7efd2e3be72940`.
Das ist **keine Originalinstallerausgabe**, kein G2-Abschluss und kein Beleg für
Zustandserhalt oder Runtimefunktion. Die Dekodierung überspringt Kommentare,
verarbeitet aneinandergereihte C-Stringliterale bis zum echten Semikolon und lässt
das C-NUL weg. Hashes dürfen nur mit genau dieser Quellenidentität verglichen werden.

**Kleinster Folgeauftrag:** isolierten Originalinstaller-/Assetvergleich ausdrücklich
freigeben, nicht Produktanalyse oder globales Teamsetup. Danach:

1. Originalbinary/Archiv/Quellen desselben Releases verifizieren. Parser, komplette
   Install-/Startup-/Detektions-/Daemon-/Schreibpfade erneut lesen; Grenzen gelten
   auch für `--plan`. Dedizierten wegwerfbaren Prüfkontext mit eigenen Benutzer-/
   Dateisystem- und Prozessgrenzen wählen; keine persönlichen Homes, Credentials,
   aktiven Daemons oder Host-Sockets zugänglich machen. Ein temporärer HOME allein
   ist kein Isolationsbeweis. Freigabe muss mögliche Kindprozesse/Daemonwirkung
   einschließen oder sie wirksam ausschließen. Keine Installation zum Testen dieser
   Dokumentation im Autorenkontext.
2. Darin absolute `PROBE_HOME`, `PROBE_CODEX_HOME`, `PROBE_HERMES_HOME`,
   `PROBE_CACHE`, `PROBE_RUNTIME`, XDG-Verzeichnisse und `PROBE_TMP` festlegen,
   nicht global exportieren. HOME und beide Harnesshomes müssen allein in diesen
   Prüfbereich zeigen. Codexdetektion prüft das aufgelöste Configverzeichnis:
   dieses mit synthetischem fremdem Config-/AGENTS-Inhalt anlegen. Zwei getrennte
   Fälle vorbereiten: ohne hooks.json (TOMLroute), mit synthetischer hooks.json
   (JSONroute). Symlinks/externen Config-Follow ausschließen, PATH auf genehmigte
   Werkzeuge begrenzen, alle Ausgangsdateien/Hashes und Prozesszustand aufnehmen.
3. Erst in diesem Scope, mit freigegebener absoluter `CBM_BINARY`, Originalroute
   ausführen. Die folgende Shellform ist ein **zukünftiges Rezept**, kein Laufbericht;
   Variablen müssen aus Schritt 2 stammen, `PROBE_BIN` darf keine bestehende Binary
   enthalten (der Installer hat auch bei skip-binary einen Zielkonfliktpfad):

   ```sh
   env -i HOME="$PROBE_HOME" CODEX_HOME="$PROBE_CODEX_HOME" HERMES_HOME="$PROBE_HERMES_HOME" XDG_CONFIG_HOME="$PROBE_XDG_CONFIG" XDG_CACHE_HOME="$PROBE_XDG_CACHE" XDG_DATA_HOME="$PROBE_XDG_DATA" XDG_STATE_HOME="$PROBE_XDG_STATE" XDG_RUNTIME_DIR="$PROBE_RUNTIME" CBM_CACHE_DIR="$PROBE_CACHE" CBM_RUNTIME_DIR="$PROBE_RUNTIME" TMPDIR="$PROBE_TMP" PATH="$PROBE_PATH" "$CBM_BINARY" install --clients=codex --skip-binary --plan --dir="$PROBE_BIN"
   env -i HOME="$PROBE_HOME" CODEX_HOME="$PROBE_CODEX_HOME" HERMES_HOME="$PROBE_HERMES_HOME" XDG_CONFIG_HOME="$PROBE_XDG_CONFIG" XDG_CACHE_HOME="$PROBE_XDG_CACHE" XDG_DATA_HOME="$PROBE_XDG_DATA" XDG_STATE_HOME="$PROBE_XDG_STATE" XDG_RUNTIME_DIR="$PROBE_RUNTIME" CBM_CACHE_DIR="$PROBE_CACHE" CBM_RUNTIME_DIR="$PROBE_RUNTIME" TMPDIR="$PROBE_TMP" PATH="$PROBE_PATH" "$CBM_BINARY" install --clients=codex --skip-binary --dir="$PROBE_BIN"
   ```

   stdout/stderr/Exitcodes in separate Capturedateien des Prüfbereichs sichern.
   Vor der zweiten Zeile Plan, Baseline und Quellschreibscope vergleichen; bei
   fremden Zielen abbrechen. Kein `--force`, `--reset-indexes` oder automatisches
   `--yes`. Nicht aus dem fehlerhaften Plan allein Berechtigung ableiten. Beide
   Hookrepräsentationen in frischen Teilbereichen testen; Hermes analog mit
   `--clients=hermes` und seinem nachgewiesenen Detektionspfad getrennt prüfen.
4. Vollständiges echtes Dateidelta aufnehmen. Erwartung im konfliktfreien Codexfall:
   Skill, AGENTS, config.toml und drei Agent-TOMLs (sechs Pfade), mit vorhandener
   hooks.json sieben. Nicht bloß diese Erwartung als beobachteten Output abschreiben.
   Fremde synthetische Konfiguration/AGENTS/Hooks müssen inhaltlich erhalten sein.
   Zusätzliche/fehlende Ziele und Fehler sind Blocker, keine tolerierten Warnungen.
5. Aus **echter** Ausgabe nur Skill und Original-Aktivierung/Hookwerte selektieren,
   MCP nativ mergen. Die drei Agent-TOMLs bleiben allein im isolierten Output,
   werden nicht ins Team übernommen. Vollständigen Transfermanifest mit SHA-256
   und Quelle→Zielabbildung führen. Für pfadgebundene Commands `cli.c` und
   Originalrenderer zurückverfolgen; Testbinarypfade niemals produktiv aktivieren.
   Zulässige Parametrisierung separat notieren und semantisch zurücklesen.

Unveränderliche Skillbytes bytegenau mit der echten Originalausgabe vergleichen; pfadparametrisierte Konfiguration nicht als insgesamt bytegleich ausgeben.

6. Nur wenn Originaloutput, Erhalt fremder Werte, erlaubte Dateimenge und selektiver
   Bytevergleich bestehen, G2 mit konkretem Beleg schließen. Andernfalls Konflikt
   vor A01-Abnahme vorlegen; kein eigener CBM-Fork/Installerwrapper, keine still
   zusätzliche Helfergruppe. Native Zielintegration/Discovery/Funktion bleiben
   danach eigene R1-Prüfungen, nicht durch diesen isolierten Lauf erledigt.

### Betrieb, Indexstatus und echte Relationsprüfung (später)

MCP-Sitzungen tatsächlich an die jeweilige Workspacewurzel binden; ein einmaliger CLI-Index ist kein Watcher-Nachweis.
Die sitzungsgebundene Registrierung des CWD muss im echten Worker nachgewiesen
werden; bei mehreren Repos jede relevante Root registrieren, nicht nur deren
Elternordner. Daemon-/Cache-/Buildkontext über alle vier Verbraucher abgleichen.

Im geladenen Originalskill erst `list_projects`, Projekt nach `root_path` wählen;
als `project` den zurückgegebenen Namen oder absoluten Root verwenden, keinen
geratenen Ordnernamen. `get_graph_schema` für Beziehungen/Properties lesen.
Konkrete MCP-Argumentformen aus `src/mcp/mcp.c` (an Zielversion erneut prüfen):

```json
{"repo_path":"<TEST_REPO>","mode":"fast","persistence":false,"async":true}
```

Dies an `index_repository` senden; mit demselben repo_path und `status:true`
bis `succeeded`, `failed` oder `cancelled` begrenzt pollen. Ein lebender
MCP-/Daemonkontext ist Voraussetzung für async; Timeout/Fehler offenlegen.
Danach `index_status(project="<aufgelöstes Projekt>", verbose=true)`:
Bereitschaft, Root, gespeicherte Revision/Generation, Counts, Coverage und Watchzustand
prüfen. Schema-/Feldnamen nicht aus einer alten Antwort erfinden.

`search_graph(project=..., label="Function", name_pattern=".*t5_leaf.*")` liefert
qualifizierten Namen; `trace_path(project=..., function_name="<exakter Treffer>",
direction="both", depth=3)` muss den Aufrufer zeigen. Alternativ echte
`query_graph`-Relation, nicht nur Symboltexttreffer:

```text
MATCH (a)-[r:CALLS]->(b) WHERE a.name = 't5_entry' RETURN b.name
```

Zusätzlich `check_index_coverage` für alle Belegpfade, `get_code_snippet` und
Pagination (`has_more`/offset bzw. next_cursor) beachten. Fehlende/ausgeschlossene
Bereiche durch gezieltes Lesen prüfen; ein grüner Indexstatus ist kein vollständiger
Negativbeweis. Nach Änderung Watcherregistrierung/erfolgreiche Aktualisierung
nachweisen oder nativ erneut `index_repository` und Status verwenden. Erst dann
neue Relation abfragen; ein Dateisystemzeitstempel ersetzt diesen Beleg nicht.
Git-Kontextwechsel kann Originalvollaufbau erfordern.

## Synthetischer Abnahmefall und Update-/Rückweg

Nur später im freigegebenen **separaten Testworkspace**, nicht im Produktprojekt,
ein kleines Repo mit `probe.py` anlegen und den Prüfcommit festhalten:

```python
def t5_leaf():
    return 1


def t5_entry():
    return t5_leaf()
```

Nach erster erfolgreicher Symbol-/Relationsquery autorisiert `t5_added` hinzufügen
und `t5_entry` zusätzlich `t5_added()` aufrufen lassen. Änderung und Prüfcommit bzw.
uncommitted Diff/Dateihashes festhalten. Originalupdate durchführen, erfolgreiche
Generation/Indexstand prüfen und neue Relation `t5_entry` → `t5_added` tatsächlich
abfragen; alten Graphen als Negativkontrolle nicht aktuell nennen. Gespeicherter
Indexzustand/Prüfrevision und relevanter Arbeitsbaum müssen zusammenpassen.
Bei Graphify ggf. Belegmetadaten separat speichern statt native Gitfelder zu erfinden.

Je gewähltem Weg alle drei Rollen und Team-Codex auf tatsächliche Skill-/Referenz-
auflösung und Analysezugriff prüfen. Bei CBM zusätzlich Hermes `pre_llm_call` und
Codex beide Hookereignisse samt Kontext und unveränderte sechs Originalagenten
prüfen. Hook-Consent, neue Sitzung/Resume und echter Coder-Worker sind eigene
Nachweise. Kein siebter Graphhelfer. Ein erfolgreicher Elterncall beweist kein
Child-MCP; der Originalskill regelt explizite Evidenzübergabe an Kinder.

Tool-/Skillupdates getrennt von Indexupdates behandeln: neuen geeigneten
Originalstand prüfen, vollständige Dateimenge/Lizenzen/Hashes neu aufnehmen,
Runtimekompatibilität klären, fremde Änderungen nicht überschreiben. CBM:
Build-/Daemon- und G2-Deltas erneut prüfen, keine gemeinsame Runtime ungefragt
aktualisieren; Hookänderungen erneut vertrauen lassen. Anschließend begrenzte
Funktions-/Relations-/Änderungsprüfung im Testworkspace wiederholen.

Rückweg nur für diesem Setup eindeutig zugeordnete Skill-, Policy-, MCP- und
Hookeinträge nach Freigabe; Vorherzustände gezielt wiederherstellen. Gemeinsame
Binary/Daemon, andere Profile/Agents, Projekt-AGENTS und fremde Indizes erhalten.
Graphdaten haben einen eigenen Daten-/Löschscope. Offene G2-/R1-Gates und
Teilergebnisse im privaten Setuprecord melden, nicht als vollständige A01/B-Abnahme.
