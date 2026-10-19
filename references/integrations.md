# Originalintegrationen im bestätigten Zielkontext

Alle Befehle sind **spätere Rezepte**, keine Bau-/Testaktionen. Vorher Bestand,
Zielpfade, native Leser und Freigaben aus [Setup](setup.md) prüfen. Pro Quelle
aktuellen geeigneten Originalstand auflösen, Revision/Release, vollständige
Dateimenge, Hashes, Lizenz/Notice und Zielharness im privaten Setuprecord erfassen.
Historische Researchrevisionen sind keine Installationsvorgabe. Fremdcode zunächst
statisch prüfen; Installer, Hooks, PM-Aufnahme und echte Calls gesondert genehmigen.
Keine Dateien aus privaten Quellprofilen kopieren und keine Fremdplugins reparieren.

<a id="project-tools"></a>
## Projektwerkzeuge aus dem tatsächlichen Projekt

Lies pro Repository Root-/Bereichs-AGENTS, Manifeste, Lockfiles, Wrapper und Build-/
Testkonfiguration. Erfasse je Fähigkeit Quellpfad/Revision, Constraint, Aufruf-CWD,
Aufrufweg, tatsächliche Binary-/Paketauflösung und Prüfstatus. Unterschiedliche
Stacks und mehrere Repos unter einem Workspace mit Leerzeichen bleiben eigenständig.
Produktbibliotheken sind keine global zu installierenden Entwicklungswerkzeuge.

Trenne Host-Runtimes/Grundwerkzeuge von projektlokalen Runnern, Buildplugins,
Prozessoren/Generatoren, Lintern/Formattern, Testbibliotheken und Testdiensten.
Wrapper und `packageManager` gehen einer geratenen globalen Toolliste vor.
DevHours ist nur eine Referenz für diese **Kategorien**, keine universelle Java-/
Node-/pnpm-/PostgreSQL-/Browserpflicht und keine Voraussetzung für den Export.
Fehlende Zielconstraints offenlegen, nicht `latest` oder Referenzversionen einsetzen.

Passenden Bestand wiederverwenden. Downloads durch Wrapper/Corepack, frozen
Installationen, Buildskripte, Browserbezug und Dockerzugriff können schreiben oder
Code ausführen; dafür konkreten Scope genehmigen lassen. Keine pauschale Freigabe
aller Installationsskripte. Prüfen und Formatieren unterscheiden; Zielprojekt-
Testreihenfolge einschließlich vorgelagerter Generierung respektieren. Worker-
CWD/PATH, nötiges JAVA_HOME oder andere toolbezogene Pfade, Caches/Berechtigungen
im realen Coder-, Reviewer- und Codexkontext nachweisen. Eine Adminshell ist kein
Workerbeleg. Projekt-AGENTS bleiben unverändert; keine Produktanalyse beim Setup.

<a id="hermes-base"></a>
## Vorhandene Hermes-Basisskills

Original: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent).
Für den Coder den vollständigen Distributionsbaum `skills/autonomous-ai-agents/codex`,
für den Reviewer `skills/devops/sdlc-review` auflösen; vorhandene Distribution und
kanonische Lizenz-/Begleitdateien wiederverwenden. Unterpfade am tatsächlichen
Stand bestätigen. Fehlen sie, aktuellen offiziellen Distributionsbezug mit
Installationseffekt klären, keine gleichnamige private Ersatzfassung installieren.

Später je Rolle Katalog, Hauptskill und alle benötigten Referenzen im tatsächlichen
Profil laden, Quellpfad/Revision nachweisen. `codex` bleibt unverändert; konkrete
Teamhomes und Arbeitsgrenzen liefert der installierte `devteam-workflow`.
`sdlc-review` ist eigenständige fachliche Reviewfähigkeit, nicht im Maker nachgebaut.

<a id="team-codex"></a>
## Team-Codex: Binary, Homes, Anmeldung, Modellpolicy

