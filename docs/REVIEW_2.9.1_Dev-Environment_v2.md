# Review: Docker development environment skill — `SPEC_2.9.1_Dev-Environment_v3.md`

**Verdict: APPROVED**
**Reviewer:** Fujiko (independent document review, Kanban task `t_2523e1d2`)
**Review round:** 1 of this card — artifact lens (cold read of the v3 delta before the handoff narrative, then execution of the affected checks)
**Date:** 2026-11-17T02:50+01:00
**Scope:** document review only. No implementation, no profile or package change, no commit, no container operation. Mariko remains the author; nothing is routed to Anjin.

The three blocking findings of round 1 (B1–B3) are closed, and all eight recommendations (N1–N8) are applied as specified. I reproduced the mechanical claims independently instead of accepting them: the eight anchors, the role-paragraph agreement, the prototype exception, the R7/R8 placement, and the green/red/green focused contract test. I found no new blocking defect. Two cosmetic inaccuracies, one host-local tooling caveat and the evidence limits in §5 are recorded below; none of them requires another round.

---

## 1. Reviewed identity and frozen inputs

| Item | Value |
| --- | --- |
| Reviewed document | `/home/mariko/projects/generic-devteam/docs/SPEC_2.9.1_Dev-Environment_v3.md` |
| SHA-256 | `e582378337f513717deec398e74b81eb7cf3f831b94683af3bfbab41e2b9315e` (matches `frozen-inputs.json`) |
| Superseded | `SPEC_2.9.1_Dev-Environment_v2.md` = `c920b2d9…ac741dc` (matches) |
| Prior review | `REVIEW_2.9.1_Dev-Environment_v1.md` = `9aca846f…1a2d9f` (matches, unchanged) |
| Maker baseline | `94ded22fa58b1c41956985c3edd562c443bae7af`; `git diff HEAD` empty for tracked files; only the four untracked drafts appear in `git status` |
| Role templates | planner `769070f6…3bfc9`, coder `f0fde663…7be80d`, reviewer `a595fcba…ab2800` — all match |
| Test surface | `references/test_brownfield_planning.py` = `cd62da77…cb7eb` (matches) |

Hash equality was measured immediately before review and again immediately before delivery (§7). No input drift, so no moving target.

## 2. What I verified by execution, not by claim

Independent script `/home/mariko/projects/generic-devteam-review/dev-environment-v3/fujiko_recheck_v3.py` (output retained in `fujiko-recheck/`), plus `fujiko_anchor_check.py`:

- **All eight anchors match exactly once at the stated source line**: R1 planner:12, R2 coder:77, R3 coder:24, R4 reviewer:86, R5 reviewer:43, R6 planner:104, R7 planner:48, R8 planner:77. Count and line were computed from the frozen templates, not read from the specification.
- **The shared authority paragraph is byte-identical in all three rendered role texts** (identical SHA-256 of the paragraph line: `4c2cab45…2746b8`), and its exact sentence also appears in the candidate skill (4 occurrences of the building/running classification: skill + 3 roles).
- **The prototype-only exception is byte-for-byte unchanged** and still contiguous between "During grilling," and "During the interview,"; R7 was inserted after the design-check block, not inside that exception.
- **R7 and R8 sit where they must**: design checks → `load the owned dev-environment` → step 3; and step 7 → guide/container requirement → step 8. Placement is inside "Planning workflow", which was the point of B1.
- **The focused contract test behaves green / red / green** against the unmodified test file with only the Planner template swapped: baseline `OK` (1 test), R1-with-old-assertion `FAIL` (assertion error quoting the obsolete phrase), all-replacements-with-corrected-assertion `OK`. Same result from the author's published command (`verify_draft.py`), which I ran from a copied location: it prints `PASS` and writes only beside itself.
- **The `assertNotIn` single-source checks are untouched and still valid**: the obsolete phrase occurs twice in the test file — once in the negative `assertNotIn` block (line 155, against `SKILL.md`) and once in the positive `assertIn` block (line 165, against the template). Only the positive one is replaced, exactly as section 5 now states.
- **No other test in the package pins a replaced phrase.** I grepped all eight ALT phrases across `references/`: no test asserts the R2, R3, R4, R5 or R6 clause verbatim. Three R6/R7/R8 fragments are asserted with `assertIn` in `test_render_reasoning.py` (lines 542, 613, 682) and survive as substrings of the new text — checked directly in the combined templates. That file's stricter structural assertion `re.findall(r"^(\d+)\. ", workflow)` still yields `1..11`, because R7/R8 insert 3-space-indented continuation lines that cannot match a column-0 step heading. The design-slice test that splits the workflow at "For relevant module/interface choices during design:" still contains R7's sentence and all four of its original clauses.
- **Candidate static form**: `check_candidate_skill.py` with the exact reproduction command from section 8 returns `problems: []`, exit 0; the script exists at the named path. Exactly one synthetic-data grant remains in the candidate ("The team may generate synthetic data…"), and the removed sentence is gone.
- **Whitespace and tracked-file claims hold**: `git diff --no-index --check` reports no whitespace error; tracked Maker files are unmodified.

