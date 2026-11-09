# Devteam Interface Improvements — Maker Revision Plan

> **For workers:** This document specifies a later Maker revision. Implementation requires separate approval. Keep the established Planner → Coder/Codex → independent Reviewer workflow. Do not create tickets, update live teams, change runtime configuration, or deploy from this planning request.

**Status:** Consolidated plan for Max's final review; not released for implementation.
**Document version:** 2.0.0. The major revision replaces incompatible authority, file-exclusivity, escalation, and retry-policy statements in the earlier proposal. This is not a Maker package release.
**Goal:** Reduce unnecessary technical handoffs, repeated investigation, and approval loops while preserving independent review and customer-owned decisions.
**Architecture:** Keep separate Planner, Coder, Codex, and Reviewer roles. The Coder owns implementation decisions within the accepted plan. The Planner plans, accompanies execution in Mattermost, checks real escalations, and obtains customer decisions. Use native Kanban transitions and existing recovery helpers.
**Technical basis:** Maker role templates, Maker-owned skills and references, existing Python instruction/rendering/update tests, native Hermes Kanban, and Team-Codex.
**Specification:** Sections 1–6 consolidate the original proposal, Picard's review, and Max's subsequent decisions in this conversation. They are the specification for the implementation work in sections 7–9. Read this document as a whole; the historical documents are provenance, not competing instructions.

## 1. Baseline and scope

Working repository: `/home/mariko/projects/generic-devteam`.
Inspected branch: `develop`.
Inspected commit: `bd7664b531250c5583dec58d21570de1cace1120`.
Inspected Maker package version: `1.1.22`.