Original: [openai/codex](https://github.com/openai/codex),
[Konfigurationsorte](https://developers.openai.com/codex/config-advanced.md),
[Skills](https://developers.openai.com/codex/skills.md),
[Authentifizierung](https://developers.openai.com/codex/auth.md).
Geeignete vorhandene Binary wiederverwenden, tatsächlichen absoluten Binarypfad
auflösen und dokumentieren; bei Fehlen aktuellen offiziellen Bezug prüfen und
gezielt genehmigen lassen. Kein eigener Codex je Hermes-Rolle.

Im tatsächlich aufgelösten Coderhome zwei eindeutig diesem Team zugeordnete
Verzeichnisse anlegen: `devteam/codex-home` und `devteam/user-home`.
`CODEX_HOME` zeigt auf ersteres, `CODEX_PROCESS_HOME` auf letzteres.
Nur der Codex-Prozess erhält HOME und CODEX_HOME; der Hermes-Prozess behält sein Profilhome.
Keine globale Shell-/Service-Env ändern. Grundform für jeden Team-Codex-Aufruf:

```sh
env HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" PONYTAIL_DEFAULT_MODE=full "$CODEX_BINARY" login --device-auth
```

Das ist ausschließlich der reguläre Login bei passender Kontounterstützung;
sonst den aktuellen offiziellen regulären Login im **gleichen Teamkontext**
verwenden. Nutzer durch den geschützten Login führen, keine Tokens in Chat,
Argumente oder Protokolle übernehmen. Hermesauth beweist keinen Codexzugang;
keine pauschale Authdateikopie und kein Authproxy.

Jeder spätere Codexauftrag bekommt dieselbe prozesslokale Doppelbindung durch
den Coder und den unveränderten Hermes-`codex`-Skill, ohne zusätzlichen Wrapper.
`CODEX_HOME/config.toml` trägt die bestätigte native Modell-/Reasoningauswahl
(`model`, `model_reasoning_effort`, bei gewählter eigener Providerroute
`model_provider` samt offiziell unterstützter Definition). Nur vom Zielstand
unterstützte Werte setzen, vorhandene Einträge gezielt erhalten. Abgleich mit
`devteam/model-policy.md`; eine Markdownpolicy erzwingt keinen Modellwechsel.
Höhere freigegebene Routen an konkreten nativen Auswahlwegen festmachen, im echten
Call belegen; ansonsten vor der betroffenen Hochrisikoarbeit an den Planner.

Skills gehören nach `CODEX_PROCESS_HOME/.agents/skills/<name>/`, Original-TOMLs
nach `CODEX_HOME/agents/`. Prüfe im **echten Worker** zusätzlich kompatibles
`CODEX_HOME/skills`, Projekt-/Ancestor-`.agents/skills`, Projektkonfiguration,
Admin-/Systemquellen und geerbte Overrides. Doppeltes HOME reduziert persönliche
Skills, ist aber keine Sandbox oder Garantie gegen alle anderen Quellen. Erhalte
persönliche Codexdateien und dokumentiere effektive Skill-/Config-/Pluginroots.
Pfade für projektbezogene Tools nach HOME-Wechsel bewusst prüfen; nicht kompletten
persönlichen Zustand zur „Reparatur“ kopieren.

<a id="superpowers"></a>
## Superpowers — nur Planner

Original: [obra/superpowers](https://github.com/obra/superpowers), vollständiges
Repository mit `.hermes-plugin/plugin.yaml`, `.hermes-plugin/__init__.py`, gesamtem
`skills/`-Baum und MIT-`LICENSE`. Aktuelle native Originalroute:

```sh
hermes -p "$PLANNER" plugins install obra/superpowers --enable
```

Nach Aufnahme die native Pluginregistrierung und alle Originaldateien im Planner
prüfen. Im neuen tatsächlichen Plannerkontext Bootstrap `using-superpowers/SKILL.md`
**und** `references/hermes-tools.md` sowie profilrichtige Skillreferenzen belegen.
Keine zusätzlichen Superpowers-Installationen in Coder, Reviewer oder Team-Codex.
Bei fehlenden Pfaden/Versionskonflikt Teilstand erhalten und klären, keine eigenen
Pluginpfadpatches. Rückweg: nur eigene Plannerregistrierung nativ deaktivieren/
entfernen, ursprüngliche fremde Plugin-/PM-Bestände bewahren.

<a id="ponytail"></a>
## Ponytail — Coder und Team-Codex separat

Original: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail),
[Original-Installationsanleitung](https://github.com/DietrichGebert/ponytail/blob/main/INSTALL.md).
Ganzes Repository mit `plugin.yaml`, `__init__.py`, `.codex-plugin/plugin.json`,
Skills, Hooks/Runtime-JavaScript und MIT-Lizenz beziehen. Node im Codex-Worker-PATH
ist Voraussetzung der Originalhooks, nicht aus einer SOUL ableitbar.

```sh
hermes -p "$CODER" plugins install DietrichGebert/ponytail --enable
```

Nur beim vom Autor dokumentierten Root-`plugin.json`-/Manifestgate-Konflikt:
aktuelle Originalanleitung prüfen, vollständiges **unverändertes** Repository im
bestätigten `<Coderhome>/plugins/ponytail` bereitstellen, danach profilbezogen
`hermes -p "$CODER" plugins enable ponytail`. Diese Verzeichnisroute ist eine
Plugin-/PM-Aufnahme und braucht dieselbe Freigabe; kein Manifestfix/Trustbypass.
Bei anderem Fehler anhalten statt die Ausnahme pauschal anzuwenden.

Im gebundenen Team-Codex-Prozess:

```sh
env HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" PONYTAIL_DEFAULT_MODE=full "$CODEX_BINARY" plugin marketplace add DietrichGebert/ponytail
env HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" PONYTAIL_DEFAULT_MODE=full "$CODEX_BINARY" plugin add ponytail@ponytail
```

Native Hookfreigabe über `/hooks` für die tatsächlichen Originaldefinitionen
prüfen: SessionStart, SubagentStart und UserPromptSubmit. Keine Hookfreigabe als
vorausgesetzt melden. Pluginroot, Datenroot (`PLUGIN_DATA`, `.ponytail-active`)
und tatsächliche Moduswahl erfassen. Hermes-Default `full` kann durch Env oder Userdefaults verdrängt werden; ein
Slashwechsel ist prozesslokal. Konkreter Originalleser in `__init__.py`:
`PONYTAIL_DEFAULT_MODE` → `defaultMode` aus
`$XDG_CONFIG_HOME/ponytail/config.json` (falls gesetzt), sonst
`$HOME/.config/ponytail/config.json` → eingebautes `full`.
Prüfe diese Quellen im tatsächlichen Coder-Prozess, ohne dessen HOME zu verändern.
Ist kein abweichender Override wirksam, den eingebauten persistenten Default
verwenden und frisch gestarteten Coder samt injiziertem `full` belegen. Bei
abweichendem gemeinsamem Override: keine globale Userdefault-Änderung als
Setupnebenwirkung. Nur eine am Ziel nachgewiesene profilbezogene native
Prozesskonfiguration für `PONYTAIL_DEFAULT_MODE=full` nach konkreter Freigabe
verwenden; fehlt ein solcher Weg im geteilten Owner, diese Fähigkeit blockieren
und den Konflikt benennen. Kein erfundener YAML-Schlüssel oder Pluginpatch.

Team-Codex liest denselben Default über `hooks/ponytail-config.js`. Übergib für
**jeden Team-Codex-Aufruf** zusätzlich prozesslokal `PONYTAIL_DEFAULT_MODE=full`
in der `env`-Präfixliste neben HOME/CODEX_HOME; halte diesen festen Zusatz in der
Modell-/Risikopolicy unter dem tatsächlichen Codex-Aufrufweg fest. So überschreibt
ein geerbtes XDG-Konfigurationsverzeichnis nicht still den Teamdefault, ohne
persönliche Dateien zu ändern. Der originale SessionStart-Hook setzt den aktiven
Modus, `hooks/ponytail-runtime.js` schreibt ihn unter dem tatsächlichen
`PLUGIN_DATA` nach `.ponytail-active` (gegebenenfalls zusätzlich projektbezogen).
`/ponytail full` ist der originale Moduswechsel, nicht allein der Persistenzbeleg.
Prüfe neuen tatsächlichen Worker/Gatewayprozess und Team-Codex inklusive
Resume/Child: persistenter Datensatz und injizierter Modus sind getrennte Belege.
Ein `full`-Wort in SOUL genügt nicht.
Rückweg: eigene Pluginregistrierung/Hookfreigabe und zugeordnete Modusdateien
gezielt zurücknehmen; keine gemeinsamen Runtimes oder persönlichen Plugins löschen.

<a id="caveman"></a>
## Caveman und find-skills

Original [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman): exakt
vollständigen Hauptskill `skills/caveman/SKILL.md` **und** `README.md` beziehen,
Original-`LICENSE`, `LICENSE-MIT`, `NOTICE` erhalten. Der recherchierte Original-
Alias `full` wird auf `caveman` abgebildet (`src/hooks/caveman-config.js`). Aktuellen
Dateibaum/Mapping bestätigen; kein zusätzliches CLI-/Proxy-/Routingprodukt.

Nach `<Coderhome>/skills/caveman/`, `<Reviewerhome>/skills/caveman/` und
`<CODEX_PROCESS_HOME>/.agents/skills/caveman/` mit vollständigen Begleitdateien
bereitstellen. Für beide Hermesrollen `skills.auto_load` gezielt um `caveman`
erweitern; bestehende Liste zunächst lesen, duplikatfrei mergen und als JSON-Liste
über `hermes -p "$PROFILE" config set skills.auto_load "$AUTO_LOAD_JSON"` setzen,
danach `config get skills.auto_load`. Nicht die ganze vorhandene Liste ersetzen.
Im echten neuen Kontext geladenen Originalhauptskill nachweisen. Team-Codex erhält
`$caveman` ausdrücklich in **jedem neuen Auftrag**, auch nach Neustart/Resume.
Diese Pflicht steht dauerhaft in der [lokalen Modell-/Risikopolicy](../unklar/templates/model-policy.md).
Beim Setup die Klausel mit ausgeben und über MODEL_POLICY_REF im Coderhome rücklesen;
der installierte Alltagsvertrag darf nicht vom erneuten Laden dieses Makers abhängen.

Nur Chat wird verkürzt. Code, Dokumentation, Commits, Memory und Sicherheitsklarheit
bleiben normal verständlich. Planner bleibt normale Sprache. Rückweg entfernt nur
die eigenen identifizierten Skillkopien und den eigenen Autoload-Eintrag.

<a id="find-skills"></a>
Original [vercel-labs/skills](https://github.com/vercel-labs/skills): vollständiges
`skills/find-skills/` (recherchiert genau `SKILL.md`) und MIT-`LICENSE` nach
`<CODEX_PROCESS_HOME>/.agents/skills/find-skills/`. Aktuelle Begleitdateimenge
erneut prüfen, nicht nur eine URL kopieren. Native Discovery/geladener Skill und
später eine genehmigte Suche über den Originalskill belegen. `npx skills` kann
Paketbezug auslösen; Suchergebnis und Installationsfreigabe bleiben getrennt.
Ergänzungsvorschläge gehen über Coder zum Planner, nicht automatisch installieren.

<a id="codex-agents"></a>
## Sechs unveränderte Original-Agent-TOMLs

[VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents),
MIT-`LICENSE` erhalten. Genau die sechs Originalpfade des
[Manifests](../manifest.json) beziehen: `test-automator`, `security-auditor`,
`reviewer`, `anti-ui-slop-reviewer`, `ui-fixer`, `docker-expert`.
Keine anderen Agentpakete pauschal installieren. Nach `CODEX_HOME/agents/` unter
Originalbasename schreiben, erst nach Kollisions-/Eigentumsprüfung.

Pro Datei **drei getrennte Nachweise** führen:

1. Vollständige Originalbytes/Revision/Hash, TOML parsebar, Name,
   `developer_instructions`, `model`, `model_reasoning_effort`, weitere Original-
   Felder unverändert. Mit dem Original vergleichen, nicht nur Pins abschreiben.
2. Native Discovery im tatsächlichen Team-Codex mit dieser Datei und wirksamen
   Pins. Modellpolicy und Zugang prüfen; eigene Modell-/Reasoningauswahl ersetzt
   keinen Originalpin. Provider/Approval/MCP können aus dem Parent kommen, eine
   TOML-Sandboxzeile allein ist keine neue Sicherheitsgarantie.
3. Nach Testfreigabe **je Helfer ein echter begrenzter Delegationsaufruf** im
   separaten Testworkspace mit engem Auftrag/Schreibscope, tatsächlichem Modell,
   Ergebnis und Nachweis. Kein umfassender fachlicher Benchmark. Ein Katalogeintrag
   oder Elterncall genügt nicht. Kein Helfer ersetzt unabhängigen Hermesreview.

Fehlt ein Original-Modellpin im gewählten Zugang, halte die betroffene Pflichtfähigkeit offen und erhalte die Originaldatei.
Planner benennt fehlende Verfügbarkeit und den nötigen autorisierten Zugang;
keine stille Modellsubstitution, kein zweiter Anbieter als pauschale Voraussetzung.
Rückweg nur eigene sechs unveränderte Kopien nach Hashabgleich; fremde Agenten bleiben.
Native Referenz: [Custom Agents](https://developers.openai.com/codex/subagents.md).

<a id="hindsight"></a>
## Hindsight am vorhandenen Dienst

Original [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight/tree/main/hindsight-integrations/hermes),
vollständiger Unterbaum `hindsight-integrations/hermes` samt benötigten übergeordneten
Originallizenzen/Notices. Native Katalogaufnahme, keine private Pluginversion:

```sh
hermes -p "$PROFILE" plugins install hindsight
hermes -p "$PROFILE" memory setup
hermes -p "$PROFILE" config get memory.provider
```

Geführt **vorhandenen** Dienst (`local_external`) wählen, bestätigte neue gemeinsame
Projektbank binden, `memory.provider=hindsight` rücklesen. Bei Wiederaufnahme
vorhandene eigene Bank statt einer Doppelbank verwenden. Native Setupfelder und
tatsächliche Bankidentität prüfen; kein Embedded-Server als Ersatz. Aktueller
recherchierter Katalogadapter 1.2.3 verlangt Hermes >=0.21.4, Python >=3.11 sowie
`hindsight-client>=0.10.1,<1` und `hindsight-embed>=0.10.1,<1`; das sind Quellenbefunde,
keine vorab genehmigte Installation. Zielkatalog und gemeinsame PM-Wirkung prüfen.

Der Originaladapter liest profilbezogen `<Rollenhome>/hindsight/config.json`,
dann legacy geteilte Konfiguration, dann Envfallback. Erstelle/merge deshalb nach
nativer Memoryeinrichtung die **profilbezogene JSON-Datei** mit dem Dateitool,
erhalte fremde Einträge, parse/rücklese sicher; nicht erfundene
`memory.hindsight.*`-YAML-Schlüssel setzen. Dieser JSON-Weg ist der Original-
Konfigurationsleser, keine zweite Runtime. Erforderliche nichtgeheime Felder je Rolle:

```json
{
  "mode": "local_external",
  "api_url": "BESTAETIGTER_DIENST",
  "bank_id": "BESTAETIGTE_NEUE_BANK",
  "memory_mode": "hybrid",
  "auto_recall": true,
  "recall_prefetch_method": "recall",
  "recall_tags": ["scope:shared", "role:planner"],
  "recall_tags_match": "any_strict",
  "auto_retain": true,
  "retain_every_n_turns": 2,
  "retain_tags": ["role:planner"],
  "observation_scopes": "per_tag",
  "recall_types": ["observation", "world", "experience"],
  "reflect_tags": ["scope:shared", "role:planner"],
  "reflect_tags_match": "any_strict"
}
```

Die drei Rollen erhalten in **allen drei Taglisten** jeweils `role:planner`,
`role:coder` oder `role:reviewer`. Dienst/Bank durch echte bestätigte Werte ersetzen.
Geheimnis nötigenfalls geschützt über natives `HINDSIGHT_API_KEY`; nicht in Record
oder diese JSON-Vorlage. Prüfe konkurrierende `apiKey`/`api_key`, Banktemplates,
Legacy-/Env-/CWD-Bankdiscovery und effektive Bankauswahl ohne Secrets auszugeben.
Explizite Rollenfelder und Bank müssen tatsächlich beim Verbraucher ankommen.

Leser am verwendeten Adapter prüfen: `_load_config`, Providerinitialisierung,
`_build_retain_kwargs`, `_recall`, `_reflect`, `_do_recall`, `_tool_reflect`.
Recall muss `tags`/`tags_match` und gewählte Typen, Retain die Tags und
`observation_scopes`, Reflect **eigene** `reflect_tags`/`reflect_tags_match` an
`areflect` weitergeben. Recallfilter werden nicht automatisch auf Reflect vererbt.
SDK/Server müssen die Originalfelder unterstützen. `per_tag` erhält Rollen-
Konsolidierung, `any_strict` schließt ungetaggte Treffer aus; eine globale
ungetaggte Observation ist nicht `scope:shared`-Wissen. Tags sind keine ACL.

**Spätere begrenzte Abnahme:** nur autorisierte Testdaten in der eigenen Bank;
gezielt eigene Rolle, andere Rolle, Shared und ungetaggt unterscheiden. Pro Rolle
Konfiguration → echte Requestfelder → gespeicherte Tags/Retainintervall zwei Turns
→ Recallresultate → konsolidierte Ergebnisse getrennt belegen. Bestätigtes
projektweites Wissen bewusst mit `scope:shared` fördern; keine Wissensvorbefüllung.
Reflect (explizit **und** Prefetch) erst nach nachgewiesener Rollenfilterweitergabe
nutzen. Bis dahin Prefetch auf `recall` belassen und nur gefilterten Recall verwenden.
Kein eigener Pluginfix. Bankweite Directives sind nicht durch Tags voll isoliert.
Rückweg: eigenes Memorybinding nativ deaktivieren/gezielt zurücksetzen; eigene
JSON-Feldänderungen zurücknehmen. Bankinhalte bleiben ohne Löschfreigabe erhalten.

Quellen: [Hermes Memory Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers),
[geprüfter Katalogadapter](https://github.com/vectorize-io/hindsight/blob/d952b6e655fccab4581ee0722b51c5f103873d12/hindsight-integrations/hermes/__init__.py),
[Recall](https://hindsight.vectorize.io/developer/api/recall#tags),
[Reflect](https://hindsight.vectorize.io/developer/api/reflect#tags).

<a id="mattermost"></a>
## Mattermost geführt — ausschließlich Planner

Maßgeblich: [offizielle Hermes-Anleitung](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/mattermost)
und Zielversion. Führe diese Schritte mit Wartepunkten durch, statt nur Variablen
aufzulisten. Bei anderer Oberfläche aktuellen offiziellen UI-Weg prüfen.

1. Bestätige Server und vorgesehenes Team. Führe den Nutzer zur Kanalanlage in
   seiner Oberfläche, bei Wiederaufnahme zum zugeordneten vorhandenen Projektkanal.
   Über Kanalname → **View Info** echte Kanal-ID ermitteln; Name/Slug ist kein
   Ersatz. Typ und Teamzuordnung zurücklesen (öffentlich O / privat P).
2. Bei fehlender eigener Botidentität: Admin muss nötigenfalls System Console →
   Integrations → Bot Accounts → Enable Bot Account Creation freigeben. Nutzer
   über Menü → Integrations → Bot Accounts → Add Bot Account führen. Eigener
   Planner-Bot, Rolle **Member** genügt; keine Adminrechte für den Bot verlangen.
   Token direkt geschützt sichern lassen, niemals in Chat abfragen. Bestehenden
   eindeutig diesem Setup zugeordneten Bot erhalten.
3. Bot ins richtige Team und über Kanalname → **Add Members** in den Projektkanal
   aufnehmen; echte Bot-ID/Username und Mitgliedschaft prüfen. Menschliche User-ID
   über Avatar → Profile ermitteln und ausdrücklich bestätigen, nicht Bot-ID oder
   Anzeigename. Weitere Nutzer nur nach ausdrücklicher Zulassung.
4. `hermes -p "$PLANNER" gateway setup` aufrufen, Mattermost auswählen, Nutzer
   Server/Bot-Token über den nativen geschützten Eingabeweg eingeben lassen.
   Alternativ legt der Nutzer den Token direkt in die aufgelöste private Planner-
   Secretkonfiguration, nie als Shellargument. Allein Planner erhält diese Anbindung.
5. Direktgespräch zwischen Mensch und Planner-Bot öffnen. Die **andere** DM-Kanal-ID
   aus den tatsächlichen Kanalobjekten bestimmen. Falls die UI keine DM-ID zeigt,
   unterstützten autorisierten Lookup der Kanalmetadaten nutzen, Secret im Client
   schützen; keinen `curl -H ...TOKEN`-Befehl mit echtem Wert erzeugen. DM-Typ D
   und beide Teilnehmer prüfen. DM-ID ist weder Projektkanal-, Bot- noch User-ID.
6. Nichtgeheimes Verhalten explizit über native Profilkonfiguration setzen. Der
   gelesene Adapter verwendet `platforms.mattermost.extra` für die vier folgenden
   Werte. Lies vorhandenes `extra` geschützt und erhalte alle anderen Einträge.
   Merge diese vier Felder als JSON-Daten in `MATTERMOST_EXTRA_JSON` (hier nur
   Strukturbeispiel, Kanalwert durch die bestätigte echte ID ersetzen):

   ```json
   {
     "require_mention": true,
     "free_response_channels": ["BESTAETIGTE_PROJEKTKANAL_ID"],
     "allowed_channels": ["BESTAETIGTE_PROJEKTKANAL_ID"],
     "reply_mode": "off"
   }
   ```

   `reply_mode` muss ein **String** bleiben: einzelne untypisierte `off`-Werte
   können von `config set` als bool coerced werden. Das JSON-Mapping erhält den
   Stringtyp; nicht das ganze vorhandene `extra` durch das Beispiel ersetzen.
   Vorher auf versehentlich dort gespeicherte Secrets prüfen; bei solchen Werten
   keine argumentbasierte Gesamtausgabe, sondern den geschützten nativen Editor
   für genau diese Felder verwenden. Keine Secrets in CLI-Argumenten.

   ```sh
   hermes -p "$PLANNER" config set platforms.mattermost.extra "$MATTERMOST_EXTRA_JSON"
   hermes -p "$PLANNER" config get platforms.mattermost.extra.require_mention
   hermes -p "$PLANNER" config get platforms.mattermost.extra.free_response_channels
   hermes -p "$PLANNER" config get platforms.mattermost.extra.allowed_channels
   hermes -p "$PLANNER" config get platforms.mattermost.extra.reply_mode
   ```

   Nativer Wizard/Secretresolver verwendet außerdem `MATTERMOST_URL`,
   `MATTERMOST_TOKEN`, `MATTERMOST_ALLOWED_USERS` und `MATTERMOST_HOME_CHANNEL`.
   `MATTERMOST_ALLOWED_USERS` auf die bestätigte menschliche User-ID begrenzen;
   `MATTERMOST_ALLOW_ALL_USERS` darf die Begrenzung nicht aufheben. Die in Phase 5
   aus Kanalmetadaten bestimmte DM-ID zunächst für die spätere Homebindung
   festhalten; in dieser Konfigurationsphase keine Home-Nachricht senden.
   Native Wizardroute für die Konfiguration verwenden, nicht pauschal nichtgeheime
   Einstellungen in `.env` duplizieren. Home setzen und rücklesen folgt in Phase 8.
7. Prüfe die effektive Auflösung gegen Leser: Adapter `extra` gegenüber
   `MATTERMOST_REQUIRE_MENTION`, `MATTERMOST_FREE_RESPONSE_CHANNELS`,
   `MATTERMOST_ALLOWED_CHANNELS`, `MATTERMOST_REPLY_MODE`; URL/Token über
   `_url_and_token`, Nutzer über native Gatewayautorisierung, Home über
   Gateway-Konfigurationsresolver. Hier den Home-Leser prüfen; den gespeicherten
   Homezielwert erst nach dem Setzen in Phase 8 rücklesen. Konkurrierende Werte gezielt klären, kein
   komplettes Config-/Env-Dump. Kanal-Allowlist greift vor Mention; DMs umgehen
   Kanalprüfung, **nicht** menschliche Autorisierung. Fehlender Leser ist ein
   Setupblocker, keine Erlaubnis zu schwächeren Regeln.
8. Erst nach vollständigen angenommenen Rollen-/Binding-/Policydateien und
   konkreter Aktivierungsfreigabe den bestehenden vorgesehenen Multi-Profile-
   Gateway nutzen und das richtige Plannerprofil/Adapterrouting nachweisen.
   Unterstützte profilbezogene Aufnahme/Start verwenden; keinen zweiten Besitzer,
   globale Migration oder zentralen Restart als Standard auslösen. Bei bereits
   durch Create hot-admittiertem Planner den protokollierten frühen Aktivierungsstand
   berücksichtigen: vollständige effektive Aufnahme der angenommenen Rollen und
   aktuelles Adapterrouting erneut belegen, nicht einen ersten Start behaupten.
   Erst dann den Nutzer im getrennten Mensch–Bot-DM `/sethome` senden lassen;
   dieser Slashbefehl benötigt ein MessageEvent des laufenden Planneradapters.
   Den tatsächlich gespeicherten Homekanal zurücklesen: `MATTERMOST_HOME_CHANNEL`
   bzw. die native Homebindung muss die anhand der Metadaten bestätigte DM-ID sein,
   ohne zusätzliche Home-Threadbindung. Keine Projekt-ID als Homefallback.
   Bei fehlendem Adapter-/Homebeleg hier halten. Danach lass den Nutzer
   zuerst `@botname` im Projektkanal senden, warte auf echte Antwort. Dann zweite
   Nachricht **ohne Erwähnung**, danach DM-Dialog. Fehlende Antwort hält den Schritt
   offen: Identität, Mitgliedschaft, IDs, Zulassung, Verbindung/Overrides prüfen.
9. Die separate native Ticket-Wakebindung aus [Setup](setup.md) vor Ticketfreigabe
   anlegen und im freigegebenen Pipelineweg bis zur echten Planner-Kanalnachricht
   nachweisen. Homeziel allein beweist das nicht. Keine eigenen Threads, Registry
   oder zusätzliche Statuskanäle. Direkte Gespräche bleiben an ihrem berechtigten
   Zugang; der Projektkanal ist Ziel asynchroner Taskberichte, kein Gesprächszwang.

Rückweg: nur eigene Planner-Adapteraktivierung und dokumentierte Config-/Home-/
Allowliständerungen zurücknehmen; Tokenrotation nur gezielt nach Nutzerauftrag.
Bot, Kanal, Bank und Nachrichten nicht ungefragt löschen. Coder/Reviewer erhalten
keine Mattermost-Konfiguration. Normale native Nachrichtenübermittlung genügt;
keine historische besondere Thread-Abnahme hinzufügen.

## Codeanalyse und Quellenstand

Die Wahl zwischen `codebase-memory` und `graphify` bleibt verbindlich.
[Codeanalyse](../unklar/references/code-analysis.md) enthält beide vollständigen Originaldateimengen,
Runtime-/Zielkontexte, Aktivierung, Index-/Query-/Updateprüfung und Rückwege.
Genau den gewählten Weg auf alle drei Hermes-Rollen und Team-Codex anwenden.
G2/A01-CBM bleibt offen: echte Originalausgabe und Bytevergleich der selektiven
Übernahme ohne zusätzliche Helfer benötigen eine gesonderte Freigabe. Keine
Umdeutung der statischen Ableitung zum Installerbeleg. Die sechs VoltAgent-Helfer
bleiben unverändert. Quellen stehen im [Bezugsquellenverzeichnis](upstream-sources.md).

Statische Recherche vom 18.10.2026: Superpowers `bb92a77741419a4ab5f06e711a283343f1ada0c3`,
Ponytail `09c434ab73ca43761c5d8b0c5d341926c2fba710`, Caveman
`bad48a0e1df55e05e3f52249afa35ecc1909ee76`, find-skills
`13e4063a1cf913f5606d57d42ab83a86f5001e04`, VoltAgent
`16f880a2a0486f880da75d2baffcd68af4cc4811`. Diese Identitäten belegen die gelesenen
Originalwege, nicht erfolgreiche Installation oder eine dauerhafte Versionsliste.
