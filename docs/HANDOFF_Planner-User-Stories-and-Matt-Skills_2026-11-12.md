# Handoff: Planner user stories, Matt skills, TAS and retrospective

## Purpose and current snapshot

Updated 12 November 2026 for the next discussion with Max, especially the remaining Coder, Team-Codex and Reviewer proposals.
Completed package work is not permission to change live teams.

- Maker: `/home/mariko/projects/generic-devteam`, branch `v3`.
- Observed Maker HEAD: `2dc4ebf15ad7cce6f9a44c018c8251e6d0f7c9fc`.
- Committed Maker package: `2.4.0`; current working-tree candidate: `2.5.0`.
- Max committed the earlier story-planning, TAS/Retro, questionnaire and TAS-pin changes. The bounded planning adaptations below remain uncommitted.
- TAS: `/home/mariko/projects/tas`, published `main` and clean local HEAD both `1f7bfeffdc5ddd0eb9a8be59e2153ce6394c4268`, package `1.1.0`.

Re-read Git status, branch and HEAD on resumption. Preserve Max's commits and local changes.
If HEAD moved during work, inspect the recorded baseline through current HEAD plus remaining working changes.
The original handoff's older snapshots remain in Git history; they are not current work instructions.

### Current bounded planning adaptation

Max authorized selected `to-spec` and `to-tickets` methods as extensions of the existing Planner workflow, without installing either original skill.
The `2.5.0` candidate adds glossary/accepted-ADR use in plans and tickets, user-facing problem/solution, concrete test seams and analogous tests, meaningful scope boundaries, and prototype-derived decisions.
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
Further role changes begin as discussion and require their own agreed scope.

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

## Remaining discussion: other roles

Read [Matt-Pocock-Skill-Evaluation.md](Matt-Pocock-Skill-Evaluation.md) as the original full evaluation, not the current implementation ledger.
Its pending recommendations for TAS, Retro and questionnaire are superseded by this handoff.

| Consumer | Candidate | Discussion boundary |
|---|---|---|
| Hermes-Coder / Team-Codex | `diagnosing-bugs` | Reproduction, minimization, falsifiable hypotheses and targeted probes; compare the complete method with current coverage. |
| Team-Codex | `tdd` | Independent expected values and small red/green slices; inspect original constraints before choosing an adaptation. |
| Team-Codex | `prototype` | Only for an explicit design uncertainty, not routine production development. |
| Authorized PR author | `pr` | Optional original helper; preserve repository templates and separate commit/push/publication authority. |
| Independent Reviewer | `code-review` | Requirements versus standards compliance; compare with native `sdlc-review`, not a replacement by default. |
| Independent Reviewer | `tdd` | Test-quality lens, especially assertions capable of disagreeing with the implementation. |
| Hermes-Coder / genuine session transfer | `handoff` | Optional helper, not an extra report per ticket or a narrative for biasing an independent pass. |
| Planner, separately commissioned | `improve-codebase-architecture` | Architecture survey only; not another mandatory planning gate. |

None of these remaining candidates is commissioned or installed by this handoff.
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
- Review transcript: `/home/mariko/.hermes/cache/delegation/live/deleg_c3cd0dd6/task-0.log`. Review and implementation are complete; no worker remains pending.

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

> Read `/home/mariko/projects/generic-devteam/docs/HANDOFF_Planner-User-Stories-and-Matt-Skills_2026-11-12.md` and check the current Git state. Read the current bounded-adaptation evidence before continuing; its independent review is separate from earlier approvals. Continue with me in German on remaining Matt skill proposals for Coder, Team-Codex and Reviewer. Preserve committed earlier stages and current uncommitted work. CI is deferred. Start as discussion, not installation or automatic implementation, and critically compare complete original methods with current role contracts.
