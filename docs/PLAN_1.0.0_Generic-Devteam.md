# Generic Devteam — setup-only Maker implementation plan

> **Execution:** Scotty implements through Codex. Julia reviews each phase on the same ticket through `kanban_request_review(reviewer="julia")`. Kirk coordinates. Do not create separate review tickets, extra coding agents, or an additional LLM judge.

**Status:** Draft for Max's implementation approval. The design specification is accepted; this plan is not yet approved for execution.
**Goal:** Preserve the equipped team's capabilities and update safety while removing recurring research and behavioral qualification from ordinary setup.
**Architecture:** Keep the existing prose-driven Maker, templates, helpers, and file updater. Simplify the record without changing its consumer contract, then replace the normal setup/readback contract consistently across entry points and references. Keep development verification outside the normal setup path.
**Tech stack:** Markdown/TAS instructions, JSON manifest/private records, existing Python helpers and unittest fixtures, local Git.
**Workspace and existing repository:** `/home/joi/projects/generic-devteam`; no initialization, relocation, or restructuring.
**Spec:** [Accepted design](specs/2026-11-01-maker-setup-scope-design.md), substantive accepted content in commit `0694e651df32dbe7d5187d6d4105fb2b91819b0c`.
**Implementation baseline:** Maker `1.1.4`, code/package commit `a44d15e3aad77b891fa5c95ebeba49a780e4525e`; planning commits on `develop` do not change that package.
**Plan version:** `1.0.0`, the first SemVer-named implementation plan in this repository. Do not renumber historical unversioned planning material.
**Target package version:** `1.1.5`, one PATCH for this coherent compatible recipe/documentation revision under `AGENTS.md`. Set it in both version fields at the final phase, not per intermediate commit. If the starting package changes before execution, Kirk reconciles the baseline and version before work starts.

## 1. Global constraints

- Read `HERMES.md`, `AGENTS.md`, the accepted spec, and `references/tas-authoring-standard.md` before work. Write changed agent instructions in plain technical English.
- Preserve three profiles, independent review, complete assigned skills/helpers, model and reasoning limits, Codex identity/homes, chosen code analysis, Hindsight role/bank configuration, communication permissions, and board/workspace bindings.
- Preserve role-template bytes, installed skill payloads, component assignments, render fields, and transforms unless a concrete setup backlink needs a minimal correction approved by Kirk within the accepted scope.
- Do not replace runtime roles' legitimate Git, task, approval, review, or security checks with weaker rules.
- Preserve existing update formats and legacy safeguards. Do not change `SCHEMA`, `copy-v1`, `bound-recovery-v1`, or the renderer compatibility policy.
- Prefer no production Python changes. If a consumer unexpectedly depends on removed prose, keep compatibility through a minimal correction and regression; do not redesign the updater.
- Do not add shared dependency installation, upgrade, repair, version-certification infrastructure, a team registry, a new state store, or a second installer.
- Do not change live profiles, private setup records, shared Hermes configuration, services, identities, credentials, or the installed default-profile launcher.
- Do not run an actual team setup, model/delegation call, synthetic memory conversation, communication test matrix, or coding/review test card under this plan.
- Do not push, publish, deploy, deliver an archive, or restart running agents. Report the reviewed repository result; Max decides any later delivery or activation separately.
- Keep internal review evidence local or as durable card attachments. Do not put file paths in `artifacts`, `metadata.artifacts`, or automatically deliverable handoff text.
- Treat intermediate commits as revision work, not a Maker release ready for team installation. The coherent package result requires both phase reviews.

## 2. Review focus and owning phase

| Risk/input | Expected result | Verification owner |
|---|---|---|
| Shortened record, nested Codex process HOME, custom paths | Existing parsers retain exact values and correct source/target mappings | Phase 1 template-to-updater fixture and existing nested-home tests |
| Older installation, missing binding, local edits or conflict | Reuse confirmed evidence; preserve edits; block unsupported updates without claiming success | Phase 1 existing legacy, binding, conflict, and rollback tests |
| Missing prerequisite or conflicting/centrally managed setting | Report the affected setup item; accept an already correct effective value; no research, upgrade, or restriction bypass | Phase 2 instruction walkthrough |
| Development instructions reachable through a required reference or installed launcher | Ordinary package entry no longer assigns them; external launcher divergence remains explicit until separately changed | Phase 2 reference trace and launcher handoff |
| Correct files but untested agent behavior | Report setup-output verification, not behavioral qualification; no permanent pending gate for excluded experiments | Phase 2 completion/record consistency review |

## 3. Phase 1 — simplify records without losing update support

