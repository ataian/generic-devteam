# REVIEW — Maker-Plan `PLAN_devteam_v3_codercutter.md`, Runde 3 (Coder-Cutter)

Reviewer: Fujiko (independent, review-only; one-shot run in profile `fujiko`, model `deepseek/deepseek-v4.1-flash-1017`, reasoning high, tools `file,terminal`, read-only)
Date: 2026-11-23 (CET)
Review object: `docs/v3/PLAN_devteam_v3_codercutter.md`, sha256 `9df2e3658ed779b00822caa7a8da6ef7f31f823cd167fe1f4d5eb2cb6b914018`
Frozen state: HEAD `b5ced6be25d34350830f55f1b181e0e262cde0d1`; `git status --short` = `?? docs/v3/`
CAC criterion: the three CAC references read in full again
Owner's yardstick for this round: not the byte size, but that the Coder stays a coordinator

**VERDICT: CHANGES REQUIRED** — all thirteen round-2 findings resolved; the role design and the Coder-owned half confirmed complete. Remaining: §9.5 still missed eighteen test methods and four readback sites, one §9.6 needle, one wrong table row, and four documentation-level defects. No part of the design needed to change.

---

## Reviewer report (verbatim)

EXACT REVIEWED STATE

  At handover
    repository      /home/mariko/projects/generic-devteam
    HEAD            b5ced6be25d34350830f55f1b181e0e262cde0d1 (branch develop)
    git status      ?? docs/v3/
    plan sha256     9df2e3658ed779b00822caa7a8da6ef7f31f823cd167fe1f4d5eb2cb6b914018
    round-2 sha256  504bde04e1a2902b581026993132c36cfc3b1b6ac14cae80e00f27344180aafe
    implemented?    no: git diff --stat empty; manifest.json version 2.14.4; no
                    skills/demo-handover, no demo entry in manifest.files

  Immediately before this verdict (re-run)
    HEAD            b5ced6be25d34350830f55f1b181e0e262cde0d1
    git status      ?? docs/v3/
    plan sha256     9df2e3658ed779b00822caa7a8da6ef7f31f823cd167fe1f4d5eb2cb6b914018
    round-2 sha256  504bde04e1a2902b581026993132c36cfc3b1b6ac14cae80e00f27344180aafe
    git diff --stat empty

  My measurements (render_role, role "coder", fixture bindings of
  test_render_reasoning.py:58-73, default "medium" / maximum "high";
  §9.2 extracted in memory from plan lines 277-340, no file written)

    baseline coder.SOUL.md.template   19,652 B / 140 lines (wc -l)
    §9.2 unrendered                    8,297 B / 64 lines
    §9.2 rendered                      8,107 B / 64 lines (64 newlines, ends with \n)
    14 placeholders, identical to manifest.role_templates.coder.render_fields
    rendered ```sh: fence at column 0, bash -n clean
    reference suite at HEAD: 85 tests, OK
    reference suite with §9.2 substituted for the coder template: 38 fail/error,
    of which 25 distinct failing methods are coder-related

VERDICT: CHANGES REQUIRED

  The role design is right and the thirteen round-2 findings are genuinely closed.
  What is not closed is the consequence contract the last round demanded: §9.5 still
  leaves eighteen deterministic renderer test methods and four reference readback
  sites undispositioned, two of its rows prescribe the wrong action, and one §9.6
  positive check cannot pass against either render. §5:228 ("tests pass") and §9.5
  ("the changes these texts force") therefore still contradict each other. All of it
  is documentation work; no part of the design needs to change.

ROUND 2 FINDINGS

  N1  RESOLVED
      §5:198 now reads "`demo-handover` is the only Coder surface carrying the runtime
      procedure ... Planner and Reviewer keep their own condensed clauses unchanged,
      as §7 requires." I re-read planner.SOUL.md.template:74-75 and
      reviewer.SOUL.md.template:85: both keep their demo clauses and are untouched by
      the plan. The row is now satisfiable without breaking a non-goal.

  N2  RESOLVED as scoped (its eight sites are now rows), and the residual incompleteness
      is filed separately as F1, because it is a different defect: not a missing row for
      a site the finding named, but eighteen further sites the plan never looked at.
      Verified present as rows: test_diagnosing_bugs.py:189-210 (§9.5:413),
      test_render_reasoning.py:186-200 (:403), :205-215 (:404), :294-305 (:405),
      :307-318 (:406), test_update_team.py:282-285 (:409), :1004-1007 (:411),
      test_build_evidence.py:71-72 (:412). Every one of these line ranges exists and
      contains what the row says it contains, except :307-318 (F4).

  N3  RESOLVED
      §9.6:421 "each of these strings occurs once in the 2.14.4 render and zero times in
      the 3.0.0 render". Measured on both renders: "Inspect the actual diff" 1/0,
      "build-evidence" 1/0, "$diagnosing-bugs" 1/0, "six VoltAgent" 1/0,
      "Maintain the project changelog" 1/0, "analysis integration" 1/0,
      "consumer per changed symbol" 1/0, "harness repair" 1/0, "Hindsight bank" 1/0,
      "Stage only" 1/0, "a demonstration runtime is not permanent" 1/0. Direction and
      all eleven values are correct.

  N4  RESOLVED
      §9.1:266 names the receiving surface ("become Team-Codex duties in
      `templates/team-codex-AGENTS.md`") and §9.5:398 adds the `## Skills` block with
      "the two reassigned duties from §9.1 verbatim". The quoted texts at §9.1:266 are
      the 2.14.4 sentences (baseline:116-117) with their Coder-specific trailing clauses
      dropped, which is correct for a reassignment.

  N5  RESOLVED
      §9.2:312: "a failing harness is a setup defect, so direct Codex to fix its cause
      once. After two rounds of harness-only findings, `kanban_block(kind=\"capability\",
      reason=...)` and record the defect, the command and the smallest next step."
      The actor is Codex and the block verb is named. Consistent with §2.1:48, §3.1:87.

  N6  RESOLVED
      §9.2:292: "... including the project agent-guide path when Codex needs the
      development environment; brief under 4 KB, pointing to the exact plan revision."
      §9.5:400's disposition (rewrite the test to read the `Delegate` block) is now
      implementable: the test currently errors with IndexError on
      `split("5. Provide Codex")`, which no longer exists.

  N7  RESOLVED
      (a) §9.2:322 "tool and system prohibitions remain binding"; (b) §9.2:322 "Preserve
      explicit customer financial and resource caps, configured limits, provider quotas,
      operational permissions and native failure-loop guards"; (c) §9.2:334 "Actual state
      is the live branch, code and tests; required state is the exact accepted plan
      revision. Memory overrides neither, and a ticket edit alone does not update an
      active worker's baseline."; (d) §9.2:335 "Save role tooling experience under
      `role:coder` and promote only verified durable project facts to `scope:shared`";
      (e) §9.2:297 "... and if both are HIGH, use `{{CODEX_REASONING_MAX}}` ... Higher
      reasoning grants no product authority." Obligation strength is MUST again.
      Note: (a) and (b) are restored in merged, re-cased wording, which breaks their
      old test assertions - see F3.

  N8  RESOLVED
      §9.2:283 "accepted goal and contracts, interoperability, security, privacy, data
      integrity, permissions and cost" - same set as §3.2:96, "contracts" appears once.

  N9  RESOLVED
      The §9.2:321 bullet is byte-identical to the rendered planner:12 line. Verified by
      string identity of the rendered bullet (present exactly once in the coder render),
      and test_render_reasoning.py:100's `len(set(paragraphs)) == 1` therefore holds.

  N10 RESOLVED
      §9.5:397 now states "`ponytail.targets.hermes` becomes empty" and
      "`codebase-memory` and `graphify` `[planner, coder, reviewer]` ... Remove `coder`
      everywhere per §2.2"; §9.5:415 covers upstream-sources.md:103, which I confirmed
      still reads "Hermes Coder and Team-Codex" for ponytail.

  N11 RESOLVED
      Measured 8,107 B and 64 lines, by splitlines and by newline count, against a
      140-line baseline counted the same way. §9.2:270, §4/W1:135 and §5:197 all say 64.

  N12 RESOLVED
      §9.3:368 "Create the demonstration user via `demo.sh user`, with the password
      supplied only through the environment variable the script documents." Literal
      restored; the password value/channel sentence stays in the SOUL (§9.2:324).

  N13 RESOLVED
      §9.5:398 "Retitle to `# Team-Codex instructions`; add a `## Skills` block ...
      `references/integrations.md:118` re-derives the payload comparison from the
      template, not from a stored fixture." I read integrations.md:118: it compares the
      payload to "the selected CLI's rendering of the expected ordered layers", i.e.
      template-derived, so the note is accurate.

