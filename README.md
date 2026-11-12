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
Hermes/distribution skills and existing services remain operator prerequisites; Maker does not pin, install, upgrade or repair Hermes or the Hindsight service.
The manifest locks independently delivered upstream assets to exact commits; setup and team updates consume those pins without a fresh latest-version search.
First Codex/analysis runtime installation can be included in the disclosed upfront setup scope; preserve existing/shared installations unless their concrete change is explicitly approved.

## Voraussetzungen

- Eigene Linux-Umgebung, vorhandenes laufendes Hermes und bestehendes Benutzerkonto.
- Bereits erreichbare Mattermost-/Hindsight-Dienste, berechtigte Zugänge und ein
  geeigneter Modellanbieter. Hermes- und Codex-Anmeldung werden separat geprüft.
- Complete preparation decisions for project/workspace and repository boundaries, role display names,
  derived IDs/collision resolution, actual native models/providers and reasoning, exactly one analysis branch,
  Codex Git identity/access, bank/board create-or-reuse, communication permissions, and execution scope.
- Compatible Codex and chosen analysis runtime, or their disclosed approved first installation. Authorized profile-local installations, shared PM effects,
  and activation. No server/account/daemon provisioning or project toolchain qualification.

## Direkt aus dem Checkout verwenden

Für Setup und Updates benötigt der ausführende Agent einen schlanken Maker-Wrapper oder eine passende eigene Adaption.
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
The Reviewer uses a separate fresh-context pass for material security, data-integrity, transaction, or concurrency invariants.
This requirement does not duplicate every test suite or restart the full review after each correction.
The Reviewer reuses valid evidence and reruns affected checks while retaining required independent and final-state acceptance checks.
Planner, Coder, Reviewer and Team-Codex receive the selected complete Graphify/CBM integration, including native configuration and discovery readbacks.
Reviewer retains conditional library-version/consumer and independent visual acceptance checks without the three implementation-oriented skill bundles.
Package changes do not activate these rules in existing teams; use the separately authorized team-update procedure.
The Coder owns implementation decisions within the accepted goal and binding constraints.
Reviewer findings and customer-decision questions return to the Coder first; only the Coder escalates a missing customer decision through needs-input to the Planner.
The Planner checks actual blockers and coordinates sufficient customer answers in Mattermost.
Technical interruptions preserve unfinished review; approval completes the exact reviewed commit directly to DONE.
Work continues while a justified next approach remains, within explicit customer limits, provider quotas, operational permissions, and native safeguards.
After the last required ticket reaches DONE, the Planner sends a short customer report from existing results and independent verdicts, without a closing ticket or another technical review.
The file helper retains obsolete copies. Complete the [required version-gated Reviewer skill retirement](references/update.md#required-reviewer-skill-retirement-1122) after file application within the approved team update; preserve all assets outside its exact scope.
The Planner receives Matt Pocock's original `grill-me`, `grilling`, `domain-modeling`, and `to-questionnaire` skills at the same pinned revision.
Its SOUL requires `grilling` for requirements and conditionally loads domain modelling during that interview.
Glossaries capture vocabulary; requirements and phase gates remain in the accepted plan. Unaccepted ADRs remain proposed.
Coder and Reviewer consume relevant accepted definitions through existing routing; role authority and native dispatch remain unchanged.
Interview, design, and explicit plan acceptance remain separate. Acquisition and readbacks use the [integration recipe](references/integrations.md#grill-me).
Use `to-questionnaire` on request to draft a Markdown questionnaire for one external expert; creation does not authorize sending or accepting new scope.
The Planner decomposes work by actor, behaviour, benefit, and independently verifiable outcomes, not technical layers.
Necessary foundations trace to enabled stories; stories, phases, and tickets need not map one-to-one.
Tickets use concise user-story titles and structured bullets: goal/context, acceptance criteria, technical implementation, verification, dependencies and exact plan/phase/commit binding.
Cards remain understandable alone, aligned with the authoritative accepted plan, and subject to Coder implementation discretion.
Plans and ticket text use glossary vocabulary and relevant accepted ADRs, including without active domain modelling.
Plan synthesis states the user's problem and user-visible solution, concrete test seams and analogous tests, meaningful scope boundaries, and decisions clarified by actual prototypes.
Broad mechanical changes use conditional Expand–Migrate–Contract planning with working, verified intermediate states and existing native dependency/review gates.
These are bounded adaptations of Matt Pocock's `to-spec` and `to-tickets`, not installations of either skill or a new tracker/approval workflow.
Team-Codex receives the owned [diagnosing-bugs](skills/diagnosing-bugs/README.md) adaptation; Coder explicitly invokes it and validates original evidence without repeating full diagnosis.
Concrete symptom/cause evidence and an exact reproducible check preserve the direct-fix path for clear bugs.
Unclear or competing causes, intermittent/state-dependent failures, performance isolation, or an unresolved/recurring apparent fix trigger the full method, including regressions emerging during ordinary implementation.
Existing Planner routing, risk-sensitive verification, and independent review remain unchanged; complete-tree setup/update and native discovery checks do not prove live behavior.
Relevant module/interface choices use caller-contract, complexity-encapsulation, abstraction-removal, and present-variability checks within existing design work.
The Planner also receives the owned [retro skill](skills/retro/README.md), adapted from Matt Pocock with full-process token economy.
Request it with `/retro`, “Machen wir eine Retro zum letzten Lauf”, or a named historical session, ticket, or project.
It proposes source-backed process/environment improvements, not product acceptance; it changes nothing automatically and remains separate from `/refine`.
Setup and updates check native name/command collisions and load the complete skill tree without running a retrospective.
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
The file helper does not install runtime components, stop workers, or restart sessions.
The mandatory prose companion path compares all assigned upstream assets on every update, even at the same Maker version.
Restore missing selected Reviewer analysis assets and bindings through that approved path, including previously retired assets and already-current installation metadata.
Any full plugin update and any CBM/Graphify runtime or Team-Codex CLI change requires advance explicit approval of actual targets, versions and shared effects.
Pins do not grant that permission; deferred required companion work leaves the team update incomplete.
For the incompatible `2.0.0` routing change, use [Workflow migration](references/update.md#workflow-migration-200) before applying authority changes.
Settle active old-contract work, distinguish an active Planner review return from parked-card recovery, and preserve same-card history and unrelated local adaptations.
Verify subsequent-context loading separately from saved files; a clean merge or newer package version does not prove migration completion.
Report skipped and failed teams separately.

## Setup output verification

Use [Verification](references/verification.md) for ordinary setup output readbacks and baseline completion.
Reuse evidence from each step; do not add synthetic memory, helper, communication, coding/review, or indexing trials.
Report real incomplete bindings precisely. Excluded behavior tests are outside scope, not pending gates.
The completion statement requires the private installation marker and pristine personalized baselines.

## Maker development and review

For agent-instruction authoring/review, load the standalone [TAS upstream](references/upstream-sources.md#tas).
This Maker contains no maintained TAS copy and installs no TAS into team roles.
The manifest pin identifies published TAS `1.1.0`, including its writing-for-agents adaptation; record any commissioned local changes separately.

For explicitly requested authoring/review or separately commissioned behavioral qualification,
use [Development verification](references/development-verification.md).
Its package, renderer, updater and recovery regressions are development checks, not per-team setup duties.
Package tests do not prove live behavior, runtime reload, or independent review.
