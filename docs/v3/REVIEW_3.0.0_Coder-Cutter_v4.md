# REVIEW — Maker-Plan `PLAN_devteam_v3_codercutter.md`, Runde 4 (Coder-Cutter)

Reviewer: Fujiko (independent, review-only; one-shot run in profile `fujiko`, model `deepseek/deepseek-v4.1-flash-1017`, reasoning high, tools `file,terminal`, read-only, substitution run in her own scratch copy)
Date: 2026-11-23 (CET)
Review object: `docs/v3/PLAN_devteam_v3_codercutter.md`, sha256 `3559cca440309c443ad26ba1600ce084f17a6bd467a59ef201405e19c0d475fd`
Frozen state: HEAD `b5ced6be25d34350830f55f1b181e0e262cde0d1`; `git status --short` = `?? docs/v3/` at handover and before the verdict
CAC criterion: the three CAC references read in full again

**VERDICT: APPROVED WITH FINDINGS** — implementation may begin. Role design, §9.2, §9.3, the measurements and the W4 test rule are approved; no finding touches a design decision, an authority, a permission or a safety boundary. Five remaining findings are ledger accuracy.

---

## Reviewer report (verbatim)

EXACT REVIEWED STATE

  At handover (2026-11-23, profile fujiko, read-only)
    repository      /home/mariko/projects/generic-devteam
    HEAD            b5ced6be25d34350830f55f1b181e0e262cde0d1 (branch develop)
    git status      ?? docs/v3/
    plan sha256     3559cca440309c443ad26ba1600ce084f17a6bd467a59ef201405e19c0d475fd
    implemented?    no: git diff --stat empty; manifest.json 2.14.4; no skills/demo-handover;
                    no demo path in manifest.files
    scratch copy    /home/mariko/.hermes/profiles/fujiko/cache/scratch/r4 (copy only;
                    substitution committed there, never in the checkout)

  Immediately before the verdict (re-run)
    HEAD            b5ced6be25d34350830f55f1b181e0e262cde0d1
    git status      ?? docs/v3/
    plan sha256     3559cca440309c443ad26ba1600ce084f17a6bd467a59ef201405e19c0d475fd
    git diff --stat empty

  My measurements (§9.2 extracted from plan lines 279-347, sha256 af198f0c…7808)
    §9.2 unrendered                     8,436 B / 69 lines
    §9.2 rendered (fixture bindings)    8,247 B / 69 lines
    2.14.4 unrendered                  19,652 B / 140 lines
    2.14.4 rendered                    19,463 B / 140 lines
    placeholders                        14, set-equal to manifest.role_templates.coder.render_fields
    §9.4 columns                        all 16 cells reproduce; sums to 19,652 and 8,436 exactly
    suites at HEAD                      test_render_reasoning 85 tests OK
    suites with §9.2 substituted        test_render_reasoning 36 failures + 2 errors over exactly
                                        25 methods; test_build_evidence 1; test_diagnosing_bugs 1
    the two invocation tests            both ok against §9.2 (fences found by r"   ```sh", executed)

VERDICT: APPROVED WITH FINDINGS

The role design, the §9.2 and §9.3 texts, the measurements and the W4 test rule are approved; implementation may begin. §9.5's site ledger is still short by seven test assertions that the plan's own documentation edits break, and §9.5/§4 carry three inaccurate sentences. No finding requires a design decision, a change to §9.2/§9.3, or any authority, permission or safety boundary.

