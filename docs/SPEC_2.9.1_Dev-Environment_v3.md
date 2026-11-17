# Docker development environment skill — draft

Document version: v3 — corrections from Fujiko review round 1; development-runtime autonomy and database scope preserved.
Supersedes `SPEC_2.9.1_Dev-Environment_v2.md`; earlier drafts and `REVIEW_2.9.1_Dev-Environment_v1.md` remain unchanged.
Status: proposed; not installed, implemented in the Maker, or approved for rollout.
Baseline: Maker 2.9.1, commit `94ded22fa58b1c41956985c3edd562c443bae7af`. Tracked package files are unchanged; v1 is an untracked discussion draft.
Authoring: TAS checkout `git@github.com:ataian/tas.git`, commit `fe3a7d251518b793fedaec3041558c2840b4c796`; clean working tree. Entrypoint, authoring standard, Caveman and skill mechanics read.

## 1. Goal and confirmed decisions

As a project owner, I want the configured team to establish or adopt a reusable Docker development environment, so agents and human developers can build and test the same checkout without installing the project toolchain on the host.

- Target Linux hosts running Hermes. Hermes, Team-Codex, Git and Docker remain on the host.
- The Planner receives the generic construction/adoption skill through the Maker. The existing Coder/Team-Codex and independent Reviewer perform implementation and acceptance.
- Distinguish project workspace from code repository root. Default location: `docker/dev/` relative to the confirmed code repository root.
- Handle both a missing environment and an existing environment. Discuss unresolved stack choices with the customer; derive existing constraints from AGENTS.md and current manifests.
- Keep portable environment definitions in the shared project repository. Keep machine-specific configuration, credentials and runtime state in Git-ignored `docker/dev/.local/`.
- Produce exactly two development-environment guides: compact `docker/dev/AGENTS.md` for agents; standalone `docker/dev/HOWTO-human.md` for humans working without agents.
- Root AGENTS.md directs development planning, implementation and review to the agent guide. Runtime agent instructions neither mention nor link the human guide. No explicit prohibition against reading it.
- When a project has a development environment, the Planner makes reading its agent guide and using that environment binding in relevant tickets. If no environment exists, omit that requirement; absence alone adds no work blocker. Role SOULs explicitly permit operation of an assigned development environment; their implementation and independent-review boundaries remain intact.
- Environment authors and reviewers create, read and maintain both guides. Filename separation is information routing, not an access-control guarantee.
- Reuse tool containers, installed dependencies and caches during ordinary work. Temporary isolated test containers remain valid where the project needs them.
- When the project needs a development database, include its compatible engine directly in the development Compose project. A separately managed external database is not the default construction pattern.
- For PostgreSQL, create one template-derived database per new development branch. Reuse its database on return; keep the baseline separate from branch writes.
- The team may generate synthetic test/demo data. Template provenance and initialization follow the project contract; permission to generate synthetic data does not authorize importing operational data.
- The assigned development runtime is the team's tool. Start, stop, restart, rebuild, recreate, seed and reset disposable development resources without repeated customer approval.
- This authority covers project-local development containers, images, volumes and synthetic runtime data. Source-code ownership, real user data, unrelated resources and host administration retain their existing boundaries.
- The team may use the environment for tests and customer demonstrations. Leave a demonstrated application running and provide its verified URL and concrete SSH local-forward command when needed.
- Additional third-party services and simulators are project-specific work for the customer and team, outside this Maker skill's construction scope.

This draft proposes future team authority; it does not authorize executing container operations, installation, host or profile changes, publication or deployment during this documentation task.

## Withdrawn from v1

- Constructing arbitrary third-party services or simulators: excluded at the customer's request. The generic environment covers project tooling, application runtime and an optional database.
- Keeping Coder and Reviewer SOULs unchanged: withdrawn because the Coder requires separate operational approval and the Reviewer forbids service restarts. Section 5 replaces the conflicting clauses and clarifies review-helper runtime permissions.
- Excluding the database-cloning pattern as MTB-specific: withdrawn for PostgreSQL. Branch template cloning is reusable; MTB's external Compose, dataset and infrastructure remain project-specific.
- Treating every reset as a separate permission request: replaced by standing authority over the assigned disposable development runtime. Routine pause/resume still retains state.

## 2. Recommended shape

**One Planner skill, two generated project guides.** Keep the first skill self-contained; add references only when a real conditional procedure justifies them. The Planner passes the applicable environment requirements into the accepted implementation task, rather than installing the construction skill into every role.

Alternatives considered:

| Approach | Trade-off | Disposition |
| --- | --- | --- |
| Planner construction skill plus repository agent guide | Separates occasional setup reasoning from recurring use; all agents share one short project contract. | Recommended. |
| One setup-and-use skill installed into every role | Repeats construction details during routine development; couples project commands to role-profile distribution. | Not selected. |
| Universal environment generator and mandatory command wrapper | Could standardize commands, but adds a framework before supported project shapes are known. | Not selected. Reuse native Compose and existing project commands. |

The default layout is intentionally small:

```text
docker/dev/
  compose.yaml
  Dockerfile                  # one or more, as the stack requires
  .dockerignore               # aligned with the actual build context
  .gitignore                  # excludes .local/
  AGENTS.md                   # agent operations only
  HOWTO-human.md              # human setup and operations
  config.example.env          # example name; only when configuration is needed
  .local/                     # untracked local inputs and runtime state
```

Existing compatible layouts are adopted rather than relocated merely to match this tree. Both new guides still default to `docker/dev/` and name the actual Compose entrypoint. Scripts are optional, justified by repeated error-prone operations rather than by this layout.

## 3. Proposed skill text

Proposed package path: `skills/dev-environment/SKILL.md`. The following fenced block is the complete candidate, not an active skill file.

````markdown
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
````

## 4. Proposed root agent pointer

Generated into the target repository's existing root AGENTS.md, reconciled with any existing development-environment clause:

> For development planning, implementation and review, read `docker/dev/AGENTS.md`. Use its container commands for builds, tests and development servers.

No human-guide filename, negative reading instruction, setup narrative or copied command table accompanies that pointer. The environment's AGENTS.md is versioned, not a second per-profile skill. The same file is the source for Planner, Coder, Reviewer and Team-Codex. Explicit loading is required; the design does not assume nested AGENTS.md auto-loading.

## 5. Maker integration proposed for a later changeset

| Surface | Proposed change | Existing basis / verification |
| --- | --- | --- |
| `skills/dev-environment/SKILL.md` | Add the candidate as an owned Planner-only skill. | New file; no universal generator or mandatory helper. |
| `manifest.json` | Add file membership and `own_skills.dev-environment`, with `targets.hermes = [planner]`, unchanged SKILL.md transport and owned provenance. | Existing owned-skill schema and `references/update_team.py` iterate assigned complete skill trees. |
| `references/upstream-sources.md` | Add the owned component and Planner assignment to the source/role matrix. | `references/setup.md` uses that matrix for complete-tree copying. |
| `templates/roles/planner.SOUL.md.template` | Add skill invocation (R7) and conditional ticket-guide use (R8); distinguish assigned development operation from external approvals and include demo access (R1, R6). | Exact replacements R1, R6, R7, R8 below. |
| `templates/roles/coder.SOUL.md.template` | Replace the blanket operational approval clause with assigned-development authority; pass it to Team-Codex. | Exact replacements below; productive code still goes through Codex. |
| `templates/roles/reviewer.SOUL.md.template` | Replace the blanket restart ban; distinguish read-only product sources from mutable test runtime for review and helpers. | Exact replacements below; no self-repair, self-approval, push or external deployment. |
| `SKILL.md` | Refine the existing optional first-task offer to name development-environment creation/adoption. | Current final handoff offers a first planning task and does not start it automatically. Retain that boundary. |
| `README.md`, `NOTICE.md` | Update the owned component overview and provenance where applicable. | No SG1-specific hosts, networks, credentials or local paths in delivered instructions. |
| `references/test_render_reasoning.py`, `references/test_update_team.py`, `references/test_brownfield_planning.py` | Extend the exact role matrix and delivery/update coverage. In `test_plan_separates_binding_scope_from_coder_discretion`, update only the Planner `soul_clause` assertion at line 165 to the R1 NEU sentence. Preserve the existing `assertNotIn` checks. | The current Planner assertion pins the replaced wording; after R1 it must assert `For other resources, do not infer permission to mutate them from permission to inspect them.` |
| New focused package contract tests | Cover create/adopt, guide separation, root pointer, database inclusion, PostgreSQL isolation, runtime authority, demo handoff and retained role boundaries. Assert the shared authority paragraph is identical across the three role templates. | Follow `references/test_devteam_cleanup.py`; distinguish static contracts from agent behavior. |
| `SKILL.md` and `manifest.json` versions | Apply one compatible-feature MINOR bump when implementing the package changeset. | No package bump for this repository-only discussion draft. |

