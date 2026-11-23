# Maker 2.14.3 — Reviewer-Bindung im Planner-Text

**Dokumentversion:** v4 — Risikoabschnitt korrigiert: er beschrieb eine Ausnahme als Ablaufweg; ersetzt durch die feste Kette und das tatsächlich beobachtbare Signal. v3 hielt die Entscheidung zu `planner.SOUL.md.template:80` fest, v2 den Ersatz durch die Streichung an `kanban-phase-release.md:50`.
**Status:** umgesetzt (2026-11-23), Pakettests grün: 266 Tests, `OK (skipped=1)`; die zwei betroffenen Testdateien einzeln 93 Tests, `OK`. Eingebaut auf Basis-Commit `6ecc3e4dfee8a2c7b966af0694a99ec82a08b172` (Maker 2.14.3) als **2.14.4**. Textstandard CAC: Entrypoint `cac` 1.2.0 und `/home/mariko/projects/cac/SKILL.md` samt Referenzen am 2026-11-23 gelesen. Kein Versionsbump für dieses Dokument: `docs/` ist laut `NOTICE.md` und `README.md` repository-only.

## Befund

`templates/roles/planner.SOUL.md.template:78` verlangt: „Set assignee, reviewer, workspace, dependencies, and required runtime fields natively." Der Reviewer ist an dieser Stelle nicht setzbar:

