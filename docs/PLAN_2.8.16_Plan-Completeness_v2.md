# PLAN — Planvollständigkeit und Rollenabgrenzung

| Feld | Wert |
|---|---|
| Appversion (Ausgangsversion) | Maker **2.8.15** (`859dc08`) |
| Dokumentversion | **v2** (v1: erster Entwurf; v2: „visible" entfernt, Exportpfade und Altdaten in den Planner aufgenommen, Invariantenregel umformuliert und in Schritt 4 verschoben, S5 zurückgezogen) |
| Datum | 2026-11-15 |
| Charakter | Vorbereitung. Templates und Version ändern sich erst auf ausdrückliches „umsetzen". |
| Auslöser | Lauf 5 (ECOG-5, 15.11.2026) und die Auswertung dieses Laufs |

## 1. Beobachtungen, die diesen Plan tragen

1. **Der Druck-Verbraucher fehlte im Plan, obwohl der Coder ihn fand.** `carter.SOUL:19` verlangt vor dem ersten Codex-Call eine Verbraucherliste und nennt „print views" wörtlich. Carter hat sie erstellt und den Druckpfad gemeldet („Print view reuses read-only table warning"). Der Plan des Planners nannte ihn nicht; `grep -i print` findet in Plan und Design keinen Treffer. Die Planner-Suche hat eine andere Grenze: „using the changed symbol, contract, or route as the boundary of that search" (`planner.SOUL:76`).
2. **Der Coder durfte den Fund nicht selbst als in-scope behandeln.** Seine Regel sagt: „Name consumers outside the acceptance scope as explicitly out of scope instead of leaving them unmentioned" (`coder.SOUL:19`). Ein betroffener Verbraucher fällt damit formal aus dem Auftrag, obwohl die Änderung ihn verändert. „Sichtbar" ist dafür kein brauchbares Merkmal: Ein Mapper, ein Import oder eine gespeicherte Zuordnung arbeitet auch dann falsch, wenn keine Oberfläche etwas zeigt.
3. **Die Invariantenregel steht in Schritt 7, nicht in Schritt 4.** `planner.SOUL:76-77` hängen an der Ticket-Erstellung. Der angenommene Plan selbst wird von ihnen nicht erreicht — deshalb konnte der Druck kein Plan-Kriterium werden.
4. **`:77` erlaubt, eine Invariante als Limit abzulegen, statt sie zu behandeln.** Ein Limit ist eine aufgeschriebene, akzeptierte Lücke: Der Plan führt sie im Abschnitt „Invariant coverage and limits", der Coder setzt sie auf die Karte, der Reviewer übernimmt sie als „limits retained" — danach prüft sie niemand mehr. Lauf 5 nutzt diesen Weg: „no focused ECOG test found; A1/A7 add narrow coverage", „General delete/error-flow coverage stays out of scope". Damit hängt die Behandlung einer Invariante davon ab, ob zufällig schon ein Test existiert, obwohl der Auslöser die Änderung ist. `:78` verhindert bereits, dass daraus eine Testreihe über den Auftrag hinaus wird.
5. **Zwei Sätze widersprechen sich in der Sache.** `planner.SOUL:82` verlangt vor der Freigabe „verify that the board enforces exactly one active task per agent and that the Planner wake subscription works". Die Reihenfolge erzwingen aber die Abhängigkeitskanten und der Dispatcher; die Nebenläufigkeitsgrenze ist ein Einrichtungsfakt. Der Wake dagegen trägt jede Review- und Abschlussmeldung und bleibt prüfpflichtig.
6. **Der Coder bestätigt den Branch, aber nicht den Arbeitsbaum.** `coder.SOUL:21` verlangt „Confirm the card's implementation branch exists at the named baseline commit". Existiert der Branch am Basiscommit, während der Arbeitsbaum auf einem anderen steht, ist die Regel erfüllt und die Arbeit liefe falsch. Carter prüfte in Lauf 5 zusätzlich `git branch --show-current` und lag richtig; verlangt war es nicht.

## 2. Änderungen

### S1 — Planner verliert die Konkurrenzprüfung, behält die Wake-Prüfung

`templates/roles/planner.SOUL.md.template:82`