R7 binds skill invocation in the Planner workflow. R8 binds guide use at ticket authoring only when an environment exists. Creating an environment remains a separately accepted task. Keep concrete commands in the project guide, not in SOULs or repeated ticket instructions.

The construction skill is delivered only to the Planner. Coder and Reviewer receive the applicable construction/verification requirements through the accepted task. Routine agent use needs only the repository guide. The human guide is an output of the environment task, not a role-profile dependency.

Existing-team delivery follows the existing authorized updater. It does not automatically run the skill, rebuild an environment or change the project's guides. Native discovery and first-use behavior remain qualification checks for implementation, not claims established by this document.

### Role-authority reconciliation

These are proposed source replacements, not live SOUL changes. Each ALT block must match exactly once at implementation time. The same bounded authority is present in each role because each receives its own SOUL. Runtime commands and resource identities remain in the project guide.

#### R1: `templates/roles/planner.SOUL.md.template:12`

Give the Planner the same bounded runtime authority without granting product implementation or external access.

ALT:

```text
- Do not infer permission to mutate a resource from permission to inspect it.
```

NEU:

```text
- When the project has an assigned development environment, operate its runtime under the project agent guide without further customer approval. This includes start, stop, restart, rebuild, recreation, synthetic data generation and disposable-state reset for tests or demonstrations. Keep source ownership, operational data, host administration, shared infrastructure and external effects within their existing boundaries. Coordinate disruptive operations with other team users. Building and running a candidate in the assigned development runtime for tests or demonstrations are development operations, not publication or deployment.
- For other resources, do not infer permission to mutate them from permission to inspect them.
```

#### R2: `templates/roles/coder.SOUL.md.template:77`

Replace the repeated operational approval trigger at its source; preserve external-operation and native-tool boundaries.

ALT:

```text
- A coding ticket alone does not grant operational approval. If the customer separately and explicitly approves operational actions, you can execute them within the confirmed scope. Tool and system prohibitions remain binding.
```

NEU:

```text
- When the project has an assigned development environment, operate its runtime under the project agent guide without further customer approval. This includes start, stop, restart, rebuild, recreation, synthetic data generation and disposable-state reset for tests or demonstrations. Keep source ownership, operational data, host administration, shared infrastructure and external effects within their existing boundaries. Coordinate disruptive operations with other team users. Building and running a candidate in the assigned development runtime for tests or demonstrations are development operations, not publication or deployment.
- Outside that development scope, a coding ticket alone does not grant operational approval. Execute operational actions only within separately confirmed customer authorization. Tool and system prohibitions remain binding.
```

#### R3: `templates/roles/coder.SOUL.md.template:24`

Carry the granted authority into Team-Codex, which does not automatically receive the Coder SOUL.

ALT:

```text
5. Provide Codex with the concrete goal, current evidence, file scope, constraints, acceptance criteria, and verification plan.
```

NEU:

```text
5. Provide Codex with the concrete goal, current evidence, file scope, constraints, acceptance criteria, and verification plan.
   When an assigned development environment exists, include its agent-guide path and the development-runtime authority from Exception routing.
```

#### R4: `templates/roles/reviewer.SOUL.md.template:86`

Permit independent runtime verification while preserving the ban on product repair and external operations.

ALT:

```text
- Never self-implement, self-approve, or extend product scope. Do not push, deploy, restart services, or change host configuration from a review task.
```

NEU:

```text
- When the project has an assigned development environment, operate its runtime under the project agent guide without further customer approval. This includes start, stop, restart, rebuild, recreation, synthetic data generation and disposable-state reset for tests or demonstrations. Keep source ownership, operational data, host administration, shared infrastructure and external effects within their existing boundaries. Coordinate disruptive operations with other team users. Building and running a candidate in the assigned development runtime for tests or demonstrations are development operations, not publication or deployment.
- Never self-implement, self-approve, or extend product scope. Do not push, deploy, operate unrelated services, or change host configuration from a review task.
```

#### R5: `templates/roles/reviewer.SOUL.md.template:43`

Read-only describes product sources, not test data or runtime state; shared restarts remain coordinated within the team.

ALT:

```text
Require read-only investigation and findings, evidence, and gaps only to you. Helpers must not implement, issue Kanban transitions, or enlarge scope or permissions.
```

NEU:

```text
Require read-only product-source investigation and findings, evidence, and gaps only to you. Helpers may operate assigned test runtimes within your development authority; coordinate shared runtime changes through you. Helpers must not implement, issue Kanban transitions, or enlarge scope or permissions.
```

#### R6: `templates/roles/planner.SOUL.md.template:104`

