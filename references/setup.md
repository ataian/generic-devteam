# Guided native target setup

- Scope: authorized target setup only. Use established supported interfaces and recipes. Skip recurring parser, source, loader and SDK investigations.
- Inputs: confirmed nonsecret data only. Never interpolate raw user text as shell code.

Use English for development communication and artifacts. Preserve exact identifiers, quotations, errors, and deliberately localized product text.

## 1. Inventory before changes

1. **Native targets.** Resolve account, Hermes revision/distribution, terminal backend, profiles and actual homes. Check directories and registration. Treat any existing unmarked directory as a collision.
2. **Dispatch.** Identify existing gateway/multi-profile owner, Planner adapter, dispatcher home/DB and notifier. Read effective `kanban.auto_decompose` via the [known resolver](kanban-block-triage-escalation.md#set-the-homes-and-the-readback-that-counts). Require `false` before release. Limit authorized changes to the owner and selected profiles.
3. **Prerequisites.** Check required interfaces and dependencies through established read-only status/configuration paths. Skip project toolchain qualification and general timeout/retry/rate-limit investigations.
   - Missing Hindsight service or Hermes distribution prerequisite: operator action. Maker cannot install or repair it.
   - Codex and selected analysis runtime: record paths, versions, owners and shared consumers before proposing installation or change.
   - Codex shell sandbox: independent Review passes require it. Before any write run `bwrap --unshare-user --ro-bind / / --dev /dev -- /bin/true` and require exit status 0. On Ubuntu 24.04, `kernel.apparmor_restrict_unprivileged_userns=1` blocks `/usr/bin/bwrap` until an AppArmor profile grants `userns`, as the packaged `linux-sandbox` profile does. If blocked, report the missing capability for the operator. Preserve sandbox and approval settings.
   - Asset pins: read exact `source_revision` per independent asset from the manifest. Skip latest-version searches. Record pins separately from runtime versions and operational permission.
4. **Shared effects.** Identify concrete bootstrap/PM effects before CLI invocation or plugin addition. Even help/bootstrap can sync dependencies. Absolute plugin paths can alter shared PM inputs. Inspect other profiles only for a concrete shared effect. Obtain approval for the required scope before those effects. Preserve unrelated profiles and shared runtimes.
5. Check your own wrapper or local adaptation under [Maker wrapper](main-agent-wrapper.md).

## 2. Complete upfront preparation

- Reuse authorized established readbacks, session answers, `clarify` results, confirmed JSON and the pre-profile handoff.
- Ask independent missing choices together. Resolve dependent choices in preparation. No new interview skill or product-planning workshop.
- Gate: resolve every foreseeable choice before creating profiles, files, bank/board objects, installing assets or activating integrations.

| Group | Complete before starting |
|---|---|
| Project and roles | Separate project name and canonical absolute workspace; repository boundaries or confirmed absence; display names for Planner (`PLANER_NAME`), Coder (`CODER_NAME`), Reviewer (`REVIEWER_NAME`); selectable homes and collision resolutions |
| Models and analysis | Combined default set below or confirmed overrides; actual native model/provider IDs and supported reasoning; availability of original VoltAgent model/reasoning settings at the manifest revision; exactly one of CBM or Graphify; repository/corpus scope, roots, cache/output paths and any optional watcher intent |
| Codex identity | Explicitly authorized `user.name`/`user.email` reuse, provenance, access method and protected login route; discovery alone is not consent |
| Shared objects | Existing service endpoints; intended board/bank names; create versus authorized reuse and ownership |
| Communication | Mattermost server/team, intended Planner bot, human and any additional authorized users, allowed project channel, channel type and DM participants; existing IDs or explicit creation intent |
| Execution scope | Exact local writes, including team-owned Codex home instructions, profile assets, shared PM/configuration effects, external identity actions and activation; prepare protected access where possible |

- Inventory: complete pinned plugin packages and legal files. Check runtime/asset compatibility before scope acceptance.
- Absent Codex or selected analysis runtime: disclose exact first-installation release/source, paths and effects. Accepted upfront scope covers that installation without repeating version questions per component.
- Existing/shared installations: preserve them. Disclose and obtain explicit approval for each concrete required change. If a pin conflicts, report the exact mismatch and obtain an update/defer decision before dependent writes.
- Shared Hermes PM: plugin admission can change dependencies. Obtain shared scope before bootstrap or native installation. Exclude Hermes core, distribution skills and Hindsight service from Maker installation/update/repair.

- `PROJECT_NAME`: one segment without slash, backslash or traversal.
- Workspace: confirm its canonical absolute path independently of the name. Use it for `PROJECT_DIR`, `terminal.cwd` and board default workspace. Never derive the path from the name.
- `REPOSITORY_ROOTS`: one line with separate planning and implementation roots. Preserve nested checkouts and multiple roots. No repository moves, Git initialization or project tool installs.
- Before creation: check existing project instructions and native profile/board bindings for contradictions.
- Planner write authority includes the project's `HERMES.md`. It describes only the local installation; the Planner reconciles its board and workspace entries with the card binding and records the correction.

### New profile IDs

1. Preserve display names and existing confirmed IDs, including on resume/update. For a new ID, trim whitespace, lowercase, transliterate German umlauts to `ae`/`oe`/`ue` and `ß` to `ss`, remove decomposable accent marks, replace remaining runs outside `[a-z0-9_-]` with `-`, strip leading/trailing separators and limit to 64 characters.
2. Validate against `[a-z0-9][a-z0-9_-]{0,63}`, reserved names, target ownership, directories/registration and cross-role collisions. Examples: `Kirk` = `kirk`, `Julia` = `julia`, `Jörg` = `joerg`, `Jean Luc` = `jean-luc`.
3. Show valid derived IDs in the final summary without separate questions. For an empty/unusable candidate, same-normalized-name collision, reserved name or existing-profile conflict, obtain one explicit resolution. Never silently prefix, suffix, rename, delete or clone.
4. Before writes compare canonical homes, symlinks, SOUL/skill targets, Codex state and bank/board/channel ownership. Reuse only if native identity and ownership match confirmed setup evidence.

### Offer model defaults once

| Consumer | Model family | Native reasoning policy |
|---|---|---|
| Planner | Sol | Fixed high (`PLANNER_REASONING`) |
| Hermes Coder | Sol | Fixed medium (`CODER_REASONING`) |
| Reviewer | Sol | Default medium, maximum high (`ROLE_REASONING_DEFAULT` / `ROLE_REASONING_HIGH`) |
| Team-Codex | Sol | Default medium, maximum high (`CODEX_REASONING_DEFAULT` / `CODEX_REASONING_MAX`) |

- Offer the complete set once. Acceptance confirms the limits without separate maximum questions. Preserve confirmed overrides.
- Resolve actual native Sol model/provider IDs per target via established availability/configuration interfaces. `sol-medium` and `sol-high` describe model/reasoning combinations. Never submit them as guessed native IDs. Record `CODEX_MODEL` and reasoning separately.
- Validate defaults against maxima using target semantics, including nonstandard or nonconfigurable reasoning. Resolve unavailable or incompatible model/provider/reasoning during preparation. No silent provider/model switch or selection of the highest supported level.
- Six VoltAgent specialists: preserve original pinned model/reasoning via [the helper recipe](integrations.md#codex-agents). Resolve availability and conflicting customer limits before setup. Apply the Team-Codex model/default/maximum matrix to the main process only.
- Hermes Coder: fixed reasoning. Add no Hermes-Coder maximum, technical maximum setting, render field or migration.
- Task-selected Codex reasoning: default when neither complexity nor impact is HIGH. Either HIGH permits up to maximum. Both HIGH require maximum. Keep bounded retry/review escalation and unchanged model/provider rules in the Coder SOUL. No per-task customer approval within the confirmed range.

### Final summary and start decision

1. Keep confirmed nonsecret values once in the existing dataset. On interruption use the existing pre-profile handoff until the Planner home exists. Transfer values unchanged to the private record after creation.
2. Present all parameters, derived IDs, target homes, create/reuse choices, models/limits, Git identity, analysis, communication permissions, concrete writes, shared effects and activation scope. Include template-based role personalization in acceptance.
3. Disclose each deferred action, reason and execution point: protected login requiring a new home, native `/hooks` approval after configuration, genuine Planner DM `/sethome` after role delivery and adapter activation. Prepare protected credentials earlier where supported. Never collect secrets in chat or JSON.
4. Obtain the start decision after resolving every foreseeable choice. Use the dataset in later steps. Substitute generated native IDs from readbacks. Read resolved homes from native outputs. Do not ask the user to invent or repeat either or reopen agreed role rules. Ask later only for a new conflict/failure, newly knowable decision, user scope change or disclosed deferred interaction.

## 3. Fresh profiles, confirmed models

Prerequisites: collision check and activation approval. Use this sequence for Planner, Coder and Reviewer with confirmed technical `PROFILE`, nonsecret `DESCRIPTION`, provider/model and respective `EFFORT`: `PLANNER_REASONING`, `CODER_REASONING`, `ROLE_REASONING_DEFAULT`. Planner and Hermes Coder keep fixed levels. Set reasoning only with confirmed support. Otherwise record missing capability or deliberate inapplicability.

- Create uses model seeding and can inform the running multiplexer. No clone or credential copy. Keep all required base skills. Do not use `--no-skills`.
- Immediately after create and again on resume check actual activation. If the Planner is already hot-admitted, record the early multiplexer effect. Report section 7 as a routing/context check for that Planner, never as its first start.
- Require complete accepted role/skill files, native bindings and verified effective loading before intentional adapter activation, `/sethome` or task work. Hold other Home/dialog operations at the same gate. If the existing owner cannot hold this boundary, stop and clarify an approved profile-scoped native path. Never switch off other profiles globally. Before later messages recheck roles and effective adapter routing, including for an already served Planner.
- After profile creation, record the **actually resolved profile home** and use it for all targets. Immediately after confirmed Planner creation, start private `devteam/setup.md` from the [record template](../templates/setup-record.md) (directory 0700, file 0600). Log changes as they happen.
- Before setting provider/model, check inherited provider/endpoint definitions and deliberately set the intended route.

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

For the Coder and Reviewer profiles only, set the per-wait cap. A wait call may occupy that cap and ends with the process; it does not extend the worker-run limit. A worker may raise this cap to the card runtime, so the Coder passes `timeout=14400` explicitly to each wait.

```sh
hermes -p "$PROFILE" config set terminal.timeout 14400
hermes -p "$PROFILE" config get terminal.timeout
```

Disable the automatic skill-review trigger only in the Planner profile:

```sh
hermes -p "$PLANNER" config set skills.creation_nudge_interval 0
hermes -p "$PLANNER" config get skills.creation_nudge_interval
```

Protection per selected role: require effective `security.protected_instruction_files: false`. Reuse a correct central value without a duplicate profile entry. If needed and authorized, set the profile-local value natively:

```sh
hermes -p "$PROFILE" config set security.protected_instruction_files false
hermes -p "$PROFILE" config get security.protected_instruction_files
```

Record effective protection and its management source. Report genuine conflicts. Never alter central policy or bypass administrative restrictions.

Grant the team's regular container commands in all three profiles, so a standard development operation does not become an approval question. The runtime matches a grant only against a simple command line: a compound line (`;`, `&&`, `|`, a heredoc) or `$` expansion inside double quotes never matches. The project guide therefore needs one script entrypoint, and these entries cover the direct commands around it.

```sh
hermes -p "$PROFILE" config set command_allowlist '["docker *","docker-compose *","env * docker *","env * docker-compose *"]'
hermes -p "$PROFILE" config get command_allowlist
```

Record the effective list, the reason for each entry, and that `approvals.single_query_mode`, `unattended_mode` and `cron_mode` stay `deny`. Add no entry outside the development environment. Reconcile the same list on update; a team updated from an older Maker otherwise keeps the old empty list.

In the correct native profile, use protected login and read back model configuration. Check environment/YAML, session/per-model/CLI overrides, fallbacks and required helper routes through established interfaces. Return relevant nonsecret fields and effective override sources only. A stored key or warning alone cannot prove an effective value.

### Planner Kanban tools

Kanban is default-off for model tools even with a configured board and working `hermes kanban` CLI.

- Confirmed Planner profile: explicitly enable all three surfaces. Desktop/TUI use `cli`, Mattermost uses `mattermost`, and OpenAI-compatible WebUI calls use `api_server`.
- Before enabling, capture native tool selections per platform and saved `platform_toolsets`, root `toolsets` and `agent.disabled_toolsets`.
- Preserve unrelated enabled and disabled tools, MCP selections and global suppression entries. If native enable would broaden unrelated permissions, such as clearing a `no_mcp` sentinel, stop for a supported scoped resolution. Never replace `platform_toolsets` or root `toolsets` with a Kanban-only list.

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

- Verify `kanban` enabled without stripping warnings on all three platforms. Compare complete before/after selections and suppression entries. Resolve session/tool-selection conflicts before claiming availability in the affected context.
- Record readbacks privately. Keep the binding incomplete if availability or preservation fails. Readbacks establish configuration only. No new model call, task, service restart or session restart to check adoption by a running conversation.

Keep native Kanban guards, the single active task, and the fixed independent Reviewer unchanged.

## 4. Own board and Team-Codex

Only when no own board exists and identity is confirmed:

```sh
hermes kanban boards create "$BOARD" --name "$PROJECT_NAME" --default-workdir "$PROJECT_DIR"
hermes kanban boards list --json
```

1. Compare board ID, name and default workspace. Record evidence and the same readback ID in `BOARD` and `KANBAN_BOARD_NAME`. Use `--board "$BOARD"` for every later operation. No global switch. Bind repository, branch and plan revision per task, outside setup.
2. Bind `devteam/codex-home` and `devteam/user-home` inside the actual Coder home via [Team-Codex](integrations.md#team-codex). Store in `confirmed_values`: `CODEX_BINARY` (verified stable absolute entrypoint, never release-specific target), `CODEX_PROCESS_HOME` and `CODEX_HOME`. Compare both homes with configuration readbacks.
3. Deliver/configure the selected analysis branch's complete original components only. Bind authorized repository/MCP roots. No indexing, product-data queries or artificial test workspace. Stop on conflict with the confirmed branch. For [CBM](code-analysis.md#codebase-memory), bind the canonical account cache literal in MCP TOML `env` before hook approval. Include complete native Codex subagents alongside the six VoltAgent helpers. Read back targets, assets, runtime binding and licenses for Planner, Coder, Reviewer and Team-Codex.
4. After analysis integration writes, deliver [Team-Codex instructions](integrations.md#team-codex-instructions) to the confirmed config home. Preserve any CBM pointer and verify effective sources before intentional adapter activation, `/sethome` or task work.

## 5. Hindsight and Mattermost

- [Hindsight](integrations.md#hindsight): same confirmed new or authorized reused bank for every role on the existing service.
- [Mattermost](integrations.md#mattermost): Planner profile only. Use prepared identities, membership, permissions and existing IDs. Resolve new channel/DM IDs from metadata. Defer step 8 to section 7's delivery, effective loading, binding and routing checks.
- Keep credentials and communication targets out of shared project instructions and all role SOULs.

## 6. Own skills, roles, and text personalization

- Before role acceptance, deliver complete original [grill-me, grilling, domain-modeling, and to-questionnaire](integrations.md#grill-me) trees and [Superpowers](integrations.md#superpowers) to the Planner. All four originals are fixed equipment. Record full source/target comparisons privately. If a required tree or companion is unavailable, withhold dependent Planner output and report the asset.
- Continue the private [setup record](../templates/setup-record.md) at `<actual planner home>/devteam/setup.md` outside project, Git and Maker tree (directory 0700, file 0600). Reconcile confirmed data and actual targets before overwriting. Record authorization, upfront readiness and disclosed deferred actions.
- Completed step evidence: native identity or exact own path, previous state/hash, verified readback and next prerequisite. Use the existing target-readback, progress, blocker and installation/update sections.
- Asset evidence: compare complete assigned inventories and legal files against manifest `source_revision`. Record required and observed sources/revisions and licenses. Keep compatible runtime reuse separate from pinned delivery. Unknown provenance cannot prove a pristine baseline.
- Raw data: lossless single `json` block. Use `confirmed_values` for setup inputs and `confirmed_bindings` for resolved technical bindings. Preserve all existing keys/types, including native-only models/reasoning and role/recovery bindings. Never reconstruct raw values from prose/tables, invent missing values or store secrets.

Generate from `record_template_text` with this pure fragment. On resume use the existing record:

```python
import json
record_head, record_json = record_template_text.split("```json\n", 1)
_, record_tail = record_json.split("\n```", 1)
record_text = record_head + "```json\n" + json.dumps(
    {"confirmed_values": confirmed_values, "confirmed_bindings": confirmed_bindings},
    ensure_ascii=True, indent=2,
) + "\n```" + record_tail
```

In authorized setup write `record_text` only to the confirmed own record target. Read exact bytes as `record_readback_text`. Parse this way for readback and resume:

```python
import json
record_data = json.loads(record_readback_text.split("```json\n", 1)[1].split("\n```", 1)[0])
confirmed_values = record_data["confirmed_values"]
confirmed_bindings = record_data["confirmed_bindings"]
```

Compare parsed values with the confirmed dataset and, on resume, relevant native objects. Stop the affected step for incomplete/invalid JSON, missing required confirmed input or target drift. Resolve missing input/drift before rendering or writing. Correct stale prose from readbacks without repeating choices or creates. Use these fragments for the confirmed dataset. No synthetic development regressions, behavior or research gates in setup.

1. **Copy skills.** Use the [source and role matrix](upstream-sources.md#bundled-components). Copy complete own trees from `skills/` to `<role home>/skills/<name>/`, including licenses, notices and references. Keep names and bytes unchanged except the recovery launcher. Bind it through the Maker step below after copying. No source-profile discovery.
   - Team-Codex: `screenshot-to-code` and `diagnosing-bugs` under `.agents/skills/` in process HOME. Before personalization follow the [diagnosis recipe](integrations.md#diagnosing-bugs) for collisions, full bytes and native discovery.
   - Planner: deliver `prototype` by [its recipe](integrations.md#prototype) before personalizing dependent SOUL clauses.
2. **Verify configuration.** Compare actual Hermes/Codex native settings, limits and helper routes with preparation data. Compare all six VoltAgent TOMLs byte-for-byte with the manifest revision, including original model/reasoning. Save sources, authorization and readbacks privately. Keep the native Codex model ID out of render fields. For every assigned consumer, read back the selected [analysis bindings](code-analysis.md) from section 4. Record roots and the installed operational update reference.
3. **Render.** In approved target setup, load [references/render_text.py](render_text.py) by reviewed package absolute path, e.g. `importlib.util.spec_from_file_location`. Never import a same-named foreign module from the search path. The renderer takes strings and has no file I/O, runtime load or CLI. Read templates in UTF-8 with the file tool.
   - `role`: `planner`, `coder` or `reviewer`. `role_manifest`: matching `role_templates` entry. Use existing SOUL templates and confirmed raw names, project, bank, board, IDs and reasoning render values from `confirmed_values`. `ROLE_NAME` is the role's display name. Missing values block output. No empty defaults or invented IDs.
   - Planner fields: `PROJECT_DIR`, `REPOSITORY_ROOTS`. Coder fields: `PLANNER_PROFILE`, `CODEX_BINARY`, `CODEX_PROCESS_HOME`, `CODEX_HOME`. Before rendering, match `PLANNER_PROFILE` to `confirmed_bindings.roles.planner.id` and `CODEX_PROCESS_HOME` to `confirmed_bindings.roles.team-codex.home`. The record holds actual resolved bindings. Pass raw absolute paths for shell quoting in the invocation block.
   - Exclude fixed Planner/Hermes-Coder reasoning and Codex model ID from render fields. Keep communication values with Planner. Use original technical data for shell values. Generate no separate runtime configuration. Bind recovery via the Maker step below.

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

4. **Validate renderer contract.** Check [role fields](native-workflow.md#2-personalize-role-souls): nonempty, raw and single-line. Names at most 120 characters. No control/format characters, template braces, indentation, backticks, backslashes or fence breakouts. Unknown, missing, additional or damaged fields fail. Replace all matching occurrences exactly in one nonrecursive pass. Escape normal Markdown. Inline code and fenced process/examples get raw validated values. No Markdown backslashes in native IDs, bank or path. Preserve every non-placeholder byte. Append no persona or process rewrite.
5. **Write.** Compare exact `soul_text` with approved personalization. Ask again only for a newly observed conflict or scope change. Recheck ownership immediately before writing. Use file tools to write `soul_text` only to the confirmed role home's `SOUL.md`. Replace only the compared neutral SOUL created for this setup. Stop for foreign or concurrently changed content. No shell interpolation or recursive global replacement.
6. **Read back every target.** Record installed paths and exact readbacks. Verify configured modes without synthetic worker experiments.
   - Roles: exact mapping, byte-identical complete `soul_text`, unchanged non-placeholder bytes, no leftover fields or Coder/Reviewer communication values. Compare role/project/bank/board values and technical IDs with the record. Check effective native configuration and logged restrictions.
   - Skills: compare full file sets and bytes with source. Compare recovery launcher with bound Maker output. Verify all three original skill trees and complete companions in the Planner home. Maker references alone cannot deliver them.
   - Planner: verify required `grilling` load, interview precedence and separate plan acceptance. Verify conditional `domain-modeling` load, authorized document boundaries, vocabulary-only glossary, proposed ADR status and existing plan gate.
   - Coder: verify default/max values and process binding. Check `$diagnosing-bugs` routing and original evidence validation via the [diagnosis recipe](integrations.md#diagnosing-bugs). Check compact task/resume instructions and propagation to fresh delegation, with scope, evidence and permissions intact.
   - All three SOULs: check compact exchanges and audience boundaries. Preserve the Reviewer's review procedure. Inspect the target loader/context boundary and prove **complete effective SOUL loading** per role. Length and file existence alone cannot prove loading. Stop on truncation. Do not reduce role obligations.
   - Team-Codex: under bound homes and cwd, verify [instruction delivery and loading](integrations.md#team-codex-instructions). Record saved bytes and effective sources separately.
   - Analysis: verify selected integration, complete original skills and native activation for Planner, Coder, Reviewer and Team-Codex. No second alternative or reference-only delivery.
   - Gate: before intentional adapter activation, `/sethome` or task work, require the complete accepted role/skill files, native bindings and effective loading above. Follow the hot-admission path in section 3 where applicable.

### Bind the planner recovery invocation

Maker owns binding and launcher generation. Copy the full `brownfield-feature-planning` tree. Keep `scripts/recover_triage.py` unchanged. Record these inputs in private `confirmed_bindings.triage_recovery`:

- `python`: verified dispatcher interpreter.
- `script`: installed Planner skill script path.
- `db`: canonical absolute existing dispatcher DB. Match it to the confirmed board identity and dispatcher resolver.
- `planner_profile`: technical ID from `confirmed_bindings.roles.planner.id`.

Reuse confirmed values without another interview. If an existing record lacks the binding, resolve it from confirmed identities and current dispatcher configuration. Stop on disagreement. Run after copying the tree:

```sh
python3 -B references/bind_recovery.py --home /actual/planner-home
```

- Binder reads private setup JSON and writes `skills/brownfield-feature-planning/scripts/recover-triage` in the resolved Planner home, mode 0700. It shell-quotes the interpreter, generic script, dispatcher DB and Planner ID. Task ID is the sole runtime argument, separate from the fixed command.
- Compare installed bytes with `bind_recovery.render_launcher` using confirmed bindings. Record hash and shell-quoted installed path in `setup.md`. Deliver the callable launcher inside the Planner skill tree before recording installation.
- Keep record reads, variable collection and configuration generation with Maker. Do not personalize Python via the SOUL renderer or create a setup recovery test card. Follow the installed recovery reference's approval and API checks before later invocation.

<a id="7-einzelprüfungen-und-wake-vor-ticketfreigabe"></a>
## 7. Output verification and communication binding

1. After complete accepted roles, skills and native bindings, verify discovery, full effective SOUL and Team-Codex instruction loading, effective configuration and selected integration connections. Use established readbacks and reuse file/configuration evidence under [Verification](verification.md). No model/helper calls, memory experiments, dialog/rejection matrices or project indexing/updates.
2. Confirm the intended Planner adapter routing and pass the instruction gate before intentional activation, `/sethome` or task work. Use [Mattermost step 8](integrations.md#mattermost) for disclosed activation and genuine DM `/sethome` binding/readback. For an already hot-admitted Planner, record the early effect and check current routing/context before `/sethome`. Leave the binding incomplete if the adapter or Home cannot be read back.
3. Verify effective `kanban.auto_decompose=false` via the [dispatcher resolver](kanban-block-triage-escalation.md). Reuse a correct central value without a duplicate override.

### Later normal task subscriptions

Only for later authorized tasks. Create blocked-first, bind the complete approved chain, then subscribe before release. Use actual confirmed `PLANNER`, `BOARD`, `TASK`, channel and human IDs. Mattermost public `O` maps to `channel`, private `P` to `group`. Never use a DM for task wake.

```sh
hermes -p "$PLANNER" kanban --board "$BOARD" notify-subscribe "$TASK" \
  --platform mattermost --chat-id "$PROJECT_CHANNEL_ID" \
  --chat-type "$PROJECT_CHAT_TYPE" --user-id "$HUMAN_USER_ID" \
  --notifier-profile "$PLANNER" --delivery-mode wake
hermes -p "$PLANNER" kanban --board "$BOARD" notify-list "$TASK" --json
```

- Read back **all** card subscriptions: board/task, project channel/type, authorized human, Planner profile, `delivery_mode=wake`, unbound subscription thread ID and no contradictory origin bindings. The unbound thread requirement applies to the subscription only. The event cursor starts at subscribe. Never wait until completion to subscribe.
- Auto-subscribe=false leaves old rows. Re-subscribe can retain a filled wrong profile stamp. Obtain change approval, then replace only the exact own row via current native unsubscribe syntax and re-creation. Halt and clarify foreign subscriptions.
- Before release, read back complete chain, routing and effective auto-decompose via the known resolver. Later `triage` follows existing Planner recovery/authorization rules and grants no decomposition authority. No graph repair, fan-out experiments or pipeline tasks in setup.

## 8. Partial continuation, rollback paths, and handover

1. Load evidence and confirmed values from `devteam/setup.md` via section 6 JSON readback, or the existing pre-profile handoff. Reuse confirmed names, project, bank, board, profile IDs, models and reasoning.
2. Compare native identities, account HOME/workspace, effective model configuration and last written SOUL bytes with saved evidence. Native objects establish current state. Resolve missing inputs or drift before render/write. Correct stale prose from readbacks without repeating successful creates or confirmed choices.
3. Resume the first incomplete step. Record latest verified step, exact own objects, missing prerequisite, next action, required authorization and success signal.

| Case | Preserved partial state | Next prerequisite / success signal | Targeted rollback path |
|---|---|---|---|
| Foreign role/bank/board name | All existing objects | Prove ownership or confirm a new identifier; native unambiguous readback | Do not change/delete a foreign object |
| Half-finished own setup | Already evidenced profiles, board, bank, sources, and hashes | Reconcile drift with native objects; check the first open gate successfully | Revert only documented own file version/config entries |
| PM effect not approved | Referenced sources outside discovery | Approve the shared scope; verify the new generation and existing profiles | Revoke own plugin inclusion natively; do not remove a shared runtime |
| Hindsight/Mattermost unavailable | Verified profiles, files and own bank/channel | Operator restores required service/access; established availability and configuration readbacks pass | Reset only authorized own connection entries; preserve bank/channel contents |
| Codex sandbox not startable | Inventory and confirmed values | Operator provides the bwrap capability host-wide; the check command ends with status 0 | Leave team configuration unchanged; do not weaken sandbox and approval rules |
| Selected Team-Codex model or reasoning level unavailable | Original helper sources and existing verified setup | Authorized compatible access and exact configuration/inventory readbacks | Preserve the confirmed selection and report the affected incomplete capability |
| Personal Codex skill root effective | Personal equipment untouched | Correct both home bindings and actual resolution. Prove team roots. | Revoke only own process binding/skill copies |
| Team-Codex instructions shadowed, truncated or unverified | Saved-file evidence and foreign sources preserved | Resolve the effective home/cwd, precedence or loader gap. Verify complete loading. | Restore only the approved own instruction change after a drift check |
| Wrong wake owner | Card blocked, work state preserved | Re-create the own subscription correctly and read it back | Remove natively only the exact assigned subscription |

- Preserve partial states. Do not substitute a server for an unreachable service.
- Rollback: if needed and approved, first deactivate own plugins/adapters natively per profile. Restore only logged own SOUL, Team-Codex instruction, skill, config/autoload/hook and subscription changes. Preserve shared binaries, PM generations, other profiles, personal Codex data, project rules and graph caches. Require **separate data-deletion approval** for profile/board/bank/channel/session deletion, including own objects. Verify rollback by readback.
- Handoff under [Verification](verification.md): exact versions, output readbacks, evidence paths and real incomplete bindings. Use **Team configured; setup outputs verified** only after required outputs and the baseline below are complete. Excluded behavior checks are outside the completion gate.

## Record the installation baseline

1. Prerequisites: complete setup delivery, configuration/file readbacks and recovery binding. Complete assigned pinned-asset and native-loading readbacks before claiming completion. Skip excluded behavior/research checks.
2. Follow [Team updates](update.md#record-a-new-team). If the team already exists, use its documented existing-team baseline path. Save actual role IDs and homes in private `confirmed_bindings.roles`. For `team-codex` use process HOME.
3. Run `update_team.py init` against the reviewed committed Maker source. Initialization records the baseline only. It cannot install files, replace setup readbacks or certify upstream assets.
4. Read back `devteam/installation.json` and pristine personalized `baselines/<sha256>`. Record package SemVer and exact Maker commit separately. Keep metadata, pristine baselines, proposals, backups, result journals and rollback evidence.

## Version-bound sources

[Profile](https://hermes-agent.nousresearch.com/docs/reference/profile-commands),
[configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration),
[PM](https://hermes-agent.nousresearch.com/docs/reference/package-management),
[multi-profile gateways](https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways),
[Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban).
Static source anchors (no CLI/runtime evidence): Hermes `d923a5eb487a17c0a68801bba9ef0f56c81040a8`,
upstream `9e01b44dd23978f9ff40b7837467f3a9f1582130`.
Relevant files:
`hermes_cli/profiles.py`, `profile_model_seed.py`, `config.py`, `kanban_parser.py`,
`kanban_db_dispatch.py`, `kanban_db_notify.py`, `pm/plugins_state.py`,
`pm/workspace.py`, `hermes_bootstrap.py`.
