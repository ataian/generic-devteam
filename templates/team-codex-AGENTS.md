# Team-Codex instructions

Write all communication and artifacts in technical English for the team, not as customer-facing prose. Preserve exact identifiers, quotations, error messages and deliberately localized product text. Prefer the shortest complete form: labeled facts, bullets or short prose. Preserve exact payload, warnings, authority, conditions, exceptions, order and uncertainty. Keep code conventions and formal formats.

- **Task:** Keep goal, file scope, constraints, evidence, criteria, verification and all task-specific directions. Existing tools, permissions and gates apply.
- **Resume:** Reconcile assignment, checked state, delta, blockers and remaining work. Keep standing constraints and required instructions after restart too. Distinguish reused evidence from new checks.
- **Children:** Give each brief the relevant writing rule, task inputs and inherited limits, including in a fresh context. Preserve specialist settings and write scope. Keep briefs distinct. Exclude implementation narrative and prior findings from blind checks.
- **Result:** `Change:` actual outcome. `Checked:` actual results, checked state and decisive evidence or resolvable reference. Name the executor when relevant. `Open:` material failures, unrun or incomplete checks, remaining work and limits with consequences. Keep required negatives. Omit empty labels. Formal output requests win. Identify uncommitted work explicitly. Claim only checks backed by results. Independent review belongs to the designated Reviewer.

## Skills

- For bug/diagnosis tasks, require the literal `$diagnosing-bugs` cue in each Codex task and resume, never as a shell variable. Pass the exact symptom, accepted context, and verification criteria; require the skill for unexplained failures or regressions emerging during implementation too. Validate diagnosis against the original symptom and actual evidence; do not automatically repeat the full method.
- For build-, browser- and process-dependent evidence, use the literal `$build-evidence` cue for the affected mode; the reference owns selector derivation and the isolation-checker limit.
- Record one failing run of a new test before the production change.
- For persisted value-set, enum, schema or outbound-mapping changes, verify stored data and every export path.
