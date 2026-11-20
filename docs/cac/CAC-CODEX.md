# CAC-CODEX — Compact Artifact Contract

Purpose: compact task intake and result handoff; **no reduction in implementation reasoning, verification, or code quality**.

## 1. Authority and scope

- CAC controls agent-facing instructions, task prompts, progress/final responses, findings, and internal agent-authored implementation notes.
- Preserve relevant instructions from owned `diagnosing-bugs` and other invoked skills; CAC never replaces the method or its acceptance gates.
- Keep source code, identifiers, interfaces, tests, user-facing text, API docs, error diagnostics, and changelogs correct and maintainable. Compress **reports** rather than code readability or necessary domain explanation.
- Do not change third-party skill text, Codex CLI, the six pinned specialist TOMLs, or Ponytail merely to implement a writing standard.

## 2. Input contract: Hermes Coder → Codex

Send the minimum complete task context; retain exact approved binding and verification intent. Recommended task prompt:

```text
Task: <ticket ID + observable objective>
Binding: <repo> | branch <name> | base <sha> | accepted plan <path>@<sha>
Read: <relevant local instructions/paths and accepted glossary/ADR context>
Scope: <affected behavior and material consumers; binding limits>
AC:
- <testable criterion>
- <testable criterion>
Verify: <existing harness, required RED evidence, integration/risk checks>
Tools: <only needed skill cues, e.g. literal $diagnosing-bugs for bug work>
Specialists: use only for concrete benefit; retain installed model/reasoning limits
Report: CAC-CODEX result; missing checks and blockers explicit; no work diary
```

- Read full relevant plan, code and instructions even when the prompt is short; the Coder must already bind the task to the exact accepted plan and branch.
- Pass established terms and implementation-critical facts; do not paste all upstream SOULs, full plans, old reviews, or successful tool logs when directly retrievable and already mandated.
- When a source is inaccessible to Codex, include its essential task-specific content; a path alone is insufficient.
- On resume include current diff/state, exact remaining AC/findings, invalidated evidence, and required method cues; do not repeat already satisfied preparation.
- Do not silently turn suggestions into constraints or expand scope because a possible improvement seems attractive.

## 3. Work contract

1. Inspect actual repo/branch, relevant code, accepted contract, callers/consumers, tests, and existing work before editing. Preserve unrelated changes.
2. Resolve implementation decisions within delegated accepted scope; report unresolved authority, security, API, or requirement conflicts.
3. Use appropriate tests and existing infrastructure. Preserve recorded RED-before-fix where required by the Hermes Coder policy; if no RED was observed, report that fact.
4. Diagnose actual failures; require literal `$diagnosing-bugs` for bug tasks, resumes, and newly encountered unexplained regressions as directed by the Coder.
5. Preserve completeness across changed value sets, persisted data, schema/enum consumers, exports, APIs, and risk invariants. Do not remove required coverage to save tokens.
6. Use optional Codex specialists only for distinct demonstrated benefit. Keep their pinned settings, permissions, source boundaries, and native review independence.
7. Do not invent recovery/dispatch loops, modify model/provider/reasoning settings outside policy, or install tooling without authorization.
8. Continue to a verified result when feasible; fix recoverable tool failures. Escalate concrete blockers rather than retrying the same failed path indefinitely.
9. Supply exact test failures/warnings; preserve original results retrievably. A brief success report is allowed only after inspection of actual results.
10. Keep implementation changes legible and proportional. Do not abbreviate source code or discard important comments merely to reduce LLM tokens.

## 4. Output contract: Codex → Hermes Coder

Default final response:

```text
result: DONE | BLOCKED | PARTIAL
scope: <ticket ID + brief implemented effect>
files: <paths only when needed for handoff>
AC: <verified criterion IDs; identify unchecked ones>
checks: Tests passed | <failed/skipped/unavailable check + impact>
RED: <evidence ref> | not demonstrated
risks: <material remaining risks/limits; omit if none>
blocker: <specific action/permission needed; only if blocked>
evidence: <retrievable source/result path when needed>
```

- `DONE` means Codex finished its delegated work, **not** that the ticket has passed independent review or that the code is published/deployed.
- Do not assert a commit ID unless one actually exists and was checked. In the v4 flow the Hermes Coder owns committing and `kanban_request_review`.
- Report output state accurately: implemented, checked, unverified, or blocked. Never transform an unsuccessful or unavailable check into `Tests passed`.
- When a test fails, include exact failure identity, reproduction trigger, observed error, relevant file/location, and next corrective action. Use a path/reference for full logs when accessible.
- A one-line output is enough if all required context is already available and no gaps exist. No fixed maximum applies to necessary findings.
- Use compact Markdown or `key: value`; JSON/YAML only when an actual consumer parses it. These illustrative labels are not Codex API keys.

## 5. Language / artifact policy

- English, direct technical clauses. Keep conditions, negations, permissions, and evidence explicit.
- Remove progress narration, self-congratulation, repeated ticket text, raw successful test listings, and speculative redesign essays.
- Use stable names and clear references. Do not invent private abbreviations or symbolic codes that need explanation.
- For documentation required by the product or other humans, follow project conventions and intended audience; CAC compactness is specific to agent-facing artifacts.
- Human questions about missing permissions or product decisions must contain sufficient context/options; avoid mechanical shorthand.

## 6. Integration constraints for `generic-devteam` v4

- The Coder currently puts literal `$caveman` in every Codex task/resume. Replace that prompt style cue with the **shortest reliable CAC-CODEX instruction**, using an already supported loading path. Do not assume new skill metadata or a passive file link is loaded.
- Do **not** remove or repurpose `PONYTAIL_DEFAULT_MODE=full`; Ponytail is a separate configured integration with native hooks. Preserve all approved process-local HOME/CODEX_HOME bindings.
- Existing literal `$diagnosing-bugs` cues remain mandatory where currently specified.
- Preserve installed Codex specialist TOMLs unchanged, `sdlc-review` independence, and exact model/reasoning boundaries.
- Do not create or overwrite an `AGENTS.md` in the customer's product repository as a side effect of Maker setup. Any project-specific AGENTS.md change is a separately scoped product action.
- Optimize recurring context: compare a brief inline CAC prompt clause with a verifiably loaded owned CAC skill before choosing. A longer mandatory skill may cost more than a concise stable prompt.

## 7. Verification

- Test representative feature, bug/RED, resumed task, rejected finding, high-risk invariant, unavailable dependency, and partial-check scenarios.
- Measure prompt+loaded-skill+response tokens and full correction/retry cost; compare to v4 baseline.
- Preserve task success, actual validation, handoff adequacy, independence, and existing guardrails. Restore information when compression increases uncertainty or correction loops.

**Core rule:** Codex performs the full engineering task, then returns the smallest accurate, actionable result to Hermes Coder.