The concise-report rule must still allow the access instructions needed to use the delivered demonstration.

ALT:

```text
- When the last required ticket is DONE, confirm the required plan tickets completed and send a short Mattermost customer report. Name only what deviated from the plan: unplanned decisions, found gaps, reported test limits, carried limitations. Do not restate planned steps or successful checks. State separately what publication still requires.
```

NEU:

```text
- When the last required ticket is DONE, confirm the required plan tickets completed and send a short Mattermost customer report. Name only what deviated from the plan: unplanned decisions, found gaps, reported test limits, carried limitations. Beyond that, for a running customer demonstration, include the verified browser URL and concrete SSH local-forward command when needed; disclose any untested client-side access. Do not restate planned steps or successful checks. State separately what publication still requires.
```

#### R7: `templates/roles/planner.SOUL.md.template:48`

Bind environment-skill invocation after the existing design checks; preserve the prototype-only exception and its contiguous instructions.

ALT:

```text
   Use these checks within existing design work, not a new architecture phase or approval gate.
```

NEU:

```text
   Use these checks within existing design work, not a new architecture phase or approval gate.
   When asked to create, adopt or revise a project's Docker development environment, load the owned `dev-environment` with `skill_view(name="dev-environment")`.
```

#### R8: `templates/roles/planner.SOUL.md.template:77`

Make guide loading and container use explicit when authoring relevant tickets.

ALT:

```text
   Structure concise bullets as goal/context, acceptance criteria, technical implementation, verification, and dependencies plus exact plan/phase/commit binding.
```

NEU:

```text
   Structure concise bullets as goal/context, acceptance criteria, technical implementation, verification, and dependencies plus exact plan/phase/commit binding.
   When the project has a development environment, include its agent-guide path in each relevant ticket. Require reading that guide and using its container commands for builds, tests and development servers. Without an environment, omit this requirement; do not block ordinary work or require setup.
```

### Related clauses checked

- Planner role boundaries still reserve product implementation for the Coder. Its existing no-repeat-approval rule agrees with the development mandate.
- Coder role authority points to Exception routing for service changes; replacing that source reaches the existing caller without duplicating its policy.
- Reviewer source-read-only and no-self-repair rules remain. Its helper read-only limit is clarified by R5; runtime mutation does not authorize code changes.
- Reviewer external one-shot approvals remain nonrenewable. Assigned development operation is a standing scope, not a consumed external allowance.
- Existing publication/deployment gates remain: local test/demo runs are explicitly classified as development operations, not a new external deployment.
- Missing environments create no obligation to install one. The conditional authority has no effect until an environment is assigned.

### Implementation checks for the replacements

Check all three rendered role SOULs, their project-guide loading path and the Team-Codex prompt handoff. Keep the existing native runtime guards. Extend package tests to cover allowed runtime actions and preserved source/external boundaries; a keyword match alone is insufficient.

Rehearse: Coder restart, Reviewer database seeding/reset, review-helper test execution, Planner demo handoff, absent environment, and attempted host/shared-service mutation. The first actions remain within assigned development authority; absence imposes no setup blocker; host/shared mutations remain outside it. Independent review still cannot repair product code.

## 6. Evidence from SG1 and deliberate exclusions

Read-only sources inspected:

- Planner setup conversation `20261109_182335_7691a0` in profile `jack`, including the customer's container-reuse and host-Codex decisions.
- Original construction brief: `/home/mariko/projects/mtb/docs/MTB_Entwicklungsumgebung_Docker.md`.
- Current example under `/home/mariko/projects/mtb/de.uke.iam.mtb/docker/dev/`: README.md, compose.yaml, Dockerfile and .gitignore.
- Workspace/repository HERMES.md and AGENTS.md; Maker role template, source matrix, setup and updater mapping.

The SG1 README mixes setup, routine use, runtime internals and recovery. Its Compose file requires an external project-specific network. The described configuration switching includes Linux write leases and rename exchange. These explain why merely shortening that README would not produce a generic environment recipe.

Retain the reusable concepts: host-side agents, container toolchains, persistent dependencies, explicit local configuration, PostgreSQL template cloning, independent review and real command execution. The user confirmed integrated Compose databases and branch cloning for this draft. Do not generalize MTB's external database Compose, operational dataset, relay topology, token simulator, process supervisor, application gates, exact tool versions or fixed network names. A project may still need such mechanisms when its actual requirements establish the need.

SG1 conversion is a separate task. This proposal does not claim its current environment is broken or that a simpler replacement has already been verified.

## 7. Draft review and implementation gates

Draft self-review checks:

