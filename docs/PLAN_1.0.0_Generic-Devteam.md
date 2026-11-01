# Generic Devteam — setup-only Maker implementation plan

> **Execution:** Scotty implements through Codex. Julia reviews each phase on the same ticket through `kanban_request_review(reviewer="julia")`. Kirk coordinates. Do not create separate review tickets, extra coding agents, or an additional LLM judge.

**Status:** Draft for Max's implementation approval. The original design specification is accepted. This draft includes Max's subsequent upfront-interview and post-trial cleanup requirements. No implementation or cleanup is released by this document.
**Goal:** Preserve the equipped team's capabilities and update safety while removing recurring research and behavioral qualification from ordinary setup.
**Architecture:** Keep the existing prose-driven Maker, templates, helpers, and file updater. Simplify the record without changing its consumer contract, then replace the normal setup/readback contract consistently across entry points and references. Keep development verification outside the normal setup path.
**Tech stack:** Markdown/TAS instructions, JSON manifest/private records, existing Python helpers and unittest fixtures, local Git.
**Workspace and existing repository:** `/home/joi/projects/generic-devteam`; no initialization, relocation, or restructuring.
**Spec:** [Design specification](specs/2026-11-01-maker-setup-scope-design.md), original accepted content in commit `0694e651df32dbe7d5187d6d4105fb2b91819b0c`, with Max's subsequent interview and deferred-cleanup additions in the current revision.
**Implementation baseline:** Maker `1.1.4`, code/package commit `a44d15e3aad77b891fa5c95ebeba49a780e4525e`; the planning commits do not change that package.
**Required working branch:** `fix/makerscope`, selected by Max and already containing the planning commits. Use this branch for planning updates, Phases 1–2, and the later authorized cleanup. Verify the branch before edits and commits. Do not switch back to `develop`, merge, or publish without a separate instruction.
**Plan version:** `1.0.0`, the first SemVer-named implementation plan in this repository. Do not renumber historical unversioned planning material.
**Target package version after Phase 2:** `1.1.5`, one PATCH for this coherent compatible recipe/documentation revision under `AGENTS.md`. Set it in both version fields at Phase 2 completion, not per intermediate commit. Assess the later cleanup version separately against the then-tested stand. If the starting package changes before execution, Kirk reconciles the baseline and version before work starts.

## 1. Global constraints

- Read `HERMES.md`, `AGENTS.md`, the accepted spec, and `references/tas-authoring-standard.md` before work. Apply TAS to every new or revised text in each phase. Use plain technical English for agent instructions; retain the user-facing language rule.
- Limit TAS authoring and review to the phase's own textual changes. Read unchanged context when needed to preserve meaning, but do not audit, translate, or rewrite unchanged text solely for TAS compliance. This restriction does not remove the separate setup-scope reference review required by this plan.
- Preserve three profiles, independent review, complete assigned skills/helpers, model and reasoning limits, Codex identity/homes, chosen code analysis, Hindsight role/bank configuration, communication permissions, and board/workspace bindings.
- Preserve role-template bytes, installed skill payloads, component assignments, render fields, and transforms unless a concrete setup backlink needs a minimal correction approved by Kirk within the accepted scope.
- Do not replace runtime roles' legitimate Git, task, approval, review, or security checks with weaker rules.
- Preserve existing update formats and legacy safeguards. Do not change `SCHEMA`, `copy-v1`, `bound-recovery-v1`, or the renderer compatibility policy.
- Prefer no production Python changes. If a consumer unexpectedly depends on removed prose, keep compatibility through a minimal correction and regression; do not redesign the updater.
- Do not add shared dependency installation, upgrade, repair, version-certification infrastructure, a team registry, a new state store, or a second installer.
- Do not change live profiles, private setup records, shared Hermes configuration, services, identities, credentials, or the installed default-profile launcher.
- Do not automatically run an actual team setup, model/delegation call, synthetic memory conversation, communication test matrix, or coding/review test card during implementation. Max's later practical setup trial is a separate human-controlled gate with its own confirmed target and action scope.
- Do not push, publish, deploy, deliver an archive, or restart running agents. Report the reviewed repository result; Max decides any later delivery or activation separately.
- Keep internal review evidence local or as durable card attachments. Do not put file paths in `artifacts`, `metadata.artifacts`, or automatically deliverable handoff text.
- Treat intermediate commits as revision work, not a Maker release ready for team installation. The coherent package result requires both phase reviews.
- Keep root `HERMES.md` and temporary planning material through Phases 1–2 and Max's practical trial. Do not perform final tree cleanup during the Maker rewrite. Final clean-clone portability belongs to the deferred Phase 3.

