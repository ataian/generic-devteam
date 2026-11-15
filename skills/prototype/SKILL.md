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

Help the Planner understand the customer's wishes and help the customer resolve uncertainty during the requirements interview.
A prototype is throwaway code that answers one question, not an early product implementation.
Use it when clicking through an example will clarify more than another verbal explanation.
Keep ordinary clarification conversational when a demo adds no value.

## Authority and boundaries

The Planner writes and adjusts these aids directly during grilling, before final plan acceptance when useful.
This narrow clarification workflow replaces product-implementation gates for these aids only.
No Coder, Team-Codex, delegation, Kanban ticket, test suite, independent review, or additional approval round is required or used.
Write no automated tests for the demo.
Opening it and trying its relevant controls is enough; correct obvious runnable defects directly.
Product implementation retains its existing accepted-plan, Codex, testing, and independent-review requirements.

Store every prototype file in the Planner's existing planning `docs/` directory alongside the plan, including when planning and product repositories differ.
Use an obvious name such as `prototype-approval-flow.html` and a visible throwaway label.
Keep prototypes out of the product directory, application routes, build configuration, and production assets.
Use synthetic data, in-memory state, and existing local capabilities.
Do not connect to real mutations, sensitive data, or live services, or install dependencies for the demo.
No commit, throwaway branch, publication, separate report, or cleanup ritual is required.
Existing Git/publication permissions still apply when such actions are explicitly requested.

## Direct clarification loop

1. State the concrete question briefly in the conversation and visibly in the demo.
   Reuse interview context; ask only if the uncertainty itself remains ambiguous.
2. Choose the smallest useful shape and read its branch before building:
   - Logic, state transitions, or data shape: [LOGIC.md](LOGIC.md).
   - Layout, information hierarchy, or interaction presentation: [UI.md](UI.md).
   If the selected file is unavailable, report its path and continue verbal clarification rather than inventing its method.
3. Write the demo yourself in the planning `docs/` directory and open it with the available local preview/browser capability.
   Try the relevant controls; distinguish actual execution from an unverified preview.
   If preview access is unavailable, provide the file and disclose that limitation without building preview infrastructure.
4. Let the customer explore it and adjust it directly in the same conversation as needed.
   Simplify when construction starts becoming a development project; return to verbal examples if the aid no longer saves decision effort.
5. Capture the answer and the customer's decision, or remaining uncertainty, in the ongoing conversation and existing planning documents.
   Resume grilling from that answer, without a separate prototype acceptance ceremony.
   Only the clarified decision enters the product plan; the demo proves neither production correctness nor approval of new scope.

Later product work implements the accepted decision through the normal team workflow.
Treat prototype code as explanatory material, not reviewed production code.
