# Generic Devteam — Maker für Linux

Dieses Paket führt durch die Einrichtung eines eigenen Planner-, Coder- und
Reviewerprofils in einem vorhandenen Hermes. Produktive Umsetzung läuft über
Team-Codex, Koordination über natives Kanban, gemeinsames Wissen über eine neue
Hindsight-Bank und Kommunikation über den eigenen Mattermost-Bot des Planners.
Es enthält eigene Rollen-/Skillvorlagen, keine kopierten Fremdinstallationen.

Der Repositoryroot ist zugleich der vollständige Skillbaum: [SKILL.md](SKILL.md)
ist der Einstieg für Hermes, diese README das HOWTO. `references/`, `templates/`
und `tests/` gehören dazu. Nutzung und weitere Bearbeitung erfolgen in diesem
Repository.

**Liefergrenze:** Der geführte Maker, allgemeine Integrationsrezepte und beide
[Codeanalysewege](unklar/references/code-analysis.md) sind statisch dokumentiert, mit
vollständigen Originaldateimengen und Zielkontexten. A01-CBM bleibt wegen G2 offen.
G1 (endliche native Rate-Limit-Gesamtgrenze)
bleibt ein Halt vor betroffener automatischer Dispatchfreigabe; G2 betrifft den
noch ausstehenden Originaloutput-/Bytevergleich der selektiven CBM-Integration.
Statische Pakettests sind keine Betriebsbereitschaft und kein unabhängiger Review.

## Voraussetzungen

- Eigene Linux-Umgebung, vorhandenes laufendes Hermes und bestehendes Benutzerkonto.
- Bereits erreichbare Mattermost-/Hindsight-Dienste, berechtigte Zugänge und ein
  geeigneter Modellanbieter. Hermes- und Codex-Anmeldung werden separat geprüft.
- Projektname/Workspace, Rollennamen, bestätigte neue Bank und Boardkennung,
  konkrete Modellwahl und genau eine Analysewahl (`codebase-memory` oder `graphify`).
- Freigabe der tatsächlichen lokalen Installationen, gemeinsamen PM-Wirkungen und
  Aktivierung. Keine Server-/Benutzer-/Daemonbereitstellung durch diesen Maker.

## Direkt aus dem Checkout verwenden

Öffne den Checkout im vorhandenen Hermes und beauftrage:

> Lies `SKILL.md` im Repositoryroot und die dort verlangten Referenzen vollständig.
> Führe mich durch die technische Einrichtung meines neuen Projektteams. Beginne
> mit Bestand und Projektname/Workspace; zeige mir die konkreten Änderungen
> einschließlich PM-/Aktivierungswirkungen vor der Freigabe. Führe noch keine
> Produktarbeit aus.

Dieser dateibasierte Einstieg benötigt keine vorherige Registrierung des Makers
im Skillkatalog. Für dauerhaftes Laden über den Skillnamen folgt die Installation.

## Einmal installieren, anschließend geführt aufrufen

Dies ist eine Anleitung für den künftigen Nutzer, keine Aufforderung, beim Lesen
oder Bauen des Pakets ein Setup auszuführen.

1. Beziehe den **gesamten Skillbaum direkt aus dem Repositoryroot** oder als
   separates Paketarchiv: `SKILL.md`, `README.md`, `manifest.json`, `LICENSE`,
   `NOTICE.md` sowie `references/`, `templates/` und `tests/`. Git-Metadaten sind
   kein Bestandteil der Skillinstallation. Herkunft und Lizenz stehen in
   [NOTICE](NOTICE.md) und [Originalquellen](unklar/references/upstream-sources.md).
2. Ermittle das tatsächliche Home des Hermes-Profils, in dem du den Maker aufrufen
   willst, über die vorhandene Profilkonfiguration. Prüfe vor jedem CLI-Aufruf
   mögliche Bootstrap-/PM-Wirkungen gemäß [Setup](unklar/references/setup.md).
3. Nach Freigabe kopiere diesen vollständigen Baum in dessen
   `skills/generic-devteam/`. Existiert das Ziel, vergleiche zuerst Herkunft und
   lokale Änderungen; niemals fremde Anpassungen überschreiben. Die eingebetteten
   `SKILL.md.template` bleiben im Maker unverändert und sind keine aktiven Skills.
