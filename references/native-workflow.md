# Rollenbindungen einrichten und prüfen

Diese Referenz ergänzt den [Setupablauf](setup.md): Sie ordnet bestätigte Werte
ihren Zielen zu und beschreibt die Personalisierung der Rollen. Der laufende
Arbeitsprozess und die Reasoning-Eskalation stehen in den Rollen-SOULs; fachliche
Anleitungen bleiben in den jeweils installierten Skills.

## 1. Eigene Skills unverändert kopieren

Die [Quellenübersicht](upstream-sources.md#mitgelieferte-bausteine) nennt die
mitgelieferten Skillbäume und ihre Zielrollen. Je Ziel den vollständigen Baum aus
`skills/` einschließlich Referenzen, Skripten und vorhandenen Lizenz-/Notice-Dateien
kopieren. `SKILL.md` bleibt `SKILL.md`; Inhalte werden weder gerendert noch umbenannt.

- Hermes: `<tatsächlich aufgelöster Rollenhome>/skills/<Skillname>/`.
- Team-Codex: `<CODEX_PROCESS_HOME>/.agents/skills/<Skillname>/` gemäß Rollenmatrix.
- Vorhandene Ziele auf Eigentum und Änderungen prüfen; bei Konflikten anhalten.
- Dateimenge und Bytes vergleichen, danach Discovery und Laden im Zielharness prüfen.

Die kopierten Pakete müssen ohne das Makerpaket funktionieren. Es wird kein
zusätzlicher gemeinsamer Workflowskill und keine generierte Bindingdatei benötigt.

## 2. Rollen-SOULs personalisieren

Die Vorlagen für [Planner](../templates/roles/planner.SOUL.md.template),
[Coder](../templates/roles/coder.SOUL.md.template) und
[Reviewer](../templates/roles/reviewer.SOUL.md.template) werden nur an den
vorgesehenen Platzhaltern verändert. Das [Manifest](../manifest.json) beschreibt
je Rolle die tatsächlich vorkommenden `render_fields`.

| Feld | Bestätigter Wert |
|---|---|
| `ROLE_NAME` | Eigener Anzeigename der jeweiligen Rolle |
| `PLANER_NAME` | Planner-Anzeigename; Schreibweise mit einem N |
| `CODER_NAME` | Coder-Anzeigename |
| `REVIEWER_NAME` | Reviewer-Anzeigename |
| `PROJECT_NAME` | Projektkennung als einzelnes Segment; bestimmt nicht den Workspace |
| `HINDSIGHT_BANK_NAME` | Tatsächlich zugeordnete gemeinsame Projektbank |
| `KANBAN_BOARD_NAME` | Native Boardkennung, nicht der Anzeigetitel |
| `CODER_PROFILE` | Technische Coderprofilkennung, soweit in der Vorlage vorhanden |
| `REVIEWER_PROFILE` | Technische Reviewerprofilkennung, soweit in der Vorlage vorhanden |
| `CODEX_REASONING_DEFAULT` / `CODEX_REASONING_MAX` | Bestätigter Team-Codex-Standard und erlaubte Obergrenze; nur Coder-Vorlage |
| `ROLE_REASONING_DEFAULT` / `ROLE_REASONING_HIGH` | Bestätigter Reviewer-Standard und höchste erlaubte Prüfstufe; nur Reviewer-Vorlage |

Anzeigenamen und technische Kennungen getrennt halten. Alle Mehrfachvorkommen
aus demselben bestätigten Datensatz ersetzen. Der eigene Anzeigename liefert
`ROLE_NAME`; weder zusätzliche Persona noch neue Rollenregeln anhängen.

Der reine [Textrenderer](render_text.py) validiert die rollenbezogene Feldmenge
und ersetzt in einem Durchlauf. Fehlende, zusätzliche oder beschädigte Felder
sind Fehler. Werte bleiben unverändert: keine stille Kürzung oder Normalisierung.
Namen sind nichtleerer einzeiliger Klartext; technische Kennungen und Projektname
müssen außerdem die jeweiligen Syntax- und Pfadprüfungen bestehen. Markdown wird
kontextgerecht maskiert; technische Werte in Codekontexten bleiben unverfälscht.
Alle Nichtplatzhalterbytes der bestätigten Vorlage bleiben erhalten.

Vor dem Schreiben die personalisierte Fassung annehmen lassen. Ziel ist ausschließlich
`SOUL.md` im bestätigten Rollenhome. Anschließend vollständig zurücklesen und mit
dem erzeugten Solltext vergleichen. Fremde oder zwischenzeitlich geänderte Dateien
nicht überschreiben. Die effektive Aufnahme der vollständigen SOUL im jeweiligen
Profil prüfen; Dateiexistenz allein genügt nicht.

## 3. Technische Werte an ihren tatsächlichen Zielen binden

| Wert | Ziel und Prüfung |
|---|---|
| Rollenprofil und Anzeigename | Native Profilregistrierung und passende personalisierte SOUL |
| Projektworkspace | Bestätigten kanonischen absoluten Workspace gegen Projektkontext, Profil-`terminal.cwd`, Board-Standardworkspace und späteren Ticketworkspace prüfen; die SOUL verlangt diesen Abgleich |
| Boardkennung | SOUL und explizite Boardauswahl bei Ticketaktionen; nativen Boardzustand zurücklesen |
| Projektbank | Native Memorykonfiguration und Bankplatzhalter der SOUL; Rollenfilter funktional prüfen |
| Hermes-Modell und Reasoning | Native Profilkonfiguration; wirksame Auswahl einschließlich Overrides prüfen |
| Team-Codex | Getrennte Prozess-/Konfigurationshomes und geeignete Binary gemäß [Integrationsrezept](integrations.md#team-codex); im tatsächlichen Worker prüfen |
| Codeanalyse | Genau eine Alternative gemäß [Analyserezept](code-analysis.md), mit Originalskills und passender nativer Aktivierung |
| Planner-Kommunikation | Native Plannerkonfiguration und konkrete Wake-Subscription; Projektkanal, DM und Nutzeridentität getrennt halten |

Projektname und kanonischen absoluten Workspace getrennt bestätigen. Die SOULs
leiten keinen Pfad aus PROJECT_NAME ab, sondern verlangen den Abgleich mit der
vorhandenen Projekt-/Profil-/Boardbindung; kein zusätzlicher Renderplatzhalter
oder zweiter Laufzeit-Bindingdatensatz. Den Workspace im bestehenden Setuprecord
dokumentieren und nativ als terminal.cwd/Board-Standardworkspace binden. Technische
Plannerprofilkennung aus der bestätigten Zuordnung gegen die native Registrierung
prüfen und für Klärungs-, Vorschlags- und TIMER-Rückwege zugänglich halten; nicht
aus dem Anzeigenamen ableiten. Verschachtelte Checkouts und abweichende Git-Roots
erhalten; bei widersprüchlichen Bindungen vor Anlage anhalten und klären.
Repository, Branch, Planrevision und Ticket-/Run-/Event-IDs werden erst beim jeweiligen
Auftrag bestimmt. Sie sind keine vorab zu erfindenden Setupwerte.

Konkrete Modelle und feste Planner-/Hermes-Coder-Stufen stehen in der nativen
Konfiguration. Reviewer und Team-Codex erhalten die bestätigten Standard-/Maximalwerte
wörtlich in ihren Rollen-SOULs. Beim Setup nur Wechsel innerhalb der erlaubten
Grenzen prüfen, einschließlich CLI-/Session-Overrides und Helferpins. Der Renderer
prüft sichere Einzelwerte, nicht Modellunterstützung oder Stufenrangfolge; diese
werden gemäß Setup vor dem Rendern geprüft. Fehlende Unterstützung oder Freigabe
ist ein konkreter Blocker, kein Anlass für einen stillen Modell-/Providerwechsel
oder eine höhere Stufe. Die Rollenregel ist keine technische Ausführungssperre.

Kommunikationszugänge und Kanalbindungen bleiben beim Planner. Geheimnisse gehören
in geschützte native Zugangswege. Der private [Setuprecord](../templates/setup-record.md)
dokumentiert Werte, Ziele und Nachweise; er ist keine zusätzliche Laufzeitkonfiguration.

## 4. Funktionsprüfung und Wiederaufnahme

1. Rollen, Profile, Board, Workspace und Bank anhand der tatsächlichen Zielobjekte
   abgleichen; Codex-Prozessbindung gesondert im Worker prüfen.
2. Vollständige Skillbäume, tatsächliches Laden und vollständige SOUL-Aufnahme prüfen.
   Caveman-Auftragsregel und Ponytail-Prozessbindung müssen auch nach Resume gelten.
3. Native Reviewübergabe an den unabhängigen Reviewer, Rückgabe an den Coder und
   Planner-Wake anhand der aktuellen Zielschnittstellen prüfen. Der begrenzte
   Pipelineversuch folgt dem [Setupablauf](setup.md#7-einzelprüfungen-und-wake-vor-ticketfreigabe).
4. Konkrete Laufzeitgrenzen und Fehler, einschließlich Retryverhalten, im Setuprecord
   festhalten. Statische Quellenprüfung ersetzt keinen echten Funktionsnachweis.
5. Bei Wiederaufnahme native Objekte und eigene Dateien mit dem letzten geprüften
   Stand vergleichen und am offenen Schritt fortsetzen. Keine zweite Zustandsquelle
   aus alten Setupwerten herstellen.

Diese Schritte gehören zum später ausdrücklich beauftragten Zielsetup. Beim
Bearbeiten dieses Pakets werden keine Profile, Dienste oder Agenten aktiviert.