## 2. Review focus and owning phase

| Risk/input | Expected result | Verification owner |
|---|---|---|
| Shortened record, nested Codex process HOME, custom paths | Existing parsers retain exact values and correct source/target mappings | Phase 1 template-to-updater fixture and existing nested-home tests |
| Older installation, missing binding, local edits or conflict | Reuse confirmed evidence; preserve edits; block unsupported updates without claiming success | Phase 1 existing legacy, binding, conflict, and rollback tests |
| Missing prerequisite or conflicting/centrally managed setting | Report the affected setup item; accept an already correct effective value; no research, upgrade, or restriction bypass | Phase 2 instruction walkthrough |
| Development instructions reachable through a required reference or installed launcher | Ordinary package entry no longer assigns them; external launcher divergence remains explicit until separately changed | Phase 2 reference trace and launcher handoff |
| Correct files but untested agent behavior | Report setup-output verification, not behavioral qualification; no permanent pending gate for excluded experiments | Phase 2 completion/record consistency review |
| Foreseeable input postponed until installation | Complete that choice in the upfront interview; later questions need a new cause or a disclosed technical dependency | Phase 2 input inventory and interview walkthrough; Max's later trial |

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
- [ ] **3. Simplify the template.** Keep the single JSON block as the confirmed-data source. Keep short sections for authorizations, actual setup targets and availability/readbacks, progress/blocker/next action, and installation-baseline references. Reserve a compact readiness summary for the complete upfront dataset and any disclosed technically deferred actions; do not duplicate raw values or add a schema. Remove duplicate raw-value tables, behavioral experiment checklists, and mandatory evidence for helper calls, consolidation, interview quality, pipeline runs, or general platform limits. Do not store secrets.
- [ ] **4. Align record-writing and resume instructions.** Update the relevant parts of `setup.md` and `update.md` to use the retained structure. Distinguish missing confirmed input, actual target drift, and stale descriptive prose. Resume only the incomplete step. Keep `update_team.py init` after delivery/readback and recovery binding; preserve `installation.json`, personalized `baselines/<sha256>`, update proposals, backups, and result journals.
- [ ] **5. Verify the real contract.** Run the template regression and existing updater tests listed below. Confirm no edits to the production helper algorithms, role templates, or skill payloads. Review every new or revised text against TAS; keep that language review limited to this phase's diff. Check `git diff --check`.
- [ ] **6. Commit and hand off.** Commit only Phase 1 files with `refactor: simplify setup records while preserving update evidence`. Request Julia review on the same ticket. Do not install this intermediate revision into a team.

**Acceptance:** The revised record is parseable by unchanged consumers; exact setup values and installation/update metadata survive the synthetic round trip; local edits and conflict/legacy safeguards remain effective. Removed research checks are not retained as mandatory pending record items. All new and revised texts comply with TAS; no unrelated TAS cleanup is included.

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

