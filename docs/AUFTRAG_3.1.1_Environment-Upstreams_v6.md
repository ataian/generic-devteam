# Fujiko — follow-up plan review, v6

Request: “einverstanden. plan anpassen und fujiko zum review geben”. Review only the v6 delta and any regression it causes. The accepted change replaces the retired Planner reference with the two delivered references and reconciles the adjacent profile scope. The workflows remain unchanged.

Read only the following documents and relevant tracked Maker sources/tests at 4e2fe1e29c2050b8835fdb4a268e0ed14f29d410 (git diff HEAD | sha256sum: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), plus the selected local upstream files at the plan’s pins. Do not search other drafts, reports, profiles or sessions.

| Input | SHA-256 |
|---|---|
| Candidate: /home/mariko/projects/generic-devteam/docs/PLAN_3.1.1_Environment-Upstreams_v6.md | 38455862bbcde489d4487c590b16eef9f346709ce0ef1a604dcc48da829013a6 |
| Delta baseline: /home/mariko/projects/generic-devteam/docs/PLAN_3.1.1_Environment-Upstreams_v5.md | b94f6dc2e3aae312c9b0cc29a0680f0ac8b40758af99aadaaa750a89f51f4f00 |
| Primary review: /home/mariko/projects/generic-devteam/docs/REVIEW_3.1.1_Environment-Upstreams_v5.md | 54b2a8837037faa7be0523cc86b3a1ec7d61fa141bbf05d29e71122ed6c37d91 |

| ID | Prior finding |
|---|---|
| D1 | `setup.md:260` requires a reference v5 deletes (required, one line) |

Verify D1 independently against setup.md:259–261, actual Planner-only assignments, both pinned reference files and existing test assertions. Does the correction preserve unrelated Planner/Coder checks, distinguish per-role delivery, and cover the missing-reference failure? Check the v5→v6 diff for unrelated changes; retain supported closures including C1/C2. Confirm closure when justified; no finding quota. Verdict first (APPROVED or CHANGES_REQUESTED), D1 closed/partial/open with file:line, new material issues if any, evidence limits and candidate hash. Static plan review only: no implementation, tests, Docker, network, board, profile or commit actions. Only write `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.1_Environment-Upstreams_v6.md`.
