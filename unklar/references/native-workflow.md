# Native Workflowbindungen einrichten und prüfen

## Eigentum der technischen Details

Der Maker richtet Bindungen ein; der vollständig mitinstallierte
[devteam-workflow](../templates/skills/devteam-workflow/SKILL.md.template) besitzt
alle laufenden Rezepte für Tickets, Kettenfreigabe, Review, Rückgabe und Wake.
Seine [native Referenz](../templates/skills/devteam-workflow/references/native-contracts.md)
ist die einzige technische Alltagsanleitung. Rollen-SOULs binden die Rollenpflichten
und rollenbezogene Beispiele. Verbindliche native Syntax und Zielbindung
werden zusätzlich gegen den installierten Workflow und Zielstand geprüft.

Dieses Dokument ist der T2-Vertrag für Rollenautorenschaft (T3) und Setup (T4),
kein vollständiger Setupguide. Fremdkomponentenbezug und übrige Integration bleiben
separate Paketaufgaben. Hier entstehen weder Profile noch Dienstobjekte.

## Vollständige eigene Bäume bereitstellen

Rollenmatrix und tatsächliche Dateien aus [manifest.json](../../manifest.json) lesen.
Je Zielskill **alle** Dateien seines Baums einschließlich eigener Lizenz/Notices
kopieren. Nur `SKILL.md.template` wird am bestätigten Ziel zu `SKILL.md` umbenannt.
Die native Suche prüft den exakten Namen `SKILL.md`; der Transportname ist nach
statischer Resolverprüfung kein aktiver Einstieg. Das ersetzt keine spätere echte
Discoveryprüfung. Screenshot bleibt vollständig bytegleich, auch seine Referenzen
und Lizenz; keine Bindingersetzung in diesem Baum.

Die fünf Skill-Neufassungen brauchen keine historischen Quellprofile. Innerhalb
der Skillbäume enthält ausschließlich
[team-bindings.md](../templates/skills/devteam-workflow/references/team-bindings.md)
zu rendernde Setupfelder. Sie liegt danach im jeweiligen installierten
Workflowskill unter `references/team-bindings.md`. Der Alltag lädt keine Datei
aus dem Makerpaket. Der Maker stellt die lokalen Bindungen für alle Rollen bereit.
Die quellnahen Rollen-SOULs haben zusätzlich die unten deklarierten Felder;
übereinstimmende technische Werte stammen stets aus demselben Setupdatensatz.

## Rollen-SOULs — Render- und Kontextvertrag für T4

Das Manifest liefert genau drei `role_templates`: [Planner](../../templates/roles/planner.SOUL.md.template),
[Coder](../../templates/roles/coder.SOUL.md.template) und [Reviewer](../../templates/roles/reviewer.SOUL.md.template).
Produzent ist der Maker im ausdrücklich freigegebenen Zielsetup. Er ordnet die
Vorlage dem bestätigten technischen Rollenprofil zu und schreibt die gerenderte
Fassung dort als `SOUL.md`; dieser Transportname ist kein aktueller
Installationsauftrag. Keine neue globale SOUL, keine Übernahme eines Quellprofils
und keine SOUL-Installation in Team-Codex. Bestehende fremde Zieldateien nicht
überschreiben; bei Wiederaufnahme nur eindeutig zu diesem Setup gehörende Stände
nach Abgleich weiterverwenden.

