# PLAN 2.8.17 — Plan-Review-Findings

| Feld | Wert |
|---|---|
| Datum | 2026-11-15 |
| Basis | Maker 2.8.16, Branch `v3`, HEAD `0931b49` |
| Quelle | `docs/HANDOFF_2.8.16_Plan-Review_Entscheidungen_v1.md` (Punkte 1, 2, 6, 7, 8, 9) |
| Zielversion | 2.8.17 (PATCH) |
| Nicht enthalten | Punkte 3, 4, 5 (keine Änderung), Punkt 10 (offen), Baustelle 2 (`HANDOFF_2.8.16_Updater-Skill-Abbau_v1.md`) |

Alle NEU-Texte sind wörtlich aus der Entscheidungsnotiz übernommen.

## Versionsentscheidung

PATCH: 2.8.16 → 2.8.17. Der vergleichbare Skill-Rückbau (Reviewer-Retirement) ist in
1.1.22 als PATCH gelandet; die Änderungen hier sind Textpräzisierungen und eine
Bündelung ohne neue Rolle, keine neue Fähigkeit und kein neuer Ablauf.

Betroffene Versionsfelder: `manifest.json:3` und `SKILL.md:4` (Maker), sowie
`skills/plan-versioning-semver/SKILL.md:4` (Skill 1.2.0 → 1.3.0).

## Änderung 1 — `templates/roles/reviewer.SOUL.md.template:84`

ALT:
```
- Assess an explanation without requiring a project edit or an empty commit. A Coder answer or customer decision does not itself approve the implementation.
```
NEU:
```
- Assess an explanation without requiring a project edit or an empty commit. A Coder answer or customer decision does not itself approve the implementation; it closes the finding it answers, and the implementation still needs its own evidence.
```
Begründung: Eine Antwort darf keine Freigabe durch Behauptung sein, muss aber das beantwortete Finding schließen, sonst kann der Reviewer dasselbe Finding wiederholen.
Prüfschritt: `grep -F` auf den ALT-Satz vor dem Edit; `grep -n "it closes the finding it answers"` danach; Satz erscheint genau einmal.

## Änderung 2 — `templates/roles/reviewer.SOUL.md.template:94` und `:95`

ALT (`:94`):
```
- Report a missing test as a limit on the card; do not turn it into a requirement inside the same review round.
```
ALT (`:95`):
```
- Do not request tests beyond the acceptance criteria and the invariants named on the card.
```
NEU (drei Zeilen, ersetzen `:94`/`:95`):
```
- Return a missing test on a named invariant as a finding with `kanban_request_changes`; judging the finding belongs to the Coder.
- Where the plan or ticket excludes behaviour you find in scope, request the inclusion once; accept a maintained exclusion and record it as a carried limitation on the card.
- A test limitation otherwise exists only where the accepted plan declares the invariant unverifiable and states why. Do not request tests beyond the acceptance criteria and the invariants named on the card.
```
Begründung: `:94` schrieb drei verschiedene Herkünfte eines fehlenden Tests (plan-akzeptierte Grenze, Coder-Lücke, Planlücke) als akzeptierte Grenze fest; nur die dritte Herkunft ist eine Grenze.
Prüfschritt: beide ALT-Zeilen per `grep -F` belegen; danach sind `:94`/`:95` weg und die drei neuen Zeilen vorhanden; die Schließwirkung steht nur in `:84`.

## Änderung 3 — `templates/roles/coder.SOUL.md.template:65`

ALT (Zeilenende):
```
… An explanation needs no project edit or empty commit.
```
NEU:
```
… An explanation needs no project edit or empty commit. Give each declined finding its reason and the scope boundary it rests on; the decision stands for that round.
```
Begründung: Ohne Grund und Scope-Grenze ist eine Ablehnung für den Reviewer nicht bewertbar und wird erneut gemeldet.
Prüfschritt: `grep -F "Resolve Reviewer returns within your authority"` vor dem Edit; Satz danach genau einmal.

## Änderung 4 — `templates/roles/coder.SOUL.md.template:55`