ROUND 3 FINDINGS

  F1  RESOLVED for its named scope — residual of the same class filed as NEW-1.
      The measured failing set with §9.2 substituted is exactly 25 methods in
      test_render_reasoning.py; the §9.5 table has 25 rows and the two sets are
      identical (scripted set comparison: no row without a failure, no failure without
      a row). Closure numbers reproduce exactly: 36 failures + 2 errors, 1, 1; the same
      copy with the 2.14.4 template is 85 tests OK. The formerly unnamed eighteen methods
      and the four readback sites now have rows, the two invocation methods pass and are
      correctly absent from the table, and the five-file phrase loop is named at :1098–:1107.
      Not resolved: seven assertions that break only when the §9.5 documentation edits are
      applied are still unnamed (NEW-1), and the transform sentence does not fit three of the
      five code-analysis.md lines (NEW-2).

  F2  RESOLVED
      §9.6:458 now reads "`--sandbox danger-full-access` in the run fence and
      `-c sandbox_mode='\"danger-full-access\"'` in the resume fence". Measured in the §9.2
      render: 1 and 1; the old conjunct "exec --sandbox danger-full-access" is absent from
      both renders. Check now passes against the text it guards.

  F3  RESOLVED
      §9.2:283 "Codex implements; only Codex CLI writes productive project code." and
      §9.2:329 "…native failure-loop guards. Tool and system prohibitions remain binding."
      are the 2.14.4 sentences (baseline by string equality). test_render_reasoning.py:103/:105
      therefore pass untouched — the method is not among the 25 failures. §9.5:436 still says
      ":82–:105 needs re-pointing only", which is now a no-op; see NEW-3.

  F4  RESOLVED
      The five assertions live at :302–:306 inside test_voltagent_specialists_…
      (:299–:307). §9.5:434 now reads "`:302`–`:306`… wait: "`:299`–`:306`: re-point the
      reasoning and caps assertions, delete the catalogue pair. `:309`–`:329` test the pinned
      package and stay unchanged". Measured: :302 "Keep the configured model and provider.",
      :305 caps reasoning, :306 customer financial/resource caps (re-point targets exist at
      §9.2:299 and §9.2:329); :303/:304 the specialist-settings pair; :309–:329 are the
      pinned-package and update tests, green today. The row's range ends one line before the
      method's last assertion (:307 assertNotIn), which is harmless.

  F5  RESOLVED
      Recomputed with one method (section including heading, split at top-level '#'):
      64/1,268/8,382/3,635/2,378/2,288/1,489/148 = 19,652; 68/926/871/2,104/2,609/579/1,131/148
      = 8,436. Every cell matches §9.4:386–394, and both columns sum exactly to their totals.
      8,247/19,463 = 42.4 %, i.e. 57.6 % below baseline. "1.0 KB larger than the draft" is
      consistent with the 7,248 B prior render recorded in REVIEW_3.0.0_Coder-Cutter_v3.md;
      the prior draft itself is not in the repository, so that single figure is consistent,
      not independently re-derivable.

  F6  RESOLVED
      §9.2:330 "…stays in place: have Codex verify in a clean detached worktree at the
      candidate commit, and never delete, rewrite or mask it." The Coder-side verification
      verb is gone; the protection half is intact.

  F7  RESOLVED
      §9.2:325 "…then `kanban_block(kind=\"needs_input\", reason=...)`; keep card and
      assignment, verify the recipient, and confirm the existing subscription wakes
      `{{PLANNER_PROFILE}}`." Profile identifier restored (the wake mechanism is keyed by it;
      test_update_team.py:284 renders `fixture-planner`), comma splice resolved into three
      clauses.

  F8  RESOLVED
      §9.5:443 maps each string: four diagnosis sentences at :198–:200 (:199 carries two),
      :201 → one-session bullet, :202–:203 → delegation brief, :204 → handoff wording,
      :205 → caps sentence. All five targets exist in §9.2 with the stated content
      (:300, :295, :335, :329).

