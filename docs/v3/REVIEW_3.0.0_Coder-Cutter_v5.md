# REVIEW — Maker-Plan `PLAN_devteam_v3_codercutter.md`, Runde 5 (Coder-Cutter), CAC-Audit

Reviewer: Fujiko (independent, review-only; one-shot run in profile `fujiko`, model `deepseek/deepseek-v4.1-flash-1017`, reasoning high, tools `file,terminal`, read-only)
Date: 2026-11-23 (CET)
Review object: `docs/v3/PLAN_devteam_v3_codercutter.md`, sha256 `dce9c113684b20bc3ccbd50db7e0c2e77e48e0ebe2503a14800fa9cfee0c3c04`
Frozen state: HEAD `a4af6bd31911b22d580b8dff20cf3ac2e3393420`, `git status` = ` M docs/v3/PLAN_devteam_v3_codercutter.md`
CAC criterion: `cac/SKILL.md`, `references/cac-notation.md`, `references/cac-authoring-contract.md`, read in full; §9.2, §9.3 and §10.2 audited line by line against six tests

**VERDICT: CHANGES REQUIRED** — two blocking-class findings, both in §10. §9.2 and §9.3 pass every CAC test except one ambiguity in §9.2 `:336`. The substance: §10 rested on a false premise — the Maker *does* prescribe a per-card skill, in the Brownfield phase-release procedure.

---

## Reviewer report (verbatim)

EXACT REVIEWED STATE

  At handover (2026-11-23, profile fujiko, read-only)
    repository   /home/mariko/projects/generic-devteam
    HEAD         a4af6bd31911b22d580b8dff20cf3ac2e3393420  ("plan v3 added")
    git status   " M docs/v3/PLAN_devteam_v3_codercutter.md"
    plan sha256  dce9c113684b20bc3ccbd50db7e0c2e77e48e0ebe2503a14800fa9cfee0c3c04
    implemented  no: manifest.json 2.14.4; no skills/demo-handover; no demo entry
                 in manifest.files; test suite green at HEAD (85 tests OK)
    history      docs/v3/REVIEW_3.0.0_Coder-Cutter_v1..v4.md all tracked at HEAD;
                 round 4 report committed and unchanged

  Immediately before the verdict (re-run)
    HEAD         a4af6bd31911b22d580b8dff20cf3ac2e3393420
    git status   " M docs/v3/PLAN_devteam_v3_codercutter.md"
    plan sha256  dce9c113684b20bc3ccbd50db7e0c2e77e48e0ebe2503a14800fa9cfee0c3c04
    my writes    none inside the checkout; substitution work only in
                 /home/mariko/.hermes/profiles/fujiko/cache/scratch/r5/repo

VERDICT: CHANGES REQUIRED

Two findings block implementation. Finding 1 is substantive: §10's changeset leaves the
Maker instruction that actually prescribes the pin untouched, so the directive it places in
the Planner SOUL is contradicted by the procedure the Planner loads at that exact step, and
§10.1's causal claim is false as written. Finding 2 is mechanical but produces a red suite:
§10.2's code block is not the byte-exact target text and, taken literally, breaks a green
assertion that §10.3 declares unaffected. §9.2 and §9.3 contain no BLOCKING or MAJOR issue;
their one finding each is a wording remark. The measurements, the §9.4 table and the five
factual claims in §10 are reproduced except claim 3 and the causal half of claim 5.

CAC AUDIT

Basis read in full before judging: cac/SKILL.md, references/cac-notation.md,
references/cac-authoring-contract.md. Contract anchors used: notation §1 (minimum complete
expression, exact literals), §5 (audience), contract:7 (shortest version … same authority),
:10 (actor/trigger/obligation/order/exceptions/scope/failure exit; exact commands, paths,
literals), :11 (state observed/whom/which revision; pointer must resolve), :12 (durable
authority in role instructions, procedure at its point of use, change the owning clause).

