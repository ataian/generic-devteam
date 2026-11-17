# Entscheidungen 2.8.17 — Besprechung Plan-Review nach 2.8.16

| Feld | Wert |
|---|---|
| Datum | 2026-11-15 |
| Basis | Maker 2.8.16, Commit `bef909a`, HEAD `0931b49` (Handoff), Branch `v3` |
| Zweck | Beschlossene Textänderungen sammeln, bevor irgendetwas im Maker umgesetzt wird |
| Stand | Punkt 1 vollständig beschlossen, nicht umgesetzt |

Umsetzung am Ende der Besprechung, nach `plan-versioning-semver`: ein Plandokument, danach Templatetext und PATCH-Bump 2.8.16 → 2.8.17.

## Punkt 1 — Finding: `reviewer.SOUL.md.template:94`/`:95`

### Befund

`:94` erlaubt, einen fehlenden Test als Grenze auf der Karte abzulegen, statt ihn zurückzugeben. Mit 2.8.16 muss der Planner jede brechbare Invariante abdecken (`planner.SOUL:57`); ein fehlender Test hat seitdem nur noch drei Herkünfte:

| Fall | Herkunft | Behandlung |
|---|---|---|
| a | Plan erklärt die Invariante als nicht verifizierbar, mit Grund | Grenze — mit dem Plan angenommen |
| b | Invariante steht auf der Karte, der Coder hat sie nicht getestet | Befund, zurück an den Coder |
| c | Plan und Karte nennen die Invariante nicht | Befund, Planlücke |

`:94` behandelt alle drei gleich und schreibt (b) und (c) als akzeptierte Grenze fest. `:95` ist davon unberührt und bleibt als Grenze gegen Coverage-Ausweitung richtig.

### Entscheidung

1. Rückgabe beendet die Zuständigkeit des Reviewers. Ob und wie der Coder eskaliert, steht nicht in der Reviewer-Regel.
2. Ein begründetes Nein des Coders ist eine gültige Auflösung. Der Reviewer darf dasselbe Finding danach nicht erneut melden.
3. Falsch als out of scope eingestuft: Reviewer fordert die Aufnahme einmal ein. Bleibt der Coder bei der Ablehnung, akzeptiert der Reviewer und hält den Widerspruch als getragene Grenze auf der Karte fest.
4. Eine Testgrenze ohne Erklärung im angenommenen Plan ist keine Grenze.
5. `:94`/`:95` werden zu drei Zeilen zusammengeführt; die Schließwirkung einer Coder-Antwort steht einmal, in `:84`, nicht zusätzlich in der Testregel.
6. Der Planner trägt jedes im Plan deklarierte Limit mit seiner Begründung auf die betroffene Karte. Grund: Der Reviewer soll die plan-akzeptierte Grenze (Fall a) nicht als fehlenden Nachweis (Fall b/c) lesen. Die Begründung bleibt so kurz wie im Plan; die Karte wiederholt den Plan nicht.

Verworfen: die Rückgabe an den Planner als Teil der Reviewer-Regel. `reviewer.SOUL:83` lässt nur den Coder zum Planner eskalieren; außerdem ist das nicht Zuständigkeit des Reviewers.

### Textvorschlag (englisch, TAS-geprüft, noch nicht eingespielt)

Ersetzt `reviewer.SOUL.md.template:94` und `:95`:

> Return a missing test on a named invariant as a finding with `kanban_request_changes`; judging the finding belongs to the Coder.
> Where the plan or ticket excludes behaviour you find in scope, request the inclusion once; accept a maintained exclusion and record it as a carried limitation on the card.
> A test limitation otherwise exists only where the accepted plan declares the invariant unverifiable and states why. Do not request tests beyond the acceptance criteria and the invariants named on the card.

Ergänzt `reviewer.SOUL.md.template:84` (bisheriger Satz bleibt, Wirkung wird auf das Finding begrenzt):

> Assess an explanation without requiring a project edit or an empty commit. A Coder answer or customer decision does not itself approve the implementation; it closes the finding it answers, and the implementation still needs its own evidence.

Ergänzt `coder.SOUL.md.template:65`:

> Give each declined finding its reason and the scope boundary it rests on; the decision stands for that round.

Ergänzt `planner.SOUL.md.template:79` (die ersten beiden Sätze bleiben unverändert):

