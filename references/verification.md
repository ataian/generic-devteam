# Paketprüfung und Funktionsprüfung des Teams

Korrekte Paketdateien und ein funktionierendes Team sind zwei getrennte Ergebnisse.
Prüfe jeweils den aktuellen Stand und dokumentiere nur tatsächlich ausgeführte
Prüfungen. Frühere Reviews oder erfolgreiche Einzeltests gelten nicht automatisch
für eine geänderte Fassung.

## 1. Paket vor Verwendung prüfen

Diese Prüfungen benötigen weder eine Teaminstallation noch Modell- oder Dienstaufrufe.
Vorhandene geeignete Prüfwerkzeuge verwenden; fehlende Voraussetzungen konkret benennen.

- [ ] **Dateibestand:** Die Dateiliste in [manifest.json](../manifest.json) stimmt
  mit dem vorgesehenen Lieferumfang überein. Rollen, eigene Skills und benötigte
  Begleitdateien sind vorhanden; Arbeitsunterlagen gehören nicht zur Installation.
- [ ] **Verweise:** Relative Links und Zielanker funktionieren. Jeder kopierte
  Skill ist mit seinen eigenen Referenzen unabhängig vom Maker nutzbar. Das fertige
  Paket hat keine Abhängigkeiten auf den vorübergehenden Altbestand.
- [ ] **Vollständige Skills:** Dateimenge, Zielrollen und Lizenz-/Notice-Dateien
  stimmen mit der [Quellenübersicht](upstream-sources.md) überein. Eigene Skillbäume
  werden vollständig und unverändert kopiert.
- [ ] **SOUL-Personalisierung:** Die Rollenfelder aus dem Manifest passen zu den
  Vorlagen. Mit synthetischen Werten über [render_text.py](render_text.py) prüfen:
  alle Platzhalter ersetzt, übriger Inhalt erhalten, technische Kennungen nicht mit
  Anzeigenamen verwechselt; fehlende oder ungültige Werte werden abgewiesen.
- [ ] **Syntax:** JSON und vorhandene YAML-/TOML-Daten mit passenden Parsern prüfen,
  Pythonbeispiele als Syntaxbaum, Shellbeispiele mit `bash -n`. Reine Textfragmente
  zur Recordverarbeitung und Personalisierung mit synthetischen Daten prüfen.
- [ ] **Inhalt:** Setup, Rollenmatrix und Integrationsrezepte passen zusammen.
  Keine Zugangsdaten oder unbeabsichtigten privaten Zielbindungen im Lieferumfang.
- [ ] **Planner-Interview:** Manifest und Bezugsrezept enthalten beide Originalskills
  `grill-me` und `grilling` ausschließlich für den Planner, samt vollständigen
  Begleitdateien und Lizenz. Die Planner-SOUL verlangt das Laden von `grilling`
  vor neuen Plänen, regelt den Vorrang gegenüber anderen Frageregeln und erhält
  technische Delegation sowie ausdrückliche Planannahme. Setup und Protokoll
  prüfen Verfügbarkeit und tatsächliche Nutzung getrennt.

Vorhandene Pakettests können diese Prüfung unterstützen. Maßgeblich sind ihre
wirklichen Prüfinhalte und Ergebnisse; eine frühere Testbeschreibung oder ein
Testlauf ohne gefundene Tests ist kein Nachweis.

## 2. Team nach Einrichtung prüfen

Erst im beauftragten Zielsetup mit bestätigten Rollen, Diensten, Modellzugängen,
Nachrichtenzielen und begrenztem Testumfang ausführen. Die konkreten Schritte stehen
in [Setup](setup.md), [Rollenbindungen](native-workflow.md) und
[Integrationen](integrations.md); hier wird nur das Ergebnis zusammengeführt.