**Predecessor:** Explicit approval of this plan. No predecessor implementation phase.
**Goal:** Produce a compact setup record that remains directly usable by the current binder and updater.
**Repository:** `/home/joi/projects/generic-devteam`.
**Modify:** `templates/setup-record.md`, `references/setup.md` record-writing/resume/baseline instructions only, `references/update.md` affected record references only, `references/test_update_team.py`.
**Read and preserve:** `references/update_team.py`, `references/bind_recovery.py`, `references/render_text.py`, `references/test_bound_recovery.py`, `manifest.json`.
**Interface consumed:** `setup_data(state)` parses exactly one fenced JSON block from private `devteam/setup.md`; `initialize(...)` and `bind_recovery.install(home)` consume `confirmed_values` and `confirmed_bindings`.
**Interface produced:** The same JSON keys/types and private paths, with less duplicated human-maintained prose. No schema or helper signature change.

- [ ] **1. Trace record consumers.** Confirm `setup_data`, `initialize`, `prepare`, and `bind_recovery.install` against the actual execution baseline. Keep `confirmed_bindings.roles` with `planner`, `coder`, `reviewer`, `team-codex` and each `id`/`home`; keep `triage_recovery` with `python`, `script`, `db`, `planner_profile`. Preserve all required `confirmed_values`, including workspace/repository boundaries, technical role IDs, and reasoning values.
- [ ] **2. Add one template-based regression in the existing `UpdaterTests`.** Name it `test_setup_record_template_preserves_update_round_trip`. Use the actual repository `templates/setup-record.md`, replace its single JSON block with the fixture's existing complete confirmed data, and write it privately to the fixture state. Assert `setup_data` returns those exact values. Initialize the synthetic team, verify version/commit/roles/mappings and pristine baseline bytes, make the existing fixture's nonconflicting local/source changes, prepare/apply with existing review decisions, and rollback. Assert local edits survive, metadata tracks only verified outputs, and rollback restores the recorded prior bytes/metadata. Use existing fixture methods; no new harness. This is a compatibility characterization and may pass before the text rewrite; do not fabricate a failing baseline.
- [ ] **3. Simplify the template.** Keep the single JSON block as the confirmed-data source. Keep short sections for authorizations, actual setup targets and availability/readbacks, progress/blocker/next action, and installation-baseline references. Remove duplicate raw-value tables, behavioral experiment checklists, and mandatory evidence for helper calls, consolidation, interview quality, pipeline runs, or general platform limits. Do not store secrets.
- [ ] **4. Align record-writing and resume instructions.** Update the relevant parts of `setup.md` and `update.md` to use the retained structure. Distinguish missing confirmed input, actual target drift, and stale descriptive prose. Resume only the incomplete step. Keep `update_team.py init` after delivery/readback and recovery binding; preserve `installation.json`, personalized `baselines/<sha256>`, update proposals, backups, and result journals.
- [ ] **5. Verify the real contract.** Run the template regression and existing updater tests listed below. Confirm no edits to the production helper algorithms, role templates, or skill payloads. Check `git diff --check`.
- [ ] **6. Commit and hand off.** Commit only Phase 1 files with `refactor: simplify setup records while preserving update evidence`. Request Julia review on the same ticket. Do not install this intermediate revision into a team.

**Acceptance:** The revised record is parseable by unchanged consumers; exact setup values and installation/update metadata survive the synthetic round trip; local edits and conflict/legacy safeguards remain effective. Removed research checks are not retained as mandatory pending record items.

**Focused command** (repository root):

```sh
python3 -B -m unittest discover -s references -p 'test_update_team.py' -v
```

**Existing regression anchors:** `test_complete_skill_tree_and_personalized_baseline`, `test_nested_coder_codex_home_supports_init_plan_apply`, `test_three_way_keeps_local_edits_and_pristine_new_baseline`, `test_legacy_souls_preserve_drift_and_do_not_adopt_skills`, `test_old_installation_missing_path_binding_stops_without_writes`, `test_conflict_stops_without_target_writes`, `test_partial_write_failure_keeps_revision_and_can_rollback`, `test_rollback_refuses_edits_made_after_update`.

Run the full required suite before the package-change commit under section 5's bounded execution rules. A focused green result is not a replacement for missing mandatory regression evidence.

## 4. Phase 2 — establish one setup-only contract throughout the Maker

**Predecessor:** Julia approves Phase 1.
**Goal:** Deliver the complete narrower setup path without removing team functionality or reintroducing research through references.
**Repository:** `/home/joi/projects/generic-devteam`.
**Modify:** `AGENTS.md` (development-reference pointer only), `SKILL.md`, `README.md`, `NOTICE.md`, `manifest.json`, `references/setup.md`, `references/native-workflow.md`, `references/integrations.md`, `references/code-analysis.md`, `references/kanban-block-triage-escalation.md`, `references/verification.md`; reconcile `references/update.md`, `references/upstream-sources.md`, and `templates/setup-record.md` only where affected by this contract.
**Create:** `references/development-verification.md` for retained Maker-development checks; `docs/operations/maker-launcher-handoff.md` for the external-launcher compatibility finding and proposed minimal replacement text. Do not install that replacement.
**Conditional correction only:** Exact setup backlinks in `templates/roles/*.SOUL.md.template` or `skills/**`, after documenting the concrete conflicting instruction and obtaining Kirk's technical scope decision. No broad rewriting.
**Interface consumed:** Phase 1's unchanged record/update contract and the current supported configuration recipes.
**Interface produced:** Normal entry → necessary setup recipes → setup-only readback and versioned installation record. Development checks have a separate explicit development trigger.

