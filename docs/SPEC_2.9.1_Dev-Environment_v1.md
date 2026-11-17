# Docker development environment skill — draft

Document version: v1 — first discussion draft with complete proposed skill text.
Status: proposed; not installed, implemented in the Maker, or approved for rollout.
Baseline: Maker 2.9.1, commit `94ded22fa58b1c41956985c3edd562c443bae7af`; clean working tree before this document.
Authoring: TAS checkout `git@github.com:ataian/tas.git`, commit `fe3a7d251518b793fedaec3041558c2840b4c796`; clean working tree. Entrypoint, authoring standard, Caveman and skill mechanics read.

## 1. Goal and confirmed decisions

As a project owner, I want the configured team to establish or adopt a reusable Docker development environment, so agents and human developers can build and test the same checkout without installing the project toolchain on the host.

- Target Linux hosts running Hermes. Hermes, Team-Codex, Git and Docker remain on the host.
- The Planner receives the generic construction/adoption skill through the Maker. The existing Coder/Team-Codex and independent Reviewer perform implementation and acceptance.
- Distinguish project workspace from code repository root. Default location: `docker/dev/` relative to the confirmed code repository root.
- Handle both a missing environment and an existing environment. Discuss unresolved stack choices with the customer; derive existing constraints from AGENTS.md and current manifests.
- Keep portable environment definitions in the shared project repository. Keep machine-specific configuration, credentials and runtime state in Git-ignored `docker/dev/.local/`.
- Produce exactly two development-environment guides: compact `docker/dev/AGENTS.md` for agents; standalone `docker/dev/HOWTO-human.md` for humans working without agents.
- Root AGENTS.md directs development/build/test work to the agent guide. Runtime agent instructions neither mention nor link the human guide. No explicit prohibition against reading it.
- When a project has a development environment, the Planner makes reading its agent guide and using that environment binding in relevant tickets. If no environment exists, omit that requirement; absence alone adds no work blocker. Coder and Reviewer SOULs remain unchanged.
- Environment authors and reviewers create, read and maintain both guides. Filename separation is information routing, not an access-control guarantee.
- Reuse tool containers, installed dependencies and caches during ordinary work. Temporary isolated test services remain valid where the project needs them.

This draft does not authorize changes to SG1, another team profile, containers, host configuration, publication or deployment.

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
description: Set up or adopt a project's Docker dev environment.
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

## Procedure

1. **Locate and classify.** Resolve the project workspace and each affected Git root independently.
   Read applicable AGENTS.md files, manifests, lockfiles, CI build/test commands and existing development definitions.
   Distinguish development tooling from deployment packaging; inspect only nonsecret configuration sources.
   Classify the requested environment as absent, usable, or incomplete/incompatible; an inspection failure is not absence.
   Done: repository root, current entrypoint, required toolchain and concrete gaps are known.

2. **Set the project contract.** For a new environment, discuss unresolved stack choices and development/test needs with the customer.
   Reuse decisions already established by project rules and manifests; surface conflicts rather than silently upgrading the stack.
   Identify required application services, test data, external integrations, browser checks and host architecture.
   Propose isolated local services and synthetic data by default. Existing external services require explicit bindings and permitted operations.
   State separately which checks and application workflows the environment will support.
   Done: the customer-owned choices and authorized service/data boundaries are settled through the existing planning process.

3. **Select the branch.**
   - **Create:** plan the smallest environment meeting the project contract, using the construction criteria below. Default to `docker/dev/` under the code repository root.
   - **Adopt:** derive commands and configuration from the existing definitions and project scripts. Preserve working layout, local inputs and data. Plan only necessary gaps and the two guides; do not create a parallel stack.
   - **Incomplete:** preserve reusable parts and name the precise missing capability. Obtain the required decision before repairs outside the accepted scope.
   Use the existing accepted-plan handoff for implementation and independent review; this skill adds no separate approval process.
   Done: each required capability, guide and verification outcome has an owner in the accepted task.

4. **Build or bind.** Have the Coder/Team-Codex implement the accepted environment or its bounded adoption changes.
   Use the construction criteria only for new or modified components; a documentation-only adoption does not authorize a redesign.
   Missing local inputs must produce a useful error naming the input and preparation step, without printing secrets.
   Done: the declared commands and local configuration mechanism exist, and preserved state remains intact.

5. **Write the two guides.** Have the implementation team produce both documents from the actual commands and configuration.
   - `docker/dev/AGENTS.md`: concise executable commands for readiness/resume, build, relevant tests, application start/stop and required regeneration. State working directory, local configuration location and essential target/safety conditions. Include dependency refresh and image rebuild triggers. Use one canonical command per operation; omit setup history, implementation explanations and copied run logs.
   - `docker/dev/HOWTO-human.md`: standalone instructions for a human using Linux without agents. Cover prerequisites, first setup after clone, local configuration from tracked examples, ordinary development/tests, pause/resume, updates and relevant troubleshooting. Explain each required local value, its source, and whether it is secret or generated.
   Keep the agent guide self-contained for ordinary work. Its references and the root agent pointer lead only to operational sources needed for that work.
   Add or reconcile a short root AGENTS.md pointer requiring the agent guide before development builds, tests or server starts. Use the actual repository-relative path.
   Keep shared commands portable; resolve machine-specific inputs through `.local/` rather than copying one developer's values into tracked instructions.
   Done: both audiences can follow their own guide, with no unresolved command placeholders; existing instructions agree with the new entrypoint.