- [ ] **1. Rewrite entry and sequence around the accepted outcome.** Define the five setup steps from spec section 4 and the upfront-input contract below. Inventory every user question in the setup and integration recipes. Move all foreseeable choices into a grouped preparation interview before any installation step. Resolve dependent questions within that preparation stage. Present the complete confirmed setup and disclosed later actions for the start decision. State the established dependencies and bounded missing-prerequisite response. Load only the chosen analysis branch; do not require both complete alternatives as work instructions.
- [ ] **2. Retain concrete bindings; remove recurring investigation.** Apply the decisions below to the existing recipes. Preserve command/configuration details that actually create the required state. Do not replace them with vague instructions to discover a working integration.
- [ ] **3. Split verification by actor and trigger.** Make `verification.md` the ordinary setup-output checklist. Move useful package/unit/recovery/updater regression instructions and explicitly commissioned behavioral qualification to `development-verification.md`. Link that file from the development section of README and the authoring context, not as required setup reading. Preserve historical research only if useful; do not create another research archive or per-setup audit ledger.
- [ ] **4. Reconcile completion, failure, and resume wording.** Use `Team configured; setup outputs verified` only when required setup outputs/readbacks and update baseline are complete. Name real incomplete bindings precisely. State excluded behavioral testing as outside scope, not an outstanding gate. Keep the actual update operation's `applied`, `skipped`, `failed`, unknown-baseline, and retained-file distinctions.
- [ ] **5. Preserve package identity and contents.** Compare component assignments, role fields, transforms, own skill trees, helper inventory, and legal files with the baseline. Add `references/development-verification.md` to the sorted manifest file list. Explicitly exclude repository-only `docs/` and `HERMES.md` from the package file-accounting prose in README/NOTICE; do not ship private project routing or break portable authoring references. Change the descriptive manifest `stage` from `runtime-acceptance-open` to `setup-recipe`; explain that it describes a recipe package, not tested live-team behavior. Set `SKILL.md` and `manifest.json` versions together to `1.1.5` after the coherent change is complete.
- [ ] **6. Prepare the launcher handoff without rollout.** Read the current external launcher, not only its historical snapshot. In the repository handoff document, identify contradictory setup obligations and provide a minimal English replacement entry that points to the canonical Maker, distinguishes setup/update/development triggers, and adds no second setup checklist. Preserve the known Maker path and the no-live-rollout boundary. Do not overwrite the installed launcher or another profile. Report that the actual installed entry remains unaligned until separately authorized replacement.
- [ ] **7. Verify the normal path and retained quality.** Trace every mandatory setup reference and conditional branch. Check at least: ordinary available-dependency setup; missing Hindsight service; already-correct central setting; conflicting target identity; interrupted setup with stale prose; existing-team file update. Walk the input flow with an omitted profile name, an analysis-dependent choice, an already-confirmed Git identity, a later-generated object ID, and a protected login that requires the new home. Confirm that all knowable choices block installation until resolved, confirmed answers are not asked again, generated IDs are read back, and unavoidable later interactions were disclosed. Record expected action and actual instruction location briefly in review evidence, not a new runtime record. A keyword scan is supporting evidence, not proof that a reference cannot reintroduce an obligation.
- [ ] **8. Run development checks and review the delta.** Run the existing full suite; check manifest file existence/uniqueness, relative links/anchors, package version equality, and `git diff --check`. Review every new or revised text against TAS, limited to this phase's diff; do not perform a whole-repository language audit. Compare generated component/role contracts against the baseline. Reuse Phase 1 fixture evidence; rerun changed-path tests at the final source revision. Do not add a test framework or tests that merely duplicate documentation literals.
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

**Acceptance:** The ordinary package entry requires only necessary setup and own-output readbacks; no excluded research/behavior tests return through mandatory references, record fields, update instructions, or completion labels. All foreseeable user choices are resolved before installation starts. Remaining interaction is limited to new issues/decisions or disclosed technically deferred actions. Team assets and update contracts are preserved. All new and revised texts comply with TAS; no unrelated TAS cleanup is included. The source package is reviewed; installed launcher/team changes remain explicitly unperformed. Pause for Max's practical trial; do not start cleanup.

