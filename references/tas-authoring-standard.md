# TAS: Technical Agent Specification

**Status:** Package authoring standard.
**Scope:** All agent-context Markdown, including SOULs, skills, references, setup and update instructions, and project instructions.
**Language:** English for development communication and artifacts, including role communication, tickets, handoffs, findings, technical project documentation, and agent instructions. Preserve exact identifiers, quotations, error messages, and deliberately localized product text.
**Basis:** Caveman prose style, operational contracts, and progressive disclosure. This is not full ASD-STE100 compliance.

## Purpose

Use TAS to write agent-context Markdown. A SOUL defines durable role behavior. It is not a project encyclopedia, tutorial, change log, or runtime configuration dump. Put other content in the appropriate document type below.

## Style source

Use the original `caveman` writing skill from the source declared in [the integration recipe](integrations.md#caveman).
For package authoring, read that original directly when it is not already available; installation is not required or authorized.
Apply its style to authored Markdown and other persisted prose, overriding its persisted-content exception.
Use original `caveman-review` for findings, including Auto-Clarity; retain the assigned review procedure and native outcomes.
Preserve exact technical payload, safety warnings, conditions, and exceptions.
Clarity takes precedence over word or line limits.
Generated roles receive these scope rules through their SOULs, not through this authoring reference.

## Instruction contracts

1. Identify the actor, action, input, and required result. Keep triggers and conditions next to the action.
2. Preserve permissions and exceptions; do not replace conditions with absolute rules.
3. Put stable, non-negotiable boundaries before procedural detail.
4. Require observable evidence rather than broad traits such as 'be rigorous'.
5. Distinguish `planned`, `implemented`, `tested`, `reviewed`, `approved`, `published`, and `deployed`.
6. Verify required coverage and results before reporting success. Keep successful-check reporting concise; identify failures and missing required checks.
7. Do not invent requirements, missing source facts, approval, tool capabilities, or test results.
8. State unresolved decisions and the authorized escalation target.

## Content placement

- **SOUL:** Role, authority, prohibited actions, non-negotiable invariants, escalation ownership, primary workflow decisions, communication contract.
- **Shared policy:** Source-of-truth method, common Git safety, memory retention, generic cost discipline. Include here only when the policy is reliably loaded for each role.
- **Skills/references:** Exact tool recipes, lengthy decision trees, test methods, failure recovery details, examples.
- **Project context:** Real repository paths, architecture, accepted requirements, deployment target, setup records.
- **Runtime configuration:** Model/provider identifiers, reasoning limits, home directories, environment bindings, integration configuration. A SOUL may require these values to be validated, without duplicating volatile values.

## Compression contract

Classify every original instruction before rewriting:
- `KEEP`: role or safety invariant; preserve its scope and conditions.
- `MOVE`: procedural detail; move only after ensuring that the destination is loaded when needed.
- `MERGE`: duplicate instructions; retain one authoritative rule.
- `REMOVE`: stylistic filler, redundant examples, or obsolete information confirmed by evidence.
- `REVIEW`: ambiguity, conflict, or apparently obsolete behavior; do not silently change it.

A shorter text is not better if it weakens an approval gate or introduces an unhandled state transition.

## Rule pattern

**WHEN [trigger], [actor] MUST [action] using [source/tool]; THEN verify [result].**

Examples:
- If Codex is unavailable, stop implementation and record the actual error with `kanban_block(kind="capability", reason=...)`.
- After `kanban_request_review`, verify the task status and reviewer assignment.
- If no relevant test ran, report `not tested`. Do not report a successful verification.

## Output contract

- Use concrete paths, commits, test names, and state labels where needed.
- Give a reviewer a reproducible finding, not an impression.
- Give a coder a testable acceptance criterion, not an interpretation task.
- Bind tickets to the exact accepted plan and phase instead of copying requirements or standard team procedures.
- Keep development decisions, accepted exceptions, consequential failures, blockers, outcomes, and verdicts on the existing card.
- Keep routine procedures, successful-test catalogues, command recipes, and log inventories out of ticket prose.

## Rewrite acceptance checks

1. All critical role, approval, security, and review invariants still have an explicit owner.
2. All important conditions and exceptions remain effective.
3. All Kanban transitions name the correct tool and target role.
4. Commits, publication, and deployment remain separate decisions.
5. Runtime-specific prerequisites remain available at execution time.
6. Model/Reasoning limits and Code-only boundaries cannot be bypassed through delegation.
7. Memory cannot overrule the current implementation or accepted requirements.
8. No new behavior was introduced solely to make an agent-context document appear complete.
9. No reference points to a missing or non-loaded file or skill.
10. Rehearse ordinary and failure cases before deployment.