6. **Verify and hand over.** Have the independent Reviewer check the acceptance cases below against the final candidate.
   Keep outcomes and limitations in the existing task; no additional evidence handbook is required.
   Report established capabilities, missing checks and required local inputs. Distinguish repository delivery from publication and live use elsewhere.
   Done: every promised capability has execution evidence or is explicitly reported as unverified; required missing evidence prevents a readiness claim.

## Construction criteria

- **Toolchain:** derive compatible versions from project rules, manifests and lockfiles. Pin image/tool inputs reproducibly using suitable existing project conventions; preserve dependency resolution semantics.
- **Compose:** keep development services separate from production deployment. Use project-scoped resources and configurable local ports/identity so another checkout can coexist without sharing mutable data accidentally. Prefer Compose service lifecycle management over a new process supervisor.
- **Source and identity:** bind the local checkout read/write where required. Resolve its location on each machine; support the user's UID/GID without requiring unused IDs in the base image or recursively changing source ownership.
- **Reuse:** keep tool containers available for repeated `exec` operations. Preserve caches and isolated container dependencies across stop/start. Refresh dependencies when their inputs change; rebuild tools when tool-image inputs change, not for ordinary source edits.
- **Local inputs:** track secret-free configuration examples and ignore `.local/`. Separate portable defaults from local overrides; explain whether each local file is supplied or generated. First setup must preserve existing local configuration and state. Respect existing application configuration paths when adopting a project.
- **Isolation:** exclude secrets and private state from build contexts and published artifacts. Publish development listeners only on loopback by default. Keep test targets separate from operational databases and prevent unapproved outbound effects.
- **Services:** include the local dependencies needed by the accepted workflow, or explicitly declare the external prerequisites and their local configuration. No machine-specific external network, service name or existing dataset becomes an undocumented prerequisite.
- **Nested test containers:** when required, verify daemon access, mount-path semantics, connectivity and normal test cleanup. Docker socket access grants host-level authority; make that boundary part of the accepted design rather than mounting it by default.
- **Simplicity:** reuse native Compose and project commands. Add a helper only for a demonstrated operation they cannot express safely and clearly. Preserve the project's data/removal permissions; routine pause/resume retains state.

## Acceptance cases

- **Fresh checkout:** exercise setup from tracked files plus documented local inputs in a separate Linux checkout path. Do not reuse undeclared dependencies or caches from the original checkout. Verify the supported user identity and architecture, writable source without root-owned artifacts, and isolated resources. State any untested host/architecture boundary.
- **Functional use:** run a real build and the agreed relevant tests in the containers. Check application readiness and browser/test-service behavior where included. A version command, running container or skipped test is not that evidence.
- **Reuse:** repeat ordinary commands and pause/resume. Verify reuse of the tool container and retained dependencies/caches without rebuilding or reinstalling. Temporary test containers may differ between runs.
- **Safe adoption:** use the actual existing entrypoint. Confirm expected mounts, local endpoints and test targets without disclosing credentials; preserve external data and unrelated services. Repairs remain bounded by the accepted task.
- **Missing input:** omit a required local input in an isolated test setup. Confirm an actionable failure before application writes, with no secret disclosure or overwrite of another local configuration.
- **Audience separation:** exercise routine commands using only the agent guide and its operational sources. Check the human guide independently from first setup through normal use. Agent instructions contain no pointer to the human guide and no instruction prohibiting its reading.

## Pitfalls

A repository bind mount exposes local ignored files too; Git exclusion is not a sandbox.
A fixed Compose project name can collide across checkouts; local identity must be stable for resume and distinct for independent environments.
Existing infrastructure and safety machinery from one project are evidence to inspect, not templates to impose on every project.
````

## 4. Proposed root agent pointer

Generated into the target repository's existing root AGENTS.md, reconciled with any existing development-environment clause:

> Before development builds, tests or server starts, read `docker/dev/AGENTS.md` and use its container commands.

No human-guide filename, negative reading instruction, setup narrative or copied command table accompanies that pointer. The environment's AGENTS.md is versioned, not a second per-profile skill. The same file is the source for Planner, Coder, Reviewer and Team-Codex. Explicit loading is required; the design does not assume nested AGENTS.md auto-loading.

## 5. Maker integration proposed for a later changeset

