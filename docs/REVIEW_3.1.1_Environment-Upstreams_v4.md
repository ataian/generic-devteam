# Review — Environment upstreams Maker plan, v4

Reviewed input: `docs/PLAN_3.1.1_Environment-Upstreams_v4.md`
SHA-256 `b201d06a0c3397b0eb885da730f2513152937cba48d5c79c2252e881103b4a76` — computed and confirmed.
Evidence input (not a second review target): `docs/REVIEW_3.1.1_Environment-Upstreams_v1.md`,
SHA-256 `103b8f8461cec2390434adb1ac67b32030bc90dd9dcd24a6de1f35e3e52b9e6f` — computed and confirmed.
Maker root `4e2fe1e29c2050b8835fdb4a268e0ed14f29d410`; `git diff HEAD | sha256sum` =
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty tree, clean) — confirmed.

## 0. Verdict

**CHANGES_REQUESTED** — one narrow blocker, plus one required readback line in the same file.

All three previous blockers are closed, and ten of the thirteen remaining findings are closed
against source. The remaining defect is not in the mechanisms but in the cleanup map of
`references/setup.md`: two obligations that contradict the new contract survive in the procedure the
setup agent actually executes, and neither is named in v4.

1. **Blocker.** `references/setup.md:145` still instructs "Supply the demonstration password only
   through the documented environment variable". v4 §2 makes `<project>/demo/settings.json` (mode
   `0600`, outside Git) the *only* storage of the choice, and the installed `disposable-demo` reads
   that file, not an environment variable. The sentence sits inside the block v4 §1 line 23 edits
   (`setup.md:135–147`) — but that instruction scopes the edit to "replace only the stale launcher
   entries", so the implementer is told to keep it. It is also invisible to the plan's own final
   sweep, because that grep (v4 §"Final verification" step 1) searches the token `DEMO_PASSWORD`,
   while the line spells the phrase in prose.
2. **Required in the same edit.** `references/setup.md:261` still makes setup verify "the installed
   `demo-handover` skill with its `SKILL.md` readback". `demo-handover` is deleted by v4 §5 line 64
   and is not replaced by an installed skill of that name; the Coder's demo capability is now
   `disposable-demo`. A literal implementation leaves a readback gate that asserts a skill the
   package no longer delivers.

Both are one-line repairs in one file. Nothing in the grant derivation, renderer compatibility,
pinning, adoption order or handover design needs to change.

## 1. Previous findings — disposition

| ID | Status | v4 locus | Source evidence |
|---|---|---|---|
| B1 | **closed** | §1 lines 23–24 | `setup.md:141` old array; `dev-runner.py:245–251`; `demo.sh:5–6`; `demo_state.py:537` |
| B2 | **closed** | §§2,5 lines 33, 62 | `render_text.py:12–15,26,49–58,71`; `update_team.py:28–34,632–635,288–311` |
| B3 | **closed** | §2 line 32; §4 line 56 | `disposable-demo/SKILL.md:19`; `README.md:36` table |
| I1 | **closed** | §1 line 22 | `upstream-sources.md:15–16`; old `own_skills` targets |
| I2 | **closed** | §1 lines 15, 22 | both pins' own package inventories; all delivered links resolve |
| I3 | **closed** | §4 lines 48, 56 | `planner.SOUL.md.template:76,98` |
| I4 | **closed** | §4 lines 51, 53 | `setup.md:32`; `planner:99`; `demo_accounts.py:163,210–215` |
| I5 | **closed** | §4 line 49 | `disposable-demo/SKILL.md:16` |
| I6 | **closed by design** | disposition line 72; §4 line 47 | customer decision: no generic pre-skill demo procedure |
| I7 | **closed** | §2 line 31 | `setup.md:33` Execution-scope row; `SKILL.md:18`; `README.md` settings section |
| S1 | **closed** | §2 line 33 | every listed line verified; `render_text.py` retention is the B2 decision |
| S2 | **partial** | §1 line 22 | no `LICENSE` and no licence/copyright line at either pin |
| S3 | **closed** | §3 line 39 | `coder:16` brief pointer vs `coder:51` operational |
| S4 | **closed** | §1 line 24; §4 line 56 | native readback + skipped-password case present |
| S5 | **closed** | §3 line 40 | `dev-environment/references/toolchain.md:59–74` |

