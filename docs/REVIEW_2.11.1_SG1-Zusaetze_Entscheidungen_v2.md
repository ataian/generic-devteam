# SG1-Zusätze – Entscheidungen

**v2:** Punkt 1 beschlossen und im Maker-Arbeitsbaum 2.11.2 umgesetzt. [Bewertung und Quellen zu allen sechs Punkten](REVIEW_2.11.1_SG1-Zusaetze_Entscheidungen_v1.md).

| Nr. | Entscheidung |
|---|---|
| 1 | Angenommen: Nur wenn Git die vorgesehene Plandatei ignoriert, prüft der Planner die passende Regel. Eine genehmigte Ausnahme betrifft ausschließlich diesen Pfad; fehlt die Freigabe, meldet er den Ausschluss. Alle anderen Ausschlüsse bleiben bestehen. |
| 2–6 | Offen; keine Paketänderung für diese Punkte. |

**Prüfung zu 1:** 19 Brownfield-Tests bestanden, Größenbudgets eingehalten. Gesamtsuite: 243 Tests, 1 übersprungen, keine Fehler. `git diff --check` sauber. Unabhängiges Textreview: Ausnahme bedingt, kein zusätzlicher Routinecheck, bisherige Staging-Pflichten erhalten. Kein SG1-Update.
