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

**Delivery boundary:** This is a `setup-recipe` package. Normal setup checks available prerequisites,
performs authorized profile-local installation/configuration, reads back its outputs, and saves the versioned installation baseline.
Completion is **Team configured; setup outputs verified**. Configuration/file readbacks do not guarantee live team behavior.
Missing shared runtimes/services are operator prerequisites, not an instruction to install or repair them.

## Voraussetzungen

- Eigene Linux-Umgebung, vorhandenes laufendes Hermes und bestehendes Benutzerkonto.
- Bereits erreichbare Mattermost-/Hindsight-Dienste, berechtigte Zugänge und ein
  geeigneter Modellanbieter. Hermes- und Codex-Anmeldung werden separat geprüft.
- Complete preparation decisions for project/workspace and repository boundaries, role display names,
  derived IDs/collision resolution, actual native models/providers and reasoning, exactly one analysis branch,
  Codex Git identity/access, bank/board create-or-reuse, communication permissions, and execution scope.
- Available Codex and chosen analysis runtime. Authorized profile-local installations, shared PM effects,
  and activation. No server/account/daemon provisioning or project toolchain qualification.

## Direkt aus dem Checkout verwenden

Für Setup und Updates benötigt der Main-Agent einen schlanken Maker-Wrapper oder eine passende eigene Adaption.
Der [Bootstrap-Prompt](references/main-agent-wrapper.md) beschreibt diesen Einstieg.

Öffne den Checkout im vorhandenen Hermes und beauftrage:

> Read repository-root `SKILL.md` and its required setup references. Configure my new team.
> Group all foreseeable choices during preparation, show the complete parameters and concrete changes,
> disclose later protected login/hook approval and `/sethome` actions, then obtain the start decision.
> Do not begin product work.

Dieser dateibasierte Einstieg benötigt keine vorherige Registrierung des Makers
im Skillkatalog. Für dauerhaftes Laden über den Skillnamen folgt die Installation.

## Einmal installieren, anschließend geführt aufrufen

Dies ist eine Anleitung für den künftigen Nutzer, keine Aufforderung, beim Lesen
oder Bauen des Pakets ein Setup auszuführen.

1. Obtain the complete package tree from the repository root or a separately authorized archive.
   Use the exact manifest inventory: entry, README, manifest, legal files, authoring instructions, references, templates and complete own skills.
   Exclude repository-only `docs/`, `HERMES.md`, Git metadata, `.gitignore`, and `vortrag/` from package accounting and installation.
   See [NOTICE](NOTICE.md) and [Sources](references/upstream-sources.md) for provenance and licenses.
2. Ermittle das tatsächliche Home des Hermes-Profils, in dem du den Maker aufrufen
   willst, über die vorhandene Profilkonfiguration. Prüfe vor jedem CLI-Aufruf
   mögliche Bootstrap-/PM-Wirkungen gemäß [Setup](references/setup.md).
3. Nach Freigabe kopiere diesen vollständigen Baum in dessen
   `skills/generic-devteam/`. Existiert das Ziel, vergleiche zuerst Herkunft und
   lokale Änderungen; niemals fremde Anpassungen überschreiben. Die vollständigen
   eigenen Skillbäume behalten ihre `SKILL.md`.
   Copy complete skill trees to their assigned targets.
   Personalize role templates and bind only the recovery launcher through the Maker setup step.
   Keep all other skill bytes unchanged.
4. Prüfe in diesem Profil native Discovery von `generic-devteam`, lade `SKILL.md`
   und `references/setup.md` ausdrücklich. Der bestehende Sitzungskatalog und ein
   neu aufgelöstes Skillpaket sind unterschiedliche Nachweise; keinen globalen
   Gatewayrestart allein zur Katalogaktualisierung auslösen.
5. Beauftrage im Ziel-Hermes beispielsweise:

   > Load generic-devteam. Complete grouped preparation for my new team before any setup writes.
   > Present all parameters, changes and disclosed deferred interactions for the start decision.
   > Configure and verify setup outputs; do not begin product work.

Complete independent questions together and dependent choices within preparation.
Offer the Sol default set once: Planner fixed high; Hermes Coder fixed medium;
Reviewer and Team-Codex default medium, maximum high.
Resolve actual supported native model/provider IDs separately; never submit `sol-medium`/`sol-high` shorthand as guessed IDs.
Preserve confirmed overrides and resolve unavailable defaults before starting.
Derive new native IDs under [Setup](references/setup.md#new-profile-ids); preserve existing IDs.
Do not ask separately about valid derived IDs or add a persona.
Protected login, native hook approval and genuine DM `/sethome` may require created targets;
disclose these interactions upfront and keep secrets in protected native paths.

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
Für neue Planungen erhält der Planner die Originalskills `grill-me` und `grilling`
von Matt Pocock. Seine SOUL verlangt `grilling` für die Anforderungsklärung;
Interview, Entwurfsarbeit und ausdrückliche Planannahme bleiben getrennt.
Bezug und Prüfung stehen im [Integrationsrezept](references/integrations.md#grill-me).
Bei Unterbrechung den Maker mit dem privaten Setuprecord wieder aufrufen; er liest
native Profile, Board und Dienstobjekte erneut und setzt am ersten offenen Gate
fort. Kein blindes Wiederholen von Create, Login, Bank- oder Kanalanlage.

Updates zunächst außerhalb aktiver Discovery prüfen, mit installierten Revisionen
und eigenen Anpassungen vergleichen und den gezielten Änderungsumfang genehmigen
lassen. Vorherige eigene Dateistände geschützt aufbewahren. Rückbau betrifft nur
protokollierte eigene Objekte/Einträge; Datenlöschung braucht eine eigene Freigabe.

## Update existing teams

To request a file update, ask: “Check the Maker for changes and apply them to my local teams.”
Read [Team updates](references/update.md) before changing any team files.
The updater uses existing setup values, per-team installation evidence, and pristine personalized baselines.
It preserves local edits through a three-way comparison.
It requires semantic review and an explicit activity decision before application.
It retains backups and provides a guarded rollback.
It does not install runtime components, stop workers, or restart sessions.
Report skipped and failed teams separately.

## Setup output verification

Use [Verification](references/verification.md) for ordinary setup output readbacks and baseline completion.
Reuse evidence from each step; do not add synthetic memory, helper, communication, coding/review, or indexing trials.
Report real incomplete bindings precisely. Excluded behavior tests are outside scope, not pending gates.
The completion statement requires the private installation marker and pristine personalized baselines.

## Maker development and review

For explicitly requested authoring/review or separately commissioned behavioral qualification,
use [Development verification](references/development-verification.md).
Its package, renderer, updater and recovery regressions are development checks, not per-team setup duties.
Package tests do not prove live behavior, runtime reload, or independent review.
