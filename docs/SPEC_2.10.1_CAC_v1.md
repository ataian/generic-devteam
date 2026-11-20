# Compact Artifact Contract for generic-devteam

Design for review; proposed, not installed. Branch `cac`, Maker `2.10.1`, baseline `7910b031f195e6302022e83b48f58e83081082a1`. Inputs: [Hermes draft](cac/CAC-HERMES.md), [Codex draft](cac/CAC-CODEX.md), current role templates and the owner's clarification. The drafts describe intent, not an extension of role authority.

## Decision

Make the shortest **complete** representation the standard. For recurring agent exchanges, use the compact shape for that exchange: one labeled line, short bullets or a shallow mapping. Use brief prose *within* the shape for a condition, causal link, risk or rationale that labels would obscure. Do not replace a complete structured handoff with a narrative. No universal YAML schema, parser, word cap or empty fields. Keep exact literals, actors, obligation levels, exceptions, sequence, scope, uncertainty, evidence ownership and gaps. Never optimize by asking the recipient to reconstruct missing context.

Keep TAS's separation of authority from procedure, source grounding, verifiable completion, reachable pointers and state distinctions. Keep Caveman's answer-first style, exact payload, concise findings and clarity exceptions; neither upstream remains a required style load. Write internal development artifacts in English. Human-facing text follows its audience, including documentation produced by Codex. CAC neither formats source code nor changes any formal interface, placeholder, native command or required output literal.

## Placement

Use a project-owned authoring reference for maintainers; put short operative rules and recurrent handoff shapes directly in the SOUL of the role that writes them. Put procedural examples in the existing skill at the writing step; do not duplicate the full standard on every invocation. For Team-Codex use a verified, team-local instruction source for the main process and ensure the compact task/result contract reaches children and resumes at the existing delegation boundary. Confirm loader, precedence and updater coverage before selecting a new transport; do not assume a Hermes SOUL is visible in Codex. Preserve unrelated project AGENTS, independent reviewer inputs, specialist configuration and Ponytail. No dependency on repository-only `docs/` at runtime.

| Existing exchange | Required content to preserve; render compactly |
|---|---|
| Planner → implementation ticket | One real user story: real actor, desired behaviour, benefit. The existing title suffices; do not repeat it in `Goal/context`. For a foundation, name the real beneficiary and enabled story. Keep the self-contained criteria, relevant context, test requirements, limits, decisions, dependencies and exact plan bindings; native fields stay native. A native title limit must not silently truncate meaning. |
| Coder → Codex | Goal, evidence, file scope, constraints, criteria and verification plan. Preserve required skill triggers, permissions, specialist settings and restart/resume instructions. |
| Codex → Coder | Concise change and actual result; identify the checked state, relevant evidence, failures, unrun checks and remaining work. Say who executed what when needed. A reply is not the independent verdict. |
| Coder → Reviewer | Exact implementation commit, result, material risks, verification gaps and retrievable original evidence. Preserve recorded RED or the explicit absence of RED; preserve the existing success literal and readback. |
| Reviewer → Coder | Location; concrete failure condition and observation; expected behaviour/correction target; impact; decisive evidence. A fix suggestion is optional, not a transfer of implementation discretion. Distinguish verified defects from questions. Describe a finding once; reference it on return. |
| Reviewer → closing record | Reviewed commit, criteria and findings closed, evidence reused and carried limits. Keep comment, readback, native verdict and machine-readable metadata distinct, in their existing order. |
| Clarification, blocker, status | Use the existing channel and action. Include the decision or change, owner, paused work, evidence, relevant options/recommendation or next action as the existing case requires. Do not turn an information request into an approval or a status string into a transition. |

## Planner → customer

Lead with the result or the decision needed. Use the customer's language, ordinary sentences and exact technical details where they help the decision. For a choice, give the recommendation, consequence and precise question. For routine progress, report what changed for the customer; do not copy internal fields, logs or successful-test lists. Keep the existing final-report contract: deviations, gaps, limits, demonstration access and untested access where applicable, pending publication and retrospective offer. No added reports, contacts, gates or recurring status cadence. The Planner remains the team's customer contact; audience changes style, not routing.

## Conflicts and corrections to the inputs

- Both drafts explicitly disclaim workflow changes. Promoting their illustrative fields to an exhaustive schema would nevertheless drop duties: the Hermes finding lacks the required correction; its handoff allows a generic reference where review requires an exact commit. The two-options example must not force a fabricated alternative.
- CAC-CODEX's null example forbids a null `id` but omits that `id` must **exist**. Presence and nullability are separate. A missing field and a present null must both fail when that is the source rule. This is a concrete counterexample to accepting a shorter rewrite by inspection of length alone.
- Omitting repeated context is conditional: include what the recipient cannot unambiguously retrieve, preserve accepted card scope, and do not expose the implementation narrative to a reviewer investigation that must start independently.
- The prompt requests a whole-project sweep; current `HERMES.md` limits TAS-only sweeps. Scope the exception to this commissioned migration, not an open-ended licence for future rewrites. Inventory every current project-owned agent text; keep already-optimal text with a reason. Preserve historical records, legal notices, external originals, code and customer-owned instructions.
- The planner title already carries the story; the customer's clarification explicitly rejects mandatory duplication in the body. Shortening a story into a technical task label is not acceptable.
- Removing Caveman is a deliberate **delivery change**, not just wording. Cover `caveman-review`, autoload, literal `$caveman`, setup/update/verification and rediscovery. The file updater alone does not retire external assets or edit autoload. Preserve unrelated entries, backups, local changes and Ponytail; report unsafe or shared survivors instead of deleting them or declaring retirement complete. No rollout is authorized here.
- Astra-6.2/high for Mariko and Sol-6.2/high or medium for efficient subtasks apply only to the later Maker implementation session. No delegation to another lead profile and no change to generated teams' model limits. Verify effective routes; an option name or prompt is not proof of the model.

## Acceptance

Inventory old obligations and show their effective owner after the rewrite. Independently compare old/new outcomes for a ticket, normal handoff, failed/skipped check, review return, approved exact commit, capability blocker, customer decision and short customer report. Include cold start and resume for Codex. Test rendered files and isolated setup/update fixtures; preserve old local edits, conflicts, rollback and unrelated configuration. Measure before/after with the same tokenizer and comparable inputs: always-loaded role context, incremental Codex prompt, and representative exchange totals including required references. Treat bytes as a proxy only. Report semantic losses and regressions; do not claim production savings or observed compliance from file tests. No live teams, shared systems, publication or activation in the Maker change.
