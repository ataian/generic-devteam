# Logic prototype

Build a single self-contained HTML file for business logic, state transitions, or data shape.
Use plain inline HTML/CSS/JavaScript: no framework, bundler, server, or installation.
The customer can open the file directly and drive it without developer tools.

## Build the question, not the product

1. Show the question and starting assumptions at the top.
2. Isolate the relevant state and transitions from DOM rendering in one small script module.
   Choose a reducer, explicit state machine, pure functions, or a small state-owning module according to the question.
   Keep button handlers as a thin shell over that logic.
3. Label actions and state in the customer's domain language, not implementation names.
   Render the full relevant state as readable fields after each action, with important changes visible.
4. Add free-play buttons for relevant actions and a reset to a known initial state.
   Make attempted illegal actions and their effect visible when that is part of the question.
5. Provide short guided scenarios for the awkward cases that need clarification.
   Use tabs when several scenarios help; reset each walkthrough to its stated starting state.
   Each step performs the actual demo action, rather than displaying a canned outcome.
6. Keep presentation restrained and readable; omit polish, abstractions, speculative features, and error handling unrelated to running the demo.
7. Open the file, try its relevant controls, and hand it to the customer for the direct clarification loop in [SKILL.md](SKILL.md).

Use synthetic in-memory examples even when discussing persistence or an API contract.
Explain what the demo models and what it does not establish about the real application.
Keep the entire aid in the Planner's planning `docs/`; no logic is automatically lifted into product code.
