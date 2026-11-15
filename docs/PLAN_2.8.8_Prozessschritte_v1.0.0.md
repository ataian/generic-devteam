# PLAN — Prozessschritte für das Devteam

| Feld | Wert |
|---|---|
| Ausgangsversion | Maker **2.8.8** (`f3213de`), Rollout-Stand in SG1 |
| Planversion | **1.0.0** |
| Datum | 2026-11-14 |
| Belegquelle | Lauf 3 (`projects/devteam-tokenprofiling/ecog-replay-2026-11-14-lauf3/`), Board `sg1`, Karte `t_d3894cd4`, Commit `4f06947a` |
| Vorgänger | Lauf 2 (`ecog-replay-2026-11-13/`), Lauf 1 (`jack-v2-2026-11-10/ecog/`) |
| Charakter | Vorschlag. Rollen-Template-Änderungen und Team-Rollout bleiben getrennte Freigaben (`AGENTS.md:14`). |

## 0. Umsetzungsstand (2026-11-14, 21:00)

| Punkt | Entscheidung | Stand |
|---|---|---|
| 2.1 Branch je Ticket | umsetzen, **erweitert:** Planner fragt Kunde nach Branchname und Startpunkt | in 2.8.9 |
| 2.2 PR durch den Planner | nicht jetzt — gehört ins PR-Paket | offen, `PLAN_2.8.9_Pull-Request-Prozess_v1.0.0.md` |
| 2.3 Pipeline rücklesen | nicht jetzt — PR-Paket | offen |
| 2.4 Wirkungsanalyse | umsetzen | in 2.8.9 |
| 2.5 Rot-vor-grün | umsetzen | in 2.8.9 |
| 2.6 Daten-/Exportverträglichkeit | umsetzen | in 2.8.9 |
| 2.7 Aufräumen | umsetzen | in 2.8.9 |
| 2.8 Retro | umsetzen, **aber ohne Automatik:** nur im Abschlussbericht erwähnen | in 2.8.9 |
| 2.9 ADR/Entscheidung festhalten | **gestrichen** — Planner-SOUL:35–40 regelt es enger und widerspricht einer zweiten Aussage | nicht umgesetzt |
| 2.10 Ticket↔PR verknüpfen | PR-Paket; Kanban bleibt auf Coder/Reviewer begrenzt, Jira kommt später | offen |
| 2.11 Invarianten + ihre Tests | umsetzen | in 2.8.9 |
| 2.12 Quelle gegen Ausführung trennen | umsetzen | in 2.8.9 |

## 1. Ausgangslage

Lauf 3 hat den Kostentreiber aus Lauf 2 beseitigt: eine Karte, ein Implementierungslauf, eine Reviewrunde, ein APPROVE, 0 `changes_requested`. Der Prozess endet aber weiterhin bei „DONE" — und dort enden auch die Handlungen der Agenten.

Belegt aus Lauf 3 und für diese Planung relevant:

- Karte `t_d3894cd4` hat `branch_name = NULL`; gearbeitet wurde auf dem langlebigen Branch.
- Der Commit `4f06947a` ist lokal; kein Push, kein Pull Request, keine Pipeline-Ausführung (die Repo-Pipeline hat neun Workflows, u. a. `test-e2e.yml` und `check-format-*.yml`).
- Der Übergabetext weist keinen fehlschlagenden Testlauf vor der Änderung aus, obwohl zehn Testläufe stattfanden.
- Es gibt keine Liste der Verbraucher des geänderten Symbols; Print-Ansicht und DNPM-Export wurden nur zufällig mitgeprüft.
- Der `retro`-Skill liegt im Planner-Werkzeugkasten und wurde nicht aufgerufen.

Nicht Gegenstand dieses Plans: Planfreigabe durch den Kunden, manuelle Abnahme im laufenden System, Vergabe von Push-Rechten. Das sind menschliche Schritte.

## 2. Die zehn Schritte

Format je Schritt: Beobachtung → Ort im Maker → Formulierung (EN, TAS-konform) → Wirkung → Voraussetzung → Aufwand.

### 2.1 Ticket-Branch je Lauf