THE IDEA

  Direction 1 — no implementer duty survives in §9.2. No finding.

    Diff reading / judging code     ABSENT. :284 "Implementation choice is Codex's: no second
                                    technical brief, no diff review, no test replay.";
                                    :340 "Verify commit existence and identity, not its content."
    Running or choosing tests       ABSENT. :284 "no test replay"; :295 requires only Codex's
                                    reported result; no test-strategy or test-selection rule
                                    anywhere in the text.
    Analysis / source scan /
    consumer enumeration            ABSENT. :291 "No second ticket fetch, no plan or source scan
                                    of your own."; :292 "Establish operational facts only";
                                    :342 "ask Codex for the code fact instead of investigating".
    Harness construction or repair  ABSENT. :319 "a failing harness is a setup defect, so direct
                                    Codex to fix its cause once"; the staging ladder and the
                                    synthetic-harness rules are gone (cursorise: 0 hits for
                                    "harness repair").
    Test strategy                   ABSENT. No formulation of a test plan appears; §1:24 and
                                    §3.1:87 assign it to Codex and §9.2 does not restate it.
    Commit content                  ABSENT. :340 identity/existence only.
    Independent verification        ABSENT. :284 "You approve neither your own implementation
                                    nor its completion."; :335 hands to the Reviewer.
    A second brief                  ABSENT. :284 "no second technical brief"; :294 "Pass the
                                    original task with its binding references and limits… brief
                                    under 4 KB, pointing to the exact plan revision."

  Direction 2 — every coordinator duty is present. No finding.

    Delegation               :291 card body and when to read comments; :292 operational facts;
                             :293 branch existence at the named start commit and checkout, return
                             to {{PLANER_NAME}} on failure; :294 original task, binding
                             references, limits, agent-guide path, 4 KB brief; :295 compact result.
    Session continuity       :300 one session per ticket, `thread_id` from `thread.started`,
                             resume for corrections/failures/Reviewer returns, new session only
                             with a recorded continuity failure, no concurrent turns; :299 model
                             and reasoning limits; :317 literal substitution and RESULT_FILE;
                             :318 worker guard.
    Blocker routing          :323 question back to Codex; :324 decision inside authority;
                             :325 missing requirement/scope/permission/customer choice/contract →
                             `kanban_comment` + `kanban_block(kind="needs_input")` + subscription
                             wake + reread after resumption; :326 capability; :327 transient with
                             one TIMER request; :330 unrelated work to the Planner, no cards.
    Decisions in authority   :285 "Decide only what Codex cannot: accepted goal and contracts,
                             interoperability, security, privacy, data integrity, permissions
                             and cost. Several small decisions MUST NOT accumulate into an
                             unapproved redesign."; :324 record on card, resume Codex, decision
                             stands for the round, reasons and scope for declined findings.
    Kanban + review handoff  :335 `kanban_request_review(summary=..., reviewer="{{REVIEWER_PROFILE}}")`,
                             never `kanban_complete`, check `ok: true` and `status: "review"`,
                             correct or escalate, no project changes until native return;
                             :336 labelled summary with actor and revision.
    Operational authority    :328 development/demo runtime authority; :329 no ticket-implied
                             approval outside it, caps and guards, prohibitions binding; :330
                             local-input protection; :331 demo card → `demo-handover` skill and
                             password via environment variable only; :287 command grants are not
                             the Coder's to change.

