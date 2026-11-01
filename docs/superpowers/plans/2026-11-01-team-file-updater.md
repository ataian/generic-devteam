# Team File Updater Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this approved plan inline. Do not dispatch subagents.

**Goal:** Add a user-triggered, per-team three-way file updater without changing live teams.

**Architecture:** Keep private installation records and immutable personalized Maker baselines in the planner's existing `devteam/` directory. Use the manifest and role renderer to produce explicit mappings. Save reviewable proposals before applying guarded writes with backups and exact readbacks.

**Tech Stack:** Python standard library, Git, existing unittest suite.

**Spec:** Approved Auftrag 1 and Max's final baseline and SemVer correction in the task handoff. Do not implement Auftrag 2.

## Global Constraints

- Change repository files only.
- Do not push or modify live profiles.
- Keep all role templates unchanged.
- Use package SemVer `1.1.0` for this compatible feature.
- Use `1.0.0` at `21cae6551c03b6ab84d004f41fc81c921e3e9837` as the user-defined legacy SOUL safepoint.
- Do not claim that the user-defined safepoint proves historical installation.
- Do not assume the same baseline for legacy skills.
- Do not stop workers, restart sessions, delete obsolete files, or prune backups.
- Apply TAS to all new or changed agent-context Markdown instructions.

## Review Focus

- Preserve local edits and stop on conflicting edits.
- Reject traversal, symlinks, duplicate targets, and stale proposals.
- Keep metadata at the old revision after partial failure.
- Require an explicit proceed or skip decision for active or unknown activity.
- Require agent semantic review and user decisions for operational dependencies.

## Task 1: Record and compare

**Files:** Create `references/update_team.py`, `references/test_update_team.py`, and `references/update.md`.

**Interfaces:** CLI `discover`, `legacy-baseline`, `init`, `plan`, `apply`, and `rollback`. Exercise Python helpers through isolated temporary Git repositories and profile trees.

- [x] Write and run failing tests for records, mapping coverage, legacy provenance, and three-way merges.
- [x] Implement Git-bound source rendering, private state, and explicit mapping validation.
- [x] Write and run failing tests for conflicts, activity, semantic review, dependencies, drift, backups, failures, and rollback.
- [x] Implement proposal, application, and rollback without a global success marker or file deletion.
- [x] Run the final updater and existing package tests.

## Task 2: Integrate and verify

**Files:** Create project `AGENTS.md`. Modify `manifest.json`, `SKILL.md`, `README.md`, `references/setup.md`, `references/verification.md`, and `templates/setup-record.md`.

- [x] Add setup recording, update discovery, and verification instructions.
- [x] Add the project SemVer rule and synchronize both package version fields.
- [x] Verify package inventory, syntax, whitespace, TAS wording, and unchanged role templates.
- [ ] Commit only task files locally.
- [ ] Run the baseline CLI and package tests after the real commit.
- [ ] Write the implementation report to the requested scratch path with exact CLI output, limits, and commit ID.

## Decisions during implementation

The final user correction replaces the earlier updater-introduction baseline proposal.
The implementation has no self-referential introduction hash or separate release counter.
Visible process matches establish activity, but their absence leaves activity unknown.
The CLI therefore requires an explicit activity decision for every apply or rollback.
The parent agent performs the independent review after this task.
