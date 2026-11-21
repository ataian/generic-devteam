---
name: dev-environment
description: Create, adopt or revise a containerized coding environment.
version: 0.3.0
author: Max, Mariko (Hermes Agent)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [development, docker, compose]
    related_skills: []
---

# Containerized project toolchain

- Trigger: the customer asks the Planner to create, adopt or revise a coding environment.
- Purpose: containerized build and test tools for the working checkout. Do not install these tools on the host. The container is not an agent sandbox.
- Developer workflow: edit the checkout, run targeted tests and optionally start the app from source for local feedback.
- Built-image demos and end-to-end tests use the project's deployment configuration; the demo handover card is that authorization.

## Plan from the developer's task

1. Read project instructions, manifests, lockfiles, CI commands and existing Compose definitions. Distinguish source tools from services running built images.
2. Find the shortest path from edit to build and selected test. Resolve missing Docker access with the operator.
3. Reuse a working toolchain and entrypoint. If absent, plan the tools under `docker/dev/`. If incomplete, fix only the gap within the accepted scope. Preserve local inputs and data. Documentation-only adoption authorizes no rebuild.
4. Hand the agreed workflow to the Coder and independent Reviewer through existing planning.

## Build for repeated edits

- Bind-mount the current checkout directly into the tool container. Edits, untracked files and new test resources must appear without staging, copying or synchronizing. Write generated files as the invoking user.
- Toolchain: use native build and test commands, required versions and the project's usual selector for new tests. Reuse tools and dependency caches. Rebuild the tool image only when its inputs change.
- Inputs: keep machine-specific values local and ignored. Track portable, secret-free defaults. Name missing required inputs without printing values. Exclude secrets from image builds and served artifacts. Bind local listeners to loopback by default.
- Database: add a project-compatible database to development Compose only if needed for coding. Use synthetic data and verify the dev target before writes. If branch databases are agreed, select the matching database and preserve its state on return. Reset only the selected disposable state.
- Permissions: reuse project services and helpers within existing permissions. Additional services, host administration and Docker socket access require their own agreed scope.

## Hand over one operating guide

- Guide: one short `docker/dev/AGENTS.md`, or the actual guide path in an adopted layout.
- Entrypoint: give the guide one script with one verb per operation (`docker/dev/dev.sh up`, `stop`, `test`, `reset`). A compound command line, or `$` expansion inside double quotes, never matches an agent grant.
- Content: only environment-specific changes to the coder's workflow. Use one line per operation with a short label and exact invocation. State non-obvious targets or destructive effects where relevant.
- Occasional operations: point to existing helper commands or their help. Keep implementation detail and acceptance evidence out of recurring context.
- Loader: root `AGENTS.md` requires the guide by repository-relative path when a task uses the environment.

## Verify the developer workflow

- Documentation-only adoption: check the existing entrypoint, report gaps and leave the setup unchanged.
- Toolchain change:
  1. The Coder prepares one reversible source change and a new, untracked targeted test in a disposable checkout with synthetic test data.
  2. The Reviewer follows the guide in a disposable checkout, runs a real project build and checks both source states independently with the Coder's probe. Rerun the selected test after the edit. Its result must reflect the change without staging files or rebuilding the tool image.
- Verify source startup or branch selection when included in the accepted task. Record results and any unverified capability on the existing task. Acceptance ends at the developer workflow.
- Demo handover: separate closure step with its own card, not an environment acceptance case; it runs the built application through the app compose.
