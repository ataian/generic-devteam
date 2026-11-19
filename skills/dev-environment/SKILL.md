---
name: dev-environment
description: Create, adopt or revise a containerized coding environment.
version: 0.2.0
author: Max, Mariko (Hermes Agent)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [development, docker, compose]
    related_skills: []
---

# Containerized project toolchain

Use this skill when the customer asks the Planner to create, adopt or revise a coding environment.
The container supplies build and test tools that must not be installed on the host. It is not an agent sandbox.
Developers edit the checkout, run targeted tests and may start the app from source for local feedback.
Demos and end-to-end tests of built images use the project's deployment configuration under separate authorization.

## Plan from the developer's task

Read the project instructions, manifests, lockfiles, CI commands and existing Compose definitions. Distinguish tools operating on source from services running built images.
Identify the shortest path from a source edit to a build and a selected test. Resolve missing Docker access with the operator.
Reuse a working toolchain and its entrypoint. If absent, plan the tools under `docker/dev/`; if incomplete, fix only the gap within the accepted scope.
Preserve existing local inputs and data. Documentation-only adoption does not authorize rebuilding the environment.
Hand the agreed developer workflow to the Coder and independent Reviewer through the existing planning process.

## Build for repeated edits

- Bind-mount the current checkout directly into the tool container. Edits, untracked files and new test resources must be visible without staging, copying or synchronizing. Write generated files as the invoking user.
- Use the project's native build and test commands and version requirements. Let the coder select a new test by the project's usual selector. Reuse tools and dependency caches; rebuild the tool image only when its inputs change.
- Keep machine-specific inputs local and ignored; track portable, secret-free defaults. Name a missing required input without printing its value. Keep secrets out of image builds and served artifacts. Bind local listeners to loopback by default.
- Include a project-compatible database in development Compose only when the coding workflow needs one. Use synthetic data and verify the dev target before writes. If branch databases are agreed, select the matching database and preserve its state on return. Reset only the selected disposable state.
- Reuse project services and helpers within their existing permissions. Additional services, host administration and Docker socket access require their own agreed scope.

## Hand over one operating guide

Write one extremely short `docker/dev/AGENTS.md` in Caveman Full style. In an adopted layout, use its actual guide path.
Keep only what a coder needs to do differently to work in this environment: terse label and exact invocation, one line per operation. State a non-obvious target or destructive effect where it matters.
Point to existing helper commands or their help for occasional operations. Leave implementation detail and acceptance evidence out of recurring agent context.
In the root AGENTS.md, require the guide when a task uses the environment. Use its repository-relative path.

## Verify the developer workflow

For documentation-only adoption, check the existing entrypoint and report gaps. Leave the setup unchanged.
For toolchain changes, the Coder prepares one reversible source change and a new, untracked targeted test in a disposable checkout. Use synthetic test data.
The Reviewer follows the guide in a disposable checkout and runs a real project build. Use the Coder's probe to check both source states independently.
After the source edit, rerun the selected test and verify its result reflects the change without staging files or rebuilding the tool image.
Verify source startup or branch selection when included in the accepted task.
Record the result and any unverified capability on the existing task. Acceptance ends at the developer workflow.
