---
name: dev-environment
description: Create, adopt or revise a Docker dev environment.
version: 0.1.0
author: Max, Mariko (Hermes Agent)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [development, docker, compose]
    related_skills: []
---

# Docker development environment

## When to use

Use when the customer asks the Planner to create, adopt or revise a project's Docker development environment.
For ordinary development, use the project's agent operations guide.

## Prerequisites

Use the configured team's planning, implementation and independent-review workflow.
Hermes, Team-Codex, Git and Docker run on the Linux host; project toolchains run in containers.
Inspect existing Docker/Compose access. Missing host capabilities are prerequisites to resolve with the operator, not permission to install or reconfigure the host.
This skill covers project tooling, application runtime and an optional development database.
Additional third-party services or simulators belong to separately agreed project-specific work.

## Operating scope

Bind the assigned development resources and their data classification in the project agent guide.
The team may start, stop, restart, rebuild and recreate these resources without further customer approval.
The team may generate synthetic data and reset disposable development state for tests and demonstrations.
Coordinate disruptive operations with other team users of the same runtime; this needs no customer approval round.
Preserve source work, credentials, operational data, unrelated resources and the PostgreSQL baseline during ordinary branch work.
Host administration, shared infrastructure and external effects retain their existing authorization boundaries.
Building and running a candidate in the assigned development runtime for tests or demonstrations are development operations, not publication or deployment.
Role responsibilities remain unchanged: implementation belongs to the Coder/Team-Codex; the Reviewer operates the runtime without repairing product code.

## Procedure

1. **Locate and classify.** Resolve the project workspace and each affected Git root independently.
   Read applicable AGENTS.md files, manifests, lockfiles, CI build/test commands and existing development definitions.
   Distinguish development tooling from deployment packaging; inspect only nonsecret configuration sources.
   Classify the requested environment as absent, usable, or incomplete/incompatible; an inspection failure is not absence.
   Done: repository root, current entrypoint, required toolchain and concrete gaps are known.

2. **Set the project contract.** For a new environment, settle unresolved stack choices and development/test needs through the Planner's existing customer clarification path.
   Reuse decisions already established by project rules and manifests; surface conflicts rather than silently upgrading the stack.
   Identify database needs, test/demo data, browser checks and host architecture.
   Reuse the project's database engine and compatible version; settle a missing engine choice with the customer.
   For PostgreSQL, establish the template's initialization and permitted data source; operational data requires a separate explicit authorization.
   Identify dependencies outside this skill's scope and state their effect on supported checks and demonstrations.
   State separately which checks and application workflows the environment will support.
   Done: the customer-owned choices and authorized service/data boundaries are settled through the existing planning process.

3. **Choose the construction path.**
   - **Create:** plan the smallest environment meeting the project contract, using the construction criteria below. Default to `docker/dev/` under the code repository root.
   - **Adopt:** derive commands and configuration from the existing definitions and project scripts. Preserve working layout, local inputs and data. If the development database is externally managed, plan its bounded integration or resolve retention with the customer. A documentation-only task preserves the current database and reports this gap; do not claim integration or create a competing stack.
   - **Incomplete:** preserve reusable parts and name the precise missing capability. Obtain the required decision before repairs outside the accepted scope.
   Use the existing accepted-plan handoff for implementation and independent review; this skill adds no separate approval process.
   Done: each required capability, guide and verification outcome has an owner in the accepted task; existing operational rules agree with the assigned development scope.

4. **Build or bind.** Have the Coder/Team-Codex implement the accepted environment or its bounded adoption changes.
   Use the construction criteria only for new or modified components; a documentation-only adoption does not authorize a redesign.
   Missing local inputs must produce a useful error naming the input and preparation step, without printing secrets.
   Done: the declared commands and local configuration mechanism exist, and preserved state remains intact.