| Prüfung | Erfolgssignal |
|---|---|
| Rollen und Skills | Richtige Profile, vollständige SOUL-Aufnahme, benötigte Skills tatsächlich geladen; vorgesehene Modi funktionieren auch in einem neuen Kontext. |
| Planner-Interview | Beide Originalskillbäume samt Lizenz bytegleich zur protokollierten Quelle; `grilling` im Planner nativ gefunden und vollständig geladen, ausdrücklicher `grill-me`-Aufruf lädt `grilling`. Die SOUL-Ladepflicht ist im neuen Kontext/Resume wirksam; fachliches Verhalten separat im gemeinsamen Probelauf prüfen. |
| Modelle und Reasoning | Echte begrenzte Aufrufe verwenden die eingerichteten Modelle. Planner nutzt das höchste unterstützte Reasoning; höhere Stufen für Coder/Reviewer funktionieren gemäß SOUL. |
| Team-Codex | Prozesshomes, Konfiguration und Skillroots stimmen im tatsächlichen Worker; Codex erzeugt ein geprüftes Testartefakt. Installierte Helfer gemäß Integrationsrezept funktional prüfen. |
| Memory | Gemeinsame Projektbank und Rollenfilter funktionieren beim Speichern und Abrufen; nur freigegebene synthetische Testinhalte verwenden. |
| Mattermost | Planner antwortet auf Erwähnung, ohne Erwähnung gemäß Konfiguration und im DM; Wake erreicht den richtigen Projektkanal und wird vom Planner bearbeitet. Native Eingangsprüfungen weisen nicht freigegebene Nutzer/Bots im Projektkanal und Nachrichten des bestätigten Nutzers in nicht freigegebenen Kanälen ab; zusätzliche kanalweite/globale Grants erweitern die bestätigte Freigabe nicht. Ablehnungsfälle gemäß [Integrationen](integrations.md) ohne Modellstart prüfen. |
| Codeanalyse | Die gewählte Alternative besteht die [Index-/Relations-/Aktualisierungsprüfung](code-analysis.md#funktionspruefung). |
| Profilbezogener Anweisungsdateischutz | In jedem erzeugten Planner-, Coder- und Reviewerprofil steht `security.protected_instruction_files` ausdrücklich als boolesches `false` in der jeweiligen `config.yaml`; der effektive Leser liefert ebenfalls `false`. Gespeicherten und effektiven Wert je Profil im Setuprecord belegen; ein globales `false` allein genügt nicht. Globale/administrative Konfiguration unverändert, etwaige Verwaltungskonflikte offen ausgewiesen. |
| Betriebsgrenzen | Tatsächliche Timeout-, Retry- und Rate-Limit-Behandlung sowie relevante Grenzen sind bekannt. Konkrete Probleme vor der betroffenen Nutzung klären. |
| Board-Automatik | Der Resolver des Dispatchers liefert `(False, N)` im dispatchenden Home und in jeder Rollenprofilkopie; der Auto-Decomposer erzeugt keine neuen Karten oder Parent-Kanten. Automatisch nach `triage` verschobene Karten klärt der Planner innerhalb seines Mandats; ihr Status allein ist kein Zerlegungsauftrag. Details in der [Kanban-Automatik](../references/kanban-block-triage-escalation.md). |

Vorhandene fremde Profile, persönliche Codex-Ausstattung und Produktdaten bleiben
erhalten. Ein gespeicherter Konfigurationswert beweist noch keine wirksame Fähigkeit.

## 3. Ein gemeinsamer Probelauf

Ein kleiner harmloser Auftrag im separaten Testrepository genügt:

1. Beginne mit einem kurzen Brief, der zwei voneinander unabhängige offene
   Produktentscheidungen und eine davon abhängige Folgeentscheidung enthält.
   Planner lädt selbständig `grilling` und fragt die unabhängigen Entscheidungen
   in derselben Runde jeweils mit Empfehlung ab. Die abhängige Frage stellt er
   erst nach Klärung ihrer Voraussetzung; aus dem Testrepository ermittelbare
   Fakten recherchiert er selbst.
   Bestätigte Antworten bleiben bei Wiederaufnahme erhalten. Erst nach bestätigtem
   gemeinsamen Verständnis erstellt er den kurzen Plan; der Nutzer nimmt ihn
   ausdrücklich an. Vor dieser Planannahme entstehen keine Tickets. Skillladebeleg
   und Dialogverlauf festhalten; bloße Dateiexistenz besteht diesen Test nicht.
2. Planner erzeugt daraus ein Ticket; der native Dispatcher übergibt es dem Coder.
3. Coder lässt Codex das Testartefakt erzeugen, prüft es und erstellt den vorgesehenen Commit.
4. Coder übergibt dieselbe Karte an den unabhängigen Reviewer; dieser prüft das Ergebnis.
5. Nach erfolgreichem Review bearbeitet der Planner den tatsächlichen Wake und
   berichtet im vereinbarten Projektkanal.

Ticket, Commit und Nachricht müssen zum selben Testauftrag gehören. Vorhandene
Einzelnachweise können aus diesem Lauf stammen; keine unnötige doppelte Ausführung.
Ein künstlicher Fehler- oder Reviewrücklauf ist für diesen Probelauf nicht nötig.

## 4. Ergebnis festhalten

Im privaten [Setup-Protokoll](../templates/setup-record.md) je Prüfung notieren:
**geprüfter Stand · bestanden / konkreter Fehler / noch ungeprüft · kurzer Beleg**.
Bei einem Fehler dessen Auswirkung und die nächste notwendige Maßnahme nennen.

- **Paket geprüft:** Die Dateiprüfungen sind bestanden; keine Aussage über ein Zielteam.
- **Zielsetup teilweise geprüft:** Erfolgreiche Fähigkeiten und offene Punkte einzeln benennen.
- **Team technisch geprüft:** Die benötigten Fähigkeiten und der gemeinsame Probelauf
  sind tatsächlich bestanden. Fachliches Projekt-Onboarding folgt als eigener Auftrag.

Nach Änderungen nur die davon betroffenen Prüfungen und nötigen Integrationswege
wiederholen. Veröffentlichung, Commit-Freigabe und Paketexport sind separate Aufgaben.