4. Prüfe in diesem Profil native Discovery von `generic-devteam`, lade `SKILL.md`
   und `references/setup.md` ausdrücklich. Der bestehende Sitzungskatalog und ein
   neu aufgelöstes Skillpaket sind unterschiedliche Nachweise; keinen globalen
   Gatewayrestart allein zur Katalogaktualisierung auslösen.
5. Beauftrage im Ziel-Hermes beispielsweise:

   > Lade generic-devteam. Führe mich durch die technische Einrichtung meines
   > neuen Projektteams. Beginne mit Bestand und Projektname/Workspace; zeige mir
   > die konkreten Änderungen einschließlich PM-/Aktivierungswirkungen vor der
   > Freigabe. Führe noch keine Produktarbeit aus.

Der Skill wartet an nötigen Eingabe-/Freigabepunkten. Namen sind Klartext, keine
Profilpfade. Die Rollen verwenden ihre festen Texte ohne zusätzliche Persona.
Der Reviewer bindet `~/projects/<PROJECT_NAME>` fest; das Setup gleicht diesen
Pfad auf dem Zielkonto mit dem bestätigten absoluten Workspace ab. Abweichungen
werden vor Anlage geklärt, nicht durch stilles Umschreiben der SOUL verdeckt.
Das private Protokoll landet im tatsächlichen Plannerhome unter `devteam/setup.md`,
nicht im Projekt oder öffentlichen Paket. Geheimnisse gehören ausschließlich in
den geschützten Zielweg; das Protokoll speichert nur Secretort/Prüfstatus.

## Ergebnis und Wiederaufnahme

Die Rollen bekommen vollständige eigene Skillbäume, unveränderte Rollenpflichten,
gerenderte Teambindungen und eine erreichbare Modellpolicy. Im Ziel bezogene
Originalkomponenten werden mit Revision, Dateimenge und Lizenz nachgewiesen.
Bei Unterbrechung den Maker mit dem privaten Setuprecord wieder aufrufen; er liest
native Profile, Board und Dienstobjekte erneut und setzt am ersten offenen Gate
fort. Kein blindes Wiederholen von Create, Login, Bank- oder Kanalanlage.

Updates zunächst außerhalb aktiver Discovery prüfen, mit installierten Revisionen
und eigenen Anpassungen vergleichen und den gezielten Änderungsumfang genehmigen
lassen. Vorherige eigene Dateistände geschützt aufbewahren. Rückbau betrifft nur
protokollierte eigene Objekte/Einträge; Datenlöschung braucht eine eigene Freigabe.

## Öffentliche Paketprüfung — ohne Dienste oder private Quellen

Python ab 3.11 (`tomllib`), bereits verfügbarer sicherer YAML-Parser `ruamel.yaml`
und `bash` für reine Syntaxprüfung sind nötig. Keine Test-Abhängigkeit wird
automatisch installiert. Aus diesem Paketroot:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test*.py' -v
```

Geprüft werden Dateimenge, Syntax/Frontmatter, Rollenmatrix, Links, Herkunft,
Screenshotbytes, JSON-/TOML-Rezepte samt MCP-/Hookdaten, Shellsyntax mit `bash -n`
(ohne Ausführung) und die reine Stringvalidierung/Ersetzung aus
[render_text.py](references/render_text.py). Dieses Modul hat weder Dateischreiber
noch Setup-/CLI-Einstieg. Synthetische Daten-/Textfälle samt negativen Mutationen
sind **keine Agentenverhaltensprüfung**. Es werden keine Hermes-/Codex-Module,
operativen Helfer, Bootstraproutinen, Modelle oder Dienste gestartet.

Die [Prüfanleitung](unklar/references/verification.md) erklärt alle Checks, synthetischen
Fälle, isolierten Defektkopien und die getrennten A-/B-Kriterien. Der unabhängige
Whole-Branch-Review des Paketstands ist abgeschlossen; der anschließende
Paketexport wurde auf Dateimenge, Commitbytes und ZIP-CRC geprüft. Spätere
Änderungen benötigen ihre eigene betroffene Prüfung. A01-CBM/G2 bleibt offen,
die G1-Budgetanforderung aus A03 ist im untersuchten nativen Stand unerfüllt.

Die spätere Zielabnahme umfasst reale Discovery/Promptaufnahme, persistente Modi,
Modellcalls und sechs begrenzte Original-Agentdelegationen, gefilterte
Memoryrequests, Erwähnungs-/Free-Response-/DM-Dialog und den unabhängigen
Pipelineweg bis zur Planner-Projektkanalnachricht. Offene Kriterien bleiben offen.
