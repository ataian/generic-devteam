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

Owner: Team-Codex diagnoses and implements within the accepted task. Evidence selects direct fix or full diagnosis.

## When to use

- Trigger: bug or diagnosis task, or an unexplained test failure or regression during ordinary implementation.
- Inputs: accepted goal and context, exact symptom, expected behavior and verification criteria. Resolve unclear required behavior through existing task routing.

## Boundaries

- Probes: stay within scope, resource limits, operational permissions and native safeguards.
- Data: use protected input/data paths. Never expand secret environment values into commands or logs. Redact credentials and PII before returning output or captured artifacts.
- Both paths retain required security, data-integrity, acceptance and independent-review checks. Risk alone does not require extended cause exploration. Ticket and diff size do not select the path.

## Classify from evidence

1. Investigate briefly using available code, repros and original results.
2. Check full-diagnosis triggers first. Switch before attempting guessed fixes, as soon as uncertainty is evident or any trigger applies:
   - Cause still unclear after the initial investigation, or plausible causes need distinguishing.
   - Intermittent failure or dependence on state, timing or environment.
   - Performance regression requiring measurement and isolation.
   - Original symptom survives an apparent fix or recurs.

   Read [the full method](references/method.md) completely. If missing or unreadable, report its path and stop the affected diagnosis. Reuse completed investigation, repros and checks. Deepening within accepted scope requires no new Planner or customer approval.
3. Use direct fix only if concrete evidence supports both symptom and cause, the affected flow and required correction are clear, and a focused test or reproducible check can demonstrate the exact bug and its correction. Demonstrate the error, fix the cause, then verify. Do not generate alternatives, build a separate harness, or further minimize an already simple case to satisfy a checklist.

## Verification and handoff

Verify resolution of the original symptom and passing required regression, acceptance and risk checks. Keep the existing handoff and independent review. Use compact bullets within task conventions.

- Cause: confirmed cause, if established.
- Checked: meaningful verification and retrievable original evidence.
- Open: remaining uncertainty and any failed, unavailable, or incomplete required checks with their consequences.

No separate diagnosis dossier is required.