> Make the card understandable without opening the full plan. Include concrete story criteria and necessary implementation context; label binding constraints and suggestions separately. Carry each limit the accepted plan declares onto its ticket, with the stated reason.

### Begründung

- `reviewer:84` in der alten Fassung sagt, dass eine Antwort keine Wirkung hat. Das ist zu absolut und erlaubt dem Reviewer, dasselbe Finding zu wiederholen. Die neue Fassung verhindert weiterhin eine Freigabe durch Behauptung, schließt aber das beantwortete Finding.
- `carried limitation` ist der Begriff aus `planner.SOUL:102` („found gaps, reported test limits, carried limitations"), damit Planner, Karte und Abschlussbericht denselben Anker benutzen.
- Die Coder-Zeile macht eine Ablehnung bewertbar; ohne Grund und Scope-Grenze hat der Reviewer nichts, worüber er urteilen könnte, und fragt erneut.

### Prüfschritte bei Umsetzung

- Vor dem Edit `grep -F` auf alle ALT-Zeilen: `reviewer.SOUL.md.template:84`, `:94`, `:95`; `coder.SOUL.md.template:65`; `planner.SOUL.md.template:79`.
- Danach `python3 -B -m unittest discover -s references -p 'test_*.py'`, Erwartung `OK (skipped=1)`.
- Ein PATCH-Bump für den zusammenhängenden Änderungssatz.
- Keine Test-Assertion hängt an den heutigen Zeilen `:94`/`:95` (geprüft am 2026-11-15).

## Punkt 2 — A1: Bibliotheks-Versionierung

### Befund

`project-lib-versioning` ist per `manifest.json:243-261` für Planner und Coder ausgeliefert und liegt in beiden Profilen. Die Planner-SOUL nennt den Skill nirgends (`planner:121` nennt nur `plan-versioning-semver` und `minimal-change-engineering`). Inhaltlich ist der Skill zu großen Teilen Coder-Ausführung: Schritte 1, 6, 9, 11 sind Maven-Detail, Schritt 3 steht wortgleich in `plan-versioning-semver`, Schritte 2 und 10 sind Ausführungsdetails, Schritte 5/7/8 prüft `reviewer:30`. Schritt 4 (bei `0.x`/`-SNAPSHOT` nicht raten, Planner fragen) ist durch den `needs_input`-Blocker des Coders abgedeckt.

Eigentlicher Fund: Der Coder hat keine SemVer-Regel. `coder:80` verlangt nur Changelog und „version grouping"; die Klassen MAJOR/MINOR/PATCH stehen in `plan-versioning-semver`, das laut Manifest nur für den Planner ausgeliefert wird. Die einzige SemVer-Autorität des Coders ist heute der Lib-Skill.

### Entscheidung

1. SemVer wird an einer Stelle gebündelt: `plan-versioning-semver` gilt künftig für Anwendungen **und** eigene Bibliotheken und wird an Planner und Coder ausgeliefert.
2. `project-lib-versioning` wird aus dem Maker entfernt.
3. Der Planner braucht keinen Zeiger auf den Lib-Skill; die Planaussage (Versionsschritt je Bibliothek, Kette) folgt aus der gebündelten SemVer-Regel.

### Textvorschlag (englisch, noch nicht eingespielt)

`skills/plan-versioning-semver/SKILL.md`, Abschnitt „Application version" wird zu „Application and library versions":

> The three classes apply to the application version and to each self-owned library. A changed library carries its own version step; a consumer library that needs one after its dependency changes carries it as well, and its own consumers follow.

Dazu `description` und Frontmatter-Version des Skills (1.2.0 → 1.3.0), `manifest.json` (`targets.hermes` → `[planner, coder]`).

### Löschumfang

- `skills/project-lib-versioning/SKILL.md` (einzige Datei im Skillbaum)
- `manifest.json:53` (Dateiliste) und `:243-261` (Komponenteneintrag)
- `NOTICE.md:34`
- `references/upstream-sources.md:21`
- `references/update.md:420` (Tabelle)
- Tests: `references/test_render_reasoning.py:716,784,818,843`, `references/test_update_team.py:901`
- `references/update.md` §„Required Reviewer skill retirement (1.1.22)" nennt den Skill als Rückbauziel für Reviewer; der Abschnitt ist beim Reviewer-Rückbau in 1.1.22 gelaufen und bleibt als Historie stehen — beim Löschen prüfen, ob die Nennung dort noch gebraucht wird.

### Offen bei der Umsetzung

- Bump-Klasse des Makers: MINOR, wenn der Wegfall als Feature gilt, MAJOR, wenn fremde Teams auf die Skilldatei zählen.
- Installierte Kopien in Jacks und Carters Profil bleiben nach dem Maker-Commit als Waisen liegen; der Updater entfernt sie heute nicht — siehe Baustelle 2.

## Punkt 3 — A4: Risikokatalog, zweite Hälfte

### Befund

2.8.16 nennt in `planner:57` vier Achsen als Suchgrenze: Sicherheit, Datenintegrität, API-Verträge, Nebenläufigkeit. Der Reviewer führt daneben einen breiteren Katalog: `reviewer:26` (Korrektheit, Sicherheit, Datenintegrität, API-Verträge, Nebenläufigkeit, Wartbarkeit, Regressionen), `reviewer:58` (Reasoning-Schwelle mit Auth/Session/Bearer, Rechten, Secrets, Krypto, Sperren, Transaktionen, destruktiven Änderungen, Migrationen, extern sichtbaren API-Änderungen, breiten Moduländerungen, Kerndomain-Invarianten), `reviewer:74` (Prüffokus mit Auth/Authz, Rechten, Persistence, Transaktionen, Nebenläufigkeit, DTO-/Mapper-Grenzen, externen API-Verträgen, Legacy-Hotspots, Migrationen, Regressionsrisiko).

Jeder konkrete Katalogeintrag fällt unter eine der vier Achsen: Auth/Authz/Rechte/Secrets/Krypto → Sicherheit; Persistence, destruktive Änderungen, Migrationen, Schema-Migrationen → Datenintegrität; extern sichtbare API-Änderungen, DTO-/Mapper-Grenzen → API-Verträge; Transaktionen, Sperren, Race Conditions → Nebenläufigkeit. Nicht abbildbar sind nur „legacy hotspots" und „high regression risk" — das sind Urteile über das Repository, keine Achsen.

Hinweis zur Berichtsgrundlage: Der Prüfbericht ist gegen 2.8.15 geschrieben; seine Feststellung „Planner-Status: Lücke" bezieht sich auf den alten testgebundenen Invariantenbegriff (alt `planner:76-78`), den S3 in 2.8.16 durch `:57` ersetzt hat.

### Entscheidung

Keine Änderung. Der Reviewer-Katalog wird nicht in den Planner übernommen, und die vier Achsen erhalten keine Geltungsbereichs-Zusätze.

### Begründung

1. Der Katalog ist keine Risiko-Taxonomie, sondern eine Review-Checkliste mit Reasoning-Schwellen und Repo-Urteilen; er mappt vollständig auf die vier Achsen.
2. Eine Kopie wäre eine zweite Aussage derselben Bedeutung — genau das Driftrisiko, das A4 selbst benennt.
3. Eine Aufzählung von Geltungsbereichen wirkt als Abschluss, nicht als Beispiel: Aus „security and access rights" wird „Sicherheit heißt Rechte", und nicht Genanntes fällt aus dem Suchraum. Die vier Achsen bleiben als offene Kategorien wirksamer.
4. Der Planner braucht eine Suchgrenze, der Reviewer eine Prüfliste; unterschiedliche Granularität ist hier richtig, nicht inkonsistent.

## Punkt 4 — A5: Separater Hochrisiko-Durchgang

### Befund

`reviewer:62`
> If the change affects material security, data-integrity, transaction, or concurrency invariants, obtain a separate pass before the verdict even when the main review finds no defect.

Auslöser sind damit dieselben Achsen wie in `planner:57` (plus Transaktionen). `reviewer:39` ordnet die Prüftiefe ausdrücklich dem Reviewer zu: „Judge complexity, coupling, and independent work… This is your review judgment, not another customer approval gate." `reviewer:73` verlangt, Hochrisikoprüfungen und die Abdeckung des separaten Durchgangs im Review-Nachweis zu halten; `planner:102` meldet Abweichungen am Projektende. `planner:55` verlangt Phasen mit Anforderungen, Dateien, Abhängigkeiten, Verifikation, Abnahmegates und Commitgrenzen — keine Aufwandsschätzung, also auch keine Stelle für „Aufwand je Prüfdurchgang".

### Entscheidung

Keine Änderung. Der Plan weist den separaten Hochrisiko-Durchgang nicht als eigenen Prüfschritt, Aufwand oder Gate-Zeitpunkt aus.

### Begründung

1. Der Auslöser ist derselbe wie bei Punkt 3: Nennt der Plan die brechbaren Invarianten, leitet der Reviewer den Pass daraus ab; nennt er sie nicht, hilft keine Zeile über Prüftiefe.
2. Eine Planaussage über Prüftiefe nimmt die Reviewer-Entscheidung vorweg und kollidiert mit `reviewer:39`. Die schädliche Variante — „diese Phase braucht keinen separaten Durchgang" — würde als akzeptierte Begrenzung der Prüfung gelesen, also genau der Mechanismus, der in Punkt 1 geschlossen wurde.
3. Das Planmodell hat keine Aufwandsdimension (`planner:55`); eine einzuführen wäre eine neue Dimension, keine Zeile.
4. Sichtbarkeit entsteht an der richtigen Stelle: Beleg nach der Prüfung (`reviewer:73`) und Abschlussbericht (`planner:102`) statt Prognose vor der Prüfung.

## Punkt 5 — A6: Vergleichsbedingungen visueller Kriterien

### Befund

`reviewer:31` (Punkt 10) verlangt beim visuellen Abnehmen Vergleichbarkeit (Viewport, Zoom/DPR, Source-Ausschnitt, Datenzustand, Schriften, freigegebene Abweichungen). Die Bedingungen stehen in `skills/screenshot-to-code/references/visual-check.md:5-11`; der Skill ist laut `manifest.json` für Planner und Coder ausgeliefert, Trigger: „For a screenshot, UI mockup, or a PDF page explicitly commissioned as a UI template: for product clarification, planning, implementation, or independent review."

`planner.SOUL` enthält kein Wort zu visual, screenshot, render oder viewport (geprüft). `planner:58` bleibt allgemein: „State each acceptance criterion as an observable outcome whose violation is demonstrable."

### Entscheidung

Keine Änderung. Weder eine Planner-Regel zu Vergleichsbedingungen noch ein Zeiger auf `screenshot-to-code`.

### Begründung

1. Der Trigger ist der Zeiger. Eine Aufgabe „Screenshot/Mockup als UI umsetzen" lädt den Skill über seine Beschreibung; ein zusätzlicher SOUL-Satz wäre die Doppelung.
2. Die fünf Bedingungen als Liste in die SOUL zu ziehen hätte den A4-Effekt (Aufzählung liest sich als abschließend) und wäre eine zweite Quelle mit Driftrisiko.
3. Restfall „visuelles Kriterium ohne Vorlagen-Rebuild": Trigger greift auf die Aufgabe, nicht auf die Kriterienart, also lädt der Skill dort nicht. Der Fall ist aber durch `planner:58` und `reviewer:31` abgedeckt — ein Kriterium ohne Vergleichsbedingungen ist nicht zeigbar, der Reviewer gibt es als Befund zurück. Das ist der Korrekturpfad aus Punkt 1.
4. Ein Zeiger lohnt dort, wo der Auslöser nicht als Aufgabe erkennbar ist; ein Screenshot-Auftrag ist es.

## Punkt 6 — A7: Bug-Pläne brauchen Symptom, Sollverhalten und Repro

### Befund

`skills/diagnosing-bugs/SKILL.md` (nur `codex: team-codex`): „Use the accepted goal, context, exact symptom, expected behavior, and verification criteria." `coder:26` gibt das weiter: „Pass the exact symptom, accepted context, and verification criteria; require the skill for unexplained failures or regressions…" `coder:77` verlangt einen dokumentierten RED-Lauf des neuen Tests.

Der Coder kann nur weitergeben, was die Karte enthält. Die Planner-SOUL hat zu Bug-Plänen nichts: kein Vorkommen von bug, defect, symptom, reproduction außer `:44` (Failure Modes als Caller-Wissen) und `:128` (Berichte). Anders als bei Punkt 5 liegt der Inhalt in einem Skill, das der Planner nicht bekommt — es gibt keinen Trigger, der einspringt.

### Entscheidung

Eine Zeile in Schritt 4, direkt nach `planner:51`:

> For a defect, name the observed symptom, the expected behaviour, and a reproduction that demonstrates it; the acceptance criterion is the corrected behaviour under that reproduction.

### Begründung

1. Der Planner ist die einzige Quelle des Symptoms; ohne es kann `coder:26` nichts weitergeben und `coder:77` keinen RED-Beleg erzeugen.
2. Das Kriterium wird dadurch eine benannte Beobachtung statt „geht wieder".
3. Kein Driftrisiko: Symptom, Sollverhalten und Reproduktion stehen in keinem anderen Planner-Abschnitt.
4. Beweislage: statischer Befund aus dem Prüfbericht, kein belegter Lauf; die Kette `coder:26` → Karte ist strukturell, nicht bloß plausibel.

## Punkt 7 — A8: Testharness benennen, Werkzeugwahl beim Coder

### Befund

`coder:55` verlangt heute: „Extend an existing test harness instead of writing a new one… A further case in the existing fixture needs no decision; a second harness or an additional fixture tree beside the existing one changes the verification path and needs the Planner's decision."

`planner:59` verlangt „Identify verification interfaces and explain their fit", nennt aber nicht die Identität des vorhandenen Harness oder Fixture-Baums. `planner:63` behandelt einen Dev-Harness als Verifikationsgerüst, `planner:26` verbietet, Testaufbau zu einem eigenen Projekt zu machen. Beides regelt die Behandlung, nicht die Identität.

Zweiter Befund: Die Coder-Zeile macht aus einem technischen Mittel ein Genehmigungsthema und widerspricht der Linie, dass technische Entscheidungen beim Coder liegen.

### Entscheidung

1. `planner:59` wird um einen Satz erweitert:

> Identify verification interfaces and explain their fit. Prefer existing behavior-facing test seams at the highest useful level. Name the existing test harness or fixture tree each new check extends.

2. `coder:55` wird neu gefasst; die drei ersten Sätze bleiben wortgleich:

> Extend an existing test harness instead of writing a new one. Treat a synthetic harness that serves application files as verification scaffolding: deny the protected names and cover the transform, resolver, or editor routes that the acceptance criterion demonstrates, then stop. Further hardening of that boundary belongs in the handoff note, not in the harness. When the named harness or fixture tree cannot carry a required check, extend it or use another existing verification path, and record the choice with its reason on the card. A change to what the criterion proves follows the existing clarification path. A further case in the existing fixture needs no decision.

### Begründung

1. Der Coder braucht die Identität des Harness, um „vorhandenen erweitern statt neuen bauen" anwenden zu können; der Planner liest das Repo über die Brownfield-Analyse und kann sie benennen.
2. Die Grenze verschwindet nicht, sie wandert an die richtige Stelle: Ändert der neue Pfad, was das Kriterium beweist, ist das eine Anforderungsfrage und geht über `coder:64` (`needs_input`). Reine Werkzeugwahl bleibt beim Coder mit Aufzeichnungspflicht.
3. Aufsicht bleibt erhalten: `coder:85` verbietet abgeschwächte Tests, `reviewer:40` prüft gegen die angenommenen Kriterien, `planner:101` liest Karte und Reviewurteil bei jedem Phasenabschluss.
4. Kein neuer Entscheidungspunkt, keine Blockade mitten in der Umsetzung.

## Punkt 8 — A9: Indexbefund ersetzt keine Quelllesung

### Befund

`coder:87` — „Index findings replace neither a source read nor a test. A missing edge does not prove a missing dependency."
`planner:120` — „… Validieren der Index-Frische … Missing index links do not prove a missing dependency. If a mandatory integration fails, block dependent work; do not silently substitute tools."
`reviewer.SOUL` enthält keine Regel zum Strukturindex (geprüft).

Der Planner hat damit die Warnhälfte, aber nicht die Nachweishälfte. „Fehlende Kante beweist nichts" verhindert nicht, dass der Index als Beweis für Abwesenheit genommen wird und ein Verbraucher aus der Dateiliste fällt — derselbe Fehlertyp wie A2.

### Entscheidung

`planner:120`, Satzersetzung (der Rest der Zeile bleibt):

> Use the approved structural analysis integration and its original skill. Validate index freshness and relevant code/test coverage. Missing index links do not prove a missing dependency; read the affected source before the plan drops a consumer. If a mandatory integration fails, block dependent work; do not silently substitute tools.

`coder:87` bleibt unverändert.

### Begründung

1. Ein Satz statt zwei: Die Warnung bekommt ihre Folge, und der Anker bleibt derselbe wie im Coder.
2. Beide Regeln bleiben bei ihren Rollen. Die SOULs werden getrennt geladen und können nicht aufeinander zeigen; der Coder braucht die Regel für seine Arbeit, der Planner für den Planinhalt. Konsistenz entsteht über gleichen Wortlaut, nicht über eine gemeinsame Datei.
3. `reviewer.SOUL` bleibt unverändert: Der Reviewer prüft gegen Plan und Quelle, nicht gegen den Index; eine Indexregel wäre dort eine Werkzeugpflicht ohne Prüfwert.

## Punkt 9 — A10: Beweisform eines Testkriteriums

### Befund

`sdlc-review/SKILL.md:99` (Punkt 5 der Code-Prüfung), beim Reviewer über `reviewer:74` geladen: „Confirm that tests assert behavior rather than merely snapshotting source text or constants."

Der Planner hat dazu nichts: `planner:58` regelt die Form des Kriteriums, `planner:61` die Wiederverwendung vorhandener Tests. Ein Kriterium „Test X existiert und ist grün" ist damit erfüllbar, ohne dass Verhalten geprüft wird; `coder:77` (RED-Beleg) hilft nicht, weil ein RED-Lauf eines Quelltext-Snapshots genauso wertlos ist.

### Entscheidung

Ein Satz nach `planner:58`:

> Where a criterion rests on a test, the plan names the behaviour that test exercises.

### Begründung

1. Zwei verworfene Fassungen, aus zwei entgegengesetzten Gründen. Eine lange Fassung („…that test must exercise the behaviour; an assertion that mirrors source text or constants does not carry the criterion") wiederholte die Aussage aus `sdlc-review:99` in einer zweiten Rolle — dieselbe Kopie, die bei A4 und A6 verworfen wurde. Eine kurze Fassung („Tests that assert source text or constants do not carry a criterion") sagte dem Planner nicht, was er schreiben soll.
2. Die gewählte Fassung enthält den Planner-Akt (je Kriterium das Verhalten benennen) und nichts vom Reviewer-Akt (prüfen).
3. Ein Snapshot-Test kann die Forderung nicht erfüllen, ohne dass das Verbot ausgeschrieben werden muss.
4. `sdlc-review:99` bleibt als Prüfpflicht beim Reviewer; die Rollen teilen die Aufgabe, statt sie zu duplizieren.

## Punkt 10 — Reviewtiefe in Lauf 5 (offen, Klärung läuft)

### Befund

`VERGLEICH_2.8.15_Laeufe-1-5_v1.0.0.md:18,66-79,117-118`: Daniel hat in Lauf 5 unabhängig auf Browser-Ebene geprüft (Cypress 8 passing, 21 `sha256sum`, 4 Vision-Aufrufe), aber weder Backend-Test noch Generierung noch Frontend-Build selbst ausgeführt; die Nachweise des Coders existierten (`:57`: 14 Backend-Tests grün, 8 Browserfälle grün, Check 255 Warnungen/0 Fehler, Build 13.383 Module). Kommentar 2.974 statt 5.304 Zeichen (−43,9 %), ohne kriterienweise Zuordnung, 0 Befunde. In Lauf 4 hatte er Backend-Test und Build selbst ausgeführt. Die Reviewer-SOUL ist bytegleich (`:79`).

### Stand

**Entschieden: zwei Textänderungen in `reviewer:92` und `reviewer:100`.** Grundlage: `/home/mariko/.hermes/cache/scratch/review-lauf4-vs-5/BERICHT.md`, tragende Belege vom Parent nachgeprüft. Die Begründung wurde im Verlauf zweimal korrigiert — siehe Nachtrag.

### Korrektur der Ausgangslage

`VERGLEICH_2.8.15_Laeufe-1-5_v1.0.0.md:18` und `:72` legen nahe, Lauf 4 habe Backend-Test, Generierung und Frontend-Build selbst ausgeführt. Die Rohdaten widerlegen das: `ecog-replay-2026-11-14-lauf4/review/data.json` führt unter `uebernommen` „Generierung, Backend-Compile/Spotless, Frontend-Check/Build, Produktionsausschluss". Selbst ausgeführt wurden in Lauf 4 nur Cypress (6 passing) und der Backend-Test (4 Tests, 0 Fehler, `node docker/dev/tests.mjs ecog`). Der Unterschied zwischen den Läufen ist **eine** Prüfart, nicht drei.

### Ursache (belegt)

1. **Kein Kriterienunterschied.** Lauf 5 hatte 10 statt 9 Kriterien, A6 verlangt echte Backend-Persistenz, A10 Generierung/Compile/Build mit Zählzwang. Der Dispatch-Kontext war bis auf Karte und Übergabe bytegleich (16.136 Zeichen Präambel, Reviewer-SOUL `e950ab6c…` identisch in 2.8.9, 2.8.15 und HEAD).
2. **Technischer Grund:** Die Ein-Kommando-Aktion `ecog` in `docker/dev/tests.mjs` existiert nur im Lauf-4-Commit `8b1aa423`; `45f82b48` fasst die Datei nicht an. Geprüft per `git show`.
3. **Übergabe in dieselbe Richtung:** Lauf 5 erklärte „test_executor: Team-Codex … No duplicate full rerun by Carter" und lieferte keine Kommandos; Lauf 4 lieferte `newly_executed_by_carter` mit Zählern, Logs und zwei exakten Kommandozeilen. Daniel hat die Zuschreibung wörtlich übernommen.
4. **Rundelinse stützt das:** `sdlc-review:65/66` verlangt in Runde 1 Artefaktlesen, Ausführen erst in Runde 2; `reviewer:99` verlangt ausdrücklich das Lesen vorhandener Artefakte statt eines erneuten Laufs. Lauf 4 hat über die Pflicht hinaus gearbeitet.
5. **Kein Zeit- oder Kontextdruck:** Lauf 5 mit 477 s kürzer, mehr Reasoning-Token pro Output, 0 Kompaktierungen.

### Bewertung der Lauf-4-Zusatzprüfungen

- Backend-Test: **sinnvoll, aber nicht zwingend.** Er fügte genau eine Aussageklasse hinzu („ein zweiter Ausführer hat es am geprüften Commit getan"), die Evidenz des Coders war hash-gebunden und vollständig.
- Generierung und Frontend-Build: **überflüssig** — und in Lauf 4 gar nicht selbst gelaufen.
- Eigene `dist`-Suche (Produktionsausschluss): **sinnvoll, aber nicht zwingend.** Sie ist die einzige Prüfung, deren Ersatz schwächer ist als das Original, weil ein Build-Log keine Abwesenheit im gebauten Bundle beweist. Genau diese Suche fehlt in Lauf 5.

### Ergebnis

Das Unterlassen des eigenen Backend-Laufs in Lauf 5 ist eine akzeptable Schwankung innerhalb gültiger Regeln. Der belastbare Mangel ist die **Form**: keine kriterienweise Nachweiszuordnung (A1–A10 in einem Satz) und 28 statt 53 gelesene Pfade. Beides ist bereits zweifach vorgeschrieben — `sdlc-review:91` („Map every acceptance criterion to concrete implementation or output evidence") und `:176` sowie `reviewer:42`. Ein weiterer SOUL-Satz träfe die Ursache nicht; Lauf 5 hat eine bestehende Pflicht nicht erfüllt, nicht eine fehlende befolgt. Ein Fehlurteil ist durch die Daten nicht belegbar.

### Beobachtungsvorschlag statt Regel (nicht beschlossen)

Bei den nächsten zwei bis drei Läufen drei Kennzahlen mitschreiben: (a) Zahl der gelesenen Pfade im Review, (b) Existenz einer kriterienweisen Zuordnung (Ja/Nein je Kriterien-ID), (c) ob der Coder für eine neue Testklasse eine ausführbare Harness-Aktion mitliefert. Erst wenn (b) erneut ausfällt und (c) vorhanden war, ist eine Änderung begründet — dann als prüfbare Ausgabeform, nicht als Ausführungspflicht.

### Nebenbefunde

- Der technische Hebel liegt beim Harness, nicht beim Reviewer: Lauf 4 war billiger, weil der Coder eine feste Aktion für die neue Testklasse mitlieferte. Ob der Maker diese Erwartung führen soll, ist eine eigene Frage und nicht Teil dieser Besprechung.
- `VERGLEICH_2.8.15_Laeufe-1-5_v1.0.0.md:18` und `:72` sind sachlich falsch und sollten korrigiert werden — das Dokument liegt im Tokenprofiling-Projekt, nicht im Maker.
- Datenlücken: Lauf-4-Karte `t_741139dc` und Kommentare 29–51 sind aus `sg1/kanban.db` gelöscht, die Lauf-4-Reviewersitzung `local-94a4943d…` aus `profiles/daniel/state.db`; Lauf-5-Metadaten behaupten einen Evidence-Anhang, die Karte hatte keine.

### Nachtrag — korrigierte Begründung (Max' Einwand)

Eine erste Fassung dieses Punktes las `reviewer:100` („Read existing result artifacts instead of rerunning a successful check only to obtain a clearer summary") als über das Ziel geschossenen Sparsatz und schlug eine Ergänzung vor. Das war falsch angesetzt. Die vier betroffenen Sätze zusammengenommen:

- `:92` — Wiederverwendung nur solange Eingaben, Abhängigkeiten und Testbedingungen gültig sind.
- `:97` — „Keep the original executor and checked state; distinguish reused evidence from newly executed checks."
- `:98` — „Run checks affected by changes or insufficient evidence; retain required independent checks and explicit final-state acceptance tests."
- `:100` — Vorhandene Ergebnisse lesen statt eines erneuten Laufs **nur zum Zweck einer schöneren Zusammenfassung**.

`:97` verlangt, den ursprünglichen Ausführer zu kennen und zu benennen — nicht, ihn als Ersatz zu akzeptieren. `:98` verlangt unabhängige Prüfungen und Abnahmetests am Endzustand. Daniel hat die Ausführung der Umsetzungsseite als unabhängige Deckung verbucht; damit hat er zwei bestehende Regeln nicht angewandt, und zusätzlich gegen Punkt 1 verstoßen, weil er die Lücke als Grenze ablegte, ohne dass der angenommene Plan sie erklärt hatte. Sein Vorgehen war also nicht durch den Text gedeckt.

Folge: Die vorgeschlagene Ergänzung an `:100` ist in dieser Form zurückgezogen — sie hätte einen Satz hinzugefügt, wo der bestehende reicht.

### Entscheidung nach Max' zweitem Einwand

Die Lesart „der Reviewer prüft, ob ein Test schon gelaufen ist" ist die falsche. Gewollt ist: Der Reviewer führt selbst durch, was er zur Deckung braucht, und wiederverwendet nur **seine eigenen** früheren, noch gültigen Läufe — etwa nach einem `changes_requested`-Rücklauf die Tests, die von den Änderungen nicht berührt sind. Fremde Ausführung ist eine Behauptung, die er prüft, keine Deckung.

Das Prinzip stand bereits in `reviewer:90` („A Coder report or memory does not replace direct verification"), wurde aber von zwei Zeilen ohne Eigentümer verwischt. Deshalb zwei Textänderungen statt einer:

- `reviewer:92` — „Reuse evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid." wird zu „Reuse your own evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid; evidence from the implementing side is a claim to verify, not coverage."
- `reviewer:100` — „Read existing result artifacts instead of rerunning a successful check only to obtain a clearer summary." wird zu „Rerun a check only when your own valid evidence does not already cover the change; a clearer summary is no reason to repeat it."

Die Sparabsicht bleibt, die Unabhängigkeit bekommt ihren Eigentümer, `:90` und `:98` („retain required independent checks and explicit final-state acceptance tests") stimmen jetzt zusammen. Die Scope-Verengung nach einem Rücklauf steht schon in `:91` („assess the delta") und `:97` („Run checks affected by changes or insufficient evidence").

Testanpassung: `test_render_reasoning.py` prüfte die alte Zeile in einer Liste (`:212`) und die Wiederverwendungsregel gemeinsam für Coder und Reviewer (`:242`). Beide Assertions wurden nicht gestrichen, sondern aufgeteilt: der Coder behält seine generische Fassung, der Reviewer bekommt die neue mit Eigentümer.

Umsetzung: eingespielt, Suite `OK (skipped=1)` bei 212 Tests.
