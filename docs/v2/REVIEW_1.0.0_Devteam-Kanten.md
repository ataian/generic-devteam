# Review response — Devteam interface improvements

**Document version:** 1.0.0.
**Author:** Picard, planning review.
**Status:** Review findings and customer clarification. Not an implementation approval or live-team policy activation.
**Reviewed proposal:** [Devteam Interface Improvements — Review Plan, 1.0.0](2026-11-08_155912-PLAN_1.0.0_Devteam-Kanten.md).
**Source baseline inspected:** Maker commit `f5105a13d3a1516252810e62636e0cc07ad4333c`, branch `develop`, in `/home/mariko/projects/generic-devteam`.
**Scope:** Capture the preceding read-only analysis and incorporate Max's subsequent routing clarification. Preserve the supplied proposal unchanged. Do not change templates, installed skills, profiles, tickets, runtime configuration, or package version.

## 1. Assessment

The proposed separation can reduce unnecessary handoffs without removing independent quality review. MTB history contains technical questions that the Coder could resolve under the proposed authority instead of sending them through another Planner investigation.

Before implementation, clarify the boundary between Coder decisions and binding plan changes, preserve the Planner's planning-file authority, and make the Reviewer-to-Coder return mandatory. Add targeted acceptance scenarios for evidence permissions, recovery, and complete cross-phase acceptance. Do not add another role, dispatcher, evidence register, or closing ticket.

This is a policy and contract review. It is not a live execution test of the proposed workflow, a Maker release approval, or a measured token-saving claim.

## 2. Customer clarification: every Reviewer return goes to the Coder

### Confirmed target behavior

Max clarified the intended future process after the initial review response:

> „der reviewer muss immer zum \"coder\" zurückgeben. weil dieser diese fragen erstmal selbst beantworten könnte. es gibt keine eskalation an den \"planner\" mehr, nur falls der coder eine sache nicht entscheiden kann, eskaliert der coder an den planner (der dann den kunden fragt/bespricht). aber ein reviewer wird niemals an den planner geben dürfen“

Apply that clarification when revising the proposal:

1. The Reviewer returns defects, unresolved questions, and requirement conflicts to the Coder on the existing ticket.
2. The Coder first checks whether the question is answerable within the accepted requirements and the Coder's authority.
3. If it is answerable, the Coder records the answer and directs Codex to make any necessary implementation changes. No Planner decision round is required.
4. Only if the Coder cannot decide does the Coder escalate to the Planner.
5. The Planner discusses the missing decision with the customer. The Planner does not act as the implementation-time technical decision owner.
6. After sufficient clarification and any necessary baseline coordination, the task returns to the Coder. The Coder submits the resulting candidate or explanation to the independent Reviewer.
7. The Reviewer retains the independent quality verdict. A Coder answer, Planner message, or customer decision does not itself approve the implementation.

The decision route is:

```text
Reviewer → Coder
             ├─ can decide → resolve → Reviewer
             └─ cannot decide → Planner ↔ Customer
                                  ↓
                                Coder → Reviewer
```

There is no deliberate Reviewer-to-Planner decision route, including when the Reviewer believes customer clarification is necessary. That assessment must first pass through the Coder.

### Correction to the initial review response

The initial response proposed a direct Reviewer clarification branch through the Planner, followed by return to the applicable review or implementation phase. That recommendation is withdrawn for the target process. It bypasses the Coder's opportunity to resolve the question and can create unnecessary customer escalations.

The confirmed change removes the Planner's technical decision layer during implementation. The initial review also raised existing Planner-owned budget exceptions. Max has not explicitly decided their future ownership. Do not infer their revocation, transfer, or automatic retention from the technical routing clarification. Record this as an open authority-reconciliation point, not an accepted policy change. Existing live mandates remain unchanged until an authorized update. See R4.

### Required proposal changes

- **Section 5.2, line 120:** The current sentence says that the Planner obtains a customer decision when the Reviewer discovers a genuine requirement conflict. It omits the mandatory Coder assessment. Replace it with the route above.
- **Section 3.2, point 6, and section 5.1, point 6:** Cover clarification returns as well as demonstrated implementation defects. A question is not automatically a proven code defect.
- **Section 4.2:** Add both a Reviewer question resolved by the Coder and a Reviewer question that only the Coder escalates through the Planner.
- **Section 4.1:** Reconcile conflicting Reviewer instructions and companion skills, not only the old Coder-to-Planner clarification instruction. Report an upstream conflict instead of silently overriding or patching an upstream method.

