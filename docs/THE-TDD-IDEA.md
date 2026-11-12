# THE-TDD-IDEA

## Status and authority

**Deferred for a separate discussion. No TDD integration commissioned.**

This handoff isolates the TDD discussion from the wider Matt Pocock skill evaluation.
Max questioned whether integration is worthwhile now and requested this record instead of implementation.
The next session starts with that decision, not an installation or an assumed implementation plan.

Latest request:

> hmm irgendwie zweifel ich noch ob das zu diesem zeitpunkt eine gute idee ist es einzubauen. mach bitte mal ein handoff "THE-TDD-IDEA" mit allein infos und bisherigen entscheidungen, vorschlägen usw. damit wir dieses thema allein später mal wieder aufgreiffen können.

Recorded from the discussion on 12 November 2026.
No TDD skill, role rule, manifest component, runtime binding, or live-team update was implemented for this proposal.
This document is repository-only planning material, not a delivered Maker component or a package-version change.

## 1. Question being parked

Would an explicitly selected TDD method improve our agent team's work enough to justify another skill and integration rules?
If yes, can Matt's original remain unchanged, or does the team need an owned adaptation?
Deferral is not rejection. Neither installation nor eventual adoption is promised.

## 2. Max's position and discussion conclusions

### Explicit user position

- Max finds TDD useful occasionally and often excessive as a human coder.
- He does not want a universal test-first requirement for every development change.
- He reads Matt's skill as a consciously selected method: "nutze tdd hier", not "immer".
- He challenged the suggestion that the alternative to one-test-at-a-time was writing all tests first.
- He is now unsure whether introducing the skill is a good idea at this stage.

### Shared understanding reached

- Separate choosing TDD from following its rules after selection.
- If TDD is selected, use a short feedback loop: failing behavior test, minimal implementation, green verification, then the next slice.
- This is a coding loop, not one ticket, commit, agent run, or customer approval per test.
- Neither side advocated writing the entire test suite before implementing everything.
- A tightly related group of cases can sometimes be practical; that flexibility was discussed, not accepted as a change to Matt's exact one-test rule.
- Test quality matters with or without test-first development.
- A regression test written before a bugfix does not establish a universal TDD mandate.

### Not decided

- Whether to add any TDD skill.
- Original upstream plus integration rules versus an owned adaptation.
- Exact activation, planning, test-boundary, refactoring, dependency, and review rules.
- Any rollout, pilot, new test-quality mandate, or Reviewer skill assignment.

## 3. What Matt's inspected original actually says

Inspected source checkout:
`/home/mariko/archive/mattpocock-evaluation-20261112/skills`

Inspected clean source revision:
`4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`

Paths below are relative to that checkout.

### Entry and activation

`skills/engineering/tdd/SKILL.md:3` describes activation when the user wants test-first features or bugfixes, mentions red-green-refactor, **or wants integration tests**.
It does not require TDD for every implementation.
The integration-test trigger is broader than Max's proposed explicit TDD choice.
A skill description is selection guidance, not verified runtime enforcement of opt-in behavior.

### Method

- Read existing `GLOSSARY.md` and respect relevant ADRs.
- Test observable behavior through public interfaces, rather than implementation structure.
- Agree test seams with the user before writing tests; no tests at unconfirmed seams.
- Explain what each proposed seam catches and misses.
- Use independently grounded expectations: specification, worked example, or known-good value.
- Avoid assertions that reproduce the implementation's calculation or derive their own expected answer tautologically.
- Avoid horizontal slicing: all tests first, then all implementation.
- Write a failing test before implementation; add only enough code to pass it.
- Use one seam, one test, and one minimal implementation per cycle.
- Refactoring is explicitly outside this red-green loop and belongs to the review stage.

**Important correction:** despite the familiar red-green-refactor activation wording, this inspected version does not put refactoring inside each cycle.

### Companions and references

- `skills/engineering/tdd/tests.md`: behavior-facing examples; public API; one logical assertion; warnings about private methods, internal mocks, call-count/order assertions, and direct database verification instead of the interface.
- `skills/engineering/tdd/mocking.md`: mock system boundaries; prefer a test database where suitable; avoid mocking owned internal collaborators; use dependency injection and specific operation interfaces.
- `skills/engineering/tdd/agents/openai.yaml`: accompanying upstream metadata; inspect before any eventual complete-tree acquisition.
- `skills/engineering/codebase-design/SKILL.md`: consulted when interface shape is uncertain, expressly as vocabulary, not an extra design session.
- `skills/engineering/code-review/SKILL.md`: referenced for the review stage; it has its own two-axis parallel-subagent review process.

The design reference prescribes architecture terms and discourages substitutes such as "service" or "API".
That vocabulary must not silently replace an accepted project glossary.
Its `DEEPENING.md` permits internal seams and directs deletion of superseded shallow-module unit tests.
Those companion instructions are not blanket permission to remove coverage.
The TDD reference does **not** automatically require a deepening or Design It Twice session.

## 4. Agent-specific reasoning discussed — recommendations, not measurements

Mariko's assessment:

- Short loops can expose mistaken assumptions before an agent builds a large implementation on them.
- A test can still encode the agent's own wrong assumption. Test-first alone does not make the expectation independent or correct.
- Clear calculations, validations, state rules, stable interface contracts, and reproducible bugs are plausible uses for test-first work.
- Unsettled interfaces or UI interactions may benefit from bounded exploration before fixing the test shape.
- Existing regression coverage may be more important than new TDD ceremony during a refactor.
- Text or declarative changes do not automatically need invented unit tests.
- Higher risk requires stronger evidence, not automatically more TDD cycles or customer approvals.

