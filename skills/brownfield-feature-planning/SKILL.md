---
name: brownfield-feature-planning
description: "Plan changes grounded in an existing application."
version: 1.1.0
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

- Scope: features and corrections in an existing application. Ground the plan in current code, accepted requirements, and observable behavior.
- Use team clarification/design skills and their approval rules. Use the Planner's `domain-modeling` workflow. Apply the Planner's plan-synthesis, vocabulary, and accepted-ADR rules.
- Clarification demo: load Planner-only `prototype` with `skill_view(name="prototype")`.
- On an explicit request for an expert questionnaire, load the original `to-questionnaire` with `skill_view(name="to-questionnaire")`.
  Draft for one recipient. Keep existing authorization gates for sending and plan acceptance.

## Boundaries

- Keep existing roles and execution policy.
- Keep accepted product decisions binding when revising a plan.
- Keep independent review and required safety checks.
- Label existing, proposed, and verified behavior separately. Use specialist procedures only for requirements in accepted scope.

## Planning procedure

### 1. Establish the outcome and baseline

1. Read the request, project rules, accepted decisions, and existing plan. State the observable result and scope. Reuse settled answers.
2. For automation, map agreed manual steps to inputs, existing commands, mutations, and results. Keep bounded utilities within scope.
3. Verify workspace, actual Git roots, branch, HEAD, and working-tree changes. Keep planning and implementation roots distinct. If an older proposal conflicts with the customer's selected branch, inspect that branch without switching or merging to match the proposal.
4. Distinguish proposal revision, current code baseline, and accepted-plan commit. Use required analysis integration under its freshness and coverage rules. If baseline changes during approval, recheck affected findings.
5. External plan: establish storage and Git ownership during planning. Resolve versioning authorization before handoff. Specification can proceed. Do not create an extra repository or commit into a sibling to satisfy the baseline rule.

### 2. Trace the actual behavior

1. Trace active entrypoint, callers, bound UI state where applicable, service boundary, persistence, outputs, and tests. Exclude comments, removed controls, and historical plans from active behavior. Trace transformations, limits, normalization, and downstream lookup before promising behavior.
2. Check repository methods before planning new persistence/API work. Classify each file against the current tree as new, modified, or reused. Resolve paths against actual production, test, and generated-source roots.
3. Access change: bind acceptance cases to actor, entrypoint, and persisted state. Distinguish ordinary access from expressly accepted privileged exceptions. Check server authorization separately from disabled UI controls. Verify existing authority tokens. Display names do not establish roles.
4. External data: load [Data discovery](references/data-discovery.md) before choosing coverage, mappings, or validation. Before inspecting operational files or a populated database, load the protected-source procedure in [Replacement imports](references/replacement-imports.md). Source availability proves neither connectivity nor successful import nor reset authority.

### 3. Select the smallest viable integration

1. Compare relevant approaches against interfaces, clients, data ownership, and deployment constraints. For relevant module/interface choices, apply the Planner's caller-contract and abstraction checks. Reuse working commands and business logic. An earlier project's solution carries no requirement here.
2. Ask only consequential product questions unanswered by code and accepted requirements. Keep unresolved sources and behavior explicit. Avoid implied defaults.
3. Derive a finite acceptance path from requirements and concrete changed-code risks. Apply the Planner's test-seam rules to this acceptance path. Include relevant failure, repeat-run, privacy, and data-integrity checks. Use existing verification facilities before proposing new infrastructure. Treat missing fixtures as bounded team preparation. Keep import-only delivery free of unrequested UI, upgrades, and whole-application test platforms.
4. Name the authorized isolated environment if tests are in scope. Artifact creation grants no deployment authority. Ask for a deployment host only when application there is in scope. Documentation-only and script-only delivery need none.

### 4. Build reviewable phases

