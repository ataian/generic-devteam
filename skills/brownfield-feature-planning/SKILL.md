---
name: brownfield-feature-planning
description: "Plan changes grounded in an existing application."
version: 1.0.1
author: Max, Mariko (Hermes Agent)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [feature-planning, brownfield, requirements]
    related_skills: [superpowers:brainstorming, minimal-change-engineering]
---

# Brownfield feature planning

## When to use

Use for a feature or correction that changes an existing application.
Ground the plan in the current code, accepted requirements, and observable behavior.
Use the team's requirement-clarification and design skills under their existing approval rules.
This skill supplies existing-code analysis and handoff procedures, not a new role or execution policy.

## Boundaries

- Keep accepted product decisions binding when revising a plan.
- Keep independent review and required safety checks.
- Resolve technical choices within the accepted goal and your role's authority.
- Ask the customer about changed use cases, material trade-offs, or scope expansion.
- Separate existing behavior, proposed behavior, and verified behavior.
- Do not infer permission to mutate a resource from permission to inspect it.
- Treat pseudonymized operational data as sensitive, not synthetic.
- Keep credentials, identifiable filenames, free text, and source values out of shared planning evidence.
- Use synthetic examples when evidence must be shared.
- Apply specialist procedures only to requirements present in the accepted scope.
- Leave implementation, independent review, and dispatcher execution with their assigned owners.

## Planning procedure

### 1. Establish the outcome and baseline

Read the request, applicable project rules, accepted decisions, and relevant existing plan.
State the requested observable result and its scope boundary.
Reuse settled answers instead of restarting the interview.
For automation, map the agreed manual steps to inputs, existing commands, mutations, and results.
Do not expand a bounded utility into application lifecycle management.

Verify the workspace, actual Git roots, branch, HEAD, and working-tree changes.
Keep planning and implementation repository roots distinct.
If an older proposal conflicts with the customer's selected current branch, inspect that branch without switching or merging merely to match the proposal.
Record the proposal revision, current code baseline, and later accepted-plan commit as distinct identities.
Use the required analysis integration under its existing freshness and coverage rules.
Recheck affected findings if the baseline changes during approval.

If the plan belongs outside the application repository, establish its storage and Git ownership during planning.
Resolve required versioning authorization before ticket handoff without blocking the specification itself.
Do not initialize an extra repository or commit into a sibling repository merely to satisfy the baseline requirement.

### 2. Trace the actual behavior

Inspect the relevant entrypoint, callers, bound UI state where applicable, service boundary, persistence, outputs, and tests.
Distinguish active code from comments, removed controls, and historical plans.
Trace transformations, limits, normalization, and downstream lookup semantics before promising behavior.
Check available repository methods before planning new persistence or API work.
Classify each proposed file as new, modified, or reused against the current tree.
Resolve paths against their actual production, test, and generated-source roots.

For access changes, bind each acceptance case to its actor, entrypoint, and persisted state.
Distinguish ordinary access from explicitly accepted privileged exceptions.
A disabled UI control is not server-side authorization.
Verify existing authority tokens rather than inventing identity roles from their display names.

If the change uses external data, load [Data discovery](references/data-discovery.md) before deciding coverage, mappings, or validation rules.
If supplied operational files or a populated database will be inspected, load the protected-source procedure in [Replacement imports](references/replacement-imports.md) before accessing them.
An available source is not proof of connectivity, successful import, or authority to reset it.

### 3. Select the smallest viable integration

Compare relevant approaches against existing interfaces, clients, data ownership, and deployment constraints.
Reuse working commands and business logic rather than creating parallel implementations.
Ask only consequential product questions that the code and accepted requirements do not answer.
Keep unresolved source or behavior decisions explicit instead of introducing implied defaults.
Do not adopt an earlier project's solution as a requirement.

Define a finite acceptance path from the required behavior and concrete changed-code risks.
Include relevant failure, repeat-run, privacy, and data-integrity cases.
Use existing verification facilities before proposing new test infrastructure.
Treat missing fixtures as bounded preparation work for the team.
Do not turn an import-only delivery into an unrequested UI, upgrade, or whole-application test platform.

Creating deployment artifacts does not authorize applying them.
Ask for a deployment host when application to that host is in scope, not as a prerequisite for a documentation-only or script-only delivery.
Name the authorized isolated verification environment when tests are in scope.

### 4. Build reviewable phases

Place common constraints once, followed by each phase's requirements, files, interfaces, dependencies, tests, acceptance gate, and commit boundary.
Give each phase a coherent independently reviewable deliverable.
Map each gate to the repository changes that make it achievable.
Order producer artifacts before their consumers across separately versioned repositories.
Name required local build or installation prerequisites.
Pass the actual applicable project/module rule paths to the coding handoff.
Do not create placeholder rule files or suppress real read errors to make preflight appear successful.

