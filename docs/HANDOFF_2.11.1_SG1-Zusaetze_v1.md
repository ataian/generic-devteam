# SG1 auf Maker 2.11.1 — offene Entscheidung zu sechs lokalen Zusätzen

**Dokumentversion:** v1 — erste Fassung, Entscheidungsgrundlage.
**Status:** proposed; Team-Update angehalten. Nichts an SG1 wurde geschrieben.
**Datum:** 2026-11-20 · **Entscheider:** Max, in einer Folgesitzung.

## Stand

| Feld | Wert |
|---|---|
| Team | SG1 — Planner `jack`, Coder `carter`, Reviewer `daniel`, Team-Codex `carter/devteam/user-home` |
| Maker-Quelle | `/home/mariko/projects/generic-devteam`, Branch `cac`, Arbeitsbaum clean |
| Von | `2.10.0` (`65903e5467d471f552cd1c5f0aa81b1055b74083`), letzter Lauf `b9555111d9854713bbee32f80165c39b` |
| Auf | `2.11.1` (`b589e4afcd21644f3defeb3831fb4bd672a3ee11`) |
| Proposal | `/home/mariko/.hermes/profiles/jack/devteam/proposals/a94fafdc7a7547369dd8b6b96ca8e929.json` |
| Umfang | 51 Einträge, 25 geändert, **3 Konflikte**, 0 `obsolete`, 6 `dependencies` |
| Suite | nicht gelaufen (kein Maker-Diff) |

Geändert: alle drei SOUL-Templates, 9 Mindest-Skill-Bäume, davon die drei Planner-Referenzen im Konflikt.

`dependencies` (unverändert gegenüber 2.10.0 nur bei diesen Dateien): `references/integrations.md`, `references/setup.md`, `references/code-analysis.md`, `references/native-workflow.md`, `references/kanban-block-triage-escalation.md`, `manifest.json:upstream_components`.

## Was 2.11.1 inhaltlich ist

CAC (Compact Artifact Contract): neue Team-Codex-Anweisungsdatei `templates/team-codex-AGENTS.md` (`+8` Zeilen, Manifest-Datei), `references/cac-authoring.md` neu, alle Rollen- und Skilltexte auf knappe Form umgeschrieben. Die Upstream-Pins `caveman`, `caveman-review` und `tas` fallen auf `null`; alle übrigen Pins (`superpowers`, `ponytail`, `codebase-memory`, `codex-cli`, `graphify`, `hindsight`, `sdlc-review`, `grill-me`, `find-skills`, `codex-custom-agents`, `hermes-codex`, `hermes-core`) sind zwischen beiden Commits identisch.

## Bereits geprüft (read-only)

- **Aktivität:** Board `sg1` hat 3 Tasks, alle `done`, `task_runs` ohne `running`/`claimed` (letzter Run 55, `daniel`, `done`). Die vier sichtbaren PIDs sind ausschließlich `codebase-memory-mcp` — der bekannte Fehlalarm des Helfers, kein Board-Betrieb.
- **Planner-Kanban-Bindung:** `kanban` steht für `cli`, `mattermost` und `api_server`; `agent.disabled_toolsets` = `[]`. Keine Konfigurationsänderung nötig.
- **Caveman-Bestand, Retirement-Fähigkeit:** fünf Bäume (`jack/skills/caveman`, `carter/skills/caveman`, `daniel/skills/caveman`, `daniel/skills/caveman-review`, `carter/devteam/user-home/.agents/skills/caveman`) sind byte-genau der gepinnte Stand `1e91f1306d602d4ca23618701b1185575ae1869b`; zusätzlich liegen nur die Lizenzdateien `LICENSE`, `LICENSE-MIT`, `NOTICE` (in den zwei Cartern-Bäumen zusätzlich `LICENSING.md`) — laut Setup-Record Teil der damaligen Auslieferung. `skills.auto_load` = `[caveman]` in allen drei Rollen.

## Die drei Konflikte

Der Maker hat diese drei Dateien vollständig neu geschrieben (`brownfield-feature-planning/SKILL.md` 208 → 113 Zeilen). Jeder lokale Zusatz liegt dadurch im umgeschriebenen Bereich, und `git merge-file` bricht ab. `update_team.py apply` verweigert konfliktbehaftete Proposals grundsätzlich. Es gibt drei saubere Wege: Zusätze vorher in den Maker übernehmen (dann läuft das Team-Update konfliktfrei), Zusätze fallen lassen, oder die drei Dateien bleiben unangetastet.

Fundstellen sind die installierten Dateien unter `/home/mariko/.hermes/profiles/jack/skills/brownfield-feature-planning/`.

### 1 — `SKILL.md:146-147`, Plan-Staging; im neuen Stand nicht vorhanden

> Check the planning repository's ignore rules before staging a new plan; an explicit document allowlist can hide an otherwise valid amendment from `git status`.
> Extend such an allowlist only for the authorized filename; keep operational data and nested repositories excluded rather than bypassing the boundary with broad force-adds.

Empfehlung: aufnehmen. Trifft jedes Projekt mit Doku-Allowlist.

### 2 — `SKILL.md:174-175`, Amendment an eingefrorener Basis; nicht im neuen Stand

> When preserving a frozen base, state the amendment's exact precedence and replace contradictory active ticket instructions; merely appending permission leaves workers with conflicting requirements.
> Bind the frozen documents and amendment to their respective exact commits.

Empfehlung: aufnehmen. Projektunabhängige Amendment-Regel.

### 3 — `references/kanban-status-inspection.md:69`, Run-Identität; nicht im neuen Stand

