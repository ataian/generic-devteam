---
name: generic-devteam
description: Richte ein natives Hermes-Projektteam unter Linux ein.
version: 0.1.0
author: Max
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [setup, devteam, profiles, kanban]
    related_skills: []
---

# Generic Devteam

Geführte technische Einrichtung von Planner → Coding-Orchestrator/Codex →
unabhängigem Reviewer in einer vorhandenen Hermes-Installation. Du führst den
Nutzer linear durch bestätigte Eingaben, native Einrichtung und getrennte
Nachweise. Du baust weder einen Installerframework noch einen zweiten Dispatcher.

## Wann verwenden

- Der Nutzer beauftragt ausdrücklich ein neues Projektteam oder die Wiederaufnahme
  seiner begonnenen Einrichtung.
- Bei Paketautorenschaft/Review nur Dateien prüfen. Das Lesen dieses Skills erteilt
  keine Installation, Aktivierung, Dienst- oder Modellfreigabe.
- Fachliche Projektplanung folgt später als eigener Auftrag.

## Voraussetzungen

Linux, vorhandenes funktionsfähiges Hermes im bestehenden Benutzerkonto,
erreichbares Mattermost und Hindsight, autorisierte Modellzugänge. Ein geeigneter
Anbieter genügt; Hermes, Codex, Hilfsmodelle und Original-Agentpins separat prüfen.
Benötigte Werkzeuge folgen dem tatsächlichen Zielprojekt. Native Schutz- und
Freigabeeinstellungen bleiben erhalten. Geheimnisse nur über geschützte native
Eingabewege; keine Tokenwerte in Chat, Argumenten, Protokoll oder Git.

## Geführter Ablauf

1. Lade [Setup](references/setup.md) vollständig sowie den
   [Rollenbindungen](references/native-workflow.md). Beginne mit Zielbestand,
   Gateway-/Dispatcherzuständigkeit und gemeinsamen PM-Wirkungen, nicht mit Create.
2. Frage Projektname und kanonischen absoluten Workspace getrennt; leite den Pfad
   nicht aus dem Namen ab. Gleiche ihn mit Projektkontext und vorhandenen nativen
   Profil-/Boardbindungen ab; verschachtelte Checkouts bleiben erhalten.
   Kläre widersprüchliche Bindungen vor Anlage. Danach Bank, Rollennamen und Board einmal
   bestätigen; rollenfeste Texte ohne Persona-Abfrage verwenden. Bestätige
   technische Kennungen getrennt von Anzeigenamen, Modelle und genau eine
   Codeanalyse und Planner-Kommunikationsziele. Keine erneute Auswahl fester
   Rollen, Modi oder Komponenten. Lasse den konkreten Änderungsumfang freigeben.
3. Verwende die [private Protokollvorlage](templates/setup-record.md). Prüfe jede
   vorhandene Zielidentität vor Anlage; bei Wiederaufnahme native Objekte abgleichen.
4. Führe die Setupschritte in Reihenfolge aus: Profile/Modellbindung und privater
   Record, Board samt `kanban.auto_decompose: false` im dispatchenden Home und in
   jeder Rollenprofilkopie, Team-Codex/Originalkomponenten, Memory-/Messagingkonfiguration,
   eigene Skillbäume, personalisierte Rollen und endgültige Bindungen; danach erst Einzelprüfungen.
   Setze in jedem erzeugten Rollenprofil `security.protected_instruction_files: false`
   gemäß Setup; keine Änderung an der globalen Hermes-Konfiguration.
   Lade dazu [Integrationen](references/integrations.md),
   [Quellen](references/upstream-sources.md), beide [Codeanalysewege](references/code-analysis.md)
   und [Manifest](manifest.json); für das Board zusätzlich die
   [Kanban-Automatik](references/kanban-block-triage-escalation.md);
   richte genau die gewählte Alternative ein.
5. Halte bei fehlenden Voraussetzungen an der betroffenen Fähigkeit an. Prüfe
   Timeout-, Retry- und Rate-Limit-Behandlung am tatsächlichen Zielstand und kläre
   konkrete Probleme vor der betroffenen Nutzung.
   Dokumentierte Rezepte sind keine
   installierten Fähigkeiten; erster Index-/Querytest nur im separaten Testworkspace.
6. Nach gesonderter Aktivierungs-/Testfreigabe die tatsächlichen Zielkontexte,
   Modellwege, Modi, Memoryrequests, normalen Kanal-/DM-Dialog und Planner-Wake
   prüfen. Kleiner unabhängiger Pipelineweg in separatem Testworkspace, niemals
   beiläufig im Produktprojekt. Ergebnisse mit Belegen im Protokoll festhalten.
7. Übergebe eingerichtete Bindungen, Versionen, offene Voraussetzungen und den
   nächsten sicheren Schritt. Empfiehl anschließend einen konkreten ersten
   Planungsauftrag an den Planner; starte kein automatisches Projekt-Onboarding.

## Fallstricke

Profilanlage kann einen laufenden Multiplexer informieren. Pluginaufnahme und
selbst ein normaler CLI-Bootstrap können gemeinsame Dependencyarbeit auslösen.
Ein neues Profil ist trotz Neuanlage nicht zwingend modellkonfigurationsleer.
Team-Codex-Homes sind Arbeitszustand, keine OS-Sandbox. Eine SOUL-Erwähnung beweist
weder Skill-Discovery noch vollständige Promptaufnahme. Ein zugestellter Wake ist
kein planweiter Abschluss, und `queued` ist noch keine Zustellung. Ein aktiver
Auto-Decomposer (`kanban.auto_decompose: true`) macht aus einer zweimal gleichartig
blockierten Karte ungefragt neue Karten samt Parent-Kanten und zerlegt damit die
genehmigte Kette; der Wert gehört vor jeder Kette im dispatchenden Home und in den
Rollenprofilen auf `false` und rückgelesen.

## Verifikation

Lies jedes angelegte native Objekt und jede Zielausgabe zurück. Die
[Prüfanleitung](references/verification.md) trennt Paketprüfung, Teamfunktionen
und gemeinsamen Probelauf. Dateiprüfungen belegen kein Agentenverhalten.
Sind nur die Paketprüfungen bestanden, lautet das Urteil:
**„Paket geprüft; Setup-Laufzeitabnahme offen.“** Konkrete Fehler und ungeprüfte
Fähigkeiten bleiben ausdrücklich sichtbar.
