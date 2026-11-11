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
Use team clarification/design skills and their approval rules.
Keep existing roles and execution policy.

## Boundaries

- Keep accepted product decisions binding when revising a plan.
- Keep independent review and required safety checks.
- Leave execution-time technical decisions within the accepted goal and constraints to the Coder.
- Distinguish binding requirements and architectural constraints from implementation suggestions.
- Expected file lists are guidance unless explicitly marked as hard boundaries.
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

Read the request, project rules, accepted decisions, and existing plan.
State the observable result and scope.
Reuse settled answers.
For automation, map agreed manual steps to inputs, existing commands, mutations, and results.
Keep bounded utilities within scope.

Verify the workspace, actual Git roots, branch, HEAD, and working-tree changes.
Keep planning and implementation repository roots distinct.
If an older proposal conflicts with the customer's selected current branch, inspect that branch without switching or merging merely to match the proposal.
Distinguish proposal revision, current code baseline, and accepted-plan commit.
Use the required analysis integration under its existing freshness and coverage rules.
Recheck affected findings if the baseline changes during approval.

For an external plan, establish storage and Git ownership during planning.
Resolve versioning authorization before handoff, not specification.
Do not create an extra repository or commit into a sibling to satisfy the baseline rule.

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

State common constraints once.
Give each phase an independently reviewable deliverable with requirements, files, interfaces, dependencies, tests, gate, and commit boundary.
Map gates to enabling changes.
Assign each acceptance criterion to an implementation ticket and its existing independent Reviewer.
Place combined-behavior checks in the phase where integrated behavior becomes available.
Use existing results for the Planner's final customer report, not a new technical review or closing ticket.
Order producer artifacts before their consumers across separately versioned repositories.
Name local build/installation prerequisites and applicable project/module rule paths in the plan.
Do not create placeholder rule files or suppress real read errors to make preflight appear successful.

Preserve accepted phase and review boundaries unless amended by the required authority.
For a scope/gate conflict, preserve the gate and propose the smallest repository-specific prerequisite.
Obtain amendment approval before adding or releasing work.
Keep workspace boundaries and versioned baselines.

Inspect existing version sources and relevant Git history before requiring a version bump.
If the intended version step is already fulfilled on the accepted baseline, reuse that result.
A matching tag alone does not establish matching source or artifact identity.

### 5. Define limits and verify the plan

Distinguish effort, delivery time, foreground waits, process deadlines, and native stuck-worker protection.
Calculate phase-table estimates with a tool.
Include independent review; state whether waits, provider delays, and corrections are included.
Work until the acceptance criteria are met. Correct recoverable failures independently.
Do not repeat a failed approach unchanged. Escalate the concrete obstacle when no justified next approach remains.
Stop when the accepted result and required checks are complete.
Preserve explicit customer financial/resource caps, configured limits, provider quotas, operational permissions, and native failure-loop guards.
Use supported long-running execution, not generic Codex timeouts or correction-count approvals.
Prose size proves neither cost nor a global cap.

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

For an authorized documentation commit, inspect staged/unstaged changes and validate before staging.
Check exits between validation and writes.
Stage only intended planning files and run `git diff --cached --check`.
Verify committed files, parent baseline, and working tree.
After a checker defect, inspect the commit and rerun the corrected check without duplicate commits or history rewrites.

Record ticket documentation directly on the existing Kanban card.
Keep decisions, exceptions, consequential failures/remedies, blockers, outcomes, and verdicts there.
Attribute evidence to its executor and exact checked state.
Native run outputs remain available evidence, not an authored run-log duty.
Keep product documentation in its owning repository.
Preserve historical records without treating them as current instructions.
On continuation, reconcile assignment, working tree, and blockers; resume unfinished work.
Reuse evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid.
A new commit alone does not invalidate every prior result.
Require renewed checks for affected areas or insufficient evidence, while retaining independent review and explicit final-state acceptance tests.
Keep original evidence; do not create a separate summary or evidence register.

When handing the accepted plan to Kanban, load [Phase release](references/kanban-phase-release.md).
Use that procedure for partial ticket-creation or release recovery too.
Report the verified handoff state, not assumed worker execution or product completion.

## Revising an existing plan

Read the plan, accepted specification, repository rules, and replacement instructions.
Distinguish superseded skill defaults from explicit product decisions and approved exceptions.
Record consequential in-scope decisions on the existing ticket.
For an authorized binding amendment, update the versioned plan and affected current and future ticket bindings before release.
Preserve already-reviewed history and verify the returning worker's applicable baseline.
Revise the existing plan for unchanged intent; amend accepted specifications or rules only with authority.
Keep valid safety gates, review boundaries, and budget decisions.
Compare revised requirements, phases, gates, commits, and documentation diff.
Obtain explicit revised-plan acceptance before creating or releasing affected work.
Plan revision does not authorize execution.

Distinguish cancellation from narrowing the authorized goal.
Use [Phase release](references/kanban-phase-release.md) before scope-related card/graph changes.
Preserve reusable work and valid prerequisites.
Verify prerequisites and ownership before resuming authorized work.

## Conditional references

Load a reference only when its trigger applies.
Read its procedure and prerequisites, not unrelated branches.
Conditional references add no scope.

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
