# Maker development verification

Use for explicit Maker authoring, review or separately commissioned qualification. Ordinary setup and file updates have their own checks.
Cover the changed contract in the existing suite. Keep native delegation guards and the existing test framework.

## Package and helper regression

Run the focused renderer suite before the aggregate suite:

```sh
python3 -B -m unittest discover -s references -p 'test_render_reasoning.py' -v
python3 -B -m unittest discover -s references -p 'test_*.py' -v
git diff --check
```

Keep development fixtures outside installed role skill trees. Use the following checks where affected.

- **Package.** Check manifest paths, sorted uniqueness, version equality, links and anchors. Compare assignments, transforms, role fields, full owned skill bytes, helpers and legal files with the approved baseline. Check affected JSON/TOML/YAML and shell/Python syntax. Render synthetic values through the existing renderer and compare nonplaceholder bytes.
- **Instruction fidelity.** Use [CAC authoring](cac-authoring.md) to compare old and new decisions, evidence and required loads, including negative and exception cases. Follow setup references through missing dependencies, collisions, resume, defaults/overrides, model availability and update dependency decisions. Check migration order, old-contract workers, local authority reconciliation and the difference between saved files and effective loading.
- **Update fixtures.** Cover template parsing, initialization, pristine and unknown legacy baselines, three-way merge, local edits, conflicts, partial writes and rollback. Exercise Planner-only environment delivery and Team-Codex diagnosis tree additions, dependency decisions, collisions, adaptations and retained additions on rollback. These fixtures need no Docker, PostgreSQL or live agents.
- **Recovery.** Use `test_bound_recovery.py` for binding, shell quoting, modes and setup-independent invocation. Run `test_triage_recovery.py` with the installed Hermes interpreter and synthetic databases. Cover legacy active Planner-review returns and parked clarification recovery/reopen. Preserve pending independent review, same-card history, original implementer provenance, counters and parent gates. Record skipped or denied transitions as missing evidence and keep the guard.
- **Skill contracts.** Use `test_diagnosing_bugs.py` for proportional paths, method pointer, delivery/legal and explicit Team-Codex invocation. Use `test_prototype.py` for Planner-only clarification authority, branch/legal coverage, delivery and updates. Keep throwaway demos outside package review gates. Use `test_dev_environment.py` and renderer checks for checkout-based tooling, guide scope, developer-workflow acceptance and deployment boundaries. Treat these as static contracts.
- **Native Codex loading.** Use the isolated [Team-Codex prompt check](integrations.md#team-codex-instructions) for the selected CLI. Cover separate homes, existing home text, home override, nested project instructions and truncation. Compare the assembled instructions and include a failed shadowing expectation. Record the exact CLI version and fixture context separately from the manifest pin and actual team adoption.

## Reviewer method and team routing

- **Routing.** Upstream `sdlc-review` sends human decisions through `kanban_block` and defects through request-changes. The Maker Reviewer returns customer questions to Coder through `kanban_request_changes` without inventing a defect. Only Coder escalates unresolved decisions through Planner. Technical interruptions block and recover unfinished review with provenance. Preserve upstream method, lenses, baseline checks, preload, native guards, independent critical-invariant passes and exact-commit approval.
- **Investigation.** The Reviewer SOUL owns direct small corrections or distinct parallel Spec and technical-quality reviews, followed by decisive-evidence validation and gap closure. Skip an automatic third full review. Use `test_review_investigation.py` for rendered/exported scenarios and operative-body/qualification mutations. Use the updater fixtures for actual SOUL delivery, preserved local rules, collisions, pristine baselines and rollback. Compare ordinary, missing-plan, correction, qualified/unqualified HIGH helper and unavailable-capability cases against the same coverage and native outcomes.
- **Helper qualification.** Inspect native schema and effective model/provider/reasoning before crediting evidence. The inspected built-in schema supports parallel `tasks` with separate `goal`/`context` and lacks generic per-task model/reasoning fields. Native configuration can override inheritance. Verify HIGH on the actual route. Use an existing permitted compatible route and keep profile settings and guards intact.
- **Compatibility.** Qualify this team-specific routing against the installed skill and transitions. Report concrete drift. Keep upstream unpatched, unshadowed and enabled. Preserve the existing read-order tension between startup handoff-first and the artifact lens's cold read. Static contracts do not establish live compliance or general upstream compatibility.
- **Acceptance.** Map integrated acceptance to the existing implementation phase and its independent Reviewer. Add no closing ticket or Planner technical re-review. Verify the final Planner report uses existing ticket results and verdicts and identifies pending publication.

## Separately commissioned behavioral qualification

Require a concrete target, protected access, data/write scope, and activation authorization before live checks.
Do not turn this section into a pending setup checklist.
Select only checks needed by the commissioned question:

- Hindsight: inspect adapter/SDK forwarding if needed; use authorized synthetic role/shared/untagged data to distinguish retain, recall, reflect, prefetch, and consolidation. Preserve `per_tag`, `any_strict`, and tag semantics.
- Codex: check main-process model/reasoning requests, HIGH/HIGH selection, retries/resumes, bounded review escalation, unchanged VoltAgent pins at the manifest revision, and persistent Ponytail behavior and effective team-local writing instructions. Verify that main-process selections do not override these six specialists. Run individual helpers only when commissioned.
- Git: if commit behavior is in scope, use an isolated repository without local identity and compare author/committer on its actual commit with the confirmed team identity.
- Analysis: in an authorized scratch repository, index `probe_entry` calling `probe_leaf`, query that relationship, add `probe_added`, and verify the native update path. For CBM distinguish MCP, hooks, cache binding, subagents, and watcher behavior.
- Communication: distinguish mention, free response, DM, unauthorized-user/channel rejection, and actual subscription delivery. Use synthetic ingress without model calls for rejection checks where supported.
- Planning/pipeline: if commissioned, use a harmless scratch brief with independent and dependent questions, explicit plan acceptance, blocked-first complete chain and subscription, Codex artifact, independent same-card review, and actual Planner report.
- Platform diagnosis: inspect parser/source/loader behavior or timeout/retry/rate-limit handling only for a concrete development question. Do not install or repair shared dependencies without separate authority.
- Board diagnosis: inspect existing graph/events only for an authorized incident. Preserve history and claims; use the installed Planner recovery recipe. Do not experiment with fan-out or patch the kernel during setup.

Report static checks, executed runtime checks, skips, denials, failures, and unperformed live evidence separately.
A package pass does not prove that a live team loaded the files or behaves correctly.