## 3. Findings and recommended amendments

### R1 — Define Coder discretion versus a binding plan amendment

**Priority:** Resolve before implementation.
**Proposal references:** Sections 2.1, 2.2 points 1–4, and 5.2.

The Coder gains technical authority, while approved architectural constraints and exact plan baselines remain binding. The proposal does not fully define the case where the product goal is unchanged but a necessary implementation differs from a binding technical prescription.

Distinguish these cases explicitly:

| Case | Target handling |
|---|---|
| Free implementation detail or explicitly nonbinding implementation suggestion | Coder decides within the accepted constraints. |
| Question already answered by an applicable requirement or recorded customer decision | Coder applies that decision without asking again. |
| Necessary change to an explicitly binding technical constraint | Coder does not silently override it. Use the agreed amendment authority; if outside the Coder's mandate, escalate through the Planner to the customer. |
| New product behavior, scope, external permission, or unresolved customer trade-off | Coder escalates through the Planner to the customer. |

State whether file lists are hard boundaries or expected affected paths. Distinguish a necessary root-cause correction from an unrelated repair. Keep the rule against cumulative redesign through individually small decisions.

Assign authorship and coordination of any required versioned plan amendment. The Planner can maintain the accepted planning record and coordinate affected phases without repeating the technical investigation or becoming the technical approver. State which future phases must adopt the amendment; preserve already-reviewed history and verify adoption by affected workers.

**MTB evidence:** Board `mtb`, task `t_a6fa0cf6`, contained different classes of questions:

- Runs 26–27: treatment of MSI findings without a supplied NGS report required a customer domain decision.
- Runs 28–29: `NgsReportRepository` used String while the entity ID was UUID. A bounded technical correction was specified while preserving the service/HTTP contract.
- Runs 30–31: mapping an absent optional report specimen produced an invalid transient object. A bounded null-handling correction was specified.

The latter two cases are plausible candidates for direct Coder decisions under the new authority. This is a process assessment of historical task records, not a fresh code diagnosis or permission to reopen those completed tasks.

### R2 — Preserve planning-document authority outside Codex-only implementation

**Priority:** Resolve before implementation.
**Proposal reference:** Section 1, line 16.

“Codex remains the only unit that changes project files” is broader than the intended implementation boundary. It can include the Planner's plans, project context, and planning prerequisites. Requiring the Coder to commission every planning-document change would create new handoffs and a circular dependency during clarification.

Limit Codex-only authorship to implementation changes, including associated tests, configuration, scripts, and product documentation. Preserve the Planner's authority for authorized project bootstrap, project context, planning documents, and their local Git history. Preserve separate plan and implementation repository roots.

This exception permits planning work, not product implementation or unilateral changes to approved requirements.

### R3 — Specify native returns without bypassing the Coder

**Priority:** Resolve before implementation.
**Proposal references:** Sections 2.2 points 6–7, 3.2 point 6, 5.2, and 5.4.

Use the customer clarification in section 2 as the routing requirement. The intended ordinary clarification flow is:

1. The active Reviewer records the precise question and available evidence on the existing card.
2. The Reviewer returns the card to the original Coder through the native review-return operation.
3. The Coder resolves it or uses the proposed `needs_input` path to the Planner/customer.
4. After clarification, the Coder resumes and requests independent review again.

If the Coder resolves the question without a file change, do not manufacture a code edit or empty commit. Hand back the explanation and still-valid exact-commit evidence for the Reviewer's own assessment.

**Native semantics inspected:**

- `request_changes` requires an active run claimed from review and restores the original implementer.
- `unblock_task` restores the source phase, including review provenance, and reapplies parent gating.
- A Planner wake session cannot use `kanban_request_changes` as though it owned an active review run on a blocked card.

These facts constrain recovery. They do not justify a new direct Reviewer-to-Planner decision route.

Automatic crash, quota, capability, or triage events remain distinct from deliberate decision escalation. A native event may wake the Planner for recovery coordination; it must not authorize the Planner to decide the Reviewer's unresolved implementation question or bypass the Coder. Preserve native guards. If a failure prevents the normal return, recover the permitted transition and then continue through the Coder-first decision route.

