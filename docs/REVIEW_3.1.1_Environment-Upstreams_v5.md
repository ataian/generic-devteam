# Review — Environment upstreams Maker plan, v5

Reviewed input: `docs/PLAN_3.1.1_Environment-Upstreams_v5.md`
SHA-256 `b94f6dc2e3aae312c9b0cc29a0680f0ac8b40758af99aadaaa750a89f51f4f00` — computed and confirmed.
Baseline for the delta: `docs/PLAN_3.1.1_Environment-Upstreams_v4.md`
SHA-256 `b201d06a0c3397b0eb885da730f2513152937cba48d5c79c2252e881103b4a76` — confirmed.
Primary prior report: `docs/REVIEW_3.1.1_Environment-Upstreams_v4.md`
SHA-256 `2091a450ff8eb2ca5c212e50d37bff758b456d5c596f93f1a4e5e89dadb6e263` — confirmed.
Further evidence (not a second target): `docs/REVIEW_3.1.1_Environment-Upstreams_v1.md`
SHA-256 `103b8f8461cec2390434adb1ac67b32030bc90dd9dcd24a6de1f35e3e52b9e6f` — confirmed.
Maker root `4e2fe1e29c2050b8835fdb4a268e0ed14f29d410`; `git diff HEAD | sha256sum` =
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty, clean) — confirmed.
Upstream pins present and clean at the candidate's commits: `2c6331d1…` (disposable-demo), `3205d3a7…` (dev-environment).

## 0. Verdict

**CHANGES_REQUESTED** — one required correction, no blocker.

Both findings from the previous round are genuinely closed at their exact anchors, and the five v5 edits
are internally coherent. What remains is the *other half of the same bullet* the author repaired: the
Planner skill readback at `references/setup.md:260` still requires a `skill_view` reference to
`references/requested-demo.md`, a file v5 deletes and removes from the upstream package — and the clause
declares delivery incomplete when that reference does not resolve. v5 names `setup.md:261` line-exactly
and leaves `:260`, one line above it, unaddressed. Same class as C2, same file, same failure mode,
one line.

No design element needs to change. The grant derivation, renderer disposition, adoption order, release
binding, credential handover and provenance boundary are sound and were re-verified against source.

## 1. C1 and C2 — independent verification

### C1 — closed

Source, `references/setup.md:145` (verified verbatim):

> Omit project entries whose entrypoint or verb the project does not have. Keep the Docker grants
> regardless of project scripts or demo choice. Supply the demonstration password only through the
> documented environment variable, never as an argument and never in a grant.

Three things now close it together, and they agree:

1. §2 line 33 adds `references/setup.md:145` to the removal list and supplies the exact replacement:
   "Store a chosen shared demo password only in `<project>/demo/settings.json` (mode `0600`, excluded
   from Git), never as an argument and never in a grant."
2. The instruction is scoped as "replace only the final sentence", so the two preceding sentences
   (`Omit project entries…`, `Keep the Docker grants…`) survive untouched — the earlier defect was
   exactly the opposite scoping.
3. §1 line 23, which governs the same block (`setup.md:135–147`), now carries the carve-out "update
   the adjoining password instruction under §2" instead of exposing `:145` to the "retain unrelated
   approved entries" rule.

Test pin: `references/test_build_evidence.py:92` asserts the literal substring
`never as an argument and never in a grant` inside `setup.md`. The replacement sentence ends with
exactly that substring, so the pinned restriction is preserved rather than deleted, and line 33 adds a
positive assertion for the settings path plus the absence of the old environment-variable instruction.
The storage target matches the pin: `disposable-demo/README.md:30` (mode `0600`, operator-owned, outside
Git), `:32–36` (settings vocabulary), `SKILL.md:19` (read `settings.json`, absent policy → `test1234`).