NEW FINDINGS

  1. MAJOR — §9.5 still leaves seven test assertions undispositioned that the plan's own
     documentation edits break; following the ledger produces a red suite in two files.
     Location: docs/v3/PLAN_devteam_v3_codercutter.md:436–447
     Text: ":966–:985, :1082–:1095 and the five-file phrase loop at :1098–:1107 follow the
     manifest and `upstream-sources.md` rows." and "`references/code-analysis.md:3`, `:30`,
     `:38`, `:94`, `:127`; … The \"Planner, Coder, Reviewer and Team-Codex\" phrase becomes two
     roles plus Team-Codex…"
     Measured (repository, HEAD):
       test_render_reasoning.py:1081  "| Planner, Coder and Reviewer | `graphify/skill-claw.md`"
                                      — outside :1082–:1095; breaks when code-analysis.md:30
                                      becomes two roles
       test_render_reasoning.py:1097  row.endswith("| Planner, Coder, Reviewer and Team-Codex |")
                                      for codebase-memory/graphify in upstream-sources.md —
                                      outside :1082–:1095 and outside :1098–:1107
       test_render_reasoning.py:1220  "…graphify` skill in Planner, Coder, Reviewer and
                                      Team-Codex." — unnamed; breaks with code-analysis.md:38
       test_render_reasoning.py:1231  "…inspect Planner, Coder, Reviewer and Team-Codex…"
                                      — unnamed; breaks with update.md:138
       test_update_team.py:327        "Check the `kanban_request_review` response" — §9.2:335
                                      says "Check `ok: true` and `status: \"review\"`"; outside
                                      :282–:285, :410–:427, :1004–:1007
       test_update_team.py:543        "The existing subscription wakes `fixture-planner` for
                                      customer coordination." — §9.2:325 drops "for customer
                                      coordination"; unnamed
       test_update_team.py:1010       "$build-evidence" in the installed Coder SOUL — unnamed;
                                      breaks with §9.2 and the manifest retarget
     Measured, not asserted: on the scratch copy with §9.2 committed, test_update_team
     reports failures at :327, :421, :423, :543, :1010 (:421/:423 are covered by the
     :410–:427 row); the four test_render_reasoning lines are pinned to strings that
     §9.5:446/:447 changes and are green only while those documents are untouched.
     Replacement: extend §9.5:436 to "`:1081`–`:1097` (code-analysis.md and upstream-sources.md
     rows), `:1220`, `:1231` (code-analysis.md:38, update.md:138)" and extend §9.5:444 to
     ":282–:285, :327, :410–:427, :543, :1004–:1010".
     Reason: §5:228 and §8:2 require the suites to report zero Coder-related failures, and
     §9.5 presents itself as the complete list of "follow-on changes these texts force". The
     closure criterion only covers suites measured with §9.2 alone; it never measures the
     state after the documentation edits, which is where these seven break.

  2. MINOR — §9.5:446's transform does not describe three of the five lines it names.
     Location: plan:446
     Text: "The \"Planner, Coder, Reviewer and Team-Codex\" phrase becomes two roles plus
     Team-Codex where it names the analysis integration"
     Measured: code-analysis.md:30 and :127 read "| Planner, Coder and Reviewer | …" and :94
     reads "# Run for Planner, Coder and Reviewer with their respective ROLE_HOME." — the
     named four-role phrase does not occur there, and Team-Codex has its own rows at :31/:128,
     so "plus Team-Codex" does not apply. The correct result for those three is "Planner and
     Reviewer".
     Replacement: "…:3 and :38 lose only Coder (two roles plus Team-Codex); :30, :94 and :127
     become \"Planner and Reviewer\"."
     Reason: an implementer who searches for the named phrase finds it at neither :30, :94 nor
     :127 and can leave three Coder analysis assignments in place; the tests that pin those
     strings (:1081/:1097, NEW-1) stay green while the document still lists the Coder as an
     analysis consumer, contrary to §2.2:69 and §2.2:77. Mitigating: W2:139 independently
     forbids Coder-side structural analysis, so the risk of a silent miss is reduced.

  3. MINOR — §9.5:436 prescribes a test edit that is no longer needed.
     Location: plan:436
     Text: "`:82`–`:105` needs re-pointing only (`:103` to \"only Codex CLI writes productive
     project code\", `:105` to the restored sentence) because the Coder text now carries both"
     Measured: both strings are present verbatim (§9.2:283, §9.2:329) and
     test_rendered_development_authority_agrees_and_keeps_role_boundaries passes untouched
     (it is not among the 25 failures). No edit to :103/:105 is required.
     Replacement: "`:82`–`:105` unchanged: both pins are satisfied verbatim by §9.2:283 and
     §9.2:329."
     Reason: F3 was closed by restoring the sentences, not by re-pointing the test; leaving
     "needs re-pointing" in the ledger invites an unnecessary edit to a green assertion and
     misstates the closed state.

  4. MINOR — five documentation sites that state a removed Coder duty are named only at file
     level.
     Location: references/update.md:86, references/native-workflow.md:40,
     references/upstream-sources.md:14, references/development-verification.md:22, README.md:131
     Text: "…dependent Coder call clause…"; "verify the Coder's explicit diagnosis call";
     "| build-evidence | Coder, Reviewer and Team-Codex |"; "…delivery/legal and explicit Coder
     invocation."; "Coder explicitly invokes it and validates original evidence…"
     Measured: all five still describe duties §9.1/§9.2 remove. §9.5 names none of them
     (update.md only at :138, native-workflow.md only at :28/:52, upstream-sources.md only at
     :103 and the analysis rows). None is test-pinned, so nothing fails; the drift is silent.
     Replacement: one row: "`update.md:86`, `native-workflow.md:40`, `upstream-sources.md:14`,
     `development-verification.md:22`, `README.md:131` | drop the Coder half of each
     assignment and of the diagnosis-invocation wording."
     Reason: §2.2:77 requires a removed Coder assignment to cease being discoverable, and
     §2.2:75 mandates the bounded mechanical reconciliation; the four documents are otherwise
     only covered by the general file-level instruction in W2/W4.

  5. MINOR — W6's rationale names a password rule the delivered text does not contain.
     Location: plan:166
     Text: "The copy is byte-identical: no render field, so the password rule names the private
     team record."
     Measured: §9.3:370–375 says the password "stays in the role instructions; this skill
     carries the runtime procedure", and §9.2:331 says it is "supplied only through the
     environment variable the script documents". Neither text names a private team record;
     only references/native-workflow.md:28 does.
     Replacement: "The copy is byte-identical: no render field is needed, because the password
     sentence stays in the SOUL and the skill carries only the procedure."
     Reason: CAC — the sentence asserts something about the delivered texts that is not true
     of them (cac-notation.md §1 "Keep identifiers … exact"; contract:10). An implementer may
     add a team-record sentence to §9.3, which would break the byte-identical copy claim.

  Explicit "no finding" lines
    C, direction 1 and 2   no finding; see THE IDEA for clause references.
    D, the 25-method table  no finding. Every named method exists, and the row's class letter
                            and note match what the method asserts in all 25 cases I opened
                            (:410–:424, :426–:438, :457–:498, :553–:633, :659–:696, :742–:789,
                            :299–:329).
    D, named reference and manifest sites  no finding for §9.5:442, :443, :445, :448, :449,
                            :450, :451, :452. Verified in the repository: test_build_evidence.py:70–:72,
                            test_diagnosing_bugs.py:189–:210, verification.md:31/:33,
                            setup.md:230/:257/:260, native-workflow.md:28, manifest.json:201/:252,
                            manifest target values (plan-versioning-semver [planner, coder],
                            build-evidence [coder, reviewer] + codex, screenshot-to-code
                            [planner, coder] + codex), no demo entry in manifest.files today.
    E, §9.2 obligation strength and literals  no finding. MUST/SHOULD/MAY preserved; the
                            literals I checked are byte-exact against 2.14.4 or against the
                            test's own expectation: `kanban_block(kind="needs_input", reason=...)`,
                            `kind="capability"`, `kind="transient"`,
                            `kanban_request_review(summary=..., reviewer="{{REVIEWER_PROFILE}}")`,
                            `thread.started`, `PONYTAIL_DEFAULT_MODE=full`,
                            `-c model_reasoning_effort='\"REASONING\"'`,
                            `-c sandbox_mode='\"danger-full-access\"'`, `demo.sh retire`,
                            `demo.sh user`. Observation, not a finding: §9.2:325 reduces
                            `kanban_comment(task_id=..., body=...)` to the tool name plus the
                            required labels; the argument names are recoverable from the tool
                            and the labels `Question:`/`Why it matters:` are exact, and the
                            test that pins the call form (test_render_reasoning.py:483) is
                            re-pointed by the §9.5 row for that method.
    E, §9.3   no finding. Frontmatter shape matches skills/build-evidence/SKILL.md; the
                            lifecycle, teardown and creation sentences are the 2.14.4 literals
                            (baseline coder.SOUL.md.template:78) with only the sentence-initial
                            capital changed; password and "never as an argument" correctly
                            remain in the SOUL; both `demo.sh` verbs present.
    E, audience rule   no finding. §9.2 and §9.3 are team-internal technical English; no
                            human-facing text is compressed.
    E, duplication   no finding. "You approve neither your own implementation nor its
                            completion" (:284) and "never `kanban_complete` on your own
                            implementation" (:335) are a boundary and its transition verb, both
                            separately pinned by tests; not duplicated meaning.