- Both create and adopt paths produce the same two audience-specific guides.
- Existing incomplete environments retain their working parts; no silent replacement or host repair authority.
- `.local/` preparation is part of human setup; agent commands consume local inputs without publishing their values.
- Host agents and containerized project execution remain distinct.
- Routine agent pointers omit the human document entirely. Only environment-authoring requirements name it.
- No layout-only migration, MTB-specific infrastructure, third-party service construction or universal wrapper. An external development database is a bounded adoption decision, not silently treated as an integrated Compose service.
- Planner orchestration, implementation and independent review retain their current owners.
- With an environment, relevant tickets require its agent guide and container use. Without one, tickets omit that requirement and gain no environment-related work blocker. All role authority clauses agree with autonomous assigned-development operations; code ownership and independent review remain intact.
- Linux portability is testable without claiming support for untested architectures or other operating systems.
- A required database belongs to the development Compose project. PostgreSQL adds branch template cloning, target verification and state-preserving resume.
- Synthetic data generation and disposable-runtime reset are team operations; operational data and host/shared resources remain outside that authority.
- Customer demos include a running application and usable access instructions; no claim of untested client connectivity.
- The data source for a concrete project's PostgreSQL template is settled in its environment task. This generic specification does not authorize operational-data imports.

Before package acceptance, validate the skill frontmatter, manifest membership/role matrix, conditional invocation, complete-tree delivery and existing-team update handling. Extend the existing package suite; check modified instruction meaning independently of keyword assertions. Qualify an absent-environment case with a different stack and a pre-existing-environment case. Execute container scenarios only under the separately authorized test scope.

## 8. Correction scope and verification

Fujiko's round-1 report is `REVIEW_2.9.1_Dev-Environment_v1.md`. Its verdict applies to v2, not this revision.

Corrections for final review:

- **B1:** replace the unanchored Planner proposals with exact R7/R8 replacements. R7 follows the design-check block, leaving the prototype-only exception intact; R8 lives in ticket-authoring step 7.
- **B2:** include `references/test_brownfield_planning.py` in the changeset and specify the changed positive assertion. Preserve the negative single-source checks.
- **B3:** retain the Reviewer's deployment prohibition. Define building and running a candidate in the assigned development runtime as permitted development operations in the skill and all three roles. Restart, rebuild, recreation, seeding and disposable-state reset remain autonomous; product-source repair and external deployment remain outside Reviewer authority.
- **N1:** separate required demonstration access from deviation-only reporting with `Beyond that`.
- **N2:** retain one synthetic-data permission in the candidate's Operating scope; remove its repeated grants from contract setting and baseline preparation.
- **N3:** identify the existing local checker and exact reproduction command below. It is an authoring helper, not a delivered Maker dependency.
- **N4:** distinguish this documentation task's execution authorization from the future team's proposed runtime authority.
- **N5:** require a package test for agreement of the shared authority paragraph across role templates.
- **N6:** use the Planner's existing customer clarification path; no parallel interview route.
- **N7/N8:** use `Choose the construction path` and `Coder/Team-Codex` consistently.

Authoring checks for this revision:

```sh
python3 /home/mariko/.hermes/skills/generic-devteam/scripts/check_candidate_skill.py /home/mariko/projects/generic-devteam/docs/SPEC_2.9.1_Dev-Environment_v3.md --forbid MTB --forbid mtb --forbid SG1
```

Checks passed: candidate validation; all eight ALT matches and original source lines; R1–R8 applied to temporary role copies; identical shared authority paragraphs; R7/R8 placement; unchanged prototype exception. The existing focused brownfield test passed at baseline, failed with R1 and the old assertion, then passed with all replacements and the corrected positive assertion. Its negative single-source checks were unchanged. The v2-to-v3 diff was inspected; whitespace, v2 frozen-input hashes and unchanged tracked Maker files were verified.

Reproduce the role and focused-test checks with `python3 -B /home/mariko/projects/generic-devteam-review/dev-environment-v3/verify_draft.py`. It writes only review fixtures and test logs beside itself. These are static text checks and one focused contract test, not package implementation or runtime qualification.

Final independent review is pending. No Docker, PostgreSQL, generated-team or live-profile behavior has been exercised for this revision. The full package suite remains an implementation gate; a documented requirement to run it is not evidence it passed.

This document is a design and complete text candidate. Static document checks do not prove skill discovery, agent adherence, Docker builds, usable generated guides or portability. Review this written draft before creating the implementation plan or changing the Maker package. No commit, push, live installation or SG1 conversion is included.