Describe incomplete-question returns too: asking the Coder to supply missing facts is not a customer decision. Classify clarification-only returns separately from substantive defect-correction cycles when applying retry/reasoning limits. Do not reset native counters or misreport a clarification as a proven defect.

### R4 — Reconcile old discretionary budgets with the new decision owner

**Priority:** Resolve conflicting authority before applying the new rules to a team.
**Proposal references:** Sections 1, 2.1, 2.2 point 4, and 5.3.

The initial review noted that MTB's existing Planner mandate allows bounded discretionary budget extensions. Max clarified the technical decision route, but did not explicitly decide whether those separately delegated budget exceptions remain with the Planner or move elsewhere. Their future owner is therefore an open point, not a confirmed change.

Clarify that narrow boundary before applying conflicting instructions. Do not silently revoke, preserve, transfer, or expand spending authority. In particular, a retained budget exception must not become a back door for routine Planner technical approval. The Planner's planning, documentation, and organizational recovery responsibilities are separate from this question.

Preserve consumed budgets across corrections, reviewers, restarts, and sessions. Native circuit breakers, reasoning limits, access rules, and operational permissions remain separate constraints. No reset, replacement card, or retry loop is authorized by this policy review.

### R5 — Independent verification does not create execution permission

**Priority:** Add an explicit acceptance scenario.
**Proposal references:** Sections 3.2 points 4–5 and 4.2.

The proposal preserves permissions in general. Add a concrete scenario because the distinction has failed in MTB practice.

For the MTBNORD export, a single authorized upload/readback allowance had already been consumed. The permitted verification scope was also narrow. Historical Reviewer reflection/behavior probes exceeded that scope even though they were local. The deviation was recorded, not retroactively authorized.

Require these outcomes:

- Verification and external-action allowances apply across Coder, Reviewer, separate passes, restarts, and affected successor phases according to the actual authorization.
- An independent check does not receive a new upload, access, or execution allowance.
- Classify a check by what it executes, not by its name or whether it invokes a test runner.
- If permitted evidence is insufficient, identify the missing proof and return the issue through the Coder-first route. Do not approve without evidence or execute a forbidden check.

Keep the Reviewer's independent source assessment and required separate passes. Evidence reuse is not blind acceptance of a Coder summary.

### R6 — Assign cross-phase acceptance before the final report

**Priority:** Clarify the completion contract.
**Proposal reference:** Section 5.1, point 8.

A final report from existing task results is appropriate. Every cross-phase or final-state acceptance criterion must nevertheless have an execution phase and an independent review owner.

Assign those checks within the existing phase plan. At closure, the Planner reconciles completeness, exact reviewed commits, outstanding obligations, and separate publication permissions. The Planner does not start a surprise full technical review.

Individual green cards do not prove an unassigned integration criterion. Conversely, do not create a dedicated closing ticket when the existing phases can carry the required evidence.

## 4. Additional acceptance scenarios

These refine the proposal's existing scenarios. They are not executed test results.

| Scenario | Required outcome |
|---|---|
| Reviewer asks an in-scope technical question | Return to Coder; Coder resolves it; Reviewer assesses the answer. No Planner/customer decision round. |
| Reviewer identifies an apparently unresolved requirement | Return to Coder first. Only the Coder escalates if current requirements and delegated authority do not resolve it. |
| Coder answer requires no project-file change | Preserve the exact implementation commit and valid evidence; no empty commit; independent review still occurs. |
| Necessary correction differs from a binding technical prescription | No silent override. Apply the explicit amendment authority and coordinate affected phase baselines. |
| Two different customer questions occur on one card | Preserve both decisions and recover legitimate triage safely. Different wording does not reset same-kind block accounting. |
| An old or duplicate wake arrives | Reconcile exact task, current blocker, run, decision scope, and assignment. Do not clear a newer blocker or release an already-active worker again. |
| Customer gives a sufficient answer | Record the answer, finish necessary plan/binding coordination, and safely return to Coder without asking for another start command. Distinguish queued, started, and baseline adopted. |
| A vague escalation needs more facts | Return for bounded Coder investigation; do not invent a customer decision or a Planner technical approval round. |
| A correction changes a shared dependency | Renew affected checks and assess dependent behavior; delta review is not limited to the directly edited file. |
| A one-shot external allowance is exhausted | Reuse valid original evidence. Do not repeat the action for independent confirmation. Route any remaining decision through the Coder. |
| A clarification-only return occurs repeatedly | Keep it distinct from proven implementation defects when interpreting substantive correction limits; preserve native history and counters. |
| A team update encounters an old Planner-review clarification card | Use a migration rule that reconciles current ownership and safely returns to Coder. Do not abandon the card or keep the old route as a competing default for new questions. |
| All individual phases pass but a final acceptance criterion has no evidence | Report the specific unfulfilled gate; do not declare the full scope complete from phase status alone. |

