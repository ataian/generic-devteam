---
name: minimal-change-engineering
description: "Smallest correct change for code, scripts, cron, config."
version: 1.0.1
author: "Derived static template; original authorship recorded in preservation audit"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [coding, minimalism, scope-discipline, refactoring, ops, verification]
    related_skills: [systematic-debugging, simplify-code, token-efficiency]
---

# Minimal-Change Engineering

Scope: code, scripts, cron jobs, configuration, automation and infrastructure scripts.

Follow the authority and approval rules in your SOUL.md.
Do not weaken required approvals, verification, or safety measures to reduce the size of a change.

## The rules

1. Make the smallest correct change that fulfills the user's actual goal.
2. Inspect and reuse the existing implementation before adding code.
3. Prefer project patterns, standard libraries and native platform features.
4. Refactor, rename, reorganize or clean up surrounding areas only when the task requires it.
5. Skip hypothetical abstractions, options, dependencies, frameworks, wrappers and future-proofing.
6. Preserve behavior outside the requested scope.
7. Keep necessary validation, error handling, security, idempotency, locking, logging, backups and verification.
8. For operational scripts and infrastructure, minimize the change within safety requirements, regardless of line count.
9. Mention a genuinely better redesign as described below. Perform it only if the user asks.

## Root cause beats a small diff (rules 1 + 6)

1. Before editing, trace the actual flow end to end and grep all callers of the function you will change.
2. Fix the cause in the shared path when caller-specific patches would leave sibling callers broken. The required fix is in scope even if it adds lines or touches files beyond the report.

## In scope vs. out of scope

- In scope: root-cause fix, trust-boundary validation, data-loss prevention, a check that proves the fix, docs/`SKILL.md`/`README` sections describing changed behavior, code made dead by the change.
- Out of scope unless requested: renames, formatting sweeps, import sorting, helper or base-class extraction, `--verbose`/config flags or env toggles, replacing working libraries, incidental cleanup, log-level changes, docs or comments in untouched areas, consistency edits to unrelated callers, framework wrappers for working scripts.

## Say the scope before editing

Before the first edit, state the files and reasons in one line. Announce any newly necessary file before expanding scope.

## Verification is never the thing you cut

- Non-trivial logic: leave one runnable assert-style self-check or small test. No framework or fixtures. Trivial one-liners need none.
- Operations and infrastructure: verify with exit status, expected output, `systemctl status`, a log line or an idempotent re-run. Running the command alone is insufficient.
- On rule 8 work, never cut validation, retries, locks or backups to shorten the diff.

## Naming a better design (rule 9)

Do the task as specified. Only if a redesign would be materially simpler, safer or cheaper, name it as an option in one closing sentence. Do not block completion on that option.

## Pitfalls

- Check for a broken shared path and cosmetic changes that obscure the fix. Before completion, update any docs, `SKILL.md` or `README` sections that describe the changed behavior.
- On cron, systemd or backup work, apply rule 8. Retain rule 7 verification everywhere.
- If the narrow site cannot satisfy the task, explain why and fix the right site.

## Relation to ponytail

Ponytail applies to coding agents only when separately available and authorized. Its stricter "deletion over addition", mandatory `ponytail:` debt markers and `lite/full/ultra` modes describe that skill.
Apply this Hermes skill across its full scope. Keep its validation, security, idempotency, backup and verification requirements. Do not import Ponytail's debt ledger or modes.
