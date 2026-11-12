# Full diagnosis method

Read this method when the skill's evidence classification selects full diagnosis.
Reuse completed work and continue at the first unresolved diagnostic question.
The skill's scope, protected-data, risk-verification, and native-guard boundaries remain binding throughout.

## 1. Build a feedback loop

Read relevant accepted glossary definitions and ADRs; distinguish desired behavior from observed code.
Build and run a symptom-specific red/green-capable feedback loop with available project tools.
Prefer a failing unit, integration, or e2e test at a seam reaching the failure.
Other suitable loops include an HTTP script, CLI fixture comparison, browser check, trace replay, minimal harness, property/fuzz test, bisection, or differential test.
Use available project tools instead of installing a new framework by default.
Assert the exact symptom, not merely absence of a crash.
Keep the actual invocation and decisive redacted result retrievable through existing evidence conventions.

Improve loop speed, specificity, and determinism.
Narrow setup and test scope; control time, random seeds, filesystem, network, and other relevant conditions where feasible.
Optimize toward seconds without dropping necessary slow integration checks.
For intermittent failures, record reproduction rates and controlled conditions before and after the fix.
Increase reproducibility with controlled triggers or timing probes within authorized resource and operational limits.
A single green run does not establish resolution.
Choose sufficient repeated evidence for this failure; do not invent a fixed repetition count or reproduction-rate threshold.

Without a reproducible loop, label hypotheses provisional and use them only to guide safe evidence collection.
Do not claim a confirmed cause or fix without supporting evidence.
State what was tried and which evidence is missing.
Request required environment/access, redacted artifacts, or production-instrumentation permission through existing routing.
Missing reproduction grants no additional access or operational authority.
Use human-assisted reproduction only as a necessary last resort through existing communication and protected-input facilities.
Never collect passwords or tokens as observations.

Complete this step with an executed red-capable signal, or an explicit reproduction/evidence blocker.

## 2. Reproduce and minimize

Reproduce the actual reported failure and capture decisive evidence.
Confirm repeated failures match the user's error, wrong output, or measured slowdown rather than a nearby defect.
Minimize where it reduces diagnostic uncertainty: remove one input, step, caller, or dependency at a time while preserving the same failure.
Keep the original scenario for final verification.
Complete minimization when further reductions would lose the failure or no longer help distinguish causes.

## 3. Hypothesize

Where ambiguity remains, rank competing falsifiable hypotheses by evidence and state each prediction.
Choose predictions that can distinguish causes, not an arbitrary quota of alternatives.
Ask through existing routing only when customer knowledge, a decision, or permission is needed.
Continue authorized technical investigation without a hypothesis-by-hypothesis approval round.
Complete this step with testable predictions for the remaining ambiguity.

## 4. Probe and isolate

Use each targeted probe to distinguish those predictions; change one variable at a time.
Prefer a debugger or REPL, then targeted boundary instrumentation, over indiscriminate logging.
Tag temporary instrumentation for safe cleanup.
For performance regressions, establish a baseline and measure/profile, compare, or bisect before declaring cause or improvement.
Production instrumentation and load testing require their existing operational permission.
Preserve the user's dirty tree; use an isolated authorized work area for destructive bisection.
Complete isolation when observations support a cause and exclude the competing predictions; otherwise revise hypotheses from new evidence.

## 5. Fix and lock in regression coverage

Use a regression seam that exercises the real failure pattern, including multi-caller or chain behavior when needed.
Turn the useful repro into that regression check.
Run the regression red before the fix, then green afterward.
If red is forced by a code or fixture mutation, compare with a pristine copy to verify that mutation first.
Correct the evidenced cause within task scope.
Rerun the original unminimized scenario after the fix.
For intermittent and performance failures, compare the controlled conditions and meaningful repeated measurements with the baseline.
Document a missing suitable seam or required access precisely; preserve explicit acceptance and safety checks.
A missing seam neither waives a required check nor authorizes architecture redesign.
Complete this step only with the original symptom resolved and required verification satisfied; report remaining gaps explicitly.

## 6. Clean up and hand off

Remove only task-owned temporary artifacts and instrumentation within existing ownership and approval limits.
Check tagged instrumentation is gone; retain required operational diagnostics.
Retain a useful repro as regression coverage or in a clearly designated debug area when justified.
State confirmed cause and meaningful verification in existing commit, handoff, or task conventions.
Preserve original evidence and disclose uncertainty, failed checks, and unavailable verification.
Complete through the existing Coder validation and independent-review handoff, not another report bundle or approval workflow.