Sweep: line 80's grep now includes `documented environment variable`. I checked that this token also
hits `skills/demo-handover/SKILL.md:20` ("Supply its password only through the documented environment
variable"), which v5 deletes — the addition therefore catches both the prose site and the file the
channel came from. Closed.

### C2 — closed

Source, `references/setup.md:261` (verified verbatim):

> Coder: verify default/max values and process binding, and the installed `demo-handover` skill with
> its `SKILL.md` readback. Check compact task/resume instructions and propagation to fresh delegation,
> with scope, evidence and permissions intact.

§1 line 25 quotes the exact substring it replaces — "and the installed `demo-handover` skill with its
`SKILL.md` readback" — and replaces only that, keeping the model/process and delegation checks. The
replacement asserts `disposable-demo` and `dev-environment` in Planner, Coder and Reviewer profiles,
matching the manifest targets in line 22 (`both → Planner, Coder, Reviewer`) and the per-role delivery
requirement in line 15. It is testable as stated: "the setup checklist references the two installed
skills and no longer requires `demo-handover`". Closed.

## 2. Findings table

| ID | Status | v5 locus | Source evidence |
|---|---|---|---|
| B1 | closed | §1 lines 23–24 | `dev-runner.py:245–251`; `demo.sh:5–6`; `demo_state.py:537`; `setup.md:141,147` |
| B2 | closed | §§2,5 lines 33,62 | `render_text.py:12–15,26,71`; `update_team.py:632–637`; 3.1.1 digest |
| B3 | closed | §2 line 32; §4 line 56 | `disposable-demo/SKILL.md:19`; `README.md:32–36` |
| I1 | closed | §1 line 22 | `manifest.json:228–244` (coder-only), `:245–262` (planner-only) |
| I2 | closed | §1 lines 15,20,22 | both pins' trees; package-internal links resolve (`install.md:45` → generated project guide, by design) |
| I3 | closed | §4 lines 48,56 | `planner.SOUL.md.template:76,98` |
| I4 | closed | §4 lines 51,53 | `setup.md:32`; `planner:99`; `demo_accounts.py:163,210–215` |
| I5 | closed | §4 line 49 | `disposable-demo/SKILL.md:15–16` |
| I6 | closed by design | line 74; line 3 | customer decision — no generic pre-skill demo procedure |
| I7 | closed | §2 line 31 | `setup.md:33`; `SKILL.md:18`; `README.md:30` |
| S1 | closed | §2 line 33 | all listed lines carry the token; `:145` now included |
| S2 | closed | §1 line 22 | no licence file at either pin; permission record now scoped |
| S3 | closed | §3 line 39 | `coder.SOUL.md.template:16,51` |
| S4 | closed | §1 line 24; §4 line 56 | native readback in context; skipped-password case |
| S5 | closed | §3 line 40 | `dev-environment/references/toolchain.md:59–74` |
| C1 | **closed** | §§1–2 lines 23,33 | `setup.md:145`; `test_build_evidence.py:92` |
| C2 | **closed** | §1 line 25 | `setup.md:261` |
| D1 | **required** | none named | `setup.md:260` |

Re-verified anchors, not taken from the prior report:

- B1: `dev-runner.py:245` builds `verbs = ["help", *dispatch, "update"]`, `:246–247` adds `start` only
  when services exist, `:250–251` requires exactly one nonempty operand for `test-selected` and none
  otherwise; `demo.sh:5–6` routes `start`/`user` to `demo_accounts.py`; `demo_state.py:537` accepts
  exactly `start|status|stop|retire|purge`. `README.md:73–74` derives the grant set with `user` only
  when Keycloak is selected. Line 24's "operand-free demo start" matches `demo_state.py:537`.
- B2: `render_text.py:12–15` is the acceptance set, `:26` is `LITERAL_FIELDS` (escaping only), `:71`
  is the password character rule. The 3.1.1 blob hashes to
  `034d96e0624097ce1baea19d1498f591d4aa8697a340a392139ad11f04e926c6`, computed here from
  `git show 4e2fe1e:references/render_text.py`; `REVIEWED_RENDERERS` (`update_team.py:34`) still lacks
  it, and the gate at `:632–636` therefore rejects a 3.1.1 team today. Line 62's corrected vocabulary
  ("`ROLE_FIELDS` for acceptance, `LITERAL_FIELDS` controls escaping") is now exactly right.
- I5: line 49's timing is now correct, not merely cautious — `demo.json` is written at install step 3
  (`SKILL.md:15`), and `docker_host`/`docker_daemon_id` are set there (`:16`), so the binding is needed
  when the file is written, before deployment.
- I2/I4: the delivered sets are a subset of the pins chosen by the pins' own links (`SKILL.md:11`,
  `:14–20`, `:40`); `demo_accounts.py:163` is the `.runtime/accounts.json` record and `:210–215`
  entries carry `password` plus realm/client roles.
