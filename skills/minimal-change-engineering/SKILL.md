---
name: minimal-change-engineering
description: "Smallest correct change for code, scripts, cron, config."
version: 1.0.0
author: "Derived static template; original authorship recorded in preservation audit"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [coding, minimalism, scope-discipline, refactoring, ops, verification]
    related_skills: [systematic-debugging, simplify-code, token-efficiency]
---

# Minimal-Change Engineering

A calibrated version of "lazy senior dev". Applies to: code, scripts, cron jobs,
configuration, automation, infrastructure scripts.

Subordinate to `SOUL.md` and the Risk & Autonomy Scale: this skill never shortens a
Level 3 gate, verification, or a safety measure.

## The rules

1. Make the smallest correct change that fulfills the user's actual goal.
2. Inspect and reuse the existing implementation before adding new code.
3. Prefer existing project patterns, standard libraries, and native platform features.
4. Do not refactor unrelated code, rename things, reorganize files, or "clean up"
   surrounding areas unless required for the task.
5. Do not add abstractions, configuration options, dependencies, frameworks, wrappers,
   or future-proofing for hypothetical needs.
6. Preserve existing behavior outside the requested scope.
7. Minimalism never overrides reliability or safety: keep necessary validation, error
   handling, security, idempotency, locking, logging, backups, and verification.
8. For operational scripts and infrastructure, prefer the smallest *safe* change over
   the fewest lines of code.
9. If a broader redesign would genuinely be better, mention it briefly, but do not
   perform it unless the user asks for it.

## Root cause beats a small diff (rules 1 + 6)

A bug report names a symptom. Before editing, trace the real flow end to end and grep the
callers of the function you are about to touch. One guard in the shared function is a
smaller diff than one per caller, and patching only the caller named in the ticket leaves
a sibling caller broken. A small change in the wrong place is not minimal, it is a second
bug.

So: fixing the shared code path the reported symptom flows through is **in scope**, even
when it ends up more lines and touches more than the file the report named.

## In scope vs. out of scope

**In scope** (part of the task, not a side change): the root-cause fix; validation at
trust boundaries; error handling that prevents data loss; the check that proves the fix;
updating the doc/`SKILL.md`/`README` section whose described behavior just changed;
removing code the change makes dead.

**Out of scope** (do not do unless asked): renames, reformatting sweeps, import sorting,
extracting helpers or base classes, adding `--verbose`/config flags or env toggles,
swapping a working library, "while I'm here" cleanups, log-level changes, rewriting docs
or comments in untouched areas, changing unrelated call sites for consistency, wrapping a
working script in a framework.

## Say the scope before editing

Before the first edit, state which files you will touch and why (one line). If a file
outside that set turns out to be necessary, say so instead of silently expanding the diff.
This is the cheapest way the user can catch scope drift early.

## Verification is never the thing you cut

Per SOUL "No success without verification": the smallest change still needs evidence.

- Non-trivial logic: leave one runnable check behind (assert-style self-check or a small
  test) — no framework, no fixtures. Trivial one-liners need none.
- Ops/infra: verify by evidence (exit status, expected output, `systemctl status`, log
  line, idempotent re-run), not by "the command ran".
- Never trade a validation, retry, lock, or backup for a shorter diff on rule 8 work.

## Naming a better design (rule 9)

Only when a redesign would be materially simpler, safer, or cheaper: **one sentence, at
the end, as an option** — not a question that blocks completion, not a three-paragraph
proposal, and not on every task. Then do the task as specified.

## Pitfalls

- **Symptom patch dressed up as minimalism** — the named caller got a guard, the shared
  function stayed broken.
- **Cleanup smuggling** — the real fix plus four cosmetic edits; the diff is no longer
  reviewable as one change.
- **Docs left stale** — behavior changed, the adjacent `SKILL.md`/`README` still describes
  the old flow. That is an incomplete task, not a minimal one.
- **Line count as the metric on infra** — fewest lines on cron/systemd/backup work is the
  wrong objective; smallest *safe* change is (rule 8).
- **Minimalism as an excuse to skip verification** — rule 7 wins.
- **Refusing a broader fix that is genuinely required** — if the task cannot be fulfilled
  correctly at the narrow site, say so and fix the right site.

## Relation to ponytail

If separately available and authorized, Ponytail is stricter and dogmatic ("deletion over addition", mandatory
`ponytail:` debt markers, `lite/full/ultra` modes) and aimed at coding agents only. This
skill is the Hermes-side calibrated version: same bias toward the smallest correct diff,
but validation, security, idempotency, backups and verification are explicitly
non-negotiable, and it covers cron/config/automation work, not only code. Do not import
ponytail's debt-ledger or mode machinery here.