ALT: gesamte Zeile
```
- Extend an existing test harness instead of writing a new one. Treat a synthetic harness that serves application files as verification scaffolding: deny the protected names and cover the transform, resolver, or editor routes that the acceptance criterion demonstrates, then stop. Further hardening of that boundary belongs in the handoff note, not in the harness. A further case in the existing fixture needs no decision; a second harness or an additional fixture tree beside the existing one changes the verification path and needs the Planner's decision.
```
NEU:
```
- Extend an existing test harness instead of writing a new one. Treat a synthetic harness that serves application files as verification scaffolding: deny the protected names and cover the transform, resolver, or editor routes that the acceptance criterion demonstrates, then stop. Further hardening of that boundary belongs in the handoff note, not in the harness. When the named harness or fixture tree cannot carry a required check, extend it or use another existing verification path, and record the choice with its reason on the card. A change to what the criterion proves follows the existing clarification path. A further case in the existing fixture needs no decision.
```
Begründung: Die Werkzeugwahl ist eine technische Entscheidung des Coders; nur eine Änderung dessen, was das Kriterium beweist, ist eine Anforderungsfrage.
Prüfschritt: `grep -F` auf den ALT-Abschnitt `A further case in the existing fixture needs no decision; a second harness`; danach ist dieser Abschnitt weg und „record the choice with its reason on the card" vorhanden.

## Änderung 5 — `templates/roles/planner.SOUL.md.template:79` (Endstand `:81`)

ALT (Zeilenende):
```
… label binding constraints and suggestions separately.
```
NEU:
```
… label binding constraints and suggestions separately. Carry each limit the accepted plan declares onto its ticket, with the stated reason.
```
Begründung: Der Reviewer soll die plan-akzeptierte Grenze nicht als fehlenden Nachweis lesen; die Karte trägt die Begründung des Plans.
Prüfschritt: `grep -F "Make the card understandable without opening the full plan"` vor dem Edit; Satz danach genau einmal.

## Änderung 6 — `templates/roles/planner.SOUL.md.template:51` (neue Zeile danach; Endstand `:52`)

ALT: keine (Einfügung nach `:51` `Briefly state the user's problem and proposed user-visible solution before technical detail.`)
NEU (eigene Zeile):
```
   For a defect, name the observed symptom, the expected behaviour, and a reproduction that demonstrates it; the acceptance criterion is the corrected behaviour under that reproduction.
```
Begründung: Der Planner ist die einzige Quelle des Symptoms; ohne es kann der Coder weder `diagnosing-bugs` bedienen noch einen RED-Beleg erzeugen.
Prüfschritt: `grep -nF` auf die Ankerzeile; die neue Zeile steht direkt dahinter, Einrückung wie die Nachbarzeilen.

## Änderung 7 — `templates/roles/planner.SOUL.md.template:61` (neue Zeile danach; Endstand `:63`)

ALT: keine (Einfügung nach der Kriterienzeile `State each acceptance criterion as an observable outcome whose violation is demonstrable.`)
NEU (eigene Zeile):
```
   Where a criterion rests on a test, the plan names the behaviour that test exercises.
```
Begründung: Ein Kriterium „Test X existiert und ist grün" ist sonst erfüllbar, ohne dass Verhalten geprüft wird.
Prüfschritt: `grep -nF "State each acceptance criterion as an observable outcome"`; neue Zeile direkt danach, genau einmal.

## Änderung 8 — `templates/roles/planner.SOUL.md.template:59` (Endstand `:60`)

ALT (Zeilenende):
```
   Identify verification interfaces and explain their fit. Prefer existing behavior-facing test seams at the highest useful level.
```
NEU:
```
   Identify verification interfaces and explain their fit. Prefer existing behavior-facing test seams at the highest useful level. Name the existing test harness or fixture tree each new check extends.
```
Begründung: Der Coder braucht die Identität des vorhandenen Harness, um „vorhandenen erweitern statt neuen bauen" anzuwenden.
Prüfschritt: `grep -F "Identify verification interfaces and explain their fit"` vor dem Edit; Satz danach genau einmal.

## Änderung 9 — `templates/roles/planner.SOUL.md.template:120` (Endstand `:122`)

ALT:
```
Missing index links do not prove a missing dependency.
```
NEU:
```
Missing index links do not prove a missing dependency; read the affected source before the plan drops a consumer.
```
Begründung: Die Warnhälfte allein verhindert nicht, dass ein Verbraucher allein wegen fehlender Indexkante aus dem Plan fällt.
Prüfschritt: `grep -F` auf den ALT-Satz; danach `grep -c "read the affected source before the plan drops a consumer"` = 1.

## Änderung 10 — `skills/plan-versioning-semver/SKILL.md`

