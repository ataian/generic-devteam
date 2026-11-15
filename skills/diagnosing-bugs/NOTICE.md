# Provenance and adaptation

Adapted from [Matt Pocock's skills](https://github.com/mattpocock/skills) at exact revision `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`:

- `skills/engineering/diagnosing-bugs/SKILL.md`: original six-phase diagnosis method.
- `skills/engineering/diagnosing-bugs/agents/openai.yaml`: inspected display metadata; not copied.
- `skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh`: inspected last-resort human loop; not copied or required.
- Repository-root `LICENSE`: full original MIT text retained in [LICENSE](LICENSE), including `Copyright (c) 2026 Matt Pocock`.

Owned adaptation by Max and Mariko (Hermes Agent), under MIT.
New adaptation text also falls under the Maker's MIT license.
This provenance is not automatic upstream synchronization.

## Changes and reasons

- Add evidence-based direct-fix classification before the full method. Small clear bugs need verification, not redundant hypotheses, a separate harness, or ritual minimization.
- Disclose the full method in `references/method.md` only for documented diagnostic uncertainty, intermittency, performance isolation, or an unresolved/recurring apparent fix.
- Retain the feedback-loop, reproduction, minimization, falsifiable-hypothesis, targeted-probe, performance-measurement, regression-seam, original-scenario, and cleanup sequence.
- Replace fixed hypothesis/repetition quotas and universal minimization with evidence-dependent actions. Necessary slow checks remain valid.
- Permit clearly provisional hypotheses for safe evidence collection without reproduction; confirmed-cause/fix claims still require evidence.
- Use existing task routing for necessary customer input and permissions, rather than routinely showing hypothesis lists or adding approval rounds.
- Keep Team-Codex as method owner; Coder invokes and validates original results. Preserve native handoff and independent Reviewer.
- Preserve protected inputs, credentials/PII redaction, dirty-tree ownership, resource limits, and operational permissions. Human assistance remains a last resort without importing an unnecessary shell workflow.
- Use portable skill metadata and native Codex `$diagnosing-bugs` invocation. No foreign invocation restriction blocks implicit use for newly emerging regressions.
- Use concise technical English; keep task evidence in existing records instead of adding a diagnosis dossier.