| Feld | Inhalt / Herkunft | Ziel / Verbraucher |
|---|---|---|
| `ROLE_NAME` | Eigener bestätigter Anzeigename: Planner = `PLANER_NAME`, Coder = `CODER_NAME`, Reviewer = `REVIEWER_NAME` | Alle Vorkommen der jeweiligen Rollen-SOUL |
| `PLANER_NAME` | Bestätigter Planner-Anzeigename; genau ein N in PLANER | Rollenbezüge und Prozessdarstellung, nicht technische Profil-ID |
| `CODER_NAME` | Bestätigter Coder-Anzeigename | Rollenbezüge und Prozessdarstellung |
| `REVIEWER_NAME` | Bestätigter Reviewer-Anzeigename | Rollenbezüge, soweit in der Vorlage vorhanden |
| `PROJECT_NAME` | Bestätigter Projektname, einzelnes Pfadsegment ohne Traversal | Projektbezug; Reviewerpfad fest `~/projects/<PROJECT_NAME>` |
| `HINDSIGHT_BANK_NAME` | Bestätigte eigene Projektbank, gegen Dienstobjekt geprüft | Alle Bankvorkommen, identisch zur nativen Memorybindung |
| `KANBAN_BOARD_NAME` | Tatsächliche Boardkennung aus nativer Rücklese, identisch zu `BOARD`, nicht Board-Anzeigetitel | Projekt-/Boardbezug |
| `CODER_PROFILE` | Bereits bestätigte technische Coderprofilkennung | Nur Planner: technischer Assignee, kein Anzeigename |
| `REVIEWER_PROFILE` | Bereits bestätigte technische Reviewerprofilkennung | Planner/Coder: technischer Reviewer/Handoff, kein Anzeigename |

Je Rolle nur die tatsächlich vorkommenden Felder aus `render_fields` übergeben;
alle passenden Mehrfachvorkommen ersetzen. `role_fields(template, role)` prüft die
zulässige rollenbezogene Feldmenge vor der Auswahl, `render_role(template, values,
role)` lehnt fehlende, zusätzliche, unbekannte und beschädigte Felder ab. Der Maker
setzt `ROLE_NAME` aus dem eigenen bestätigten Anzeigenamen; wenn dessen benanntes
Feld ebenfalls vorkommt, prüft der Renderer die Gleichheit zusätzlich. Anzeigenamen
und Profil-IDs bleiben getrennt, auch wenn sie zufällig gleich heißen. Kein
`ROLE_PERSONA`: Die Rollen verwenden feste Texte, ohne Persona-Abfrage oder Anhang.

Werte nicht trimmen oder umbenennen: nichtleerer einzeiliger Klartext, Rollennamen
höchstens 120 Zeichen, keine Steuer-/Formatzeichen oder Templateklammern. Führendes/
abschließendes Whitespace und führende Bindestriche ablehnen, ebenso Backticks,
Backslashes und dreifache Tilden (Code-/Fence-Ausbruch). Profil-IDs folgen
`[a-z0-9][a-z0-9_-]{0,63}`; Bank-/Boardwerte müssen der sicheren Syntax
`[A-Za-z0-9][A-Za-z0-9_.:/-]*` entsprechen. Das ist eine Textsicherheitsprüfung,
keine native Existenz-/Verfügbarkeitsprüfung.
Projektname darf weder Slash/Backslash noch `.` oder `..` als ganzen Wert enthalten.
Den tatsächlichen absoluten Workspace auf dem Zielkonto vor Anlage mit dem festen
Reviewerpfad abgleichen; Abweichung mit dem Nutzer klären, keine neue Pfadpolicy.

Normaler Markdown/HTML wird als Text maskiert; Inlinecode und fenced Prozesstext
sowie technische Beispielargumente erhalten unveränderte validierte Rohwerte.
Markdownbackslashes dürfen keine Bank-, Board-, Profil-ID oder Pfade
verfälschen. Keine rekursive Ersetzung; sämtliche Nichtplatzhalterbytes bleiben
unverändert. Die quellnahen Rollen besitzen eigene Strukturen, keinen erzwungenen
identischen neunstufigen Prozess. Planner berichtet dem Kunden; Coder und Reviewer
berichten dem Planner. Die portable Plannerregel erlaubt bis zu drei eigenständig
entschiedene Budgeterweiterungen im beschriebenen Ticketkontext; sie löst nicht das separate
native Rate-Limit-Gesamtbudget-Gate G1.

Der [Setupweg](../../references/setup.md) führt Eingang → Bestätigung → privaten Record →
Wiederaufnahme/Abgleich → rollenbezogene Feldauswahl → `render_role` → Annahme →
Schreiben ins bestätigte Rollenhome als `SOUL.md` → bytegenaue Rücklese aus.
Tests verwenden ausschließlich synthetische Daten und öffentliche Vorlagen;
private Quell-SOULs sind keine Testabhängigkeit und kein Installationsziel.