1. State common constraints once. Cut work by actor, desired behaviour, and benefit before mapping stories to phases and tickets. Each slice needs an observable, independently verifiable outcome across relevant layers. Adding an actor prefix to database/API/UI layer work does not make it a story.
2. Justify foundations by the stories they enable and their verification gate. Include preparation or refactoring only when justified by the goal. Context-window fit may inform sizing. Keep coherent, independently reviewable outcomes without a fixed size cap.
3. For broad mechanical changes that cannot safely land as independent vertical slices, load only [Expand–Migrate–Contract](references/kanban-phase-release.md#expandmigratecontract) during planning, before plan acceptance.
4. Give each phase an independently reviewable deliverable with requirements, files, interfaces, dependencies, tests, gate, and commit boundary. Map gates to enabling changes. Order producers before consumers across separately versioned repositories.
5. Name local build/install prerequisites and applicable project/module rule paths in the plan. Do not create placeholder rules or suppress real read errors to pass preflight.
6. Preserve accepted phase/review boundaries unless amended by the required authority. Keep workspace boundaries and versioned baselines. If scope conflicts with a gate, keep the gate and propose the smallest repository-specific prerequisite. Obtain amendment approval before adding or releasing work.
7. Inspect version sources and relevant Git history before requiring a bump. Reuse an already fulfilled version step on the accepted baseline. A matching tag alone proves neither source nor artifact identity.

Use existing results for the Planner's final customer report, not a new technical review or closing ticket.

### 5. Define limits and verify the plan

- Estimates: calculate phase-table values with a tool. Include independent review. State whether waits, provider delays, and corrections are included. Distinguish effort, delivery time, foreground waits, process deadlines, and native stuck-worker protection. Prose size proves neither cost nor a global cap.
- Limits: preserve explicit customer financial/resource caps, configured limits, provider quotas, operational permissions, and native failure-loop guards. Use supported long-running execution. Avoid generic Codex timeouts and correction-count approvals.
- Progress: work until acceptance criteria and required checks are complete, then stop. Correct recoverable failures independently. Do not repeat a failed approach unchanged. Escalate the concrete obstacle when no justified next approach remains.
- Plan check: map every specification requirement to files, tests, gates, dependencies, and commit boundaries. Verify actual phase numbers and acceptance-case IDs. If the checker misresolves a path, correct the checker. The error cannot establish a missing product file.
- Evidence: distinguish document validation from executed application verification. Describing a lock, migration, parser, or rollback proves no working behavior.

### 6. Accept, version, and hand off

1. Do not create implementation tickets before explicit plan acceptance. Keep rejected or unapproved plans unreleased.
2. Keep the accepted plan and phase plan in the agreed versioned project location. Bind every task to their absolute paths and exact Git commits.
3. Authorized documentation commit: inspect staged/unstaged changes and validate before staging. Check exits between validation and writes. Stage only intended planning files. Run `git diff --cached --check`. Verify committed files, parent baseline, and working tree. If the checker was defective, inspect the commit and rerun the corrected check without duplicate commits or history rewrites.
4. Record ticket documentation directly on the existing Kanban card. Keep decisions, exceptions, consequential failures/remedies, blockers, outcomes, and verdicts there. Attribute evidence to its executor and exact checked state. Native run outputs remain available evidence, not an authored run-log duty.
5. Keep product documentation in its owning repository. Retain historical records as history. On continuation, reconcile assignment, working tree, and blockers before resuming unfinished work.
6. Reuse evidence only while checked inputs and relevant dependencies, configuration, and test conditions remain valid. A new commit alone does not invalidate every prior result. Renew checks for affected areas or insufficient evidence. Retain independent review and explicit final-state acceptance tests. Keep original evidence. Do not create a separate summary or evidence register.
7. For Kanban handoff, partial ticket-creation, or release recovery, load [Phase release](references/kanban-phase-release.md). Report verified handoff state. Worker execution and product completion require their own evidence.

## Revising an existing plan

1. Read the plan, accepted specification, repository rules, and replacement instructions. Distinguish superseded skill defaults from binding decisions and approved exceptions.
2. Revise the existing plan if intent is unchanged. Amend accepted specifications or rules only with authority. Preserve valid safety gates, review boundaries, budget decisions, and already-reviewed history.
3. Record consequential in-scope decisions on the existing ticket. For an authorized binding amendment, update the versioned plan and affected current and future ticket bindings before release. Verify the returning worker's applicable baseline.
4. Compare revised requirements, phases, gates, commits, and documentation diff. Obtain explicit revised-plan acceptance before creating or releasing affected work. Revision alone does not authorize execution.
5. Distinguish cancellation from narrowing. Load [Phase release](references/kanban-phase-release.md) before scope-related card/graph changes. Preserve reusable work and valid prerequisites. Verify prerequisites and ownership before resuming authorized work.

## Conditional references

Load a reference only when its trigger applies. Read only the applicable procedure and prerequisites. Conditional references add no scope.

| Trigger | Required reference |
|---|---|
| External source, catalog, lookup, or optional data integration | [Data discovery](references/data-discovery.md) |
| Import replacement, reset, identity remapping, or supplied operational test data | [Replacement imports](references/replacement-imports.md) |
| Accepted plan enters Kanban, partial ticket-creation, release recovery, or approved scope/graph amendment | [Phase release](references/kanban-phase-release.md) |
| Status, completion, review, or blocker notification | [Status inspection](references/kanban-status-inspection.md) |
| Recovery from an interrupted run, resolved blocker, or automatic triage | [Recovery](references/kanban-triage-recovery.md) |
| Operator tool or explicitly agreed operator-executed verification | [Operator acceptance](references/operator-script-acceptance.md) |
| Explicit user request for a process retrospective | [Standalone retro routing](references/project-retrospectives.md) |

## Verification

- Before presenting: confirm baseline, required scope, reachable acceptance path, and remaining decisions.
- Before board transition: use the applicable reference to verify ownership, prerequisites, and the exact written target.
- Keep test result, independent review approval, phase approval, and whole-product acceptance distinct.
- Briefly report status, attributed evidence, consequential caveats, and next responsible actor. Put task-specific facts in the versioned plan or existing card.
