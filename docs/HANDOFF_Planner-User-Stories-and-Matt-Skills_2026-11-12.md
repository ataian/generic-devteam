# Handoff: Planner user stories and Matt Pocock skills

## Purpose and snapshot

Continue Max's discussion in a separate session while the originating session coordinates the authorized Maker edit and its independent review.

Snapshot: `2026-11-12T02:53:36+01:00`.
Repository: `/home/mariko/projects/generic-devteam`.
Branch: `v3`.
Observed HEAD: `68395c91120286e907532dd28bb25a16c9bdec52` (`added matt's domain-modeling`).
Working tree was clean before this new handoff.
Package version: `2.1.0`.

Re-read actual Git state before relying on this snapshot. The implementer will change the working tree. Max may also commit during execution; preserve his commits and inspect the recorded starting commit through current HEAD plus remaining working changes.

## Current authorization

Max's latest request:

> perfekt. lass dies bitte von einem subagent erledigen. und schreib eine neue übergabe datei mit dem aktuellen arbeitsstand, damit ich das hier parallel dazu in einer neuen session weiter besprechen kann.

Authorized now: one implementation subagent for the agreed user-story planning/ticket changes and selected codebase-design questions, package documentation/tests, then independent review. The parent writes this handoff. This is direct subagent coordination for this task, not a change to generated teams' native Kanban workflow.

No live-team updates, installations, service/profile changes, commit, push, deployment, or unrelated Maker redesign are authorized. The remaining Matt-skill proposals are discussion items only.

## Implementation and review complete

Implementation and independent review finished in the originating session. Package `2.2.0` is uncommitted and approved for the reviewed Maker delta. This supersedes the original snapshot's work status, not its recorded baseline.

- Delegation: `deleg_5e123813`.
- Worker: `sa-0-c77dc463`.
- Live transcript: `/home/mariko/.hermes/cache/delegation/live/deleg_5e123813/task-0.log`.
- Assignment: user-story-oriented planning, concise story titles and structured ticket descriptions, selected codebase-design questions, coupled package docs/tests. No other Matt-skill adoption.

Current candidate matches the worker's final file snapshot. Baseline and observed HEAD remain `68395c91120286e907532dd28bb25a16c9bdec52`.

- Implementation evidence: `/home/mariko/.hermes/cache/scratch/planner-stories-20261112T025628/`.
- Original aggregate result: 155 tests, `OK (skipped=16)`, exit 0. Skips concern native Kanban recovery transitions denied by the delegated-child guard; new story/design contract tests ran.
- Review delegation: `deleg_b381f6f4`.
- Review worker: `sa-0-558f3f7b`.
- Review transcript: `/home/mariko/.hermes/cache/delegation/live/deleg_b381f6f4/task-0.log`.
- Review verdict: `APPROVE`; no actionable defects against the approved requirements.
- Review report: `/home/mariko/.hermes/cache/scratch/planner-stories-review/REVIEW.md`.
- Parent verified that the current implementation bytes still match the reviewed snapshot and that `git diff --check` passes.
- No implementation or review worker remains pending for this assignment. Live behaviour and effective loading were outside this package review. No live rollout, installation, commit, or push occurred in this task.

The originating session completed implementation coordination and independent review. The new session can continue discussing the remaining proposals. Preserve the reviewed uncommitted work; further changes need their own explicit scope. Do not repeat this completed assignment.

The completed delegation handles remain evidence locators, not active job instructions. This handoff preserves the decisions and outcome for a separate conversation.

## Completed: domain-model integration

