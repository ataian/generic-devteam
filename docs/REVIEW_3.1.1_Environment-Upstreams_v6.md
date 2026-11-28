# Review — Environment upstreams Maker plan, v6 (delta review)

Reviewed input: `docs/PLAN_3.1.1_Environment-Upstreams_v6.md`
SHA-256 `38455862bbcde489d4487c590b16eef9f346709ce0ef1a604dcc48da829013a6` — computed and confirmed.
Delta baseline: `docs/PLAN_3.1.1_Environment-Upstreams_v5.md`
SHA-256 `b94f6dc2e3aae312c9b0cc29a0680f0ac8b40758af99aadaaa750a89f51f4f00` — computed and confirmed.
Primary prior report: `docs/REVIEW_3.1.1_Environment-Upstreams_v5.md`
SHA-256 `54b2a8837037faa7be0523cc86b3a1ec7d61fa141bbf05d29e71122ed6c37d91` — computed and confirmed.
Maker root `4e2fe1e29c2050b8835fdb4a268e0ed14f29d410`; `git diff HEAD | sha256sum` =
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) — confirmed.
Upstream pins present and clean at the plan's commits: `3205d3a7…` (`demo_and_dev/dev-environment`),
`2c6331d1…` (`demo_and_dev/disposable-demo`) — confirmed by `git rev-parse HEAD` and empty `git status`.

## 0. Verdict

**APPROVED.**

D1 is **closed** at its exact anchor. The v6 delta is three hunks — the header line, the rewrite of §1's
readback bullet, and one new row in the disposition list — with no unrelated edits, and it introduces no
new contradiction with `setup.md`, `manifest.json`, the two pins or the existing regression modules. C1 and
C2 remain closed and were re-verified rather than assumed. Three wording items are recorded below as
non-blocking notes; none makes a delivered checklist unsatisfiable, ambiguous at a single anchor, or
technically wrong.

## 1. D1 — independent verification

### Source, `references/setup.md:259–261` (read verbatim)

> 259 — Skills: compare full file sets and bytes with source. Compare recovery launcher with bound Maker
> output. Verify all three original skill trees and complete companions in the Planner home. Maker
> references alone cannot deliver them.
> 260 — Planner: verify required `grilling` load, interview precedence and separate plan acceptance.
> Verify conditional `domain-modeling` load, authorized document boundaries, vocabulary-only glossary,
> proposed ADR status and existing plan gate. Verify once that the Planner text's
> `skill_view(name="dev-environment", file_path="references/requested-demo.md")` resolves to the
> installed `dev-environment` reference; an unresolvable reference leaves delivery incomplete.
> 261 — Coder: verify default/max values and process binding, and the installed `demo-handover` skill
> with its `SKILL.md` readback. …

### The contradiction, re-derived without using the prior report's conclusion

- `setup.md:260` is one physical line; its third and final sentence is the `requested-demo.md` resolution
  gate, and its own failure clause declares delivery incomplete.
- §4 line 55 replaces `templates/roles/planner.SOUL.md.template:64–65`, the only carrier of that
  `skill_view` call (verified: `grep -n requested-demo templates/roles/planner.SOUL.md.template` returns
  only `:65`). §1 line 20 of both drafts delivers `dev-environment` as `SKILL.md`,
  `references/{install.md,toolchain.md}`, `scripts/{dev.sh,dev-runner.py,run-in-tools.sh}`. §5 line 64
  deletes `skills/dev-environment/references/requested-demo.md`.
- The pin's tree contains no `requested-demo.md`: `git ls-tree -r --name-only 3205d3a7…` lists only
  `references/install.md` and `references/toolchain.md` under `references/`.
- Therefore both operands of the `:260` gate disappear while the gate keeps its own failure condition.
  That was D1, and v5 named only `:261` — one line below it.

### What v6 does, checked line by line

Line 25 now carries three anchor-exact instructions:

1. `:259` — *retain* verification of the three original Planner skill trees and their companions in the
   Planner home, and *distinguish* that check from the environment skills in every assigned profile.
   This is a no-change instruction for the source text, which is correct: `:259` is about the Planner's
   original (non-environment) trees and remains true after the delivery change — none of them is deleted
   by §5 (deleted: `skills/demo-handover`, `skills/dev-environment`, `requested-demo.md`).
2. `:260` — *replace only the final sentence* with: in the Planner profile load `references/install.md`
   and `references/toolchain.md` from the installed `dev-environment` skill; either unresolved reference
   leaves delivery incomplete.