## 3. Closure of the blocking findings

### B1 — Unanchored Planner replacements → closed
R7 and R8 now exist as anchored `ALT`/`NEU` blocks in the same style as R1–R6, with stated lines (48 and 77) that both match exactly once. The promise "Exact replacements R1, R6, R7, R8 below" is therefore true; the table row no longer overclaims. The author chose :48 for R7 instead of my suggested :33. That is a defensible deviation and not a regression: :48 is still inside "Planning workflow", follows the design-check block, and keeps the prototype-only exception untouched, which is what my B1 required: the clause must bind in the workflow rather than in "Communication". R8 is inside step 7, which owns ticket-body structure, so the guide requirement now binds ticket authoring as intended.

### B2 — Missing update surface with a proven regression → closed
Section 5 names `references/test_brownfield_planning.py` and specifies the change precisely: update only the positive `soul_clause` assertion at line 165 to the R1 NEU sentence, preserve the negative single-source checks. Line numbers and scope are correct (verified above, including that line 155 is the `assertNotIn` block and must stay). The regression is not merely asserted but reproducible: red with the old assertion, green after the specified correction. Requirement 10's single-source intent is preserved because R1 keeps the narrowed "For other resources, …" rule and the test still enforces that the rule does not migrate into the planning skill.

### B3 — Reviewer deployment carve-out → closed
R4 now reads "Do not push, deploy, operate unrelated services, or change host configuration from a review task." The qualified "deploy outside the assigned development environment" is gone, so the implied in-environment deployment permission no longer exists. At the same time the correction avoids the over-correction I warned about in the assignment: `restart` is no longer prohibited (it is now covered by the assigned-runtime authority paragraph), and the authority paragraph keeps every enumerated operation autonomous — start, stop, restart, rebuild, recreation, synthetic data generation, disposable-state reset — explicitly "without further customer approval". Building and running a candidate in the assigned runtime is classified as a development operation in the skill and in all three role texts, so the classification no longer has a referent-less carve-out: deployment stays prohibited, ordinary runtime work stays permitted. Product-source ownership, real data, host administration, shared infrastructure and external effects are unchanged in all three paragraphs.

### Recommendations N1–N8 → all applied
- **N1:** `Beyond that,` now separates the deviation-only compass from the mandatory demo access; both requirements stand in separate scopes.
- **N2:** one permission remains, in the candidate's Operating scope; the duplicates in contract setting and baseline preparation are deleted. The surviving mentions in section 1 (confirmed customer decision) and step 4 ("apply … synthetic test/demo data") are requirement and instruction, not competing authority.
- **N3:** the real checker path and the exact command are named and reproduce cleanly. Correctly labelled as an authoring helper, not a delivered dependency.
- **N4:** the boundary sentence now distinguishes this documentation task's execution authorization from the future team's runtime authority.
- **N5:** the shared-paragraph agreement is required of the future package tests. My independent hash check confirms the three paragraphs are identical today.
- **N6:** step 2 routes stack choices through the Planner's existing customer clarification path; no parallel interview.
- **N7/N8:** "Choose the construction path" and "Coder/Team-Codex" are used consistently; the old phrasings do not survive anywhere in the document or the package.

## 4. New findings (none blocking)

**Cosmetic-1 — section 5 reviewer row understates the new prohibition.** The verification column reads "no self-repair, self-approval, push or external deployment", while R4 prohibits *all* deployment. The binding text is the stricter one, so the practical risk is a future reader mistaking the summary for the contract. Fix opportunistically when the changeset is written; no new round needed.

**Cosmetic-2 — "read-only" remains partially unqualified in the Reviewer SOUL.** R5 defines read-only as product-source read-only for helpers, but the high-risk section still says "Apply the same model/provider, reasoning, access, approval, and read-only limits to this pass". The new authority paragraph outranks it by specificity ("from a review task"), so behaviour is determined; only the vocabulary is uneven. Optional.

**Tooling caveat — the checker is host-local.** `check_candidate_skill.py` lives under `/home/mariko/.hermes/skills/generic-devteam/scripts/` and is not in the Maker repository (`find` over `generic-devteam` returns nothing). The reproduction command therefore works on this host, as I verified, but not from a fresh repository checkout. Acceptable for a document gate; worth one word in the implementation task.