**ALT**
> Before you change a ticket to `todo`, verify that the board enforces exactly one active task per agent and that the Planner wake subscription works.

**NEU**
> Before you change a ticket to `todo`, verify that the Planner wake subscription works.

**Begründung:** Sequenzierung liegt bei den Abhängigkeitskanten und dem Dispatcher; die Konkurrenzgrenze ist Einrichtungsfakt.
**Erhalten bleibt:** vollständige Elternkette, Assignee, Reviewer, Board, Workspace, Planbaseline; Freigabe erst nach gültiger Kette.

### S2 — Planner benennt die Wirkungsfläche im Plan

`templates/roles/planner.SOUL.md.template`, neue Zeile in Schritt 4 nach `:55` („Write a phase-based plan with requirements, affected repositories/files, dependencies, verification, acceptance gates, and commit boundaries."), vor `:56`.

**NEU**
> Name every consumer of each changed symbol, schema, or component in the plan: code, exports, print views, generated clients, and downstream mappings, with one line of evidence per consumer. Where the change alters a value set, enum, schema, or mapping, name the existing stored values and export paths it can break. A consumer whose behaviour the change can alter needs its own acceptance criterion.

**Begründung:** Die Verbraucherliste entsteht heute erst beim Coder, also nach Planannahme und nach der Kriterienfestlegung. Damit kann ein betroffener Verbraucher kein Kriterium mehr werden. Exportpfade und bestehende gespeicherte Werte gehören in dieselbe Frage — was hängt an der Änderung — und nicht in einen zweiten Satz. Der Planner prüft keine Datenbank; er benennt, welche bestehenden Werte mit dem geänderten Vertrag in Berührung kommen und was daran brechen kann. Das Prüfen der Daten bleibt beim Coder (`coder.SOUL:78`).
**Bewusst nicht „visible":** Ein Verbraucher ohne Oberfläche kann genauso brechen. Maßgeblich ist, ob die Änderung sein Verhalten ändern kann, nicht ob man es sieht.
**Erhalten bleibt:** `:44` („Identify everything callers must know") beschreibt den Zuschnitt einer Abstraktion, nicht die Verbraucher einer Änderung — andere Bedeutung, bleibt stehen.

### S3 — Invariantenregel wandert in Schritt 4 und wird umformuliert

`templates/roles/planner.SOUL.md.template:76-78` — Block nach Schritt 4 verschieben, dabei `:76` und `:77` ersetzen.

**ALT (`:76`)**
> Name each existing invariant the change can break and the test that covers it, using the changed symbol, contract, or route as the boundary of that search.

**ALT (`:77`)**
> When no existing test covers such an invariant, record that gap on the card as a limit; a new test for it needs its own acceptance criterion.

**NEU**
> Name each invariant the change can break, using the changed symbol, contract, route, its consumers, and the untested risk axes (security, data integrity, API contracts, concurrency) as the boundary of that search. An invariant the change can break must be covered: reuse the existing test, or add a new acceptance criterion when none covers it. Name a limit only for an invariant this project cannot verify, and state why.

**Erhalten bleibt (`:78`, unverändert, wandert mit)**
> Do not turn that search into a coverage goal: adjacent behaviour, untested modules, and general test improvements stay out of scope and are named as out of scope.

**Begründung:** Ob ein Test existiert, entscheidet künftig nur noch, ob er wiederverwendet oder geschrieben wird — nicht, ob die Invariante behandelt wird. Das Limit wird zur Ausnahme mit Begründung; „kein Test vorhanden" ist kein Grund mehr, sondern der Anlass. Die Risikoachsen erweitern die Suchgrenze um das, was keine Testsuche liefert. `:78` bleibt die Bremse gegen Testausweitung.

### S4 — Coder entscheidet über die Scope-Grenze bei betroffenen Verbrauchern

`templates/roles/coder.SOUL.md.template:19`, zweiter Satz.

**ALT**
> Name consumers outside the acceptance scope as explicitly out of scope instead of leaving them unmentioned.

**NEU**
> A consumer whose behaviour the change can alter belongs to the accepted scope: cover it with Codex and with acceptance evidence. Name unchanged consumers and unrelated missing tests as explicitly out of scope instead of leaving them unmentioned.

**Begründung:** Die Grenze verläuft am tatsächlichen Effekt, nicht am Ticketwortlaut. Der Coder entscheidet damit innerhalb seines Mandats, ohne die Testausweitung zu öffnen.
**Erhalten bleibt:** Pflicht zur Liste, ein Beleg je Verbraucher, Nennung ausgeschlossener Verbraucher.

### S5 — Coder prüft auch den Arbeitsbaum

`templates/roles/coder.SOUL.md.template:21`

**ALT**
> Confirm the card's implementation branch exists at the named baseline commit before the first Codex call. Return the card to the Planner when it is missing or based elsewhere; do not create, rename, or rebase that branch.

**NEU**
> Confirm before the first Codex call that the card's implementation branch exists at the named baseline commit and that the working tree is on that branch. Return the card to the Planner when it is missing, based elsewhere, or not checked out; do not create, rename, or rebase that branch.

**Begründung:** Zwei Zustände, zwei Prüfungen.
**Erhalten bleibt:** keine Branch-Erzeugung, kein Rebase, Rückgabe an den Planner bei Abweichung.

## 3. Zurückgezogen gegenüber v1

**Die Änderung an `skills/brownfield-feature-planning/references/kanban-phase-release.md:29` entfällt.** Sie hätte die Planner-SOUL im Skill wiederholt — genau die Doppelung, die abgebaut werden soll. Beim Nachlesen ist der Konflikt auch kleiner als in v1 beschrieben: Die Zeile verbietet das Nachprüfen von **Einrichtungsfakten** (Gateway, Dispatcher, Adapter-Eigentum, Routing, Dateiidentität). Die Wake-Subscription ist keine Einrichtungsprüfung, sondern eine Bindung pro Karte, die dieselbe Referenz in §2.12/13 ohnehin verlangt. Es bleibt bei einer Quelle: der SOUL (S1).

Folge für die Auswertung: Der Befund „Phase-Release verletzt" im Vergleichsbericht ist zu pauschal. Betroffen ist die Klasse der Einrichtungsprüfungen — Gateway-Status, `config get` je Profil, Hermes-Quelltext, Adapter-Probe, Hilfe-Serien. Die `notify-list`-Rücklesung gehört nicht dazu. Der Bericht wird entsprechend korrigiert.

## 4. Versionierung

Ein zusammenhängender Textänderungssatz: PATCH-Bump **2.8.15 → 2.8.16** in `SKILL.md` und `manifest.json`, ein Commit. Kein Rollout auf Teams in diesem Schritt — Regeln wirken für künftige Pläne; Jacks Team bekommt sie erst mit einem eigenen Update.

## 5. Prüfschritt bei Umsetzung

1. Vor dem ersten Edit: `git status` sauber, `git log -1` = `859dc08`.
2. Jede ALT-Zeile vor dem Edit mit `grep -F` gegen die Datei prüfen.
3. Nach den Edits: `python3 -B -m unittest discover -s references -p 'test_*.py'` — erwartet `OK (skipped=1)`. Kein Test bindet die fünf geänderten Sätze (geprüft: `grep -rn "one active task per agent\|print views\|wake subscription\|setup facts\|do not re-check" references/*.py` → kein Treffer).
4. Nach der Verschiebung prüfen, dass keine Kopie der Invariantenregel in Schritt 7 stehen bleibt: `grep -n "Name each existing invariant\|as a limit" templates/roles/planner.SOUL.md.template` muss nach der Änderung nur die neue Fassung in Schritt 4 treffen.
5. Nach dem Bump: Versionsfelder in `SKILL.md` und `manifest.json` vergleichen.

## 6. Nicht in diesem Änderungssatz

Die Prüfung weiterer Coder-/Reviewer-Regeln (Bericht `generic-devteam-review/plan-completeness-2026-11-15.md`) ergab zehn Lücken und sechzehn Doppelungsbefunde. Übernommen sind daraus nur die Risikoachsen in S3 und die Wirkungsfläche in S2. Die übrigen Fundstellen — Bibliotheks-Versionierung, Bug-Pläne ohne Symptom/Sollverhalten, zweiter Harness/Fixture-Baum, separater Hochrisiko-Durchgang, visuelle Vergleichsbedingungen — brauchen eigene Entscheidungen und einen eigenen Schritt.