> Use the JSON run `id` in reports, not a formatted CLI row number; task-local display ordinals can differ from durable run identities.

Empfehlung: aufnehmen.

### 4 — `references/kanban-status-inspection.md:92` (Satz 5), Handoff-Evidenz; nicht im neuen Stand

> If the handoff places acceptance evidence or limitations in run metadata, read those fields rather than treating the latest comment as the complete result.

Empfehlung: aufnehmen. Verhindert, dass vorhandene Evidenz als leer gilt.

### 5 — `references/kanban-status-inspection.md:110-116`, eigener Abschnitt; im neuen Stand nicht vorhanden

> ## Inspect a changes-requested return
>
> 1. Read the latest independent-reviewer verdict and native `changes_requested` event, including the exact rejected commit and remaining findings.
> 2. Re-read current task/run state; the native review transition may already have reassigned and queued the original implementer, or the dispatcher may already have started correction.
> 3. Leave that same-card return intact. Do not apply ordinary blocker-unblock recovery, reopen review, create a replacement card, or manually dispatch work that is already ready or running.
> 4. Keep resolved findings resolved unless new evidence reopens them. Route only the outstanding in-scope correction and its required regression to the implementer; repeated review rounds alone do not require a new scope decision.
> 5. Verify the successor remains parent-gated and report queued versus started correction precisely. A `BLOCK` verdict is rejection, not approval, and does not by itself prove the board status is `blocked`.

Empfehlung: aufnehmen. Eigene Prozedur, die der neue Stand gar nicht führt.

### 6 — `references/kanban-triage-recovery.md:153-159`, sieben Zeilen; der neue Stand deckt rund die Hälfte

> Read the blocked event's `source_status`, prior handoff and required continuation before selecting a transition.
> Inspect installed CLI help and native transition semantics; a command name alone does not establish its recovery role.
> When native `unblock_task` restores event-derived review phase, use `kanban_unblock` for a resolved review-origin block.
> Require satisfied parents and read back `review` or an actual reviewer claim, unchanged reviewer assignment and original implementer handoff.
> Installed `reopen_review_task` can mean `review` to `ready`/`todo` with reassignment to the original implementer.
> Use that operation only for an authorized implementer return, not interrupted-review restoration.
> If a transition refuses the current state, re-read state and semantics before another transition; do not force a status change.

Neu steht bereits (Zeilen 21, 77-78 der neuen Fassung): „Before reopening, verify prior handoff and required continuation. Leave pending review acceptance with the Reviewer.", „Inspect local help before `hermes kanban --board <board> reopen-review <task>` … same version/identity checks before `reopen_review_task(conn, task_id)`", „Once blocker is resolved, parents satisfied, and target runs ended, use `kanban_unblock(task_id=..., board=...)` from the authorized orchestrator."

Echt zusätzlich sind vier Aussagen: `source_status` lesen; „ein Kommandoname belegt keine Wiederherstellungsrolle"; `reopen_review_task` kann auf den ursprünglichen Implementierer umhängen und ist nur für autorisierte Rückgabe, nicht für unterbrochenen Review; bei Ablehnung Zustand neu lesen statt erzwingen.

Empfehlung: gekürzt aufnehmen, nicht wörtlich 1:1.

## Zur Entscheidung

Vier mögliche Ergebnisse, je mit Folge für das Team-Update:

| Entscheidung | Folge |
|---|---|
| 1–5 vollständig, 6 gekürzt (**Empfehlung**) | Maker-Changeset 2.11.2 mit Suite-Lauf, danach SG1 konfliktfrei auf diesen Commit |
| 1–5 vollständig, 6 entfällt | dasselbe, ein Schritt weniger |
| alle sechs wörtlich 1:1 | dasselbe, mit Doppelungen in der Triage-Referenz |
| keiner | Maker-Text gewinnt; die drei Dateien werden auf den neuen Stand gesetzt, die Zusätze entfallen |

Die Übernahme in den Maker braucht: Änderung an `skills/brownfield-feature-planning/SKILL.md`, `references/kanban-status-inspection.md`, `references/kanban-triage-recovery.md`, SemVer-Bump (`SKILL.md` + `manifest.json`), Lauf von `python3 -B -m unittest references.test_brownfield_planning` und der Gesamtsuite inklusive Größenbudget-Check. Commits und Push liegen bei Max.

## Bereits entschieden

Caveman-Stilllegung (CAC) läuft im selben Zug wie das Datei-Update, mit Backup, Quarantäne der fünf Bäume, Entfernen von `caveman` aus den drei `skills.auto_load`-Listen und vollständigen Readbacks. Gilt unabhängig von der Konfliktentscheidung; die Stilllegung setzt aber einen erfolgreichen `apply` voraus.

## Nächste Schritte in der Folgesitzung

1. Entscheidung zu den sechs Zusätzen treffen.
2. Bei Übernahme: Maker-Changeset, Suite grün, neuer Commit als Update-Ziel.
3. `plan --home /home/mariko/.hermes/profiles/jack --target <commit>` neu erzeugen, auf `conflicts 0` prüfen.
4. `apply` mit `--activity-decision proceed`, `--semantic-review '<Befund>'`, `--dependency-decision '<Entscheidung>'`.
5. CAC: Anweisungsdatei nach `carter/devteam/codex-home/AGENTS.md` (CBM-Zeiger bleibt), fünf Bäume in Quarantäne, `skills.auto_load` in `jack`/`carter`/`daniel` auf den Rest kürzen, Readbacks, Eintrag in `devteam/setup.md`.
6. Nullprobe: erneuter `plan` → `changed 0`, `conflicts 0`, `obsolete 0`.
