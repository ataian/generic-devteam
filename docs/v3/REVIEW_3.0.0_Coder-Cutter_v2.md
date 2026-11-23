# REVIEW — Maker-Plan `PLAN_devteam_v3_codercutter.md`, Runde 2 (Coder-Cutter)

Reviewer: Fujiko (independent, review-only; one-shot run in profile `fujiko`, model `deepseek/deepseek-v4.1-flash-1017`, reasoning high, tools `file,terminal`, read-only)
Date: 2026-11-23 (CET)
Review object: `docs/v3/PLAN_devteam_v3_codercutter.md`, sha256 `4d8aab9a24c026ea34835efe72f5b81aa6386dbe43ed8370674eae5e44506f55`
Round-1 report reviewed alongside: `REVIEW_3.0.0_Coder-Cutter_v1.md`, sha256 `4a663f75…15da7`
Frozen state: HEAD `b5ced6be25d34350830f55f1b181e0e262cde0d1`; `git status --short` = `?? docs/v3/` at handover and before the verdict
CAC criterion: the three CAC references read in full again

**VERDICT: CHANGES REQUIRED** — nine of thirteen round-1 findings resolved, F6/F8/F13 partially, plus thirteen new findings from the correction itself. Four are structural: an unsatisfiable acceptance row, a consequence list still missing eight test sites, static checks stated backwards, and two "reassigned" duties without a receiving surface.

---

## Reviewer report (verbatim)

EXACT REVIEWED STATE

  At handover
    HEAD            b5ced6be25d34350830f55f1b181e0e262cde0d1 (branch develop)
    git status      ?? docs/v3/
    plan sha256     4d8aab9a24c026ea34835efe72f5b81aa6386dbe43ed8370674eae5e44506f55
    review sha256   4a663f756acdb113c5fbd59a0fb2a470de2af3ad0defc74625c0faeda0315da7

  Immediately before this verdict (re-run, identical; git diff --stat empty)
    HEAD            b5ced6be25d34350830f55f1b181e0e262cde0d1
    git status      ?? docs/v3/
    plan sha256     4d8aab9a24c026ea34835efe72f5b81aa6386dbe43ed8370674eae5e44506f55
    review sha256   4a663f756acdb113c5fbd59a0fb2a470de2af3ad0defc74625c0faeda0315da7

  My measurements (render_text.render_role, role "coder", fixture bindings of
  test_render_reasoning.py:58-73; no file written; the §9.2 block was extracted
  in memory from plan lines 277-339)

    Baseline templates/roles/coder.SOUL.md.template
      19,652 bytes, 140 lines (wc -l and splitlines agree; file ends with \n)
      140 lines, 19,652 bytes  -> matches plan claim exactly
    §9.2 text, unrendered
      7,419 bytes, 63 lines    -> bytes match plan claim exactly
    §9.2 text, rendered
      7,248 bytes, 63 lines (wc-equivalent 63 newlines; 64 only if you count
      the empty string after the final newline)
      -> bytes match plan claim exactly; plan's "64 lines" is one too many
    14 placeholders, identical to manifest.role_templates.coder.render_fields
    {{DEMO_PASSWORD}} x1; `demo-handover` x1; "The customer owns product scope" x1
    Rendered ```sh block: bash -n clean; byte-identical flags to baseline:36-70

VERDICT: CHANGES REQUIRED

  The correction is substantially successful: F1, F2, F4, F5, F7, F9, F10, F11
  and F12 are genuinely fixed and I verified the invocation reproduces the
  2.14.4 baseline. Three problems block approval, none of them cosmetic:
  the §5 acceptance row now claims a property the plan's own non-goals make
  impossible (§5:198), the §9.6 static checks are stated backwards for all
  eleven needles, and §9.1 declares two rules "reassigned to Team-Codex" while
  no artifact on any surface receives them. The consequence list §9.5 was
  extended for still misses eight deterministic test sites, one of which W4
  names explicitly ("diagnosing-bugs tests").

ROUND 1 FINDINGS

F1  RESOLVED (BLOCKING -> closed)
    §9.2:299-308 restores the ```sh fence with both forms:
      "{{CODEX_BINARY}} exec --model MODEL_ID --sandbox danger-full-access \
       -c model_reasoning_effort='\"REASONING\"' --json -o RESULT_FILE - < PROMPT_FILE"
      "{{CODEX_BINARY}} exec resume --model MODEL_ID -c sandbox_mode='\"danger-full-access\"' \
       -c model_reasoning_effort='\"REASONING\"' --json -o RESULT_FILE SESSION_ID - < FOLLOWUP_PROMPT_FILE"
    Verified against baseline:36-70: every flag, both environment bindings,
    PONYTAIL_DEFAULT_MODE=full, --model in both forms, --sandbox in the fresh
    form, -c sandbox_mode only in the resume form, --json, -o, the trailing
    "- < PROMPT_FILE" / "SESSION_ID - < FOLLOWUP_PROMPT_FILE". The
    model_reasoning_effort literal is byte-identical to the template
    (grep -o: 2 occurrences in each file, same string including the backslashes).
    §9.2:299 restores background=true, pty=true, workdir; §9.2:310 restores
    "Read the final message from `RESULT_FILE`; the event stream is not the result."
    bash -n on the rendered fence: no syntax error.