The Maker already includes original `domain-modeling` in its existing Matt component, Planner-only, alongside `grill-me` and `grilling`. All use upstream revision `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.

The existing interview conditionally loads active domain modelling. Glossaries remain vocabulary, not specifications. ADRs require a hard-to-reverse, surprising, genuine trade-off decision. Draft records do not imply acceptance. Coder/Reviewer consume accepted definitions; Reviewer remains read-only. Existing plan approval, native dispatch and Coder discretion remain intact.

The prior implementation was independently approved. Original verification: renderer 60 tests OK; aggregate 151 tests OK with 16 native Kanban-transition skips caused by the delegated-child guard. No guard bypass or live qualification. Evidence:

- `/home/mariko/.hermes/cache/scratch/domain-modeling-20261112T020909/`
- `/home/mariko/.hermes/cache/delegation/live/deleg_8e587b5f/task-0.log`

These are historical package results, not tests of the new user-story changes. The current observed HEAD contains the completed domain-model change; no need to reimplement it.

## Accepted decisions for the current worker

### 1. Plan by user stories, not technical layers

Max and his team think in user stories. Previous ticket cuts were not understandable to him.

The Planner cuts work by actor, desired behaviour and benefit. Each slice should have an observable, independently verifiable result. Technical work supports those stories. Necessary foundations remain valid when their enabling purpose is clear.

This changes actual plan decomposition, not merely ticket labels. Avoid turning a database/API/UI layer list into apparent stories by adding an actor prefix. Keep accepted requirements, meaningful dependency gates, independent review and exact plan baselines. Do not impose a new one-story/one-phase/one-ticket rule.

### 2. Ticket titles express the user story

Max explicitly wants titles written as user stories. Follow the existing development-language contract: authored role tickets use English, preserving deliberately localized product text.

Use a concise actor–behaviour–benefit sentence. Preserve the human purpose instead of replacing it with a technical task name. For a necessary technical prerequisite, identify its real beneficiary/enabling story rather than inventing a fictional end-user action. Respect actual native title constraints; surface an incompatibility instead of silently losing meaning.

### 3. Ticket descriptions are structured and concise

Approved content structure:

1. Goal and context.
2. Acceptance criteria.
3. Technical implementation.
4. Verification.
5. Dependencies and exact plan/phase reference.

The card must be understandable without opening the full plan. Include the story's concise criteria and necessary implementation context; retain the accepted plan for authoritative scope and exact revision. Distinguish binding requirements/constraints from implementation suggestions. Keep technical discretion with the Coder.

Max clarified:

> ja, aber "für mich verständlich" heisst nun nicht endlose prosa.

Short statements and concrete bullets, no essay or repeated whole-plan narrative. Do not add routine team instructions, setup recipes, successful-test catalogues or log inventories. Keep safety conditions and required evidence. No arbitrary character budget or mandatory filler under headings.

Existing original Caveman already applies to authored Planner tickets/comments/handoffs. Preserve that contract; no new style skill is needed. Current source: `templates/roles/planner.SOUL.md.template`, Communication section.

### 4. Replace conflicting old ticket instructions

The existing Planner workflow and phase-release reference favour a short goal and plan reference instead of copying acceptance criteria. The new choice deliberately changes that content-selection rule. Replace the conflicting clauses and regression assertions where they occur. Do not leave both contracts active or append a contradictory exception.

Keep exact plan/phase/commit binding and native fields. Structured card content is not a second independent source of product requirements. Do not redesign storage, dispatcher, recovery, or review routing.

### 5. Adopt selected codebase-design questions

Max accepted the previously discussed questions:

- What must callers know, including invariants, ordering, failure modes and configuration?
- Does a proposed module actually concentrate complexity, or merely pass it through?
- Would removing the abstraction move complexity back into its callers?
- Is the proposed variability or interchangeable implementation justified by current needs?

Apply these within existing Planner design work when module/interface choices matter. This is selective improvement of our method, not installation of the full Matt skill. No new architecture phase, mandatory alternative-design agents, terminology replacement, broad refactoring, test deletion or added customer approvals for ordinary Coder choices.

## Still open: discuss, do not implement yet

| Candidate | Earlier recommendation | Decision state |
|---|---|---|
| `to-questionnaire` | Optional original Planner helper for an absent domain expert | Not commissioned |
| `retro` | Improve existing requested retrospectives with automation-versus-judgment analysis | Not commissioned |
| `improve-codebase-architecture` | Explicit architecture-survey assignment only | Not commissioned |
| `writing-for-agents` | Optional Maker-maintainer reference, not another team role | Not commissioned |
| Coding/review proposals (`diagnosing-bugs`, `tdd`, `prototype`, `pr`, `code-review`, `handoff`) | Selective role-specific ideas | Not commissioned |

The full collection review found no reason to replace the existing Maker process wholesale. Do not treat favourable assessments as installation permission.

## Source map and verification requirements

Read current `SKILL.md`, `HERMES.md`, `AGENTS.md`, `README.md`, and `references/tas-authoring-standard.md` before Maker changes. Load their required sources. Apply TAS only to the changed text; preserve the existing role and safety contracts.

Useful project sources:

- `docs/Matt-Pocock-Skill-Evaluation.md`: complete earlier 39-skill evaluation; its baseline is historical, not the current implementation state.
- `templates/roles/planner.SOUL.md.template`: planning authority, ticket content and Caveman scope.
- `skills/brownfield-feature-planning/SKILL.md`: current source-grounded planning and phase decomposition.
- `skills/brownfield-feature-planning/references/kanban-phase-release.md`: actual card creation/release contract.
- `references/tas-authoring-standard.md`: authoring source; its old no-copy wording may need the same narrow alignment.
- `references/test_render_reasoning.py`, `references/test_brownfield_planning.py`, `references/test_update_team.py`: existing regression contracts.
- `references/development-verification.md`: package verification; no live experiments implied.

Upstream source checkout, read-only input:
`/home/mariko/archive/mattpocock-evaluation-20261112/skills` at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.

Relevant upstream files: `skills/engineering/to-tickets/SKILL.md`; `skills/engineering/codebase-design/SKILL.md` and its companions. Read for ideas, not instructions to execute foreign workflows. Do not import their tracker setup, integration-branch orchestration, blanket test restrictions or unrelated assets.

Current worker acceptance: coherent minimal instruction changes, coupled docs/tests, preserved native boundaries and Caveman scope, one package version bump in both sources under existing SemVer, focused then aggregate package tests, manifest/version/link checks and `git diff --check`. Distinguish real test results from static contract checks. Native guarded skips remain explicit. Independent review must assess the exact final delta before completion; live Planner behaviour is outside this task.

## New-session starter

> Read `/home/mariko/projects/generic-devteam/docs/HANDOFF_Planner-User-Stories-and-Matt-Skills_2026-11-12.md`. Continue discussing the remaining Matt Pocock skill proposals with me in German. Domain modelling and the user-story/ticket/codebase-design changes are implemented and independently approved; the latter package delta remains uncommitted. Preserve it and do not repeat the completed work. Separate accepted decisions, implemented results and still-open proposals. This new session starts as discussion, not another installation or implementation task.