VERIFIED CLAIMS

  - HEAD, plan sha256 and `git status --short` identical at handover and before the verdict;
    `git diff --stat` empty; nothing implemented.
  - §9.2 extracted byte-exactly from the plan's four-backtick block: 8,436 B / 69 lines;
    rendered 8,247 B / 69 lines; baseline 19,652 B / 140 unrendered and 19,463 B / 140 rendered
    with the same fixture values (default "medium", maximum "high"). §9.2:269, §4/W1:135 and
    §5:197 all agree with these values.
  - Exactly 14 placeholders and no residual `{{` in the render; the set is equal to
    manifest.role_templates.coder.render_fields, so the manifest field list is unchanged.
  - §9.4 reproduces cell by cell on one counting method; both columns sum to their totals.
  - §9.5's closure criterion reproduces exactly: 36 failures + 2 errors over 25 methods,
    1 in test_build_evidence.py, 1 in test_diagnosing_bugs.py; the same copy with the 2.14.4
    template is 85 tests OK; the 25 table rows are set-equal to the 25 measured failing methods.
  - Both invocation tests pass with §9.2 in place and genuinely execute the rendered recipes
    (r"   ```sh" finds two fences; argv compared; stdin compared).
  - §9.6's eleven negative needles: 1 occurrence in the 2.14.4 render, 0 in the §9.2 render,
    all eleven. Positive checks: "The customer owns product scope" 1; run-fence sandbox flag 1;
    resume-fence sandbox mode 1; `background=true`, `pty=true`, `workdir`, `thread.started`,
    "the event stream is not the result" each ≥1; capability and transient in separate bullets;
    `{{DEMO_PASSWORD}}` exactly once; `demo-handover` pointer exactly once.
  - The rendered development-authority bullet is string-identical to
    planner.SOUL.md.template:12 and occurs once, so test_render_reasoning.py:100 holds.
  - §9.1's byte statements: `Codex controls and risk` 3,635 B, `Git, evidence, and memory`
    2,288 B, `Communication` 1,489 B, demo step 991 B ("~1,000 B").
  - Reading discipline: the plan and the repository were read first; §9.7–§9.9's tables were
    consulted afterwards as pointers only and were not used as proof. The checkout was not
    written to; all substitution work happened in the scratch copy.

