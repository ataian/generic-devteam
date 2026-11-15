# Handoff: Planner user stories, Matt skills, TAS and retrospective

## Purpose and current snapshot

Updated 12 November 2026 after implementation, independent review and parent acceptance of proportional two-axis review delegation.
Completed package work is not permission to change live teams.

- Maker: `/home/mariko/projects/generic-devteam`, branch `v3`.
- Diagnosis implementation start HEAD: `a2131704598e3864a4bde8882cc6ea2b69169474`.
- Max committed diagnosis and the TDD discussion record as Maker `2.6.0`; current implementation baseline is `018d899d4c6a4caf7c1e23ee6813e1207d0b8fe4`, branch `v3`.
- Maker `2.7.0` review adaptation is complete, tested and independently approved; its changes remain unstaged and uncommitted.
- The working tree was clean before this handoff update. Preserve that commit and subsequent local work; the review-delegation implementation has its own scope below.
- Max committed the earlier story-planning, TAS/Retro, questionnaire, TAS-pin and bounded to-spec/to-tickets adaptations. Preserve their complete committed content.
- TAS: `/home/mariko/projects/tas`, published `main` and clean local HEAD both `1f7bfeffdc5ddd0eb9a8be59e2153ce6394c4268`, package `1.1.0`.

Re-read Git status, branch and HEAD on resumption. Preserve Max's commits and local changes.
If HEAD moved during work, inspect the recorded baseline through current HEAD plus remaining working changes.
The original handoff's older snapshots remain in Git history; they are not current work instructions.

### Current bounded planning adaptation

Max authorized selected `to-spec` and `to-tickets` methods as extensions of the existing Planner workflow, without installing either original skill.
Committed `2.5.0` adds glossary/accepted-ADR use in plans and tickets, user-facing problem/solution, concrete test seams and analogous tests, meaningful scope boundaries, and prototype-derived decisions.
Conditional Expand–Migrate–Contract planning keeps intermediate states working and verified through native dependency and independent-review gates.
Plan acceptance, story-first cards, Coder discretion, existing roles, and publication permissions remain unchanged.
No integration-branch fallback, closing ticket, new tracker, live-team update, commit, or push is authorized by this change.
Implementation evidence: `/home/mariko/.hermes/cache/scratch/planner-spec-tickets-20261112/implementation.md`.
Independent review: **SPEC: PASS; QUALITY / TAS: PASS**, with no substantive findings. Report: `/home/mariko/.hermes/cache/scratch/planner-spec-tickets-20261112/review.md`.
Parent verification: renderer 66 tests, OK; aggregate 173 tests, OK (skipped=1). The native transition scenarios skipped in the child ran successfully in the parent. The sole parent skip is the negative delegation-fence test, which passed in the child.
Parent evidence: `/home/mariko/.hermes/cache/scratch/planner-spec-tickets-20261112/parent-test-results.json`. The reviewed implementation snapshot was verified unchanged before this status-only update. The review results below cover earlier changes only.

## Authorization and execution boundary

The previous completed assignment covered this handoff, original `to-questionnaire` integration, and the published TAS pin.
Those two implementation points are complete below. Final independent review status is recorded under Verification.
CI was explicitly deferred; do not implement it.

This was package authoring and permitted offline/synthetic regression testing, not a Maker setup run.
No live-team installation, profile/service change, deployment, commit or push was performed by Mariko.
Diagnosis is complete. Max separately commissioned the review-delegation extension below through a subagent with TAS. Other remaining role proposals are discussion-only.

### Proportional diagnosis adaptation — implemented and independently approved

Max approved implementation through one bounded subagent with TAS; an independent read-only reviewer approved the candidate and the parent completed package acceptance.
Owned `skills/diagnosing-bugs/` targets Team-Codex only, with a compact evidence classifier and conditionally required full method.
Direct fixes require concrete symptom/cause evidence, a clear affected flow/correction, and an exact reproducible check.
Unclear or competing causes, intermittent/state-dependent failures, performance isolation, and unresolved/recurring apparent fixes trigger full diagnosis without restarting completed work or adding approval rounds.
The skill also covers unexplained failures/regressions emerging during ordinary implementation.
Coder supplies a literal `$diagnosing-bugs` cue and validates original evidence without automatically repeating diagnosis; Planner/Reviewer contracts and native guards remain unchanged.
Manifest, setup, native bindings, integration/readbacks, and the existing whole-tree updater carry complete method/legal bytes and the call policy together.
Full Matt source and companions at the existing pin were read; NOTICE records proportionality, protected-data, and target-workflow adaptations.
No original HITL helper is bundled: existing communication/protected input suffices for necessary last-resort human reproduction.

