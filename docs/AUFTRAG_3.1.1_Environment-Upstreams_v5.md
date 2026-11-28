# Fujiko — follow-up plan review, v5

Sole candidate: `/home/mariko/projects/generic-devteam/docs/PLAN_3.1.1_Environment-Upstreams_v5.md` SHA-256 `b94f6dc2e3aae312c9b0cc29a0680f0ac8b40758af99aadaaa750a89f51f4f00`. Your previous report `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.1_Environment-Upstreams_v1.md` SHA-256 `103b8f8461cec2390434adb1ac67b32030bc90dd9dcd24a6de1f35e3e52b9e6f` is evidence, not a second target. Review the plan as an implementation contract, not a built system. Verify source anchors at Maker `4e2fe1e29c2050b8835fdb4a268e0ed14f29d410` (git diff HEAD | sha256sum: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855). Only other allowed inputs: Maker tracked package/tests/project rules, sibling demo_and_dev/docs/Maker-handoff_v2.md and the two upstream packages/scripts/tests in sibling demo_and_dev at the candidate's pins. No other plans, sessions, profiles or credentials.

Terminology: use “the customer” for the human commissioning and receiving the work, not a personal name; distinguish demo users and technical operators. Preserve customer decisions: “ich will dass er auch die credentials der demo user auflistet”; no generic pre-skill demo procedure; “der maker soll einfach die alten die alten einträge entfernen und dann frisch fragen, keine migration der alten einstellungen.” These last two decisions supersede the older handoff. Do not reopen them. Check that the existing full Docker and Compose authorizations remain distinct from scoped launcher grants.

For each previous finding below verify closed / partial / open with v5 and source file:line. Mark an intentional exclusion closed by design with reason. Independently verify the author's disposition; check corrected paths together for new contradictions. Confirm closure where supported; no finding quota. Distinguish blockers from implementation discretion. No implementation, tests, Docker, board, commits, network, or writes except the single report `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.1_Environment-Upstreams_v5.md`. Verdict first (APPROVED / CHANGES_REQUESTED), findings table, smallest necessary corrections and evidence limits. Confirm candidate hash.


Primary prior report: `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.1_Environment-Upstreams_v4.md` SHA-256 `2091a450ff8eb2ca5c212e50d37bff758b456d5c596f93f1a4e5e89dadb6e263`. Baseline v4 plan `/home/mariko/projects/generic-devteam/docs/PLAN_3.1.1_Environment-Upstreams_v4.md` SHA-256 `b201d06a0c3397b0eb885da730f2513152937cba48d5c79c2252e881103b4a76` may be read for the delta. Confirm C1/C2 against both setup clauses and the exact test pin; check the owner-permission evidence boundary, renderer vocabulary and engine-binding timing. Retain supported earlier closures; check for regressions. No implementation or rollout. Customer request: “bitte pass den plan entsprechend an, wenn du keine fragen an mich hast. und gib den neuen plan an fujiko zum review”.

| ID | Prior finding / status |
|---|---|
| B1 | closed |
| B2 | closed |
| B3 | closed |
| I1 | closed |
| I2 | closed |
| I3 | closed |
| I4 | closed |
| I5 | closed |
| I6 | closed by design |
| I7 | closed |
| S1 | closed |
| S2 | partial |
| S3 | closed |
| S4 | closed |
| S5 | closed |
| C1 | `setup.md:145` keeps a retired password channel (blocker) |
| C2 | `setup.md:261` makes setup verify a deleted skill (required, one line) |
