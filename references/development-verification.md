# Maker development verification

Use this reference only for an explicit Maker authoring, review, or separately commissioned qualification task.
Do not load it as a prerequisite for ordinary setup or a file update.
Run checks that cover the changed contract in the existing suite.
Do not add a second test framework or bypass native delegation guards.

## Package and helper regression

Run the focused renderer suite before the aggregate suite:

```sh
python3 -B -m unittest discover -s references -p 'test_render_reasoning.py' -v
python3 -B -m unittest discover -s references -p 'test_*.py' -v
git diff --check
```

Use the existing updater fixtures for template parsing, initialization, pristine baselines,
three-way merge, local edits, conflicts, legacy unknown baselines, partial writes, and rollback.
Use `test_bound_recovery.py` for binding, shell quoting, modes, and setup-independent invocation.
Use `test_triage_recovery.py` with the installed Hermes interpreter and synthetic scratch databases.
Retain skipped/denied native transitions as missing evidence; never bypass their guard.
Keep all development fixtures outside installed role skill trees.
Cover legacy active Planner-review returns and parked clarification recovery/reopen in the existing synthetic recovery tests.
Keep pending independent review, same-card history, original implementer provenance, counters, and parent gates intact.
Check migration order, old-contract worker preservation, local authority reconciliation, and saved-files versus effective-loading evidence in the existing instruction tests.

Check manifest file existence, sorted uniqueness, version equality, relative links and anchors.
Compare component assignments, transforms, role fields, complete own skill bytes, helpers, and legal files with the approved baseline.
Check JSON/TOML/YAML and shell/Python syntax where affected.
Render synthetic role values through the existing renderer; compare nonplaceholder bytes.
Review changed instructions under [upstream TAS](upstream-sources.md#tas), including their conditions and required references.
Trace setup references semantically; a keyword scan alone does not establish scope.
Walk missing dependencies, collisions, resume, defaults/overrides, model availability, and update dependency decisions.

## Reviewer method and team routing

Upstream `sdlc-review` describes human decisions as an escalation through `kanban_block` and request-changes as a defect return.
The Maker Reviewer explicitly refines that routing: customer-decision questions return to Coder first through `kanban_request_changes`, without inventing a defect.
Only the Coder escalates unresolved customer decisions through the Planner.
Genuine technical interruptions still block and recover unfinished review with its provenance.
Keep upstream method, lenses, baseline checks, automatic loading, native guards, independent critical-invariant passes, and exact-commit approval unchanged.
This is a team-specific policy refinement, not a claim of universal upstream compatibility or live compliance.
Inspect the installed skill and transition semantics when qualifying that boundary; report concrete drift rather than patching, shadowing, or disabling upstream.
The upstream startup instruction to read the handoff first and the artifact lens instruction to read cold retain their existing read-order tension.

Assess the combined contract through the existing implementation phase and its independent Reviewer.
Map integrated acceptance to that phase instead of adding a closing ticket or a Planner technical re-review.
Check that final Planner reporting uses existing ticket results and verdicts and distinguishes pending publication.

## Separately commissioned behavioral qualification

Require a concrete target, protected access, data/write scope, and activation authorization before live checks.
Do not turn this section into a pending setup checklist.
Select only checks needed by the commissioned question:

- Hindsight: inspect adapter/SDK forwarding if needed; use authorized synthetic role/shared/untagged data to distinguish retain, recall, reflect, prefetch, and consolidation. Preserve `per_tag`, `any_strict`, and tag semantics.
- Codex: check main-process model/reasoning requests, HIGH/HIGH selection, retries/resumes, bounded review escalation, unchanged VoltAgent pins at the manifest revision, and persistent Ponytail/Caveman behavior. Verify that main-process selections do not override these six specialists. Run individual helpers only when commissioned.
- Git: if commit behavior is in scope, use an isolated repository without local identity and compare author/committer on its actual commit with the confirmed team identity.
- Analysis: in an authorized scratch repository, index `probe_entry` calling `probe_leaf`, query that relationship, add `probe_added`, and verify the native update path. For CBM distinguish MCP, hooks, cache binding, subagents, and watcher behavior.
- Communication: distinguish mention, free response, DM, unauthorized-user/channel rejection, and actual subscription delivery. Use synthetic ingress without model calls for rejection checks where supported.
- Planning/pipeline: if commissioned, use a harmless scratch brief with independent and dependent questions, explicit plan acceptance, blocked-first complete chain and subscription, Codex artifact, independent same-card review, and actual Planner report.
- Platform diagnosis: inspect parser/source/loader behavior or timeout/retry/rate-limit handling only for a concrete development question. Do not install or repair shared dependencies without separate authority.
- Board diagnosis: inspect existing graph/events only for an authorized incident. Preserve history and claims; use the installed Planner recovery recipe. Do not experiment with fan-out or patch the kernel during setup.

Report static checks, executed runtime checks, skips, denials, failures, and unperformed live evidence separately.
A package pass does not prove that a live team loaded the files or behaves correctly.