3. `:261` — the unchanged v5 repair, preserved verbatim.

Why (2) is technically correct, not merely a deletion:

- Both named files exist at the pin and are the only two references there. The pin's own entrypoint makes
  them the skill's required references: `SKILL.md:11` — "Follow [installation](references/install.md) …
  Use the [toolchain contract](references/toolchain.md) …". That is exactly the general rule the plan
  already states in §1 line 15 ("load the entrypoint and its required references"), so `:260` becomes the
  Planner-specific instance of an obligation the plan already owns.
- The replacement preserves the surrounding checks: sentence 1 (`grilling` load, interview precedence,
  separate plan acceptance) and sentence 2 (`domain-modeling`, document boundaries, glossary, ADR status,
  plan gate) are explicitly named as retained. The instruction is sentence-scoped, so an implementer
  cannot read it as permission to rewrite the bullet — the same scoping discipline that made C1 land.
- The failure condition survives in the same sentence ("either unresolved reference leaves delivery
  incomplete"). Both the single-reference-missing case and the skill-not-installed case (neither
  resolves) are covered; nothing silently degrades to a vacuous pass.
- The check is decidable statically by the setup operator: two named paths inside one installed skill
  directory. No text-tie to a role clause is required, so it cannot dangle again when role prose changes.

### Per-role distinction — checked against the actual assignment map

- Planner-only today: `manifest.json:245–262`, `targets.hermes: ["planner"]`, `transport` including
  `references/requested-demo.md`. That is why `:260`'s gate was written Planner-scoped in the first place.
- The plan widens delivery to all three roles (§1 line 22: both components → Planner, Coder, Reviewer),
  which *creates* the risk the prior round flagged: a Planner-shape check standing next to a three-role
  delivery. v6 resolves it explicitly rather than by assertion — `:260` verifies the Planner's reference
  load, `:261` verifies both skills in all three profiles, `:259` stays Planner-home. The three bullets
  now describe three different objects instead of two competing shapes. This is a real reconciliation,
  not a relabelling.
- It is also substantively right: only the Planner installs/adopts the environment (§3 lines 38–40); the
  Coder runs documented project commands and the Reviewer performs read-only checks (§3 line 39, §4
  lines 49–50). Reference-level load is a Planner requirement; role-level skill load is the three-role
  requirement. No role is asked to load something it cannot use.

### Test pin — checked against the assertions that actually exist

- `references/test_dev_environment.py:55–63` pins exactly the three strings the fix changes: the call in
  the rendered Planner, the call in `setup.md`, and `"leaves delivery incomplete"`. Line 25's new
  assertion ("names both delivered references and no longer mentions `requested-demo.md`") sits in the
  same module and has a genuine red baseline: `grep -c "references/install.md" references/setup.md` = 0
  and `references/toolchain.md` = 0 today, while `requested-demo` appears only at `:260`.
- The retained half of the assertion is real: `test_build_evidence.py`-style literal pins elsewhere are
  unaffected, and the `requested-demo` tokens in `test_render_reasoning.py:115,157`,
  `test_build_evidence.py:140` and `test_update_team.py:779–886` are covered by §4 line 55 / §5 line 64
  and the line-82 rule "Replace obsolete literal assertions, preserve unrelated checks".

**D1: closed** (`references/setup.md:260`, plan §1 line 25).

## 2. Delta audit — no unrelated changes

`diff -u v5 v6` is exactly three hunks:

| Hunk | Content | Assessment |
|---|---|---|
| Header line 3 | v5 → v6; "Addresses D1 in Fujiko's v5 review: correct the Planner reference check and distinguish Planner-only skill checks from environment checks in each assigned profile." | Accurate description of the actual edit; no claim of closure, no scope inflation |
| §1 line 25 | `:259` / `:260` / `:261` instructions plus the module-scoped test assertion | The only substantive edit; analysed above |
| Disposition list | new row "D1: §1 — replace the obsolete Planner reference check and clarify its profile scope." | Matches the edit; sits correctly above C1/C2 |

Nothing else moved: §§2–5, the integration rule, the workflow table, the final verification ladder and the
out-of-scope block are byte-identical to v5. No workflow, grant, renderer, adoption-order or credential
handover provision was touched, so the statement that the workflows remain unchanged holds for the delta.

## 3. Retained closures — re-verified, not carried over