Implementation, exact test results, hashes, full snapshots and diff: `/home/mariko/.hermes/cache/scratch/diagnosing-bugs-maker-20261112/implementation.md`.
Independent review: **SPEC: PASS; QUALITY / TAS: PASS**, with no substantive findings. Report: `/home/mariko/.hermes/cache/scratch/diagnosing-bugs-maker-20261112/review.md`.
Parent verification: renderer 66 tests, OK; aggregate 184 tests, OK (skipped=1); package/export checks passed. Native transitions unavailable in the child ran in the parent. The sole parent skip, `No delegation fence in this process`, is the negative guard test exercised in the child.
Parent evidence: `/home/mariko/.hermes/cache/scratch/diagnosing-bugs-maker-20261112/parent-test-results.json`. All 21 scoped files matched the independently reviewed hashes before this status-only handoff update. Other reviewed implementation files remain unchanged.
Package checks and independent instruction review do not prove live discovery, model behavior, or activation; those are outside this authoring assignment.
Max subsequently committed this work in `018d899d4c6a4caf7c1e23ee6813e1207d0b8fe4`. Mariko performed no live installation, profile/runtime/service change, commit, push, or CI work.

### Code-review — implemented, tested and independently approved

Max approved the following design and commissioned its Maker implementation through one subagent.
For the next skill discussion, treat `code-review` as settled and continue with the other candidates.
The requested forward-looking assumption is now backed by completed implementation, tests and independent review. Live-team activation remains outside scope.

- Keep the existing independent Reviewer as the sole owner of coverage and the final verdict. Native `sdlc-review`, dispatcher integration, same-card Coder return, and exact-commit completion remain in force.
- Divide investigation rather than adding two full reviews to an unchanged third full review.
- Small, clearly bounded corrections can be reviewed directly. Changes with multiple substantive behavior cases or technical interactions use two parallel fresh-context helpers when both have meaningful distinct work. Use judgment, not line/file-count thresholds.
- **Spec / requirement fidelity:** check the complete accepted plan, assigned ticket criteria, missing or changed behavior, scope drift, and whether evidence supports claimed fulfillment.
- **Technical quality / standards:** check correctness, applicable repository conventions, surrounding code and callers, failure paths, regressions, architecture, security, and data integrity. This deliberately broadens Matt's Standards axis so technical correctness is not orphaned.
- Bind both helpers to the same exact code state and accepted plan baseline. Give neutral evidence/source access and distinct briefs, not the other helper's findings or the main Reviewer's provisional conclusions.
- The Reviewer validates decisive findings, resolves contradictions, closes concrete coverage gaps, and obtains needed execution evidence. Do not repeat every investigation or test suite automatically. Keep findings evidence-backed and distinguish violations from preferences.
- Preserve the two axes in the assessment; one successful axis cannot cancel a defect on the other. The Reviewer owns the combined disposition. No new tickets, approval rounds, mandatory report files, or review roles.
- Re-review affected areas and prior requested changes while reusing still-valid evidence. Do not restart both axes merely because a correction round or commit changed.
- Preserve configured model/provider, reasoning, access, read-only, resource and operational limits through delegation. Helpers investigate and report; they do not implement or issue Kanban verdicts.
- A technical helper may also satisfy the existing critical-invariant separate pass only when it meets every existing condition: explicit invariant coverage, fresh context, required HIGH reasoning, same allowed model/provider and permissions, and no Coder narrative or prior review conclusions before its own assessment. Otherwise obtain the required targeted pass. Neither unconditional extra passes nor removal of that safeguard is approved.
- Adapt this method into the existing Reviewer equipment. Do not install Matt's original `code-review`, tracker setup, or competing orchestration. Keep upstream `sdlc-review` unchanged and disclose any existing upstream wording tension rather than bypassing native loading.

Matt source: `skills/engineering/code-review/SKILL.md` and `agents/openai.yaml` in the archived pinned checkout below. Its original two parallel Standards/Spec reports, project-overrides-smell baseline and evidence-based judgment are useful references. Its reference-only committed diff, tracker discovery, optional missing spec, fixed report word limit and separate aggregation workflow do not replace our accepted-plan binding, required checks, or native verdict.

#### Execution ledger — final acceptance

