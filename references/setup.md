# Guided native target setup

Execute this recipe only for an authorized target setup.
Use established supported interfaces and known recipes, not recurring parser, source, loader, or SDK investigation.
Use confirmed nonsecret values as data; never interpolate raw user text as shell code.
Use English for development communication and artifacts. Preserve exact identifiers, quotations, errors, and deliberately localized product text.

## 1. Inventory before changes

1. Resolve the existing account, Hermes revision/distribution, terminal backend, native profile inventory, and actual homes.
   Check both directories and registration; an existing unmarked directory is a collision.
2. Identify the existing gateway/multi-profile owner, Planner adapter, dispatcher home/DB, and notifier.
   Read effective `kanban.auto_decompose` through the [known resolver](kanban-block-triage-escalation.md#set-the-homes-and-the-readback-that-counts).
   Require `false` before release; scope authorized changes to the owner and selected team profiles.
3. Check required interface and dependency availability through established read-only status/configuration paths.
   Do not qualify the project's toolchain or investigate general timeout, retry, or rate-limit behavior.
   A missing Hindsight service or Hermes distribution prerequisite requires operator action; Maker does not install or repair them.
   Inspect Codex and the selected analysis runtime's paths, versions, owners and shared consumers before proposing a first installation or change.
   Check the Codex shell sandbox before any write, because the independent Review passes depend on it.
   Run `bwrap --unshare-user --ro-bind / / --dev /dev -- /bin/true` and require exit status 0.
   On Ubuntu 24.04, `kernel.apparmor_restrict_unprivileged_userns=1` blocks `/usr/bin/bwrap` until an AppArmor profile grants `userns`, as the packaged `linux-sandbox` profile does.
   A blocked sandbox is an operator prerequisite: report the missing capability, and keep Codex sandbox and approval settings unchanged.
   Read each independent asset's exact `source_revision` from the manifest without a new latest-version search.
   Keep required pins separate from installed runtime versions and operational permission.
4. Identify concrete shared bootstrap/PM effects before invoking CLI or adding plugins.
   Even help/bootstrap can sync dependencies; absolute plugin paths can alter shared PM inputs.
   Inspect other profiles only when a concrete shared effect requires it.
   Preserve unrelated profiles and shared runtimes; obtain the necessary scope authorization before those effects.
5. Check your own wrapper or a local adaptation under [Maker wrapper](main-agent-wrapper.md).

## 2. Complete upfront preparation

Read available facts through authorized established interfaces.
Reuse session answers, `clarify` results, confirmed JSON, and the pre-profile handoff.
Ask independent missing decisions together, then resolve dependent follow-ups within this same preparation stage.
Do not create profiles, files, bank/board objects, install assets, or activate integrations while any foreseeable choice is missing.
Do not require a new interview skill or product-planning workshop.

| Group | Complete before starting |
|---|---|
| Project and roles | Separate project name and canonical absolute workspace; repository boundaries or confirmed absence; display names for Planner (`PLANER_NAME`), Coder (`CODER_NAME`), Reviewer (`REVIEWER_NAME`); selectable homes and collision resolutions |
| Models and analysis | Combined default set below or confirmed overrides; actual native model/provider IDs and supported reasoning; availability of original VoltAgent model/reasoning settings at the manifest revision; exactly one of CBM or Graphify; repository/corpus scope, roots, cache/output paths and any optional watcher intent |
| Codex identity | Explicitly authorized `user.name`/`user.email` reuse, provenance, access method and protected login route; discovery alone is not consent |
| Shared objects | Existing service endpoints; intended board/bank names; create versus authorized reuse and ownership |
| Communication | Mattermost server/team, intended Planner bot, human and any additional authorized users, allowed project channel, channel type and DM participants; existing IDs or explicit creation intent |
| Execution scope | Exact local writes, profile assets, shared PM/configuration effects, external identity actions, and activation; protected access preparation where possible |

Include complete pinned plugin packages and legal files in the preparation inventory.
Check runtime/asset compatibility before accepting the setup scope.
If Codex or the selected analysis runtime is absent, disclose its exact first-installation release/source, paths and effects in that scope.
The accepted upfront scope covers that first installation without repetitive per-component version questions.
Preserve existing/shared installations; disclose and obtain explicit approval for a concrete required change rather than silently upgrading during new team setup.
Plugin admission can change shared Hermes PM dependencies; obtain that shared scope before invoking bootstrap or native installation.
Keep Hermes core, distribution skills and the Hindsight service outside Maker installation/update/repair scope.
If a pin conflicts with a preserved runtime, report the exact mismatch and obtain the required update/defer decision before dependent writes.

Resolve workspace separately from project name; do not derive a path or move an existing repository.
Keep `PROJECT_NAME` as a single segment without slash, backslash, or traversal.
Bind the confirmed canonical workspace as `PROJECT_DIR`, native `terminal.cwd`, and board default workspace.
Save `REPOSITORY_ROOTS` as single-line text with separate planning and implementation assignments.
Preserve nested checkouts and multiple roots; do not initialize Git or install project tools.
Check existing project instructions and native profile/board bindings for contradictions before creating anything.

### New profile IDs

Keep display names unchanged. For derivation only, trim whitespace, lowercase, transliterate German umlauts to `ae`/`oe`/`ue` and `ß` to `ss`,
remove decomposable accent marks, replace remaining runs outside `[a-z0-9_-]` with `-`, strip leading/trailing separators, and limit to 64 characters.
Validate the candidate against `[a-z0-9][a-z0-9_-]{0,63}`, reserved names, target ownership, existing directories/registration, and collisions across selected roles.
Examples: `Kirk` = `kirk`, `Julia` = `julia`, `Jörg` = `joerg`, `Jean Luc` = `jean-luc`.
Show valid derived IDs in the final summary, without separate ID questions.
For an empty/unusable candidate, same-normalized-name collision, reserved name, or existing-profile conflict, obtain one explicit resolution.
Do not silently prefix, suffix, rename, delete, or clone.
Preserve existing confirmed IDs on resume and update.
Compare canonical homes, symlinks, SOUL/skill targets, Codex state, bank/board and channel ownership before writes.
Reuse only objects whose native identity and ownership agree with the confirmed setup evidence.

### Offer model defaults once

| Consumer | Model family | Native reasoning policy |
|---|---|---|
| Planner | Sol | Fixed high (`PLANNER_REASONING`) |
| Hermes Coder | Sol | Fixed medium (`CODER_REASONING`) |
| Reviewer | Sol | Default medium, maximum high (`ROLE_REASONING_DEFAULT` / `ROLE_REASONING_HIGH`) |
| Team-Codex | Sol | Default medium, maximum high (`CODEX_REASONING_DEFAULT` / `CODEX_REASONING_MAX`) |

Offer this complete set once; accepting it confirms its limits without separate repeated maximum questions.
Resolve Sol separately to the actual supported native model/provider identifier for each target through established availability/configuration interfaces.
`sol-medium` and `sol-high` describe model/reasoning combinations; never submit them as guessed native model IDs.
Record the actual Codex model ID as `CODEX_MODEL` and reasoning separately.
If the selected model, provider, or reasoning level is unavailable or incompatible, resolve that conflict during preparation.
Preserve accepted overrides. Do not silently change provider/model or choose the highest supported level.
Use the six VoltAgent specialists' original model and reasoning settings under [the helper recipe](integrations.md#codex-agents).
Resolve their availability and any conflicting customer limits before setup; preserve the pinned originals.
The Team-Codex model and default/maximum matrix govern the main process, not these six specialists.
Validate defaults against maxima using the chosen target's supported semantics, including nonstandard or nonconfigurable reasoning.

Keep Hermes Coder fixed reasoning separate from task-selected Codex reasoning.
Below HIGH complexity and HIGH impact, Codex uses its default.
Either HIGH permits up to the maximum; both HIGH require the maximum.
Keep bounded retry/review escalation and unchanged model/provider rules in the Coder SOUL.
No per-task customer approval is needed within the confirmed range.
Do not add a Hermes-Coder maximum, technical maximum setting, render field, or migration.

### Final summary and start decision

Store confirmed nonsecret values once in the existing setup dataset, then transfer them unchanged to the private Planner record after creation.
Before that home exists, use the existing pre-profile handoff on interruption; do not create another store.
Present the complete parameters, derived IDs, target homes, create/reuse choices, models/limits, Git identity, analysis settings, communication permissions, concrete writes, shared effects, and activation scope.
Include the template-based role personalization in preparation acceptance; generated native IDs are substituted from readbacks without reopening agreed role rules.
Disclose protected logins requiring the new home, native `/hooks` approvals after configuration, and the genuine Planner DM `/sethome` action after role delivery/adapter activation.
State each action's reason and execution point. Prepare protected credentials earlier where supported; never collect secrets in chat or JSON.
Obtain the start decision only after all foreseeable decisions are complete.
Later questions require a new conflict/failure, newly knowable decision, user scope change, or disclosed deferred interaction.
Generated object IDs and resolved homes are readback outputs; do not ask the user to invent or repeat them.
Later recipe steps consume this dataset without reopening confirmed choices.

## 3. Fresh profiles, confirmed models

`PROFILE`/`DESCRIPTION` each stand for a confirmed new technical role
and nonsecret description. Proceed only after collision check and activation approval:

```sh
hermes profile create "$PROFILE" --no-alias --description "$DESCRIPTION"
hermes profile show "$PROFILE"
hermes -p "$PROFILE" config set terminal.cwd "$PROJECT_DIR"
hermes -p "$PROFILE" config set model.provider "$PROVIDER"
hermes -p "$PROFILE" config set model.default "$MODEL"
hermes -p "$PROFILE" config set agent.reasoning_effort "$EFFORT"
hermes -p "$PROFILE" config set kanban.auto_subscribe_on_create false
hermes -p "$PROFILE" config get terminal.cwd
hermes -p "$PROFILE" config get model.provider
hermes -p "$PROFILE" config get model.default
hermes -p "$PROFILE" config get agent.reasoning_effort
hermes -p "$PROFILE" config get kanban.auto_subscribe_on_create
hermes -p "$PROFILE" config get security.protected_instruction_files
```

Apply these steps to Planner, Coder and Reviewer using their confirmed model/provider values.
Disable the automatic skill-review trigger only in the Planner profile:

```sh
hermes -p "$PLANNER" config set skills.creation_nudge_interval 0
hermes -p "$PLANNER" config get skills.creation_nudge_interval
```

Use `PLANNER_REASONING`, `CODER_REASONING` or `ROLE_REASONING_DEFAULT` as the respective `EFFORT`.
Planner and Hermes Coder retain their fixed levels.
Require effective `security.protected_instruction_files: false` for each selected role.
Accept an existing centrally managed effective `false` without a duplicate profile entry.
If needed and authorized, set the profile-local value through the supported native configuration path:

```sh
hermes -p "$PROFILE" config set security.protected_instruction_files false
hermes -p "$PROFILE" config get security.protected_instruction_files
```

Record the effective value and its management source.
Do not alter central policy or bypass an administrative restriction; report a genuine conflict.

Set reasoning only with confirmed support; otherwise log the missing capability
or the deliberately inapplicable value. Create uses model seeding
and can inform the running multiplexer. Check inherited provider/endpoint
definitions and set the intended route deliberately; no clone and no credential
copy. No `--no-skills`: required base skills must be fully present.
Record the **actually resolved profile home**, not a computed
default path. Use it for all subsequent targets. Immediately after
confirmed planner creation, start the private `devteam/setup.md` from the
[record template](../templates/setup-record.md) (directory 0700, file 0600);
log further changes continuously, not only after all integrations.

Check the actual activation state immediately after create and again on resume:
if the planner profile is already hot-admitted, record this early multiplexer effect in the
setup record; do not report section 7 as the start of activation.
Until complete accepted role/skill files and native bindings plus their
effective loading exist, trigger no home/dialog operation or task work.
If this boundary cannot be held in the existing owner, stop setup
and clarify an approved profile-scoped native path; do not switch off other profiles
globally. Before later messages, prove the new roles and the effective adapter routing
again, also for the already served planner.

Read back only relevant nonsecret fields and effective override sources.
Check environment/YAML, session/per-model/CLI overrides, fallbacks and required helper routes through established interfaces.
Use the correct native profile for protected login and model configuration readback.
A stored key or warning alone does not establish its effective value.

### Planner Kanban tools

Kanban is default-off; board configuration and a working `hermes kanban` CLI do not enable model tools.
Enable it explicitly in the confirmed Planner profile for all three entry surfaces below.
Desktop/TUI use `cli`; Mattermost uses `mattermost`; OpenAI-compatible WebUI calls use `api_server`.
Before enabling, capture each platform's native tool selection and the saved `platform_toolsets`, root `toolsets`, and `agent.disabled_toolsets`.
Preserve unrelated enabled and disabled tools, including MCP selections and global suppression entries.
If native enable would broaden unrelated permissions, such as clearing a `no_mcp` sentinel, stop for a supported, scoped resolution.
Do not replace `platform_toolsets` or root `toolsets` with a Kanban-only list.

```sh
hermes -p "$PLANNER" tools list --platform cli
hermes -p "$PLANNER" tools list --platform mattermost
hermes -p "$PLANNER" tools list --platform api_server
hermes -p "$PLANNER" config get platform_toolsets
hermes -p "$PLANNER" config get toolsets
hermes -p "$PLANNER" config get agent.disabled_toolsets
hermes -p "$PLANNER" tools enable kanban --platform cli
hermes -p "$PLANNER" tools enable kanban --platform mattermost
hermes -p "$PLANNER" tools enable kanban --platform api_server
hermes -p "$PLANNER" tools list --platform cli
hermes -p "$PLANNER" tools list --platform mattermost
hermes -p "$PLANNER" tools list --platform api_server
hermes -p "$PLANNER" config get platform_toolsets
hermes -p "$PLANNER" config get toolsets
hermes -p "$PLANNER" config get agent.disabled_toolsets
```

Require `kanban` enabled without stripping warnings on every listed platform; compare the complete before/after selections and suppression entries.
Resolve conflicting session/tool-selection overrides before claiming availability in that context.
Record readbacks in the existing private setup record; keep the binding incomplete if required availability or preservation fails.
These readbacks establish configuration, not adoption by a running conversation; do not start model calls, tasks, or service/session restarts.
Keep native Kanban guards, the single active task, and the fixed independent Reviewer unchanged.

## 4. Own board and Team-Codex

Only when no own board exists and identity is confirmed:

```sh
hermes kanban boards create "$BOARD" --name "$PROJECT_NAME" --default-workdir "$PROJECT_DIR"
hermes kanban boards list --json
```

Compare board ID, name, and default workspace. Store the readback
board identifier identically as `BOARD` and `KANBAN_BOARD_NAME`, with evidence in the record.
Every later operation carries
`--board "$BOARD"`; no global board switch. Repository, branch, and
plan revision are bound anew for each task, not invented in setup.

Bind `devteam/codex-home` and `devteam/user-home` inside the actual Coder home through [Team-Codex](integrations.md#team-codex).
For CBM, bind the canonical account cache as a literal in the team MCP TOML `env` before hook approval under [Code analysis](code-analysis.md#codebase-memory).
Record the actual Codex binary and both homes for configuration readback.
Deliver/configure the complete original components for the chosen analysis branch only.
Read back analysis targets, assets, runtime binding and licenses for Planner, Coder, Reviewer and Team-Codex.
For CBM include its complete native Codex subagents alongside the six VoltAgent helpers.
Bind authorized repository/MCP roots without indexing or querying product data.
Do not create an artificial test workspace or switch analysis alternatives silently.

## 5. Hindsight and Mattermost

Use [Hindsight](integrations.md#hindsight) for every role with the same confirmed new or authorized reused bank on the existing service.
Use [Mattermost](integrations.md#mattermost) only in the Planner profile.
Consume the preparation dataset for identity, membership, permissions and existing IDs.
Read back generated channel/DM IDs from actual metadata.
Defer Mattermost step 8 until complete accepted role files, bindings, and adapter routing are verified in section 7.
Do not place communication credentials or targets in shared project instructions or role SOULs.

## 6. Own skills, roles, and text personalization

Before role acceptance, deliver complete original [grill-me, grilling, domain-modeling, and to-questionnaire](integrations.md#grill-me) trees to the Planner alongside [Superpowers](integrations.md#superpowers).
All four are fixed Planner equipment; record complete source/target checks privately.
If any required tree or companion is unavailable, withhold the dependent Planner output and report the missing asset.

Continue the private record from [setup-record.md](../templates/setup-record.md)
at `<actual planner home>/devteam/setup.md` after Planner creation.
Use directory mode 0700 and file mode 0600 outside the product project, Git, and Maker tree.
Do not overwrite an existing record without reconciling its confirmed data and actual targets.
Record authorizations, complete upfront dataset readiness, and disclosed technically deferred actions.
For each completed step, record the native identity or exact own file path, previous state/hash,
verified readback, and next prerequisite.
Keep component source, revision, license, and complete file evidence in the target-readback section.
Compare every assigned upstream asset with its manifest `source_revision`, complete file set and legal files; record required and observed sources separately.
Record compatible runtime reuse separately from pinned asset delivery; unknown provenance is not a pristine baseline.
Keep progress, blockers, and installation/update evidence in their respective sections.
Do not add behavioral or research checks as record completion gates.

Store confirmed raw values losslessly in the template's single `json` block.
Use `confirmed_values` for confirmed setup values and `confirmed_bindings` for resolved technical bindings.
Preserve all existing keys/types, including native-only model/reasoning values and role/recovery bindings.
Do not recover raw values from prose or Markdown tables.
Do not invent missing values or store secrets.
The following pure Python fragment generates text from `record_template_text`
(use the existing record on resume):

```python
import json
record_head, record_json = record_template_text.split("```json\n", 1)
_, record_tail = record_json.split("\n```", 1)
record_text = record_head + "```json\n" + json.dumps(
    {"confirmed_values": confirmed_values, "confirmed_bindings": confirmed_bindings},
    ensure_ascii=True, indent=2,
) + "\n```" + record_tail
```

Write `record_text` only to the confirmed own record target during an authorized setup.
Read back its exact bytes as `record_readback_text`.
Use the same pure fragment for readback and resume:

```python
import json
record_data = json.loads(record_readback_text.split("```json\n", 1)[1].split("\n```", 1)[0])
confirmed_values = record_data["confirmed_values"]
confirmed_bindings = record_data["confirmed_bindings"]
```

Compare the parsed values with the confirmed dataset and, on resume, the relevant native objects.
Stop the affected step for incomplete/invalid JSON, missing required confirmed input, or actual target drift.
Resolve missing input or drift before rendering or writing.
If only descriptive prose is stale, correct it from readbacks without repeating confirmed choices or creates.
Use these fragments for the confirmed dataset; do not run synthetic development regressions per setup.

1. Copy the **complete own skill tree** from `skills/` into `<role home>/skills/<name>/`
   according to the [source and role matrix](upstream-sources.md#bundled-components); Team-Codex gets
   `screenshot-to-code` and `diagnosing-bugs` in its process HOME under `.agents/skills/`.
   Apply the [diagnosis delivery recipe](integrations.md#diagnosing-bugs) for collision checks, complete bytes, and native discovery before role personalization.
   Deliver Planner-only `prototype` through [its recipe](integrations.md#prototype) before personalizing its dependent SOUL clauses.
   Keep all skill names and bytes unchanged except the recovery launcher.
   Bind that launcher through the Maker step below after copying the full tree.
   Licenses, notices, and references belong to it. No discovery in the source profile.
2. Read back the native Hermes/Codex settings, permitted limits, and helper routes against the preparation dataset.
   Compare the six VoltAgent TOMLs byte-for-byte with the manifest revision, including their original model and reasoning settings.
   Record configuration sources, authorization and actual readbacks privately.
   Keep the native Codex model ID outside role render fields.
   Verify Caveman source, installed trees, autoload, and native skill discovery/loading through [the writing-skill recipe](integrations.md#caveman).
   Bind only the chosen [analysis branch](code-analysis.md) for all assigned consumers; record roots and the installed operational update reference.
3. Use the pure text path for role personalization:
   [references/render_text.py](render_text.py). It reads/writes no files,
   loads no runtime, and has no CLI entry point. Load the module in the approved
   target setup through the absolute path of the reviewed Maker package (e.g.
   `importlib.util.spec_from_file_location`), not from a foreign same-named
   module on the search path. Read the templates with the file tool in UTF-8 and pass strings:

   ```python
   own_name = {"planner": "PLANER_NAME", "coder": "CODER_NAME", "reviewer": "REVIEWER_NAME"}[role]
   role_source = {**confirmed_values, "ROLE_NAME": confirmed_values[own_name]}
   fields = role_fields(role_template_text, role)
   if fields != set(role_manifest["render_fields"]):
       raise ValueError("Vorlage und deklarierte Rollenfelder widersprechen sich")
   missing = fields - role_source.keys()
   if missing:
       raise ValueError("Missing confirmed role bindings: " + ", ".join(sorted(missing)))
   role_values = {field: role_source[field] for field in fields}
   soul_text = render_role(role_template_text, role_values, role)
   ```

   Use the confirmed raw names, project, bank, board, profile IDs, and reasoning render values from `confirmed_values`.
   Include `PROJECT_DIR` and `REPOSITORY_ROOTS` for the Planner.
   Include `PLANNER_PROFILE` for the Coder.
   Check `PLANNER_PROFILE` against `confirmed_bindings.roles.planner.id` before rendering.
   Do not pass fixed Planner/Hermes-Coder reasoning or the Codex model ID as role fields.
   `role_manifest` is the matching entry from `role_templates`. Missing values
   stop the output; no empty defaults and no invented new IDs.
   `ROLE_NAME` always matches the own display name, never the technical ID.
   `role` is `planner`, `coder`, or `reviewer`. `confirmed_bindings` documents
   the actually resolved target values in the private record.
   Do not generate a separate runtime configuration file from these values.
   Render the role bindings through the existing SOUL templates.
   Bind the recovery launcher through the Maker step below.
   Communication values stay with the planner. Use technical
   values unchanged as data, not the escaped Markdown rendering as shell values.
4. The text path validates the [role field contract](native-workflow.md#2-personalize-role-souls): nonempty
   single-line raw values, names at most 120 characters, no control/format characters,
   template braces, indentation, backticks, backslashes, or fence breakouts.
   It replaces all matching multiple occurrences exactly in one pass, without
   recursive evaluation. Normal Markdown is escaped; inline code and fenced
   process/example text receive raw validated values, no Markdown backslashes
   in native IDs, bank, or path. Unknown, missing,
   additional, or damaged fields are errors. All non-placeholder bytes
   stay unchanged; append no additional persona or process rewrite.
5. Use the role personalization accepted during preparation.
   Compare exact rendered output with that scope, then write `soul_text` only to the confirmed role home `SOUL.md`.
   Ask again only for a newly observed conflict or scope change.
   Recheck target ownership immediately before writing with file tools.
   Do not use shell interpolation or recursive global replacement.
   Replace only the compared neutral SOUL created for this setup; stop for foreign or concurrently changed content.
6. Read back every target: exact role mapping, complete output, no leftover fields,
   byte-identical agreement with `soul_text`, unchanged
   non-placeholder bytes of each role, no communication values in Coder/Reviewer,
   role/project/bank/board values and technical IDs against the record,
   effective native configuration, and logged restrictions. Compare
   skill file set and bytes completely with the source.
   Compare the recovery launcher against its bound Maker output instead of the generic template.
   Read back the Planner's `grilling` load requirement, interview precedence, and separate plan acceptance.
   Read back the Planner's conditional `domain-modeling` load and authorized document boundaries, vocabulary-only glossary, proposed ADR status, and existing plan gate.
   Verify all three original skill trees and complete companions in the Planner home; Maker references alone do not deliver them.
   Read back the Coder SOUL's default/max values and process binding.
   Read back the Coder's `$diagnosing-bugs` routing and original-evidence validation under [the diagnosis recipe](integrations.md#diagnosing-bugs).
   Read back every role's Caveman load requirement and persisted-prose scope.
   Read back the Reviewer's `caveman-review` trigger and preserved review procedure.
   Read back the Coder SOUL process binding, per-task `$caveman` clause, and scope/clarity propagation, including restart/resume.
   Record the installed path and exact readback. Verify configured modes without a synthetic worker experiment.
   Verify the selected analysis integration, complete original skills and native activation for Planner, Coder, Reviewer and Team-Codex.
   Do not add a second alternative or leave only a Maker reference.
   Before home/dialog/task work, read the loader/context boundary at the target and prove
   **complete effective SOUL loading** per role; length and file existence do not suffice.
   Stop at truncation; do not silently reduce role obligations.

### Bind the planner recovery invocation

The Maker owns recovery binding and launcher generation.
Copy the complete `brownfield-feature-planning` skill tree.
Keep `scripts/recover_triage.py` unchanged.
Record `python`, `script`, `db` and `planner_profile` under `confirmed_bindings.triage_recovery` in the private setup JSON.
Use the verified dispatcher interpreter for `python`.
Use the installed planner skill path for `script`.
Use the existing dispatcher DB's canonical absolute path for `db`.
Use the confirmed technical planner ID from `confirmed_bindings.roles.planner.id` for `planner_profile`.
Check the DB against the confirmed board identity and dispatcher resolver.
Reuse the existing confirmed setup values without another interview.
If an existing team's record lacks this binding, resolve it from its confirmed identities and current dispatcher configuration.
Stop if those sources disagree.
Run the Maker binder after copying the skill tree:

```sh
python3 -B references/bind_recovery.py --home /actual/planner-home
```

The binder reads the existing private setup JSON and writes `skills/brownfield-feature-planning/scripts/recover-triage` in that planner home with mode 0700.
It binds the interpreter, generic script, dispatcher DB and planner ID with shell-safe quoting.
It accepts only the task ID at runtime.
Compare the installed bytes against `bind_recovery.render_launcher` with the confirmed binding.
Record the generated file hash and shell-quoted installed launcher path in `setup.md` as Maker audit evidence.
Keep the task ID separate from that fixed command.
Deliver the callable launcher inside the planner skill tree before recording the installation.
Do not assign setup-record reads, variable collection or configuration generation to the planner.
Do not personalize the Python source through the SOUL renderer.
Do not create a recovery test card for each setup.
Follow the installed recovery reference's approval and API checks before any later invocation.

<a id="7-einzelprüfungen-und-wake-vor-ticketfreigabe"></a>
## 7. Output verification and communication binding

After complete accepted roles, skills and native bindings, check discovery, full SOUL loading,
effective configuration and selected integration connection status through established readbacks.
Do not run model/helper calls, memory experiments, dialog/rejection matrices, or index/update projects.
Use Mattermost step 8 for the disclosed activation and genuine DM `/sethome` binding/readback.
Reuse the configuration and file evidence under [Verification](verification.md).
Check effective `kanban.auto_decompose=false` with the [dispatcher resolver](kanban-block-triage-escalation.md).
A correct central setting needs no duplicate profile override.

### Later normal task subscriptions

This is an operational recipe for later authorized tasks, not a setup test-card requirement.
Create tasks blocked-first, bind the complete approved chain, and subscribe before release.
Use actual confirmed `PLANNER`, `BOARD`, `TASK`, channel and human IDs.
Mattermost public `O` maps to `channel`, private `P` to `group`; DM is not the task-wake target.

```sh
hermes -p "$PLANNER" kanban --board "$BOARD" notify-subscribe "$TASK" \
  --platform mattermost --chat-id "$PROJECT_CHANNEL_ID" \
  --chat-type "$PROJECT_CHAT_TYPE" --user-id "$HUMAN_USER_ID" \
  --notifier-profile "$PLANNER" --delivery-mode wake
hermes -p "$PLANNER" kanban --board "$BOARD" notify-list "$TASK" --json
```

Read back **all** subscriptions of the card: board/task, project channel, chat type,
authorized human, planner profile, `delivery_mode=wake`, unbound subscription
thread ID, and no contradicting origin bindings. This is not a special
thread requirement for normal replies. Auto-subscribe=false does not remove old rows.
Re-subscribe does not reliably replace a filled wrong profile stamp.
After change approval, replace an own wrongly stamped subscription through native unsubscribe and re-creation.
Use the current native unsubscribe syntax and exact own row identity;
halt/clarify foreign subscriptions. The event cursor starts at subscribe,
so do not subscribe only after completion.

Before later task release, read back the complete chain, routing, and effective auto-decompose setting.
Use the known resolver; do not repair existing task graphs or run fan-out experiments during setup.
A later `triage` status requires the Planner's existing recovery/authorization rules; it does not authorize decomposition.
Do not create a pipeline task to complete setup.

## 8. Partial continuation, rollback paths, and handover

Load confirmed data and evidence from `devteam/setup.md`, or the existing pre-profile handoff dataset.
Use the JSON readback in section 6 as the raw-value source.
Read the relevant native objects and resume only the first incomplete setup step.
Reuse confirmed names, project, bank, board, technical profile IDs, models, and reasoning.
Compare native identities, target account HOME/workspace, effective model configuration,
and the last written SOUL bytes with the confirmed data and delivery evidence.
If required confirmed input is missing, obtain it before using it.
If actual targets drift, resolve that drift before rendering or writing.
If only descriptive prose is stale, update the prose from readbacks.
Do not repeat successful creates or confirmed choices because prose is stale.
Native objects remain authoritative for current state; the record is evidence.
After a failure, preserve the latest verified step, exact own objects, missing prerequisite,
next action, required authorization, and success signal.
Keep the following targeted recovery cases:

| Case | Preserved partial state | Next prerequisite / success signal | Targeted rollback path |
|---|---|---|---|
| Foreign role/bank/board name | All existing objects | Prove ownership or confirm a new identifier; native unambiguous readback | Do not change/delete a foreign object |
| Half-finished own setup | Already evidenced profiles, board, bank, sources, and hashes | Reconcile drift with native objects; check the first open gate successfully | Revert only documented own file version/config entries |
| PM effect not approved | Referenced sources outside discovery | Approve the shared scope; verify the new generation and existing profiles | Revoke own plugin inclusion natively; do not remove a shared runtime |
| Hindsight/Mattermost unavailable | Verified profiles, files and own bank/channel | Operator restores required service/access; established availability and configuration readbacks pass | Reset only authorized own connection entries; preserve bank/channel contents |
| Codex sandbox not startable | Inventory and confirmed values | Operator provides the bwrap capability host-wide; the check command ends with status 0 | Leave team configuration unchanged; do not weaken sandbox and approval rules |
| Selected Team-Codex model or reasoning level unavailable | Original helper sources and existing verified setup | Authorized compatible access and exact configuration/inventory readbacks | Preserve the confirmed selection and report the affected incomplete capability |
| Personal Codex skill root effective | Personal equipment untouched | Correct the double binding and real worker resolution; prove team roots | Revoke only own process binding/skill copies |
| Wrong wake owner | Card blocked, work state preserved | Re-create the own subscription correctly and read it back | Remove natively only the exact assigned subscription |

Preserve existing partial states; an unreachable service is no mandate for a substitute server.
Before rollback, end activation of own plugins/adapters natively per profile,
if necessary and approved. Reset only logged own `SOUL.md`, skill copies,
config/autoload/hook entries, and
subscriptions in a targeted way. Preserve shared binaries, PM generations, other
profiles, personal Codex data, project rules, and graph caches.
Profile/board/bank/channel/session deletion needs **separate data-deletion approval**,
even when the object belongs to this setup. Readback proves the rollback path.

Hand off exact versions, output readbacks, evidence locations, and real incomplete bindings under [Verification](verification.md).
Report **Team configured; setup outputs verified** only after the installation baseline below is complete.
Excluded behavioral checks are outside scope, not pending gates.

## Record the installation baseline

After complete setup delivery, configuration/file readbacks, and recovery binding pass, follow [Team updates](update.md#record-a-new-team).
Complete all assigned pinned-asset and native-loading readbacks before claiming setup completion; file-helper initialization does not certify upstream assets.
Save the actual role IDs and homes under `confirmed_bindings.roles` in the existing private setup JSON.
Use the actual process HOME for the `team-codex` role.
Run `update_team.py init` against the reviewed committed Maker source.
Read back `devteam/installation.json` and its pristine baseline files.
Record the package SemVer and exact Maker commit in the setup evidence.
Keep installation metadata, pristine personalized `baselines/<sha256>`, proposals, backups, result journals, and rollback evidence.
Do not use the initialization helper to install files or replace setup readbacks.
Do not make excluded behavioral or research checks a prerequisite for initialization.
If the team already exists, use the documented existing-team baseline path instead.

## Version-bound sources

[Profile](https://hermes-agent.nousresearch.com/docs/reference/profile-commands),
[configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration),
[PM](https://hermes-agent.nousresearch.com/docs/reference/package-management),
[multi-profile gateways](https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways),
[Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban).
Static research anchors: Hermes `d923a5eb487a17c0a68801bba9ef0f56c81040a8`
and upstream `9e01b44dd23978f9ff40b7837467f3a9f1582130`; in particular
`hermes_cli/profiles.py`, `profile_model_seed.py`, `config.py`, `kanban_parser.py`,
`kanban_db_dispatch.py`, `kanban_db_notify.py`, `pm/plugins_state.py`,
`pm/workspace.py`, `hermes_bootstrap.py`. No CLI/runtime evidence from these sources.