The installed block recurrence logic compares the block kind, not the question text. Repeated `needs_input` pauses can therefore reach triage even for different questions. The proposal already acknowledges this; the test should make it explicit.

Native notification documentation does not guarantee exactly-once delivery. Require idempotent handling of repeated events rather than claiming transport-level exactly-once behavior. A stored subscription or queue admission alone does not prove successful Planner execution. Do not add a custom polling or delivery framework to this policy change.

## 5. Safeguards to retain

- Separate Coder execution control from independent Reviewer judgment.
- Keep actual diff inspection, scope control, evidence validation, selective staging, and commit verification before handoff.
- Do not accept Codex's completion text as proof.
- Reuse evidence only while checked inputs, relevant dependencies, configuration, and conditions remain valid.
- Preserve explicit independent and final-state checks and separate passes for material critical invariants.
- Keep exact implementation commits, attributable original results, open findings, and accessible references in compact handoffs.
- Retain older binding decisions when selecting context. Do not equate “latest comments” with the full current contract.
- Keep native serial dependencies, review-done gates, claims, recovery, and history.
- Keep approval, publication, deployment, and customer acceptance distinct.
- Keep Maker source edits separate from an authorized update of installed teams and effective loading in future sessions.
- Do not claim a percentage saving from the SOOS audit. It already shows evidence reuse and delta review; it does not isolate the causal effect of this proposal.

## 6. Evidence and limits

### Sources inspected during the analysis

- Original proposal: `/home/mariko/.hermes/plans/2026-11-08_155912-PLAN_1.0.0_Devteam-Kanten.md`. The adjacent copy preserves its content and original filename.
- Maker source baseline stated above:
  - `templates/roles/planner.SOUL.md.template`: authority, plan binding, clarification, and phase follow-up.
  - `templates/roles/coder.SOUL.md.template`: execution control, exception routing, evidence reuse, and review handoff.
  - `templates/roles/reviewer.SOUL.md.template`: independent assessment, separate passes, native outcomes, and evidence reuse.
  - `references/native-workflow.md` and `references/kanban-block-triage-escalation.md`.
  - `references/tas-authoring-standard.md`.
  - `skills/brownfield-feature-planning/SKILL.md` and `references/kanban-triage-recovery.md` within that skill.
- Native implementation read in `/home/mariko/.hermes/hermes-agent/hermes_cli/kanban_db.py`: `block_task` and `_route_block` around lines 3124–3244, `request_changes` around lines 3411–3457, and `unblock_task`/`reopen_review_task` around lines 3560–3637. These are inspected source semantics, not a newly executed lifecycle test or a permanent version pin.
- Official [Kanban documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban): source-phase restoration, block recurrence, notification modes, and delivery limitations.
- MTB board card `t_a6fa0cf6`, runs 26–33 and associated comments: domain clarification, UUID correction, optional-specimen mapping correction, and eventual independent review.
- Picard session `20261015_073835_60cc3d14`: the sufficient customer answer followed initially by documentation without completed resumption; later safe continuation; MTBNORD-export verification restrictions and recorded deviation. Session references are historical evidence, not current implementation instructions.
- Historical SOOS report: `/home/mariko/projects/devteam-tokenprofiling/soos-2026-11-08/workers/CODER-REVIEWER-AUDIT-DE.md`, especially sections 2, 4, and 5. Its findings were read, not independently re-measured here.
- Current-session customer clarification quoted in section 2. It supersedes the incompatible recommendations in the initial conversational review, not active installed policies by itself.

### Verification boundary

The analysis used document, task-history, session, and targeted native-source reads. It did not execute application tests, live handoff experiments, external uploads, model benchmarks, or team updates. Historical test results were not presented as newly executed checks.

Only the copied proposal and this review response are deliverables of the documentation request. They are repository-only planning artifacts, not delivered Maker package assets. No package-version bump, implementation ticket, template change, deployment, or live policy activation follows from their creation or local commit.
