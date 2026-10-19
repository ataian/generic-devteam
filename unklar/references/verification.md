# Paketprüfung und gesonderte Zielabnahme

## Aussage und Voraussetzungen

Diese Anleitung trennt statische Autorenvorprüfung, unabhängigen Review des
unveränderlichen Kandidaten und echte Einrichtung. Eine grüne Suite ist **keine
Agentenverhaltensprüfung**, keine Discovery-/Promptaufnahmeprüfung und keine
Betriebsfreigabe. Das Paket ist wegen G1 und G2 nicht vollständig abgenommen.

Für die öffentliche Suite: Python **ab 3.11** (`tomllib` aus der Standardbibliothek),
vorhandenes `ruamel.yaml` für vollständiges sicheres YAML und `bash` für `bash -n`.
Nichts automatisch nachinstallieren. Einen vorhandenen passenden Interpreter
verwenden; sonst fehlende Voraussetzung melden. Die Autorenvorprüfung verwendete
Python 3.14.7. Konkrete Versionen bei jedem neuen Lauf selbst protokollieren.
Die Module nutzen nur Paketdateien, Standardbibliothek und den sicheren YAML-Parser.

Aus dem Paketroot, auch in einer separat exportierten Kopie ohne Buildrepository:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test*.py' -v
```

Temporäre Defektkopien entstehen außerhalb des Kandidaten unter dem vom Nutzer
bestimmten `TMPDIR` (sonst Standard-Tempverzeichnis des Interpreters). Der Bereich
muss beschreibbar sein. Die Suite verändert weder Zielprofile noch das Paket.
Alle Testmodule entdecken, nicht nur `test_package.py` starten.

## Was die öffentliche Suite tatsächlich prüft

- Exakte reguläre Dateimenge laut Manifest; keine Symlinks oder entweichenden
  Pfade. Nur Gitmetadaten (`.git/`, `.gitignore`) und die separate Vortragsbeilage
  `vortrag/` sind im Checkout vom Skillpaket ausgenommen. Rollen, sechs eigene Skillbäume und vollständige Fremdkomponentenmatrix
  werden gegen unabhängig festgelegte Sollmengen geprüft.
- YAML-Frontmatter als Mapping, sämtliche JSON-Dateien, Python einschließlich
  `.py.example` nur als AST; dokumentierte Shellblöcke nur per `bash -n`.
  Die beiden Codex-TOML-Beispiele werden mit `tomllib` geparst und auf MCP-Namen,
  Argumente, Env-Namen sowie beide Lifecycle-Hooks, Matcher, Commands,
  Windowsfeld und Timeout geprüft. Kein Hook wird ausgeführt.
- Relative Links innerhalb des Exports und separat installierbarer Skillbäume,
  Transportnamen, vollständige Lizenzen/Notices gemäß Manifest, Screenshotmenge
  und gespeicherte kanonische SHA-256. Fremdassets sind Bezugsrezepte, keine Kopien.
- Deklarierte Rollen-/Bindingfelder und deren Eigentümer; unbekannte oder defekte
  Templatefelder sind Fehler. Das reine `render_text.py` wird als einziges
  Nichttestmodul importiert. Echte Rollentemplates werden mit mehrfachen Feldern,
  Anzeigenamen ungleich Profil-IDs, Projekt/Bank/Boardwerten sowie Inline-/
  Absatzmarkern und Einrückung geprüft. Abgelehnte Eingaben werden nicht
  still normalisiert; Nichtplatzhalterbytes und rohe technische Pfadwerte bleiben
  erhalten. Kommunikationsausgabe bleibt ausschließlich beim Planner.
  Die tatsächlich ausgelieferten reinen Setup-Pythonfragmente befüllen die echte
  Recordvorlage per JSON und lesen synthetische Rohwerte verlustfrei aus Scratch
  zurück. Das Original-Renderfragment wird ausgeführt; Mutationen der Coder-
  Namenszuordnung und Alias-/Profilzuordnung müssen an benannten Assertions scheitern.
  Modelländerungen über Policy/Konfiguration benötigen keinen SOUL-Re-Render;
  Ausgabe ohne konkrete Modell-ID und sicher gequotete Laufzeitvariablen prüfen.
- Bekannte private Pfad-, Token- und Runtime-Dateimuster in Lieferdaten;
  Pythonprüfer enthalten selbst Regexmuster und werden als Code zusätzlich gelesen.
  Quellteamidentitäten zusätzlich beim Exportreview ausschließen, ohne eine private
  Namensliste in öffentlichen Tests zu hinterlegen. Musterprüfung ist keine
  universelle Geheimniserkennung oder Lizenzprüfung.
- Synthetische [Setupfälle](../tests/fixtures/setup-cases.json) und
  [Zielkontext](../tests/fixtures/target-context.md): zwei Repositorys, Root- und
  Bereichsregeln, abweichende Rust-/Pythonwerkzeuge sowie Leerzeichen/Markdownzeichen
  im Workspacepfad bis zur tatsächlich gerenderten Teambindung.
- Reale Textentfernung in isolierten Kopien: Wiederaufnahmeabschnitt bei erhaltener
  Überschrift, Plan-vor-Ticket-Anweisung, Karten-/Kantenerhalt und unabhängiger
  Review vor Folgearbeit. Das operative Projektwerkzeugrezept darf nicht verschwinden,
  während nur Fixturelabels stehen bleiben. Der Rollenvertrag prüft die genehmigte
  Planner-Budgetgrenze und den Kundenabschluss ohne eigenmächtige Folgeprozesse.
- Fehlende Referenz, fehlende/zusätzliche Fremdkomponente, gültige aber falsche Rolle,
  entweichender Link sowie TOML-Syntax-/Datenmutationen müssen gezielt scheitern.
  Die Kandidatenhashes vor/nach den isolierten Negativkopien bleiben gleich.

Textvertragsprüfungen erkennen bestimmte entfernte Anweisungen; sie messen weder
Verständnis noch tatsächliche Entscheidungen eines Agenten. Ein unabhängiger Leser
bewertet die beschriebenen Handlungen pro Fall zusätzlich semantisch.

## A — Paketkriterien einzeln beurteilen

| Kriterium | Erforderlicher Nachweis / aktueller Paketstatus |
|---|---|
| A01 Vollständigkeit | Maker, Rollen, sechs eigene Fähigkeiten, Rollenmatrix und beide Quellenrezepte vorhanden. **Für CBM offen:** G2 erfordert freigegebenen isolierten Originalinstalleroutput, vollständiges Dateidelta, selektive Assetübernahme und Bytevergleich. Statische Literalableitung reicht nicht. |
| A02 Portabilität | Gesamte Suite in isoliertem öffentlichem Paketbaum, interne Unterlagen ausgeschlossen, Links/Dateimengen/Hashes geprüft; native Installation/Discovery davon getrennt. |
| A03 Beschlusskonsistenz | Rollen-/Git-/Modell-/Risikoregeln statisch vergleichen. **G1-Budgetanforderung unerfüllt** im untersuchten nativen Stand: Cooldown/max_retries belegen kein endliches Rate-Limit-Gesamtbudget. Halt vor betroffener automatischer Dispatchfreigabe; geeigneter unterstützter Zielstand oder ausdrückliche Anforderungsänderung erforderlich. |
| A04 Statische Qualität | Gesamte öffentliche Suite einschließlich Renderer und Negativkopien erfolgreich; Parser/Interpreter und unveränderliche Paketidentität festhalten. Dies ist keine native Funktionsprüfung. |
| A05 Nutzbarkeit | Einstieg, Voraussetzungen, Herkunft, Wiederaufnahme, Updates/Rückwege und Grenzen ohne private Quellen verständlich; nur Lieferdateien exportieren. |
| A06 Unabhängiger Review | **Gesamtpaketreview abgeschlossen:** Der eingefrorene Paketstand wurde unabhängig geprüft; die vorgemerkten Korrekturen sind geschlossen. Bei späteren Änderungen neuen Stand eindeutig identifizieren, betroffene Änderungen unabhängig prüfen und Checks wiederholen. Autorenvorprüfung und frühere Komponentenreviews allein ersetzen keinen Gesamtpaketreview. |

G3: Screenshot-Lizenz und Originalbytes sind erhalten; die fünf weiteren Skills
sind Neufassungen mit eigenen vollständigen Lizenzen. Aktuelle Rollen-SOULs sind
quellnahe Ableitungen bzw. die maßgebliche Nutzerfassung, siehe [NOTICE](../../NOTICE.md).
Historische ungeklärte Rechte werden dadurch nicht rückwirkend geklärt.

## B — echte Einrichtung, alle Kriterien weiterhin offen

Vor Beginn einen ausdrücklich freigegebenen Testkontext festlegen: neue eigene
Rollen/Bank/Board, Dienste, autorisierte Modellnutzung, Testworkspace, Projekt-/DM-
Kanäle, gemeinsame PM-/Gatewaywirkungen sowie numerisches Zeit-/Versuchsbudget.
G1 nicht durch einen beaufsichtigten Erfolgsdurchlauf als gelöst darstellen.

| Kriterium | Späterer echter Erfolgsnachweis |
|---|---|
| B01 Profile/Discovery | Rollenfähigkeiten und persistente Modi im tatsächlichen Worker-/Profilkontext laden; vollständige SOUL-Aufnahme belegen. Fremde Profile und persönliche Codex-Ausstattung vor/nach vergleichen. |
| B02 Modellzugänge | Reale begrenzte Calls für Hermes, Team-Codex und erforderliche Hilfspfade mit dem gewählten geeigneten Anbieter. Fehlende unveränderte Originalpins konkret blockieren. |
| B03 Codex | Effektives Team-HOME/CODEX_HOME und Skillroots, echte Implementierung sowie je ein begrenzter Delegationscall der sechs Originalhelfer; unveränderte Pins und tatsächliche Childdaten prüfen. |
| B04 Memory | Neue eigene Bank, automatische Einstellungen, tatsächliche Retain-/Recall-Requests und gespeicherte Tags; neutrale autorisierte Testmarker für Shared/eigene/fremde Rolle/ungetaggt. Reflect/Prefetch nur mit belegter Filterweitergabe. |
| B05 Mattermost | Botmitgliedschaft, berechtigter Mensch und getrennte Kanaltypen/IDs; Erwähnungsantwort, Free-Response, DM und normale Nachrichten praktisch prüfen. Wake gehört in den Projektkanal, nicht DM. |
| B06 Pipeline | Harmloser Auftrag im separaten Testrepo: Plan → getrennte Annahme → native Karte/Dispatcher → Codex-Artefakt, Tests, Commit → unabhängiger Review derselben Karte → korrelierter Planner-Wake und tatsächliche Projektkanalantwort. Kein künstlicher Fehler-/Reviewrücklauf nötig. |
| B07 Grenzen | Produktprojekt und fremden Zustand erhalten, genehmigtes Budget/Versuche erfassen, Pflichtnachweise einzeln ehrlich bewerten. Testdaten nur im freigegebenen Umfang zurücknehmen. |

Die [Integrationsrezepte](../../references/integrations.md), [Codeanalyse](code-analysis.md) und das
[Setup](../../references/setup.md) bestimmen die konkreten Zielprüfungen. Für den gewählten
Analyseweg echte Workspacebindung, Index, Symbol-/Relationsquery sowie Nachführung
nach einer autorisierten Änderung belegen; die nicht ausgeübte Alternative bleibt
hinsichtlich Laufzeit offen. Fachliches Projekt-Onboarding folgt separat.

## Freeze, unabhängiger Review und erst danach Finalexport

1. Lokalen Kandidaten gezielt committen; Commit und SHA-256 jeder Paketdatei
   protokollieren. Während des unabhängigen Reviews Paketbytes unverändert halten.
2. Review gegen die geltende Spezifikation samt offenen G1/G2 durchführen lassen.
   Korrekturen als neue Commits, betroffene Prüfungen wiederholen, neuen Freeze
   benennen. Kein Amend, kein automatischer Push und keine Gesamtfreigabe aus
   bestandenen Parserchecks.
3. **Erst nach Review** aus genau dieser Commitidentität nur den Paketbaum exportieren:

   ```sh
   git archive --format=zip --output="$ARCHIVE" "$REVIEWED_COMMIT:package/generic-devteam"
   ```

   `ARCHIVE` ist ein neuer Ausgabepfad außerhalb des Pakets, `REVIEWED_COMMIT` die
   tatsächlich geprüfte Identität. Bei einem eigenständigen öffentlichen Repository
   entfällt der Subtreezusatz; nie das interne Buildrepository vollständig exportieren.
4. Normalisierte Archivdateimenge mit `git ls-tree -r --name-only` desselben
   Commit-Subtrees vergleichen, CRC mit `zipfile.testzip()` prüfen und **jeden**
   Member byteweise gegen `git show <commit>:package/generic-devteam/<pfad>`
   vergleichen. Zusätzlich SHA-256 des Archivs festhalten.
5. Eine zuvor isoliert geprüfte öffentliche Datenkopie ist nur Exportvorprüfung,
   kein freigegebenes Finalarchiv. Finale Review-/Archividentität und A-/B-Urteile
   getrennt dokumentieren; offene Kriterien niemals pauschal als erledigt melden.
