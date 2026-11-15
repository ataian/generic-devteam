---
name: diagnosing-bugs
description: Diagnose bugs, unexplained failures, and regressions.
version: 0.1.0
author: Max, Mariko (Hermes Agent); adapted from Matt Pocock
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [debugging, diagnosis, regression]
    related_skills: []
---

# Diagnosing bugs

Team-Codex owns diagnosis and implementation within the accepted task.
Use evidence to choose a direct fix or the full diagnosis method.

## When to use

Use for bug/diagnosis tasks and unexplained test failures or regressions found during ordinary implementation.
Use the accepted goal, context, exact symptom, expected behavior, and verification criteria.
If required behavior is unclear, resolve it through existing task routing.

## Boundaries

Keep all probes within existing scope, resource limits, operational permissions, and native safeguards.
Redact credentials and PII before returning outputs or captured artifacts.
Use protected input/data paths; do not expand secret environment values into commands or logs.
Preserve required security, data-integrity, acceptance, and independent-review checks on both paths.
Risk alone does not require prolonged cause exploration; ticket or diff size does not select the path.

## Classify from evidence

Start with a short targeted investigation using available code, repros, and original results.
Check full-diagnosis triggers before selecting the direct-fix path.
Use the direct-fix path only when all three conditions hold:

- Concrete evidence supports both the symptom and its cause.
- The affected flow and required correction are clear.
- A focused test or reproducible check can demonstrate the exact bug and its correction.

Demonstrate the error, correct its cause, and run relevant verification.
Do not generate alternatives, build a separate harness, or further minimize an already simple case to satisfy a checklist.

Use full diagnosis when any condition applies:

- The cause remains unclear after the first targeted investigation.
- Multiple plausible causes need distinguishing.
- The failure is intermittent or depends on state, timing, or environment.
- A performance regression needs measurement and isolation.
- An apparent fix leaves the original symptom unresolved, or the failure recurs.

Switch as soon as uncertainty is evident, before guessed fix attempts.
Reuse completed investigation, repros, and checks instead of restarting.
Technical deepening within accepted scope needs no new Planner or customer approval.
Read [the full method](references/method.md) completely when any full-diagnosis trigger applies.
If the required reference is missing or unreadable, report its path and stop the affected diagnosis.

## Verification and handoff

Verify the original symptom is resolved and required regression, acceptance, and risk checks pass.
Report unavailable or incomplete required checks and their consequence through existing task conventions.
State confirmed cause and meaningful verification with original evidence retrievable; label remaining uncertainty.
Keep independent review and the existing handoff unchanged; no separate diagnosis dossier is required.