F2  RESOLVED
    §9.2:282: "The customer owns product scope and external permissions;
    {{PLANER_NAME}} obtains missing customer decisions and maintains authorized
    plan amendments." Matches baseline:7 and §1's matrix row "Planner / customer"
    (plan:23). Planner SOUL:8 customer-approval requirement is no longer
    contradicted.

F3  RESOLVED (judged as the decided variant, not my proposal)
    §9.2:323: "On a released demo handover card, read the `demo-handover` skill.
    Its demonstration user's password is `{{DEMO_PASSWORD}}`, supplied only
    through the environment variable the script documents, never as an argument
    and never on a card."
    §9.3:362: "The demonstration user's password stays in the role instructions;
    this skill carries the runtime procedure."
    Is the split complete? Yes. Owner per step (baseline:78):
      - permanence/max-one/reviewed-commit      -> skill bullet 1
      - replace = retire + ownership proof + gone check -> skill bullet 1
      - preserve review evidence/unrelated      -> skill bullet 1
      - documented teardown verb, no hand-built removal -> skill bullet 2
      - start at reviewed commit                -> skill bullet 3
      - create user (documented verb)           -> skill bullet 4
      - password value + channel (env var, never argument/card) -> SOUL:323
      - seed data                               -> skill bullet 5
      - record commit/URL/login/data command    -> skill bullet 6
    No step is unowned on either surface, and the two surfaces cross-reference
    each other by name, so a fresh Coder loading the skill in the SOUL's
    context recovers the value, the channel and the verb. "never on a card" is
    a new clause, but it is a guard consistent with planner SOUL:75 and needed
    now that the literal is resident; it is not a widened permission.
    One residual: the skill says "(`demo.sh user` or equivalent)" where
    baseline:78 named the literal `demo.sh user` — see N12.

F4  RESOLVED
    §9.2:319 capability: "record the actual error and work state; diagnosing the
    failure stays allowed. Then `kanban_block(kind=\"capability\", reason=...)`.
    No model switch, no replacement card." — no TIMER, matching baseline:101.
    §9.2:320 transient: "record the original error, reset date/time/zone or
    uncertainty and the remaining work, then `kanban_block(kind=\"transient\",
    reason=...)` and one TIMER request to {{PLANNER_PROFILE}} through
    `kanban_create`, naming board, task, reset or uncertainty and the requested
    one-time resume." — classification, TIMER content and the timed resume all
    match baseline:102. The two routes are no longer merged.

F5  RESOLVED (with a delivery dependency on N2)
    §9.5:402 adds the cues to templates/team-codex-AGENTS.md, which is the only
    Codex instruction surface (integrations.md:95: delivered as
    `$CODEX_HOME/AGENTS.md`). §2.2's diagnosing-bugs row still reads "Keep with
    Team-Codex; remove mandatory Coder invocation/independent diagnosis" and
    §5:193 still claims Codex "retains SemVer/changelog rules and
    `build-evidence`/`diagnosing-bugs`". The re-homing is real. The tests that
    assert the old cues still need their disposition — see N2.