- Commissioned scope: package authoring and offline regression checks only; no live-team rollout, installation, runtime/profile changes, staging, commit, push or CI work.
- Worker requirements and execution evidence: `/home/mariko/.hermes/cache/scratch/code-review-maker-20261112/brief.md` and `implementation.md` respectively.
- Recorded initial baseline: `/home/mariko/.hermes/cache/scratch/code-review-maker-20261112/parent-start-state.json`.
- Implementation worker dispatched: `deleg_09fd1ac3`, child `sa-0-bec737ab`. Transcript: `/home/mariko/.hermes/cache/delegation/live/deleg_09fd1ac3/task-0.log`.
- Implementation completed as Maker `2.7.0`: twelve scoped files, including one new test file. Method lives in the existing Reviewer SOUL; no separate review skill or runtime equipment was added.
- Independent read-only review: **SPEC: PASS; QUALITY / TAS: PASS**, with no substantive findings. Report: `/home/mariko/.hermes/cache/scratch/code-review-maker-20261112/review.md`; exact reviewed identities: `reviewed-hashes.json` in the same directory.
- Parent verification: renderer 66 tests, OK; aggregate 196 tests, OK (skipped=1); package/export checks passed. The sixteen native cases skipped under the worker's delegation guard ran successfully in the parent. The sole parent skip, `No delegation fence in this process`, is the negative guard test that passed in the worker. Guards were preserved.
- Independent reviewer additionally ran ten focused contract tests and two updater regressions successfully; it reused the state-bound parent suite evidence rather than repeating full suites.
- Parent evidence: `/home/mariko/.hermes/cache/scratch/code-review-maker-20261112/parent-test-results.json`. Before this status update, all 74 reviewed repository files matched their recorded hashes, including all twelve implementation files. Only the parent-owned handoff changes after that comparison; implementation remains unchanged.
- Package acceptance is complete. No implementation or review gate remains pending. Leave current work unstaged and uncommitted; no live installation, profile/runtime/service change, commit or push was performed.
- These checks cover authored contracts, rendering, package delivery and synthetic updater behavior. Effective helper settings, real delegated review behavior and live activation were not tested and are not implied by acceptance.
- Better quality or token savings from this review split are hypotheses, not measured outcomes.

### Handoff skill — not adopted

Max chose not to add Matt's `handoff` to the devteam equipment.
Existing plan/ticket/Codex/review/resumption contracts already carry normal transitions. Another generic summary would mostly duplicate those records.
A manually requested session/topic handoff remains possible; it does not require installing the skill or adding a mandatory report per ticket.
Do not reopen adoption without a new request or a concrete missing transition.

## Completed decisions and implementations

### Domain modelling and user-story planning

Implemented and independently approved in the earlier package changes; already committed by Max.

- Planner receives original `grill-me`, `grilling` and complete `domain-modeling` at the existing Matt pin.
- Domain modelling is conditional within the requirements interview. Glossaries define vocabulary, not requirements. Qualifying ADRs remain proposed until accepted.
- Coder and Reviewer consume accepted definitions; Reviewer remains read-only. Native dispatch and existing plan approval remain intact.
- Decompose by actor, behaviour, benefit and independently verifiable outcomes before mapping to phases/tickets. Necessary foundations trace to enabled stories. No one-story/one-phase/one-ticket rule.
- Ticket titles express concise actor–behaviour–benefit stories, not technical-layer tasks with actor prefixes.
- Descriptions contain goal/context, acceptance criteria, technical implementation, verification, dependencies and exact plan/phase/commit binding.
- Cards stand alone without duplicating the complete plan. Keep concise bullets, binding constraints distinct from suggestions, and Coder implementation discretion.
- Existing Caveman applies to persisted role text with clarity and safety preserved; no arbitrary length cap or successful-check catalogue.
- Selected design questions cover caller contracts, actual complexity encapsulation, complexity returning when an abstraction is removed, and variability justified by present needs.
- The full `to-tickets` and `codebase-design` workflows were not installed. Their unrelated tracker, orchestration and test restrictions were not imported.

Earlier story implementation/review evidence: `/home/mariko/.hermes/cache/scratch/planner-stories-20261112T025628/` and `/home/mariko/.hermes/cache/scratch/planner-stories-review/REVIEW.md`.
These identify the earlier stage, not the final questionnaire tests below.

### TAS extraction and writing-for-agents adaptation

Implemented, independently reviewed and published by Max.

- Sole normative source: `/home/mariko/projects/tas`; Maker's own TAS copy was removed.
- TAS `1.1.0` incorporates Matt's pointer/trigger, information-hierarchy, leading-word, completion and pruning method, with a skill-mechanics reference and complete provenance/legal files.
- Maker consumes it through `references/upstream-sources.md#tas`; no TAS installation into team roles or additional runtime role was introduced.
- **DONE: published pin adopted.** Maker `upstream_components.tas.source_revision` is `1f7bfeffdc5ddd0eb9a8be59e2153ce6394c4268`.
- Parent independently compared GitHub `refs/heads/main`, local clean TAS HEAD and the actual committed package. The former TAS publication/pin blocker is closed.
- Maker README and source recipe now describe the published pin, not the initial TAS package or pending publication.

