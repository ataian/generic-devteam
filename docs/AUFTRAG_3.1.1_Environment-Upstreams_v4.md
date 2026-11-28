# Fujiko — follow-up plan review, v4

Sole candidate: `/home/mariko/projects/generic-devteam/docs/PLAN_3.1.1_Environment-Upstreams_v4.md` SHA-256 `b201d06a0c3397b0eb885da730f2513152937cba48d5c79c2252e881103b4a76`. Your previous report `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.1_Environment-Upstreams_v1.md` SHA-256 `103b8f8461cec2390434adb1ac67b32030bc90dd9dcd24a6de1f35e3e52b9e6f` is evidence, not a second target. Review the plan as an implementation contract, not a built system. Verify source anchors at Maker `4e2fe1e29c2050b8835fdb4a268e0ed14f29d410` (git diff HEAD | sha256sum: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855). Only other allowed inputs: Maker tracked package/tests/project rules, sibling demo_and_dev/docs/Maker-handoff_v2.md and the two upstream packages/scripts/tests in sibling demo_and_dev at the candidate's pins. No other plans, sessions, profiles or credentials.

Terminology: use “the customer” for the human commissioning and receiving the work, not a personal name; distinguish demo users and technical operators. Preserve customer decisions: “ich will dass er auch die credentials der demo user auflistet”; no generic pre-skill demo procedure; “der maker soll einfach die alten die alten einträge entfernen und dann frisch fragen, keine migration der alten einstellungen.” These last two decisions supersede the older handoff. Do not reopen them. Check that the existing full Docker and Compose authorizations remain distinct from scoped launcher grants.

For each previous finding below verify closed / partial / open with v4 and source file:line. Mark an intentional exclusion closed by design with reason. Independently verify the author's disposition; check corrected paths together for new contradictions. Confirm closure where supported; no finding quota. Distinguish blockers from implementation discretion. No implementation, tests, Docker, board, commits, network, or writes except the single report `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.1_Environment-Upstreams_v4.md`. Verdict first (APPROVED / CHANGES_REQUESTED), findings table, smallest necessary corrections and evidence limits. Confirm candidate hash.

| ID | Previous finding |
|---|---|
| B1 | Per-role command grants still describe the retired launchers |
| B2 | Renderer field removal contradicts historical verification |
| B3 | A skipped password choice has no instruction point |
| I1 | `disposable-demo` role targets are never enumerated |
| I2 | No install/verify recipe exists for the two upstream trees |
| I3 | The final demo card has no binder for the reviewed revision |
| I4 | The handover destination may not be owner-only |
| I5 | Demo engine binding inputs have no owner |
| I6 | Legacy demo retirement is only an ambiguity stop |
| I7 | Project writes at setup and update are not disclosed as scope |
| S1 | Replace "setup examples" (line 32) with the concrete sites, so leftovers are not a matter of   interpretation: `references/setup.md:43,74,208,238,255`; `templates/setup-record.md:4,19,21`;   `references/native-workflow.md:28,37`; `references/render_text.py:14,26,71`; three `render_fields`   entries in `manifest.json`. |
| S2 | Neither pin contains a `LICENSE` file or a copyright/license line in `SKILL.md`, `README.md`   or `HERMES.md`. "Record … any license files present" then records nothing; state the owner's   permission in `NOTICE.md` instead of leaving an implicit all-rights-reserved redistribution. |
| S3 | `templates/roles/coder.SOUL.md.template:16` is the Codex brief pointer; build/check/test   routing is `:51`. §3 line 38 cites both without distinguishing them. |
| S4 | Add a grant-settlement assertion and a skipped-password installation case to the §4 matrix   (line 55); today it tests rendered prose only. |
| S5 | §3 line 39 is correct, but naming the two mounts (checkout → `/workspace`, writable cache;   `dev-environment/references/toolchain.md:59–74`) would tie the "untracked test" criterion to the   contract it depends on. |