- `kanban_create` nimmt `title`, `assignee`, `body`, `parents`, `tenant`, `priority`, `workspace_kind`, `workspace_path`, `project`, `triage`, `idempotency_key`, `max_runtime_seconds`, `initial_status`, `skills`, `goal_mode`, `completion_contract`, `goal_max_turns`, `model` — kein `reviewer` (`tools/kanban_tools_schemas.py`, Schema `kanban_create`).
- `reviewer` existiert nur an `kanban_request_review` („Optional reviewer profile; reassigns the task before review dispatch"). Diesen Aufruf macht der Coder: `templates/roles/coder.SOUL.md.template:76` übergibt `reviewer="{{REVIEWER_PROFILE}}"`. `request_review` protokolliert Implementer und Reviewer am Event (`hermes_cli/kanban_db.py`, `request_review`).
- Die Handoff-Prüfung existiert als ausführbare Anweisung: `skills/brownfield-feature-planning/references/kanban-status-inspection.md:69` — „On handoff, verify reviewer assignment and implementer `review_requested` provenance."

Folge im Betrieb: Der Planner konnte die Zeile am 2026-11-22 nicht erfüllen und schrieb sich die Lücke selbst in seine installierte Skill-Kopie — `skill_manage`-Patch in Session `20261122_162036_3ac688` (16:37:24) auf `kanban-phase-release.md` und in Session `20261122_171015_5594a979` (17:12:06). Eine Anweisung, die die Rolle nicht ausführen kann, erzeugt Rollen-Prosa; die Zeile ist die Ursache, nicht der Zusatz.

## Entscheidung

Der Planner setzt nur, was `kanban_create` annimmt. Die Anforderung „Reviewer auf der Karte setzen" fällt weg, statt durch eine Beschreibung des Coder-Verhaltens ersetzt zu werden: Der Maker-Defekt ist die Anweisung. Eine Beschreibung ist keine Anweisung — sie gibt der Rolle nichts zu tun und wiederholt die Aufgabe einer anderen Rolle.

Die Reviewer-Prüfung geht nicht verloren: Sie steht als Handlung am Handoff (`kanban-status-inspection.md:69`), wo sie beobachtbar ist.

## Änderungen

Jede ALT-Zeichenkette am 2026-11-23 gegen die jeweilige Datei hochgezählt (`read_text().count(...)`), erwartet und gefunden: **1**.

### 1. `templates/roles/planner.SOUL.md.template:78`

ALT:

```
   Set assignee, reviewer, workspace, dependencies, and required runtime fields natively.
```

NEU:

```
   Set assignee, workspace, dependencies, and required runtime fields through the Kanban tools.
```

### 2. `templates/roles/planner.SOUL.md.template:79` (Schritt 8)

ALT:

```
8. Create dependent tickets `blocked`. Verify complete parent chain, assignee, reviewer, board `{{KANBAN_BOARD_NAME}}`, workspace, plan baseline and Planner wake subscription before any `todo` release.
```

NEU:

```
8. Create dependent tickets `blocked`. Verify complete parent chain, assignee, board `{{KANBAN_BOARD_NAME}}`, workspace, plan baseline and Planner wake subscription before any `todo` release.
```

### 3. `skills/brownfield-feature-planning/references/kanban-phase-release.md:50` — Streichung

ALT (eine Zeile, eingerückt unter Schritt 3):

```
   Set the independent Reviewer profile explicitly on every implementation card and read it back. A card bound to the Planner or the Coder is not independently reviewed.
```

NEU: entfällt ersatzlos; Schritt 3 endet mit der Kartenprüfung in Zeile 49.

Begründung: Der Satz verlangt ein Feld, das es nicht gibt (siehe Befund), und ist damit eine Aufgabe ohne Adressat. Die zugehörige Handlung steht bereits als Handoff-Prüfung in `kanban-status-inspection.md:69`. Ein Ersatzsatz, der erklärt, dass der Coder den Reviewer bindet, wäre Prozessbeschreibung einer anderen Rolle — untersagt durch `planner.SOUL.md.template:78` („Omit … restatements of role duties or workflow") und `reviewer.SOUL.md.template:113` („omit … from ticket prose").

### 4. Tests

| Datei | Änderung |
|---|---|
| `references/test_render_reasoning.py:811` | Vertragssatz „Set assignee, reviewer, workspace, dependencies, and required runtime fields natively" durch „Set assignee, workspace, dependencies, and required runtime fields through the Kanban tools" ersetzen (je 1 Vorkommen) |
| `references/test_build_evidence.py:119-131` | Der Satz aus Änderung 3 wird nicht mehr geprüft; statt dessen die überlebende Handlung: `kanban-status-inspection.md` lesen und „verify reviewer assignment and implementer `review_requested` provenance." assertieren. Die zwei übrigen Release-Sätze der Schleife bleiben |

Die Deckung der Reviewer-Prüfung bleibt damit gleich stark, sie zeigt nur auf den Ort, an dem die Anweisung jetzt steht.

## Umsetzung

- Geändert: `templates/roles/planner.SOUL.md.template` (zwei Zeilen), `skills/brownfield-feature-planning/references/kanban-phase-release.md` (eine Zeile entfernt), `references/test_render_reasoning.py` und `references/test_build_evidence.py` (je eine Vertragszeile), `SKILL.md` und `manifest.json` (Version 2.14.4).
- Abweichung vom Plan: keine. Die Testanpassung in `test_build_evidence.py` prüft statt des gelöschten Satzes die überlebende Handoff-Zeile; die zwei übrigen Release-Sätze der Schleife bleiben unverändert.
- Lauf: `references/test_build_evidence.py` und `references/test_render_reasoning.py` einzeln — 93 Tests, `OK`. Gesamtsuite `python3 -B -m unittest discover -s . -p 'test_*.py'` — 266 Tests in 466 s, `OK (skipped=1)`.
- Restvorkommen geprüft: `grep` nach „Set the independent Reviewer profile" und „required runtime fields natively" über `templates/`, `skills/`, `references/` liefert null Treffer.

## Zurückgezogen gegenüber v1

**NEU-Satz für Zeile 50:** „Review is bound by the Coder's native review request to the team's Reviewer profile. Verify that the actual review event names that profile; a review bound to the Planner or the Coder is not independent."

Von Max am 2026-11-23 verworfen, drei Gründe:

1. Der erste Satz ist keine Anweisung, sondern die Beschreibung einer Tatsache, die durch die Coder-SOUL gewährleistet wird. Der Planner kann damit nichts anfangen; CAC verlangt die Handlung des Adressaten, nicht die Wahrheit über eine andere Rolle.
2. Der zweite Satz prüft etwas, das niemand mehr setzen soll: Ohne Setz-Anweisung bleibt offen, worauf sich die Prüfung bezieht.
3. Er wiederholt die Aufgabe einer anderen Rolle und verstößt damit gegen `planner.SOUL.md.template:78` („Omit team setup, routine procedures and restatements of role duties or workflow from the body") und gegen `reviewer.SOUL.md.template:113` („omit … from ticket prose").

Ebenfalls verworfen (unverändert aus v1): die Bedingungssatz-Variante („If the installed Kanban exposes reviewer assignment only on the native review-request transition …"); das Einschränken der Rollen beim Ändern eigener Skills — Rollen dürfen ihre installierten Skills anpassen, und nach der Experimentierphase laufen Teams ohne Datei-Updates; der Orphan-Codex als Textregel — Ursache war die zu kurze Wartezeit, korrigiert über Konfiguration im Setup-Rezept 2.14.1/2.14.3.

## Entschieden: Zeile 80 bleibt unverändert

`templates/roles/planner.SOUL.md.template:80` (Schritt 9): „Assign implementation to `{{CODER_PROFILE}}`; direct review to `{{REVIEWER_PROFILE}}`."

Max am 2026-11-23: Die Zeile hat in den Läufen keinen Fehler verursacht und bleibt. Sie ist damit nicht Teil dieses Changesets und wird nicht weiter bewertet.

## Wo die Reviewer-Prüfung tatsächlich stattfindet

- Wer: nur der Planner. `manifest.json` → `own_skills.brownfield-feature-planning.targets.hermes = ["planner"]`; installiert ausschließlich in `profiles/jack`. Coder und Reviewer erhalten die Skill nicht.
- Wann: `skills/brownfield-feature-planning/SKILL.md:104` — „Status, completion, review, or blocker notification | Status inspection"; die Referenz selbst beginnt mit „Trigger: handoff, completion, or blocker notification."
- Handlung dort: `kanban-status-inspection.md:69` — „On handoff, verify reviewer assignment and implementer `review_requested` provenance."
- Nutzungsbeleg: 39 Ladevorgänge dieser Referenz in den Planner-Sessions (jack `state.db`, Stand 2026-11-23; darunter der Blocker-Wake am 2026-11-22 17:10).

## Voraussetzungen und Aufwand

- Freigabe für ein Maker-Changeset; ein Bump auf **2.14.4** (PATCH, reine Text- und Teständerung) für `SKILL.md` und `manifest.json`.
- Suite einmal am Ende: `python3 -B -m unittest discover -s references -p 'test_*.py'`, erwartet `OK (skipped=1)`; vorher die zwei betroffenen Testdateien einzeln.
- Aufwand: vier Dateien (zwei Templates, eine Referenz, zwei Testdateien), ein Commit.

## Risiko

Keine neue Ausnahme. Die Bindung ist ein gerendertes Literal in der Coder-SOUL (`coder.SOUL.md.template:76`), Reihenfolge, Assignee und Review sind zur Laufzeit fest (`planner.SOUL.md.template:86`). Beobachtbar wird eine Abweichung allein am Handoff: `reviewer` ist optionaler freier Text (`tools/kanban_tools.py:890-899`), ohne ihn geht die Karte trotzdem nach `review`, aber auf dem aktuellen Assignee — die Karte stünde dann in `review` mit dem Coder als Assignee.

Diese Änderung erzeugt den Fall nicht und ändert seine Erkennung nicht: Die Prüfung steht unverändert an `kanban-status-inspection.md:69` und läuft bei der Notification, die den Planner ohnehin dorthin führt. Verschoben wird nur der Ort der Formulierung im Paket.

## Grenzen

- Nicht installiert, kein Rollout, keine Teamänderung durch dieses Dokument.
- Bestehende Teams erhalten den Text erst mit ihrem nächsten Datei-Update.
- SG1 steht nach dem heutigen `apply` auf Maker 2.14.3 (Dateien); Wartekonfiguration und die zwei read-only-Grants sind noch nicht geschrieben, die Entscheidung dazu liegt bei Max.
