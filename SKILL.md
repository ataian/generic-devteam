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
   [Bindungsvertrag](unklar/references/native-workflow.md). Beginne mit Zielbestand,
   Gateway-/Dispatcherzuständigkeit und gemeinsamen PM-Wirkungen, nicht mit Create.
2. Frage Projektname/Workspace zuerst; gleiche den absoluten Workspace auf dem
   Zielkonto mit `~/projects/<PROJECT_NAME>` aus der festen Reviewer-Vorlage ab.
   Kläre Abweichungen vor Anlage. Danach Bank, Rollennamen und Board einmal
   bestätigen; rollenfeste Texte ohne Persona-Abfrage verwenden. Bestätige
   technische Kennungen getrennt von Anzeigenamen, Modelle und genau eine
   Codeanalyse und Planner-Kommunikationsziele. Keine erneute Auswahl fester
   Rollen, Modi oder Komponenten. Lasse den konkreten Änderungsumfang freigeben.
3. Verwende die [private Protokollvorlage](templates/setup-record.md). Prüfe jede
   vorhandene Zielidentität vor Anlage; bei Wiederaufnahme native Objekte abgleichen.
4. Führe die Setupschritte in Reihenfolge aus: Profile/Modellbindung und privater
   Record, Board, Team-Codex/Originalkomponenten, Memory-/Messagingkonfiguration,
   eigene Bäume/Policy und endgültige Bindungen; danach erst Einzelprüfungen.
   Lade dazu [Integrationen](references/integrations.md),
   [Quellen](references/upstream-sources.md), beide [Codeanalysewege](references/code-analysis.md)
   und [Manifest](manifest.json); richte genau die gewählte Alternative ein.
5. Halte bei fehlenden Voraussetzungen an der betroffenen Fähigkeit an. Insbesondere
   bleibt G1 vor automatischer Dispatchfreigabe gesperrt, bis eine endliche native
   Gesamtgrenze belegt oder die Anforderung ausdrücklich geändert ist.
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
kein planweiter Abschluss, und `queued` ist noch keine Zustellung.

## Verifikation

Lies jedes angelegte native Objekt und jede Zielausgabe zurück. Die öffentlichen
[Dateitests](README.md) prüfen Paketdaten und den reinen Textweg, nicht das
Verhalten eines Agenten. Ohne echte Zielabnahme lautet das Urteil:
**„Paket geprüft; Setup-Laufzeitabnahme offen.“** G1 und die noch offenen
Codeanalyse-Funktionsnachweise bleiben dabei ausdrücklich sichtbar.