- **Beobachtung:** Kein eigener Branch; der Implementierungsstand liegt auf einem langlebigen Arbeitsbranch, der mehrere Läufe trägt.
- **Ort:** `templates/roles/coder.SOUL.md.template`, „Task execution" Schritt 2; `templates/roles/planner.SOUL.md.template`, Kartenaufbau (bei `:70`).
- **Planner-Text:** `Name the implementation branch on the card; derive it from the ticket ID and a short slug, not from the plan title.`
- **Coder-Text:** `Create that branch from the reviewed baseline commit before the first Codex call; when the card names no branch, use feature/<ticket-id>-<short-slug>.`
- **Wirkung:** Jeder Lauf ist isoliert; ein misslungener Lauf hinterlässt keinen Stand auf dem Arbeitsbranch. Voraussetzung für PR und CI.
- **Voraussetzung:** keine. Reine Git-Aktion.
- **Aufwand:** 3 Zeilen, ein Testlauf.

### 2.2 Push und Pull Request nach dem Urteil

- **Beobachtung:** Kein Push, kein PR; der Commit ist für niemanden außerhalb der Maschine sichtbar.
- **Ort:** neuer Abschnitt „Release handoff" in `coder.SOUL.md.template` nach Schritt 15; Rezept in `references/integrations.md`.
- **Text:** `When the assignment grants push permission, push the ticket branch after an APPROVE verdict and open a pull request whose body carries the ticket, the reviewed commit, the verdict, and the retained limits.` Dazu: `Never push before the verdict and never force-push.`
- **Wirkung:** Vier-Augen-Merge wird möglich; der geprüfte Stand ist adressierbar.
- **Voraussetzung:** **Push-Recht und Credential für das Team.** Heute ausdrücklich nicht vorhanden; ohne beides bleibt der Schritt unwirksam.
- **Aufwand:** 4 Zeilen Text, 1 Rezeptabschnitt, 1 Freigabe.

### 2.3 Pipeline-Ergebnis rücklesen

- **Beobachtung:** Neun Workflows im Repo, keiner wurde für diesen Commit ausgelöst.
- **Ort:** derselbe Abschnitt „Release handoff".
- **Text:** `Read the pipeline result for the pushed branch back, record status and run reference on the card, and correct a failure within your own authority without a new approval.`
- **Wirkung:** Die Prüfung ist nicht mehr nur lokal; Format-, E2E- und Versionsprüfung laufen dort, wo sie für den Merge zählen.
- **Voraussetzung:** 2.2; Werkzeugzugang zur Pipeline (`gh` fehlt auf dem Host, API-Weg vorhanden).
- **Aufwand:** 2 Zeilen, ein Werkzeugpfad.

### 2.4 Wirkungsanalyse vor der Umsetzung

- **Beobachtung:** Keine Verbraucherliste; Print-Ansicht und DNPM-Export wurden nicht systematisch geprüft.
- **Ort:** `coder.SOUL.md.template`, „Task execution" als neuer Schritt 2 (vor der Codex-Beauftragung).
- **Text:** `List every consumer of each changed symbol, schema, or component before the first Codex call: code, exports, print views, and generated clients, one line of evidence per consumer.` Dazu: `Name consumers outside the acceptance scope as explicitly out of scope instead of leaving them unmentioned.`
- **Wirkung:** Auswirkungen werden vor dem Code sichtbar, nicht nach dem Zufallsfund; der Reviewer erbt eine prüfbare Liste.
- **Voraussetzung:** keine. CBM ist beim Coder eingerichtet, `rg` genügt als Rückfall.
- **Aufwand:** 2 Zeilen. Größter Nutzen je Aufwand.

### 2.5 Rot-vor-grün belegen

- **Beobachtung:** Zehn Testläufe, aber kein ausgewiesener roter Lauf vor der Änderung.
- **Ort:** `coder.SOUL.md.template`, Schritt 13 (Staging/Commit) als Bedingung für die Übergabe.
- **Text:** `Record one failing execution of a new test before the production change and attach its output to the handoff; without a recorded RED, state that RED was not demonstrated.`
- **Wirkung:** Der Nachweis „der Test prüft wirklich etwas" ist belegt statt behauptet.
- **Voraussetzung:** keine.
- **Aufwand:** 1 Zeile, Formulierung der Übergabe.

### 2.6 Verträglichkeit persistierter Daten und Exporte