These are proposed selection heuristics, not an automatic activation matrix accepted by Max.
No comparative agent run, defect-rate measurement, token saving, or cost benefit was demonstrated.

## 5. Comparison with current Maker contracts

Inspected Maker checkout: `/home/mariko/projects/generic-devteam`.
At handoff preparation it was on branch `v3`, based on commit
`a2131704598e3864a4bde8882cc6ea2b69169474`, with unrelated diagnosis work already uncommitted.
Re-read the actual state on resumption; this snapshot is not a clean-release claim.

| Issue | Original guidance | Existing contract and proposed integration |
|---|---|---|
| Activation | Integration-test requests can select TDD. | Proposal: only an explicit user TDD choice activates it. Merely requesting integration tests does not. |
| Seam confirmation | Confirm seams with the user before tests. | Planner already identifies verification interfaces in the accepted plan. Proposal: honor that acceptance without another approval round; ordinary technical details remain with the team. |
| Test scope | Public interfaces only; never internals. | Planner explicitly retains necessary lower-level and risk-based checks. Proposal: preserve those additional checks instead of treating public-interface TDD as the entire verification policy. |
| Review/refactoring | Refactoring belongs to review; refers to Matt's review skill. | Our Reviewer is read-only and uses `sdlc-review`. Proposal: implementation corrections stay with Coder/Team-Codex; independent review remains native. No automatic second review workflow. |
| Design vocabulary | Consult `codebase-design` when interface shape is unclear. | Accepted glossary/ADRs remain authoritative. Resolve the reference's vocabulary mandates and companion reach before adding it as a dependency. |

Concrete Maker sources:

- `templates/roles/planner.SOUL.md.template:50–51`: prefer behavior-facing test seams while retaining necessary lower-level and risk-based checks.
- `templates/roles/coder.SOUL.md.template:8–10`: in-scope technical discretion and application of already accepted decisions without asking again.
- `templates/roles/coder.SOUL.md.template:34`: native independent review handoff.
- `templates/roles/coder.SOUL.md.template:80`: no unrelated refactoring or weakened tests.
- `templates/roles/reviewer.SOUL.md.template:6`: Reviewer does not edit or repair project code.
- `templates/roles/reviewer.SOUL.md.template:13`: existing `sdlc-review` method.

These identify integration questions. They do not prove that TDD cannot coexist with the team.
An explicit accepted plan could already satisfy some upstream requirements without changing their meaning.
Avoid inflating a reference into a mandatory imported workflow.

## 6. Options and the last recommendation

### A. Keep the current approach

Add no skill. Continue appropriate tests, regression evidence, small implementation steps, and independent review.
Revisit TDD when a concrete task makes the additional method useful.
This remains a valid outcome, not an incomplete integration.

### B. Preserve upstream files; add narrow team integration rules

Mariko's last recommendation, **not approved by Max**:

- Keep complete original files at a selected fixed upstream revision.
- Put explicit activation and precedence rules in the Maker integration, separate from original files.
- Carry a selected TDD method from the accepted plan/ticket through Coder to Team-Codex.
- Preserve Matt's failing-test/minimal-implementation/green loop.
- Resolve the activation, accepted seams, supplemental checks, refactoring/review, and dependency issues above.

This preserves source bytes, not unchanged upstream behavior.
The separate rules must actually reach Codex, including resumed work; a document link alone is not proof.
If overrides routinely negate the original method, an "unchanged upstream" label becomes misleading.

### C. Own a small explicit adaptation

Adapt only concrete conflicts and retain upstream provenance, licensing, companions, and a clear difference record.
Prefer this classification if changed mandates are essential, rather than concealing them behind contradictory instructions.
Costs include another maintained method and responsibility for keeping its relation to upstream understandable.

No option was selected. Max's latest instruction parks the choice.

## 7. Corrections and cautions for the next discussion

- Mariko initially mixed criticism of mandatory TDD with rules that apply only after selecting TDD. That was corrected.
- Do not present the original as requiring test-first development for every task.
- Do not present Max as preferring bulk test authoring; neither side preferred it.
- Distinguish a public callable module interface from the application's outermost UI/API. Small public module functions can be legitimate behavior-facing seams.
- Do not invent a required customer decision for each test or cycle; the original confirms seams, not every assertion individually.
- Do not silently soften Matt's one-test loop while calling the result unchanged behavior.
- Do not import automatic test deletion, architecture redesign, extra reviewers, tracker setup, or new approval ceremonies through companion references.
- No proposed test-quality lens or selection heuristic became a new team obligation merely through this conversation.

## 8. Related work and source trail

- [Wider Matt evaluation](Matt-Pocock-Skill-Evaluation.md): original comparative assessment, not the final decision ledger.
- [Wider handoff](HANDOFF_Planner-User-Stories-and-Matt-Skills_2026-11-12.md): Planner adaptations and separately commissioned diagnosis work.
- The proportional `diagnosing-bugs` adaptation has its own authorization and review work. This TDD deferral neither approves, cancels, nor completes it.
- Reading or adopting diagnosis is not implicit approval to add TDD.
- TAS source used for this handoff: `/home/mariko/projects/tas`, clean HEAD `1f7bfeffdc5ddd0eb9a8be59e2153ce6394c4268`.

## 9. Resume prompt

> Read `/home/mariko/projects/generic-devteam/docs/THE-TDD-IDEA.md`. Discuss only the deferred TDD idea with me in German. Start by assessing whether another skill is worthwhile for our current team, using a concrete use case if helpful. Do not assume adoption, reopen unrelated Maker work, or install/change anything. Keep confirmed user choices distinct from Mariko's proposals. If we choose to proceed, re-read the complete original and relevant current team contracts before selecting upstream integration versus adaptation. Package work and live-team rollout require separate authorization.
