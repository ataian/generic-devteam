REVIEW — Maker 2.10.0, `SPEC_2.9.1_Dev-Environment_v3.md` implementation
Reviewer: Fujiko (independent, review-only; no implementer dispatched, no card/profile/Git action)
Date: 2026-11-17 (CET)

VERDICT: APPROVED

===============================================================
1. EXACT REVIEWED STATE (frozen, hash-verified twice)
===============================================================

Repository: /home/mariko/projects/generic-devteam, branch worktree uncommitted.
HEAD: 94ded22fa58b1c41956985c3edd562c443bae7af — unchanged before review and again immediately before this verdict.
Working tree: 12 modified tracked files, 2 new package files, 6 untracked historical documents (SPEC v1/v2/v3, REVIEW v1/v2, PLAN). No stray artifacts.

Frozen-input verification
- frozen-inputs.json: 81 entries. I resolved every entry with `sha256sum -c` (via jq-generated check list). Result at review start AND immediately before the verdict: 81/81 OK, 0 missing, 0 mismatches.
- implementation.diff f451607167b024a04f7fe583b4d225d5c86d73b1e145f2480fc0de3e715ce9e0: content identical to the current plain `git diff`; the only textual difference is that the frozen file lacks the final newline. My own test runs produced no working-tree drift (git status identical before/after).
- Spec e582378337f513717deec398e74b81eb7cf3f831b94683af3bfbab41e2b9315e, plan d7c43ad2…, prior review v2 d3da2861…, all original logs: all match.
No moving target.

New package files reviewed (a plain tracked diff omits them)
- skills/dev-environment/SKILL.md — sha256 024ede71ef9968fbed2340d71ddc466a39d3286045da6b28e851b6282964886c
- references/test_dev_environment.py — sha256 07616df775b82200f4716efcae86c44b1afa9ca63a072023adce22882e300e3e

===============================================================
2. WHAT I VERIFIED BY EXECUTION
===============================================================

2.1 Candidate skill is the approved text, not a paraphrase
Extracted spec lines 73–208 (the complete fenced ````markdown block) and diffed against the delivered file: diff exit 0, both sides sha256 024ede71… Acceptable: byte-identical to the approved candidate, at the stated package path, with the spec's own frontmatter (name, description "Create, adopt or revise a Docker dev environment.", version 0.1.0, MIT, platforms [linux], empty related_skills).

2.2 R1–R8 applied exactly, once each, ALTs gone
Every NEU line/paragraph matches the corresponding frozen template with `grep -Fx` count = 1; every displaced ALT string is at zero occurrences in the templates (the old reviewer restart-ban and coder approval trigger now survive only inside the historical spec/review documents, which is correct).
Applied positions (current line numbers; shifted only by the insertions themselves):
- planner: 12 R1 authority paragraph, 13 narrowed "For other resources…" rule, 50 R7 skill_view load, 80 R8 conditional ticket guide, 107 R6 demo access with "Beyond that,".
- coder: 25 R3 Codex handoff line, 78 R2 authority paragraph + "Outside that development scope…".
- reviewer: 43 R5 product-source read-only + helper runtime, 87 R4 authority paragraph + "Do not push, deploy, operate unrelated services, or change host configuration from a review task."

2.3 Shared authority agreement and boundary preservation
The 26-word-per-clause authority paragraph appears exactly once in each of the three templates and hashes identically across them (9ab6bfd69ef5a21c27f2d3ac8853f91ddc4692a8d0a1a173c04a1a81d08fc1a1). It carries all four required elements: "without further customer approval" (+ the full enumerated operation list), external-boundary retention (source ownership / operational data / host administration / shared infrastructure / external effects), team coordination without a customer approval round, and the "development operations, not publication or deployment" classification. The Reviewer's deployment ban is retained and is stricter than before ("deploy", not "external deployment"); local test/demo runs are classified as development, not deployment — so no contradicting prohibition remains.
Prototype-only exception: untouched (planner lines 34–37, contiguous grilling→interview load instructions); R7 sits at line 50, outside it, after the design-check block and before step 3 — as the spec requires.

2.4 Manifest, inventory, version
manifest.json: version 2.10.0 (SKILL.md:4 also 2.10.0 → compatible-feature MINOR, equal in both files; candidate skill keeps its own 0.1.0). `files`: 68 entries, sorted (`files == sort`), zero duplicates, every path exists on disk. Revision is inventory-only: `references/test_dev_environment.py` and `skills/dev-environment/SKILL.md` added, `test_devteam_cleanup.py` merely repositioned by the sort. `own_skills` now 9 entries, `dev-environment` → targets {"hermes":["planner"]} only, skill_path + transport {"SKILL.md":"SKILL.md"}, license_path null, notice_path NOTICE.md, origin_ref to the new anchor. Not present in upstream_components (correct: owned, no upstream).