- **Beobachtung:** Bei einer Erweiterung des Wertebereichs blieben gespeicherte Daten, Export-Mappings und Fremdsysteme ungeprüft.
- **Ort:** `coder.SOUL.md.template` Schritt 10; Gegenprobe in `reviewer.SOUL.md.template` bei den Prüfpflichten (`:25`).
- **Coder-Text:** `When the change alters a persisted value set, an enum, a schema, or an outbound mapping, verify existing stored data and every export path before the handoff and record the result.`
- **Reviewer-Text:** `Verify that claim against the actual mapping or query, not against the Coder's sentence.`
- **Wirkung:** Fachliche Folgen außerhalb des Repos werden sichtbar.
- **Voraussetzung:** Leserecht auf die Test-Datenbank (vorhanden).
- **Aufwand:** 2 Zeilen, bedingt formuliert.

### 2.7 Aufräumen nach dem Urteil

- **Beobachtung:** Kein Schritt räumt Branch, Scratch oder eigene Container auf.
- **Ort:** `coder.SOUL.md.template` Schritt 15.
- **Text:** `Delete temporary branches, scratch directories, and owned containers after the verdict; keep the commit and the evidence path.`
- **Wirkung:** Kein Rückstandsballast, der spätere Läufe verlangsamt oder verdeckt.
- **Voraussetzung:** keine.
- **Aufwand:** 1 Zeile.

### 2.8 Nachbetrachtung

- **Beobachtung:** `retro` liegt im Planner-Werkzeugkasten; in drei Läufen nie genutzt.
- **Ort:** `planner.SOUL.md.template`, Abschluss (`:94`-Umfeld).
- **Text:** `After the closing verdict, record the run's reusable lessons once: a durable rule candidate as a proposal, a verified tool fact in memory; do not rewrite role rules yourself.`
- **Wirkung:** Erkenntnisse werden nicht mit dem Lauf gelöscht.
- **Voraussetzung:** keine.
- **Aufwand:** 1 Zeile.

### 2.9 Entscheidungen festhalten

- **Beobachtung:** Eine fachliche Pflicht (MVH-Hinweis) ist im Code und im Changelog, aber nicht als Entscheidung dokumentiert.
- **Ort:** `planner.SOUL.md.template`, Plan-/ADR-Umfeld (`:70`).
- **Text:** `Record a decision that outlives the ticket, such as a compliance rule, a contract change, or an irreversible choice, as a short ADR or glossary entry at the plan baseline.`
- **Wirkung:** Die Begründung überlebt den Lauf.
- **Voraussetzung:** keine.
- **Aufwand:** 1 Zeile.

### 2.10 Ticket, PR und Pipeline verknüpfen

- **Beobachtung:** Kein PR, also keine Verknüpfung; der Abschluss läuft ausschließlich über Kanban.
- **Ort:** `coder.SOUL.md.template`, Schritt 14.
- **Text:** `Reference the pull request on the ticket and read the reference back; close the ticket only through the native Kanban path.`
- **Wirkung:** Karte und Code-Stand sind gegenseitig auffindbar.
- **Voraussetzung:** 2.2, 2.3.
- **Aufwand:** 1 Zeile.

### 2.11 Invarianten benennen, die der Wechsel brechen kann (Planner)

- **Beobachtung:** Der Kartentext von Lauf 3 enthält keinen Treffer für security, read-only, role, permission oder episode. Lauf 2 verlangte im Codex-Auftrag ausdrücklich „Preserve … security/episode/read-only checks". Genau diese Prüfungen fehlten in Lauf 3 im Repo.
- **Ort:** `templates/roles/planner.SOUL.md.template`, Abschnitt zur Kartenstruktur (bei `:70`).
- **Text:** `Name each existing invariant the change can break and the test that covers it, using the changed symbol, contract, or route as the boundary of that search.` Dazu: `When no existing test covers such an invariant, record that gap on the card as a limit; writing a new test for it needs its own acceptance criterion.` Dazu: `Do not turn that search into a coverage goal: adjacent behaviour, untested modules, and general test improvements stay out of scope and are named as out of scope.`
- **Wirkung:** Die Prüfpflicht steht im Auftrag, wo sie wirkt — und sie ist auf das begrenzt, was der Wechsel berühren kann.
- **Voraussetzung:** keine.
- **Aufwand:** 3 Zeilen.

