# Plan 3.0.1 — Wait rule with the exact window for Coder and Reviewer

**Status: implemented 24 Nov 2026; uncommitted.** Base: Maker `3.0.0`, commit `7e1fee4`. CAC entrypoint
`/home/mariko/projects/cac/SKILL.md` v1.0.0 read with `references/cac-notation.md` and
`references/cac-authoring-contract.md` (24 Nov 2026). No template, test or version file changes before
approval. Owner decision taken 24 Nov 2026: the window value belongs in the role text, because the Maker
writes the same value into the profile in the same run; a pointer ("the configured window") cannot be
resolved by the role.

## 1. Observation

`templates/roles/coder.SOUL.md.template` (8,280 B / 69 lines rendered) and
`templates/roles/reviewer.SOUL.md.template` (20,058 B / 119 lines rendered) carry no rule for the window
between a background start and the result. 3.0.0 removed the last such sentence
(`PLAN_devteam_v3_codercutter.md:262`: "the polling paragraph go") and declared the topic resolved
(`:213`). Measured on the 2.14.4 baseline (SG1 run 10), the profile value is a ceiling, not the behaviour:

| Run | Turns | `process_manage` | `wait` | requested | result | observation-only turns | share |
|---|---:|---:|---:|---|---|---:|---:|
| 31 | 31 | 9 | 4 | 4 × 14,400 s | 4 × 420 s abort | 6 | 19 % |
| 32 | 35 | 7 | 7 | 300–500 s | 5 × timeout, 2 × exited | 6 | 17 % |
| 34 | 25 | 5 | 4 | 850–900 s | 3 × timeout, 1 × exited | 4 | 16 % |
| 35 (Reviewer) | 54 | 26 | 13 | 45–180 s | 9 × timeout, 4 × exited | 12 | 22 % |

The role cannot resolve a pointer: it would need `config get` first. The Maker renders the SOUL and writes
`terminal.timeout 14400` into the same profile run (`references/setup.md:106`), so the literal is exact and
checkable against its own source.

## 2. Change per step

**Step 1 — Coder SOUL.** `templates/roles/coder.SOUL.md.template`, `## Session`, one bullet after the
literal-substitution rule (current line 39), before the worker-guard rule:

```text
- Wait for that process with `timeout=14400`, never with a shorter estimate. A `timeout` status reports an elapsed window; the run continues.
```

**Step 2 — Reviewer SOUL.** `templates/roles/reviewer.SOUL.md.template`, `## Role and authority`, one
bullet after the read-tool rule (current line 8):

```text
- Wait for a background run with `timeout=14400`, never with a shorter estimate. A `timeout` status reports an elapsed window; the run continues.
```

The Reviewer carried the largest share in run 10 and starts builds and matrices the same way.

**Step 3 — bind the literal to its source.** `references/test_render_reasoning.py`:

- New test `test_wait_window_matches_the_configured_terminal_timeout`: read the number from
  `references/setup.md` (`config set terminal.timeout <n>`), then assert both rendered SOULs contain
  `` `timeout=<n>` `` and contain neither `15000` nor `28800`.
- Remove `assertNotIn("14400", result)` (current line 202). The 2.14.3 rule "values live in the recipe, not
  in the role" is superseded by the decision in the header; with the equality test, prose and profile cannot
  drift unnoticed.
- Move the rendered Coder pin from 8,280 B / 69 lines to **8,422 B / 70 lines**; add the Reviewer pin
  **20,204 B / 120 lines** (render probe with the repository fixture bindings, both measured 24 Nov 2026).
- Keep `assertNotIn("do not wait again", …)`: the new sentence forbids shortening the window, not continuing
  the run.

**Step 4 — version.** `SKILL.md` and `manifest.json` to `3.0.1` (MINOR: behaviour rule added).

## 3. Not changed

- `references/setup.md`, `references/update.md`: the three `config set` lines and update step 4 stay. They
  put the 15,000 s tool deadline above the 14,400 s window; without them the sentence would promise a limit
  that does not exist, as it did in 2.14.0.
- Hermes core: no patch, no configuration key, no new tool.
- Planner text, review procedure, authority, card states; `PLAN_devteam_v3_codercutter.md` stays as the
  historical decision — the correction lives here.

## 4. Verification after approval

```
cd references && python3 -m unittest test_render_reasoning test_build_evidence   # 95 tests, OK
cd references && python3 -B -m unittest discover -s . -t . -p 'test_*.py'        # 268 tests, OK (skipped=1)
```

Result 24 Nov 2026: `Ran 268 tests in 407.444s — OK (skipped=1)`, exit 0. The skip is the known
delegated-child guard test.

New test red before the templates changed: `test_wait_window_matches_the_configured_terminal_timeout`
failed for both roles (`'timeout=14400' not found`), green afterwards.

Deviation, recorded because it occurred: the first full run ended
`FAILED (failures=1)` on `test_complete_skill_tree_is_in_manifest` — a stray
`skills/brownfield-feature-planning/scripts/__pycache__/*.pyc` from an earlier Python run inside the
skill tree. The file is gitignored, so `git status` stayed clean while the test enumerated the filesystem.
Removed both `__pycache__` directories, re-ran unchanged: green. No source or content change was involved.

## 5. Limit

The rule lowers turn count only if the model follows it; the parameter stays free and the harness cannot
observe intent. Comparison after the next 3.0.x run: share of observation-only turns against the 2.14.4
baseline above, same accounting.

## 6. Follow-up 3.0.2 — where the window really comes from

Measured on 24 Nov 2026 with five isolated variants (`hermes -p <profile> chat -q`, one Codex job each):
the role line makes the model ask for 14400, but the accepted window is clamped by `TERMINAL_TIMEOUT` in
the worker process, default 180 s — the profile's `terminal.timeout` reaches it only through the
environment. One variant requested 14400 and was answered "Requested wait of 14400s was clamped to
configured limit of 180s", so it polled every three minutes despite the rule. `setup.md` now states the
runtime source, the 180 s fallback and the dependency on the card's `--max-runtime`; the existing recipe
test asserts all three sentences. Version 3.0.2 (PATCH: documentation only).
