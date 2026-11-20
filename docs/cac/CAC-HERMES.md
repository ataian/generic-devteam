# CAC-HERMES — Compact Artifact Contract

Purpose: minimize **total** token cost per independently accepted ticket without loss of meaning, authority, evidence, or quality.

## 1. Priority and scope

- CAC governs **information selection, placement, structure, and wording**. It does not grant tool permissions or change the native workflow.
- Existing accepted requirements, project rules, role authority, approval gates, native APIs, and safety constraints take precedence over stylistic compression. Report unresolved conflicts; do not guess.
- Apply to agent-facing SOULs, owned skills/references, planning artifacts, internal Markdown, Kanban tickets/comments, handoffs, findings, and Hindsight entries.
- Human-facing Mattermost decisions/reports remain understandable; include consequences, options, and required action. Do not impose machine shorthand on the customer.
- Keep exact identifiers, source quotations, commands, paths, errors, version/commit pins, legal text, and required machine-readable keys unchanged.
- Do not compress code, API/schema contracts, legal/provenance files, or test evidence where doing so changes meaning.
- No universal character, line, or token limit. **Minimum complete** is the criterion.

## 2. Writing rules

1. Use plain technical English. Prefer direct imperatives, short clauses, compact Markdown bullets, and established technical terms.
2. Specify **actor + trigger/condition + action + outcome/check**. Keep `MUST`, `MUST NOT`, `ONLY IF`, `BEFORE`, `AFTER`, and exceptions explicit.
3. Keep one authoritative location per rule or fact; consolidate duplicates. Do not reference a source that the recipient cannot access unambiguously.
4. Remove filler, rationale without decision value, routine narration, repeated plans, praise, generic disclaimers, and successful-log inventories.
5. Preserve reasons needed to understand accepted trade-offs, security boundaries, risky operations, non-obvious exceptions, or rejected alternatives.
6. Separate `fact`, `assumption`, `proposal`, `accepted decision`, `implementation`, `test result`, and `independent verdict`.
7. Use existing vocabulary; do not invent cryptic abbreviations, new status enums, or protocol parsers. `key: value` is a readable convention, not a new native API.
8. Summarize successes; report failures, skipped checks, uncertainty, risk, blocked actions, and actionable evidence precisely.
9. Preserve source pointers plus the minimum self-contained facts needed for the receiver's next action. A ticket must remain actionable without re-reading the entire plan.
10. Prefer **removing unnecessary information** over shortening words. If compression creates extra queries, repeat context, or ambiguity, expand it.

## 3. Rule placement and loading

| Location | Contains |
|---|---|
| SOUL | Role authority, durable decisions, safety, gates, dispatch/exception routing, compact output policy |
| Owned skill entry | Distinct invocation triggers; essential ordered steps and completion criteria |
| Conditional skill reference | Specialized recipes, edge cases, examples, recovery detail |
| Accepted plan/ADRs | Scope, behavior, decisions, invariants, acceptance, dependencies |
| Kanban card | Independently actionable task plus exact accepted-plan/branch binding |
| Hindsight | Verified durable knowledge with provenance; not task diary or alternate authority |
| Private evidence | Original logs, test outputs, source/target mappings; link, do not paste successes |

- Put mandatory rules in context that every relevant consumer **actually loads**. A passive hyperlink or a Maker-only reference is insufficient.
- Keep third-party skills and native Hermes integration untouched; adapt only owned instructions and delivery policies.
- Use progressive disclosure for conditional procedures, not to hide required gates.

## 5. Hermes Kanban message protocol

**Use existing native tool fields, statuses and transitions.** These templates specify content only. Avoid new fields/APIs/storage, and do not change existing required native metadata.

### Planner → Coder: actionable card

the actionable card (herbes kanban ticket), shall have as goal a real User Story written. <actor, behavior, benefit> are part of it, but it shall be a human readable user story, like: As a product owner, I need to see which recently released features are used least so that I can decide whether to improve, promote, or remove them.
Please research some Scrum guides on how to write a User Story and define that VERY BRIEF AND SHORT in this CAC-HERMES as important writing part instead of this text.

