# HANDOFF — Besprechung von Punkt 6: welche Coder-/Reviewer-Regeln der Planner braucht

| Feld | Wert |
|---|---|
| Datum | 2026-11-15 |
| Maker-Stand | **2.8.16**, Commit `bef909a` (Basis `aa07b0c` = 2.8.15 + Plan-Datei) |
| Branch | `v3`; Max pusht selbst |
| Zustand | Arbeitsbaum clean, Suite `OK (skipped=1)` (212 Tests, 292 s), **kein Rollout** auf Teams |
| Vorgänger | `docs/PLAN_2.8.16_Plan-Completeness_v2.md` (umgesetzt in `bef909a`) |
| Prüfbericht | `/home/mariko/projects/generic-devteam-review/plan-completeness-2026-11-15.md` (10 Lücken, 16 Doppelungsbefunde, 1 Ballast-Block) |

## 1. Warum diese Session

In 2.8.16 sind fünf Textänderungen umgesetzt. Zwei der zehn Lücken aus dem Prüfbericht sind damit erledigt (A2 Verbraucherliste, A3 Altdaten und Exportpfade), eine teilweise (A4 Risikokatalog, nur vier Achsen). Acht Punkte sind offen, dazu kommt ein neues Finding aus der Umsetzung. Diese Session entscheidet, was davon in den Maker geht — Textänderung erst nach Freigabe.

## 2. Was in 2.8.16 bereits geändert wurde

