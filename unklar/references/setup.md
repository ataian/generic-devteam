# Geführtes natives Zielsetup

Diese lineare Anleitung gilt nur für ein ausdrücklich beauftragtes Zielsetup.
Bei Paketbau/Review bleibt sie Text. Verwende die [offizielle Hermes-Dokumentation](https://hermes-agent.nousresearch.com/docs/)
und den tatsächlichen Zielcode als Versionsautorität. Rechercheanker sind keine
Installationspins und keine Erfolgsmeldung. Rezepte unten enthalten ausschließlich
bestätigte, nichtgeheime Variablen; keine rohen Nutzereingaben als Shellcode.

## 1. Bestand vor Änderungen

1. Ermittle bestehenden Benutzer, Hermes-Distribution/Revision, tatsächliche
   Profilhomes und Terminalbackend. Prüfe Profilverzeichnis **und** native
   Profilregistrierung; ein markerloses vorhandenes Verzeichnis ist eine Kollision.
2. Ordne Gateway/Multi-Profile-Owner, bediente Planneradapter, Dispatcher- und
   Notifierzuständigkeit zu. Erfasse, wer das Board tatsächlich dispatcht und aus
   welchem Home die Dispatcherparameter gelesen werden. Einstellungen im Coder
   allein sind kein Beleg für den Dispatcher. Keine neue Daemonplattform anlegen.
3. Prüfe native Profile, Config set/get, Boards, blocked-first-Erstellung,
   expliziten Reviewer/Handoff, Same-Card-Rückgabe und Wake anhand der installierten
   Parser/Leser sowie [nativer Referenz](native-workflow.md). Bei fehlender Syntax
   zuerst aktuelle Docs/Quelltext lesen; erst nach Freigabe CLI/Loader prüfen.
4. Inventarisiere aktivierte Plugins/Memoryprovider aller gemeinsam betroffenen
   Profile und die PM-Abhängigkeitsgeneration ohne Secretwerte. Normale CLIstarts,
   einschließlich Help, können Dependency-Sync, Source-Completion oder Plugin-
   Eviction auslösen. Neue absolute Pluginmemberpfade können schon bei gleichen
   Versionen gemeinsame PM-Eingaben ändern. Hole vor Pluginaufnahme die Freigabe für gemeinsame PM-Wirkungen ein.
   Prüfe Fremdquellen zunächst außerhalb aktiver Discovery. Ist diese Wirkung
   nicht genehmigt, bleiben Quellenprüfung und vorhandene Teilstände erhalten.
5. Lege G1 zunächst als `open` fest. Prüfe im Ziel-Dispatcher Rate-Limit-Requeue,
   Fehlerzähler und endliches **Gesamtbudget**. `max_retries`, Cooldown und
   Per-Run-Timeout genügen nicht; auch kein erfolgreicher beaufsichtigter Durchlauf.
   G1 hält vor betroffener automatischer Dispatchfreigabe an.
   Fortsetzung nur mit nachgewiesenem unterstütztem nativen Gesamtbudget oder
   ausdrücklicher Anforderungsänderung; kein Retryjob, Wrapper oder Corepatch.

**Erfolgssignal:** Versionen, Zuständigkeit, verfügbare Schnittstellen, PM-Wirkung
und offene Gates sind benannt. Bestehende Schutz-/Freigabeeinstellungen bleiben
unverändert. Kein „bereit“, nur weil ein Gatewayprozess lebt.

## 2. Eingaben und Kollisionsprüfung

Frage zuerst **Projektname und Arbeitsverzeichnis**. Die feste Reviewer-Vorlage
nennt `~/projects/{{PROJECT_NAME}}`: Löse diesen Pfad mit dem Home des Zielkontos
und den bestätigten Workspace absolut auf und gleiche beide vor Anlage ab.
Bei Abweichung anhalten und mit dem Nutzer klären; weder SOUL-Pfad still ändern
noch widersprüchliche Board-/Profilbindungen anlegen. Projektname ist ein einzelnes
Pfadsegment ohne Slash, Backslash oder Traversal; Leerzeichen sind zulässig.
Erfasse vorhandene Repositorygrenzen,
Root- und relevante Bereichs-AGENTS sowie Manifeste/Lockfiles/Build-/Testkonfiguration.
Der Workspace muss kein Git-Root sein und wird nicht automatisch initialisiert.
Werkzeugbedarf stammt aus diesen Dateien, nicht aus einem neuen Fachinterview.
Bei noch leerem Projekt bleiben konkrete Stackwerkzeuge offen; kein Beispielstack
wird installiert. Siehe [Projektwerkzeuge](integrations.md#project-tools).

Danach kurz den Banknamen bestätigen, Projektname als Vorschlag. Prüfe am
vorhandenen Hindsight-Dienst Existenz und Eigentum, bevor eine neue Bank gebunden
wird. Gleiche Namen beweisen keine eigene Bank. Erfrage anschließend einmal die
Anzeigenamen für Planner (`PLANER_NAME`, genau ein N), Coding-Orchestrator
(`CODER_NAME`) und Reviewer (`REVIEWER_NAME`). Rollenfeste Texte verwenden:
keine Persona-Abfrage und keine still angehängte Persona. Bestätige danach die
Boardkennung; der spätere Wert `KANBAN_BOARD_NAME` stammt aus nativer Rücklese
der Boardkennung (`BOARD`), nicht aus dem Board-Anzeigetitel. Schlage getrennte
technische Kennungen vor, nie still aus Anzeigenamen ableiten; bereits bestätigte
Profil-IDs unverändert wiederverwenden,
prüfe die aktuellen nativen Namensregeln und lasse sie bestätigen. Der gelesene
Resolver erlaubt `[a-z0-9][a-z0-9_-]{0,63}`; reservierte Namen, native Kollisionen
und echte Pfade zusätzlich prüfen. Anzeigenamen nie als rohe Pfadsegmente verwenden.

Bestätige rollenbezogene Hermes-Modelle/Provider/unterstützte Denktiefe und Codex
separat. Die hierbei bestätigte technische Codex-Modell-ID als `CODEX_MODEL`
wiederverwenden, nicht erneut abfragen oder aus dem Hermes-Modell ableiten.
Empfehlung: Planner mindestens high, Coder/Reviewer normalerweise medium,
nur soweit unterstützt. Erfasse erlaubte höhere Stufen und benötigte Hilfsmodelle;
keinen zweiten Anbieter voraussetzen. Frage genau eine Codeanalyse ab. Bestimme
Mattermost-Server, eigene Botidentität, Projektkanal und menschlichen Nutzer;
ermittle die getrennte DM-ID im geführten Kommunikationsschritt.

Vergleiche **vor Anlage** alle drei Profile, aufgelösten Profilhomes, SOUL-/Skill-
Ziele, Boardkennung, Bank, Codexzustandsbereiche und Plannerkanal mit vorhandenen
Objekten einschließlich Symlinks. Fremde oder nicht eindeutig zugeordnete Objekte bleiben unverändert.
Ein gleichnamiges eigenes Objekt darf nur nach Abgleich mit dem Setuprecord und
nativer Identität wiederverwendet werden. Bei Konflikt neue bestätigte Kennung
wählen oder Eigentum klären; nicht automatisch suffixen, löschen oder klonen.

Zeige Ziel-/Änderungsliste, Installationen, Dienstzugriffe, PM-Wirkungen,
Create-/Multiplexeraktivierung und späteren Testumfang; warte auf konkrete Freigabe.
Token/Passwörter werden nicht abgefragt oder ausgegeben, nur ihr geschützter Zielweg.
Halte bestätigte Rohwerte samt Annahmebeleg zunächst als Setupdatensatz fest und
übernimm ihn nach Planneranlage unverändert in den privaten Setuprecord. Vorher
bei Unterbrechung den nichtgeheimen Datensatz zur Wiederaufnahme übergeben, nicht
unbeauftragt einen neuen Ablageort anlegen. Ein bereits bestätigtes Feld nicht
erneut erfragen; nur fehlende Werte oder nachgewiesene Konflikte klären.

## 3. Frische Profile, bestätigte Modelle

`PROFILE`/`DESCRIPTION` stehen jeweils für eine bestätigte neue technische Rolle
und nichtgeheime Beschreibung. Nur nach Kollisionsprüfung und Aktivierungsfreigabe:

```sh
hermes profile create "$PROFILE" --no-alias --description "$DESCRIPTION"
hermes profile show "$PROFILE"
hermes -p "$PROFILE" config set terminal.cwd "$PROJECT_DIR"
hermes -p "$PROFILE" config set model.provider "$PROVIDER"
hermes -p "$PROFILE" config set model.default "$MODEL"
hermes -p "$PROFILE" config set agent.reasoning_effort "$EFFORT"
hermes -p "$PROFILE" config set kanban.auto_subscribe_on_create false
hermes -p "$PROFILE" config get terminal.cwd
hermes -p "$PROFILE" config get model.provider
hermes -p "$PROFILE" config get model.default
hermes -p "$PROFILE" config get agent.reasoning_effort
hermes -p "$PROFILE" config get kanban.auto_subscribe_on_create
```

Reasoning nur bei bestätigter Unterstützung setzen, sonst fehlende Fähigkeit
oder bewusst nicht anwendbaren Wert protokollieren. Create verwendet Modellseeding
und kann den laufenden Multiplexer informieren. Prüfe übernommene Provider-/Endpoint-
Definitionen und setze die gewünschte Route bewusst; kein Clone und keine Credential-
kopie. Kein `--no-skills`: benötigte Basisskills müssen vollständig vorhanden sein.
Halte den **tatsächlich aufgelösten Profilhome** fest, nicht einen errechneten
Standardpfad. Nutze ihn für alle nachfolgenden Ziele. Beginne unmittelbar nach
bestätigter Planneranlage das private `devteam/setup.md` aus der
[Protokollvorlage](../templates/setup-record.md) (Verzeichnis 0700, Datei 0600);
protokolliere weitere Änderungen fortlaufend, nicht erst nach allen Integrationen.

Prüfe unmittelbar nach Create und erneut bei Wiederaufnahme den tatsächlichen Aktivierungsstand:
Ist das Plannerprofil bereits hot-admittiert, diese frühe Multiplexerwirkung im
Setuprecord festhalten, nicht erst Abschnitt 7 als Aktivierungsbeginn ausgeben.
Bis zu vollständigen angenommenen Rollen-/Skill-/Policy-/Bindingdateien und ihrer
effektiven Aufnahme keine Home-/Dialogoperation oder Aufgabenbearbeitung anstoßen.
Kann diese Grenze im bestehenden Owner nicht eingehalten werden, Setup anhalten
und einen freigegebenen profilbezogenen nativen Weg klären; andere Profile nicht
global abschalten. Vor späteren Nachrichten auch beim bereits bedienten Planner
die neuen Rollen und das effektive Adapterrouting erneut nachweisen.

Lies nur relevante nichtgeheime Felder zurück. Prüfe konkurrierende Env-/YAML-,
Session-/per-Modell- und CLI-Overrides, Fallbacks sowie benötigte Hilfsmodellrouten.
Eine gespeicherte Warnung/Schlüsselannahme beweist keinen Leser. Native Login-
und Modellwahl im richtigen Profil; echte Workerroute erst bei Einzelabnahme.

## 4. Eigenes Board und Team-Codex

Nur bei fehlendem eigenem Board und bestätigter Identität:

```sh
hermes kanban boards create "$BOARD" --name "$PROJECT_NAME" --default-workdir "$PROJECT_DIR"
hermes kanban boards list --json
```

Vergleiche Board-ID, Namen und Standardworkspace. Speichere die rückgelesene
Boardkennung identisch als `BOARD` und `KANBAN_BOARD_NAME`, mit Beleg im Record.
Jede spätere Operation trägt
`--board "$BOARD"`; keine globale Boardumschaltung. Repository, Branch und
Planrevision werden bei jedem Auftrag neu gebunden, nicht im Setup erfunden.

Binde im Coderhome `devteam/codex-home` und `devteam/user-home` anhand
[Team-Codex-Rezept](integrations.md#team-codex), dann vollständige Original-
Integrationen bereitstellen. Halte die realen Codex-Binary-/Homewerte für die anschließende
Bindungsersetzung fest. Originalkomponenten zunächst bereitstellen/konfigurieren;
die in den Rezepten beschriebenen echten Einzelprüfungen folgen erst nach
vollständigen eigenen Rollen-/Bindingdateien und ihrer Annahme in Abschnitt 7.
Lade das vollständige [Codeanalyserezept](code-analysis.md) und verwende genau
den gewählten Weg für alle drei Hermes-Rollen und Team-Codex. Ziele, vollständige
Originaldateimengen, Runtime und Lizenzen zurücklesen. G2/A01-CBM bleibt bis zum
genehmigten Originaloutput-/Bytevergleich offen; statische Ableitung genügt nicht.
Erster Index-/Query-/Änderungsnachweis erst im separat genehmigten Testworkspace.
Vor aktiver MCP-/Hookaufnahme auch bei hot-admittierten Profilen den tatsächlichen
Test-CWD und MCP-Root binden; ohne Freigabe/Testbindung nur außerhalb aktiver
Integration vorbereiten. Produktroots erst mit späterem Projektauftrag aktivieren.
Keine Produktanalyse und kein stiller Wechsel zur anderen Alternative.

## 5. Hindsight und Mattermost

Führe [Hindsight](integrations.md#hindsight) für jede Rolle am vorhandenen Dienst
mit derselben bestätigten **neuen** Projektbank aus. Danach folgt ausschließlich
im Plannerprofil die [geführte Mattermost-Anbindung](integrations.md#mattermost).
Zunächst Verbindungskonfiguration, Mitgliedschaft, menschliche Zulassung und zwei
getrennte Kanalidentitäten anhand der Kanalmetadaten für die Bindungsersetzung
bestätigen, ohne eine Nachricht an den Planner zu benötigen. Die geführte Mattermost-
Rezeptphase 8 (Homebindung und Dialogtests) wartet auf die vollständige
Annahme und Rücklese aus Abschnitt 6 sowie den profilrichtigen Adapternachweis in
Abschnitt 7. Andere bereits berechtigte Gesprächswege bleiben nutzbar. Kommunikationswerte gehören
nicht in gemeinsame Projektanweisungen oder die SOULs.

## 6. Eigene Dateien, Policy und getesteter Textweg

Führe das nach Planneranlage begonnene private Protokoll aus
[setup-record.md](../templates/setup-record.md) unter dessen `devteam/setup.md` fort.
Verzeichnis nur für den Besitzer (0700), Record 0600; nicht im Produktprojekt,
Git oder Makerbaum. Vorher keine bestehende eigene Protokolldatei überschreiben.
Trage pro erfolgreichem Schritt native Identität, genaue eigene Dateipfade,
Vorherzustand/Hash, geprüften Zustand und nächste Voraussetzung ein.

Speichere bestätigte Rohwerte verlustfrei im einzigen `json`-Block der Recordvorlage,
nicht durch Rückgewinnung aus Markdowntabellen. `confirmed_values` enthält die
bestätigten Setupwerte; `confirmed_bindings` die bereits aufgelösten Bindungswerte.
Fehlende Werte nicht erfinden. Die Tabellen halten Annahme-/Rücklesebelege; JSON
trägt die unveränderten nichtgeheimen Daten. Das folgende reine Pythonfragment
erzeugt nur Text aus `record_template_text` (bei Fortsetzung: bisheriger Record):

```python
import json
record_head, record_json = record_template_text.split("```json\n", 1)
_, record_tail = record_json.split("\n```", 1)
record_text = record_head + "```json\n" + json.dumps(
    {"confirmed_values": confirmed_values, "confirmed_bindings": confirmed_bindings},
    ensure_ascii=True, indent=2,
) + "\n```" + record_tail
```

Schreibe `record_text` ausschließlich im genehmigten Zielsetup mit den Dateitools
an das bestätigte eigene Recordziel und lies es bytegenau als `record_readback_text`
zurück. Für Rücklese und spätere Wiederaufnahme gilt dasselbe reine Fragment:

```python
import json
record_data = json.loads(record_readback_text.split("```json\n", 1)[1].split("\n```", 1)[0])
confirmed_values = record_data["confirmed_values"]
confirmed_bindings = record_data["confirmed_bindings"]
```

Werte gegen den bestätigten Datensatz und bei Resume gegen native Objekte prüfen.
Unvollständiges/ungültiges JSON oder widersprüchliche Tabellen/Belege halten an.
Die Pakettests führen nur diese Textfragmente und das folgende Renderfragment mit
synthetischen Daten in Scratch aus, keine Zielanlage oder Runtime.

1. Kopiere je `own_skills.targets` im [Manifest](../../manifest.json) **den ganzen
   eigenen Skillbaum** in `<Rollenhome>/skills/<name>/`; Team-Codex bekommt
   `screenshot-to-code` in seinem Prozess-HOME unter `.agents/skills/`.
   Nur `SKILL.md.template` wird zu `SKILL.md`. Screenshot bleibt bytegleich.
   Lizenzen, Notices und Referenzen gehören dazu. Keine Discovery im Quellprofil.
2. Erstelle aus [model-policy.md](../templates/model-policy.md) eine ausgefüllte
   nichtgeheime Policy je Rollenhome unter `devteam/model-policy.md`. Fülle die
   tatsächlichen Hermes-/Codex-Auswahlen, erlaubten höheren Routen, Hilfsmodelle,
   Original-Agentpins und Freigabe-/Prüfbelege aus. Alle Rollen erhalten dieselbe
   bestätigte Policyrevision, mit lokal erreichbarem Pfad. Die bereits bestätigte
   Codex-Modell-ID bleibt in technischer Auswahl/Policy, nicht in der SOUL.
   Vor jedem Aufruf liest der Coder die aktuelle lokale Policy und tatsächliche
   freigegebene Team-Codex-Konfiguration; bei Widerspruch anhalten. Modelländerungen
   erfolgen über den vorhandenen Policy-/Konfigurationsweg ohne SOUL-Re-Render;
   keine private Quellmodellbindung übernehmen oder neue Modellfrage hinzufügen.
   Unbestätigte Felder bleiben ausdrücklich offen und sperren betroffene Nutzung.
   Übernimm die feste Team-Codex-Auftragsregel unverändert: `$caveman` ausdrücklich
   in jedem neuen Auftrag, auch nach Neustart/Resume. Sie gehört in jede ausgegebene
   lokale Policy, nicht nur in den Makertext oder einen einmaligen Testauftrag.
   Fülle auch den Codeanalyseabschnitt: genau eine Auswahl, Originalskill-Ladepflicht
   in jedem Analyseauftrag/Resume, Corpus/Roots und Nachführungsweg aus dem
   [Analyserezept](code-analysis.md). Nicht gewählte Anweisungsvariante entfernen;
   alle drei Rollen bekommen dieselbe Auswahl, Codex den entsprechenden Auftrag.
3. Erstelle je Rollenhome `devteam/g1.md`: Zielrevision, geprüfter Retrypfad,
   Status und konkrete fehlende Voraussetzung; bei Lösung endliches natives
   Gesamtbudget samt Beleg, bei Anforderungsänderung deren Annahmequelle/Umfang.
   Keine Statusanhebung aus einem Cooldown. Bindungsfeld `G1_EVIDENCE` zeigt auf
   diese tatsächlich geschriebene erreichbare Datei.
4. Verwende **denselben reinen Textweg wie die Pakettests**:
   [references/render_text.py](../../references/render_text.py). Er liest/schreibt keine Dateien,
   lädt keine Runtime und hat keinen CLI-Einstieg. Lade das Modul im freigegebenen
   Zielsetup über den absoluten Pfad des geprüften Makerpakets (z. B.
   `importlib.util.spec_from_file_location`), nicht aus einem fremden gleichnamigen
   Modul im Suchpfad. Lies die Vorlagen mit dem Dateitool in UTF-8 und übergib Strings:

   ```python
   own_name = {"planner": "PLANER_NAME", "coder": "CODER_NAME", "reviewer": "REVIEWER_NAME"}[role]
   role_source = {**confirmed_values, "ROLE_NAME": confirmed_values[own_name]}
   fields = role_fields(role_template_text, role)
   if fields != set(role_manifest["render_fields"]):
       raise ValueError("Vorlage und deklarierte Rollenfelder widersprechen sich")
   role_values = {field: role_source[field] for field in fields}
   soul_text = render_role(role_template_text, role_values, role)
   binding_text = render_bindings(binding_template_text, confirmed_bindings, role)
   ```

   `confirmed_values` sind die bestätigten Rohwerte aus dem Setuprecord (Namen,
   Projekt, Bank, rückgelesenes Board und technische Profil-IDs; die für die Policy
   gespeicherte Codex-Modell-ID wird nicht als Rollenfeld übergeben);
   `role_manifest` ist der passende Eintrag aus `role_templates`. Fehlende Werte
   stoppen die Ausgabe, keine Leerdefaults und keine neuen IDs erfinden.
   `ROLE_NAME` entspricht stets dem eigenen Anzeigenamen, nie der technischen ID.
   `role` ist `planner`, `coder` oder `reviewer`; `confirmed_bindings` enthält exakt
   die 14 Felder aus [team-bindings.md](../templates/skills/devteam-workflow/references/team-bindings.md),
   einschließlich aller Kommunikationswerte zur Validierung. Das Modul entfernt
   den vollständigen Nur-Planner-Abschnitt für Coder/Reviewer. Verwende technische
   Werte unverändert als Daten, nicht die maskierte Markdownfassung als Shellwerte.
5. Der Textweg validiert den [Rollenfeldvertrag](native-workflow.md): nichtleere
   einzeilige Rohwerte, Namen maximal 120 Zeichen, keine Steuer-/Formatzeichen,
   Templateklammern, Einrückung, Backticks, Backslashes oder Fence-Ausbrüche.
   Er ersetzt alle passenden Mehrfachvorkommen genau in einem Durchlauf, ohne
   rekursive Auswertung. Normaler Markdown wird maskiert; Inlinecode und fenced
   Prozess-/Beispieltext erhalten rohe validierte Werte, keine Markdownbackslashes
   in nativen IDs, Bank oder Pfad. Unbekannte, fehlende,
   zusätzliche oder beschädigte Felder sind Fehler. Sämtliche Nichtplatzhalterbytes
   bleiben unverändert; keine zusätzliche Persona oder Prozessneufassung anhängen.
6. Zeige die personalisierten Rollen zur Annahme. Schreibe erst danach `soul_text`
   nach `<jeweiliger Rollenhome>/SOUL.md` und `binding_text` nach
   `<jeweiliger Rollenhome>/skills/devteam-workflow/references/team-bindings.md`.
   Bestätige Dateiziel und Eigentum direkt vor dem Schreiben; nutze Dateitools,
   keine Shellinterpolation oder rekursives globales Suchen/Ersetzen. Eine von
   Create frisch erzeugte neutrale SOUL nur nach dokumentiertem Vergleich gezielt
   ersetzen; fremde/geänderte Zieltexte anhalten.
7. Lies jedes Ziel zurück: exakte Rollenzuordnung, vollständige Ausgabe, keine Restfelder,
   bytegleiche Übereinstimmung mit `soul_text` und `binding_text`, unveränderte
   Nichtplatzhalterbytes jeder Rolle, keine Kommunikationswerte in Coder/Reviewer,
   Rollen-/Projekt-/Bank-/Boardwerte und technische IDs gegen den Record,
   vorhandene zugängliche Policy/G1-Dateien. Vergleiche Skilldateimenge und Bytes
   mit Quelle, abzüglich exakt der dokumentierten Umbenennung/Bindingersetzung.
   Öffne insbesondere die über MODEL_POLICY_REF gebundene lokale Policy im Coderhome
   und lies die tatsächlich geschriebene Auftragsregel zurück: `$caveman` in
   jedem neuen Auftrag, auch nach Neustart/Resume. Fehlt sie oder zeigt die Bindung
   auf eine andere Datei, vor Codex-Nutzung korrigieren; Zielpfad/Policyrevision und
   Rücklesebeleg im Setuprecord festhalten. Dies ist noch kein B01-Modusnachweis.
   Lies den tatsächlich geschriebenen Codeanalyseabschnitt ebenfalls zurück:
   gewählte Alternative, Originalskill-Ladepflicht nach Resume und Indexstand-/
   Corpusprüfung müssen für alle Rollen erreichbar sein; Coder übergibt sie an
   Team-Codex. Keine zweite Alternative und keine bloße Makerreferenz belassen.
   Vor Home-/Dialog-/Aufgabenbearbeitung Loader-/Kontextgrenze am Ziel lesen und **vollständige effektive
   SOUL-Aufnahme** pro Rolle nachweisen; Länge und Dateiexistenz genügen nicht.
   Bei Kürzung halten, keine Rollenpflichten still reduzieren.

## 7. Einzelprüfungen und Wake vor Ticketfreigabe

Nach vollständigen angenommenen Rollen-/Skill-/Policy-/Bindingdateien die
geplanten profilrichtigen Einzelprüfungen aus den Integrationsrezepten ausführen:
Discovery, vollständige Promptaufnahme, Modelle, persistente Modi und Memory.
Für die gewählte Analyse die [Funktions-/Updateprüfung](code-analysis.md) im
separaten Testworkspace durchführen; CBM-MCP und beide Harness-Hookwege getrennt
belegen. G2-Originaloutputvergleich ist eine eigene vorherige Freigabe, kein
Nebenprodukt des Indexlaufs. A01-CBM und R1 bleiben ohne jeweilige Belege offen.
Für Mattermost Rezeptphase 8 einhalten: Planneradapter nachweisen, dann Homebindung
im DM setzen/rücklesen, danach Erwähnung/Free-Response/DM prüfen. Frühere
Hot-Admission ersetzt weder Rollenaufnahme noch Adapternachweis.
Laufzeitbelege nur im separat freigegebenen
Umfang; offene Kriterien halten die betroffene Fähigkeit gesperrt.

Alltagsrezepte bleiben im installierten `devteam-workflow`. Für die separat
freigegebene Testkarte wie für spätere Karten: blocked-first anlegen, vollständige
Kette binden, **vor Freigabe** die native Subscription setzen. `PLANNER`, `BOARD`,
`TASK` und IDs stammen aus tatsächlichen bestätigten Zielobjekten. Öffentliches
Mattermost `O` → `channel`, privates `P` → `group`; DM ist kein Wakeziel.

```sh
hermes -p "$PLANNER" kanban --board "$BOARD" notify-subscribe "$TASK" \
  --platform mattermost --chat-id "$PROJECT_CHANNEL_ID" \
  --chat-type "$PROJECT_CHAT_TYPE" --user-id "$HUMAN_USER_ID" \
  --notifier-profile "$PLANNER" --delivery-mode wake
hermes -p "$PLANNER" kanban --board "$BOARD" notify-list "$TASK" --json
```

Lies **alle** Subscriptions der Karte zurück: Board/Task, Projektkanal, Chattyp,
berechtigter Mensch, Plannerprofil, `delivery_mode=wake`, ungebundene Subscription-
Thread-ID und keine widersprechenden Herkunftsbindungen. Das ist keine besondere
Threadvorgabe für normale Antworten. Auto-Subscribe=false entfernt alte Zeilen
nicht. Re-Subscribe ersetzt einen gefüllten falschen Profilstempel nicht zuverlässig.
Ersetze eine eigene falsch gestempelte Subscription nach Änderungsfreigabe durch natives Unsubscribe und Neuanlage.
Nutze dabei die aktuelle native Unsubscribe-Syntax und exakte eigene Zeilenidentität;
fremde Subscriptions anhalten/klären. Der Eventcursor beginnt beim Subscribe,
also nicht erst nach Abschluss abonnieren.

Vor jeder betroffenen automatischen Dispatchfreigabe G1 und vollständige
Bindungs-/Kettenrücklese prüfen. Keine manuelle Ersatzpipeline, um G1 zu umgehen.
Erst wenn freigegeben: echten Dispatcher-/Codex-/Reviewweg im separaten Testworkspace
prüfen; tatsächliche Task/Run/Commit-/Eventdaten, Plannerbearbeitung und veröffentlichte
Projektkanalnachricht belegen. `queued`/`scheduled` ist nicht zugestellt. Wakes
veranlassen erneutes Lesen von Plan und Board, nicht pauschal „alles fertig“.

## 8. Teilfortsetzung, Rückwege und Übergabe

Lies native Objekte erneut und setze am ersten offenen Gate fort.
Lade zuvor die bestätigten Rohwerte und Annahmebelege aus `devteam/setup.md`
(bzw. dem übergebenen Datensatz vor Planneranlage). Namen/Projekt/Bank/Board
nicht neu erfragen, technische Profil-IDs und `CODEX_MODEL` nicht neu ableiten.
Verwende den JSON-Rückleseweg aus Abschnitt 6, keine Markdownmaskierungen als Rohwerte.
Gleiche native Identitäten, Zielkonto-Home/Workspace, Modellpolicy und die zuletzt
geschriebenen SOUL-Bytes mit dem Record ab. Bei Drift vor erneutem Rendern oder
Schreiben klären; nur fehlende Werte bestätigen lassen.
Der Setuprecord ist Nachweis, keine zweite Zustandsautorität. Nach jedem Fehler
bewahre letzte erfolgreiche Phase, genaue eigene Objekte, fehlende Voraussetzung,
benötigte Maßnahme und Erfolgssignal. Folgende Fälle gehören zum Verfahren:

| Fall | Erhaltener Teilstand | Nächste Voraussetzung / Erfolgssignal | Gezielter Rückweg |
|---|---|---|---|
| Fremder Rollen-/Bank-/Boardname | Alle vorhandenen Objekte | Eigentum belegen oder neue Kennung bestätigen; native eindeutige Rücklese | Keine fremde Anlage ändern/löschen |
| Halbfertiges eigenes Setup | Bereits belegte Profile, Board, Bank, Quellen und Hashes | Drift mit nativen Objekten abgleichen; erstes offenes Gate erfolgreich prüfen | Nur dokumentierte eigene Dateiversion/Configeinträge zurücknehmen |
| PM-Wirkung nicht freigegeben | Bezogene Quellen außerhalb Discovery | Gemeinsamen Scope genehmigen; neue Generation und bestehende Profile verifizieren | Eigene Pluginaufnahme nativ zurücknehmen, keine gemeinsame Runtime entfernen |
| Hindsight/Mattermost unerreichbar | Profile, gerenderte Dateien, vorhandene eigene Bank/Kanal | Betreiber stellt Verbindung/Zugang bereit; profilrichtiger echter Request/Dialog gelingt | Nur eigene Verbindungs-/Aktivierungseinträge zurücksetzen, Bank/Kanal erhalten |
| Original-Modellpin fehlt | Unveränderte sechs TOMLs und sonstige Einrichtung | Autorisierter geeigneter Zugang; tatsächlicher Call je Helfer | Keine Pins umschreiben, betroffene Fähigkeit offen halten |
| Persönliche Codex-Skillwurzel wirksam | Persönliche Ausstattung unangetastet | Doppelbindung und echte Workerauflösung korrigieren; Teamroots nachweisen | Nur eigene Prozessbindung/Skillkopien zurücknehmen |
| Falscher Wake-Owner | Karte blocked, Arbeitsstand erhalten | Eigene Subscription korrekt neu anlegen und nachlesen | Nur exakte zugeordnete Subscription nativ entfernen |
| G1 offen | Gesamte geprüfte statische Einrichtung | Native endliche Gesamtgrenze oder angenommene Anforderungsänderung | Karten blockiert lassen, keine Retryplattform |

Erhalte vorhandene Teilstände; ein unerreichbarer Dienst ist kein Auftrag für einen Ersatzserver.
Vor Rückbau Aktivierung eigener Plugins/Adapter profilbezogen nativ beenden,
wenn nötig und freigegeben. Nur protokollierte eigene `SOUL.md`, Skillkopien,
`devteam/model-policy.md`, `devteam/g1.md`, Config-/Autoload-/Hookeinträge und
Subscriptions gezielt zurücksetzen. Gemeinsame Binaries, PM-Generationen, andere
Profile, persönliche Codexdaten, Projektregeln und Graphcaches erhalten.
Profil-/Board-/Bank-/Kanal-/Sessionlöschung braucht **gesonderte Datenlöschfreigabe**,
auch wenn die Anlage diesem Setup gehört. Rücklese beweist den Rückweg.

Übergebe Versionen, tatsächlich bestandene A-/B-Kriterien, Belegorte und offene
Blocker. Bei fehlenden Zielnachweisen bleibt „Paket geprüft; Setup-Laufzeitabnahme
offen“. Ein technisches Team ist noch kein fachlich eingearbeitetes Projektteam.

## Versionsgebundene Quellen

[Profile](https://hermes-agent.nousresearch.com/docs/reference/profile-commands),
[Konfiguration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration),
[PM](https://hermes-agent.nousresearch.com/docs/reference/package-management),
[Multi-Profile-Gateways](https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways),
[Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban).
Statische Rechercheanker: Hermes `d923a5eb487a17c0a68801bba9ef0f56c81040a8`
und Upstream `9e01b44dd23978f9ff40b7837467f3a9f1582130`; insbesondere
`hermes_cli/profiles.py`, `profile_model_seed.py`, `config.py`, `kanban_parser.py`,
`kanban_db_dispatch.py`, `kanban_db_notify.py`, `pm/plugins_state.py`,
`pm/workspace.py`, `hermes_bootstrap.py`. Kein CLI-/Laufzeitbeleg aus diesen Quellen.