### Upfront-input contract

Use one preparation stage with grouped independent questions and only necessary dependent follow-ups. Do not require one giant form, a new interview skill dependency, or a general product-planning interview.
Use the existing `confirmed_values`/`confirmed_bindings` dataset and existing pre-profile record handoff. Do not create a new registry or wizard framework.

| Input group | Resolve before installation |
|---|---|
| Project and roles | Project/workspace, repository boundaries, display names, distinct technical profile IDs, intended role homes where selectable |
| Models and analysis | Hermes/Codex provider/model choices, fixed/default/maximum reasoning values, helper-pin conflicts, exactly one analysis alternative |
| Codex identity | Confirmed `user.name`/`user.email`, authorized identity reuse and protected access route; do not infer consent from a discovered identity |
| Shared objects | Intended board/bank names, existing service endpoints, create-versus-reuse decisions and ownership |
| Communication | Intended server, bot identity, user/channel permissions and existing channel/DM IDs where available; creation intent for objects not yet present |
| Execution scope | Concrete writes, shared effects, activation and necessary external actions; protected credential preparation where technically possible |

Read discoverable facts through established authorized read-only interfaces. Ask for actual user decisions, not values the Maker can determine.
Do not create profiles, install assets, create bank/board objects, or activate integrations while a foreseeable choice is missing.
Store confirmed nonsecret values once and reuse them through resume.
Show a concise final parameter/change summary before starting. Known instructions embedded in later recipes must consume that dataset, not reopen the interview.
Read generated IDs and resolved paths after their authorized creation. They are outputs, not missing customer decisions.
Disclose any protected login, native approval, or `/sethome` action that requires a created target. Keep it at the necessary technical point; never collect secrets in chat or bypass approval to claim an unattended run.
After installation starts, a question needs a newly observed conflict/failure, a genuinely newly knowable decision, a user-requested scope change, or a disclosed deferred action. A late foreseeable choice is a defect to fix in the recipe.

## 4A. Human gate — Max's practical setup trial

**Predecessor:** Julia approves Phases 1 and 2 at the exact trial revision.
**Owner:** Max chooses when and where to try the revised Maker. Kirk records feedback; no automatic installation or test ticket is dispatched.
**Goal:** Observe how long setup takes, how much attention it needs, and whether the resulting setup meets the intended scope before cleaning the repository.

- Keep the current planning files and `HERMES.md` available. Use the README entry rather than the old installed launcher. Distinguish temporary Maker-development context from the target team's values; do not claim the final clean-clone deliverable yet.
- Before any assisted real run, identify the exact reviewed source commit, intended target and permissions. This planning request does not authorize arbitrary account, service, or profile changes now.
- Capture start/end, total elapsed time, user-wait periods where observable, actual setup result, and later questions with their cause. Use the existing session/setup evidence and a brief summary; no benchmark framework or new permanent Maker test duty.
- Treat a late foreseeable configuration question as feedback on this revision. Distinguish it from an unexpected failure or a disclosed authentication action.
- If Max requests corrections, update the affected phase scope/baseline and obtain review before a new trial. Do not rerun unchanged work by default.
- Wait for Max's explicit decision to move to cleanup. Trial execution or Phase 2 review alone is not cleanup approval.

## 4B. Phase 3 — deferred final repository cleanup

**Status:** Planned later stage, not released with Phases 1–2. Finalize its exact file delta after the practical trial. Do not create an automatically runnable successor now.
**Predecessors:** Reviewed implementation, completed practical trial/feedback disposition, and Max's separate cleanup authorization.
**Goal:** A current repository tree usable through README from another checkout, without this undertaking's local instructions or temporary planning artifacts.
**Repository/branch:** `/home/joi/projects/generic-devteam`, `fix/makerscope`.
**Removal candidates:** `HERMES.md`, `docs/PLAN_1.0.0_Generic-Devteam.md`, `docs/specs/2026-11-01-maker-setup-scope-design.md`, `docs/operations/maker-launcher-handoff.md`, and explicitly identified temporary artifacts created only for this revision. Preserve unrelated material unless separately classified and approved.
**Possible reference corrections:** `README.md`, `AGENTS.md`, `NOTICE.md`, `manifest.json`, and changed Maker references, only where removal breaks links or leaves local instructions. Keep portable functional authoring rules and the required TAS standard.