2.5 Source/legal/README/pointer consistency
- upstream-sources.md:17 adds the matrix row with `<a id="own-dev-environment">` and a resolving link; lines 33–35 describe complete-tree copy, collision/loading checks without running construction, and the Planner-only boundary. The origin_ref anchor resolves.
- NOTICE.md:29 adds the owned-component row: author, MIT of this package, no upstream source, no separate skill legal files (true — the tree contains only SKILL.md), and an explicit "no installation or live-runtime qualification implied".
- README.md:138–145 states the same contracts and explicitly keeps "The Reviewer still cannot repair product code or deploy". No SG1/MTB hosts, paths, credentials or local authoring paths.
- SKILL.md:76 refines the existing first-task offer to name creation/adoption and keeps "do not start it automatically" — optional offer, no automatic execution.
- references/development-verification.md: new paragraph names the new test surface and states the fixture/native boundary.

2.6 Tests: actual evidence, not just green output
- references/test_dev_environment.py (6 tests): exact package inventory ({SKILL.md} only), manifest membership/targets/transport, frontmatter fields, description length ≤ 60, portability regex over the body rejecting /home/, /workspace/, MTB, SG1 and the host-local authoring checker, plus local_links. Then targeted clause-level contracts for absent/usable/incomplete, the two-guide + root-pointer audience separation, integrated DB + PostgreSQL branch workflow (collision handling, template clone, source-session check, target verification before writes, create-once/reuse, scoped reset, baseline preservation), runtime operations vs source/external boundaries, and demo handoff honesty. These are static text contracts — the file's docstring says so, and the plan labels them that way.
- references/test_render_reasoning.py (3 new tests + extended equipment matrix): I confirmed the slice markers are unique in the rendered text ("7. Create small implementation tickets", "8. Create dependent", "5. Provide Codex", "6. Read", "## Proportional investigation", "## Independent review", "3. Use the workspace"), so the assertions are not passing on empty slices. The agreement test compares the three rendered paragraphs for identity, and also asserts the boundary sentences per role and that no role text mentions HOWTO-human.md.
- references/test_update_team.py (2 new tests): real files and real Git in disposable fixtures (self.initialize/commit/proposal/apply/rollback). Delivered entry set is exactly skills/dev-environment/SKILL.md for role planner, transform copy-v1, target bytes equal to source, absent in coder/reviewer/team-codex homes; a local prefix edit survives an update (local-adaptation preservation); the collision case raises ValueError 'Text conflicts' and leaves both the unrelated local file and installation.json byte-unchanged; after resolution, rollback reports the addition retained and restores installation.json. These are fixture-level updater proofs, not live profile rollout — correctly scoped.
- The intermediate renderer failure in renderer.log (1 failure) was `test_default_equipment_retains_other_roles_and_sdlc` at test_render_reasoning.py:834, an exact-equality set over own_skills. Adding the new expected entry is the legitimate correction for an added skill, not a weakening: planner-only targeting is independently asserted by test_dev_environment.py:30 and the new updater test, and I verified the manifest entry itself.
- Negative control (isolated scratch copy of references/templates/skills/manifest.json/SKILL.md, nothing in the repo touched): mutating "Coordinate disruptive operations with other team users." in the coder template made test_rendered_development_authority_agrees_and_keeps_role_boundaries fail with `AssertionError: 2 != 1` (plus unrelated copy artifacts). The agreement assertion is real, not vacuous.
- Old negative Brownfield single-source assertions: unchanged. test_brownfield_planning.py still contains the assertNotIn block with "Do not infer permission to mutate a resource from permission to inspect it."; only the positive soul_clause line was replaced by the R1 NEU sentence ("For other resources, …"), exactly as the spec's section 5 and the plan required.

2.7 My own reruns (independent, not the logged evidence)
- python3 -B -m unittest discover -s references -p 'test_render_reasoning.py' → Ran 75 tests, OK (0.154 s)
- … -p 'test_dev_environment.py' → Ran 6 tests, OK
- … -p 'test_brownfield_planning.py' → Ran 19 tests, OK
- … -p 'test_triage_recovery.py' -v → Ran 21 tests, OK (skipped=1)
- … -p 'test_*.py' (aggregate, background) → Ran 235 tests in 356.628 s, OK (skipped=1), exit 0 — matches verification.json's 235/350.29 s/OK(skipped=1)
- git diff --check → clean
- The single skip is `test_delegation_guard_denial_leaves_synthetic_board_unchanged … skipped 'No delegation fence in this process'` — a pre-existing conditional native-guard skip in an unmodified file, not a suppressed failure of this changeset. A denied/skipped check is missing evidence, and I treat it as such: no claim rests on it.

