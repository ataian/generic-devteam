# Adapted retrospective method

Methodological basis: Matt Pocock's `retro` and its companion documentation.
See [NOTICE](../NOTICE.md) for the exact source revision and adaptations; [LICENSE](../LICENSE) retains the MIT terms.
Apply the lenses below to source-backed process friction, not to re-review the product.

## Navigation

Look for long searches, hidden dependencies, and repeatedly reconstructed facts.
Propose a navigation pointer from a file the relevant agent already reads.
Name the target, its content, and the condition for reading it.
Verify the target exists and the consuming role will reach it.
Prefer a pointer to existing documentation over another copy of volatile facts.

## Automated checks

Read the repository's check scripts and CI workflows before proposing a new check.
Inspect the relevant build-tool commands, linter/type configuration, hooks, and recorded outcomes.
Prefer wiring or repairing an existing check over reinventing it.
When neither a hook nor CI runs the relevant checks, report the missing guardrail as a source-backed candidate.
An inaccessible configuration is an evidence gap, not proof that no guardrail exists.
Distinguish a missing check, an unwired check, a silently broken check, and a check the run omitted.
Propose the cheapest suitable guardrail for the observed failure; implementation still requires selection.

## Review standards

Classify the violation before choosing its destination.
Route mechanical violations to deterministic checks in the repository's existing language and tooling.
Examples include banned APIs, import shapes, fixed syntax, and file-location rules.
Use the existing linter, hook, or CI path that catches the violation with the least added machinery.

Reserve prose review standards for genuine judgment: cross-file consistency, contextual style, or design trade-offs a deterministic check cannot decide.
Reuse an existing suitable standards or contribution document before proposing a new `CODING_STANDARDS.md`.
Name the Reviewer as the enforcement owner and verify that the review workflow loads that document.
Keep implementation-critical requirements and conventions available to the Coder.
Independent review can require source exploration; a diff alone is not always sufficient.
Keep the assigned review mandate and evidence requirements intact.

## Sparse steering

Inspect large project or global `AGENTS.md`/`CLAUDE.md` files for misplaced checks and review-only detail.
Keep durable authority, safety constraints, and necessary implementation context reachable.
Prefer sparse steering with navigation pointers to existing checks, standards, and documentation.
Propose moves only after identifying each consumer and its actual loading path.
A shorter root file with an unreachable requirement is a regression.

## Tool economy

Look for expensive calls whose useful results could come from narrower queries or existing tools.
Inspect actual arguments, returned fields, output size, retries, and the decision each call enabled.
Prefer supported filtering and local structured-data reduction to repeated large model-visible dumps.
Reuse unchanged evidence while its inputs and relevant conditions remain valid.
Keep tool-output reduction separate from reducing verification coverage.

## Token economy

Evaluate total work, not just shorter prose or fewer calls.
Inspect repeated unchanged source loading, oversized outputs, unnecessary carried context, repeated reconstruction across handoffs, duplicate analysis and documents, and unproductive retries.
Trace each repetition to its consumer, context availability, changed inputs, and decision purpose.
Distinguish authored duplication, repeated retrieval, and repeated execution before choosing a remedy.
A handoff pointer saves reconstruction only when the recipient can retrieve the needed original evidence reliably.

Repeated readbacks, independent Coder-versus-Reviewer checks, and pre/post-state checks are not automatically waste.
Preserve required evidence, safety, and meaningful independent review.
Consider stale-context risk, retrieval cost, synchronization work, and lost independent perspective as trade-offs.
Separate measured usage or savings from hypotheses.
Character counts and raw call counts are not token, billing, or quality measurements.
Use already available usage records when they answer the question; no mandatory benchmark or token-audit framework is needed.

## No-ops

Look for steering instructions that fail to change actual behavior or have become irrelevant.
Ground no-op deletion candidates in observed behavior, not intuition about model defaults.
A single session may suggest a deletion test without proving a rule useless across models and tasks.
State that uncertainty; propose a bounded comparison only when needed and separately authorized.
Delete a proven no-op sentence rather than preserving its load through cosmetic trimming.
Do not remove a safety or authority contract merely because no incident exercised it.

## Information access

Identify decisions blocked by missing logs, unavailable records, or inaccessible service state.
Prefer existing logs and narrowly scoped read-only visibility, such as captured dev-server output.
Name the missing source, the blocked decision, the access owner, and the smallest proposed access change.
Keep credentials and sensitive source content outside shared reports.
A visibility recommendation grants no permission to widen access or change infrastructure.