F6  PARTIALLY RESOLVED
    §9.5 was extended, but the following break deterministically and are not
    listed. All strings below are read from the file; all are absent from §9.2.
      references/test_diagnosing_bugs.py:189-210 — seven required strings in the
        rendered Coder text, e.g. "Validate diagnosis against the original
        symptom and actual evidence; do not automatically repeat the full
        method." and "Never use `kanban_complete` to close your own
        implementation." The file is not named in §9.5 at all, although W4
        names "the existing renderer, update-team, build-evidence and
        diagnosing-bugs tests".
      test_render_reasoning.py:186-200 — six of eight asserts fail (reasoning
        default sentence, "if both are HIGH, use `high`.", the six VoltAgent
        sentence, "Read `model` from ...", "Keep the configured model and
        provider.", the thread_id sentence). §9.5 does not list :186-200.
      test_render_reasoning.py:205-215 — six of six fail ("One primary Codex
        session per implementation task.", "Record its session id on the card.",
        "Create a new session only when continuation is impossible or the card
        records the reason.", "Evaluate results at task-level boundaries...").
        Not listed.
      test_render_reasoning.py:294-305 — requires the full worker-guard sentence
        including "and run it, or use the file tools"; §9.2:311 says only
        "Write a script file." Not listed.
      test_render_reasoning.py:307-318 — the VoltAgent test asserts five
        sentences that §9.1 deliberately removed; the test needs deletion or
        inversion. Not listed.
      test_update_team.py:282-285 — "Keep card and Coder assignment.", "The
        existing subscription wakes `fixture-planner` for customer
        coordination.", "Send one TIMER request to `fixture-planner`" all fail
        against §9.2:318/320 ("keep card and assignment", "the subscription
        wakes {{PLANER_NAME}}", "and one TIMER request to ..."). Not listed.
      test_update_team.py:1004-1007 — installs and asserts build-evidence in
        (`'coder', 'skills'`); §2.2 removes Coder from build-evidence. Not listed.
      test_build_evidence.py:72 — "the reference owns selector derivation and
        the isolation-checker limit" is gone from §9.2; only :71 is listed.
    Also the two dispositions that are listed but wrong are contained in N2/N6.

F7  RESOLVED (with a wording regression, N9)
    §9.2:321 restores the development/demo authority ("Start, stop, restart,
    rebuild, recreate, generate synthetic data and reset disposable state for
    development tests without further customer approval; respect existing
    boundaries on source ownership, operational data, host administration,
    shared infrastructure and external effects. Running from source grants no
    deployment authority"); §9.2:291 restores the branch check ("return the card
    to {{PLANER_NAME}} if either check fails. Never create, rename or rebase
    that branch."); §9.2:322 restores the local-input/worktree rule; §9.2:332
    restores "stop if changes cannot be separated safely". All four were the
    round-1 asks.

F8  PARTIALLY RESOLVED
    Bytes are now exact on all three figures I re-measured: baseline 19,652 B /
    140 lines, §9.2 unrendered 7,419 B, rendered 7,248 B. The line count is not:
    the text renders to 63 lines, not 64. The wrong figure is repeated in
    §9.2:272, §4/W1:135 and the acceptance row §5:197 — see N11.

F9  RESOLVED
    §9.2:318: "`kanban_comment` with `Question:`, `Why it matters:` and the
    paused work, adding facts, options and a recommendation when the choice is a
    decision". "paused work" is unconditional as in baseline:103; options and
    recommendation are conditional again.

F10 RESOLVED
    The disposition is now correct rather than a rewrite: §9.2:274 keeps all 14
    fields including DEMO_PASSWORD, §9.5:393 says "`role_templates.coder.render_fields`
    stays unchanged (the password literal remains)", §9.5:398 keeps the
    three-role validation test "unchanged", §9.5:403 keeps native-workflow.md:28
    — which I verified reads "| `DEMO_PASSWORD` | ... all three roles; kept only
    in private team state |" (native-workflow.md:28). Planner and Reviewer
    templates both still contain {{DEMO_PASSWORD}} (planner:75, reviewer:85).

F11 RESOLVED
    The fence is back. render_text.py:110-118 sets shell=True for ```sh and
    :99-100 shlex-quotes CODEX_BINARY / CODEX_PROCESS_HOME / CODEX_HOME inside
    it; the rendered block shows the substituted paths inside the fence, so
    setup.md:235's reliance ("Pass raw absolute paths for shell quoting in the
    invocation block") holds again.

F12 RESOLVED
    §9.4:387: "its bindings are render fields, and `references/setup.md` copies
    own skills with unchanged bytes, so the process home, the sandbox flag and
    the allowlisted binary would be dropped, not relocated." I verified
    setup.md:229 ("Keep names and bytes unchanged except the recovery launcher")
    and that skills carry no placeholders (`grep -rn '{{' skills/` finds only
    the recovery launcher). The argument now rests on the correct mechanism.
    The arithmetic also closes: the §9.4 §9.2 column (915/783/1781/2313/576/817/145)
    plus a uniform 3-byte header allowance plus the 68-byte title line equals
    7,419 exactly.

F13 PARTIALLY RESOLVED
    Restored: "Apply existing requirements and customer decisions without asking
    again." (§9.2:283); "Do not repeat a failed approach unchanged" (§9.2:312);
    "The decision stands for the round" (§9.2:317) and "verify the recipient"
    (§9.2:318); Hindsight scope filter and "Keep credentials, raw code and
    transient logs out of memory" (§9.2:334).
    Still lost, and named in neither §9.1 nor §9.2 (see N7): baseline:113
    ("Actual state: live branch, code, tests. Required state: ... Memory
    overrides neither. Ticket edits alone do not update an active worker's
    baseline."), baseline:114's write side ("Save role tooling experience under
    `role:coder`. Promote only verified durable project facts to `scope:shared`."),
    baseline:93 (customer caps/quota/failure-loop guards), baseline:107 ("Tool
    and system prohibitions remain binding.").
    And the fifth item (persisted value-set/enum/schema verification) was
    "reassigned" per §9.1:266 without a receiving surface — see N4.

NEW FINDINGS

N1  BLOCKING/MAJOR? -> MAJOR — §5:198 (acceptance row) contradicts planner:74-75
    and reviewer:85, which §7 forbids touching.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:198
    Quote: "The runtime procedure exists once, in `demo-handover`, installed in
    the Coder home and discoverable there; the SOUL carries the pointer and the
    password literal, and no lifecycle or teardown text."
    Repository: templates/roles/reviewer.SOUL.md.template:85 keeps the full
    lifecycle sentence ("a demonstration runtime is not permanent; at most one
    exists ... a stopped runtime is not a retired one. Preserve review evidence
    and unrelated resources.") plus the login check; planner.SOUL.md.template:74
    keeps the teardown verb and "a stopped runtime is not a retired one";
    planner:75 keeps the demo card and the password rule.
    Reason: "exists once" is unsatisfiable without editing Planner/Reviewer
    SOULs, which §7:216-217 and §5:196 declare unchanged. §9.5:400 even relies
    on the Reviewer copy surviving (the coder/reviewer loop must be split, not
    deleted). An implementer following §5 literally must either fail the row or
    break a non-goal.
    Replacement: "After the Coder-side move, `demo-handover` carries the runtime
    procedure for the Coder; it is the only Coder surface that does. The Planner
    and Reviewer keep their own condensed clauses unchanged (§7)."

N2  MAJOR — §9.5's consequence list is still incomplete; eight deterministic
    test sites and two wrong per-site dispositions.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:394-401
    Quote: "`references/test_render_reasoning.py`: :82–:105 ... :125–:130 ...
    :140–:165 ... :180–:183 ... :966–:985 and :1082–:1095" (no other test file
    beyond build-evidence:71 and update_team:410-427/:1010)
    Missing, all verified in the repo: test_diagnosing_bugs.py:189-210 (7/7
    asserts fail); test_render_reasoning.py:186-200 (6/8), :205-215 (6/6),
    :294-305, :307-318 (5/5); test_update_team.py:282-285 (3/4),
    :1004-1007; test_build_evidence.py:72.
    Wrong dispositions inside §9.5:
      - :397 "the `demo.sh user` password assertion stays in the Coder SOUL" —
        the asserted string is "create the demonstration user via `demo.sh user`
        with the password `Example` supplied only from private team state
        through the environment variable the script documents, never as an
        argument"; §9.2:323 says none of "demo.sh user", "from private team
        state" and words the sentence differently. It cannot stay unchanged.
      - :396 ":125–:130 ... that test must read §9.2's `Delegate` block instead"
        — the asserted sentence "When Codex needs the development environment,
        include its agent-guide path and the development-runtime authority from
        Exception routing." exists nowhere in §9.2 (see N6).
    Reason: §5:228 requires the suites to pass and W4:160 names the
    diagnosing-bugs tests explicitly. As written the plan produces a knowingly
    red suite, which is exactly the F6 defect F6 was meant to close.
    Replacement: make §9.5 a table — site | assertion | disposition (move to
    skill / invert to assert absence / rewrite to §9.2 wording / delete with
    named reason) — and include the eight sites above, plus split
    test_update_team.py:419 so the reviewer half stays.

N3  MAJOR — §9.6's static checks are stated backwards for all eleven needles.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:407
    Quote: "Static checks on the rendered Coder SOUL, each zero in 2.14.4 and
    zero in 3.0.0: `Inspect the actual diff`, `build-evidence`,
    `$diagnosing-bugs`, `six VoltAgent`, `Maintain the project changelog`,
    `analysis integration`, `consumer per changed symbol`, `harness repair`,
    `Hindsight bank`, `Stage only`, `a demonstration runtime is not permanent`."
    Measured (rendered 2.14.4 template vs rendered §9.2): every needle occurs
    exactly once in 2.14.4 and zero times in 3.0.0:
      'Inspect the actual diff' 1/0   'six VoltAgent' 1/0
      'build-evidence' 1/0            'Maintain the project changelog' 1/0
      '$diagnosing-bugs' 1/0          'analysis integration' 1/0
      'consumer per changed symbol' 1/0   'harness repair' 1/0
      'Hindsight bank' 1/0            'Stage only' 1/0
      'a demonstration runtime is not permanent' 1/0
    Reason: a check that asserts zero in the baseline as well proves nothing; a
    verifier applying §9.6 literally must report failure against 2.14.4. This is
    the same class of defect as F8 (a verification claim not reproducible from
    the repository) and it survived the rewrite.
    Replacement: "Static checks on the rendered Coder SOUL: each string occurs
    once in the 2.14.4 render and zero times in the 3.0.0 render: ..."

N4  MAJOR — §9.1:266 reassigns two rules to Team-Codex, but no surface receives
    them.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:266
    Quote: "Two rules are **reassigned rather than restored**: \"Record one
    failing run of a new test before the production change\" and \"For persisted
    value-set, enum, schema or outbound-mapping changes, verify stored data and
    every export path\" become Team-Codex duties, because the Coder no longer
    runs or reads implementation evidence."
    Repository: templates/team-codex-AGENTS.md is eight lines with four bullets
    (Task / Resume / Children / Result) and contains neither rule; §9.5's only
    Codex-surface item (:402) adds skill cues only. No §9.5 item touches a Codex
    instruction text otherwise.
    Reason: this is the F5 failure mode reproduced inside the correction — a duty
    is declared moved and then exists on no surface. CAC authoring contract:12
    ("Keep durable authority in the role instructions; put a procedure at its
    existing point of use") and SKILL.md:60 (a pointer must resolve for its
    recipient). §5:193 also does not claim them, so the loss is silent.
    Replacement: add one §9.5 item — "templates/team-codex-AGENTS.md gains the
    two reassigned duties verbatim: 'Record one failing run of a new test before
    the production change.' and 'For persisted value-set, enum, schema or
    outbound-mapping changes, verify stored data and every export path.'" — and
    extend §9.6 with a positive check on the installed AGENTS.md.

N5  MAJOR — §9.2:312 assigns harness repair back to the Coder.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:312
    Quote: "Do not repeat a failed approach unchanged; a failing harness is a
    setup defect, so fix its cause once, and two rounds of harness-only findings
    park the card."
    Contradicts: §1:24 ("Coder stages files, inspects staged diff, ... runs/chooses
    test matrices and repairs test harnesses" -> §2.1:48 "Move productive Git,
    testing and harness work to Team-Codex"), §3.1:87 ("Let Codex complete
    analysis, coding, test strategy, tests ... Hermes does not duplicate these
    steps"), §2.1:46 ("Remove Coder skill-selection and validation duties").
    Impersonals in a SOUL bind the role that reads it; "fix its cause once" is
    the Coder repairing a harness. The sentence also lost baseline:96's block
    kind ("park it with `kanban_block(kind=\"capability\", reason=...)`"), so
    "park the card" names no verb. CAC notation §1: "Compression must not create
    ambiguity."
    Replacement: "... Do not repeat a failed approach unchanged; a failing
    harness is a setup defect, so direct Codex to fix its cause once. After two
    rounds of harness-only findings, `kanban_block(kind=\"capability\", reason=...)`
    and record the defect, command and smallest next step."

N6  MAJOR — the Codex brief loses the agent-guide path, and §9.5 disposes its
    test as merely re-pointed.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:292 vs baseline:26
    Baseline: "When Codex needs the development environment, include its
    agent-guide path and the development-runtime authority from Exception
    routing." §9.2 has no equivalent: :292 says only "Pass the original task
    with its binding references and limits"; :321 grants the Coder's own runtime
    authority without telling it to hand the guide path to Codex.
    Test impact: test_render_reasoning.py:125-130 will be rewritten per §9.5:396
    to read the "Delegate" block, but the string it asserts does not exist
    there. §9.5 therefore cannot be implemented as described.
    Reason: the instruction has a real function (Codex must find the project's
    build/run commands), and its removal is listed in neither §9.1 nor §9.2.
    Replacement (one clause in §9.2:292): "Pass the original task with its
    binding references and limits, including the project agent-guide path when
    Codex needs the development environment; brief under 4 KB, pointing to the
    exact plan revision."

N7  MINOR — residual 2.14.4 losses, unlisted in §9.1, not covered by §9.2.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:283 / :297 / :334
    (a) baseline:107 "Tool and system prohibitions remain binding." — absent,
        although test_render_reasoning.py:105 asserts it and §9.5:395 implies it
        is "a differently worded bullet".
    (b) baseline:93 "Preserve explicit customer financial/resource caps,
        configured limits, provider quotas, operational permissions, and native
        failure-loop guards." — absent; §9.2:297 covers reasoning limits only.
    (c) baseline:113 "Actual state: live branch, code, tests. Required state:
        exact accepted plan revision and contracts. Memory overrides neither.
        Ticket edits alone do not update an active worker's baseline." — absent.
    (d) baseline:114 "Save role tooling experience under `role:coder`. Promote
        only verified durable project facts to `scope:shared`." — absent.
    (e) baseline:83 "if both are HIGH, use {{CODEX_REASONING_MAX}}" is reduced to
        "HIGH complexity or impact may raise to {{CODEX_REASONING_MAX}}"
        (MUST->MAY), and baseline:85 "Higher reasoning grants no product
        authority." is absent.
    Reason: (e) is an obligation-strength change (CAC notation §1 "Preserve ...
    obligation strength"; authoring contract:10); (a)-(d) are guards §5:197
    promises do not disappear and §3.4:121-124 says stay binding.
    Replacement: restore (e) in :297 ("if both are HIGH, use
    {{CODEX_REASONING_MAX}}; higher reasoning grants no product authority") and
    add one sentence to :321/:334 carrying (a) and (b); state (c) and (d) in
    §9.1 as accepted removals if Max removes them deliberately.

N8  MINOR — §9.2:283's decision list diverges from §3.2 and repeats "contracts".
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:283
    Quote: "Decide only what Codex cannot: accepted goal and contracts, security,
    privacy, data integrity, permissions, cost, external contracts."
    §3.2:96 says "... accepted goal and contracts, security/privacy/data
    integrity, interoperability, cost and permissions". "interoperability" is
    replaced by "external contracts" (not the same set), and "contracts" appears
    twice in one list. Baseline:8 additionally carried "agreed function,
    essential usability, explicit requirements".
    Reason: CAC notation §1 ("Remove ... repeated context"; "Preserve ...
    scope"); the mismatch is a §9.2-vs-§3.2 divergence.
    Replacement: "Decide only what Codex cannot: accepted goal, contracts and
    interoperability, security, privacy, data integrity, permissions,
    interoperability, cost." -> better, deduplicated: "accepted goal and
    contracts, interoperability, security, privacy, data integrity, permissions
    and cost."

N9  MINOR — §9.2:321's wording breaks the cross-role identity property.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:321
    Quote: "Start, stop, restart, rebuild, recreate, generate synthetic data and
    reset disposable state for development tests without further customer
    approval"
    planner.SOUL.md.template:12 and reviewer.SOUL.md.template:84 read "Start,
    stop, restart, rebuild, recreation, synthetic data generation and reset of
    disposable state ...". test_render_reasoning.py:100 asserts
    `len(set(paragraphs)) == 1`, i.e. all three roles say the same thing.
    §9.5:395 acknowledges only that the check "must be re-derived" — but the
    property, not the assertion, is what guards against authority drift.
    Reason: gratuitous divergence in a sentence the plan elsewhere calls
    identical across roles.
    Replacement: use planner:12's exact sentence in §9.2:321, keep the
    cross-role identity assertion.

N10 MINOR — §9.5 omits two §2.2-mandated target removals.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:393
    Quote: "`own_skills.plan-versioning-semver` loses `coder` ...;
    `build-evidence` and `screenshot-to-code` lose `coder`"
    Missing: `upstream_components.ponytail.targets.hermes` is ["coder"] today
    (manifest.json:475ff) and §2.2:68 says "Remove Hermes Coder; retain
    Team-Codex" — leaving hermes empty; `upstream_components.codebase-memory`
    and `graphify` targets.hermes are ["planner","coder","reviewer"] and §2.2:69
    requires removing the Coder's binding. upstream-sources.md:103 still reads
    "Hermes Coder and Team-Codex" for ponytail, and
    test_render_reasoning.py:982-984 pins the two analysis components' targets.
    Reason: the manifest bullet presents itself as the complete target delta;
    an implementer working from §9.5 alone leaves §2.2 half-done and
    upstream-sources.md:103 wrong. (MINOR because §2.2 states the requirement;
    the consequence list is what is incomplete.)
    Replacement: add "`ponytail.targets.hermes` loses `coder` and becomes empty;
    `codebase-memory`/`graphify` lose `coder` per §2.2; update
    `references/upstream-sources.md:103` and the analysis rows."

N11 MINOR — the rendered text is 63 lines, not 64.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:272 (also :135, :197)
    Quote: "7,248 bytes and 64 lines rendered with the repository fixture
    bindings"
    Measured: 7,248 bytes exactly; 63 lines by splitlines and by newline count
    (64 only when counting the empty element after the trailing newline). The
    baseline is 140 by the same counting rule, so the two figures are not
    measured the same way.
    Reason: §5:197 is an acceptance row; the earlier round rejected exactly this
    kind of unreproducible figure (F8).
    Replacement: "7,248 bytes and 63 lines rendered (2.14.4: 19,652 bytes, 140
    lines)".

N12 MINOR — the demo skill softens an exact command literal.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:367
    Quote: "Create the demonstration user through the project's documented verb
    (`demo.sh user` or equivalent)."
    baseline:78 said "create the demonstration user via `demo.sh user` with the
    password ... never as an argument" — the literal and no alternative. The
    "or equivalent" phrasing belongs to the teardown verb (where the guard, not
    the verb, is the point), and copying it here widens what the Coder may run.
    Reason: CAC notation §1 "Keep ... commands ... exact"; authoring contract:10
    ("Keep exact commands ... literals"). §9.6:409 also retains a `demo.sh user`
    expectation.
    Replacement: "Create the demonstration user via `demo.sh user`, or the
    project's documented equivalent when it has one, supplying the password only
    through that verb's documented environment variable."

N13 MINOR — the new line widens templates/team-codex-AGENTS.md's declared scope.
    Location: docs/v3/PLAN_devteam_v3_codercutter.md:402
    Quote: "`templates/team-codex-AGENTS.md`: gains one line placing the skill
    cues where they now belong — `$diagnosing-bugs` for unexplained failures or
    regressions, `$build-evidence` for build-, browser- or process-dependent
    evidence in the named mode, `plan-versioning-semver` for version, changelog
    or API-contract changes."
    Repository: templates/team-codex-AGENTS.md:1 "# Team-Codex communication";
    its opening paragraph is a writing rule and its four bullets are Task /
    Resume / Children / Result, all about message form. The file is delivered as
    `$CODEX_HOME/AGENTS.md` (integrations.md:95) and compared as an ordered
    payload layer (integrations.md:118).
    Contradiction? No — nothing in the four bullets conflicts with a skill
    instruction, and the proposed line does not restate the existing
    "Independent review belongs to the designated Reviewer."
    Defect: the file identifies itself as the communication contract; adding a
    delivery rule without adjusting that identity leaves a header that
    misdescribes its content, and §9.5 says nothing about the payload readback.
    Replacement: retitle to "# Team-Codex instructions" (or add a "## Skills"
    heading) and note in §9.5 that integrations.md:118's payload comparison is
    re-derived from the template, not from a stored fixture.

  Explicit no-finding lines

    B1 new duplication — no finding. Inside §9.2 no rule is stated twice: the
    only repetition is the independence clause at :282 ("You approve neither
    your own implementation nor its completion") paired with :327 ("never
    `kanban_complete` on your own implementation"), which is the same split the
    baseline carried (template:7 + template:76) and serves a different act.
    Across surfaces: the development/demo authority paragraph also stands in
    planner:12 and reviewer:84, but each role needs its resident operational
    authority (authoring contract:12) and test_render_reasoning.py:100 asserts
    the agreement — unchanged from round 1. The Coder's remaining skills are
    `hermes-codex` (whose syntax §9.2:299 explicitly does not duplicate),
    `demo-handover` (procedure only, cross-referenced at :362) and Hindsight.
    No §9.2 rule is restated in a skill the Coder loads.

    B2 new contradiction — findings N1 (against §5:198) and N8 (against §3.2);
    no finding otherwise. Checked and consistent: §1's matrix (customer owns
    scope, Coder decides within limits, runtime operations under existing
    scope), §3.1 items 1-7, §5:187-195 and the negative assertion at §5:200,
    §7:216-221, and §9.1/§9.4's own removal statements (reasoning caps, both
    invocation forms, worker guard, harness stop rule all remain present;
    `ponytail` and the "six VoltAgent" catalogue are absent as §9.1 declares).

    B3 baseline-unsupported text — findings N5 and N12; no finding otherwise.
    The sh block is byte-identical to baseline:36-70 in every flag and literal
    (verified per flag and by string comparison of the
    model_reasoning_effort arguments), `bash -n` passes, both forms are present
    and distinguishable, and all 14 placeholders are legal for role `coder`
    (render_text.py:16-21). No render field is invented or dropped. §9.2:285's
    "never change your own `command_allowlist`" is baseline:12 verbatim;
    :291 "return the card to {{PLANER_NAME}}" is baseline:22; :322 the
    local-input rule matches baseline:21 sentence for sentence.

    B4 CAC padding — finding N8 (the repeated "contracts"); no further padding.
    I applied the contract's test ("drop it and does the action, actor,
    condition or exit change?") to every sentence. §9.2:277-339: headings are
    minimal; :290 "Clarify conflicting bindings." carries baseline:124's stop
    rule; :293 the labeled result is a required output contract; :310 the
    literal-substitution sentence prevents an invented MODEL_ID; :321 is long but
    guard-dense (each clause restores a distinct permission or prohibition);
    :335 is the one-line Communication residue §9.1:264 promises. No sentence
    can be deleted without losing an action, actor, condition or exit.
    Audience rule respected: every sentence is team-internal technical English;
    nothing addresses the customer, and no role-owned human text is compressed
    (§9.3's frontmatter/trigger is agent-facing).

    B5 demo skill vs baseline step 13 — no unowned step. Owner table is in F3
    above. The only split point is the password: value and channel in the SOUL
    (:323), creation verb in the skill (bullet 4), mutual cross-reference at
    §9.3:362 and §9.2:323. A Coder reading either surface alone would be
    incomplete, but the SOUL is always resident, so the procedure is recoverable
    for the role that must act. The remaining gap is the softened literal — N12,
    not an ownership gap.

    D consequence list — findings N2, N4, N10, N13. Item-by-item against the
    repository:
      manifest.json:3 version, own_skills.demo-handover, files, render_fields,
      plan-versioning-semver, build-evidence, screenshot-to-code, :201, :252 —
      all real and correctly located (I read :201 and :252: they do assert
      "Coder passes the literal `$build-evidence` cue" and "Coder explicitly
      invokes and validates results").
      test_render_reasoning.py:82-105 — real; :82-99 loop and :100 identity both
      break (see N9 for the cause).
      :125-130 — real location, wrong disposition (N6).
      :140-165 — real (the method starts at :139); :158's coder assertion cannot
      stay unchanged (N2).
      :180-183 — real and correctly dispositioned: the three-role password test
      at :166-175 and the rejection test at :177-188 are both satisfied by
      §9.2:323, because {{DEMO_PASSWORD}} is a LITERAL_FIELD
      (render_text.py:26) and appears once.
      :966-985 — real: the exact-target dict includes build-evidence hermes
      ["coder","reviewer"], plan-versioning-semver ["planner","coder"],
      screenshot-to-code ["planner","coder"], and has no demo-handover.
      :1082-1095 — real: the upstream-sources rows "Planner and Coder" /
      "Planner, Coder and Team-Codex" and the code-analysis rows.
      test_update_team.py:410-427 — real (the password loop is :415-418, the
      lifecycle loop :419-422, `demo.sh retire` :423, `demo.sh user` :424); needs
      the coder/reviewer split.
      test_build_evidence.py:71 — real; :71's string must be rewritten because
      the moved cue no longer says "require the literal"; :72 also breaks.
      test_update_team.py:1010 — real ("$build-evidence" in the installed Coder
      SOUL).
      setup.md:230 — real; it enumerates the Codex targets by name
      ("currently `screenshot-to-code`, `diagnosing-bugs` and `build-evidence`").
      setup.md:257 — real ("Check `$diagnosing-bugs` routing ...").
      native-workflow.md:28 — real and must stay: "all three roles; kept only in
      private team state".
      team-codex-AGENTS.md — real file, eight lines, no contradiction with its
      four bullets (N13 is about its stated purpose, not its content).

VERIFIED CLAIMS

  - Both sha256 values and HEAD are identical at handover and before the
    verdict; `git status --short` is `?? docs/v3/` both times; `git diff --stat`
    is empty; nothing in the plan is implemented.
  - Baseline templates/roles/coder.SOUL.md.template: 19,652 bytes, 140 lines
    (wc -l), ends with a newline; matches the plan.
  - §9.2 (plan lines 277-339) unrendered 7,419 bytes; rendered with the
    test_render_reasoning.py:58-73 fixture bindings 7,248 bytes, 63 lines.
    Section bytes rendered: Role and authority 918, Delegate 786, Session 1,784,
    Blockers 2,316, Review handoff 579, Evidence/Git/memory 820, Project binding
    148, title 68 — the §9.4 table plus a uniform 3-byte heading allowance sums
    to 7,419.
  - Exactly 14 placeholders, equal to manifest.role_templates.coder.render_fields
    (14 entries, same names, verified by set comparison); no residual braces.
  - {{DEMO_PASSWORD}} occurs once; `demo-handover` occurs once in §9.2; "The
    customer owns product scope" occurs once. §9.6's positive checks hold.
  - Rendered ```sh block: `bash -n` clean; flags and literals byte-identical to
    baseline:36-70, including `-c model_reasoning_effort='\"REASONING\"'` (2
    occurrences per file, same bytes) and `-c sandbox_mode='\"danger-full-access\"'`
    only in the resume form.
  - §9.6's eleven static needles: each occurs exactly once in the 2.14.4 render,
    zero times in the §9.2 render — the plan's claim of "zero in 2.14.4" is
    false (N3).
  - manifest.json version 2.14.4; own_skills has no demo-handover and files has
    no demo path; ponytail/hindsight/codebase-memory/graphify live under
    upstream_components with the targets quoted in N10.
  - reviewer.SOUL.md.template:85 and planner.SOUL.md.template:74-75 still carry
    the demo lifecycle/teardown/password clauses (N1).
  - templates/team-codex-AGENTS.md is 8 lines / 1,524 bytes with four bullets
    (Task, Resume, Children, Result) and no technical-duty text (N4).
  - setup.md:229 "Keep names and bytes unchanged except the recovery launcher";
    setup.md:235 "Pass raw absolute paths for shell quoting in the invocation
    block" — both support F11/F12.
  - Reading discipline: the diff/text was read before the plan's own §9.7 table
    and the disposition table was then checked against §9.2 line by line; no
    §9.7 claim was accepted as evidence. One ephemeral file (/tmp/fence.out) was
    used solely to pipe the rendered fence into `bash -n` and was deleted
    immediately; nothing in the repository was created or modified.

OPEN QUESTIONS

  - Whether Codex accepts `-c model_reasoning_effort='"REASONING"'` as written
    (a literal backslash before each quote inside single quotes) cannot be
    settled here. It is identical to the shipped 2.14.4 baseline, so this review
    treats fidelity as the criterion; if the baseline literal is wrong, the plan
    correctly reproduces a pre-existing defect rather than adding one.
  - §9.4 says "Max approved 3.5–4 KB" while §4/W1 and the header speak of a
    `<= 5 KB` aim superseded by revision 2. The repository cannot settle which
    target Max actually set; the deviation argument is unaffected either way.
  - Whether the seven comments in test_diagnosing_bugs.py:189-210 were meant to
    be *deleted* or *inverted* (asserting the Coder no longer requires the cue)
    is a design choice for Max/Anjin; the plan needs to state one.
  - Whether Codex selects `plan-versioning-semver` from its description alone,
    or needs the explicit cue the plan now routes through AGENTS.md, remains a
    native-behaviour question the repository only partly answers.
  - Whether `ponytail` with an empty `targets.hermes` is a valid manifest state
    or needs removal from the Hermes matrix entirely: the manifest schema is not
    validated for emptiness in any test I found.

---

## Marikos Gegenprüfung (2026-11-23)

| Befund | Gegenprüfung | Ergebnis |
|---|---|---|
| N1 | `planner.SOUL.md.template:74-75` und `reviewer.SOUL.md.template:85` tragen die Demo-Regeln weiter, §7 schließt deren Änderung aus | bestätigt: „exists once" war unerfüllbar; Zeile neu gefasst |
| N2 | acht Teststellen gelesen (`test_diagnosing_bugs.py:189-210`, `test_render_reasoning.py:186-200/205-215/294-305/307-318`, `test_update_team.py:282-285/1004-1007`, `test_build_evidence.py:72`) | bestätigt; §9.5 ist jetzt eine Tabelle mit allen Stellen |
| N3 | alle elf Nadeln im 2.14.4-Render je einmal vorhanden, im §9.2-Render null | bestätigt: Prüfrichtung war umgedreht |
| N4 | `templates/team-codex-AGENTS.md` hat vier Bullets (Task/Resume/Children/Result), keine der zwei Regeln | bestätigt; Aufnahme in §9.5 |
| N5 | §2.1:48 und §3.1:87 verlagern Harnessarbeit zu Codex | bestätigt; Satz richtet sich jetzt an Codex |
| N8 | §3.2:96 nennt „interoperability", §9.2 führte „contracts" doppelt | bestätigt; Liste dedupliziert |
| N9 | `planner:12` und `reviewer:84` sind wortgleich; `test_render_reasoning.py:100` prüft diese Gleichheit | bestätigt; SOUL übernimmt den Planner-Wortlaut, Gleichheit nachgemessen: identisch |
| N11 | `wc -c -l` auf dem gerenderten Text: 8.107 B / 64 Zeilen | bestätigt; Zahlen im Plan entsprechend |

Nach der Korrektur: SOUL 8.297 B unrendered, 8.107 B / 64 Zeilen gerendert; die Development-Authority-Zeile ist bytegleich zu `planner:12`; alle elf Negativ-Nadeln fehlen; `DEMO_PASSWORD` genau einmal.

## Entscheidungen

| Befund | Umsetzung | Stand |
|---|---|---|
| N1 | Abnahmezeile auf „die einzige Coder-Fläche" umgestellt | korrigiert |
| N2 | §9.5 als Tabelle mit 21 Zeilen (Stelle / heutige Zusicherung / Verfügung) | korrigiert |
| N3 | Prüfrichtung korrigiert („einmal in 2.14.4, null in 3.0.0") | korrigiert |
| N4 | zwei abgegebene Regeln landen in `team-codex-AGENTS.md` | korrigiert |
| N5, N6 | Harness-Satz an Codex gerichtet; Agent-Guide-Pfad im `Delegate`-Block zurück | korrigiert |
| N7 | Werkzeug-/Systemverbote, Kundenobergrenzen, Reasoning-Pflichtstufe, Ist-/Soll-Zustand, Memory-Promotion zurück | korrigiert |
| N8, N9 | Entscheidungsliste dedupliziert; Development-Authority wortgleich zum Planner | korrigiert |
| N10 | `ponytail`- und Analyse-Targets in §9.5 | korrigiert |
| N11 | Zahlen neu gemessen (8.107 B / 64 Zeilen) | korrigiert |
| N12 | `demo.sh user` wieder als Literal | korrigiert |
| N13 | `team-codex-AGENTS.md` wird zu „# Team-Codex instructions" mit `## Skills`; Payload-Abgleich aus der Vorlage | korrigiert |

Eine dritte Runde ist auf diesem Stand noch nicht gelaufen.
