# Review — Environment upstreams Maker plan v1

Reviewed input: `docs/PLAN_3.1.1_Environment-Upstreams_v1.md`
SHA-256 `4cf942e604e4381a9aca35aa0ec802f077a29edd875b234eb793de83419fc0cc` — confirmed, matches the brief.
Maker root `4e2fe1e29c2050b8835fdb4a268e0ed14f29d410`; `git diff HEAD | sha256sum` =
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty diff) — confirmed.

## 0. Verdict

**CHANGES_REQUESTED**

The plan is source-faithful where it is concrete: both pins resolve to the stated commits, the
declared package inventories match what the upstream pins actually ship, the password schema and
`.runtime/accounts.json` path match the script implementations, and the cited Maker line anchors
are correct. Three mechanisms, however, do not deliver what the plan promises:

1. The per-role `command_allowlist` recipe still lists the **retired** launchers' verbs.
   `demo.sh start` and `dev.sh build`/`update` would match no grant, and the role SOULs forbid
   self-granting, so the first §3/§4 card blocks on native approval.
2. §2 removes `DEMO_PASSWORD` from "renderer input and validation" while §5 requires historical
   verification with the old field set. In the current module shape those two instructions cannot
   both hold, and `update_team.py prepare` would abort for every existing team.
3. A skipped password choice has no instruction point that the installing agent loads, so the
   approved "ask once" is not delivered.

Each has a small, local correction. The plan is otherwise close.

## 1. Coverage and sources

| Source | What was checked | Result |
|---|---|---|
| `docs/PLAN_3.1.1_Environment-Upstreams_v1.md` (hash above) | Full text, 71 lines, every claim traced to a file | Reviewed |
| Maker tracked package @ `4e2fe1e` — `manifest.json`, `SKILL.md`, `README.md`, `NOTICE.md`, `AGENTS.md` | Role fields, `own_skills`, `files`, `upstream_components`, version discipline | Consistent with 4.0.0 |
| Maker `references/{setup,update,native-workflow,upstream-sources,integrations,render_text,update_team}.md/.py` | Cited lines, grant recipe, renderer contract, `desired`/`prepare`/`apply`/`rollback`, masking | Line anchors correct; two mechanism gaps |
| Maker `templates/roles/*.template`, `templates/setup-record.md`, `templates/team-codex-AGENTS.md` | Cited anchors 45/64–65/76/99, 16/51/54, 85/86, guide routing | Anchors correct; Team-Codex has no dev-env text |
| Maker `references/test_{dev_environment,build_evidence,render_reasoning,update_team}.py` | Existing assertions that pin old names, verbs, paths | Identified; covered by plan §68 in principle |
| Maker `skills/{dev-environment,demo-handover,build-evidence}` | Retired text, callers, `requested-demo.md` | Matches the plan's replacement map |
| `ataian/disposable-demo` @ `2c6331d1fc73ae25744d11399feafc19f798c13b` (HEAD = pin) | `SKILL.md`, `README.md`, `scripts/*`, `templates/*`, `tests/smoke.md`, `demo_state.py`, `demo_accounts.py` | Pin and inventory match; schema matches |
| `ataian/dev-environment` @ `3205d3a70fe6ad65c191d07172e106895b75fa04` (HEAD = pin) | `SKILL.md`, `references/{install,toolchain}.md`, `scripts/*`, `tests/dev_environment_smoke.py` | Pin and inventory match; guide path correct |
| `demo_and_dev/docs/Maker-handoff_v2.md` (`a1f6a7b4…`) | Approved workflow, replacement map | Plan covers every row |

Both pins resolve (`git cat-file -t` → commit) and both working trees are at those commits, so the
reviewed bytes are the delivered bytes.

Positive findings worth keeping: the §4 table separates project image build from demo operation
exactly as handoff v2 asks; §5's ordering guard ("do not retire a same-name tree after its
replacement has already been installed") matches `update.md`'s apply → retire → verify order;
the Keycloak handover override is stated as a deliberate, single-purpose exception instead of a
silent contradiction; and the delivery version choice is correct under `AGENTS.md` (retired
interfaces ⇒ MAJOR).