Preserve accepted phase and review boundaries.
Change them only through the applicable plan-amendment decision.
If a worker exposes a scope/gate contradiction, preserve the gate and propose the smallest repository-specific prerequisite.
Obtain the required amendment approval before adding or releasing coding work.
Do not widen the workspace or substitute an unversioned workaround.

Inspect existing version sources and relevant Git history before requiring a version bump.
If the intended version step is already fulfilled on the accepted baseline, reuse that result.
A matching tag alone does not establish matching source or artifact identity.

### 5. Define limits and verify the plan

Separate estimated effort from hard run timeouts, retry allowances, and elapsed delivery time.
Calculate estimates from the phase table with a tool.
Include independent review and state whether waits, provider delays, and correction rounds are included.
Define the stop condition, permitted remaining work, and who may authorize an extension.
Keep approved budgets unless evidence or a new owner decision changes them.
Shorter prose does not prove cheaper implementation or a global cost cap.

Check every specification requirement against the proposed files, tests, gates, dependencies, and commit boundaries.
Check phase numbering and acceptance-case identifiers against the actual document.
Correct a checker's path-resolution error rather than treating it as a missing product file.
Distinguish document validation from executed application verification.
A plan describing a lock, migration, parser, or rollback is not evidence that it works.

### 6. Accept, version, and hand off

Do not create implementation tickets before explicit plan acceptance.
Keep a rejected or unapproved plan unreleased.
Keep the accepted plan and phase plan in the agreed versioned project location.
Bind each task to their absolute paths and exact Git commits.

For an authorized documentation commit, inspect staged and unstaged changes first.
Run document validation before staging.
Use checked exits if validation and writes share a shell invocation.
Stage only intended planning files and run `git diff --cached --check`.
Verify the resulting commit's changed files, parent baseline, and working-tree state.
If a checker defect is discovered after committing, inspect that commit and rerun the corrected check without manufacturing a duplicate commit or rewriting history.

Record ticket documentation directly on the existing Kanban card.
Include decisions, instructions, blockers, handoffs, verification results, and review outcomes there.
Attribute evidence to its executor and exact checked state.
Use native run logs for detailed execution output.
Keep product documentation in its owning repository.
Preserve historical records without treating them as current instructions.
On continuation, reconcile current assignment, working tree, and blockers, then continue unfinished work.
Reuse evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid.
A new commit alone does not invalidate every prior result.
Require renewed checks for affected areas or insufficient evidence, while retaining independent review and explicit final-state acceptance tests.
Keep evidence on the existing card and in original run outputs, not in a separate summary or evidence register.

When handing the accepted plan to Kanban, load [Phase release](references/kanban-phase-release.md).
Use that procedure for partial ticket-creation or release recovery too.
Report the verified handoff state, not assumed worker execution or product completion.

## Revising an existing plan

Read the current plan, accepted specification, repository rules, and replacement instructions.
Distinguish superseded skill defaults from explicit product decisions and approved exceptions.
Update the existing plan when intent is unchanged.
Leave accepted specifications and repository rules unchanged unless their amendment is authorized.
Keep valid safety gates, review boundaries, and budget decisions.
Compare the revised requirements, phase/gate/commit structure, and actual documentation diff.
Present the revised document for explicit acceptance before creating or releasing affected implementation work.
A request to revise the plan is not permission to execute it.

If the customer narrows active work, distinguish cancellation from continued authorization of the original goal.
Use the scope-change procedure in [Phase release](references/kanban-phase-release.md) before changing the existing cards or graph.
Preserve reusable work and still-valid prerequisites.
Resume authorized remaining work only after its prerequisites and ownership are verified.

## Conditional references

Load a reference only when its trigger applies.
Read the relevant procedure and its prerequisites, not unrelated branches.
References describe conditional work; they do not add requirements to the accepted goal.

| Trigger | Required reference |
|---|---|
| External source, catalog, lookup, or optional data integration | [Data discovery](references/data-discovery.md) |
| Import replacement, reset, identity remapping, or supplied operational test data | [Replacement imports](references/replacement-imports.md) |
| Accepted plan enters Kanban, partial handoff, or approved scope/graph amendment | [Phase release](references/kanban-phase-release.md) |
| Status, completion, review, or blocker notification | [Status inspection](references/kanban-status-inspection.md) |
| Recovery from an interrupted run, resolved blocker, or automatic triage | [Recovery](references/kanban-triage-recovery.md) |
| Operator tool or explicitly agreed operator-executed verification | [Operator acceptance](references/operator-script-acceptance.md) |
| Explicit request for a retrospective | [Project retrospective](references/project-retrospectives.md) |

## Verification

Before presenting the plan, confirm its baseline, required scope, reachable acceptance path, and remaining decisions.
Before a board transition, use the applicable reference to verify current ownership, prerequisites, and the exact written target.
An implementation test result is not independent review approval.
An approved phase is not whole-product acceptance.
Report status, attributed evidence, consequential caveats, and the next responsible actor briefly.
Keep task-specific facts in the versioned plan or existing card, not in this reusable skill.
