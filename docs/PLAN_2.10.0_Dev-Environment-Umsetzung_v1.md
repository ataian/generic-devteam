# Implement the approved development-environment specification

Status: implementation authorized by Max: “ok dann bitte umsetzen”.
Package target: **2.10.0**, one compatible-feature MINOR bump from 2.9.1.
Workspace: `/home/mariko/projects/generic-devteam`, existing branch `v3`.
Starting HEAD: `94ded22fa58b1c41956985c3edd562c443bae7af`.

## Accepted baseline

Read the complete `docs/SPEC_2.9.1_Dev-Environment_v3.md` (SHA-256 `e582378337f513717deec398e74b81eb7cf3f831b94683af3bfbab41e2b9315e`) and `docs/REVIEW_2.9.1_Dev-Environment_v2.md` (APPROVED). Earlier drafts and review reports remain historical and unchanged. The latest user instruction authorizes implementing this specification; its old statement that implementation is not yet authorized describes the earlier document-review stage.

This is one coherent Maker package task, not setup of a team or creation of a live development environment. Max corrected execution routing: “was nein stop. mach das selber.” Mariko implements directly; Fujiko independently reviews the finished changeset. No implementation ticket was dispatched.

## Phase 1 — As a project owner, equip the team for reusable Docker development

Deliver the complete candidate skill, its Planner-only installation/update mapping, reconciled role instructions, and package regression coverage. The result is a reusable Maker capability, not a universal Compose generator.

### Required changes

1. Add `skills/dev-environment/SKILL.md` from the complete fenced candidate in the approved specification. Preserve its operating scope, construction/adoption branches, PostgreSQL branch-template workflow, two-guide separation and acceptance cases. Do not import local authoring paths or review history into the delivered skill.
2. Apply R1–R8 to the three role templates after verifying each ALT matches exactly once. R7 stays after the design checks, outside the contiguous prototype-only exception. R8 binds reading the guide and using its container commands only when an environment exists. Preserve Team-Codex handoff, review-helper permissions and role boundaries.
3. Add the owned skill and exact file inventory to `manifest.json`, using existing schema and `targets.hermes = [planner]`. Use the existing complete-tree setup/updater mapping; do not create a separate installer or transport.
4. Update `references/upstream-sources.md`, `README.md`, `NOTICE.md` and the optional first-task offer in root `SKILL.md`. Setup may offer creation/adoption after handoff; it must not run the skill automatically.
5. Extend `references/test_render_reasoning.py`, `references/test_update_team.py` and focused package contract tests using existing fixtures. Update only the positive Planner assertion in `test_plan_separates_binding_scope_from_coder_discretion` in `references/test_brownfield_planning.py`; preserve its negative single-source checks. Include newly added test files in the package inventory where repository conventions require it.
6. Update the package version in root `SKILL.md` and `manifest.json` together to 2.10.0. Keep the candidate skill's own version separate. Use existing release-documentation conventions without inventing a new changelog framework.

Use the specification's integration table as the scope map; necessary adjacent tests or existing verification documentation may be adjusted with a concrete reason. Keep unrelated code, translations, configuration and upstream skills unchanged. Read `AGENTS.md`, `HERMES.md`, `README.md`, `references/development-verification.md`, and the current TAS source and required references before changing instructions.

### Acceptance criteria

- **A1 — Delivered skill:** the approved complete skill text is present; valid frontmatter, one coherent entrypoint and portable content. The manifest includes it exactly once and assigns it only to the Planner. Source/legal/README references agree.
- **A2 — Reachable use:** generated Planner instructions invoke the skill for creation/adoption/revision. Relevant tickets require the repository agent guide only when the environment exists. Team-Codex receives guide path and runtime authority. Root-pointer and two-guide contracts keep ordinary agent instructions free of the human-guide pointer.
- **A3 — Consistent authority:** the three shared authority paragraphs are identical. Autonomous start/stop/restart/rebuild/recreation/synthetic seeding/disposable reset and demonstration use are retained. Product-source ownership, Reviewer independence, operational data, host/shared infrastructure and external-effect boundaries remain intact. The prototype-only exception stays byte-identical and contiguous.
- **A4 — Database contract:** required databases belong to the development Compose project. PostgreSQL rules cover template preparation, distinct collision-safe branch bindings, create-once/reuse, actual-target verification before writes, baseline/other-branch preservation and scoped resets. External database adoption remains an explicit bounded decision. Third-party-service construction stays outside this generic skill.
- **A5 — Guidance and demonstration:** project authors produce both self-contained guides with real commands. Agent instructions require container use; demos remain running and provide a verified URL and concrete SSH forward where needed, with untested client access disclosed. No additional customer approval loop or setup blocker for absent environments.
- **A6 — Delivery/update regression:** existing renderer and updater tests exercise Planner delivery, absence from other role targets, complete bytes, existing local-rule preservation and applicable collision/update behavior using isolated fixtures. Test the actual existing mapping rather than a parallel fake installer.
- **A7 — Verification:** record failing focused regressions before implementation, then green results. Run the focused renderer suite and full package suite using the existing commands; report actual counts, skips and native denials. Validate inventory, version equality, local Markdown links/anchors and `git diff --check`. Cover absent, pre-existing and incomplete environment instruction scenarios as static contract checks; do not mislabel them as live-agent qualification.
- **A8 — Independent acceptance:** Fujiko verifies the exact final changeset against this plan and the accepted specification. A specification approval is not implementation approval. Return findings to Mariko for direct correction.

### Final document-review notes

Resolve the existing nonblocking observations only where they affect delivered text: summaries must agree with the deployment prohibition; any clarification of the high-risk pass's read-only limit must preserve the same product-source/runtime distinction already approved for helpers. No extra authority is granted. The host-local candidate checker is authoring evidence, not a required installed dependency; keep necessary new validation in the existing package tests.

### Verification commands and evidence boundaries

Run from the workspace:

```sh
python3 -B -m unittest discover -s references -p 'test_render_reasoning.py' -v
python3 -B -m unittest discover -s references -p 'test_*.py' -v
git diff --check
```

Use supported background execution with completion notification for the long aggregate suite. Preserve logs outside the shipped package, for example in `/home/mariko/projects/generic-devteam-review/dev-environment-implementation/`. Native synthetic test guards remain binding; a denied or skipped check is missing evidence, not a pass.

Package authoring permits isolated existing test fixtures, not live profile, gateway, Hindsight, tunnel, host or container operations. No Docker/PostgreSQL/live-model qualification is commissioned in this task. The skill must retain its eventual runtime acceptance cases; completion here proves package integration and static contracts only. Do not claim skill adherence or an operational environment.

### Git and handoff

Work in the existing branch and checkout. Preserve all untracked specifications and review reports. Do not initialize Git, switch/reset branches, stage, commit or push. Max has authorized implementation, not a Git commit. Isolated test-fixture commits used by existing tests are not changes to project history.

Bind review to starting HEAD plus the exact final tracked diff and every new package file, using a SHA-256 manifest saved outside the shipped package. Re-read HEAD and working-tree state before handoff to detect concurrent user changes. An empty `git diff` cannot account for new files. Provide Fujiko the complete changed-file list, accepted specification, actual checks and limitations in a review-only assignment; uncommitted work is the authorized deliverable.

Report package implementation, executed checks and independent review separately. No live-team rollout or implementation delegation is implied.