THE IDEA

  Direction 1 - does any implementer duty remain in §9.2? One, and it is narrow.

    Reading/judging the diff          ABSENT. §9.2:333 "Verify commit existence and
                                      identity, not its content."; §9.2:284 "no diff
                                      review".
    Running or choosing tests         ABSENT as a duty. §9.2:284 "no test replay";
                                      :293 requires only Codex's reported result.
    Analysis / consumer enumeration   ABSENT. §9.2:290 "Establish operational facts
                                      only"; :335 "ask Codex for the code fact instead
                                      of investigating"; §9.6 confirms "consumer per
                                      changed symbol" and "analysis integration" are 0.
    Harness repair or construction    ABSENT. §9.2:312 "direct Codex to fix its cause
                                      once"; the staging ladder is gone.
    Test strategy                     ABSENT. Belongs to Codex per §1:24 and §3.1:87.
    Commit content decisions          ABSENT. §9.2:333 forbids judging content; Codex
                                      commits (§1:24).
    Independent verification          ABSENT. §9.2:282 "You approve neither your own
                                      implementation nor its completion"; :328 hands to
                                      the Reviewer.
    A second technical brief          ABSENT. §9.2:284 "no second technical brief";
                                      :292 passes "the original task with its binding
                                      references and limits ... brief under 4 KB".
    Residual: §9.2:323 "A local input the project's development entrypoint rejects stays
    in place: verify in a clean detached worktree at the candidate commit" keeps a
    Coder-side verification verb with no Codex handoff. Filed as F6 (MINOR).
    Weaker instance, not filed separately: §9.2:321 "Before the first build, test or run,
    read the project agent guide and use its commands" is the shared operational
    authority (byte-identical to planner:12 by test), and §1:29/§3.2:100 already qualify
    it as "never ... a second verification phase". The SOUL carries no such qualifier,
    but it is the demo/dev-runtime permission, not a verification duty.

  Direction 2 - does the Coder still own what only it can do? Yes, all of it.

    Delegation               :289 card body and when to read comments; :290 operational
                             facts; :291 branch existence/checkout; :292 original task,
                             references, limits, agent-guide path, 4 KB brief.
    Session continuity       :298 one session per ticket, thread_id, resume, no concurrent
                             turns; :310 literal substitution and RESULT_FILE.
    Blocker routing          :316 question to Codex; :316-320 missing input -> comment/
                             block/subscription; :319 capability; :320 transient + TIMER.
    Decisions in authority   :283 decision set; :317 record on card, decision stands for
                             the round, reasons and scope for declined findings.
    Kanban + review handoff  :328 `kanban_request_review`, `ok: true`/`status: "review"`,
                             no `kanban_complete`, no project changes pending return;
                             :329 labeled summary with actor and revision.
    Operational authority    :321 development/demo runtime; :322 outside that scope no
                             ticket-implied approval, caps and guards; :323 local input
                             protection, no cards of its own.
    Nothing is missing on this side. The coordination half of the role is complete.