- [ ] **1. Rewrite entry and sequence around the accepted outcome.** Define the five setup steps from spec section 4. State the established dependencies and bounded missing-prerequisite response. Keep names, models, reasoning limits, selected analysis, ownership, activation, and protected access choices. Load only the chosen analysis branch; do not require both complete alternatives as work instructions.
- [ ] **2. Retain concrete bindings; remove recurring investigation.** Apply the decisions below to the existing recipes. Preserve command/configuration details that actually create the required state. Do not replace them with vague instructions to discover a working integration.
- [ ] **3. Split verification by actor and trigger.** Make `verification.md` the ordinary setup-output checklist. Move useful package/unit/recovery/updater regression instructions and explicitly commissioned behavioral qualification to `development-verification.md`. Link that file from the development section of README and the authoring context, not as required setup reading. Preserve historical research only if useful; do not create another research archive or per-setup audit ledger.
- [ ] **4. Reconcile completion, failure, and resume wording.** Use `Team configured; setup outputs verified` only when required setup outputs/readbacks and update baseline are complete. Name real incomplete bindings precisely. State excluded behavioral testing as outside scope, not an outstanding gate. Keep the actual update operation's `applied`, `skipped`, `failed`, unknown-baseline, and retained-file distinctions.
- [ ] **5. Preserve package identity and contents.** Compare component assignments, role fields, transforms, own skill trees, helper inventory, and legal files with the baseline. Add `references/development-verification.md` to the sorted manifest file list. Explicitly exclude repository-only `docs/` and `HERMES.md` from the package file-accounting prose in README/NOTICE; do not ship private project routing or break portable authoring references. Change the descriptive manifest `stage` from `runtime-acceptance-open` to `setup-recipe`; explain that it describes a recipe package, not tested live-team behavior. Set `SKILL.md` and `manifest.json` versions together to `1.1.5` after the coherent change is complete.
- [ ] **6. Prepare the launcher handoff without rollout.** Read the current external launcher, not only its historical snapshot. In the repository handoff document, identify contradictory setup obligations and provide a minimal English replacement entry that points to the canonical Maker, distinguishes setup/update/development triggers, and adds no second setup checklist. Preserve the known Maker path and the no-live-rollout boundary. Do not overwrite the installed launcher or another profile. Report that the actual installed entry remains unaligned until separately authorized replacement.
- [ ] **7. Verify the normal path and retained quality.** Trace every mandatory setup reference and conditional branch. Check at least: ordinary available-dependency setup; missing Hindsight service; already-correct central setting; conflicting target identity; interrupted setup with stale prose; existing-team file update. Record expected action and actual instruction location briefly in review evidence, not a new runtime record. A keyword scan is supporting evidence, not proof that a reference cannot reintroduce an obligation.
- [ ] **8. Run development checks and review the delta.** Run the existing full suite; check manifest file existence/uniqueness, relative links/anchors, package version equality, TAS, and `git diff --check`. Compare generated component/role contracts against the baseline. Reuse Phase 1 fixture evidence; rerun changed-path tests at the final source revision. Do not add a test framework or tests that merely duplicate documentation literals.
- [ ] **9. Commit and hand off.** Commit only Phase 2 files with `refactor: restrict Maker to setup and own-output verification`. Request Julia review on the same ticket with exact commit, checks, preserved contracts, and the external-launcher limitation. Do not declare installed teams updated.

### Concrete recipe decisions for step 2