## 2. Blockers

### B1 — Per-role command grants still describe the retired launchers

- Plan: §2 line 32 and §5 lines 59–63 never mention the grant recipe; §1 line 23 only separates
  authorizations from grants.
- Source: `references/setup.md:135–147` (array on line 141), routed from `references/update.md:93`;
  roles may not self-grant (`templates/roles/planner.SOUL.md.template:13`,
  `coder.SOUL.md.template:9`, `reviewer.SOUL.md.template:10`); the array is pinned by
  `references/test_build_evidence.py:88–130`.
- Evidence: the array grants `$DEV_ENTRYPOINT check|test|test-selected *|test-all` and
  `$DEMO_ENTRYPOINT build *|start *|status|stop|retire|retire *|user`. The new launchers accept
  `help|build|check|test|test-selected SELECTOR|update` (+`start`) with **no operands**
  (`dev-environment/scripts/dev-runner.py:245–251`) and `start|status|user|stop|retire|purge`
  with **no operands** (`disposable-demo/scripts/demo_state.py:537; demo.sh:5–6`).
- Consequence: `demo.sh start` (the primary demo verb) and `dev.sh build`/`update` match no entry
  and fall to `ask-approval`. The Coder and Reviewer may not extend their own lists, so the first
  §3 or §4 card blocks with `needs_input` — the plan's own doctrine in `setup.md:147`
  ("a missing grant blocks the affected work"). Four obsolete entries survive as dead grants.
- Smallest correction: replace the fixed verb array with the documented verbs of both launchers
  (`demo.sh start|status|user|stop|retire|purge`; `dev.sh help|build|check|test|test-selected *|update`
  plus `start` when services are configured), keep the "omit verbs the project does not have" rule,
  update the pinning assertion, and add one settlement check that every installed entry matches the
  launcher's own usage text.

### B2 — Renderer field removal contradicts historical verification