## 5. Evidence limits

- **No runtime evidence for the design.** No Docker build, container, PostgreSQL template clone, generated team or live agent behaviour was exercised — out of scope for this document review by the assignment, so this report says nothing about whether the environment skill works. The package suite, the container scenarios and the absent/pre-existing-environment qualifications remain implementation gates; section 8 correctly does not claim them.
- **The full package suite was not run.** Only the affected focused test was executed, plus static greps of every other test that touches the replaced phrases and the structural `1..11` step assertion. Baseline greenness of the whole suite is not measured here and is not needed for this verdict.
- **I did not re-run the author's `verify_draft.py` in place**, to avoid overwriting their retained fixtures and logs with my run. I ran it from a copy and reproduced the same results with my own script in `fujiko-recheck/`.
- **Section 6 (SG1/MTB source inspection) was not repeated.** Those files are evidence for the design's origin, not requirements for this revision, and the round-1 report already accepted them.
- **Behavioural adequacy of the wording is not proven by these checks.** Static matches and one contract test show that the text is anchored, consistent and green; they cannot show how a live agent applies "coordinate disruptive operations" or "without further customer approval".

## 6. Verdict

**APPROVED.** B1, B2 and B3 are closed with the deltas actually present in the text, not merely asserted. N1–N8 are applied. Devteam autonomy over the assigned development runtime is preserved and strengthened (explicit operations list, explicit "without further customer approval", explicit development-operation classification), while the role boundaries stay intact: the Reviewer still may not self-implement, self-approve, push, deploy or change host configuration; the Coder still implements through Team-Codex; the Planner still neither implements product code nor gains a parallel approval route. No new approval gate, no extra round, no new test infrastructure was demanded.

Two cosmetic inaccuracies and one host-local tooling caveat are recorded for the implementation changeset. They do not block this revision.

**Report delivery and specification approval are separate.** This report is delivered as an artifact of task `t_2523e1d2`; the specification verdict above is `APPROVED` for the reviewed identity in §1 only. It does not authorize implementation, commit, push, installation or SG1 conversion, and it does not approve any later revision of the document.

---

## Kurzfazit für Max (Deutsch)

**Urteil: APPROVED.** Die drei blockierenden Punkte aus der ersten Runde sind erledigt, die acht Empfehlungen umgesetzt. Ich habe die Behauptungen nachgerechnet statt sie zu glauben: alle acht Anker passen genau einmal an der genannten Zeile (R7 Planner:48, R8 Planner:77), der gemeinsame Befugnis-Absatz ist in allen drei Rollen bytegleich, die Prototyp-Ausnahme ist unverändert, R7/R8 sitzen an der richtigen Stelle im Planungsworkflow, und der fokussierte Vertragstest läuft grün → rot → grün wie beschrieben. `test_brownfield_planning.py:155` (assertNotIn gegen den Skill) bleibt korrekt unangetastet, nur die positive Zusicherung auf Zeile 165 wird geändert. Kein anderer Pakettest fixiert einen der ersetzten Sätze; die drei betroffenen `assertIn`-Anker in `test_render_reasoning.py` überleben als Teilstring, und die Strukturzusicherung auf die Workflow-Schritte 1–11 bleibt gültig, weil die neuen Zeilen eingerückt sind.

Inhaltlich ist die Rollengrenze jetzt sauber: Der Reviewer darf `deploy` überhaupt nicht mehr (die stillschweigende Erlaubnis "deploy outside the assigned development environment" ist weg), darf aber Laufzeit im zugewiesenen Entwicklungsumfeld autonom betreiben — starten, stoppen, neu starten, neu bauen, neu erzeugen, synthetische Daten, Reset, ausdrücklich "without further customer approval". Damit ist Devteam-Autonomie erhalten und die externe Grenze enger als vorher.

Zwei kosmetische Stellen (Abschnitt-5-Zeile sagt "external deployment", der bindende Text verbietet jedes Deployment; "read-only" ist nur in der Helper-Klausel präzisiert) und ein Hinweis zum Prüfskript (`check_candidate_skill.py` liegt nur im installierten Hermes-Profil, nicht im Maker-Repo) sind für den Umsetzungsauftrag notiert — kein Grund für eine weitere Runde. Laufzeitnachweise (Docker, PostgreSQL, generiertes Team) bleiben wie vereinbart Umsetzungs-Gates. Berichtslieferung und Spezifikationsfreigabe sind getrennt: freigegeben ist genau die geprüfte Fassung `e582378…9315e`.

*Reviewed by Fujiko — report delivered; specification verdict kept separate from card completion.*