### 2.12 Quellengeprüft von ausgeführt geprüft trennen (Reviewer)

- **Beobachtung:** Daniel hielt fest: „EpisodeService and security configuration retain authenticated doctor access, audit calls, read-only checks … No feature-related authorization change found." Das ist eine Quellenaussage im Prüfpunkt „Safeguard bypass" und liest sich wie ein Testersatz. Im Repo existiert keine Zugriffstest-Suite für `EcogStatus`.
- **Ort:** `templates/roles/reviewer.SOUL.md.template`, Abschnitt „Evidence and memory" (bei `:87`).
- **Text:** `Separate what you verified by execution from what you verified by reading source; a safeguard read but not executed is reported as source-verified.` Dazu: `Report a missing test as a limit on the card; do not turn it into a requirement inside the same review round.` Dazu: `Do not request tests beyond the acceptance criteria and the invariants named on the card.`
- **Wirkung:** Der Leser sieht, welche Schutzaussage belegt und welche nur gelesen ist — ohne dass der Reviewer neue Kriterien erfindet.
- **Voraussetzung:** keine.
- **Aufwand:** 3 Zeilen.

## 3. Changesets

| Paket | Inhalt | Voraussetzung | Version |
|---|---|---|---|
| **A** | 2.4, 2.5, 2.1, 2.7, 2.11, 2.12 | keine | 2.8.9 (PATCH) |
| **B** | 2.2, 2.3, 2.10 | Push-Recht, Pipeline-Zugang, eigene Freigabe | 2.9.0 (MINOR) |
| **C** | 2.6, 2.8, 2.9 | keine | 2.8.10 (PATCH) |

Reihenfolge: A → C → B. A ist sofort wirksam und kostet keine Rechte. B ist der größte Gewinn, aber eine Berechtigungsfrage; solange sie offen ist, bleibt der Text wirkungslos und gehört nicht ausgeliefert.

## 4. Was nicht in den Maker gehört

- **Planfreigabe:** Der Kunde prüft und akzeptiert den Plan. Kein Agentenschritt.
- **Manuelle Abnahme im laufenden System:** menschlicher Tester.
- **Vergabe von Push-Rechten und Merge-Entscheidung:** Betreiberentscheidung, keine Rollenregel.

## 5. Offene Entscheidungen

1. Bekommt das Team Push-Recht auf einen Fork oder direkt auf `develop`? Ohne Antwort bleibt Paket B entworfen, aber nicht ausgeliefert.
2. Wird `gh` auf dem Host installiert oder geht die Pipeline-Abfrage über die API? (Werkzeugweg, keine Rollenregel.)
3. Darf die Pipeline in der Testphase laufen — inklusive `deploy-dev.yml`-Nähe — oder nur die Prüf-Workflows?
4. Wer trägt den Merge: der Agent nach APPROVE oder der Mensch nach PR?

## 6. Abnahmekriterien

1. Jede geänderte Regel steht an genau einer Stelle; keine zweite Aussage dazu in derselben Datei.
2. Kein Byte-Deckel betroffen: alle Texte liegen in `templates/roles/`, nicht in `skills/brownfield-feature-planning/`.
3. `python3 -B -m unittest discover -s references -p 'test_*.py'` bleibt grün; wörtlich geprüfte Sätze bleiben unverändert.
4. Ein Bump je Changeset in `SKILL.md` und `manifest.json`.
5. Nach dem Rollout: die geänderten Stellen im Zielprofil rückgelesen, nicht nur die Version.
6. Wirksamkeitsnachweis erst im nächsten Lauf: Branch angelegt, Verbraucherliste auf der Karte, roter Lauf belegt.

## 7. Was dieser Plan nicht belegt

- Dass die zusätzlichen Schritte Tokens sparen. 2.4 und 2.5 kosten Aufrufe; ihr Nutzen ist Qualität, nicht Verbrauch.
- Dass Paket B den Prozess verbessert, solange Rechte und Werkzeuge fehlen.
- Dass ein Branch je Lauf bei dieser Repo-Größe nötig ist — belegt ist nur, dass ohne ihn kein PR möglich ist.