`docs/HANDOFF_TAS-Upstream_2026-11-12.md` records the intermediate pre-publication stage only; its old pin/open release dependency is historical.

### Owned process retrospective

Implemented and independently approved at both skill and Maker-integration level; committed by Max.

- Own `skills/retro/` package, Planner-only; Matt's method is adapted with NOTICE and retained MIT text, not installed as an upstream runtime dependency.
- Explicit user request only: `/retro` or natural language, with current conversation as the default scope.
- Diagnose process and working environment, not product acceptance or another code review. Retrieve relevant original/worker records and disclose evidence gaps.
- Include navigation, automated checks versus judgment, instruction/tool friction and token economy across loading, context, output, duplicate analysis, retries and documentation.
- Return a few source-backed priorities; separate observation from causal hypothesis. No-change is valid. Implementation needs its own authorization.
- Brownfield's former acceptance-oriented retrospective now routes to the owned skill.
- Setup/update recipes require collision checks, complete-tree delivery and native readbacks without running a retrospective.
- Actual target `/retro` availability and live-agent behavior were not qualified by package tests.

### Original to-questionnaire upstream helper

**DONE: integrated into Maker `2.4.0` for the Planner.** This is package integration, not installation into an existing live Planner.

- Extended existing `upstream_components.grill-me.subpaths` with `skills/productivity/to-questionnaire`; kept the existing Matt revision `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` and Planner-only targets.
- Original tree contains `SKILL.md` and `agents/openai.yaml`; deliver both unchanged and preserve the original root MIT license.
- Setup, sources, integration recipe, required upstream companion updates, verification, README and NOTICE cover this fourth Matt skill.
- Brownfield has an explicit request-triggered `skill_view(name="to-questionnaire")` pointer. It is optional in planning, not another mandatory interview.
- Original method: clarify recipient and needed answers, then write `to-questionnaire-<slug>.md` for one recipient holding missing knowledge. Partial answers are allowed.
- Drafting authorizes neither sending nor accepting new product scope. Keep project document conventions and existing communication/plan gates.
- Preserve upstream metadata; do not claim `disable-model-invocation` enforces an unverified Hermes invocation restriction.
- Existing file updater still does not install upstream assets. Its dependency gate and the authorized prose companion path cover the added subtree; regression tests verify this boundary.

### Coder/Reviewer allocation audit and deferred CI

The separate read-only audit found no concrete rule block justifying a blanket transfer from Coder to Reviewer. No corresponding role-template changes were made.
Keep implementation-critical knowledge with Coder and independent systematic assessment with Reviewer.
Route future concrete retro findings to an existing deterministic check or targeted Reviewer guidance, rather than adding generic rules everywhere.

Running the existing Maker suite in CI was only an optional follow-up, not a required audit fix.
Max explicitly chose to leave CI aside for now. No workflow was added; do not reopen it automatically.

## Planner-only prototype — approved scope

Max approved this clarification tool during the follow-up discussion and commissioned its Maker integration.
This decision supersedes the earlier Team-Codex prototype recommendation in the original evaluation.

- The Planner writes small throwaway demos itself during grilling to understand wishes and resolve the customer's uncertainty.
- Store all demo files in the Planner's planning `docs/` beside the plan, including with separate planning/product repositories. Keep them out of the product directory.
- No Coder/Team-Codex use, delegation, tickets, automated tests, independent review, extra approval rounds, required commit/branch, or separate report for these aids.
- Directly open/use and adjust the demo in the conversation; simplify or return to verbal clarification when building no longer saves decision effort.
- Use synthetic in-memory examples without live services, real mutations, sensitive data, or dependency installation.
- Capture the learned decision in existing planning material. Normal plan acceptance, implementation testing and independent review apply to later product work, not the throwaway demo.
- Owned `skills/prototype/` adapts Matt's complete logic/UI method with original MIT text and explicit provenance. Planner-only assignment; no original upstream runtime installation.