- **C1 — closed, and still an open implementation task.** `references/setup.md:145` still ends with
  "Supply the demonstration password only through the documented environment variable, never as an
  argument and never in a grant", and `references/test_build_evidence.py:92` still pins the substring
  `never as an argument and never in a grant`. The v6 delta does not touch §2 line 33 or §1 line 23, so
  the three-part closure (removal list entry, replacement sentence, carve-out from "retain unrelated
  approved entries") stands unchanged.
- **C2 — closed.** `:261`'s repair is present verbatim in v6 line 25, including the quoted substring, the
  retained Coder model/process and delegation checks, and the regression assertion. `requested-demo`
  occurs only at `:260` in `setup.md`, so after both repairs the checklist stops mentioning either retired
  artifact — the property the assertion tests.

## 4. Regression check for the delta

- `setup.md:259` is not made false: the Planner home genuinely holds the original, non-environment trees,
  all Planner-targeted (`manifest.json` own_skills and upstream components with `targets.hermes:
  ["planner"]`: `grill-me:485–488` incl. `skills/productivity/grilling`, `skills/engineering/domain-modeling`
  at `:479–481`; `superpowers:464–467`; `brownfield-feature-planning`). No Planner tree is deleted by §5.
- No new dependency is introduced: `:260`'s replacement references only files the plan already installs in
  the same slice (line 20), so the fresh-setup fixture and the update path (§5) do not need a new step.
- The `:261` "per-role readback above" pointer still resolves after the inserted sentences, because the
  insertion sits inside the same bullet after the opening fixture/readback sentences.
- Cross-check with line 15 and line 22: target names, paths and the "no manifest row or file copy is a
  loading check" rule are consistent with all three anchors.

## 5. Non-blocking notes (no change requested)

1. **`preserve historical upgrade fixtures` is scoped to a module that has none.** Line 25 places that
   clause in `references/test_dev_environment.py`; the historical upgrade fixtures live in
   `references/test_update_team.py` (`:779–832`; and the 3.1.0 adoption fixture at `:858–886`). That
   fixture's last assertion — `assertIn('file_path="references/requested-demo.md"', SOUL)` at `:886` —
   encodes the delivery being retired and must be *replaced*, not preserved. The module scoping in the
   sentence and §5 line 64 keep this from being a contradiction, but moving the clause to §5 ("preserve
   the drift/interruption fixtures; replace the 3.1.0 reference-adoption assertion") would remove the
   reading risk.
2. **`test_render_reasoning.py:115,157` also pin the retired call** in the rendered Planner
   (`requested = 'skill_view(…requested-demo.md)'`, asserted present twice). §4 line 55 ("and its
   callers") plus line 82 cover it, but the round named `:145`, `:259`, `:260` and `:261` line-exactly
   where it could; naming these two lines would be consistent with that standard.
3. **"three original skill trees" remains a count the plan does not establish.** v6 now turns it into a
   stated scope distinction. The phrase is defensible under the reading that the three are the
   Planner-loadable originals — `grilling` (`planner.SOUL.md.template:29`), `domain-modeling` (`:32`),
   `brownfield-feature-planning` (`:30`, `:92`) — but the Planner home holds more trees than three
   (manifest own_skills plus `grill-me`/`superpowers`/`hindsight`/`codebase-memory`/`graphify`/
   `hermes-core`). Since the instruction is only "retain", this is a pre-existing imprecision, and the
   role-scope claim v6 actually needs (Planner-only, not three-role) is correct either way.

## 6. Evidence limits

- Static plan review only. Nothing was implemented, rendered, executed, installed, migrated, deployed or
  committed; no Docker, network, board, profile or approval action was taken. The single write is this
  file.
- Inputs: the candidate, the v5 baseline (delta only), the v5 report, the tracked Maker package
  (`references/setup.md`, `manifest.json`, `templates/roles/planner.SOUL.md.template`,
  `references/test_{dev_environment,build_evidence,render_reasoning,update_team}.py`), and the two
  upstream repositories at the plan's pins. No other draft, report, profile or session was read.
- All hash claims were computed here: candidate, baseline, prior report, `HEAD`, and the empty
  `git diff HEAD`.
- Upstream evidence is limited to `git ls-tree` at the pins, `SKILL.md` and the two reference files'
  existence and cross-links. The Maker's behavioural claims about launchers, renderer and updater were not
  re-exercised in this round; they were not part of the delta and rest on the source reading in the prior
  review. No test suite was run, so no claim is made that the planned assertions currently pass — several
  of them are expected to fail by design until the plan is implemented.
- No credential value was read or printed. No legal or redistribution claim is made.

*Reviewed by Fujiko*
