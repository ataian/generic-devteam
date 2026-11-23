---
name: prototype
description: Use when a planning uncertainty needs an interactive demo.
version: 0.1.0
author: Max, Mariko (Hermes Agent); adapted from Matt Pocock
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [planning, clarification, prototype]
    related_skills: []
---

# Planning prototype

Use a throwaway demo during the requirements interview when interaction better clarifies one customer wish or uncertainty. Otherwise clarify in conversation.

## Authority and boundaries

- Owner: the Planner writes and adjusts the demo directly during grilling, before final plan acceptance when useful.
- Demo only: no Coder, Team-Codex, delegation, Kanban ticket, automated tests, test suite, independent review or extra approval round. Open it and try relevant controls. Fix obvious runnable defects directly.
- Product work retains accepted-plan, Codex, testing and independent-review requirements.
- Files: the Planner's existing planning `docs/` beside the plan, even across repositories. Use a clear name such as `prototype-approval-flow.html` and a visible throwaway label. Exclude the product directory, application routes, build configuration and production assets.
- Inputs: synthetic data, in-memory state and existing local capabilities only. No real mutations, sensitive data, live services or dependency installations.
- No required commit, throwaway branch, publication, separate report or cleanup ritual. Explicit Git or publication requests remain subject to existing permissions.

## Direct clarification loop

1. State the concrete question briefly in conversation and visibly in the demo. Reuse interview context. Ask only if the uncertainty itself remains ambiguous.
2. Choose the smallest useful shape and read its branch before building:
   - Logic, state transitions, or data shape: [LOGIC.md](LOGIC.md).
   - Layout, information hierarchy, or interaction presentation: [UI.md](UI.md).
   If the selected file is unavailable, report its path and continue verbal clarification. Do not invent the method.
3. Write the demo directly in planning `docs/`. Open it with available local preview or browser tools and try the relevant controls. Distinguish actual execution from an unverified preview. If preview access is unavailable, provide the file and report the limit without building preview infrastructure.
4. Let the customer explore the demo. Adjust it directly as needed in the same conversation. Simplify if construction grows into a development project. Return to verbal examples if the demo no longer saves decision effort.
5. Record the answer and customer decision, or remaining uncertainty, in the conversation and existing planning documents. Resume grilling from that result without separate prototype acceptance. Carry only the clarified decision into the product plan. The demo provides no evidence of production correctness or approval of new scope.

Treat demo code as explanatory material. Implement the accepted decision later through the normal team workflow.