| Änderung | Datei | Wirkung |
|---|---|---|
| S1 | `planner.SOUL:82` | Konkurrenzprüfung („one active task per agent") entfällt, Wake-Prüfung bleibt |
| S2 | `planner.SOUL`, Schritt 4 | Verbraucher (code, exports, print views, generated clients, downstream mappings), Altdaten und Exportpfade, Kriterium je betroffenem Verbraucher |
| S3 | `planner.SOUL`, Schritt 4 (verschoben aus Schritt 7) | Invariantenregel: Testbestand entscheidet nur über Wiederverwendung, nicht über Behandlung; Limit nur mit Grund; Risikoachsen Sicherheit, Datenintegrität, API-Verträge, Nebenläufigkeit; `:78` als Bremse unverändert |
| S4 | `coder.SOUL:19` | Betroffener Verbraucher gehört in den Auftrag; unveränderte Verbraucher und fremde Testlücken bleiben draußen |
| S5 | `coder.SOUL:21` | Arbeitsbaum muss auf dem Branch stehen, nicht nur der Branch existieren |

**Zurückgezogen:** eine Änderung an `skills/brownfield-feature-planning/references/kanban-phase-release.md:29`. Sie hätte die SOUL im Skill wiederholt; der dortige Satz betrifft Einrichtungsfakten und steht nicht im Konflikt mit der Wake-Prüfung.

**Nicht angefasst:** `reviewer.SOUL.md.template` (bytegleich zu 2.8.15).

## 3. Neues Finding (Auslöser für Punkt 6)

`reviewer.SOUL.md.template:94`

> Report a missing test as a limit on the card; do not turn it into a requirement inside the same review round.

Direkt daneben, `:95`:

> Do not request tests beyond the acceptance criteria and the invariants named on the card.

Das ist dieselbe Mechanik wie der alte Planner-Satz `:77`, nur auf der Reviewerseite: Fehlt ein Test, wird er als Limit auf der Karte festgehalten und darf in derselben Runde nicht zur Anforderung werden. Solange der Planner Lücken als Limit ablegen durfte, war das Paar konsistent — und hat die Lücke zementiert: der Planner erklärt sie zur Grenze, der Reviewer darf sie nicht nachziehen, niemand prüft sie. Mit 2.8.16 muss der Planner jede brechbare Invariante abdecken; damit gerät `:94` in eine neue Rolle: Es schützt jetzt nur noch vor Nachforderungen im laufenden Review, kann aber einen Planner-Fehler weiter als akzeptierte Grenze festschreiben.

Offene Fragen für die Besprechung:
1. Bleibt `:94` als Schutz gegen Nachforderungen, oder braucht es eine Pflicht, den Fall an den Planner zurückzugeben statt ihn als Limit zu verbuchen?
2. Wie verhält sich `:94` zu `:95` — ist das eine Regel oder zwei?
3. Gilt die Rückgabe auch dann, wenn die Invariante im Plan steht, der Coder sie aber nicht getestet hat?

## 4. Offene Kandidaten aus dem Prüfbericht

Reihenfolge = Vorschlag, nicht Entscheidung. Je Punkt: Quelle, was der Plan dadurch gewinnt, heutiger Planner-Stand.

1. **A1 Bibliotheks-Versionierung und Verbraucherkette** (`reviewer.SOUL:30`, `project-lib-versioning:24,29,30`). Der Plan müsste Versionsschritt je Bibliothek, rekursive Verbraucherkette und Artefaktauflösung führen. Planner-Stand: Lücke — `planner.SOUL:121` nennt den Skill nie, obwohl er per `manifest.json` für den Planner installiert ist. Erste Frage: fehlender Aufruf oder fehlende Regel?
2. **A4 Risikokatalog, zweite Hälfte** (`reviewer.SOUL:26,58,74`). 2.8.16 nennt vier Achsen (Sicherheit, Datenintegrität, API-Verträge, Nebenläufigkeit). Der Reviewer-Katalog enthält zusätzlich Rechte/Rollen, Secrets/Krypto, Transaktionen/Sperren, destruktive Datenänderungen und Migrationen mit Risiko. Frage: reichen die vier Achsen, oder wird der Katalog übernommen — und dann als Kopie mit Driftrisiko?
3. **A5 Separater Hochrisiko-Durchgang** (`reviewer.SOUL:62`). Verlangt bei Sicherheits-/Datenintegritäts-/Transaktions-/Nebenläufigkeitsfolgen einen eigenen Pass vor dem Urteil. Der Plan müsste diesen Aufwand und Gate-Zeitpunkt ausweisen. Planner-Stand: Lücke.
4. **A6 Vergleichsbedingungen visueller Kriterien** (`reviewer.SOUL:31`, `screenshot-to-code/references/visual-check.md:5-11`). Source, Viewport, Zoom/DPR, Datenzustand, anerkannte Abweichungen gehören in den Plan, sonst ist das Kriterium offen. Planner-Stand: Teilbefund — steht nur im skill-gebundenen Pfad.
5. **A7 Bug-Pläne: Symptom, Sollverhalten, Repro** (`diagnosing-bugs:22,46-52`). Der Fehlerpfad setzt diese Angaben voraus. Planner-Stand: Lücke; der Skill ist nur für Team-Codex vorgesehen, der Planner erbt ihn nicht.
6. **A8 Zweiter Harness oder Fixture-Baum** (`coder.SOUL:55`). Der Coder braucht für einen zweiten Prüfpfad eine Planner-Entscheidung. Der Plan sollte den Prüfpfad benennen. Planner-Stand: Teilbefund — Harness wird behandelt, seine Identität nicht festgelegt.
7. **A9 Indexbefund ersetzt keine Quelllesung** (`coder.SOUL:87`). Planner hat nur die zweite Hälfte („Missing index links do not prove a missing dependency", `:120`). Fehlende Indexkante darf nicht als „kein Verbraucher" in die Dateiliste wandern.
8. **A10 Tests prüfen Verhalten, nicht Quelltext** (`sdlc-review:99`). Kriterium „Test X existiert" ist ohne Verhaltensprüfung erfüllbar; der Plan müsste die Beweisform festlegen. Planner-Stand: Lücke, schwach — `:58` kommt nahe.

Dazu zwei Fragen, die keine Regel sind, aber in dieselbe Sitzung gehören:
- **Reviewtiefe aus Lauf 5.** Daniel hat weder Backend-Test noch Generierung/Build selbst ausgeführt und den Kommentar um 44 % gekürzt, ohne Regeländerung. Ist das Verhaltensschwankung oder braucht die Reviewer-SOUL eine Mindestbeweisform je Kriterium?
- **A9/A9-Verwandtschaft:** `planner.SOUL:120` und `coder.SOUL:87` sagen dieselbe Sache halb. Zusammenführen oder bei einer Rolle lassen?

## 5. Arbeitsweise, die in dieser Sitzung gilt

- **TAS zuerst:** `/home/mariko/projects/tas/SKILL.md` und `references/tas-authoring-standard.md` lesen, bevor eine Formulierung entsteht. Pakettexte sind englisch.
- **Ein Befund je Entscheidung.** Max entscheidet einzeln; keine Sammelfreigabe über acht Punkte.
- **Plandokument vor Templatetext.** Mehr als eine Regel berührt ⇒ Plan nach `plan-versioning-semver` (`PLAN_<Appversion>_<Name>_v<N>.md`) in `docs/`, Templates und Version erst nach Freigabe. Bestehende Pläne per `mv` hochzählen, nicht überschreiben.
- **Doppelungen vor Ergänzung prüfen.** Der Prüfbericht führt 16 Doppelungsbefunde; mehrere Kandidaten sind dort schon als „bereits indirekt gedeckt" ausgewiesen. Eine Ergänzung, die im Planner nur wiederholt, was ein geladener Skill sagt, fällt weg.
- **ALT-Zeilen vor dem Edit per `grep -F` prüfen**, danach `python3 -B -m unittest discover -s references -p 'test_*.py'` (Erwartung `OK (skipped=1)`), ein PATCH-Bump je zusammenhängendem Änderungssatz.
- **Kein Rollout.** Jacks Team läuft bis zu einem eigenen Update auf 2.8.15.

## 6. Quellen

- Maker: `/home/mariko/projects/generic-devteam` — `templates/roles/{planner,coder,reviewer}.SOUL.md.template`, `skills/brownfield-feature-planning/`, `skills/project-lib-versioning/`, `manifest.json`.
- Prüfbericht: `/home/mariko/projects/generic-devteam-review/plan-completeness-2026-11-15.md`.
- Lauf-5-Auswertung: `/home/mariko/projects/devteam-tokenprofiling/ecog-replay-2026-11-15-lauf5/` mit `VERGLEICH_2.8.15_Laeufe-1-5_v1.0.0.md`.
- Plan: `docs/PLAN_2.8.16_Plan-Completeness_v2.md`.
