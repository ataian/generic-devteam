# Verwendung in Hermes und Codex

Beide Runtimes verwenden dasselbe Paket. Projektregeln, Rollen und Berechtigungen stammen aus dem jeweiligen Einsatzkontext, nicht aus einer bestimmten Installation oder einem bestimmten Team.

## Fähigkeiten statt eingebauter Infrastruktur

| Bedarf | Hermes | Codex |
| --- | --- | --- |
| Skill und Referenzen | `skill_view` lädt den installierten Skill und relative Referenzen; alternativ Dateien lesen, ohne dies als Katalognachweis auszugeben. | Skill explizit mit `$screenshot-to-code` aufrufen oder anhand der Beschreibung auswählen lassen; referenzierte Dateien mit den tatsächlich vorhandenen Lesewerkzeugen öffnen. |
| Regeln und Projektdateien | `read_file`, `search_files`; Änderungen nur mit vorhandenen Schreibrechten. | Verfügbare Datei-/Shellwerkzeuge; geltende Sandbox-/Freigaberegeln erhalten. |
| Quelle/Render ansehen | Wenn angeboten `vision_analyze`; vorher tatsächliche Bildprüffähigkeit feststellen. | Verfügbare Bildsicht, beispielsweise angebotenes `view_image`; nicht allein wegen eines Dateipfads als vorhanden behandeln. |
| Browser, Aufnahme, Offlineprobe | Vorhandenes Browserwerkzeug oder zugelassene Projekt-CLI. | Vorhandene Browseranbindung oder zugelassene Projekt-CLI. Keine Browserfähigkeit bloß aus dem Runtime-Namen ableiten. |
| Checks/Build/Extraktion | `terminal` mit vorhandenen zugelassenen Projektwerkzeugen. | Vorhandenes Ausführungswerkzeug mit denselben Projektvorgaben. |
| Offene Produktentscheidung | Vorhandener Gesprächs-/Rückfrageweg; falls verfügbar `clarify`. | Vorhandener Gesprächs-/Rückfrageweg. Keine Hermes-Werkzeuge voraussetzen. |

Toolnamen beschreiben verfügbare Möglichkeiten, keine Installationsanforderungen. Fehlendes Werkzeug konkret melden; keine erfundenen Tools, heimlichen Installationen oder neuen Dienste einführen. Ein Textleser ersetzt keine Bildsicht. Toolschemas der laufenden Sitzung haben Vorrang vor Beispielen.

## Laden und Rollen

Nur benötigte Referenzen laden: Quelle/Assets bei Extraktion oder Herkunftsfragen, visueller Abgleich beim Nachbau, Offlineexport ausschließlich beim Exportauftrag. Gleichnamige Skillkopien können unterschiedlich aufgelöst werden; bei Zweifeln tatsächlich geladenen Pfad und Inhalt prüfen. Eine alte Unterhaltung beweist nicht die aktuelle Paketidentität.

Planner klären offene Produktfragen und planen. Implementierer arbeiten in freigegebenen Phasen; Reviewer prüfen unabhängig. Eine akzeptierte Spezifikation wird nicht durch den Runtimewechsel erneut zur Diskussion gestellt. Neue wesentliche Lücken rollenrichtig melden und ausschließlich abhängige Arbeit anhalten. Weder Skillaufruf noch Toolverfügbarkeit erweitert Rechte oder beauftragt Commit, Veröffentlichung oder Betrieb.
