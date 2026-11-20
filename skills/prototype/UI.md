# UI prototype

- Output: self-contained HTML in the Planner's planning `docs/` for layout, information hierarchy or interaction presentation. Use inline HTML/CSS/JavaScript and synthetic data. No app server or installation.
- Input: relevant page or supplied design. Read for surrounding navigation, vocabulary, density and styling. Represent that context in the demo and keep the real application untouched.

## Make the choice visible

1. State the question, assumptions, and throwaway status visibly.
2. For competing layouts, vary information hierarchy, layout and primary actions. Colour alone is insufficient. Build only variants needed to answer the question. Three is a useful starting point, not a quota.
3. Keep variants in one file with clear names and a visibly separate floating switcher. Previous/next controls update `?variant=` for reload and local linking. Arrow-key switching leaves focused text inputs and editable controls alone.
4. Use local stubs for interactions. Show relevant state after actions or switches. Keep meaningful context and allow structural differences.
5. Open the file and try switching and relevant interactions. In the same conversation, let the customer choose, combine useful parts or reject the alternatives.
6. Record the decision and why in existing planning material, then resume the interview.

Keep variants and switcher in planning `docs/`. No application route, package-runner command, real backend call or product build change. Implement the selected design later through the normal product workflow.
