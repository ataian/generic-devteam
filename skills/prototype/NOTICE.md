# Provenance and adaptation

Owned Planner-only adaptation of Matt Pocock's `prototype`, authored for Max with Hermes Agent.

Source: https://github.com/mattpocock/skills

Revision: `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.

Complete source read:
- `skills/engineering/prototype/SKILL.md`
- `skills/engineering/prototype/LOGIC.md`
- `skills/engineering/prototype/UI.md`
- `skills/engineering/prototype/agents/openai.yaml`
- Root `LICENSE`, retained completely in [LICENSE](LICENSE).

Retained: one explicit question; throwaway scope; logic/UI branches; self-contained clickable logic demo; separated logic/rendering; domain-language state; free play and guided awkward cases; structurally different UI variants with a switcher; no automated tests, speculative abstractions, or production hardening; capture the learned answer.

Adaptations selected by Max:
- Planner writes directly during grilling to understand wishes and resolve uncertainty. No Coder/Team-Codex use or delegation.
- No tickets, test/review pipeline, extra approval rounds, required commits, throwaway branches, or standalone reports for these aids.
- Use the Planner's planning `docs/` beside the plan, not the product directory. UI variants therefore reproduce context in standalone HTML instead of changing existing application routes or task-runner configuration.
- Use synthetic in-memory examples, without live services, sensitive data, real mutations, or dependency installation.
- Keep the artifact proportional to the question; UI variant count is not a quota. Simplify or return to conversation when building stops helping.
- Capture the decision in existing planning material; do not lift prototype logic or a winning UI directly into production. Product work retains normal accepted-plan, testing, and independent-review gates.
- Runnable interaction checks are direct use of the aid, not a test suite or acceptance cycle.

Original OpenAI display metadata was inspected but is not bundled or required by Hermes.
This owned skill uses its own portable metadata and has no automatic upstream synchronization.
The MIT license retains the original copyright and permission notice. New adaptation text also uses MIT.