- `:94` Abschnittstitel `## Application version` → `## Application and library versions`.
- Nach dem Satz „Classify each change of the application version by these three cases." wird ergänzt:
```
The three classes apply to the application version and to each self-owned library. A changed library carries its own version step; a consumer library that needs one after its dependency changes carries it as well, and its own consumers follow.
```
- `:3` `description` → `"Use when versioning: plans, app/library SemVer, changelog, API."` (61 Zeichen? siehe Prüfschritt; sonst gekürzt) — Trigger bleiben Plans, app/library SemVer, changelog, API.
- `:4` `version: 1.2.0` → `version: 1.3.0`.
- `:15-17` Einleitungssatz nennt „SemVer for the application version" — bleibt als Aufzählung der vier Regeln stehen; die Geltung für Bibliotheken steht im Abschnitt.
- `:24` When-to-use-Punkt „Set, classify or discuss the version of an application." bleibt.

Begründung: SemVer wird an einer Stelle gebündelt; der Coder hatte bisher keine SemVer-Regel außer dem zu löschenden Lib-Skill.
Prüfschritt: Abschnittstitel per `grep -n`; `description` ≤ 60 Zeichen per Python-Länge; Version 1.3.0.

## Änderung 11 — `manifest.json` (plan-versioning-semver)

ALT (`:228-231`):
```
"targets": {
  "hermes": [
    "planner"
  ]
},
```
NEU:
```
"targets": {
  "hermes": [
    "planner",
    "coder"
  ]
},
```
Begründung: Die gebündelte SemVer-Regel muss den Coder erreichen, der sie bisher nur über den Lib-Skill hatte.
Prüfschritt: `python3 -c` liest `own_skills["plan-versioning-semver"]["targets"]` und vergleicht.

## Löschung — `project-lib-versioning`

Vollständiger Löschumfang:

| Stelle | Umfang |
|---|---|
| `skills/project-lib-versioning/SKILL.md` | einzige Datei im Skillbaum; Verzeichnis wird mit entfernt |
| `manifest.json:53` | Eintrag `"skills/project-lib-versioning/SKILL.md"` in `files` |
| `manifest.json:243-261` | Komponenteneintrag `own_skills.project-lib-versioning` |
| `NOTICE.md:34` | Tabellenzeile `project-lib-versioning 1.1.0` |
| `references/upstream-sources.md:21` | Tabellenzeile mit Anker `own-lib-versioning` |
| `references/update.md:420` | Tabellenzeile im Abschnitt „Required Reviewer skill retirement (1.1.22)" |
| `references/update.md` | falsch werdende Aussagen im selben Abschnitt minimal umformuliert („these three identities" → „these two identities", „these three Reviewer skill trees" → „these two Reviewer skill trees"); historische Migrationsaussage bleibt erhalten |
| `references/test_render_reasoning.py:716` | Target-Map: Eintrag entfernt, plan-versioning-semver auf `["planner", "coder"]` |
| `references/test_render_reasoning.py:784` | `assertNotIn("project-lib-versioning", text)` bleibt als Regressionsschutz; daneben Manifest-Prüfung |
| `references/test_render_reasoning.py:818` | upstream-sources-Zeilenprüfung: Lib-Zeile raus, plan-versioning-Zeile mit „Planner and Coder" rein, Abwesenheit der Lib-Zeile geprüft |
| `references/test_render_reasoning.py:843` | 1.1.22-Retirement-Prüfung: zwei verbleibende Identitäten plus Manifest-/Abschnitts-Abwesenheit von `project-lib-versioning` |
| `references/test_update_team.py:901` | Fixture nutzt die zwei verbleibenden Reviewer-Skill-Identitäten; Abwesenheit von `project-lib-versioning` im Manifest geprüft |

Nicht berührt: `docs/` (historische Handoffs und Prüfberichte), `vortrag/`, Profile, Gateways,
`HANDOFF_2.8.16_Updater-Skill-Abbau_v1.md`.

Begründung: Der Skill ist überwiegend Coder-Ausführung, doppelt Inhalte aus
`plan-versioning-semver` und der Reviewer-SOUL; seine einzige eigene SemVer-Aussage geht in
`plan-versioning-semver` über.
Prüfschritt: `grep -rn "project-lib-versioning"` außerhalb von `docs/` liefert nur noch die
Test-Abwesenheitsprüfungen; `test -d skills/project-lib-versioning` schlägt fehl.

## Verifikation (für alle Änderungen)