OPEN QUESTIONS

  - Whether NEW-1's seven assertions should be added to §9.5 as rows or covered by widening the
    closure criterion to "after the documentation edits, the three suites plus
    test_update_team.py report zero Coder-related failures". The plan needs one of the two, so
    the criterion measures the state it actually claims.
  - §9.4:396 says "Max approved 3.5–4 KB" while the header and §4/W1 quote a superseded
    "<= 5 KB" aim. The repository cannot settle which target Max set; the deviation argument
    is unaffected.
  - Whether `ponytail` with an empty `targets.hermes` is a valid manifest state or should leave
    the Hermes matrix entirely: no test validates emptiness (unchanged from rounds 2–3).
  - Whether Codex selecting `plan-versioning-semver` from its description alone suffices, or
    the explicit cue routed through team-codex-AGENTS.md is required (unchanged).

---
Reviewed by Fujiko, round 4, read-only.

---

## Marikos Umsetzung (2026-11-23, nach dem Urteil)

| Befund | Umsetzung im Plan | Stand |
|---|---|---|
| NEW-1 sieben Assertions nach den Doku-Edits | §9.5-Bereiche auf `:1081`–`:1097`, `:1220`, `:1231` und `test_update_team.py:327`, `:543`, `:1004`–`:1010` erweitert; Abschlusskriterium ausdrücklich zweimal zu messen (mit §9.2 allein und nach den Doku-Edits) | korrigiert |
| NEW-2 Phrasen-Transformation passte nicht auf drei Zeilen | Zeile aufgeteilt: `:3`/`:38` behalten die Team-Codex-Hälfte, `:30`/`:94`/`:127` werden zwei Rollen | korrigiert |
| NEW-3 `:82`–`:105` verlangte eine überflüssige Editierung | Zeile auf „unchanged" gestellt | korrigiert |
| NEW-4 fünf Doku-Stellen ohne Zeilenzeile | neue Tabellenzeile mit den fünf Stellen | korrigiert |
| NEW-5 W6-Begründung nannte eine Passwortregel, die der Text nicht hat | auf den tatsächlichen Grund umgestellt (kein Renderfeld nötig) | korrigiert |

Damit ist der Plan umsetzungsreif; die Umsetzung (W1–W6) ist noch nicht begonnen, der Arbeitsbaum ist unverändert.
