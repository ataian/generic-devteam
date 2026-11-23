# Logic prototype

- Output: single self-contained HTML file for business logic, state transitions or data shape. Keep the entire aid in the Planner's planning `docs/`.
- Runtime: plain inline HTML/CSS/JavaScript. The customer opens and drives it directly without developer tools, framework, bundler, server or installation.
- Data: synthetic in-memory examples, including when discussing persistence or an API contract.

## Build the question, not the product

1. Show the question and starting assumptions at the top.
2. Separate state and transitions from DOM rendering in one small script module. Choose a reducer, explicit state machine, pure functions or small state-owning module to fit the question. Keep button handlers thin over that logic.
3. Use the customer's domain language for action and state labels. Leave implementation names out. After each action, show all relevant state in readable fields with important changes visible.
4. Add free-play buttons for relevant actions and a reset to a known initial state. Show attempted illegal actions and their effect when relevant to the question.
5. Give short guided scenarios for awkward cases. Use tabs if several help. Reset each walkthrough to its stated starting state. Each step performs the actual demo action.
6. Keep presentation restrained and readable. Omit polish, abstractions, speculative features and error handling unrelated to running the demo.
7. Open the file and try relevant controls. At handoff, explain what it models and what remains unproven about the real application. Continue the direct clarification loop in [SKILL.md](SKILL.md). Do not lift demo logic into product code automatically.