NEW FINDINGS

  F1  MAJOR - §9.5 consequence list is still incomplete by eighteen test methods and four
      readback sites; an implementer following it produces a red suite.
      Location: docs/v3/PLAN_devteam_v3_codercutter.md:394-417 (§9.5 table)
      Evidence (measured, not asserted): substituting §9.2 for the coder template and
      running references/test_render_reasoning.py in memory leaves 25 coder-related
      failing methods; five are covered by §9.5 rows, two are rows that prescribe the
      wrong action (F3, F4), and these eighteen are covered by nothing:
        :229-258  test_rendered_codex_command_preserves_paths_arguments_and_stdin
        :260-288  test_rendered_codex_resume_uses_recorded_session_and_followup_prompt
        :410-424  test_card_output_contract_reaches_each_rendered_role
        :426-438  test_correction_contract_preserves_evidence_and_independent_verdict
        :457-465  test_coder_separates_recoverable_errors_from_unavailability
        :467-476  test_coder_handoff_names_commit_result_and_material_gaps
        :478-498  test_coder_routes_decisions_outside_its_mandate_to_planner
        :553-558  test_coder_checks_reported_obstacles_before_escalating
        :567-580  test_coder_owns_in_scope_decisions_and_shared_path_fixes
        :582-594  test_coder_codex_assignment_and_positive_documentation_replace_write_bans
        :596-611  test_coder_progress_is_not_a_discretionary_attempt_or_timeout_budget
        :613-633  test_coder_harness_brake_keeps_scoped_test_execution_with_its_author
        :659-664  test_full_suite_runs_once_on_the_final_candidate
        :666-680  test_project_binding_owns_hermes_md_and_isolates_local_inputs
        :682-696  test_reviewer_returns_questions_to_coder_without_inventing_defects
        :742-755  test_compression_preserves_authority_evidence_owner_and_exception
        :757-770  test_compact_contract_reaches_each_writer_without_external_style_load
        :782-789  test_ticket_reporting_keeps_failures_without_success_catalogues
      Two of these are not cosmetic: :229 and :260 are the only tests that execute the
      rendered invocation, and they fail purely because their regex is
      `r"   ```sh\\n"` (three-space indent) while §9.2's fence sits at column 0 -
      measured: unindented fence found true, indented fence found false, bash -n clean.
      :553-558 (:742-755, :613-633 likewise) assert duties §2.1 deletes, so they need
      inversion, not repair; :757-770 asserts `Goal:`/`Scope:`/`Constraints:`/
      `Evidence:`/`Acceptance:`/`Verify:`, the second brief §2.1:45 removes.
      Documentation sites the table also never dispositions:
        references/verification.md:31 "Coder task/resume invocation and result
          validation" for `diagnosing-bugs` - contradicts §2.2:63 and §9.2:335;
        references/verification.md:33 and references/setup.md:260 "Planner, Coder,
          Reviewer and Team-Codex" for the analysis integration - contradicts §2.2:69;
        references/code-analysis.md:3/:30/:38/:94/:127, references/integrations.md:390,
          references/native-workflow.md:52, references/update.md:138 carry the same
          phrase (named at file level by W2, not by any §9.5 row).
      And §9.5:408's range stops at :1095, but the same test method continues at
      :1098-1107 asserting that the five reference files contain "Planner, Coder,
      Reviewer and Team-Codex"; that loop breaks once verification.md:33 changes.
      Replacement: extend the table with one row per method above (disposition: rewrite
      the regex to the unindented fence / invert the removed-duty assertions to
      §9.2 wording / re-point retained rules) and with rows for
      verification.md:31, verification.md:33, setup.md:260, and the five-file phrase
      loop at test_render_reasoning.py:1098-1107.
      Reason: §5:228 requires the suites to pass and §9.5 presents itself as the list of
      "follow-on changes these texts force". W4:160's general sentence ("tests that
      currently assert mandatory Coder diagnosis ... must be changed") is not checkable
      and does not name the invocation tests at all.

  F2  MAJOR - §9.6 positive check cannot pass: one needle does not occur in either render.
      Location: docs/v3/PLAN_devteam_v3_codercutter.md:423
      Quote: "`exec --sandbox danger-full-access` and `exec resume --model` each present"
      Measured: "exec resume --model" present once; "exec --sandbox danger-full-access"
      present 0 times in the §9.2 render and 0 times in the 2.14.4 render, because both
      place `--model MODEL_ID` between `exec` and `--sandbox`:
      "{{CODEX_BINARY}} exec --model MODEL_ID --sandbox danger-full-access \\" (§9.2:303).
      Replacement: "`--sandbox danger-full-access` in the fresh form and
      `-c sandbox_mode='\"danger-full-access\"'` in the resume form are present".
      Reason: the same class as N3 - a check that a verifier must report as failed even
      though the text is correct. It is the only automated guard §9.6 offers for the
      sandbox bindings.

  F3  MAJOR - §9.5:399 disposes a test as "no change needed" whose two assertions fail.
      Location: docs/v3/PLAN_devteam_v3_codercutter.md:399 and
                references/test_render_reasoning.py:103, :105
      Quote (plan): "No change needed if :321/:322 keep the planner wording verbatim and
      both clauses; verify before touching"
      Quote (test): ":103 self.assertIn(\"only Codex CLI writes productive project code\",
      rendered[\"coder\"])"; ":105 self.assertIn(\"Tool and system prohibitions remain
      binding.\", rendered[\"coder\"])"
      Repository: §9.2:281 reads "only the Codex CLI writes product code" and §9.2:322
      reads "...; tool and system prohibitions remain binding." Both clauses are present
      semantically; neither string matches. Measured: both asserts fail.
      Replacement: ":82-:105 | ... | Re-point :103 to `only the Codex CLI writes product
      code` and :105 to the merged lower-case sentence at §9.2:322, or restore both 2.14.4
      sentences verbatim in §9.2:281/:322."
      Reason: this is the round-2 failure mode in the opposite direction - the restored
      rules were re-worded, so the tests that pin them now fail, and the table tells the
      implementer not to touch them.

  F4  MAJOR - §9.5:406 points at the wrong lines and would delete coverage the plan keeps.
      Location: docs/v3/PLAN_devteam_v3_codercutter.md:406
      Quote: ":307–:318 | Five VoltAgent sentences | Delete with the catalogue"
      Repository: the five assertions live at test_render_reasoning.py:302-306, inside
      test_voltagent_specialists_keep_original_settings_outside_parent_matrix (:299-307).
      Lines :309-321 (test_voltagent_source_contract_is_pinned_and_unchanged) and :323-329
      (test_voltagent_update_reads_version_inventory_without_parent_rebinding) test the
      pinned package manifest and update reference, are green today, and stay green after
      3.0.0 because §9.1 removes only the SOUL catalogue and §7:219 forbids removing the
      subagent capability. Two of the five assertions are not VoltAgent sentences at all:
      :302 "Keep the configured model and provider." and :306 "Preserve explicit customer
      financial/resource caps".
      Replacement: ":299–:306 | five assertions | rewrite: delete :303-:304 with the
      catalogue, re-point :302/:305 to §9.2:297 and :306 to §9.2:322; :309-:329 unchanged
      (package pinned, §7:219)."
      Reason: as written, an implementer deletes part of a source-pinning test and loses
      the only coverage that the VoltAgent package still matches its pinned revision.

  F5  MINOR - §9.4's deviation arithmetic and 2.14.4 column do not reproduce.
      Location: docs/v3/PLAN_devteam_v3_codercutter.md:386, :375-384
      Quote: "the text lands at 8.1 KB rendered, 59 % below the baseline, and 1.3 KB
      larger than the previous draft that two review rounds rejected"
      Measured: 8,107/19,652 = 41.3 %, i.e. 58.7 % below - correct. Against the previous
      draft (8,297 unrendered vs 7,419; 8,107 rendered vs 7,248) the growth is 878 B or
      859 B, not 1.3 KB. The §9.2 column reproduces exactly as unrendered block minus a
      3-byte heading allowance (919/871/2011/2570/579/1131/148 -> 916/868/2008/2567/576/
      1128/145), and 8,208 + 68 title + 21 = 8,297. The 2.14.4 column is 3-9 B low per row
      (blocks 1268/8382/3635/2378/2288/1489/148) and sums to 19,553, not 19,652.
      Replacement: "0.9 KB larger"; label the column "§9.2 (unrendered)"; correct the
      2.14.4 cells to 1,265 / 8,379 / 3,632 / 2,375 / 2,285 / 1,486 / 145.
      Reason: §9.4 is the document's only quantified claim, and the deviation argument is
      what Max is being asked to accept.

  F6  MINOR - §9.2:323 keeps a Coder-side verification verb.
      Location: docs/v3/PLAN_devteam_v3_codercutter.md:323
      Quote: "A local input the project's development entrypoint rejects stays in place:
      verify in a clean detached worktree at the candidate commit, never delete, rewrite
      or mask it."
      Contradicts: §9.2:284 "no test replay", §3.1:88 "Do not read the diff, repeat tests,
      or independently determine correctness", §5:200 negative assertions. Impersonals in
      a SOUL bind the role that reads it; "verify" here is product verification by the
      Coder. (The guard - leave the local input alone - is the load-bearing half and must
      stay.)
      Replacement: "A local input the project's development entrypoint rejects stays in
      place: have Codex verify in a clean detached worktree at the candidate commit;
      never delete, rewrite or mask it."
      Reason: one of the two remaining Coder execution verbs; the plan's own matrix §1:29
      assigns operational steps but never verification.

  F7  MINOR (CAC) - §9.2:318 replaces an exact identifier with a display name.
      Location: docs/v3/PLAN_devteam_v3_codercutter.md:318
      Quote: "keep card and assignment and verify the recipient, the subscription wakes
      {{PLANER_NAME}}."
      2.14.4 (baseline:103) reads "The existing subscription wakes `{{PLANNER_PROFILE}}`
      for customer coordination."; test_update_team.py:284 asserts the profile ID
      (`fixture-planner` = roles['planner']['id']). The wake mechanism is keyed by profile,
      not by display name.
      CAC rule: cac-notation.md §1 "Keep identifiers, paths, commands, code symbols, and
      quoted values exact"; cac-authoring-contract.md:10 "Preserve the actor ... Keep exact
      commands, identifiers, paths, literals". The comma splice also fuses two rules
      ("verify the recipient" and "the subscription wakes ..."), which §1 forbids as
      ambiguity.
      Replacement: "...; keep card and assignment, verify the recipient, and confirm the
      existing subscription wakes `{{PLANNER_PROFILE}}`."
      Reason: the only place in §9.2 where an operative identifier is swapped for a
      descriptive one; §9.5:409 already rewrites the test, so the change is cheap to
      correct now and expensive to notice later.

  F8  MINOR - §9.5:413 under-describes the diagnosing-bugs rewrite.
      Location: docs/v3/PLAN_devteam_v3_codercutter.md:413
      Quote: "Seven strings of Coder diagnosis and handoff duty | Rewrite: `$diagnosing-bugs`
      cue moves to `team-codex-AGENTS.md`; the Coder keeps only the handoff half
      (`never kanban_complete`), which §9.2 states"
      Repository: the seven strings are test_diagnosing_bugs.py:198-205. Two of them are
      neither diagnosis nor handoff: :201 "On restart or resume, include current state,
      relevant delta, remaining work and standing constraints." (no §9.2 successor) and
      :205 "Preserve explicit customer financial/resource caps, ..." (§9.2:322 says
      "financial and resource caps"). The "handoff half" cannot be kept either: :204 says
      "Never use `kanban_complete` to close your own implementation." while §9.2:328 says
      "never `kanban_complete` on your own implementation".
      Replacement: "Rewrite: the four diagnosis sentences (:198-:200) move to
      `team-codex-AGENTS.md`; re-point :201 to §9.2:298 (session resume), :202-:203 to
      §9.2:293, :204 to §9.2:328's wording, :205 to §9.2:322's wording."
      Reason: "keeps only the handoff half" implies a mechanical deletion that leaves the
      test failing at four of seven strings.

  Explicit no-finding lines
    B, direction 2 (Coder-owned duties)   no finding. Every coordination duty is present
      and explicit; see THE IDEA for clause references.
    C, sites that do exist and are correct   no finding for §9.5:396 (:201/:252 do assert
      "Coder passes the literal `$build-evidence` cue" and "Coder explicitly invokes and
      validates results"), :397 (all six target values verified in manifest.json), :398,
      :400, :401, :402, :403, :404, :407, :408, :409, :410, :411, :412, :414, :415, :416,
      :417. §9.5:414's setup.md:230 target list ("currently `screenshot-to-code`,
      `diagnosing-bugs` and `build-evidence`") and :257 Coder `$diagnosing-bugs` readback
      both exist as described; :417's native-workflow.md:28 exists and reads "all three
      roles; kept only in private team state"; :416's "No demo recipe" is correct
      (integrations.md has no demo section).
    E, §9.2 obligation strength and literals   no finding. MUST/SHOULD/MAY are preserved
      (only :283 upper-cases an existing "must not"), and every command literal I checked
      is byte-exact against 2.14.4: `kanban_block(kind=\"needs_input\", reason=...)`,
      `kanban_request_review(summary=..., reviewer=\"{{REVIEWER_PROFILE}}\")`,
      `thread.started`, `PONYTAIL_DEFAULT_MODE=full`, `-c model_reasoning_effort='\"REASONING\"'`,
      `-c sandbox_mode='\"danger-full-access\"'`, `demo.sh retire`, `demo.sh user`.
    E, §9.3   no finding. Frontmatter shape matches skills/build-evidence/SKILL.md; the
      lifecycle, teardown and creation sentences are the 2.14.4 literals; the password is
      correctly absent so the file stays a byte-identical copy.
    E, §9.2:311 (worker guard)   no finding. Dropping "in unattended runs" and "or use the
      file tools" strengthens the prohibition in the safe direction and loses no
      permission; §9.5:405 discloses the rewrite.
    E, audience rule   no finding. §9.2 and §9.3 are team-internal technical English; no
      customer-facing text and no role-owned human text is compressed.

VERIFIED CLAIMS

  - HEAD, both sha256 values and `git status --short` identical at handover and before the
    verdict; `git diff --stat` empty; nothing implemented (manifest 2.14.4, no
    skills/demo-handover, no demo path in manifest.files).
  - §9.2: 8,297 B unrendered, 8,107 B / 64 lines rendered with the fixture bindings;
    matches §9.2:270, §4/W1:135 and §5:197 exactly.
  - Exactly 14 placeholders, set-equal to manifest.role_templates.coder.render_fields;
    no residual braces; render_role accepts the text without error.
  - The rendered development-authority bullet is string-identical to the rendered
    planner:12 line and occurs once (test_render_reasoning.py:90/:100 hold).
  - {{DEMO_PASSWORD}} occurs once in the §9.2 source; the backticked `demo-handover`
    pointer occurs once.
  - Rendered ```sh block: bash -n rc 0; both invocation forms present with every 2.14.4
    flag and literal intact; fence is unindented (source of F1's two execution-test
    failures).
  - §9.6's eleven negative needles: 1 occurrence in the 2.14.4 render, 0 in the §9.2
    render, all eleven.
  - §9.1's removal statements match the text: subagent catalogue, harness staging ladder,
    synthetic-harness rules, CBM binding, polling paragraph, RED evidence, changelog,
    analysis integration, consumer enumeration are all absent; reasoning caps, both
    invocation forms, worker-guard rule, harness stop rule, commit identity,
    destructive-Git ban, evidence pointers, state provenance, Hindsight rules are all
    present. Communication is one line (§9.2:336).
  - §9.4's §9.2 column sums to the unrendered total (8,208 + 68 + 21 = 8,297).
  - Repository sites: manifest.json:201/:252 exact; target values
    plan-versioning-semver [planner,coder], build-evidence [coder,reviewer],
    screenshot-to-code [planner,coder], ponytail.targets.hermes [coder],
    codebase-memory/graphify [planner,coder,reviewer] all as stated;
    templates/team-codex-AGENTS.md 8 lines / 1,524 B with Task/Resume/Children/Result;
    test_update_team.py:283-285, :419-424, :1008-1009; test_build_evidence.py:71-72;
    test_diagnosing_bugs.py:198-205; setup.md:230, :257, :260; verification.md:31, :33;
    upstream-sources.md:103, :126-127; native-workflow.md:28.
  - Reference suite green at HEAD (85 tests, OK), so every failure I report is caused by
    §9.2 and not by a pre-existing defect.
  - Reading discipline: the diff and the repository were read first; §9.7/§9.8's tables
    were checked against the text afterwards and were used as pointers only. No file was
    written; the render, the test substitution and bash -n were all in memory/stdin.

OPEN QUESTIONS

  - Whether every one of the eighteen methods in F1 should be inverted (assert the
    removed duty's absence) or deleted outright: the plan needs one rule, as it already
    has for the diagnosing-bugs block.
  - Whether the unindented fence in §9.2 is intended. If the SOUL is meant to keep the
    2.14.4 three-space indentation, the rendered bytes and line count change and §9.2:270,
    §4/W1 and §5:197 need re-measuring; if not, the two execution tests must be rewritten.
  - §9.4:386 says "Max approved 3.5–4 KB" while the plan header and §4/W1 quote a
    "<= 5 KB" aim superseded by revision 2. The repository cannot settle which target Max
    set; the deviation argument is unaffected either way.
  - Whether `ponytail` with an empty `targets.hermes` is a valid manifest state or should
    leave the Hermes matrix entirely: no test validates emptiness (unchanged from round 2).
  - Whether Codex selecting `plan-versioning-semver` from its description alone suffices,
    or the explicit cue now routed through team-codex-AGENTS.md is required (unchanged
    from round 2).

---
Reviewed by Fujiko, round 3, read-only.

---

## Marikos Gegenprüfung und Umsetzung (2026-11-23)

Selbst nachgemessen, nicht übernommen:
- **Die zwei Invocation-Tests** (`test_rendered_codex_command_preserves_paths_arguments_and_stdin`, `…_resume_…`) auf einer Checkout-Kopie mit dem §9.2-Text ausgeführt: beide `ok`. Ursache der von Fujiko gemeldeten Fehler war der nicht eingerückte Zaun; der Text hat jetzt zwei getrennte `sh`-Blöcke mit drei Leerzeichen Einrückung wie 2.14.4.
- **Fehlerinventar:** mit §9.2 im Template meldet `test_render_reasoning.py` 36 failures + 2 errors über 25 Methoden, `test_build_evidence.py` 1, `test_diagnosing_bugs.py` 1; mit dem 2.14.4-Template dieselbe Kopie 85 Tests `OK`. Alle Abweichungen stammen also aus §9.2.
- **Maße:** 8.436 B unrendered, 8.247 B / 69 Zeilen gerendert; 2.14.4: 19.652 B unrendered, 19.463 B / 140 Zeilen. Beide Spalten in §9.4 mit derselben Methode (Abschnitt inkl. Überschrift).

| Befund | Umsetzung | Stand |
|---|---|---|
| F1 | §9.5 trägt jetzt die Regel (re-point / invert / unchanged), die 25-Methoden-Liste, die Referenz- und Manifeststellen und ein gemessenes Abschlusskriterium | korrigiert |
| F2 | Sandbox-Prüfung je Zaun getrennt (`--sandbox …` im Lauf, `-c sandbox_mode='"danger-full-access"'` im Resume) | korrigiert |
| F3 | beide 2.14.4-Sätze wörtlich zurück (`only Codex CLI writes productive project code`, `Tool and system prohibitions remain binding.`), Tabellenzeile korrigiert | korrigiert |
| F4 | Zeile auf `:299`–`:306` korrigiert, `:309`–`:329` ausdrücklich unverändert | korrigiert |
| F5 | beide Spalten in §9.4 neu gemessen, „1,0 KB" statt „1,3 KB" | korrigiert |
| F6 | „have Codex verify in a clean detached worktree" | korrigiert |
| F7 | `{{PLANNER_PROFILE}}` für die Subscription, Kommaspleiß aufgelöst | korrigiert |
| F8 | `test_diagnosing_bugs.py` je Zeichenkette einzeln zugeordnet | korrigiert |

Eine vierte Runde ist auf diesem Stand noch nicht gelaufen.
