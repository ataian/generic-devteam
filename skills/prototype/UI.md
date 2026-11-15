# UI prototype

Build a self-contained HTML file in the Planner's planning `docs/` to clarify layout, information hierarchy, or interaction presentation.
Use inline HTML/CSS/JavaScript and synthetic data; opening the file must need no app server or installation.
Read the relevant existing page or supplied design to understand surrounding navigation, vocabulary, density, and styling.
Represent that context inside the demo instead of modifying the real application.

## Make the choice visible

1. State the question, assumptions, and throwaway status visibly.
2. For competing layouts, create structurally different variants: information hierarchy, layout, and primary actions, not colour-only changes.
   Build only the variants needed to answer the question; three is a useful starting point, not a quota.
3. Keep variants in the same file with a visibly separate floating switcher and a clear variant name.
   Let previous/next controls update `?variant=` so a chosen view survives reload and can be linked locally.
   Arrow-key switching must leave focused text inputs and editable controls alone.
4. Use local stubs for interactions and expose relevant state after actions or variant switches.
   Preserve meaningful context while keeping each variant free to differ structurally.
5. Open the file and try switching and relevant interactions.
   Let the customer choose a variant, combine useful parts, or reject the alternatives during the same conversation.
6. Record the decision and why in existing planning material, then resume the interview.

No application route, package-runner command, real backend call, or product build change belongs to this aid.
The variants and switcher stay in planning `docs/`; a selected design is implemented later through the normal product workflow.