### Kontext und Fähigkeiten — keine implizite Versorgung

- Vor Nutzung je Rolle den vollständigen installierten `devteam-workflow` samt
  `references/team-bindings.md` und `references/native-contracts.md` bereitstellen.
  Vor Teamaktionen diesen Skill ausdrücklich laden lassen. Relative Referenznamen beziehen sich auf
  dessen Skillwurzel, nicht auf die SOUL-Datei oder den Maker. Der technische
  Alltagsvertrag bleibt dort; SOUL-Beispiele müssen mit diesem Vertrag übereinstimmen.
- `MODEL_POLICY_REF` wird vom Setup erstellt oder als vorhandene bestätigte,
  erreichbare Policy gebunden. Hermes- und Codex-Auswahl samt erlaubten höheren
  Stufen stammen daraus. Vor jedem Codex-Aufruf liest der Coder die aktuelle lokale
  `devteam/model-policy.md` im eigenen Rollenhome und die tatsächliche freigegebene
  Team-Codex-Konfiguration; Widersprüche halten an. Die SOUL enthält keine Modell-ID.
  `CODEX_MODEL` und `CODEX_PROMPT_FILE` im Bashbeispiel sind sicher gequotete
  Laufzeitvariablen, keine Renderfelder. Modelländerungen folgen dem vorhandenen
  Policy-/Konfigurationsweg ohne SOUL-Re-Render und ohne neue Setupfrage.
  Kommunikationswerte bleiben ausschließlich beim Planner.
  Memorykonfiguration liegt im nativen Zielkontext; `HINDSIGHT_BANK_NAME` und
  Rollenfilter in der SOUL müssen dazu passen, Zugangsdaten bleiben außerhalb.
- Direkte Fähigkeiten gemäß `own_skills.targets` und `upstream_components.targets`
  im richtigen Harness bereitstellen. Erwähnung in einer SOUL ist kein Discovery-
  oder Aktivierungsnachweis. Bibliotheksregeln gelten auch beim Coder/Reviewer,
  obwohl ihre SOULs sie fachlich beschreiben statt jeden Skillnamen zu wiederholen.
  Codex erhält seine Arbeitsgrenzen vom Coder, keine zusätzliche Teamrolle.
- Projektregeln werden am tatsächlichen Auftrag ermittelt: geltende Root-`AGENTS.md`
  **und** alle anwendbaren Bereichs-`AGENTS.md` lesen. Bei einem Auftrag mit Root-
  und Bereichsdatei bleiben beide Geltungsbereiche erhalten; die Bereichsdatei
  ersetzt Root nicht pauschal. Der Coder übergibt Codex die verifizierten absoluten
  Pfade und ihre Geltung. Das Setup verändert oder erzeugt diese Projektregeln
  nicht nebenbei und legt keinen festen AGENTS-Pfad in der SOUL ab.
- Vor Aktivierung den Loader und seine tatsächliche Größen-/Kontextgrenze am
  Zielstand prüfen, nach Personalisierung die vollständige effektive Aufnahme
  aller drei SOULs separat nachweisen. UTF-8-Bytezahl, Zeichenanzahl, Dateiexistenz
  und Katalogtreffer sind kein solcher Nachweis. Bei Kürzung/fehlendem Kontext
  anhalten und klären, nicht still Rollenpflichten kürzen oder neue Ladewege
  erfinden. Dateitests ersetzen weder diese Prüfung noch unabhängigen Vorlagenreview.

## Bindungsfelder — Eingaben und Verbraucher

Werte aus echten nativen Zielobjekten ermitteln, vom Nutzer gewählten Scope
beachten und vor Ersetzung auf Kollision/Identität prüfen. Es sind Markdowndaten,
keine Shellfragmente: Werte mit Zeilenumbrüchen oder Steuerzeichen ablehnen,
Tabellentrenner geeignet maskieren, Pfade bei späteren Aufrufen korrekt quoten.
Den tatsächlichen Wert dabei nicht umbenennen. Das gerenderte Dokument zurücklesen;
keine unaufgelösten `{{…}}`-Felder zulassen. Niemals Token hineinschreiben.