| Existing recipe | Required change |
|---|---|
| Setup preflight | Keep target identities, resolved homes, dispatcher owner, supported required interfaces, and actual shared effects. Remove routine parser/source exploration and broad timeout/retry/rate-limit research. Do not inventory unrelated profiles without a concrete shared-effect need. |
| Project tools | Keep workspace/repository binding. Remove project toolchain installation/qualification from team setup. Leave later project preparation to an explicit project task. |
| Component sources | Reuse available established components and their known recipes. Keep provenance, full asset sets, licenses, and necessary local integration. Remove unconditional newest-upstream discovery. A missing common runtime is a prerequisite issue, not a download/repair mandate. |
| Hindsight | Keep service availability, bank ownership/create/reuse, provider activation and exact effective per-role bank/tag settings. Remove adapter-function inspection, SDK research, synthetic retain/recall/reflect/consolidation checks, and gates that require those experiments before completing setup. Preserve existing intended settings; do not change memory semantics. |
| Codex/helpers | Keep separate homes, real configuration/identity resolution, access availability, exact installed helper inventory, and model-limit compatibility. Remove required artifact generation, each-helper delegation, boundary probes, and retry/second-pass behavior tests. Do not weaken the roles' runtime reasoning policy. |
| Code analysis | Keep one selected integration, required skills/hooks/MCP, static cache binding and established connection/configuration readback. Remove artificial indexing, graph query, and incremental-update projects. Do not drop CBM subagents or Graphify supporting assets. |
| Mattermost | Keep planner-only identity, membership, exact channel/user/DM IDs, effective permissions, supported activation, and the genuine `/sethome` binding action/readback. Remove reply matrices, synthetic authorization-event experiments, and artificial wake chains. Preserve permission settings; do not replace them with allow-all. |
| Board/recovery | Keep correct dispatcher/board binding, effective `kanban.auto_decompose=false` under permitted administration, and bound recovery launcher delivery/readback. Use the known resolver recipe where necessary; do not research it anew. Remove fan-out experiments, test cards, and ordinary-setup instructions to repair existing task graphs. Runtime recovery remains in its existing role skill. |
| Central instruction-file protection | Accept the required effective value on an authorized supported management layer. Do not force a duplicate profile value or change central policy. Report genuine conflicts. |
| File updater | Preserve the operational dependency-decision gate even when changed recipes now remove tests. Keep file-only scope and existing runtime-migration boundaries. Do not relabel a clean merge as semantic approval. |

**Acceptance:** The ordinary package entry requires only necessary setup and own-output readbacks; no excluded research/behavior tests return through mandatory references, record fields, update instructions, or completion labels. Team assets and update contracts are preserved. The source package is reviewed; installed launcher/team changes remain explicitly unperformed.

## 5. Verification budget and known baseline gap

The planning-stage full suite did not complete: one invocation hit its 180-second command limit; a second hit the terminal tool's 420-second transport limit. Neither result is a completed pass. No test defect or cause was established, and no matching unittest process remained at the subsequent check.

Do not blindly repeat the same foreground full-suite invocation.
Use the existing suite with verbose output and a saved internal log. If it outlasts the synchronous tool window, use the standard tracked background terminal execution with completion notification; do not write a new runner, watchdog, cron, or test environment.
Inspect the last active test after a real stall or failure. Run only the relevant existing test to distinguish a known test/runtime prerequisite from a product regression. Preserve denial/skipped evidence; do not bypass guards or silently remove tests.
If required verification remains unavailable, return the exact missing evidence and blocker to Kirk. Do not start broad infrastructure repair or claim the phase complete. Kirk decides the smallest justified next step; changed customer scope still goes to Max.

The existing aggregate command remains:

```sh
python3 -B -m unittest discover -s references -p 'test_*.py' -v
git diff --check
```

Planning-document-only changes do not need another multi-minute aggregate run. Check their links, scope, Git diff, and approval state instead. This does not waive development tests for later package changes.

## 6. Approval, routing, and completion

- The accepted spec authorizes this plan's preparation, not implementation.
- Before tickets, commit the accepted plan/approval record and resolve the explicit project board and communication mapping. `HERMES.md` currently records them as unresolved; do not borrow a generated team's board or the active default board.
- Create only the two approved phase tickets for `scotty`, secured initially, with Phase 1 → Phase 2 as the exact parent chain. Use canonical workspace and the committed plan path/hash in both tickets.
- Read back routing, subscriptions where applicable, workspace, scope, and parent chain before release. Julia's same-card review completion gates Phase 2. Do not dispatch manually.
- Do not create a separate coding task for an external launcher rollout or existing-team update without its separate authorization.
- Report completion as reviewed Maker repository revision `1.1.5`, with preserved record/update contracts and the actual verification limits. Do not report a live-installed or behavior-qualified team.
- Keep the external launcher handoff available internally. Its unresolved activation is a clearly stated deployment boundary, not a fabricated completed change.

## 7. Plan self-review coverage

Spec sections 1–4 and 6 → Phase 2's setup boundary, concrete recipe decisions, verification split, and launcher handoff.
Spec section 5 → Phase 1's template/consumer contract and update round trip; Phase 2 preserves the operational gate.
Spec section 7 → both phases' existing checks plus Phase 2's semantic reference/scenario review.
Spec section 8 → one final package patch, no schema migration, and separate plan/rollout/publication gates.
Spec section 9 → source provenance preserved; historical investigation not rewritten.

No new product requirement, reduced team capability, or automatic delivery route is introduced by this plan.