| Surface | Proposed change | Existing basis / verification |
| --- | --- | --- |
| `skills/dev-environment/SKILL.md` | Add the candidate as an owned Planner-only skill. | New file; no universal generator or mandatory helper. |
| `manifest.json` | Add file membership and `own_skills.dev-environment`, with `targets.hermes = [planner]`, unchanged SKILL.md transport and owned provenance. | Existing owned-skill schema and `references/update_team.py:259–282` iterate assigned complete skill trees. |
| `references/upstream-sources.md` | Add the owned component and Planner assignment to the source/role matrix. | `references/setup.md:308–315` uses that matrix for complete-tree copying. |
| `templates/roles/planner.SOUL.md.template` | Add the setup-skill invocation and conditional environment requirement at the existing planning and ticket-authoring steps. | Proposed wording below; Coder and Reviewer templates remain unchanged. |
| `SKILL.md` | Refine the existing optional first-task offer to name development-environment creation/adoption. | Current final handoff offers a first planning task and does not start it automatically. Retain that boundary. |
| `README.md`, `NOTICE.md` | Update the owned component overview and provenance where applicable. | No SG1-specific hosts, networks, credentials or local paths in delivered instructions. |
| `references/test_render_reasoning.py`, `references/test_update_team.py` | Extend the exact role matrix and delivery/update coverage. | Existing tests enumerate own-skills targets and exercise manifest-driven mapping. |
| New focused package contract tests | Cover both branches, guide separation, root pointer, portability and retained role boundaries. | Follow `references/test_devteam_cleanup.py`; distinguish static contracts from agent behavior. |
| `SKILL.md` and `manifest.json` versions | Apply one compatible-feature MINOR bump when implementing the package changeset. | No package bump for this repository-only discussion draft. |

Proposed Planner invocation:

> When asked to create, adopt or revise a project's Docker development environment, load `dev-environment` with `skill_view(name="dev-environment")`.

Proposed Planner ticket-authoring clause:

> When the project has a development environment, include its agent-guide path in each relevant ticket. Require reading that guide and using the environment for the ticket's builds, tests and development servers.

Apply this clause only to an existing environment. Without one, omit the ticket requirement rather than blocking ordinary work or requiring setup implicitly. Creating an environment remains a separately accepted task. Keep concrete commands in the project guide, not in role SOULs or repeated ticket instructions.

The construction skill is delivered only to the Planner. Coder and Reviewer receive the applicable construction/verification requirements through the accepted task. Routine agent use needs only the repository guide. The human guide is an output of the environment task, not a role-profile dependency.

Existing-team delivery follows the existing authorized updater. It does not automatically run the skill, rebuild an environment or change the project's guides. Native discovery and first-use behavior remain qualification checks for implementation, not claims established by this document.

## 6. Evidence from SG1 and deliberate exclusions

Read-only sources inspected:

- Planner setup conversation `20261109_182335_7691a0` in profile `jack`, including the customer's container-reuse and host-Codex decisions.
- Original construction brief: `/home/mariko/projects/mtb/docs/MTB_Entwicklungsumgebung_Docker.md`.
- Current example under `/home/mariko/projects/mtb/de.uke.iam.mtb/docker/dev/`: README.md, compose.yaml, Dockerfile and .gitignore.
- Workspace/repository HERMES.md and AGENTS.md; Maker role template, source matrix, setup and updater mapping.

The SG1 README mixes setup, routine use, runtime internals and recovery. Its Compose file requires an external project-specific network. The described configuration switching includes Linux write leases and rename exchange. These explain why merely shortening that README would not produce a generic environment recipe.

Retain the reusable concepts: host-side agents, container toolchains, persistent dependencies, explicit local configuration, independent review and real command execution. Do not generalize the MTB database-cloning policy, relay topology, token simulator, process supervisor, application gates, exact tool versions or fixed network names. A project may still need such mechanisms when its actual requirements establish the need.

SG1 conversion is a separate task. This proposal does not claim its current environment is broken or that a simpler replacement has already been verified.

## 7. Draft review and implementation gates

Draft self-review checks:

- Both create and adopt paths produce the same two audience-specific guides.
- Existing incomplete environments retain their working parts; no silent replacement or host repair authority.
- `.local/` preparation is part of human setup; agent commands consume local inputs without publishing their values.
- Host agents and containerized project execution remain distinct.
- Routine agent pointers omit the human document entirely. Only environment-authoring requirements name it.
- No requirement to migrate a working layout, adopt MTB-specific infrastructure or add a universal wrapper.
- Planner orchestration, implementation and independent review retain their current owners.
- With an environment, relevant tickets require its agent guide and container use. Without one, tickets omit that requirement and gain no environment-related work blocker. Coder and Reviewer SOULs remain unchanged.
- Linux portability is testable without claiming support for untested architectures or other operating systems.

Before package acceptance, validate the skill frontmatter, manifest membership/role matrix, conditional invocation, complete-tree delivery and existing-team update handling. Extend the existing package suite; check modified instruction meaning independently of keyword assertions. Qualify an absent-environment case with a different stack and a pre-existing-environment case. Execute container scenarios only under the separately authorized test scope.

This document is a design and complete text candidate. Static document checks do not prove skill discovery, agent adherence, Docker builds, usable generated guides or portability. Review this written draft before creating the implementation plan or changing the Maker package. No commit, push, live installation or SG1 conversion is included.