1. Kirk records the exact tested source and final removal list in the separately released cleanup handoff before the self-referencing planning/context files are removed. Preserve the historical plan commit as the review baseline.
2. Scotty removes approved temporary files from the tracked tree through a normal Git commit. Do not merely hide them in the manifest or copy them to another directory inside the repository. Do not rewrite Git history or remove commits needed to reconstruct older update baselines.
3. Preserve functional recipes, roles, assets, updater/binder/renderer, useful maintained regression tests, legal files, and all existing live-team/private update state. Development use alone is not a deletion criterion.
4. Check the cleaned README entry in a fresh local checkout at a different path, without the default-profile launcher or this project's historical `HERMES.md`. Trace required files and links; confirm that no local path, branch, person, or board binding is imposed on the new team. Do not automatically install another team for this portability check.
5. Verify affected package/file-accounting and update-source reconstruction. Keep TAS review limited to new/revised text. Determine any package patch under the existing SemVer policy against the then-current tested release; do not invent or overwrite a historical version.
6. Commit with `chore: remove temporary Maker revision context` and request Julia review on the same cleanup ticket. No push, release, or installed-launcher change follows implicitly.

**Acceptance:** The approved temporary artifacts are absent from the final tracked tree; the README-driven entry and necessary update history remain usable; no local development binding is required for a new team. The exact cleanup commit is independently reviewed. Report historical Git presence separately from absence in the current tree.

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
- After implementation approval, create only the two Phase 1–2 tickets for `scotty`, secured initially, with Phase 1 → Phase 2 as the exact parent chain. Put the canonical workspace, required branch `fix/makerscope`, committed plan path/hash, and change-scoped TAS requirement in both tickets. Require Julia to review the phase's new and revised texts against TAS without expanding into unchanged text.
- Read back routing, subscriptions where applicable, workspace, scope, and parent chain before release. Julia's same-card review completion gates Phase 2. Do not dispatch manually.
- Do not create a separate coding task for an external launcher rollout or existing-team update without its separate authorization.
- Report Phase 2 completion as reviewed Maker repository revision `1.1.5`, ready for Max's practical trial, with preserved record/update contracts and actual verification limits. Do not report final cleanup, a live-installed team, or behavioral qualification as complete.
- Do not make Phase 3 an automatic successor of Phase 2. Create/release its scoped ticket only after Max's trial feedback and separate cleanup authorization; preserve the approved source handoff outside files scheduled for removal.
- Keep the external launcher handoff available internally. Its unresolved activation is a clearly stated deployment boundary, not a fabricated completed change.

## 7. Plan self-review coverage

Spec sections 1–4 and 6 → Phase 2's setup boundary, concrete recipe decisions, verification split, and launcher handoff.
The added upfront-input contract → Phase 1 record readiness and Phase 2 interview/recipe walkthrough.
The added trial-before-cleanup sequence → section 4A's human gate and section 4B's deferred Phase 3.
Spec section 5 → Phase 1's template/consumer contract and update round trip; Phase 2 preserves the operational gate.
Spec section 7 → both phases' existing checks plus Phase 2's semantic reference/scenario review.
Spec section 8 → one final package patch, no schema migration, and separate plan/rollout/publication gates.
Spec section 9 → source provenance preserved; historical investigation not rewritten.

The upfront interview and deferred cleanup are Max's requested additions. No reduced team capability, automatic trial, automatic cleanup release, or automatic delivery route is introduced.