### B1 — closed

v4 line 24 derives the invocation set from the actual launcher contract and line 23 keeps it separate
from the Maker's Docker authorisation. Verified against the pins: `dev-runner.py:245–251` builds
`verbs = ["help", *dispatch, "update"]` (+`start` only when services are configured), requires exactly
one nonempty operand for `test-selected` and no operands otherwise; `demo.sh:5–6` routes `start`/`user`
and requires one verb; `demo_state.py:537` accepts exactly
`start|status|stop|retire|purge`. `disposable-demo/README.md:73` adds `user` only when Keycloak is
selected, which line 24 states. The four dead entries named in the old finding (`build *`, `start *`,
`retire *`, `test-all`) are all covered by "replace only the stale launcher entries", and
`test_build_evidence.py` coverage is required explicitly (operand-free demo start, dev build, absence
of retired entries, preservation of unrelated grants, conditional verbs). The prohibition on
self-granting remains pinned at `setup.md:147`.

### B2 — closed

v4 line 33 now scopes removal to **new** artifacts (manifest role fields, required render inputs,
`native-workflow.md:28,37`, the five `setup.md` sites, `setup-record.md:4,19,21`, new role templates),
and line 62 keeps `DEMO_PASSWORD` for historical rendering. That matches the module shape:
`render_text.py:12–15` is the acceptance set checked at `:56`, `:26` only controls escaping, and
`desired()` (`update_team.py:288–311`) derives fields from the manifest at the rendered commit, so old
entries need the old field list and new ones cannot receive it.

The required predecessor digest is real and currently missing: the 3.1.1 blob hashes to
`034d96e0624097ce1baea19d1498f591d4aa8697a340a392139ad11f04e926c6`, and `REVIEWED_RENDERERS`
(`update_team.py:34`) contains only `051cf4e…`, `f0e6c90…`, `8d4eaef…`. The gate at `:632–635`
therefore rejects every 3.1.1 team today; v4 line 62 names the exact insertion and requires the real
`prepare`/`apply` path from 3.1.1 with all three old templates. `test_render_reasoning.py:80` already
forces template fields to equal manifest `render_fields`, so manifest and template must move together —
which line 33 does.

### B3 — closed