- Plan: §2 line 32 ("Remove `DEMO_PASSWORD` from … renderer input and validation") versus §5 line 61
  ("Verify old personalized bytes with the actual historical renderer/field set … reviewed renderer
  hashes").
- Source: `references/render_text.py:12–15` (`ROLE_FIELDS`), `:49–59` (`role_fields` rejects any
  undeclared field), `:26`/`:71` (`LITERAL_FIELDS` and the literal rule);
  `references/update_team.py:21` (the **current** renderer is imported at module scope), `:632–636`
  (`REVIEWED_RENDERERS` gate), `:637` (`desired(repo, old['maker_commit'], …)`).
- Evidence: the three predecessor digests in `update_team.py:28–34` do not include the 3.1.1
  renderer (`034d96e0624097ce1baea19d1498f591d4aa8697a340a392139ad11f04e926c6`). Old entries are
  rendered with the *current* `role_fields`, and the 3.1.1 templates still contain
  `{{DEMO_PASSWORD}}` at planner:76, coder:54, reviewer:86.
- Consequence: read literally, `prepare()` fails twice on every existing 3.1.1 team — the renderer
  gate refuses the unlisted predecessor, and `desired(old)` fails on the undeclared field. §5 is
  then unimplementable, and "an existing team can adopt without losing settings" is not delivered.
- Smallest correction: keep `DEMO_PASSWORD` accepted in `ROLE_FIELDS`/`LITERAL_FIELDS` for
  historical rendering and remove it only from the three new templates and the manifest
  `render_fields`; add the 3.1.1 digest as a reviewed predecessor; require the §5 line 63
  regression to prepare from the pinned 3.1.1 baseline. If the field must leave the whitelist, state
  that old entries are verified through the pinned predecessor module loaded from `old['maker_commit']`,
  not through the current `render_text`.

### B3 — A skipped password choice has no instruction point

- Plan: §2 line 31 ("carry forward the completed setup decision: use the absent-key default without
  prompting again").
- Source: `disposable-demo/SKILL.md:19` ("If a password policy already exists, use it. Otherwise
  offer shared or per-account passwords once"); settings contract `README.md:32–36`; generated guide
  `templates/AGENTS.md:10` states the absent-key default but is written at install step 4, before the
  settings decision at step 6, and does not forbid the question.
- Consequence: a skipped choice writes no `password` key, so the skill's own step 6 still offers the
  question. The installer asks Max a second time — contradicting the approved "ask once" — or writes
  a policy the setup record does not reflect.
- Smallest correction: name the carrier and the sentence. For example, the Coder's demo clause plus
  a line in the generated `<project>/demo/AGENTS.md`: "setup already recorded this choice; do not
  offer the question again; an absent `password` key means the skill default." Add the skipped path
  to the §4 test matrix.

## 3. Important findings

### I1 — `disposable-demo` role targets are never enumerated

§1 line 15 requires "Hermes role targets" as a manifest field but never states the values; line 22
names targets only for assigned environments ("the corresponding skill"). §4 depends on the Planner
(retire, read the account record), the Coder (install, start) and the Reviewer (state checks) each
loading it, while the retired `demo-handover` was Coder-only (`references/upstream-sources.md:15`,
`manifest.json` `own_skills.demo-handover`). Consequence: an implementer can copy the old Coder-only
mapping and leave the Planner's and Reviewer's clauses pointing at operations documented only
upstream. Correction: state the map explicitly (`disposable-demo` → planner, coder, reviewer;
`dev-environment` → planner, coder, reviewer; no Team-Codex copy) and assert it in the fresh-setup
fixture.

### I2 — No install/verify recipe exists for the two upstream trees

§1 line 15 says "Use the existing external-asset installation and update recipes". No generic
recipe exists; `references/integrations.md` has one Deliver/Verify/Record section per component
(e.g. `:130` Owned demo-handover, `:137` Owned prototype). Consequence: `recipe_ref` has no anchor
to point at, and the target layout (`<ROLE_HOME>/skills/<name>/…`), modes (775 for the three shell
entrypoints, 664 otherwise at the pins), the no-license statement and the native discovery readback
stay implicit; the "resolving links" gate fails late. Correction: add a checkbox to author two
sections with targets per role, the exact subpaths from §1 lines 19–20, modes, provenance and a
native readback, and point `recipe_ref` at them.

### I3 — The final demo card has no binder for the reviewed revision

§4 line 47 requires binding execution to "the actual reviewed revision once known" but names no
actor, timing or field; line 48 says "from that revision" without defining it. The card is created
at plan time (`planner.SOUL.md.template:76`) when the SHA cannot exist. Consequence: the card can be
released without a revision and the Coder must guess or use branch HEAD — exactly what the plan
forbids. Correction: require the Planner, at the existing phase-completion wake point
(`planner.SOUL.md.template:98`), to write the reviewed commit into the demo card before release, and
the Coder to refuse a card that lacks it.

### I4 — The handover destination may not be owner-only

§4 line 50 and line 52 say "directly in the customer conversation" and "direct owner handover".
`references/setup.md:32` permits additional authorized users in the project channel, and
`planner.SOUL.md.template:99` sends the customer report to Mattermost. Consequence: synthetic demo
passwords would be posted to a channel with other participants, exceeding "directly to the owner".
The plan also leaves the effective-value source undefined outside Keycloak ("use the project's
documented equivalent", line 52) although the upstream ships only the Keycloak account record.
Correction: require the owner-only route (DM, or a channel confirmed owner-only) and otherwise
report only the location; scope the one-row guarantee to an authentication mechanism that has a
private account record, or require the Coder to record effective values explicitly.

### I5 — Demo engine binding inputs have no owner

§4 line 48 omits them. `disposable-demo/SKILL.md:16` requires `docker_host` and `docker_daemon_id`
"from trusted operator-approved install or fixture configuration" and operator confirmation before
changing the binding (`README.md:11`). Consequence: the Coder reaches demo installation after a
successful build and stops for an input the plan never routed. Correction: record the approved
socket and daemon ID at setup, or make them an explicit prerequisite of the demo card, and state the
stop/report exit.

### I6 — Legacy demo retirement is only an ambiguity stop

§4 line 46 stops on "unknown ownership". The upstream ownership model requires `demo.json` and the
`io.disposable-demo.owner` label (`SKILL.md:26`, `demo_state.py` `named_resources`), which a
pre-upstream demo does not have; the retired `skills/demo-handover/SKILL.md` keeps no engine
identity. Consequence: the first plan on any existing project blocks for manual removal, so "retire
the previous demo on both answers" is delivered only for demos created by the new tool. The test
matrix (line 55) codifies the block but no viable path. Correction: define a legacy branch
(identify from the previous guide's documented names, verify exclusive ownership, remove with
Compose/engine, verify absence) or state plainly that legacy runtimes are an operator step and
planning stays blocked until absent; add that case to the matrix.

### I7 — Project writes at setup and update are not disclosed as scope

§2 line 30 writes `<project>/demo/settings.json` and excludes it from Git; §5 line 60 migrates into
the same path. `references/setup.md:37–40` frames setup as non-mutating for the project ("No
repository moves, Git initialization or project tool installs") and `:74` confines secrets to private
setup state. Consequence: setup now creates a `demo/` directory and edits `.gitignore` inside the
customer's application repository, for teams that may never get a demo, without a disclosed side
effect or a non-Git/read-only fallback beyond "block writing". Correction: state the preconditions
(existing project root, Git root, writable `.gitignore` or an explicit fallback), list the write in
the disclosed setup scope, and test the absent-`.gitignore` case.

## 4. Suggestions (optional, not blocking)

- S1 — Replace "setup examples" (line 32) with the concrete sites, so leftovers are not a matter of
  interpretation: `references/setup.md:43,74,208,238,255`; `templates/setup-record.md:4,19,21`;
  `references/native-workflow.md:28,37`; `references/render_text.py:14,26,71`; three `render_fields`
  entries in `manifest.json`.
- S2 — Neither pin contains a `LICENSE` file or a copyright/license line in `SKILL.md`, `README.md`
  or `HERMES.md`. "Record … any license files present" then records nothing; state the owner's
  permission in `NOTICE.md` instead of leaving an implicit all-rights-reserved redistribution.
- S3 — `templates/roles/coder.SOUL.md.template:16` is the Codex brief pointer; build/check/test
  routing is `:51`. §3 line 38 cites both without distinguishing them.
- S4 — Add a grant-settlement assertion and a skipped-password installation case to the §4 matrix
  (line 55); today it tests rendered prose only.
- S5 — §3 line 39 is correct, but naming the two mounts (checkout → `/workspace`, writable cache;
  `dev-environment/references/toolchain.md:59–74`) would tie the "untracked test" criterion to the
  contract it depends on.

## 5. Implementation discretion (no finding)

- Exact clause wording and placement inside the existing anchors.
- Whether `references/test_dev_environment.py` is repurposed for the upstream asset or split;
  coverage must survive either way.
- Proposal/journal field names for the settings migration, provided `redacted()` masking of the
  legacy value is retained (`update_team.py:59–101`).
- Whether the two new integration sections are one section or two, provided both anchors resolve.

## 6. Scope and evidence limits

- Reviewed the plan only, not an implementation; no code, test, Docker, Kanban, commit or upstream
  change was made. The only write is this file.
- Both upstream repositories were read at the plan's pins and were already at those commits with
  clean working trees; no other revision was consulted.
- `docs/AUFTRAG_3.1.1_Environment-Upstreams_v1.md` is also untracked and was not used.
- No live team, profile, session, credential or Hindsight bank was inspected. Claims about what a
  role will do at runtime are inferred from the instructions and scripts each role loads; they are
  not observed agent behavior.
- The grant finding rests on the documented matcher semantics in `references/setup.md:137–139` and
  the launchers' own argument checks; no `approvals test` was executed.
- No claim is made about legal redistribution beyond the absence of license files at the pins.

*Reviewed by Fujiko*