```text
Goal: <userstory>
Plan: <absolute path>@<exact commit> / phase <id>
Code: <repo/root> / branch <name> / base <sha>
Context: <only task-specific facts/constraints>
AC:
- AC1 <observable outcome>
- AC2 <observable outcome>
Verify: <test seam/existing harness + risk checks>
Deps: <ticket IDs/state; omit if none>
Limits: <accepted exclusions/verification limits; omit if none>
```

Keep task title as a concise **actor–behavior–benefit** statement. Preserve required native assignee/reviewer/workspace/parent/dependency binding separately. Explain binding constraints; label implementation ideas as suggestions.

### Coder → independent Reviewer

```text
Ticket: <id> | impl: <exact sha> | plan: <accepted sha>
AC: <completed criterion IDs or explicit gaps>
Checks: Tests passed | <required failures/skips/gaps>
RED: <recorded original failing test/evidence> | not demonstrated
Delta: <only material deviation/decision; omit if none>
Evidence: <retrievable source/log/test reference when needed>
```

The short string `Tests passed` is permitted only after checking the actual required results. Preserve original executor, checked code state, failed/absent evidence, and any invalidated reused check. Use `kanban_request_review(..., reviewer=<actual reviewer>)` and verify native review state; a comment alone does not initiate review.

### Reviewer findings and verdict

```text
REVIEW <ticket> @ <exact impl sha> | verdict: CHANGES_REQUESTED
F1 HIGH | <file:line or exact route> | <failure trigger>
Fault: <observable violation> | impact: <consequence>
Proof: <test/source/repro> | fix: <required behavior>
```

```text
REVIEW <ticket> @ <exact impl sha> | verdict: APPROVED
AC: verified | open findings: 0 | limits: <only material carried limits>
```

- Describe each distinct finding once on the **same card**. Subsequent return reasons use exact finding IDs and corrective target.
- Distinguish proven defects, unanswered questions, unverified risks, and optional improvements.
- Preserve required closing evidence, `kanban_comment` readback, native `kanban_complete` review metadata (`review_outcome`, `reviewer_checks`, `reviewed_commit`) and `kanban_request_changes`/`kanban_block` semantics from v4. Examples are **not substitutes** for these calls.
- Preserve the Reviewer’s independent source/tests checks even when the Coder supplied an attractive summary.

### Blocked work and decisions

```text
BLOCK <ticket> | kind: <native kind>
Unable: <action> | cause: <verified blocker>
Tried: <relevant authorized mitigation>
Need: <specific decision/access/capability> | owner: <actual role>
State: <affected commit/phase and remaining work>
```

Use existing native `capability`, `transient`, and `needs_input` routes; keep quota reset timestamp/zone, one-time TIMER path, and all safety guards where applicable. Never encode state transitions solely in text.

## 6. Other artifacts

- **Plan:** user-visible problem/solution, scope/exclusions, requirements/AC IDs, consumer impact, risk invariants, dependencies, phase gates, test seams, decision owner, exact accepted revision. Keep decisions reproducible; do not produce explanatory chapters without an information need.
- **Skill:** `trigger → prerequisites → operations → verifiable completion → failure/recovery`; preserve frontmatter, metadata, exact commands, legal material, required reference branches, and original third-party bytes.
- **Status:** `item + state delta + verified result/gap + next owner/action`; omit repetitive acknowledgments.
- **Customer closeout:** report verified outcome, deviations, open limitations, relevant demo access and separate publication/deployment status in clear human language.
- **Memory:** only reusable verified facts, outcomes, decisions, and non-obvious pitfalls with provenance; exclude secrets and transient logs.

## 7. Verification and success criterion

- Classify each rewritten source statement `KEEP | MOVE | MERGE | REMOVE | REVIEW`; track all MUST/conditions/exceptions and where they remain effective.
- Validate representative ordinary, failure, blocked, resumed, high-risk review, and deployment/publish-boundary cases.
- Measure before/after: always-loaded instruction tokens, repeated prompt input, artifact and tool-output tokens, retries, clarification rounds, and independent review acceptance. Use real model tokenizers when available; label byte/character proxies.
- Target metric: **total model cost per independently accepted ticket**; no claimed quality equivalence from textual brevity alone.
- Reject a reduction that loses a gate, makes a required source unreachable, or hides missing evidence. Expand the smallest necessary passage and retest.

**Core rule:** Write the least information that lets the next agent act correctly, safely, and without avoidable rereads.