§9.2 — Coder SOUL (plan:279-347; 69 lines; 8,447 B unrendered)

  Line-by-line classification (what each line is):
    279 heading            281 heading            289 heading
    297 heading            321 heading            333 heading
    338 heading            345 heading            blanks 280/282/288/
    296/298/302/308/310/316/320/322/332/334/339/344/346
    283 directive + boundary, literal "Codex CLI"
    284 directive (actor/obligation, three roles named by placeholder)
    285 directive + prohibition ("MUST NOT accumulate")
    286 prohibition (three negations)
    287 directive + prohibition, literal `command_allowlist`
    291 directive + condition ("when they matter") + prohibition
    292 directive + scope ("only")
    293 directive + condition + exit (return to {{PLANER_NAME}}) + prohibition
    294 directive + condition + literal (4 KB, plan revision)
    295 exact literals (`Change:`, `Checked:`, `Open:`)
    299 directive + condition + exception + exact literals (`{{CODEX_HOME}}/config.toml`)
    300 directive + condition + exception + prohibition
    301 directive + exact literals (`hermes-codex`, `background=true`, `pty=true`, `workdir`)
    303-307, 311-315  exact literal blocks (two `sh` fences)
    309 directive pointer        317 directive + exact literals
    318 prohibition + exact literals   319 directive + condition + exit + prohibition
    323 condition + directive + prohibition    324 condition + directive + prohibition
    325 condition + directive + literals + order + exit
    326 condition + directive + literal + prohibition
    327 condition + directive + literal + order
    328 condition + directive + scope + boundary
    329 boundary + prohibition ("Running the app from source grants no deployment authority.")
    330 condition + directive + prohibition + exit
    331 condition + directive + exact literal `{{DEMO_PASSWORD}}` + prohibition
    335 directive + exact literal + prohibition + condition + order
    336 exact literals + directive (finding below)
    340 prohibitions + literals + condition + directive
    341 directive + condition + declarative fact (state provenance) + prohibition
    342 condition + directive + literals + promotion rule
    343 directive + scope                     347 declarative facts (identifiers)

  Test 1 (shortest complete form): no finding on 283-335, 340-343, 347. Each bullet is one
  directive; the qualifiers that remain are conditions or exits, not padding. Spot-check:
  :286 "no second technical brief, no diff review, no test replay" — three distinct
  prohibitions, none removable. :293 both checks and the exit are needed. :343 "distinguish
  implemented, tested, independently reviewed and approved" — the four states are distinct
  (contract:11). Finding only on :336 (below).

  Test 2 (obligation strength vs 2.14.4): no finding. MUST/MUST NOT survive where the
  baseline states them (`MUST NOT accumulate` :285, `never` :287/:340, `must not` implicitly
  through `never` in :335) and permissive forms stay permissive (`may raise it up to` :299,
  `may use existing explicitly permitted runtime verbs` mapped to `need no further customer
  approval` :328). No MVN was strengthened or softened against the 2.14.4 wording I compared
  (:283 and :329 are the baseline sentences verbatim; test_render_reasoning.py:103/:105 pin
  them).

  Test 3 (literals byte-exact): no finding. Verified against the repository/test expectation:
  `kanban_request_review(summary=..., reviewer="{{REVIEWER_PROFILE}}")` :335,
  `kanban_complete` :335, `kanban_block(kind="needs_input", reason=...)` :325,
  `kind="capability"` :326/:319, `kind="transient"` :327, `thread.started` :300,
  `PONYTAIL_DEFAULT_MODE=full`, `--sandbox danger-full-access`,
  `-c sandbox_mode='\"danger-full-access\"'`, `--json -o RESULT_FILE - < PROMPT_FILE`,
  `demo.sh retire`/`demo.sh user`, `{{DEMO_PASSWORD}}`, `command_allowlist`. The two fences
  keep three-space indentation and are found by r"   ```sh".

  Test 4 (duplication): no finding. :284 "You approve neither your own implementation nor its
  completion" and :335 "never `kanban_complete` on your own implementation" are a boundary and
  its transition verb, separately pinned by tests. :336's fields and :295's compact result are
  different surfaces (Codex reply vs Reviewer handoff). The new :336 sentence does not restate
  either.

  Test 5 (explanation leakage): no finding on :283-343. The text is imperative or a boundary.
  Two lines carry a justification clause — :318 "the worker guard blocks both and no approval
  is available" and :342 "and ask Codex for the code fact instead of investigating" — both
  name the enforcement or the allowed alternative, i.e. an exit, not a motive; clause 5 is
  not triggered.

  Test 6 (ambiguity): FINDING 5 below (:336 "on which revision").

  FINDING (§9.2) — MINOR
    while testing §9.2 I found:1  plan:336  failing test 6
    text: "State who ran each check and on which revision; never report a Codex result as
           your own check."
    issue: "revision" has two precedents in this same text and they denote different objects:
           plan:294 "pointing to the exact plan revision" and plan:341 "the exact accepted plan
           revision", while the code state is called commit/branch everywhere (:293, :335,
           :340). A fresh Coder writing the `Checks:` field must guess whether it states the
           plan revision or the commit the check ran against.
    replacement: "State which actor ran each check and the exact commit it ran against; never
           report a Codex result as your own check."
    note: the second half of the line is a genuine improvement over the observation it
           replaced — the obligation is now a directive and the prohibition is explicit. No
           other part of the line is at issue.