| Feld | Inhalt / Herkunft | Verbraucher |
|---|---|---|
| `PLANNER_PROFILE` | Bestätigte technische Plannerprofilkennung, nicht Anzeigename | alle Rollen; Planner-Aufrufe und Notifier |
| `CODER_PROFILE` | Bestätigte technische Coderprofilkennung | alle Rollen; Assignee und Rückroutingprüfung |
| `REVIEWER_PROFILE` | Eigenständiges Reviewerprofil, verschieden vom Coder | alle Rollen; expliziter Handoff |
| `BOARD` | Tatsächliche Boardkennung aus nativer Rücklese | jede Boardaktion; niemals globaler Current-Board-Fallback |
| `PROJECT_DIR` | Absolutes vereinbartes Teamarbeitsverzeichnis | Terminalstart und Boarddefault; Ticket nennt zusätzlich seinen echten Repo-Checkout |
| `CODEX_PROCESS_HOME` | Eigener Team-Prozess-HOME für Codex | Coder bindet Aufruf; verhindert persönliche zusätzliche Skillwurzel im Teamkontext |
| `CODEX_HOME` | Eigener Teamzustand für Codex-Konfiguration/Sessions/Skills | Coder; separat von Prozess-HOME verifizieren |
| `CODEX_BINARY` | Tatsächlich aufgelöste geeignete CLI-Datei | Coder; keine angenommene Binary aus historischem PATH |
| `MODEL_POLICY_REF` | Im jeweiligen Rollenprofil erreichbarer nichtgeheimer Dateipfad zur bestätigten Modell-/Reasoning-/Risikopolicy; T4 erstellt oder verwendet sie | alle Rollen; aktuelle Hermes-/Codex-Routen und erlaubte höhere Stufen, keine Modell-ID in der SOUL |
| `G1_STATUS` | `open`, `verified-native-bound` oder `requirement-amended`; kein stiller Default auf erfüllt | alle Rollen vor betroffener automatischer Dispatchfreigabe |
| `G1_EVIDENCE` | Erreichbarer Beleg mit Zielrevision, tatsächlichem endlichem nativen Gesamtbudget; bei Änderung genaue Annahmequelle/Umfang, bei `open` konkrete offene Voraussetzung | alle Rollen; keine Erfolgsbehauptung aus Cooldown/Per-Run-Timeout |
| `PROJECT_CHANNEL_ID` | Echte Mattermost-Projektkanal-ID, getrennt von DM-Home/Bot/User | ausschließlich Planner-Wakes |
| `PROJECT_CHAT_TYPE` | `channel` öffentlich oder `group` privat, gegen Kanalobjekt geprüft | ausschließlich Planner-Wakes |
| `HUMAN_USER_ID` | Berechtigter menschlicher Mattermost-Nutzer | ausschließlich Planner-Wakes; nicht Bot-ID |

Den Abschnitt „Nur Planner“ beim Rendern für Coder und Reviewer vollständig
entfernen; dort keine Kommunikationswerte ablegen. Server, eigene Botidentität,
Token, DM-Home und Allowlists gehören in native Plannerkonfiguration, nicht in
eine gemeinsame Projekt-`HERMES.md`. Das private Zielsetup-Protokoll kann auf die
Bindungen verweisen, ist aber keine zweite Laufzeitzustandsautorität.

Repositorygrenzen, Branch, konkrete Planrevision, Task-/Run-/Event-IDs,
Idempotenzschlüssel und Prüfartefakte werden je Auftrag ermittelt. Sie sind keine
leeren Makerplatzhalter und werden nicht pauschal beim Setup erfunden. Der
konkrete Feature-Branch wird mit dem Nutzer je Repository vereinbart.

## Native Setupseite — nur nach gesonderter Zielautorisierung

Im realen Setup die aktuelle Zielversion und Schemas prüfen. Statische Grundlage
und Grenzen stehen in der nativen Referenz. Profile frisch und kollisionsbewusst
anlegen, nicht klonen. Create kann den Multiplexer benachrichtigen; Pluginaufnahme
kann gemeinsame PM-Eingaben ändern. Anlage/Aktivierung ist daher keine passive
Vorbereitung und braucht ihren konkreten freigegebenen Umfang.