1. `python3 -B -m unittest discover -s references -p 'test_*.py'` — Erwartung `OK` mit gleicher Testzahl wie vor der Änderung (212; Basis lief in dieser Umgebung mit `OK (skipped=16)`, nicht `skipped=1`).
2. `check_package.py` ist im Checkout nicht vorhanden; entfällt und wird berichtet.
3. `git diff --check`, `git status --porcelain`, `git diff --stat`.
4. Nur `reviewer`, `coder`, `planner` unter `templates/roles/` verändert.
5. Versionsfelder `manifest.json` und `SKILL.md` beide 2.8.17.

## Nachtrag: Konsistenz im Versionierungsskill (Parent, nach der Umsetzung)

Der Subagent meldete, dass Titel und „When to use" von `plan-versioning-semver` weiterhin nur die
Anwendung nennen. Das ist eine überholte Gegenaussage neben dem neuen Abschnitt und nach TAS zu
bereinigen. Zwei Ersetzungen in `skills/plan-versioning-semver/SKILL.md`:

| Stelle | ALT | NEU |
|---|---|---|
| `:13` Überschrift | `# Versioning plans and applications` | `# Versioning plans, applications and libraries` |
| `:17` Regelsatz | `…and SemVer for the application version.` | `…and SemVer for the application version and each self-owned library.` |
| `:24` When to use | `- Set, classify or discuss the version of an application.` | `- Set, classify or discuss the version of an application or a self-owned library.` |

Der Abschnitt selbst bleibt unverändert: erst die Anwendungsregel, dann der Bibliotheksabsatz.
Prüfschritt: `grep -n "application version" skills/plan-versioning-semver/SKILL.md` nennt nur noch
Stellen, die die Anwendung ausdrücklich meinen.

## Verifikation durch den Parent

- `python3 -B -m unittest discover -s references -p 'test_*.py'` → `Ran 212 tests`, `OK (skipped=1)`.
  Die Abweichung `skipped=16` im Subagenten-Lauf kommt vom Delegationsschutz der nativen
  Kanban-Tests; im Parent greift er nicht.
- `git diff --check` ohne Ausgabe; `git diff --stat` 12 Dateien; Rollenvorlagen nur reviewer/coder/planner.
- `manifest.json` 2.8.17, `SKILL.md` 2.8.17, `plan-versioning-semver` 1.3.0 mit `description`
  von 60 Zeichen, `project-lib-versioning` in Manifest und Dateiliste nicht mehr vorhanden.

## Punkt 10 — Evidenz-Eigentümerschaft im Reviewer (nachgezogen)

Grundlage: Lauf-4/5-Auswertung (`/home/mariko/.hermes/cache/scratch/review-lauf4-vs-5/BERICHT.md`,
tragende Belege vom Parent nachgeprüft) und Max' Entscheidung, dass der Reviewer fremde
Testausführung nicht als eigene Deckung verbuchen darf.

| Stelle | ALT | NEU |
|---|---|---|
| `reviewer.SOUL.md.template:92` | `Reuse evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid.` | `Reuse your own evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid; evidence from the implementing side is a claim to verify, not coverage.` |
| `reviewer.SOUL.md.template:100` | `… Read existing result artifacts instead of rerunning a successful check only to obtain a clearer summary.` | `… Rerun a check only when your own valid evidence does not already cover the change; a clearer summary is no reason to repeat it.` |

Begründung: `:90` („A Coder report or memory does not replace direct verification") und `:98`
(„retain required independent checks and explicit final-state acceptance tests") galten schon, wurden
aber von zwei Zeilen ohne Eigentümer verwischt. Die Sparabsicht bleibt; Wiederverwendung eigener
Läufe nach einem `changes_requested`-Rücklauf bleibt ausdrücklich erlaubt (`:91`, `:97`).

Testanpassung in `references/test_render_reasoning.py`, keine Assertion gestrichen:
`test_reviewer_avoids_failed_retries_and_redundant_evidence_work` prüft die neue Zeile;
`test_correction_contract_preserves_evidence_and_independent_verdict` prüft die Wiederverwendungsregel
jetzt getrennt — Coder generisch, Reviewer mit Eigentümer.

Prüfschritt: `grep -n "your own evidence\|your own valid evidence" templates/roles/reviewer.SOUL.md.template`
nennt beide Zeilen; Suite `OK (skipped=1)` bei 212 Tests (Parent-Lauf).
