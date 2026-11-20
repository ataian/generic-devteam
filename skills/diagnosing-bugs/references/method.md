# Full diagnosis method

- Load when the skill selects full diagnosis. Reuse completed work and resume at the first unresolved diagnostic question.
- Applies throughout: the skill's scope, protected-data, risk-verification and native-guard boundaries.

## 1. Build a feedback loop

1. Read relevant accepted glossary definitions and ADRs. Distinguish required behavior from observed code.
2. Build and run a red/green feedback loop for the exact symptom. Use existing project tools by default. Prefer a failing unit, integration or e2e test that reaches the failure. Other options: HTTP script, CLI fixture comparison, browser check, trace replay, minimal harness, property/fuzz test, bisection or differential test. A no-crash assertion alone is insufficient. Keep the actual invocation and decisive redacted result retrievable in existing evidence records.
3. Improve speed, specificity and determinism. Narrow setup and test scope. Control time, random seeds, filesystem, network and other relevant conditions where feasible. Aim for seconds while keeping necessary slow integration checks.
4. Intermittent failure: record reproduction rates and controlled conditions before and after the fix. Improve reproducibility with controlled triggers or timing probes within authorized resource and operational limits. Require sufficient repeated evidence for this failure. A single green run is insufficient, and no fixed repetition count or rate threshold applies.
5. No reproducible loop: report attempts and missing evidence. Use provisional hypotheses only to guide safe evidence collection. Claims of confirmed cause or fix require supporting evidence. Request required environment/access, redacted artifacts or production-instrumentation permission through existing routing. Missing reproduction grants no additional access or operational authority. Use human-assisted repro only as a necessary last resort, through existing communication and protected-input facilities. Never collect passwords or tokens as observations.

Exit with an executed red-capable signal or an explicit reproduction/evidence blocker.

## 2. Reproduce and minimize

1. Reproduce the reported failure and capture decisive evidence. Confirm repeats match the user's error, wrong output or measured slowdown. Keep the original scenario for final verification.
2. Minimize only where it reduces diagnostic uncertainty. Remove one input, step, caller or dependency at a time while preserving the same failure. Stop before a reduction loses the failure or no longer helps distinguish causes.

## 3. Hypothesize

- Remaining ambiguity: rank competing falsifiable hypotheses by evidence and state each prediction. Choose predictions that distinguish causes. No arbitrary quota of alternatives.
- Ask through existing routing only for needed customer knowledge, decisions or permissions. Continue authorized investigation without per-hypothesis approval.
- Exit with testable predictions for the remaining ambiguity.

## 4. Probe and isolate

- Probe to distinguish predictions, changing one variable at a time. Prefer a debugger or REPL, then targeted boundary instrumentation, over indiscriminate logging. Tag temporary instrumentation for safe cleanup.
- Performance: establish a baseline and measure/profile, compare or bisect before claiming cause or improvement.
- Production instrumentation and load testing require existing operational permission. Preserve the user's dirty tree. Use an isolated authorized work area for destructive bisection.
- Exit when observations support a cause and exclude competing predictions. Otherwise revise hypotheses using the new evidence.

## 5. Fix and lock in regression coverage

1. Turn the useful repro into a regression check at a seam that exercises the real failure, including multi-caller or chain behavior as needed.
2. Run the regression red before fixing the evidenced cause within scope, then green afterward. If a code or fixture mutation forces red, first compare it with a pristine copy to verify the mutation.
3. Rerun the original unminimized scenario. For intermittent and performance failures, compare controlled conditions and meaningful repeated measurements with the baseline.
4. Document any missing suitable seam or required access precisely. Keep explicit acceptance and safety checks. A missing seam gives no waiver or authority to redesign architecture.

Exit only when the original symptom is resolved and required verification is satisfied. Report any remaining gaps explicitly.

## 6. Clean up and hand off

1. Remove only task-owned temporary artifacts and instrumentation within existing ownership and approval limits. Verify tagged instrumentation is gone. Retain required operational diagnostics and any useful repro as regression coverage or in a clearly designated debug area when justified.
2. Use existing commit, handoff or task conventions for confirmed cause and meaningful verification. Preserve original evidence. Disclose uncertainty, failed checks and unavailable verification.
3. Complete through existing Coder validation and independent-review handoff. No extra report bundle or approval workflow.