Die folgenden Rezepte verbinden bereits bestätigte Werte, keine aktuellen
Paketbaubefehle. `PROFILE` wird nacheinander auf jede neue Rollenkennung gesetzt;
`PROJECT_NAME` ist der bestätigte Projektanzeigename.

```sh
hermes -p "$PROFILE" config set terminal.cwd "$PROJECT_DIR"
hermes -p "$PROFILE" config set kanban.auto_subscribe_on_create false
hermes -p "$PROFILE" config get terminal.cwd
hermes -p "$PROFILE" config get kanban.auto_subscribe_on_create
hermes kanban boards create "$BOARD" --name "$PROJECT_NAME" --default-workdir "$PROJECT_DIR"
hermes kanban boards list --json
```

Bei Wiederaufnahme vor Create auf vorhandene eindeutig eigene Objekte prüfen.
Keinen gemeinsamen Boardzeiger durch `boards switch` als vermeintliche
Profilbindung setzen. Board, Rollen und Startverzeichnis tatsächlich rücklesen.
Bestehende Subscriptions bleiben auch nach Abschalten von Auto-Subscribe zu prüfen.

Team-Codex-Binary und beide Homes aus dem echten Worker prüfen; `CODEX_HOME`
allein schließt die zusätzliche persönliche `$HOME/.agents/skills`-Wurzel nicht
aus. Anmeldung nur unterstützt und nutzerautorisiert, keine Credentialkopie.
Die Aufrufgestaltung bleibt beim installierten Hermes-`codex`-Skill und der
bestätigten Zielkonfiguration; kein zusätzlicher Wrapper in T2.

Mattermost normal über `hermes -p "$PLANNER" gateway setup` einrichten. Eigenen
Bot samt Mitgliedschaft, menschliche Zulassung, Projektkanal-Allowlist und
Free-Response sowie separate DM-Home-ID prüfen. Nur Planner kommuniziert über
diese Bindung. Den bedienten Adapter und korrekten Notifier-/Dispatcherbesitzer
feststellen; ein lebender Gatewayprozess beweist das konkrete Profilrouting nicht.

## Prüf- und Aktivierungsgrenzen

1. Vollständige eigene Bäume anhand Manifest und Rollenmatrix vergleichen;
   `SKILL.md` und benötigte Referenzen im tatsächlichen Zielharness auflösen.
   Pfade und Inhalte prüfen, nicht bloß alte Unterhaltung oder Dateiexistenz.
2. Gerenderte Arbeitsbindungen mit nativen Profil-/Board-/Workspaceobjekten
   abgleichen; Planner-Kommunikationsabschnitt nur im Plannerziel. Referenzierte
   Modellpolicy und G1-Belege müssen für die jeweilige Rolle zugänglich sein.
3. Native Request-Review-, Show-, Request-Changes-, Complete- und Wake-Schnittstellen
   am Ziel bestätigen; insbesondere Reviewer-Readback und echten Reviewclaim für
   Rückgabe. Native `archived`-Elternerfüllung darf die Reviewpflicht nicht umgehen.
4. **G1 hält vor betroffener automatischer Dispatchfreigabe an.** Die untersuchten
   Stände wiederholen Rate-Limits unbegrenzt; `max_retries`, Cooldown, einzelner
   Timeout, Promptbudget und ein beaufsichtigter Minitest lösen das nicht.
   Nur einen nachgewiesenen unterstützten nativen Weg oder ausdrücklich geänderte
   Anforderung dokumentieren. Kein eigener Retrydienst oder Corepatch.
5. Erst im separat freigegebenen Zielkontext echte Discovery, Modellwege, normale
   Kanal-/DM-Nachrichten, Wakezustellung und eine begrenzte unabhängige Pipeline
   prüfen. Auf queued/scheduled darf kein „zugestellt“ folgen. Paketdateitests
   sind weder Installation noch Agentenverhaltens- oder Laufzeitabnahme.

Offene G1-Kompatibilität bleibt konkret sichtbar; die übrigen Bindungen dürfen
vorbereitet werden, ohne unbeaufsichtigte Teamarbeit als freigegeben auszugeben.