5. **Write the two guides.** Have the Coder/Team-Codex produce both documents from the actual commands and configuration.
   - `docker/dev/AGENTS.md`: concise executable commands for readiness/resume, build, tests, start/stop/restart and required regeneration. Name assigned resources, disposable data and the operating scope above. Include dependency refresh, image rebuild, synthetic seeding, reset and demo-access commands. For PostgreSQL, include template preparation and branch database create/select/resume commands. State working directory, local configuration location and essential target conditions. Use one canonical command per operation; omit setup history, implementation explanations and copied run logs.
   - `docker/dev/HOWTO-human.md`: standalone instructions for a human using Linux without agents. Cover prerequisites, first setup after clone, local configuration, ordinary development/tests, database preparation and branch switching where applicable, synthetic data, pause/resume, demo access, updates and relevant troubleshooting. Explain each required local value, its source, and whether it is secret or generated.
   Keep the agent guide self-contained for ordinary work. Its references and the root agent pointer lead only to operational sources needed for that work.
   Add or reconcile a short root AGENTS.md pointer requiring the agent guide for development planning, implementation and review. Require its container commands for builds, tests and development servers. Use the actual repository-relative path.
   Keep shared commands portable; resolve machine-specific inputs through `.local/` rather than copying one developer's values into tracked instructions.
   Done: both audiences can follow their own guide, with no unresolved command placeholders; existing instructions agree with the new entrypoint.

6. **Verify and hand over.** Have the independent Reviewer check the acceptance cases below against the final candidate.
   Keep outcomes and limitations in the existing task; no additional evidence handbook is required.
   Report established capabilities, missing checks and required local inputs. Distinguish repository delivery from publication and live use elsewhere.
   For a customer demonstration, verify application readiness and provide the concrete browser URL and SSH local-forward command when needed.
   Derive the command from confirmed SSH access and actual loopback ports; verify the service endpoint and disclose any untested client-side access.
   Leave the demonstrated application running for customer use; coordinate later disruptive operations through the team.
   Done: every promised capability has execution evidence or is explicitly reported as unverified; required missing evidence prevents a readiness claim.

## Construction criteria

- **Toolchain:** derive compatible versions from project rules, manifests and lockfiles. Pin image/tool inputs reproducibly using suitable existing project conventions; preserve dependency resolution semantics.
- **Compose:** keep development services separate from production deployment. Use project-scoped resources and configurable local ports/identity so another checkout can coexist without sharing mutable data accidentally. Prefer Compose service lifecycle management over a new process supervisor.
- **Source and identity:** bind the local checkout read/write where required. Resolve its location on each machine; support the user's UID/GID without requiring unused IDs in the base image or recursively changing source ownership.
- **Reuse:** keep tool containers available for repeated `exec` operations. Preserve caches and isolated container dependencies across stop/start. Refresh dependencies when their inputs change; rebuild tools when tool-image inputs change, not for ordinary source edits.
- **Local inputs:** track secret-free configuration examples and ignore `.local/`. Separate portable defaults from local overrides; explain whether each local file is supplied or generated. First setup must preserve existing local configuration and state. Respect existing application configuration paths when adopting a project.
- **Isolation:** exclude secrets and private state from build contexts and published artifacts. Publish development listeners only on loopback by default. Keep test targets separate from operational databases and prevent unapproved outbound effects.
- **Database:** when required, include the compatible database service and persistent storage in the same development Compose project. Use its internal service address from application containers and project-scoped state. Provide readiness, initialization and synthetic seeding through documented commands. For PostgreSQL, apply the branch workflow below; other engines retain their native project workflow.
- **Nested test containers:** when required, verify daemon access, mount-path semantics, connectivity and normal test cleanup. Docker socket access grants host-level authority; make that boundary part of the accepted design rather than mounting it by default.
- **Simplicity:** reuse native Compose and project commands. Add a helper only for a demonstrated operation they cannot express safely and clearly. Routine pause/resume retains state; explicit resets affect only the assigned disposable development state.

## PostgreSQL branch databases