Line 32 puts the missing instruction where the Coder actually reads it: the demo clause that §4
replaces at `coder.SOUL.md.template:54`. It names the outcome precisely — team setup or adoption has
already asked, read the setting, absent key means the skill default, do not repeat the interview,
standalone installation unchanged. That is consistent with `disposable-demo/SKILL.md:19` (offer once;
absent policy uses `test1234` without prompting) and with `README.md:36` (absent file or key →
`test1234`). The skipped path is now exercised at line 56 ("no second interview, no fabricated
`password` key, unchanged upstream default").

### I1 — closed

Line 22 states both maps explicitly (`disposable-demo` → Planner, Coder, Reviewer; `dev-environment` →
Planner, Coder, Reviewer) and repeats them as manifest targets; line 25 asserts exact profile targets
in the fresh-setup fixture. This is the opposite of the retired asymmetry
(`upstream-sources.md:15` Coder-only, `:16` Planner-only). The old expectation is pinned at
`test_render_reasoning.py:1089` and is covered by line 79's "replace obsolete literal assertions".

### I2 — closed

Line 15 gives both recipes real anchors (`references/integrations.md#disposable-demo`,
`#dev-environment`), both currently unused ids, plus targets, the exact subpaths from the table,
byte and executable-bit comparison, native discovery/load readback, and the record fields. Line 22
adds provenance and modes. The delivered sets are complete in the sense the pins themselves define:
`disposable-demo/README.md:5` enumerates exactly `SKILL.md`, `README.md`, three `scripts/`, five
`templates/`, `tests/smoke.md`; `dev-environment/SKILL.md:11` links only `references/install.md` and
`references/toolchain.md`, which in turn reference nothing outside the delivered set. Every link in
the delivered files resolves (`tests/smoke.md` → `../README.md`; `install.md` → `toolchain.md`).
`git ls-tree` shows `100755` for `demo.sh`, `dev.sh`, `run-in-tools.sh` and `100644` elsewhere, which
"Git executable bits" covers without inventing a 664/775 disk expectation.

### I3 — closed

Line 48 now names actor, timing and field: the Planner, at the existing phase-completion step
(`planner:98`), reads the completed dependency's verdict, writes the exact reviewed commit onto the
demo card, reads it back and only then releases; a missing or conflicting revision blocks release, and
branch HEAD is excluded. The card is still created at `planner:76`, when the SHA cannot exist, which
is why the binder sits at the wake point. Line 56 adds the negative test.

### I4 — closed

Line 51 requires the DM with the customer, or a conversation confirmed owner-only, and explicitly
routes the credential rows to the DM when the project channel has other members; file-pointer-only
handover is refused. `setup.md:32` records the customer, additional authorised users and DM
participants, and `setup.md:74` already relies on a Planner DM, so the route is a real binding rather
than an assumption. Line 53 closes the second half of the finding: effective values come from
`.runtime/accounts.json` for Keycloak (`demo_accounts.py:163`, entries at `:210–215` carry `password`
plus realm/client roles), and for other authentication the Coder records them in a private handover
record and passes only its path. Bootstrap and service credentials are excluded, and an unreadable
record blocks the handover instead of widening permissions.

### I5 — closed

Line 49 makes the operator-approved `docker_host` and independently recorded `docker_daemon_id` a
prerequisite of the requested demo card, resolved with the operator before release, and not repeated
at setup. That matches `disposable-demo/SKILL.md:16` ("from trusted operator-approved install or
fixture configuration", operator confirmation before changing the binding) and `README.md` runtime
section. Rejecting a stale image or partial demo is retained.

### I6 — closed by design

The customer decided against a generic pre-skill demo procedure; v4 records the exclusion at line 72
and line 3, and I do not reopen it. What remains in line 47 is the obligation the customer did keep —
announce removal, retire on both answers without a second permission request, verify before releasing,
and stop and report on unknown ownership or an unreachable engine without renaming, purging or
substituting an identity. That corresponds to the second of the two alternatives the previous review
offered ("planning stays blocked until absent"), and the ambiguous-ownership case remains in the test
matrix at line 56. Residual, not a defect: line 47 does not say who performs the removal, and a
pre-upstream demo has no `demo.json` or owner label, so `demo.sh status` cannot inspect it — such a
project stops at plan acceptance by scope decision. Recording that as an operator step would be a
wording improvement only.

### I7 — closed

Line 31 discloses the writes before the existing approval (create `demo/`, narrow ignore rule only if
needed), preserves existing rules, verifies the path is ignored *and* untracked before writing a
secret, forbids creating a repository outside Git, and blocks an already tracked or unwritable target.
Tests for absent and existing `.gitignore` are required. This sits on top of the real disclosure row
`setup.md:33` ("Execution scope | Exact local writes…") and matches `SKILL.md:18` and the settings
section of `README.md` (mode `0600`, operator-owned, outside Git).

### S1 — closed

Line 33 lists the concrete sites instead of "setup examples". Each was verified to carry the token:
`setup.md:43,74,208,238,255`; `setup-record.md:4,19,21`; `native-workflow.md:28,37`; the three
`render_fields` blocks at `manifest.json:114–121,143–158,174–184`. `render_text.py:14,26,71` are
deliberately kept under B2 — an explicit, reasoned decision, not an omission.

### S2 — partial

Confirmed factually: neither pin has a `LICENSE`, and no licence or copyright line appears in either
`SKILL.md`, `README.md` or `HERMES.md`. v4 line 22 improves on v3 by stating the absence and by
forbidding the Maker's MIT from being assigned to either upstream or a relicensed copy. It still does
not record the owner's permission, which was the substance of the suggestion; "document that fact"
documents a gap, not a grant. Non-blocking (it was a suggestion), but one sentence in `NOTICE.md`
would close it.

### S3 — closed

Line 39 separates the two anchors explicitly: `coder:16` is the Codex brief pointer carrying the
project agent-guide path, `coder:51` is the operational build/check/test instruction. Both verified.

### S4 — closed

Grant settlement now exists in §1 line 24 (verify each selected exact invocation by native approval
readback in its own execution context, with the explicit note that a profile grant is not Team-Codex
runtime access) and is pinned by named cases in `test_build_evidence.py`. The skipped-password
installation case is in the §4 matrix at line 56. Placement moved out of the §4 table; the coverage
asked for is present.

### S5 — closed

Line 40 names both mounts and the container behaviour: single checkout at `/workspace` (multiple
checkouts use their configured paths), writable cache at `/opt/project-cache`, short-lived tool
containers. `toolchain.md:59–74` confirms both targets (plus the read-only `/opt/project-dev` helper
mount), so the untracked-test criterion is now tied to the contract it depends on.

## 2. New findings from checking the corrected paths together

### C1 — `setup.md:145` keeps a retired password channel (blocker)

`setup.md:145` reads: "Omit project entries whose entrypoint or verb the project does not have. Keep
the Docker grants regardless of project scripts or demo choice. Supply the demonstration password
only through the documented environment variable, never as an argument and never in a grant."

- v4 §2 line 31: "Store explicit choices **only** at `<project>/demo/settings.json`", mode `0600`,
  excluded from Git. The installed skill reads that file (`demo_accounts.py:84–100`); no environment
  variable carries demo-user passwords, and Maker setup no longer holds a password value at all.
- v4 §1 line 23 edits `setup.md:135–147` but instructs "replace only the stale launcher entries;
  retain unrelated approved entries", so a literal implementer preserves the sentence.
- The plan's own sweep at step 1 greps `DEMO_PASSWORD`; `:145` spells "demonstration password", so it
  is not surfaced and not classified.
- Impact: the delivered setup procedure would contain two opposing statements about where the demo
  password lives, in the section the grant operator reads. The plausible failure modes are a second
  interview (against the customer's "ask once"), an exported credential in the setup process
  environment, or pressure to encode it in a grant — the last is explicitly forbidden.
- `test_build_evidence.py:92` pins the clause "never as an argument and never in a grant", so the
  sentence must be rewritten, not deleted.

### C2 — `setup.md:261` makes setup verify a deleted skill (required, one line)

`setup.md:261` reads: "Coder: verify default/max values and process binding, and the installed
`demo-handover` skill with its `SKILL.md` readback."

- v4 §5 line 64 deletes `skills/demo-handover/SKILL.md` and its mappings; §1 installs
  `disposable-demo` instead. No artifact named `demo-handover` remains to verify.
- Line 22 does list `references/setup.md` for replacement, but for "old ownership"; line 15 requires
  readback recording for the new components without naming this gate. The step-1 grep does surface
  `:261`, yet the classification options ("active contract, intentional historical compatibility, or
  test") do not describe a delivery check for a deleted skill, so the disposition is undefined.
- Impact: the setup readback line would demand evidence for a skill the manifest no longer delivers,
  which blocks an honest "Setup outputs verified" report.

Checked and **not** raised: `setup.md:260` (the `requested-demo` readback) is covered by §4 line 55
("Replace … and its callers"); `integrations.md:129–133` and `upstream-sources.md:15,30` are inside
the ownership replacement and the step-1 sweep; `README.md:139`'s stale `docker/dev/AGENTS.md` is
inside the cited `README.md:137–140` range.

## 3. Smallest necessary corrections

1. Add `references/setup.md:145` to the site list in §2 line 33, and rewrite the sentence to keep the
   negative constraint while pointing at the real store: the value lives only in
   `<project>/demo/settings.json` (mode `0600`, outside Git) and never in an argument or a grant.
   Keep `test_build_evidence.py:92` satisfied.
2. Add `references/setup.md:261` to the readback replacement: verify the installed `disposable-demo`
   (`SKILL.md` readback, per role) and the `dev-environment` tree at its actual targets, replacing the
   `demo-handover` readback.
3. Optional, one sentence: state the owner's permission for both upstreams in `NOTICE.md` (S2).
4. Optional, wording: at line 62, name the set explicitly — keep `DEMO_PASSWORD` in `ROLE_FIELDS`
   (acceptance, `render_text.py:12–15`); `LITERAL_FIELDS` (`:26`) only controls escaping. The required
   3.1.1 `prepare`/`apply` test already enforces the correct reading.
5. Optional, wording: at line 49, the Engine binding is needed when `demo.json` is written
   (`SKILL.md:16`, install step 3), i.e. before installation completes, not only before deployment.

## 4. Customer decisions preserved (not reopened)

- Direct credential listing: "ich will dass er auch die credentials der demo user auflistet" — v4
  line 51 requires one row per intended demo user (username, role, effective password) and line 53
  quotes the decision, converts the pin's chat prohibition into a single, explicit, owner-scoped
  handover exception, and forbids tokens, bootstrap/service identities and non-demo accounts.
- No generic pre-skill demo procedure — line 3 and line 72; see I6.
- Remove old entries and ask fresh, no settings migration: "der maker soll einfach die alten die
  alten einträge entfernen und dann frisch fragen, keine migration der alten einstellungen" — §5
  line 61 removes `DEMO_PASSWORD` from active setup values, installation bindings and managed role
  instructions, asks the same question as new creation, writes only the fresh decision, and states
  "No general settings migration mechanism" at line 62.

These supersede the older handoff and are treated as settled.

## 5. Docker/Compose authorisation versus launcher grants

Still distinct, and the distinction is now stated twice (v4 lines 23 and 24) instead of being implied:
the four Maker grants (`docker`, `docker *`, `docker-compose`, `docker-compose *`) remain a broad,
explicitly non-project-scoped authorisation with a disclosure obligation (`setup.md:139–140`,
`test_build_evidence.py:113–135`), while the launcher entries are project-scoped, absolute-path,
one-verb, operand-free strings. The plan forbids conflating them, forbids wildcard selectors, and does
not let the upstream recipe add generic Docker grants (`references/install.md:55`, which forbids
"generic Docker or shell grants"). `update.md:93`'s "do not narrow the wildcard grants to specific
verbs" stays intact.

## 6. What is good

- The adoption order in line 63 (stage → back up → apply → remove active bindings → ask afresh →
  retire old targets → install pinned trees → read back) matches the apply/retire sequence in
  `update.md` and avoids the same-name replacement trap that line 60 describes.
- The renderer disposition is technically exact: predecessor digest, old-manifest field list, new
  templates only, and the real 3.1.1 path instead of prose verification.
- The Engine binding is routed to the only actor who can resolve it, without adding a per-setup
  question — the correct reading of `SKILL.md:16`.
- Versioning under `AGENTS.md` is right: retired owned-skill and role-binding interfaces ⇒ 4.0.0, with
  `SKILL.md` and `manifest.json` bumped together once.
- The evidence ladder in lines 79–81 keeps static contracts, temporary-fixture execution, native
  discovery and live behaviour apart, and refuses to claim a rollout from text assertions.

## 7. Implementation discretion (no finding)

- Clause wording and placement inside the existing anchors; whether `test_dev_environment.py` is
  repurposed for the upstream asset or split, provided coverage survives (the file currently pins the
  owned tree wholesale: `test_dev_environment.py:16–52`).
- Whether the two integration recipes are one section or two, provided both anchors resolve.
- Exact field names in the settings/records beyond those the pins already fix.
- How the "blocked, not eligible for automatic promotion" demo card is expressed with the native
  board, provided branch HEAD remains inadmissible as a revision.

## 8. Evidence limits

- Reviewed the plan as an implementation contract only; nothing was built, tested, executed, deployed
  or committed. No Docker, board, network or profile action. The single write is this file.
- Inputs limited to the candidate, the previous review as evidence, the Maker tracked package and
  tests at `4e2fe1e`, `demo_and_dev/docs/Maker-handoff_v2.md`, and the two upstream repositories at
  the candidate's pins (`2c6331d1…`, `3205d3a7…`, both clean at those commits). No earlier plan,
  commission, session, profile or credential was read.
- Hash claims are computed here: candidate, evidence report, the empty worktree diff, and the 3.1.1
  renderer blob digest via `git show 4e2fe1e:references/render_text.py`.
- Claims about role behaviour are inferred from the instructions and scripts each role loads. No live
  team, agent or demo was observed, and no `approvals test` was run; the grant findings rest on the
  launchers' own argument checks and the documented matcher rules.
- `accounts.json` was read as source (`demo_accounts.py`), not from a live demo, and no credential
  value was printed.
- No claim about legal redistribution is made beyond the absence of licence material at the pins.

*Reviewed by Fujiko*