Historical inputs remain unchanged:
- [Original proposal](2026-11-08_155912-PLAN_1.0.0_Devteam-Kanten.md).
- [Picard's review](REVIEW_1.0.0_Devteam-Kanten.md).

Confirm the authorized checkout, branch, and current source before implementation. The repository's historical `HERMES.md` describes another checkout and earlier work. Do not use those old bindings to switch repositories, branches, or teams for this assignment. Resolve the implementation binding before edits.

### Global constraints

- Change Maker-owned instructions and their existing tests only where this contract requires it.
- Preserve the separate roles, independent quality verdict, native dispatcher, serial dependencies, wake subscriptions, and same-ticket history.
- Preserve customer requirements, security, privacy, data integrity, external contracts, explicit financial limits, access restrictions, and operational approval boundaries.
- Preserve configured model/provider choices, reasoning limits, and required independent passes for material critical invariants.
- Keep source authorship, Maker release, authorized team update, effective instruction loading, and live behavior verification separate.
- Do not add a dispatcher, polling loop, new role, closing ticket, evidence register, or general workflow framework.
- Keep upstream components and native lifecycle semantics unchanged. Report a concrete upstream conflict instead of concealing it with a competing local policy.
- Apply the existing [TAS standard](../../references/tas-authoring-standard.md). Keep role instructions short and positive. Put detailed recovery recipes in the existing references.

## 2. Responsibilities and decision authority

### 2.1 Planner

The Planner clarifies the request, prepares the plan, obtains customer acceptance, creates dependent tickets, and accompanies execution in Mattermost.
The Planner owns authorized planning documents, project context, and planning Git history.
The Planner distinguishes binding requirements and architectural constraints from implementation suggestions.
Expected file lists describe likely affected paths unless explicitly marked as hard boundaries.

Each acceptance criterion belongs to an implementation ticket and its existing independent Reviewer.
Put combined-behavior checks in the phase where the integrated behavior becomes available.
Do not create another review role or a closing ticket for these checks.

During execution, the Planner checks a reported blocker before involving the customer.
Use the existing question and evidence to determine whether the Coder overlooked an in-scope solution or a decision is genuinely missing.
If a solution was overlooked, record the useful correction and return the work to the Coder without customer approval.
This is a check of an actual escalation, not a second mandatory technical investigation of every Coder decision.

For a genuine customer-owned decision, discuss it in Mattermost, record the sufficient final answer and its scope on the ticket, and resume the affected work.
Do not ask for another start instruction when the answer already permits continuation.

### 2.2 Coder

Move the existing execution-time discretion from the Planner template to the Coder template.
The Coder resolves technical implementation questions within the accepted goal and constraints.
Preserve agreed function, essential usability, explicit requirements, security, privacy, data integrity, permissions, cost boundaries, and external contracts.
Several small decisions must not accumulate into an unapproved redesign.

The Coder applies existing requirements and applicable customer decisions without asking again.
The Coder fixes the cause within the assignment, including a shared code path when necessary.
A suggested implementation or expected file list does not prevent that correction.
An explicit binding constraint remains binding until amended under the applicable authority.

The Coder investigates Codex questions and corrects recoverable invocation errors or incomplete runs independently.
Do not block the ticket merely to obtain permission for a corrected call, a necessary follow-up, or a valid resume.
Escalate a missing customer decision, missing permission, or a concrete obstacle that cannot be resolved within the mandate.

Use this core implementation instruction:

> Implement the ticket requirements with Codex.

Replace blanket Codex-only project-file writing rules with that instruction.
Do not replace them with file-type lists, planning-file exemptions, rules about the Coder's working files, or a content-versus-extension slogan.
The rule assigns ticket implementation to Codex; it does not prohibit the Coder from using its own working helpers.
Keep that explanation in this plan, not as an additional helper-file policy in the generated SOUL.

Use positive documentation duties:

> Document decisions, progress, and verification results on the existing Kanban ticket. Maintain the project changelog.

Use the project's established changelog convention and version grouping.
Changelog maintenance can be included in the Codex assignment.
Do not require a separate process report or an authored run-log document.
Existing platform logs remain available evidence, not another writing obligation.

### 2.3 Reviewer

The Reviewer independently assesses the candidate against the accepted requirements and owns the quality verdict.
Return defects, missing evidence, unresolved questions, and requirement conflicts to the Coder on the same ticket.
A question is not automatically a proven defect.
The Reviewer does not deliberately route a decision question to the Planner.

The Coder first resolves the return within its authority.
Only the Coder escalates an unresolved customer decision through the Planner.
After clarification, the Coder presents the candidate or explanation to the Reviewer again.
An explanation can resolve a return without a project edit or an empty commit.
A Coder answer or customer decision does not itself approve the implementation.

Successful review completes the ticket directly.
DONE has no return to the Coder.

### 2.4 Binding plan amendments

The Coder records consequential in-scope decisions on the ticket without creating a new approval record for each local choice.
For a necessary change to a binding requirement outside its authority, the Coder supplies facts, options, a recommendation, and the paused work.
The Planner obtains the required customer decision and maintains the amended versioned plan.
Update the affected current and future ticket bindings before release.
Preserve already-reviewed history and confirm that the returning worker uses the applicable baseline.
The Planner maintains the record; this does not restore routine technical approval ownership.

## 3. Native workflow and recovery

### 3.1 Normal flow

1. Customer and Planner agree on the request and accept the versioned plan.
2. Planner creates and verifies the dependent tickets, role assignments, workspaces, and Mattermost wake subscriptions.
3. Dispatcher starts the Coder for the eligible ticket.
4. Coder directs Codex, resolves in-scope questions, and establishes review readiness.
5. Coder commits task-owned changes and requests independent review.
6. Reviewer either returns findings/questions to Coder or approves the exact reviewed commit and completes the ticket.
7. Dispatcher releases eligible successors. Planner reports concise progress from existing results.
8. When the last required ticket is DONE, Planner confirms the required plan tickets have completed and sends a short customer report from their results and review verdicts.

The final report states the delivered result and any recorded outstanding limitation or separately pending publication action.
It does not introduce a new technical review by the Planner.

### 3.2 Transition contract

Use the existing technical profile and board bindings. The operations below name native contracts, not new APIs.

| Trigger and actor | Operation | Required destination/result |
|---|---|---|
| Coder has review-ready work | `kanban_request_review`, with `summary` and the bound independent `reviewer` | Same ticket enters review for the Reviewer. Verify actual state and recipient. |
| Active Reviewer has findings or questions | `kanban_comment` for the precise finding/question, then `kanban_request_changes` with `reason` | Native return restores the original Coder and reapplies dependency gates. |
| Active Reviewer approves | `kanban_complete`, with `summary` and metadata containing `review_outcome`, `reviewer_checks`, and `reviewed_commit` | Use `review_outcome="approved"`; ticket reaches DONE for the exact reviewed commit. |
| Coder needs customer input | `kanban_comment` for the question, then `kanban_block(kind="needs_input", reason=...)` | Coder remains assigned. Existing Planner subscription wakes the customer-facing Planner. |
| Planner resolves a Coder-origin ordinary blocker | `kanban_comment`, then `kanban_unblock` with exact `task_id` and `board` | Return to Coder execution, subject to parent gates and current claim checks. |
| Planner resolves automatic triage | Existing installed `scripts/recover-triage` launcher under the recovery reference's checks | Recover the same card through the appropriate native transition; verify actual phase and assignment. |
| A technical interruption occurs during review | Existing native unblock/recovery path after the cause is resolved | Restore unfinished review. A technical interruption is not a substantive return to implementation. |

For comments, pass the exact `task_id` and the text as `body`.
Read back the posted decision and resulting task state.
The Planner's Mattermost wake is an orchestration context, not an active Reviewer run.
It cannot substitute `kanban_request_changes` for ordinary unblocking or triage recovery.

### 3.3 Blocked and triage work

For this team's workflow, **triage means blocked work**.
Never deliberately create or send work to triage.
Native repeated-block routing can still put a ticket there; that event changes the recovery operation, not the task's purpose.
Do not infer decomposition, replacement tickets, or a new planning exercise from triage.

On either a blocked or triage event, the Planner:

1. Reads the exact ticket, current blocker, latest run, assignment, and existing decisions.
2. Checks whether the Coder overlooked an available in-scope solution.
3. If so, records the correction and resumes the Coder without a customer round.
4. Otherwise coordinates permitted technical recovery or obtains the missing customer decision through Mattermost.
5. Records the sufficient answer or resolved cause and any required baseline amendment.
6. Uses the state-appropriate existing transition, then verifies recipient, phase, and parent gates.

An unresolved capability failure or a known quota pause remains a real blocker.
Keep the established capability/transient classification, verified reset information, and authorized native one-time resumption procedure.
Do not confuse these with recoverable Coder invocation errors.
Technical recovery outside existing permissions requires the appropriate approval; a status label grants none.

The existing [recovery reference](../../skills/brownfield-feature-planning/references/kanban-triage-recovery.md) owns the installed native API checks and bound-launcher recipe.
Retain its guards against competing claims, wrong databases, bypassed dependencies, and direct SQL mutation.
Retain native counter semantics, including any resets performed by a legitimate native transition.
Do not manually reset counters, rotate block kinds, or replace a card to escape a guard.

### 3.4 Duplicate or stale events

Before resumption, reconcile the actual blocker, run, answer scope, and task state.
An old answer must not clear a newer blocker.
An already-active or completed task must not be released again.
Distinguish queued, started, and baseline adopted.
Use the existing native lifecycle and state guards; do not add an exactly-once transport claim or custom delivery framework.

## 4. Review readiness and independent verification

The Coder establishes a trustworthy handoff, not a second full independent review.
Inspect the actual diff, task scope, working tree, staging, commit, and original check results.
Resolve visible inconsistencies and known defects; disclose unfinished or unavailable checks.
A Codex completion message alone is not evidence.

The Reviewer assesses the source, affected dependencies, failure paths, acceptance criteria, and required checks independently.
Keep required risk-based reasoning and separate passes for material critical invariants.
Use internal Codex review helpers only for a concrete risk or evidence gap, not an automatic extra stage.

Reuse original check evidence while its inputs, relevant dependencies, configuration, and conditions remain valid.
Keep the original executor and checked state identifiable.
Repeat affected or insufficient checks and required independent or final-state checks.
A handoff or new commit alone does not invalidate every result.
After a correction, assess the delta and affected dependencies and account for every open finding.

Handoffs state the exact commit, scope, actual results, accessible evidence references, open gaps, risk, and next action.
Describe each finding once and reference it unambiguously.
Keep older binding decisions available when reducing context; latest comments alone may be insufficient.

Independent review creates no additional external-action permission.
For example, an already-consumed one-shot upload allowance does not renew when the Reviewer starts.
Use valid existing evidence; return a remaining evidence gap to the Coder if the missing check is not permitted.
Ordinary checks already covered by the assignment need no new approval.
This is a targeted acceptance case, not a new permission registry or routine approval gate.

## 5. Progress, retries, and runtime limits

Replace fixed discretionary correction counts and routine extension requests with progress-based execution:

> Work until the acceptance criteria are met. Correct recoverable failures independently. Do not repeat a failed approach unchanged. Escalate the concrete obstacle when no justified next approach remains.

Stop after the accepted result and required checks are complete.
Do not continue optional polishing or invent additional acceptance criteria.
A diagnosed correction, changed approach, necessary follow-up, or valid resume does not need another start approval.
Remove the generic escalation trigger after three substantive review returns.
Clarification-only returns are not defect-correction cycles and need no new budget counter.

Do not impose a generic short hard Codex timeout as an efficiency policy.
Distinguish the tool's foreground wait window from a process-termination deadline and from native stuck-worker protection.
Use the existing supported long-running execution path and completion signals.
A long productive run is not by itself a reason to stop or ask the customer to continue.

Preserve explicit customer financial/resource caps, configured model/reasoning limits, operational permissions, provider quotas, and native failure-loop guards.
These are not discretionary retry allowances.
Existing local team mandates need semantic reconciliation during an authorized update; do not silently transfer or enlarge them.

No runtime timeout source or global configuration change is authorized by this plan.
If an existing runtime limit prevents the approved workflow, identify its actual consumer and effect, then report the separately scoped configuration decision.
The discussed `1800`-second example is not a verified universal Maker setting and must not become a new default.
Keep tests that bound documentation size and technical per-command timeouts unrelated to Codex execution; they are not Coder attempt budgets.

## 6. Review disposition

| Review item | Resolution in this plan |
|---|---|
| R1 — discretion and binding plan changes | Move execution-time discretion to Coder; distinguish requirements from suggestions; Planner maintains authorized amendments. |
| R2 — Codex-only file changes | Replace the parent rule rather than add exceptions. Bind ticket implementation to Codex. Keep ticket documentation and changelog duties positive. |
| R3 — mandatory Coder-first returns | Findings/questions return to Coder. APPROVE goes directly to DONE. Planner screens real blockers. Triage is blocked work with a different recovery operation. |
| R4 — discretionary budgets | Remove generic attempt-based escalation and extension loops. Use progress-based stopping. Preserve explicit limits and native protection; reconcile local exceptions only where they actually exist. |
| R5 — verification permissions | Cover the concrete restricted-action case without a new routine approval system. |
| R6 — cross-phase acceptance | Assign integrated-behavior criteria to existing implementation phases and their existing Reviewer. Planner closes from results, not a new technical examination. |

The SOOS and MTB histories motivate scenarios; they are not fresh execution evidence or a measured savings estimate.

## 7. Maker change map

Paths below are relative to the repository root. They identify expected edit targets, not permission to rewrite unrelated sections.

| Source | Focused change |
|---|---|
| `templates/roles/planner.SOUL.md.template` | Move execution-time discretion and routine technical approval out. Keep planning ownership. Add actual-blocker screening, customer discussion/answer recording, state-appropriate resumption, triage-as-blocked handling, and final customer report. Replace old `ESCALATE_PLAN` review-return instructions. |
| `templates/roles/coder.SOUL.md.template` | Add transferred discretion. Replace blanket file-write restrictions with the Codex implementation instruction. Add positive ticket/changelog duties. Use needs-input instead of Planner review. Remove fixed correction-count escalation. Preserve readiness inspection and independent Reviewer handoff. |
| `templates/roles/reviewer.SOUL.md.template` | Replace direct Planner escalation with Coder-first returns. Respect permitted Coder discretion. Cover questions without fabricated defects or commits. Preserve approval-to-DONE, independent verdict, evidence reuse, and critical passes. |
| `skills/brownfield-feature-planning/SKILL.md` | Align plan discretion, binding/suggested content, integrated acceptance allocation, and progress-based planning. Remove generic retry-budget creation/renewal duties and the authored-run-log ambiguity. |
| `skills/brownfield-feature-planning/references/kanban-phase-release.md` | Preserve exact baselines, subscriptions, blocked-first dependency release, and state readback. Distinguish explicit/native limits from invented work budgets. Keep results on the existing card without an extra log-writing duty. |
| `skills/brownfield-feature-planning/references/kanban-triage-recovery.md` | Replace old Planner technical-approval assumptions. Treat triage as blocked work. Retain the bound helper and state/claim guards. Separate customer-decision return to Coder from technical review recovery. |
| `references/native-workflow.md` | Reconcile any clarification-route descriptions with existing profile bindings. Preserve renderer fields and installation bindings. |
| `references/update.md` | Add a focused transition procedure for old Planner-review clarification cards and authority conflicts during a separately authorized team update. Preserve the existing updater and unrelated retirement rules. |
| `references/test_render_reasoning.py` | Update conflicting assertions and cover the new rendered role contracts. Preserve evidence, risk, provider, and placeholder checks. |
| `references/test_brownfield_planning.py` | Cover planning/recovery consistency, positive documentation duties, and absence of competing old routes. Preserve specialist gates and context-size checks. |
| `references/test_triage_recovery.py` | Extend existing synthetic-board scenarios for needs-input recurrence, return phases, current ownership, and safe repeated recovery. Preserve guard-denial coverage. |
| `README.md`, `references/development-verification.md` | Update only workflow and authoring-verification descriptions affected by this change. Keep ordinary setup free of behavioral experiments. |
| `SKILL.md`, `manifest.json` | Apply one package version step at release and preserve synchronized versions, inventory, assignments, and render fields. Keep this repository-only plan outside the package manifest. |

Inspect the assigned execution/review skills and any Maker-owned specialist clauses for actual conflicts before editing.
Do not rewrite unrelated installed or upstream instructions.
The bound recovery script, renderer, and updater require no speculative rewrite; retain them unless a failing acceptance case demonstrates a necessary Maker-owned correction.

### Known test changes

`test_coder_routes_decisions_outside_its_mandate_to_planner` currently requires the old Planner `kanban_request_review` route and `kanban_request_changes` resume. Replace those expectations with the needs-input/orchestrator-resume contract; preserve technical profile validation and the unrelated TIMER binding.

`test_planner_renders_platform_repair_authorization_boundary` currently expects the Planner's implementation-discretion sentence. Move that assertion to the Coder contract while preserving platform-repair approval checks.

`test_planner_checks_blocker_premises_before_adding_requirements` must test screening of an actual escalation, not mandatory Planner re-investigation of ordinary Coder decisions.

Existing correction-evidence tests already cover attribution, validity, and independent verdicts. Extend them where needed instead of adding another duplicate policy.
`test_proposal_chain_budgets` measures instruction sizes; retain it.

## 8. Implementation sequence after approval

Keep the established native Coder/Codex implementation and independent Reviewer route. Do not substitute a new orchestration method from a generic planning skill.

### Phase 1 — Consistent role and recovery contract

**Consumes:** Sections 1–6 and the inspected source, refreshed against the authorized implementation checkout.
**Produces:** A coherent unpublished Maker candidate with matching role, planning, phase-release, recovery, and test contracts.
**Files:** The three role templates, Maker-owned planning/recovery references, relevant binding prose, and the existing contract/recovery test files listed in section 7.

- [ ] Confirm current Git state, applicable instructions, assigned skill-loading paths, and existing native transition contracts. Preserve unrelated work.
- [ ] Add focused failing assertions in the existing test classes for transferred discretion, Codex implementation wording, changelog duty, Coder-first questions, needs-input escalation, Planner screening, triage-as-blocked, direct approval, and progress-based continuation.
- [ ] Run the focused tests and confirm failures concern the old policy, not unavailable infrastructure or unrelated baseline failures.
- [ ] Replace conflicting clauses at their source. Keep exact routing tools in role workflows and detailed recovery in the existing reference.
- [ ] Extend synthetic native recovery tests for the lifecycle cases in section 9. Use only scratch databases and an already installed suitable interpreter. Do not bootstrap or repair Hermes to make tests run.
- [ ] Run focused rendering/planning/recovery tests. Preserve skipped or denied native checks as explicit missing evidence; do not bypass guards.
- [ ] Review the combined role-and-companion diff against every section 9 case. Distinguish static policy consistency from executed native transitions.
- [ ] Commit only the focused candidate when implementation and local commit work are authorized. Request independent review on the same phase ticket.

**Gate:** All role and companion instructions describe the same routing and authority. No competing Planner-review clarification default remains. Required source contracts and available synthetic transitions pass; missing native verification remains an explicit release blocker for the affected transition.
**Suggested commit:** `feat: simplify devteam execution authority and review handoffs`.

### Phase 2 — Update compatibility and release verification

**Depends on:** Independently accepted Phase 1.
**Consumes:** The exact reviewed candidate and existing updater/recovery contracts.
**Produces:** A reviewed Maker release candidate with safe update instructions and complete combined-contract evidence, not an installed team.
**Files:** `references/update.md`, focused README/development-verification sections, `SKILL.md`, `manifest.json`, and related existing tests where needed.

- [ ] Write the old-card migration procedure described below into the existing update instructions.
- [ ] Add focused assertions for migration order, active-worker preservation, local authority reconciliation, and the distinction between saved files and effective instructions. Reuse updater fixtures when a changed update contract needs execution coverage.
- [ ] Classify the package release once under `AGENTS.md`. Treat the coordinated incompatible clarification-route change as a MAJOR release; from the inspected package baseline the target is `2.0.0`. If another release intervened, resolve the correct next MAJOR version before editing both version sources together.
- [ ] Run the existing renderer suite before the aggregate suite using section 10. Check complete manifest inventory, unchanged rendering fields, role bindings, local links, and update preservation.
- [ ] Assess the complete candidate against all section 9 cases and the preserved independent-review obligations. The existing Reviewer performs this gate; the Planner does not repeat it.
- [ ] Commit the verified release candidate when authorized and obtain its independent same-ticket verdict. Report exact reviewed commit, actual checks, missing evidence, and separate rollout status.

**Gate:** The final candidate satisfies the complete specification and preserves existing update/local-adaptation behavior. No live activation is claimed.
**Suggested commit:** `docs: define devteam workflow migration and release verification`.

### Existing-team migration procedure to author, not execute now

1. During an explicitly authorized team update, inspect affected active cards and their actual phase/assignment before applying authority changes.
2. Let active workers finish under their existing contract or obtain a separately scoped transition decision. Do not mix old and new loaded roles on one active handoff.
3. Reconcile local instructions that preserve the old Planner-review route, fixed discretionary retry approvals, or separate customer-approved limits. Keep unrelated local adaptations. Escalate only genuinely conflicting explicit mandates.
4. For a legacy clarification card actively owned by a Planner review run, let that owner finish the established native return to its original Coder. This is a migration-only completion, not the new default.
5. For a parked legacy review card with no active run, resolve the actual blocker and use existing source-phase recovery. If clarification is complete and Coder continuation is required, use the existing guarded review-reopen procedure to restore the original implementer. Preserve pending independent review instead of reopening it indiscriminately.
6. Read back card identity, decisions, implementation owner, review provenance, parent gates, and phase. Keep the same card and its history.
7. Verify effective loading for subsequent execution contexts separately from saved file bytes. Do not restart a gateway or session merely because the files changed.

## 9. Acceptance scenarios and ownership

These are required verification cases, not claims that tests have already run.
P1 means Phase 1; P2 means the existing final-phase Reviewer confirms the complete candidate.
Static instruction tests prove wording/rendering contracts, not live agent compliance.

| ID | Scenario | Required result | Verification owner/surface |
|---|---|---|---|
| A01 | Codex asks an in-scope technical question | Coder answers and continues without Planner approval. | P1 role contract; P2 full review |
| A02 | Necessary root-cause fix differs from a suggested file list | Coder can fix the affected shared path within the goal; binding constraints remain protected. | P1 planning/Coder contract |
| A03 | A binding requirement needs changing | Coder escalates; Planner obtains the decision and updates affected baselines before continuation. | P1 amendment scenario |
| A04 | Coder needs a working helper or maintains the changelog | No blanket file-write ban or file-type policy; ticket implementation remains assigned to Codex. Ticket and changelog duties are positive. | P1 rendered Coder contract |
| A05 | Codex invocation fails recoverably | Coder corrects it without blocking or asking for another start. | P1 execution contract |
| A06 | Reviewer asks a technical question | Native return to Coder; no direct Planner decision route. | P1 role contract and synthetic return |
| A07 | Coder resolves a Reviewer question without a file edit | Explanation and valid exact-commit evidence go back to independent review; no empty commit. | P1 correction scenario |
| A08 | Reviewer question really needs customer input | Reviewer → Coder → needs-input → Planner/Mattermost → Coder → Reviewer. | P1 contract and synthetic phase checks |
| A09 | Reviewer approves | Exact-commit verdict completes the ticket; no new Coder run for a return. | P1 approval contract; P2 full review |
| A10 | Planner receives a blocked card with an overlooked solution | Planner records the bounded correction and resumes Coder without a customer round. | P1 Planner/recovery contract |
| A11 | Customer supplies a sufficient answer | Decision and necessary baseline changes are recorded; Coder resumes without another start request. | P1 ordinary unblock scenario |
| A12 | Distinct customer questions trigger automatic triage on the same card | Treat as blocked; resolve cause and recover same card. No intentional triage, decomposition, replacement card, or counter manipulation. | P1 synthetic recurrence/recovery and prose |
| A13 | A duplicate or stale wake/answer arrives | Do not clear a newer blocker, race an active claim, or release completed work again. | P1 recovery guards; P2 full review |
| A14 | A technical interruption occurs during independent review | Recover unfinished review with the same provenance; no unnecessary Coder correction round. | P1 synthetic review recovery |
| A15 | Real capability failure or provider quota stops execution | Preserve actual cause and existing native recovery ownership. Do not bypass permission or provider limits. | P1 exception contract |
| A16 | Several justified corrections or a long productive Codex run occur | Continue under existing authority; no generic correction-count approval or short-timeout policy. Report actual external/runtime constraints separately. | P1 progress contract; P2 configuration-scope review |
| A17 | Repeated attempt yields no progress or justified new approach | Diagnose and escalate the concrete impasse instead of repeating blindly. Finish when required acceptance is met. | P1 stopping contract |
| A18 | Correction affects a shared dependency | Refresh affected evidence and review dependencies; reuse unaffected valid results with attribution. Account for every open finding. | P1 existing evidence tests extended |
| A19 | Explicit one-shot external permission is already consumed | Review does not renew it. Reuse valid evidence or return the gap to Coder; ordinary permitted tests need no new approval. | P1 permission scenario; P2 full review |
| A20 | Individual components pass but combined behavior is untested | Existing integration phase and existing Reviewer cover the missing criterion before completion. Planner reports results, not a new technical review. | P1 phase-plan contract; P2 combined gate |
| A21 | Existing team has a legacy Planner-review clarification card | Safe same-card migration under current ownership; new questions use only the new route. | P2 update contract and available fixtures |
| A22 | Last required ticket reaches DONE | Planner checks the required ticket results and sends a short Mattermost customer report. No closing ticket, duplicate full review, or automatic publication. | P2 completion scenario |

**Review focus:** Overlooked technical solution (A10); triage after different questions (A12); stale decisions (A13); review-phase interruption (A14); old active Planner-review card (A21).

## 10. Verification commands and evidence boundary

Run these during the later Maker implementation, from its confirmed repository root:

```sh
python3 -B -m unittest discover -s references -p 'test_render_reasoning.py' -v
python3 -B -m unittest discover -s references -p 'test_brownfield_planning.py' -v
python3 -B -m unittest discover -s references -p 'test_*.py' -v
git diff --check
```

Use the already installed Hermes-capable interpreter for native recovery tests when required by the existing suite.
Keep temporary fixtures in the authorized scratch area.
The aggregate command can report native tests as skipped when the interpreter or guard does not permit them; a successful process exit with those skips is not native lifecycle proof.
Use [development verification](../../references/development-verification.md), including existing renderer, updater, manifest, and recovery checks.

For this plan-only deliverable, validate local links, expected paths, scenario coverage, whitespace, and the documentation-only Git scope.
Do not run package tests or live workflow experiments merely to author the plan.

A later package test pass proves neither instruction loading in existing sessions nor live-agent behavior.
Live-team rollout, runtime-limit changes, production actions, and measured efficiency experiments require separate authorization.
The expected efficiency benefit remains a hypothesis until measured on comparable work.