- I1: current manifest targets are the retired asymmetry (`demo-handover` → coder,
  `dev-environment` → planner); line 22 replaces both with the same three-role map.

## 3. D1 — `setup.md:260` requires a reference v5 deletes (required, one line)

Source, `references/setup.md:260`:

> Planner: verify required `grilling` load, interview precedence and separate plan acceptance. Verify
> conditional `domain-modeling` load, authorized document boundaries, vocabulary-only glossary,
> proposed ADR status and existing plan gate. Verify once that the Planner text's
> `skill_view(name="dev-environment", file_path="references/requested-demo.md")` resolves to the
> installed `dev-environment` reference; an unresolvable reference leaves delivery incomplete.

After v5:

- §4 line 55 replaces the Planner clause at `planner.SOUL.md.template:64–65` — which is the only place
  the text carries that `skill_view` call — with the announce/retire outcome.
- §1 line 20 delivers `dev-environment` as `SKILL.md`, `references/{install.md,toolchain.md}`,
  `scripts/{dev.sh,dev-runner.py,run-in-tools.sh}`. No `requested-demo.md` exists in the pin's tree.
- §5 line 64 deletes `skills/dev-environment/references/requested-demo.md`.

So both halves of the check become impossible: the quoted text no longer exists, and the file it points
at no longer exists. The clause's own failure condition — "an unresolvable reference leaves delivery
incomplete" — then makes the delivered setup checklist unsatisfiable, exactly the C2 impact. This is
not hypothetical: the check is an equality-style resolution assertion, so a literal implementation
either fails or silently degrades to a vacuous pass.