1. **Prepare the baseline.** Build a reproducible template from the project's agreed schema and permitted data source.
   Document how to prepare or deliberately refresh the baseline separately from branch work.
   Done: the template and creation role exist with the required privileges; the application does not target the template.
2. **Create once per branch.** Map each new development branch to a distinct PostgreSQL-safe database name within its environment.
   Include collision handling for branch-name normalization and database identifier limits.
   Use PostgreSQL template cloning, such as `createdb --template=<template> --owner=<role> <branch_database>`, inside the development database service.
   Check source sessions, privileges and target absence before creation; let PostgreSQL reject concurrent conflicts.
   Quiesce connections owned by the assigned development runtime when needed. Coordinate unknown or external connections rather than terminating them.
   Reuse an existing target only when its recorded branch binding matches; preserve an ambiguous target and resolve the collision.
   Done: the branch has its own snapshot database and an unambiguous local binding; no existing database was overwritten.
3. **Select and resume.** Before application writes, select the current branch's database in local configuration and restart affected application processes.
   Verify the actual database and role before migrations, seeding or write tests.
   Returning to a branch reuses its database and state rather than cloning again.
   Done: the running application uses the correct branch database; other branches and the baseline remain unchanged.
4. **Test and reset.** Apply development migrations and synthetic test/demo data to the selected branch database.
   Keep independent synthetic test-container suites independent; do not redirect them all to the branch database.
   Reset only explicitly selected disposable branch/test state when needed. Routine branch switches and pause/resume retain it.
   Done: the intended test/reset outcome is verified without altering the baseline or another branch.

## Acceptance cases

- **Fresh checkout:** exercise setup from tracked files plus documented local inputs in a separate Linux checkout path. Do not reuse undeclared dependencies or caches from the original checkout. Verify the supported user identity and architecture, writable source without root-owned artifacts, and isolated resources. State any untested host/architecture boundary.
- **Functional use:** run a real build and the agreed relevant tests in the containers. Check application readiness, database connectivity and browser behavior where included. A version command, running container or skipped test is not that evidence.
- **Reuse:** repeat ordinary commands and pause/resume. Verify reuse of the tool container and retained dependencies/caches without rebuilding or reinstalling. Temporary test containers may differ between runs.
- **Safe adoption:** use the actual existing entrypoint. Confirm expected mounts, local endpoints and test targets without disclosing credentials; preserve external data and unrelated services. Verify any accepted database integration separately. Repairs remain bounded by the accepted task.
- **Missing input:** omit a required local input in an isolated test setup. Confirm an actionable failure before application writes, with no secret disclosure or overwrite of another local configuration.
- **Audience separation:** exercise routine commands using only the agent guide and its operational sources. Check the human guide independently from first setup through normal use. Agent instructions contain no pointer to the human guide and no instruction prohibiting its reading.

- **Integrated database, when required:** start the database through the development Compose entrypoint. Verify readiness, application access, synthetic seeding and persistence across restart without an undeclared external database.
- **PostgreSQL branches, when PostgreSQL is used:** create two branch databases from the agreed template. Change one, then verify the baseline and the other branch remain unchanged. Switch away and back, confirming target selection and retained state. Exercise a naming collision and a connected-template failure without overwriting data or terminating unrelated sessions.
- **Runtime autonomy:** exercise restart, rebuild and a disposable-state reset through the agent guide. Verify the intended result and preservation of resources outside that operation's scope. Check that role instructions require no new customer approval for these actions.
- **Demonstration:** leave the application running, verify its local endpoint, and exercise the documented access path where client access is available. Provide the browser URL and concrete SSH forwarding command; identify an untested client boundary rather than claiming end-to-end access.

## Pitfalls

A repository bind mount exposes local ignored files too; Git exclusion is not a sandbox.
A fixed Compose project name can collide across checkouts; local identity must be stable for resume and distinct for independent environments.
Existing infrastructure and safety machinery from one project are evidence to inspect, not templates to impose on every project.