Implementation baseline: `df9e3d756e121d4b8bf8c492b0affb317bd39b7e`, clean `v3` at start.
Maker `2.8.0` implementation and package acceptance are complete, unstaged and uncommitted. Parent verification passed: prototype 7 tests, Brownfield 19 tests, renderer 66 tests; aggregate 205 tests, `OK (skipped=1)`.
The sole aggregate skip is the negative delegation-guard case: `No delegation fence in this process`.
Manifest inventory/version, exported links/anchors, changed Python syntax, original MIT bytes, unchanged upstream pins and unchanged Coder/Reviewer templates passed; `git diff --check` passed.
Independent review: **SPEC / QUALITY-TAS: PASS**, no substantive findings. Report: `/home/mariko/.hermes/cache/scratch/planner-prototype-20261112/review.md`.
Parent verified the actual report and unchanged reviewed implementation hashes; only this parent-owned status record changed afterward. These are Maker development checks, not a demo workflow requirement.
Evidence area: `/home/mariko/.hermes/cache/scratch/planner-prototype-20261112/`.
No live-team rollout, profile/runtime change, commit, push, or CI work is commissioned.

## Deferred candidates

Read [Matt-Pocock-Skill-Evaluation.md](Matt-Pocock-Skill-Evaluation.md) as the original full evaluation, not the current implementation ledger.
Its pending recommendations for TAS, Retro and questionnaire are superseded by this handoff.

| Consumer | Candidate | Discussion boundary |
|---|---|---|
| Team-Codex | `tdd` | Deferred by Max; standalone discussion record: [THE-TDD-IDEA](THE-TDD-IDEA.md). No integration commissioned. |
| Authorized PR author | `pr` | Deferred by Max in the follow-up discussion; revisit only on request. Preserve repository templates and separate commit/push/publication authority. |
| Independent Reviewer | `tdd` | Deferred with the TDD topic; no separate test-quality skill assignment commissioned. |
| Planner, separately commissioned | `improve-codebase-architecture` | Deferred by Max in the follow-up discussion; revisit only on request. Architecture survey only, not another mandatory planning gate. |

None of these deferred candidates is commissioned or installed. Prototype has its separate approved scope above. Diagnosis is implemented, tested, independently approved and committed. Review delegation's earlier completion record remains above. TDD is deferred; `handoff` is not adopted.
Matt's methods are a strong preferred baseline. Read the complete original and companions before judging; justify departures with concrete runtime differences, authority/safety conflicts or observed failure.
Assess Max's ideas critically rather than agreeing automatically. Distinguish static consumer checks from measured model behavior or token savings.

## Verification and evidence

Earlier questionnaire/TAS-pin package checks, not evidence for the current bounded adaptation or live-team qualification:

- Maker focused: `65` tests, `OK`.
- Maker aggregate: `169` tests, `OK (skipped=1)`.
- Single skip: negative delegated-guard case reports `No delegation fence in this process`; native synthetic transition checks ran in the parent. No guard was disabled or bypassed.
- TAS: `11` tests, `OK`.
- Package verifier: complete inventories, versions, Python/JSON/YAML checks, relative links/anchors, selected original Matt bytes, published TAS pin and unchanged protected assets.
- Role SOUL templates, other owned skills and the TAS checkout remain unchanged by this final delta.
- Final independent review of questionnaire/pin/handoff: `READY`; no critical, important or substantive minor findings. The parent verified all reviewed file hashes before replacing this status line.
- Review transcript: `/home/mariko/.hermes/cache/delegation/live/deleg_c3cd0dd6/task-0.log`. Review and implementation of that earlier questionnaire/pin stage are complete; this is not the status of the newly commissioned review-delegation worker.

Original current evidence under `/home/mariko/.hermes/cache/scratch/`:

- `questionnaire-tas-maker-focused.txt`
- `questionnaire-tas-maker-aggregate.txt`
- `questionnaire-tas-tests.txt`
- `questionnaire-tas-package-check.json`
- `verify_questionnaire_tas_published.py`

For new Maker edits, read current root `SKILL.md`, `AGENTS.md`, `HERMES.md`, `README.md` and the TAS source branch in `references/upstream-sources.md#tas`.
Do not reload the removed Maker-local TAS path.
Relevant consumers: role templates, Brownfield entry/references, `references/integrations.md`, `references/update.md` and existing regression suites.
Read-only Matt source checkout: `/home/mariko/archive/mattpocock-evaluation-20261112/skills` at the pinned revision above.
Use existing development checks; keep package changes, saved target files, effective loading and live behavior distinct.

## New-session starter

> Read `/home/mariko/projects/generic-devteam/docs/HANDOFF_Planner-User-Stories-and-Matt-Skills_2026-11-12.md` and check current Git state. Preserve committed earlier work and current local changes. Planner-only prototype integration is complete, package-tested and independently approved as Maker `2.8.0`, unstaged and uncommitted; do not repeat its build or review. `pr`, `improve-codebase-architecture`, TDD and CI are deferred; revisit only on request. `handoff` was not adopted. Continue in German. Package authoring does not authorize live-team updates, installation, commit or push.