===============================================================
3. ACCEPTANCE-CRITERIA WALK (A1–A8)
===============================================================
A1 Delivered skill — met (byte-identical; manifest once, Planner-only; source/legal/README agree).
A2 Reachable use — met (R7 invocation after design checks; R8 guide+container requirement inside ticket step 7 and conditional; R3 Codex handoff with guide path and runtime authority; R6 demo access; no HOWTO-human.md reference in any role).
A3 Consistent authority — met (identical paragraph hash; autonomous operations retained; boundaries and Reviewer restrictions intact; prototype exception byte-identical and contiguous).
A4 Database contract — met in the accepted text (integrated Compose DB, template cloning with create-once/reuse, collision handling, target verification before writes, baseline/other-branch preservation, scoped reset, external DB as bounded adoption, third-party services excluded).
A5 Guidance and demonstration — met as contract (two guides, canonical commands, root pointer wording, demo URL + SSH forward, untested-client disclosure, absence adds no blocker).
A6 Delivery/update regression — met (existing mapper; complete bytes; local-rule preservation; collision + rollback).
A7 Verification — met for the package gate (RED→focused-green→renderer-correction→aggregate-green is coherent and independently reproduced; counts/skip recorded; inventory, version equality, links/anchors and diff-check validated).
A8 Independent acceptance — this report.

===============================================================
4. FINDINGS (none blocking)
===============================================================
F1 — references/setup.md:308–314 names delivery recipes only for prototype and diagnosing-bugs; dev-environment rides the matrix row (upstream-sources.md:17) plus the generic step 1 complete-tree copy and step 6 "Compare skill file set and bytes completely with the source". Failure condition: an operator who works recipe-by-recipe instead of matrix-driven skips creating <planner home>/skills/dev-environment/. Consequence: the omission is caught by the step 6 byte/file-set readback (skill absent, never half-installed), so setup cannot silently pass with a missing skill. Nonblocking: the plan explicitly required the existing mapping and no new recipe; noted only for a future setup-doc touch.

F2 — Coverage gap on the optional-offer sentence. SKILL.md:76 is the only place encoding "do not start it automatically" with the dev-environment example, and no reference test asserts it. Failure condition: a later edit that drops "do not start it automatically", or that turns the offer into automatic execution, passes the whole suite. Consequence: documentation/behaviour drift risk in the handoff promise; the binding runtime behaviour lives in role SOULs, which are covered. Nonblocking.

F3 — NOTICE.md:29 and manifest.json:188 (origin_ref) are not machine-validated. No test in the package ties notice/origin_ref to an owned skill (pre-existing convention, unchanged by this diff). I verified both manually: the row is accurate (no upstream, no separate legal files) and the anchor exists at upstream-sources.md:17. Failure condition: a future edit could break the anchor or the legal row without a red test. Nonblocking.

F4 — reviewer.SOUL.md.template:64 keeps the generic "…apply the same model/provider, reasoning, access, approval, and read-only limits to this pass". Read against the combined authority — R5 (line 43) scopes read-only to product sources and explicitly allows helpers to operate assigned test runtimes within the reviewer's authority, coordinated through the reviewer; R4 (line 87) establishes the standing assigned-development scope; line 64 applies the same limits as the main review, i.e. the same scope — the net effect grants nothing new, and the only deviating reading is the more restrictive one. This is exactly the vocabulary note recorded as nonblocking in REVIEW_2.9.1_Dev-Environment_v2.md §4, and the changeset correctly did not silently redefine it. Nonblocking, as previously ruled.

F5 (reviewed and accepted, not a finding) — R5 increases helper permission from pure read-only to "may operate assigned test runtimes". It is byte-identical to the approved spec NEU, bounded by "within your development authority" and "coordinate shared runtime changes through you", and helpers still may not implement, issue Kanban transitions, or enlarge scope or permissions. It does not introduce a customer approval loop inside the assigned disposable development scope nor broaden product-source or external authority.

