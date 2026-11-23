# Adapted retrospective method

Methodological basis: Matt Pocock's `retro` and its companion documentation. See [NOTICE](../NOTICE.md) for the exact revision and adaptations and [LICENSE](../LICENSE) for the retained MIT terms.
Apply these lenses only to source-backed process friction. Product re-review stays in its assigned workflow.

## Navigation

- Signals: long searches, hidden dependencies, repeatedly reconstructed facts.
- Propose a pointer from a file the relevant agent already reads. Name the target, its content and load condition. Verify existence and reachability for that role. Prefer linking existing documentation to duplicating volatile facts.

## Automated checks

1. Before proposing a check, read check scripts and CI workflows. Inspect relevant build commands, linter/type configuration, hooks and recorded outcomes.
2. Distinguish missing, unwired, silently broken and skipped checks. If neither a hook nor CI runs the relevant checks, cite the evidence for a missing guardrail. Inaccessible configuration leaves an evidence gap.
3. Prefer wiring or repairing existing checks. Propose the cheapest guardrail suited to the observed failure. Implementation still needs selection.

## Review standards

Classify before routing:

- Mechanical, e.g. banned APIs, import shapes, fixed syntax or file-location rules: use deterministic checks in the repository's existing language and tooling. Choose the existing linter, hook or CI path with the least added machinery.
- Judgment a deterministic check cannot decide, e.g. cross-file consistency, contextual style or design trade-offs: use prose review standards. Reuse suitable standards or contribution docs before proposing `CODING_STANDARDS.md`. Name the Reviewer as enforcement owner and verify that the workflow loads the document.
- Keep implementation-critical requirements and conventions available to the Coder. Preserve the review mandate and required evidence. Independent review may need exploration beyond the diff.

## Sparse steering

- Inspect large project or global `AGENTS.md`/`CLAUDE.md` files for misplaced checks and review-only detail.
- Prefer short steering with pointers to existing checks, standards and docs. Identify every consumer and actual load path before proposing a move. Keep all requirements reachable, including durable authority, safety constraints and necessary implementation context.

## Tool economy

- For expensive calls, inspect actual arguments, returned fields, output size, retries and the decision each enabled. Look for narrower queries or existing tools with equivalent useful results.
- Prefer supported filtering and local structured-data reduction over repeated large model-visible dumps. Reuse unchanged evidence while inputs and relevant conditions remain valid. Maintain verification coverage when reducing output.

## Token economy

1. Evaluate total work. Inspect repeated unchanged source loading, oversized outputs, unnecessary carried context, repeated reconstruction across handoffs, duplicate analysis and documents, and unproductive retries.
2. Trace each repetition to its consumer, available context, changed inputs and decision purpose. Distinguish duplicate authoring, retrieval and execution before choosing a remedy. A handoff pointer saves reconstruction only if the recipient can reliably retrieve the needed original evidence.
3. Assess repeated readbacks, independent Coder-versus-Reviewer checks and pre/post-state checks on their purpose. Preserve required evidence, safety and meaningful independent review. Weigh stale-context risk, retrieval cost, synchronization and lost independent perspective.
4. Separate measured usage or savings from hypotheses. Character and call counts do not measure tokens, billing or quality. Use existing usage records when they answer the question. No mandatory benchmark or token-audit framework.

## No-ops

- Look for irrelevant steering or instructions that leave actual behavior unchanged. Ground deletion candidates in observations, not assumed defaults.
- One session can suggest a deletion test without proving irrelevance across models or tasks. State that uncertainty. Propose a bounded comparison only when needed and separately authorized.
- Delete a proven no-op sentence. Cosmetic trimming still costs context. Lack of incidents alone never justifies deleting a safety or authority contract.

## Information access

- For a decision blocked by missing logs, unavailable records or inaccessible service state, name the missing source, blocked decision, access owner and smallest proposed access change.
- Prefer existing logs and narrow read-only visibility, e.g. captured dev-server output. Exclude credentials and sensitive source content from shared reports. Recommendations grant no authority to widen access or change infrastructure.
