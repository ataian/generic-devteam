# Übergabe — Installationsablauf neu aufbauen

## Auftrag für die neue Session

Mit Max den Installationsablauf dieses Skills neu aufbauen: **nur die notwendigen Schritte und Fragen**, um auf einer frischen, funktionsfähigen Hermes-Installation ein neues Devteam einzurichten.

Hier wird das **Skill-Paket entwickelt**, nicht bereits ein Team auf diesem Host installiert. Zuerst den schlanken Ablauf mit Max klären; anschließend nur die ausdrücklich beauftragten Änderungen umsetzen.

## Verbindlicher Maßstab

- Vorhandene, ausgearbeitete SOULs und eigene Skills erhalten. Neue Teamnamen und andere bestätigte Bindungen werden durch Platzhalter eingesetzt; Arbeitsweise, Regeln und Formulierungen werden dadurch nicht neu entworfen.
- Max hat die Projektdateien selbst überarbeitet. Der aktuelle Dateistand ist Ausgangspunkt; frühere Kopien und Prüfberichte ersetzen ihn nicht.
- Jede Abweichung vom konkreten Auftrag braucht Max' vorherige Zustimmung. Keine ungefragten Ergänzungen, Umformulierungen, Zusammenführungen oder Nebenänderungen.
- Rollenregeln stehen in den SOULs. Der Installer richtet ein; er erzeugt keine zusätzliche, parallel gepflegte Rollen-/Prozesspolicy.
- Nur notwendige, noch fehlende Angaben erfragen; bestätigte Werte wiederverwenden. Technische Profilkennungen und Anzeigenamen unterscheiden.
- Kurze Tabellen, konkrete Fragen und knappe Ergebnisse statt langer Erläuterungen. Subagents für klar abgegrenzte Prüfaufträge nutzen.

## Aktueller Bestand

| Pfad | Bedeutung |
|---|---|
| `SKILL.md` | Noch bisheriger Ablauf; verlinkt weiterhin Dateien in `unklar/`. Neu aufzubauen. |
| `templates/roles/` | Planner-, Coder- und Reviewer-SOUL-Vorlagen; aktuellen Inhalt lesen und erhalten. |
| `skills/` | Eigene Skills, inzwischen von Max überarbeitet. |
| `references/render_text.py` | Vorhandener Text-Renderer; Passung zu aktuellen Vorlagen und neuem Ablauf noch prüfen. |
| `unklar/references/` | Alte umfangreiche Setup-, Integrations-, Workflow-, Quellen-, Analyse- und Prüftexte; Klärungsmaterial, keine automatisch verbindliche Bauvorgabe. |
| `unklar/templates/` | Vorübergehender Altbestand; die Modellpolicy entfällt ohne Nachfolger. Die verwendete Protokollvorlage liegt unter `templates/setup-record.md`. |
| `README.md`, `manifest.json` | Bestehende Paketbeschreibung; beim beauftragten Neuaufbau mit dem tatsächlichen Ergebnis abgleichen. |

Eigene Skills im Projekt:
- `minimal-change-engineering`
- `screenshot-to-code`
- `project-lib-versioning`
- `plan-versioning-semver`
- `brownfield-feature-planning`

Herkunft: Gordon-Team als Hauptreferenz; Planversionierung aus Picard. Brownfield basiert auf Picard, ergänzt um markierte Gordon-Abschnitte zu Planrevision, Zeit-/Kostenkontrolle und die Phasenfreigabe-Referenz. Danach hat Max die Skills weiter bearbeitet. Keine früheren Inhalte ungefragt wiederherstellen.

## Bereits geklärt

- Zielteam: Planner → Coding-Orchestrator/Codex → unabhängiger Reviewer.
- Der Skill soll die technische Einrichtung ermöglichen, nicht die fachliche Planung des späteren Projekts übernehmen.
- Konkrete Modelle stehen in der nativen Konfiguration; Reasoning-Eskalation steht in den SOULs. Planner nutzt das höchste unterstützte Reasoning, Coder/Reviewer erhöhen es nach ihren Rollenregeln am eingerichteten Modell. Die zusätzliche Modellpolicy samt aktiven Setup-/Ladeverweisen entfällt. Die Coder-Vorlage wurde dafür auf ausdrücklichen Auftrag angepasst; Codex-Prozessbindung und Caveman-Auftragsregel stehen direkt dort.
- Der vorhandene Renderer nimmt Vorlagentext und Werte entgegen und liefert Text zurück. Er liest und schreibt selbst keine Dateien. Speicherung der Antworten, Aufruf und Schreiben der Zieldateien gehören zum neu zu klärenden Installationsablauf.
- `unklar/` ist ausschließlich vorübergehendes Ausgangsmaterial und wird am Ende entfernt. Benötigte Inhalte werden gezielt in neue Dateien überführt; entfallene Inhalte erhalten keinen Nachfolger. Das fertige Paket darf keine Abhängigkeiten auf diesen Ordner haben. Die abschließende Entfernung ist noch nicht ausgeführt.

## Einstieg

1. Aktuellen Projektstand und die von Max bearbeiteten Vorlagen lesen.
2. Mit Max eine kurze Reihenfolge festlegen: notwendige Voraussetzungen → fehlende Eingaben → Einrichtung → konkrete Funktionsprüfung.
3. Jeden vorgeschlagenen Schritt am Ziel messen: Was muss tatsächlich vorhanden sein, damit das Team arbeitet? Alte Dokumentmenge und alte Tests begründen keine zusätzlichen Anforderungen.
4. Erst nach dem jeweiligen Auftrag die betroffenen Paketdateien ändern. Vorlagen, eigene Skills und bestehende Teams bleiben außerhalb dieses Umbaus, soweit Max nichts anderes beauftragt.

**Aktueller Arbeitsstand:** Quellenübersicht, Codeanalyse und Rollenbindungen liegen neu unter `references/`. Die direkt betroffenen Setup-/Integrationsverweise sind angepasst. Weitere Alttexte, Manifest-Dateiinventar und bisherige Prüf-/Lieferstandsbeschreibungen sind noch schrittweise abzugleichen; keine Gesamtfreigabe des Pakets. `SKILL.md.orig` bleibt unverändert. Kein Team installiert.