===============================================================
5. EVIDENCE LIMITS (explicit)
===============================================================
- Nothing in this review executed Docker, Compose, PostgreSQL (no template clone, no branch DB, no collision against a real server), no container, no generated team, no live profile rollout/install, no live-agent behaviour. The skill's own acceptance cases (fresh checkout, functional use, reuse, safe adoption, missing input, audience separation, integrated DB, PostgreSQL branches, runtime autonomy, demonstration) remain unexecuted.
- The renderer and package tests prove rendered/static instruction contracts and file/Git-level delivery semantics; they do not prove agent adherence, skill discovery at runtime, usable generated guides, or portability.
- Updater evidence is real files and Git inside disposable fixtures, not an actual existing-team update on a live profile; native discovery/loading was not exercised.
- The frozen logs were inspected, not reproduced wholesale by me: I re-ran the renderer suite, the new contract suite, the brownfield suite, the triage suite and the entire aggregate suite from the working tree, with matching results; I did not re-run red.log's RED state (it is historical evidence of the pre-implementation failures, and its 14 subtest failures are consistent with 11 tests + subtests).
- Consequence for the verdict: no missing evidence blocks package acceptance — the plan explicitly separates package integration and static contracts from runtime qualification, and Mariko claims no runtime evidence. The gaps above block only a later per-project live qualification/readiness claim.

===============================================================
6. VERDICT
===============================================================
APPROVED for the exact frozen working-tree state described in §1. The delivered skill is the approved text byte-for-byte, all eight role replacements are exact and singular with the ALTs removed, the shared authority paragraph is identical across roles and preserves every product-source, operational-data, host/shared and external boundary while keeping the Reviewer's deployment and self-repair bans, the manifest is complete/sorted/Planner-only with equal 2.10.0 versions, delivery and rollback are exercised through the existing mapper with fixture-level collision and local-adaptation proofs, and the old negative Brownfield single-source assertions are untouched. My independent reruns reproduce the logged results (235 tests, OK with the one pre-existing conditional skip). Findings F1–F4 are nonblocking observations for future edits; F5 is reviewed and accepted as approved text.

-----------------------------------------------------------------
Kurzfazit (Deutsch)
-----------------------------------------------------------------
Urteil: APPROVED. Geprüft ist genau der eingefrorene Arbeitsbaum auf HEAD 94ded22 — alle 81 Hashes aus frozen-inputs.json habe ich vor der Prüfung und unmittelbar vor dem Urteil verifiziert, ohne Abweichung; implementation.diff entspricht dem aktuellen git diff (nur fehlender Schlusszeilenumbruch), meine Testläufe haben nichts verändert.

Inhaltlich: Die Kandidaten-Skill ist bytegleich zum freigegebenen Text (024ede71…), alle acht Ersetzungen R1–R8 sind exakt und je einmal vorhanden, die alten Fassungen sind aus den Vorlagen verschwunden, der gemeinsame Befugnis-Absatz ist in allen drei Rollen hashgleich (9ab6bfd6…), die Prototyp-Ausnahme ist unverändert und R7/R8 sitzen an der vorgesehenen Stelle. Manifest: 68 Dateien sortiert und vollständig, dev-environment ausschließlich dem Planner zugewiesen, Version 2.10.0 in SKILL.md und manifest.json gleich, Kandidaten-Version 0.1.0 separat. Updater-Tests arbeiten mit echten Dateien und echtem Git in Wegwerf-Fixtures (Kollision, lokale Anpassung, Rollback), die statischen Renderer-/Skill-Tests sind als statische Verträge deklariert — nicht als Agentenverhalten. Die alten negativen Brownfield-Assertions sind unangetastet, nur die positive Planner-Zeile wurde getauscht.

Eigene Nachläufe: Renderer 75 OK, test_dev_environment 6 OK, Brownfield 19 OK, Triage 21 OK (1 bedingter Skip ohne Delegation-Fence), Gesamtlauf 235 Tests OK (skipped=1) in 356 s, git diff --check sauber. Eine Gegenprobe in einer isolierten Kopie hat bestätigt, dass die Absatz-Gleichheitsprüfung wirklich anschlägt (2 != 1).

Vier nicht blockierende Hinweise: keine benannte Setup-Recipe für die neue Skill (matrixgetriebene Auslieferung greift, Schritt-6-Readback fängt Lücken), die Erstaufgaben-Angebotszeile in SKILL.md hat keine Regressionszusicherung, NOTICE-Zeile und origin_ref sind nur manuell geprüft (bestehende Konvention), und die generische "read-only limits"-Formulierung im High-Risk-Absatz bleibt wie im Vorreview als Vokabelhinweis bestehen — die kombinierte Autorität ist durch R4/R5 eindeutig und eher enger. Docker-, PostgreSQL- und Live-Agenten-Nachweise fehlen weiterhin; das blockiert die Paketabnahme nicht, aber jede spätere Betriebsbereitschafts-Aussage.
