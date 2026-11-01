# TAS: Technical Agent Specification

**Status:** Package authoring standard.
**Scope:** All agent-context Markdown, including SOULs, skills, references, setup and update instructions, and project instructions.
**Language:** English for instructions. The agent's user-facing language follows the user or project setting.
**Basis:** Selected ASD-STE100 principles, operational contracts, and progressive disclosure. This is not full ASD-STE100 compliance.

## Purpose

Use TAS to write agent-context Markdown. A SOUL defines durable role behavior. It is not a project encyclopedia, tutorial, change log, or runtime configuration dump. Put other content in the appropriate document type below.

## Writing rules

1. Use plain technical English. Prefer common words and active voice.
2. State one requirement per sentence or bullet. Keep conditions next to the affected action.
3. Use direct imperatives for instructions and prohibitions. Use `must` and `must not` only when explicit requirement levels are necessary, and `can` for permissions. Use `if` for conditions.
4. Identify the actor, action, input, and required result. Include the trigger when behavior is conditional.
5. Define one term for one concept. Keep command names, status values, paths, API fields, and placeholders exact.
6. Keep exceptions when they change permitted behavior. Do not replace conditions with absolute rules.
7. Put stable, non-negotiable boundaries before procedural detail.
8. Remove motivation, character biographies, slogans, repetition, rhetorical emphasis, emoji, filler, and lengthy examples.
9. Write complete but compact sentences. Do not enforce a hard word limit or use telegraph fragments where they hide meaning.
10. Prefer actionable evidence requirements over broad traits such as 'be rigorous' or 'be professional'.
11. Distinguish `planned`, `implemented`, `tested`, `reviewed`, `approved`, `published`, and `deployed`.
12. Report what was checked. Never infer execution success from a command, a commit, or an agent's claim alone.
13. Do not invent requirements, missing source facts, approval, tool capabilities, or test results.
14. State unresolved decisions and the authorized escalation target.
15. Use short prose for explanations, ordered steps for procedures, and tables only when comparison improves clarity.

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

- State the result or blocker first.
- Follow with verified facts, relevant risks, unresolved decisions, and the next action.
- Use concrete paths, commits, test names, and state labels where needed.
- Give a reviewer a reproducible finding, not an impression.
- Give a coder a testable acceptance criterion, not an interpretation task.
- Do not add a summary that merely repeats the report.

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