Why the prior disposition does not hold: v4's report treated `:260` as covered by §4 line 55 ("Replace
… and its callers"). `:260` is not a caller; it is a readback gate that *quotes* the caller, and v4
rejected precisely this kind of cover for `:261` ("Line 22 does list `references/setup.md` for
replacement, but for 'old ownership'"). Applying the same standard to `:260` yields the same result.
v5 strengthens that reading: line 25 now says "At `references/setup.md:261`, replace only …", so a
literal implementer is told the readback repair is finished at `:261`.

Not raised, checked: `:259` ("Verify all three original skill trees and complete companions in the
Planner home") may refer to the same delivery. I could not establish from the tree which three trees
the phrase covers, so I do not assert a contradiction — but it sits immediately above the corrected
per-role readback and says "Planner home", which is the old single-home model. Reconcile the wording in
the same edit.

## 4. Smallest necessary corrections

1. **Required.** Extend the §1 line 25 repair by one sentence, in the same style as `:145`: at
   `references/setup.md:260`, replace only the final sentence with a readback of the references the
   installed `dev-environment` tree actually delivers (`references/install.md`,
   `references/toolchain.md`), or with a pointer to the per-role skill readback; no readback may
   require `requested-demo`. Keep the `grilling` and `domain-modeling` checks. Pin it in the same
   regression: assert the checklist no longer mentions `requested-demo`, as line 25 already does for
   `demo-handover`.
2. **Same edit, wording.** Reconcile `setup.md:259`'s "in the Planner home" with whichever scope the
   corrected readback asserts; do not leave two adjacent bullets describing different delivery shapes.
3. **Optional.** §5 line 61 states the outcome ("remove `DEMO_PASSWORD` from active setup values,
   installation bindings and managed role instructions") and the step-1 grep surfaces every remaining
   site, so I do not raise it as a finding. Naming the three prose sites would remove the last reading
   risk: `update.md:97` (pre-`2.14.0` row that still asks and stores in `confirmed_values`),
   `update.md:99` (adoption rule and installation-record placeholder) and `update.md:41`
   ("stored only in private team state", which becomes false for new teams once
   `<project>/demo/settings.json` is the store). `update.md:109` (pre-`2.14.0` renderer acceptance) and
   `:293` (report masking) are legitimate historical compatibility and should stay.

No other correction is warranted. Nothing else in the five edits creates a contradiction; I checked the
edited paths against each other and against the anchors they touch.

## 5. Customer decisions and authorisations

- Direct credential listing — "ich will dass er auch die credentials der demo user auflistet": line 51
  keeps one row per intended demo user (username, role, effective password) in the DM or a confirmed
  owner-only conversation; line 53 keeps the quoted decision, converts the pin's chat prohibition
  (`SKILL.md:37`) into a named, owner-scoped handover exception instead of shipping two opposing
  instructions, requires effective provisioned values, and excludes tokens, bootstrap/service
  identities and non-demo accounts. Preserved.
- No generic pre-skill demo procedure: excluded at line 74 and line 3. Not reopened.
- Remove old entries and ask fresh, no settings migration: lines 61–62 and the §2 rewrite; §5 does not
  import, suggest or fall back to an old value, and line 62 states "No general settings migration
  mechanism". Both supersede the handoff's `docs/Maker-handoff_v2.md:13` migration provision, as line 3
  says. Preserved.
- Full Docker/Compose authorisation versus scoped launcher grants remain distinct in three independent
  places: `setup.md:136` (four entries granted independently, with the non-project-scoped disclosure),
  `setup.md:141`/`:145` (project entries are absolute-path, one-verb, operand-free), and
  `install.md:55` ("Do not add wildcard selectors, generic Docker or shell grants"). Line 23 keeps the
  separation explicit and restricts the edit to "the stale launcher entries"; `update.md:93`'s "do not
  narrow the wildcard grants to specific verbs" and `test_build_evidence.py:113–135` (which decodes and
  asserts the four entries) are untouched. No new grant framework is introduced.

## 6. What is good

- The C1 replacement is a model minimal change: one sentence, line-exact, negative constraint kept, and
  the sweep token added so the prose variant can never hide again.
- The C2 instruction is line-exact, quotes the text it replaces, keeps the unrelated Coder checks, and
  states a regression assertion instead of a prose intention.
- Line 62's renderer sentence is now technically exact about acceptance versus escaping, and the
  required predecessor digest is the real 3.1.1 blob (`034d96e…`), verified here.
- Line 49's Engine-binding timing now matches the install step that writes `demo.json`, closing the last
  optional wording item from the previous round.
- Line 22's permission boundary is honest: it requires recording scope and source where documented and
  forbids asserting redistribution without evidence, instead of inferring a licence from the Maker's
  own. All three repositories share one GitHub owner, so the record is obtainable — but the plan does
  not claim it exists, which is the correct boundary for a plan.
- The evidence ladder (lines 79–82) still separates contract inspection, temporary-fixture execution,
  native discovery and live behaviour, and refuses to derive a rollout from text assertions.

## 7. Implementation discretion (no finding)

- Where the reconciled skill readback lives inside the `Read back every target` bullets, provided both
  roles and both skills are asserted once and no deleted artifact is required.
- Whether `test_dev_environment.py` (currently pinning the owned tree, `:16` onward) is repurposed or
  split, provided the coverage survives.
- Exact clause wording and whether the two component recipes are one section or two, provided both
  anchor ids resolve — `#dev-environment` and `#disposable-demo` are indeed unused today; only
  `#demo-handover` (`integrations.md:129`) exists.
- Field names in settings and records beyond those the pins fix.
- How the blocked demo card is expressed natively, provided branch HEAD stays inadmissible.

## 8. Evidence limits

- The plan was reviewed as an implementation contract. Nothing was built, executed, deployed, migrated
  or committed; no Docker, board, network, profile or approval action was taken. The single write is
  this file.
- Inputs: the candidate, the v4 plan for the delta, the v4 and v1 reports as evidence, the Maker's
  tracked package/tests and `AGENTS.md`, `demo_and_dev/docs/Maker-handoff_v2.md`, and the two upstream
  repositories at the candidate's pins. To check whether the update-procedure rows had already been
  dispositioned I grepped earlier plan drafts (v1–v3) for the single token `update.md` and read only the
  matched lines; they carry no password-channel decision, and no other part of those drafts was read.
- All hash claims were computed here: candidate, both prior reports, the v4 baseline, the empty
  worktree diff, and the 3.1.1 renderer blob.
- Behavioural claims about the updater, renderer and launchers rest on reading their source and
  argument checks; no test, `approvals test` or live team was run. No credential value was read or
  printed. `accounts.json` was read as source (`demo_accounts.py`), not from a live demo.
- No claim about legal redistribution is made beyond the absence of licence material at either pin and
  the shared repository owner.

*Reviewed by Fujiko*