§9.3 — `demo-handover` (plan:354-378)

  Line-by-line classification:
    355-366 frontmatter — existing syntax contract, untouched (CAC SKILL.md:48)
    368 heading          370 trigger + locator (see test 5 note)
    372 declarative constraint + directive + verifiable exit ("a stopped runtime is not a
        retired one")
    373 directive + exact literal `demo.sh retire` + prohibition + enforcement fact
    374 directive          375 directive + literal `demo.sh user` + prohibition
    376 directive          377 directive + enumerated facts to record

  Test 1: no finding. Each bullet is one action; :372's ownership/verification clauses are
  the failure exit for the replacement claim and cannot be dropped without losing the exit.
  Test 2: no finding — the baseline coder.SOUL step-13 wording is preserved with unchanged
  strength ("never compose … yourself", "at most one"). Test 3: no finding — `demo.sh retire`,
  `demo.sh user`, "environment variable the script documents" match the SOUL (:331) and the
  Planner template (:76) literally. Test 4: no finding — the Planner surface specifies what
  the demo card must carry; this skill instructs the Coder to record the readback. Different
  actors, no repeated rule. Test 5: no finding. :370's second sentence ("The demonstration
  user's password stays in the role instructions; this skill carries the runtime procedure")
  reads as a meta-statement, but it performs a locator function: it tells the skill's reader
  where the secret is, which prevents it being copied into or searched for in this file. That
  is an operational fact about a surface boundary, not reassurance. Test 6: no finding — the
  trigger is explicit ("a released demo handover card, not a code card") and :372's order
  (retire previous, verify gone, then start) is sequenced.

§10.2 — Planner directive (plan:541-549)

  Line-by-line classification:
    543 placement instruction (implementer-facing), form ambiguous — see finding 2
    546 the directive itself, one bullet: directive + prohibition + colon-introduced
        declarative justification — see finding 3
    549 meta-statement about the directive itself — see finding 4

  Test 1: FAILS on :546's second half. "role skills come from setup, card requirements from
    the body and its criteria" states provenance/placement that the same Planner file already
    establishes two lines earlier (template:76 "Body: Outcome/context beyond the title,
    observable criteria, …" and :77 "Make the card understandable without opening the full
    plan"). Shorter complete form: "…through the Kanban tools; set no `skills`: role skills
    come from setup."
  Test 2: no finding. "set no `skills`" is a prohibition; no MUST was added or removed
    elsewhere in the bullet.
  Test 3: FAILS. See finding 2: the block's first clause is not byte-exact against
    templates/roles/planner.SOUL.md.template:78.
  Test 4: FAILS (same clause as test 1): requirements-in-the-body is stated twice in one
    loaded file.
  Test 5: FAILS on :549; and the clause "role skills come from setup" is a declarative claim
    whose truth the Maker does not own — references/integrations.md:8 keeps Hermes and its
    distribution skills native-managed ("Maker neither pins nor installs …"), so not every
    role skill originates in setup. See finding 3.
  Test 6: FAILS on :543/:546 — "append … at the end of the sentence" versus a fenced block
    that presents the whole bullet and omits the two sentences that follow it on :78. See
    finding 2.

  FINDING (§10.2) — MAJOR  plan:546, failing tests 3, 4, 5, 6
    text as given: "- Set assignee, workspace, dependencies and required runtime fields through
      the Kanban tools; set no `skills`: role skills come from setup, card requirements from
      the body and its criteria."
    target text (templates/roles/planner.SOUL.md.template:78): "Set assignee, workspace,
      dependencies, and required runtime fields through the Kanban tools. Create and release
      the cards through Brownfield's phase release procedure; it owns the worker-run hang cap
      and the native runtime fields. Omit team setup, routine procedures and restatements of
      role duties or workflow from the body. …"
    defects: (a) the Oxford comma before "and required runtime fields" is dropped although
      test_render_reasoning.py:811 asserts that exact substring; (b) the block omits the two
      sentences that follow the replaced sentence, so "append" and the block contradict each
      other on the resulting line; (c) the justification half duplicates :76/:77 of the same
      file and asserts a provenance the Maker does not own.
    replacement (exact target line, keeping :78's remaining sentences):
      "Set assignee, workspace, dependencies, and required runtime fields through the Kanban
      tools; set no `skills`: role skills come from setup. Create and release the cards
      through Brownfield's phase release procedure; it owns the worker-run hang cap and the
      native runtime fields. Omit team setup, routine procedures and restatements of role
      duties or workflow from the body. Bind the plan; require no separate specification read
      when the plan carries the requirement."
    measured: verbatim substitution of the block's own line for :78's first sentence turns
      test_render_reasoning.py:816 red (AssertionError on the :811 string, run in scratch copy,
      1 failure / 85 tests). Substituting the replacement above keeps 85 tests OK.

  FINDING (§10.2) — MINOR  plan:549, failing test 5
    text: "This is a directive, not an explanation: it names the prohibition, the mechanism it
      replaces (setup) and the place a card requirement belongs."
    issue: explicit test-5 example — a meta-statement ("this is a directive, not an
      explanation") whose only function is to defend the wording. It also restates what the
      directive says.
    replacement: delete the line. The persuasion belongs in the review report, not in the plan.

  No finding: plan:534-539 (§10.1 evidence sentences) — they are evidence prose, not a role
  surface, and I reproduced each claim (see FACTUAL CLAIMS), with the one exception of the
  causal sentence, covered by finding 1.

MEASUREMENTS

  §9.2 extracted byte-exactly from plan:279-347 (the four-backtick block, closing fence
  excluded), sha256 of the extracted segment starts 247f8660…
    unrendered          8,447 B / 69 lines        plan claim: 8,447 B        ✓
    rendered            8,258 B / 69 lines        plan claim: 8,258 B / 69   ✓
    (fixture method of references/test_render_reasoning.py: default "medium", maximum "high",
    PROFILE fields "example-role", CODEX_* paths "/work/codex_*")
    placeholders        14, set-equal to manifest.role_templates.coder.render_fields (default
                        profile), zero residual "{{" in the render           ✓
    baseline unchanged  19,652 B unrendered / 19,463 B / 140 lines rendered  ✓

  §9.4 §9.2 column, re-measured per section (heading included, split at top-level '#'):
    Title line 68 | Role and authority 926 | Delegate 871 | Session 2,104 |
    Blockers 2,609 | Review handoff 590 | Evidence, Git, memory 1,131 | Project binding 148
    sum 8,447 = the unrendered total; every cell matches plan:386-394 exactly, including the
    updated Review handoff 590 B.                                            ✓
    2.14.4 column unchanged from round 4: 64/1,268/8,382/3,635/2,378/(—)/(2,288)/(1,489)/148
    = 19,652.

FACTUAL CLAIMS

  1. references/integrations.md:139 delivers superpowers to the Planner only.
     CONFIRMED. :137 heading "## Superpowers — nur Planner"; :139 "Deliver the complete
     [obra/superpowers](…) repository only to Planner …"; the install recipe :142 uses
     `hermes -p "$PLANNER"`.
  2. gateway/session_kanban.py:386-388 raises only when no pinned skill loads.
     CONFIRMED. :386 `skills, loaded, missing = build_preloaded_skills_prompt(...)`;
     :387 `if missing and not loaded:`; :388 `raise ValueError('kanban_skills_unavailable')`.
     Semantics are exactly as stated: a partial pin proceeds silently, a total pin raises.
     (Related runtime fact: :45-49 injects `sdlc-review` itself on the review lane, so no pin
     is needed for it either.)
  3. references/test_render_reasoning.py:811 matches the Planner sentence up to "Kanban
     tools" and is unaffected by the suffix.
     PARTLY REFUTED. The assertion is :811
     "Set assignee, workspace, dependencies, and required runtime fields through the Kanban
     tools" — with a comma before "and". It is unaffected only if the clause is appended to
     :78's existing sentence. §10.2's code block replaces that sentence without the comma and
     thereby breaks :816; measured, see the §10.2 finding. The claim is true of the intended
     change and false of the text the plan prescribes.
  4. No open card on any board carries a non-empty `skills` column.
     CONFIRMED. 148 task rows over 19 board databases (incl. _archived): blocked 9, done 136,
     ready 1, todo 2. All 18 rows with a non-empty `skills` value are `done` (codebase-memory,
     graphify, screenshot-to-code, codex, superpowers:executing-plans). The trigger card
     t_c6a2fd76 now reads `skills NULL`, status blocked/needs_input.
  5. `--skill` occurs in no Maker text.
     CONFIRMED as a string (the only occurrence in the repository is the plan itself, at
     plan:539). REFUTED as the inference drawn from it: the Maker does prescribe a per-card
     skill. skills/brownfield-feature-planning/references/kanban-phase-release.md:32 requires
     "Set native assignee and workspace, `--initial-status blocked`, idempotency key,
     **required skill**, explicit completion contract, …" and :49 verifies "Check assignee,
     workspace, **skill**, runtime/retry fields, and completion contract". `--skill`
     (dest=skills, hermes_cli/kanban_parser.py:189, "Skill to force-load into the worker") is
     exactly that field. The Planner SOUL:78 tells the Planner to "Create and release the
     cards through Brownfield's phase release procedure", i.e. the procedure it was obeying.
     "Nothing in the Maker prescribes a pin … The Planner improvised it" is therefore not
     supported. See finding 1.

  §10.1's board evidence, checked independently and upheld:
    - same turn: t_0c69298a and t_c6a2fd76 both created_at 1795361736; created payload of
      t_c6a2fd76 carries `skills: ["superpowers:verification-before-completion"]`;
      t_0c69298a carries `["codex","superpowers:executing-plans"]`.          ✓
    - died before its first turn twice: runs 36 and 37 each claimed/spawned/worker_bound, then
      worker_result exit_code 1 with empty last_output, crash, then `gave_up`
      {"failures": 2} on run 37.                                              ✓
    - cause: the operator comment records the removal of the pin and attributes runs 36/37 to
      `kanban_skills_unavailable`; Jack's comment cites Carter's
      `logs/managed-worker.log` lines 14–15 / 29–30 for the same token. The token is not in
      the stored `last_failure_error`; it is in the operator's and Jack's written evidence. ✓
      (observation: the card is blocked today for an unrelated Docker retire-formatter reason,
      not for the pin — the sentence's "and blocked" describes the crash sequence, which is
      accurate as of `gave_up`.)

THE IDEA (E)

  Direction 1 — no implementer duty survives in §9.2. No finding.
    diff/judging code        absent: :286 "no second technical brief, no diff review, no test
                             replay"; :340 "Verify commit existence and identity, not its
                             content."
    tests                    absent: :286 "no test replay"; :295 only requires Codex's compact
                             result; no test-strategy or matrix rule in the text.
    analysis/source scan     absent: :291 "No second ticket fetch, no plan or source scan of
                             your own."; :292 "Establish operational facts only"; :342 "ask
                             Codex for the code fact instead of investigating."
    harness                  absent: :319 "a failing harness is a setup defect, so direct Codex
                             to fix its cause once"; no staging ladder.
    independent verification absent: :284 "You approve neither your own implementation nor its
                             completion."; :335 hands to the Reviewer.
    (The branch-existence check at :293 and the runtime operation at :328 are the two
    mechanical/operational duties §2.1:48 and §1:29 keep with the Coder, not implementation.)

  Direction 2 — every coordinator duty present. No finding.
    delegation        :291 card body + when to read comments; :292 operational facts; :293
                      branch at start commit, return on failure; :294 original task, binding
                      references, agent-guide path, 4 KB brief; :295 compact result.
    session           :299 model/reasoning limits; :300 one session, `thread_id`, resume rules,
                      no concurrent turns; :301-317 both fences and literal substitution;
                      :318 worker guard; :319 harness exit.
    blockers          :323 question to Codex; :324 decision in authority; :325 needs_input with
                      comment → block → subscription wake → reread; :326 capability; :327
                      transient + the single TIMER request; :330 unrelated work to the Planner.
    kanban/review     :335 native transition, `ok: true` / `status: "review"`, never
                      `kanban_complete`, no project changes until return; :336 handoff fields
                      and now the actor/revision obligation.
    operations        :328 development/demo runtime; :329 no ticket-implied approval, caps and
                      prohibitions binding; :330 local-input protection; :331 demo skill pointer
                      and password literal; :287 command grants not changeable.
  The single change since round 4 (:336) adds a coordinator reporting obligation and removes
  nothing; the idea holds.

OTHER FINDINGS

1. MAJOR — §10's changeset does not reach the Maker instruction that prescribes the pin, and
   the directive it adds therefore contradicts a procedure the Planner loads at that step.
   plan:534-539 ("Nothing in the Maker prescribes a pin … The Planner improvised it"),
   plan:543-547, plan:555-558; §7:217; §2.2:73.
   Evidence: skills/brownfield-feature-planning/references/kanban-phase-release.md:32
   ("required skill") and :49 ("skill"); templates/roles/planner.SOUL.md.template:78 sends
   the Planner into that procedure; hermes_cli/kanban_parser.py:189 makes `--skill` the field
   for it. The plan declares brownfield-feature-planning "Untouched" (§2.2:73), the §7
   carve-out covers only "the card-creation directive", and §10.3's consequences table names
   neither the reference nor its test.
   Requirement: (a) correct §10.1 to state that the Maker's phase-release procedure requires
   a per-card skill and that pinning is what it was followed as; (b) add a §10.3 row:
   "`skills/brownfield-feature-planning/references/kanban-phase-release.md:32` and `:49` | drop
   `required skill` and `skill` from the set and the check list, so card skills come only from
   setup"; (c) add "`references/test_brownfield_planning.py:308` | re-point: the release
   string no longer contains `required skill`"; (d) either widen §7's carve-out to name the
   Brownfield card-creation procedure or move the prohibition there — measured:
   removing "required skill" from :32 breaks
   test_brownfield_planning.BrownfieldPackageTests.test_progress_policy_preserves_explicit_and_native_limits_only
   (1 failure / 19 tests).
   Reason: the fix otherwise leaves two contradictory instructions in the same Planner load
   path (SOUL says "set no `skills`", the loaded procedure says "required skill" and then
   verifies it); cac-authoring-contract:12 requires changing the owning clause rather than
   adding a second version.

2. MAJOR — §10.2's fenced line is not the byte-exact target text, so following it turns a
   green assertion red while §10.3 says the test is unaffected. plan:543, plan:546,
   plan:555. Measured: 1 failure / 85 tests under a verbatim substitution, 85 OK under the
   replacement given in the §10.2 finding. Same evidence as CAC finding for :546.

3. MINOR — §10.3 cites a measurement that does not exist. plan:556 "(§9.5 measurement,
   re-checked 2026-11-23 across all boards: zero open cards with a non-empty `skills`)".
   §9.5 (plan:402-454) contains no card- or skills-related measurement; the only §9.5 rows
   that mention `skills` are about `demo-handover` and manifest targets. The number is true
   (I measured 148 tasks: 0 open cards with a non-empty `skills`), but the pointer does not
   resolve, contrary to cac-authoring-contract:11. Replacement: "None carries a pin
   (measured 2026-11-23 across 19 board databases, 148 cards: every card with a non-empty
   `skills` value is `done`; 0 of 12 open cards)".

4. MINOR — §10.4's negative check names a non-existent identifier. plan:562 "Negative:
   `plan-versioning` unchanged". The skill is `plan-versioning-semver`
   (manifest.json:60/:278/:291). A negative check against a name that does not exist passes
   trivially and cannot detect a change. Replacement: "`plan-versioning-semver` unchanged".

5. MINOR — §10.4 states the rollback purpose inverted. plan:562 "the changeset is committed
   separately from them so the Coder role change can be rolled back alone". A separate commit
   isolates the pin directive for rollback; the Coder role change lives in the W1-W6 commits
   and is not made revertable by this separation. Replacement: "…committed separately from
   them so the card-pin rule can be rolled back without reverting the Coder role change".

6. MINOR — the pin changeset has no acceptance row and no Definition-of-done item. §5
   (plan:182-198) has no row for it and §8 (plan:225-232) does not name it; §7:217 is the only
   internal cross-reference. §10.4 requires the Planner render to contain the clause exactly
   once, which is a positive check but not one of the release acceptance outcomes.
   Replacement: one §5 row, e.g. "Card skill pins (§10) | the rendered Planner SOUL contains
   `set no \`skills\`` once; the phase-release procedure no longer requires a card skill; a
   `kanban_create` call without `skills` dispatches normally", plus a §8 list item.

OPEN QUESTIONS

1. Should the prohibition live in the phase-release procedure (its point of use) rather than
   in the Planner SOUL, with the SOUL keeping only the pointer? cac-authoring-contract:12
   favours the owning clause; §10.2 chose the SOUL. The SOUL and the procedure must agree
   either way, which is finding 1's core.
2. Was `required skill` in kanban-phase-release.md:32 ever honoured for a legitimate reason —
   e.g. a card that must force-load a non-role skill? The runtime already injects
   `sdlc-review` on the review lane (gateway/session_kanban.py:45-49), and all 18 historical
   pins name role assets (codebase-memory, graphify, screenshot-to-code, codex, superpowers),
   so no legitimate case is visible; the plan should say so once instead of leaving the
   reader to infer it.
3. Does the pin changeset ship with the 3.0.0 version bump or as a patch on 3.0.0? §10.4 says
   the bump happens "together with W1-W6", which leaves the separately committed pin rule
   carrying no version of its own; the repository cannot settle whether that is intended.
4. Unchanged from round 4: whether an empty `ponytail.targets.hermes` is a valid manifest
   state, and whether Codex finding `plan-versioning-semver` by description alone suffices.

Reviewed by Fujiko, round 5, read-only.

---

## Marikos Gegenprüfung und Umsetzung (2026-11-23)

Der zentrale Befund ist berechtigt und meine §10-Prämisse war falsch. Gegenprüfung:
- `skills/brownfield-feature-planning/references/kanban-phase-release.md:32` verlangt tatsächlich `required skill`, `:49` prüft `skill`; `planner.SOUL.md.template:78` schickt den Planner in dieses Verfahren. Jack hat seine Prozedur befolgt, nicht improvisiert.
- Substitution gemessen (Kopie): Änderung an `:32`/`:49` ohne Testanpassung → genau 1 Fehlschlag in `test_brownfield_planning` (19 Tests); mit neu gefasster Assertion → 19 `OK`.
- `session_kanban.py:386-388` und `integrations.md:139` wie im Bericht; 148 Karten über 19 Board-Datenbanken, keine offene Karte mit `skills`.

| Befund | Umsetzung | Stand |
|---|---|---|
| §10 ohne die tragende Maker-Anweisung, Kausalaussage falsch | §10 neu: Besitzklausel ist `kanban-phase-release.md:32`/`:49`, Planner-SOUL bleibt unverändert, §10.1 nennt Verfahren und fehlende Einschränkung | korrigiert |
| §10.2-Block nicht bytegenau, hätte `:816` rot gemacht | SOUL wird gar nicht mehr editiert; Änderung sitzt im Release-Verweis, `:308` neu gefasst | korrigiert |
| Verweis auf nicht existierende §9.5-Messung | durch die Messung selbst ersetzt (19 Datenbanken, 148 Karten) | korrigiert |
| `plan-versioning` statt `plan-versioning-semver` | korrigiert | korrigiert |
| Rollback-Zweck verdreht | korrigiert: Pin-Regel ohne Coder-Rollenwechsel rückholbar | korrigiert |
| keine Abnahmezeile, kein DoD-Punkt | §5-Zeile und §8-Punkt 6 ergänzt | korrigiert |
| §9.2 `:336` „on which revision" mehrdeutig | „the exact commit it ran against" | korrigiert |

Neu gemessen nach der Korrektur: §9.2 8.469 B unrendered, 8.280 B / 69 Zeilen gerendert; `Review handoff` 612 B. Plan 65.166 B, `git diff --check` sauber.
