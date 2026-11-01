# Generic Devteam — project context

## Identity

- Project: `generic-devteam` — Maker package for Hermes development teams.
- Canonical project root and working directory: `/home/joi/projects/generic-devteam`.
- Git repository root: `/home/joi/projects/generic-devteam`.
- Historical inspected planning baseline: `a44d15e3aad77b891fa5c95ebeba49a780e4525e`, then on `develop`, package `1.1.4`.
- Required current working branch: `fix/makerscope`. Max moved the planning commits onto this branch and selected it for the implementation work. Verify this branch before edits and commits; do not switch back to `develop` or merge without a separate instruction.
- Mattermost project channel: Max selected the established project-notification channel on 2026-11-01; use its exact ID below.
- Mattermost channel ID: `pd8fjzdqi7rz5czss5sofsgcdr`. Use `chat_type=channel`, `delivery_mode=notify+wake`, and notifier profile `kirk` for each implementation ticket. Do not add a Desktop subscription.
- Hermes Kanban board: `generic-devteam`, created with Max's authorization on 2026-11-01. Its verified default workspace is `/home/joi/projects/generic-devteam`. No separate Hermes Project ID is assigned.

## Current assignment

Max assigned Kirk the planning of a narrower Maker setup responsibility.
Preserve the generated team's capabilities, quality boundaries, setup records, and existing versioned update support.
Remove recurring Maker-development research and behavioral qualification from normal team creation.
Max accepted the written specification in its substantive form from commit `0694e651df32dbe7d5187d6d4105fb2b91819b0c` and authorized implementation planning.
Max approved plan `docs/PLAN_1.0.0_Generic-Devteam.md` for implementation of Phases 1–2 on 2026-11-01. The accepted content is in commit `696418f81aa005db13a9036fa479dd19424c5880`. Phase 3 remains separately gated after Max's practical trial.
Max requires all foreseeable setup choices to be resolved in a grouped interview before installation starts. Later questions are limited to new problems/decisions or technically deferred actions disclosed upfront.
For new profiles, derive a native-compatible lowercase ID from the display name (`Kirk` → `kirk`); ask separately only for conflicts. Preserve existing IDs on resume/update.
Offer the requested defaults as one set: Planner Sol/high; Hermes Coder fixed Sol/medium; Reviewer and Team-Codex Sol/medium with maximum high. The Coder selects Codex reasoning per task under the existing risk matrix, without changing model or provider. Do not add a separate Coder maximum or extend renderer/updater fields. Resolve native model IDs separately and preserve confirmed overrides.
After the two implementation phases and reviews, pause for Max's practical setup trial. Do not begin cleanup automatically.
Keep this file and the planning artifacts until that trial and separate cleanup authorization. The planned final cleanup removes temporary local context/planning files from the tracked tree, not Git history or functional Maker/update assets.

Read [the accepted design specification](docs/specs/2026-11-01-maker-setup-scope-design.md) and [the approved implementation plan](docs/PLAN_1.0.0_Generic-Devteam.md) for the exact scope and evidence.
Implementation tickets for Phases 1–2 are authorized with the routing above. Live-team changes, practical trial execution, cleanup, publication, and deployment are not authorized by this approval.
Verify ticket routing, subscriptions, and the serial dependency chain before releasing Phase 1.

## Repository rules

Read `AGENTS.md`, `README.md`, and `references/tas-authoring-standard.md` before changes.
Apply `references/tas-authoring-standard.md` to every new or revised text in each phase.
Use plain technical English for agent-facing instructions; retain the user-facing language rule.
Limit TAS review to the changes made for the phase. Do not audit, translate, or rewrite unchanged text solely for TAS compliance.
Keep versioned planning documents under `docs/` outside the ignored `docs/superpowers/` subtree.
Planning documents are not part of the delivered Maker manifest and do not independently bump the package version.
Apply the existing package SemVer rules when delivering an actual Maker changeset.

Kirk writes planning/project-context documents, not Maker implementation or application code.
Scotty implements an explicitly approved plan; Julia reviews that implementation independently.
Preserve unrelated working-tree changes and existing Git history.
Commit only the intended local changes.
Local commits do not authorize remote publication, rollout, service changes, or deployment.

## Scope boundaries

The Maker repository and generated/live team profiles are separate targets.
The default profile's installed launcher is outside this repository at `/home/joi/.hermes/skills/devops/generic-devteam/SKILL.md`.
Reading that launcher does not authorize editing it or any other profile.
Keep launcher rollout and existing-team updates separate from repository implementation.
Do not modify shared Hermes dependencies, identities, secrets, services, or production configuration through this planning assignment.
Preserve private team setup/update records outside project Git; store no secrets in project documentation.
