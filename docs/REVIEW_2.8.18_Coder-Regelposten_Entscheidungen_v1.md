# Coder rule reductions — approved decisions and implementation

## Scope

Max approved the collected replacements in chat and commissioned Maker-only implementation.
Baseline: `f0040ce5c748c4aa83d94c77c0be2af928a83a0a`, package `2.8.18`.
Target: `2.9.0` (MINOR: new compatible role-render fields and updater adoption).
No live-team rollout, upstream-skill edits, service changes, commit, or push.

## Approved changes

Original line numbers below refer to the baseline Coder template, not the edited file.

| Original lines | Decision |
|---|---|
| 23 | Select reasoning under the existing control section; remove the matrix wording. |
| 27–30 | Replace discovery prose with one invocation recipe. Maker binds absolute binary, process HOME and CODEX_HOME. Read the model from that config.toml; preserve model/provider, stdin, sandbox, quoted reasoning, background PTY and native completion. |
| 37 | Check the existing `kanban_request_review` response for `ok: true` and `status: "review"`. Keep failure correction/escalation and the project-change pause. Reviewer remains explicit in the preceding call; the response is not claimed to contain reviewer assignment. |
| 41–43 | Use DEFAULT unless complexity or impact is HIGH. Either HIGH permits up to MAX; both HIGH require MAX. No ceiling change. |
| 46 | Remove only `Write the model ID as a literal argument.` Preserve the remaining worker-guard paragraph verbatim. |
| 60 | Remove runtime Planner-registration rechecking. Preserve the bound Planner ID and all routes. |
| 5–12, 44–45, 47 onward except 60 | Preserve role/authority, specialist exceptions, operational gates and failure handling. In particular, capability/quota clauses remain unchanged. |

The earlier suggestion to replace all of original line 46 was withdrawn after Max's correction.
The upstream Codex skill remains unchanged; team-specific restrictions stay in the SOUL.

## Necessary companion changes

- Add `CODEX_BINARY`, `CODEX_PROCESS_HOME`, and `CODEX_HOME` to Coder render fields.
- Validate absolute paths and shell-quote these values only inside shell fences. Preserve raw paths in inline code.
- Populate fields from confirmed setup values; keep the stable binary entrypoint rather than its version-specific release target.
- Reconcile process HOME with the recorded Team-Codex skill home.
- Extend the existing updater's missing-value adoption, without inventing paths or replacing existing recorded values.
- Accept the exact reviewed predecessor renderer while retaining pristine historical baseline checks and unknown-transform rejection.
- Update affected setup/update references, setup-record guidance and existing regression fixtures.
- Renumber subsequent task steps after merging the invocation steps; their substantive text remains unchanged.

## Verification

RED before the template/renderer changes: `Ran 72 tests`; `FAILED (failures=6, errors=1)`.
The error was rejection of the not-yet-supported Codex path fields.
Targeted renderer after implementation: `Ran 72 tests`; `OK`.
Diagnosis routing: `Ran 9 tests`; `OK`.
New updater cases failed before the helper changes, then passed: `Ran 2 tests`; `OK`.

The shell-recipe test executes a local argument recorder, not real Codex. It checks arguments, quoted paths, environment, stdin and workdir.
The updater regression exercises a synthetic installation from the exact baseline, missing inputs without target writes, migration, local-rule preservation and a no-change follow-up proposal.
Static checks confirm manifest paths and uniqueness, matching version fields, retained baseline file ordering and unchanged protected rule text.
The manifest's pre-existing file ordering is not globally sorted; this changeset preserves it rather than performing an unrelated reorder.
Coder template: `16597` bytes before, `15876` bytes after. This is not a measured token or runtime saving.

Independent read-only review of the working-tree diff reported no blocking findings or unintended rule loss.
Full suite: `Ran 224 tests in 330.657s`; `OK (skipped=1)`; exit code `0`.
The skipped delegation-fence test reports `No delegation fence in this process`; the parent cannot exercise the child-only native guard.
The existing simulated-denial regression remains in the passing suite.
Final `git diff --check`: passed. Implementation remains uncommitted; no rollout or live Codex qualification performed.
