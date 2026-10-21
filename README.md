# Generic Devteam — Maker für Linux

Dieses Paket führt durch die Einrichtung eines eigenen Planner-, Coder- und
Reviewerprofils in einem vorhandenen Hermes. Produktive Umsetzung läuft über
Team-Codex, Koordination über natives Kanban, gemeinsames Wissen über eine neue
Hindsight-Bank und Kommunikation über den eigenen Mattermost-Bot des Planners.
Es enthält Rollen-SOUL-Vorlagen und fertige eigene Skillpakete, keine kopierten Fremdinstallationen.

Der Repositoryroot ist zugleich der vollständige Skillbaum: [SKILL.md](SKILL.md)
ist der Einstieg für Hermes, diese README das HOWTO. `references/`, `templates/`
und `skills/` gehören dazu. Nutzung und weitere Bearbeitung erfolgen in diesem
Repository.

**Liefergrenze:** Der geführte Maker, allgemeine Integrationsrezepte und beide
[Codeanalysewege](references/code-analysis.md) sind als Einrichtungsrezepte dokumentiert,
mit Originalkomponenten und Zielkontexten. Ihre Laufzeitabnahme erfolgt beim Zielsetup.
Timeout-, Retry- und Rate-Limit-Grenzen werden am tatsächlichen Zielstand geprüft.
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
   `NOTICE.md` sowie `references/`, `templates/` und `skills/`. Die Dateiliste steht
   im Manifest. Git-Metadaten, `.gitignore` und `vortrag/` gehören nicht zur
   Skillinstallation. Herkunft und Lizenz stehen in
   [NOTICE](NOTICE.md) und [Originalquellen](references/upstream-sources.md).
2. Ermittle das tatsächliche Home des Hermes-Profils, in dem du den Maker aufrufen
   willst, über die vorhandene Profilkonfiguration. Prüfe vor jedem CLI-Aufruf
   mögliche Bootstrap-/PM-Wirkungen gemäß [Setup](references/setup.md).
3. Nach Freigabe kopiere diesen vollständigen Baum in dessen
   `skills/generic-devteam/`. Existiert das Ziel, vergleiche zuerst Herkunft und
   lokale Änderungen; niemals fremde Anpassungen überschreiben. Die vollständigen
   eigenen Skillbäume behalten ihre `SKILL.md` und werden beim Teamsetup unverändert
   an die vorgesehenen Ziele kopiert. Nur die Rollen-SOUL-Vorlagen werden personalisiert.
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
Projektname und kanonischer absoluter Workspace werden getrennt bestätigt; der
Pfad wird nicht aus dem Namen abgeleitet. Die Rollen prüfen die vorhandene
Projekt-/Profil-/Boardbindung, auch bei verschachtelten Checkouts. Widersprüche
werden vor Anlage geklärt; bestehende Repositories werden nicht dafür verschoben.
Das private Protokoll landet im tatsächlichen Plannerhome unter `devteam/setup.md`,
nicht im Projekt oder öffentlichen Paket. Geheimnisse gehören ausschließlich in
den geschützten Zielweg; das Protokoll speichert nur Secretort/Prüfstatus.

## Ergebnis und Wiederaufnahme

Die Rollen bekommen vollständige eigene Skillbäume, unveränderte Rollenpflichten,
personalisierte SOULs und native Modell-/Reasoning-Konfiguration. Im Ziel bezogene
Originalkomponenten werden mit Revision, Dateimenge und Lizenz nachgewiesen.
Bei Unterbrechung den Maker mit dem privaten Setuprecord wieder aufrufen; er liest
native Profile, Board und Dienstobjekte erneut und setzt am ersten offenen Gate
fort. Kein blindes Wiederholen von Create, Login, Bank- oder Kanalanlage.

Updates zunächst außerhalb aktiver Discovery prüfen, mit installierten Revisionen
und eigenen Anpassungen vergleichen und den gezielten Änderungsumfang genehmigen
lassen. Vorherige eigene Dateistände geschützt aufbewahren. Rückbau betrifft nur
protokollierte eigene Objekte/Einträge; Datenlöschung braucht eine eigene Freigabe.

## Öffentliche Paketprüfung — ohne Dienste oder private Quellen

Die [Prüfanleitung](references/verification.md) enthält zwei Checklisten:
Paketdateien vor Verwendung und Teamfunktionen nach Einrichtung. Zur Paketprüfung
gehören Dateibestand, Links, vollständige Skillbäume, SOUL-Personalisierung und
Syntax. Reine Textprüfungen starten keine Modelle oder Dienste.

Beim späteren Zielsetup folgen die Funktionsprüfungen aus den Integrationsrezepten
und ein kleiner gemeinsamer Probelauf bis zum Plannerbericht. Im Setup-Protokoll
stehen die tatsächlich bestandenen Prüfungen, konkreten Fehler und ungeprüften Punkte.
Frühere Review- oder Exportergebnisse ersetzen keine Prüfung der aktuellen Fassung.
