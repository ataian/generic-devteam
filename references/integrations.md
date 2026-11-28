# Original integrations in the confirmed target context

Use only for authorized [setup](setup.md) or an approved [upstream companion update](update.md#required-upstream-companion-update). Consume confirmed preparation values without reopening choices.
Use complete original trees at the manifest's exact [source revisions](upstream-sources.md#third-party-components), with compatible installed runtimes. Exception: when an `upstream_components` entry selects `subpaths`, deliver exactly those paths unchanged per its component recipe. Skip latest-version searches. Record source/revision, full inventories/hashes, licenses/notices, targets and readbacks. Historical anchors supply provenance only.
Before writes, check ownership and preserve local edits. Review existing binary paths, versions, owners and shared consumers before proposing installation or replacement.
Include absent Codex or selected analysis runtime's exact first-installation target in upfront scope. Accepted scope covers all assigned files and roles. Preserve existing/shared installations unless a concrete change has explicit approval.
Disclose targets, versions, consumers and PM generation effects together. Approve profile-local installation, hook and shared PM effects before activation. For team updates, obtain advance explicit approval for any full plugin update, CBM/Graphify runtime change or Team-Codex CLI change.
Use only the approved native PM path. Keep Hermes and its distribution skills native-managed. Maker neither pins nor installs, upgrades or repairs them. Preserve the Hindsight service and change its adapter only within approved plugin scope.
Report pinned-asset/runtime conflicts and obtain an update/defer decision. Keep dependent outputs incomplete while deferred. Do not copy private profile components, invent replacement plugins, or bury bootstrap repair in plugin admission.

<a id="installation-output"></a>
## Installation output

Capture verbose noninteractive stdout and stderr in a 0600 log in the existing 0700 private setup area before returning output. Exclude protected login, credentials and device codes.
Preserve exit status through filtering. Inspect failures, scanner verdicts, warnings and required user actions. Return component, target, exit status, relevant findings and log path.
Read relevant log sections if unclear. If a scanner blocks installation, present its concrete findings before requesting the existing approval. A compact summary grants no approval. Obtain authorization before an override retry.

For native plugin inventory, check the installed command help and use `hermes -p "$PROFILE" plugins list --plain --no-bundled` when supported.
Return only the requested profile's installed component status and source bindings.
If these options are unavailable, filter captured native inventory results without changing the inventory check.

<a id="project-tools"></a>
## Project tools

Preserve confirmed workspace and repository boundaries, including nested and multiple repositories. Read project instructions only for binding and ownership. Defer build dependencies and toolchain qualification to an explicit project task.

<a id="hermes-base"></a>
## Vorhandene Hermes-Basisskills

Reuse the complete natively managed trees from [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent). Coder uses `skills/autonomous-ai-agents/codex` and Reviewer uses `skills/devops/sdlc-review`. Verify category-relative paths, canonical licenses and companions. Report missing native discovery as an unmet prerequisite. Keep Maker out of distribution repairs and private copies, including flattened copies.

For each actual profile, verify catalog, main skill and required reference loading, source path and revision. Keep `codex` unchanged. The personalized Coder SOUL and native target config own homes and work boundaries. `sdlc-review` supplies independent technical review. [Role bindings](native-workflow.md).

<a id="team-codex"></a>
## Team-Codex: Binary, Homes, Anmeldung, Modell und Reasoning

Original: [openai/codex](https://github.com/openai/codex),
[Konfigurationsorte](https://developers.openai.com/codex/config-advanced.md),
[Skills](https://developers.openai.com/codex/skills.md),
[Authentifizierung](https://developers.openai.com/codex/auth.md).
- **Select.** Read manifest `codex-cli.source_release` and `codex-cli.source_revision`. Confirm actual binary path, installed version/source, owner and shared consumers before writes. Reuse a compatible matching or newer CLI. Record reuse and required interface availability separately from pinned asset verification.
- **Approve.** If absent, include the official release for the actual platform in upfront setup approval. Verify provenance and checksums before installation through the established native package route. Any existing/shared binary replacement requires concrete approval. For updates, obtain explicit advance approval of every CLI change, including a move to the manifest target. Skip version changes solely to match the pin and per-role CLI installations.
- **Defer.** If the preserved CLI lacks a required interface, report the exact capability and hold dependent outputs pending a supported compatible route or an approved change.
- **Bind.** In the actual Coder home create team-owned `devteam/codex-home` (`CODEX_HOME`) and `devteam/user-home` (`CODEX_PROCESS_HOME`). Set `HOME` and `CODEX_HOME` only for Codex. Hermes keeps its profile home. Preserve global shell and service environments.

### Git-Identität im Team-Prozess-HOME (Pflicht vor dem ersten Auftrag)

Git resolves user config from process `HOME`. A fresh `devteam/user-home` needs its own author and committer identity even with Codex login and GitHub access.

1. Reuse the expressly confirmed commit identity and provenance from setup or a known authorized Git context. Clarify only missing name, email or reuse permission. Skip inference from profile names, login, commit history and examples.
2. Require a team-owned regular `$CODEX_PROCESS_HOME/.gitconfig` with `user.name` and `user.email`. Inspect ownership, links and existing contents. Reuse an exact match. Resolve differences and back up prior state before an approved targeted change. Preserve personal and repository config. Keep personal config, includes, credentials and credential helpers out of the new file and avoid links to them.
3. For a verified absent target, set `GIT_USER_NAME` and `GIT_USER_EMAIL` to confirmed nonempty single-line raw values and run the following.

   ```sh
   (umask 077
    git config --file "$CODEX_PROCESS_HOME/.gitconfig" user.name "$GIT_USER_NAME" &&
    git config --file "$CODEX_PROCESS_HOME/.gitconfig" user.email "$GIT_USER_EMAIL")
   ```

   Require both writes to succeed. Read back contents and mode 0600. Persist identity in the file so later starts and Git preflights receive it.
4. Set `IDENTITY_CWD` to an existing authorized repository or, if none exists, the team process home. Read back the team file and effective identity with the same bound process environment. Skip test repository creation.

   ```sh
   env -u GIT_AUTHOR_NAME -u GIT_AUTHOR_EMAIL -u GIT_COMMITTER_NAME -u GIT_COMMITTER_EMAIL \
     HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" \
     git -C "$IDENTITY_CWD" config --show-origin --get-regexp '^user\.(name|email)$'
   env -u GIT_AUTHOR_NAME -u GIT_AUTHOR_EMAIL -u GIT_COMMITTER_NAME -u GIT_COMMITTER_EMAIL \
     HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" \
     git -C "$IDENTITY_CWD" var GIT_AUTHOR_IDENT
   env -u GIT_AUTHOR_NAME -u GIT_AUTHOR_EMAIL -u GIT_COMMITTER_NAME -u GIT_COMMITTER_EMAIL \
     HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" \
     git -C "$IDENTITY_CWD" var GIT_COMMITTER_IDENT
   ```

   Verify the regular team `.gitconfig`, mode 0600, source and exact author/committer values without committing. Resolve conflicting `GIT_CONFIG_*`, XDG, include or repository overrides. Preserve global config and avoid identity environment overrides. On resume, reuse the confirmed identity and read back the affected binding. Record provenance, path, mode and results privately. A failed binding keeps Team-Codex setup incomplete.

Use this process binding for every Team-Codex call. The example uses ordinary device login where supported by the account.

```sh
env HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" PONYTAIL_DEFAULT_MODE=full "$CODEX_BINARY" login --device-auth
```

- **Login.** If device login is unavailable, use the current official regular login in the same team context. Guide the user through protected input. Keep tokens out of chat, arguments and logs. Verify Codex access separately from Hermes auth. Skip blanket auth-file copies and auth proxies.
- **Tasks.** Use the same process-local HOME/CODEX_HOME through unchanged Hermes `codex`. Add no wrapper. Preserve unrelated `CODEX_HOME/config.toml` entries. Set confirmed native `model` and `model_reasoning_effort`. Retain the supported `model_provider` and definition for any confirmed custom route.
- **Reasoning.** Coder reads the configured model and defaults to `CODEX_REASONING_DEFAULT`. CLI overrides can exceed that default. Keep `CODEX_REASONING_MAX` in SOUL policy without a new config key. Check supported levels and access through native readbacks. Skip higher-reasoning experiments.
- **Discovery.** Deliver skills to `CODEX_PROCESS_HOME/.agents/skills/<name>/` and unchanged [VoltAgent originals](#codex-agents) to `CODEX_HOME/agents/`. Read effective config and skill roots, including compatible `CODEX_HOME/skills`, project/ancestor `.agents/skills`, project config, admin/system sources and inherited overrides. Separate homes reduce personal inheritance without sandboxing. Preserve personal files and project tool paths. Resolve binding failures without copying personal state.

<a id="team-codex-instructions"></a>
## Team-Codex instructions

For authorized setup, deliver after writes from the selected analysis integration. Leave fresh-setup autoload entries intact.
For existing teams, use the specific [CAC migration approval and activity gate](update.md#cac-migration), even when referred here by the upstream companion recipe. Generic upstream approval alone does not authorize this write.
Follow the CAC journal and backup steps. After drift checks, recheck native activity and claims immediately before staging. Recheck again before dependent SOUL application and each retirement mutation under the same migration procedure. Keep affected work pending if an older context still needs the bindings or activity is unresolved.

1. **Resolve.** Use the reviewed Maker commit's [team instruction template](../templates/team-codex-AGENTS.md). Target only the regular `$CODEX_HOME/AGENTS.md` in the confirmed team config home. Match it and the separate process `HOME` against private setup bindings.
   For each intended Coder working directory, record the selected CLI path/version, instruction-relevant environment and flags, including `PONYTAIL_DEFAULT_MODE=full`, project root and trust, config layers, inherited overrides, fallback filenames and effective `project_doc_max_bytes`. Keep secrets out of the record. Inventory home `AGENTS.override.md` and ancestor and nested sources in [native discovery](https://developers.openai.com/codex/guides/agents-md/) order.
   Check canonical paths, ownership, links, contents, precedence and policy before writes. Preserve project, personal, shared and administrative instructions. Resolve a shadowed or conflicting home rule through approved reconciliation. Stop if safe placement or full reach remains unresolved.
2. **Deliver.** Reuse a verified identical managed copy. For an existing team-owned file, back up bytes and mode outside discovery, then prepare a one-time merge preserving unrelated local text, mode and any CBM pointer. For a new file, prepare exact template bytes at mode 0600. Recheck drift immediately before writing. Stop on a foreign target, ambiguous merge or concurrent change. Verify saved bytes and mode against the approved result.
3. **Inspect native prompt input.** Use the selected CLI's verified prompt inspection interface. For `codex debug prompt-input`, run offline in private scratch, with distinct disposable process and config homes and a disposable layout for each actual Coder cwd. Reproduce the resolved instruction inputs byte-for-byte, including overrides, repo boundaries, trust, discovery-relevant config and the effective byte limit. Map the real paths to their scratch copies. Use the same binary and instruction-relevant settings. Retain only configuration needed for discovery. Exclude credentials, live provider settings, executable hooks, plugins and MCP servers. If isolation changes instruction resolution or the actual context cannot be reproduced, keep the check incomplete.

   With absolute scratch paths, an empty inherited environment and network access blocked, use the loopback-only placeholder provider. Set `CHECK_PROJECT_DOC_MAX_BYTES` to the actual effective limit. Apply any other reproduced discovery settings in the scratch configuration or mapped CLI flags.

   ```sh
   (
     cd "$CHECK_CWD" &&
     env -i PATH=/usr/bin:/bin TERM=dumb TMPDIR="$CHECK_TMPDIR" \
       HOME="$CHECK_PROCESS_HOME" CODEX_HOME="$CHECK_CODEX_HOME" PONYTAIL_DEFAULT_MODE=full \
       "$CODEX_BINARY" debug prompt-input \
       -c 'model_provider="fixture"' \
       -c 'model_providers.fixture.name="fixture"' \
       -c 'model_providers.fixture.base_url="http://127.0.0.1:1/v1"' \
       -c 'model_providers.fixture.wire_api="responses"' \
       -c "project_doc_max_bytes=$CHECK_PROJECT_DOC_MAX_BYTES" \
       SYNTHETIC_FIXTURE_QUERY
   )
   ```

   Keep raw output private. Require zero exit status and parse stdout as JSON. Require the synthetic query as the final user input and one user instruction block headed `# AGENTS.md instructions for ` with an `<INSTRUCTIONS>` payload for the mapped cwd. Compare the whole payload to the selected CLI's rendering of the expected ordered layers, including complete CAC and preserved local/CBM text. Verify source paths and bytes separately. A matching fragment cannot identify a source.
   On unsupported CLI, probe failure, ambiguous output, missing text, shadowing or truncation, record the precise blocker and saved-file evidence. Keep effective loading incomplete, withhold dependent setup or migration steps and retain legacy bindings. Use an equivalent verified offline interface if available. Skip live prompts and preserve the selected CLI until a concrete version change is approved.
4. **Record.** In the private setup/update record, retain Maker SemVer and commit, template path/hash, target and installed/previous hashes and modes, applicable backup, and exact CLI/home/cwd context, source order, limits and result. Verify task/resume propagation in the delivered Coder SOUL. Check any Reviewer-side Codex helper in its own context. If its home differs, use its existing brief and preserve independent evidence boundaries. Report saved-file, isolated native-loading and live behavior evidence separately. Skip style conversations and worker restarts.

<a id="diagnosing-bugs"></a>
## Owned diagnosing-bugs — Team-Codex

- **Deliver.** Check native names/commands and all resolved skill candidates across user, project/ancestor, config, admin and system roots. Reuse the managed skill through normal update comparison. Resolve unrelated name collisions with the user before replacement or shadowing. After ownership, local-edit, backup and approval checks, copy the complete tree unchanged from the selected Maker revision to `<CODEX_PROCESS_HOME>/.agents/skills/diagnosing-bugs/` through the existing mapping. Include `references/method.md`, README, NOTICE and the full MIT license.
- **Verify.** Before role personalization, compare complete file sets and bytes. Under the bound Team-Codex HOME/CODEX_HOME, read back one unambiguous native discovery entry and full `SKILL.md` and `references/method.md` via the established read-only interface, without a model call or bug experiment. After instruction delivery, read back the `## Skills` block of the delivered Team-Codex instructions: the literal `$diagnosing-bugs` cue, the brief with symptom and verification criteria, validation against original evidence, and the compact result contract. The Coder SOUL carries none of these cues; reading them there is a failed readback.
- **Record and recover.** Record saved-tree, discovery and call-policy evidence separately in the private setup/update record. Leave live diagnosis and running-conversation adoption unverified. Use guarded file-update rollback. Newly added files require separate removal approval.

<a id="disposable-demo"></a>
## disposable-demo — Planner, Coder, Reviewer

- **Source.** [ataian/disposable-demo](https://github.com/ataian/disposable-demo) at `2c6331d1fc73ae25744d11399feafc19f798c13b`. Acquire `upstream_components.disposable-demo.subpaths` from the named repository; never a branch tip, working copy or republished copy. Do not install `AGENTS.md`, `HERMES.md`, `docs/`, `.gitignore` or `tests/test_*.py`.
- **Deliver.** In each profile named by `targets`, check native names and all resolved skill candidates for collisions. After ownership, local-edit and approval checks, copy the selected files unchanged to `<ROLE_HOME>/skills/disposable-demo/` with their repository-relative paths. Compare complete file sets and bytes with the pinned Git objects. Take modes from the pinned tree: `scripts/demo.sh` is `100755`; every other selected file is `100644`.
- **Verify.** Read back one unambiguous native discovery entry, load `SKILL.md`, and resolve `README.md` and `tests/smoke.md` from it. A manifest row, successful copy or file hash alone is not a loading check; an unresolved required reference leaves delivery incomplete.
- **Record and recover.** Record commit, installed root, inventory with hashes and modes, and discovery/load readbacks in the private setup/update record. Keep saved-file, native-loading and live behavior evidence separate. Do not start a demo during setup. Use guarded file-update rollback; added files need separate removal approval.

<a id="dev-environment"></a>
## dev-environment — Planner, Coder, Reviewer

- **Source.** [ataian/dev-environment](https://github.com/ataian/dev-environment) at `3205d3a70fe6ad65c191d07172e106895b75fa04`. Acquire `upstream_components.dev-environment.subpaths` from the named repository; never a branch tip, working copy or republished copy. Do not install `HERMES.md`, `.hermes/`, `docs/`, `.gitignore` or `tests/`.
- **Deliver.** In each profile named by `targets`, check native names and all resolved skill candidates for collisions. After ownership, local-edit and approval checks, copy the selected files unchanged to `<ROLE_HOME>/skills/dev-environment/` with their repository-relative paths. Compare complete file sets and bytes with the pinned Git objects. Take modes from the pinned tree: `scripts/dev.sh` and `scripts/run-in-tools.sh` are `100755`; `SKILL.md`, `references/install.md`, `references/toolchain.md` and `scripts/dev-runner.py` are `100644`.
- **Verify.** Read back one unambiguous native discovery entry, load `SKILL.md`, and resolve `references/install.md` and `references/toolchain.md` from it. A manifest row, successful copy or file hash alone is not a loading check; either unresolved reference leaves delivery incomplete. In the Planner profile this load is the environment-reference check; it does not replace the separate `grilling` and `domain-modeling` loads.
- **Project use.** Setup delivers files only. At project installation the authorized setup operator applies the installer to the actual project root; ordinary team setup does not build the project or start services. Team-Codex reaches the generated project guide through the checkout; no second Codex skill installation.
- **Existing-team adoption.** A 3.1.1 Planner home already has an owned `dev-environment` tree at this same discovery name. Stage the pinned tree outside discovery, back up the old tree, and retire it before installing this tree; never merge over it or retire it after the replacement is installed. Follow [environment adoption](update.md#environment-skill-adoption-400).
- **Record and recover.** Record commit, installed root, inventory with hashes and modes, and discovery/load readbacks in the private setup/update record. Keep saved-file, native-loading and runtime evidence separate. Use guarded file-update rollback; added files need separate removal approval.

<a id="prototype"></a>
## Owned prototype — Planner only

- **Deliver.** Check native names/commands and all resolved Planner skill candidates for collisions. Reuse the managed skill through normal update comparison and resolve unrelated same-name targets before replacement or shadowing. After ownership, local-edit, backup and approval checks, copy the complete tree unchanged to `<PLANNER_HOME>/skills/prototype/`, including `LOGIC.md`, `UI.md`, NOTICE and the full MIT license. Use the existing `own_skills.targets` mapping. No additional installer or runtime is required.
- **Verify.** Before role personalization, compare the complete saved tree and read back one unambiguous native entry and full `SKILL.md`, `LOGIC.md` and `UI.md`. After SOUL delivery, read back the direct-authoring exception and conditional grilling trigger. Within approved update scope, reconcile local rules that route these aids through Codex or product-development gates. Withhold the dependent Planner clauses if delivery/loading or a local-rule conflict remains unresolved, including legacy SOUL-only updates.
- **Record and recover.** Keep results in the private setup/update record. Separate delivery from live behavior and adoption by an already running conversation. During setup, do not build a demonstration as an installation check. Use guarded file-update rollback. Added files require separate removal approval.

<a id="superpowers"></a>
## Superpowers — nur Planner

Deliver the complete [obra/superpowers](https://github.com/obra/superpowers) repository only to Planner, including `.hermes-plugin/plugin.yaml`, `.hermes-plugin/__init__.py`, `skills/` and MIT `LICENSE`. Use the native install route.

```sh
hermes -p "$PLANNER" plugins install obra/superpowers --ref "$SUPERPOWERS_REVISION" --enable
```

Set `SUPERPOWERS_REVISION` from the manifest's `superpowers.source_revision`, not a branch, tag or catalog default.
The installed native `plugins install --ref` accepts an immutable 40-character commit.
For an approved replacement, the native pin-moving route is `plugins install <source> --force --ref <commit>`.
Use it only after the companion backup, drift, shared-PM and scanner-approval checks; `--force` can also accept caution findings.
If the installed interface cannot enforce the pin, stop that component without updating Hermes.

- **Readback.** Check native registration and all original files. In the new Planner context, verify `using-superpowers/SKILL.md`, `references/hermes-tools.md` and profile-correct skill references.
- **Failure and recovery.** Preserve partial state and resolve missing paths or version conflicts without plugin path patches. Roll back only the own Planner registration through native deactivate/removal. Preserve foreign plugin and PM state.

<a id="grill-me"></a>
## grill-me / grilling / domain-modeling / to-questionnaire — Planner only

Original: [mattpocock/skills](https://github.com/mattpocock/skills).
Deliver all four as fixed Planner equipment.

1. **Resolve.** Use the manifest's existing `grill-me.source_revision` outside active discovery.
   Check complete assets and provenance without searching for the newest upstream revision.
   Keep complete `skills/productivity/grill-me/`, `skills/productivity/grilling/`, `skills/engineering/domain-modeling/`, and `skills/productivity/to-questionnaire/` trees from that same revision.
   Include every `agents/openai.yaml` and all companion files, including `GLOSSARY-FORMAT.md` and `ADR-FORMAT.md`.
   Check required skill references for delivery completeness. Report a changed or missing asset contract instead of inventing a replacement.
2. **Deliver.** After target/collision checks and setup approval, copy the unchanged trees into the actual resolved Planner home's `skills/grill-me/`, `skills/grilling/`, `skills/domain-modeling/`, and `skills/to-questionnaire/` respectively.
   Include the original root `LICENSE` in each target tree and preserve other applicable legal files.
   Record source, resolved revision, complete file inventories/hashes, and actual target paths in the private setup record.
   Preserve local adaptations; reuse matching complete originals.
   Acquire only these selected skills, without additional plugin or Node installation, catalog import, or upstream setup-skill execution.
3. **Bind invocation.** Preserve `grill-me` metadata, including `disable-model-invocation: true`. Its explicit user entry calls `grilling`.
   The Planner SOUL loads `grilling` directly for each new plan and conditionally loads `domain-modeling` during that interview.
   Map upstream "Skill tool" calls to Hermes `skill_view`.
   `grill-with-docs` only routes to those two skills; do not install it or add another interview phase.
   Keep domain-document authority and conditional use in the delivered Planner SOUL, without a runtime dependency on the Maker.
   Surface any upstream source-format or location conflict with existing project conventions before document writes; preserve upstream skill bytes and resolve the conflict within authorized planning boundaries.
   On an explicit questionnaire request, load the original `to-questionnaire` through Hermes `skill_view`.
   Use it for one recipient who holds missing expertise; it is optional during planning, not another mandatory interview.
   Preserve its metadata without treating `disable-model-invocation` as a verified Hermes access control.
   Drafting does not authorize sending the questionnaire or accepting its answers as product scope; retain existing communication and plan-acceptance gates.
4. **Verify.** Compare complete file sets and bytes with the selected source, including legal files.
   Verify native discovery and complete loading of all four main files and required companions through established readbacks.
   After role delivery, read back the Planner SOUL's grilling precedence, conditional domain load, document authority, and existing plan-acceptance gate.
   Do not run a planning interview, explicit skill invocation experiment, or resume conversation during setup.

Restore only recorded own skill targets from their preserved pre-change state within the applicable authorization.
Removal of new files requires deletion approval; preserve other skills, profiles, and global configuration.

<a id="ponytail"></a>
## Ponytail — Team-Codex

Use the complete [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) repository, including `plugin.yaml`, `__init__.py`, `.codex-plugin/plugin.json`, skills, hooks, runtime JavaScript and MIT license. Verify Node on the actual Codex worker PATH for the original hooks. [Upstream installation guide](https://github.com/DietrichGebert/ponytail/blob/main/INSTALL.md).

Set `PONYTAIL_REVISION` from the manifest's `ponytail.source_revision`.
No Hermes role receives the plugin; only the Team-Codex context does.

### Team-Codex pinned local source

The upstream marketplace's nested plugin source uses `main`.
Even `plugin marketplace add DietrichGebert/ponytail --ref "$PONYTAIL_REVISION"` pins only the marketplace checkout, not that nested plugin download.
Use Codex's supported local-source marketplace registration instead.
Keep the complete Ponytail repository unchanged at `<Coderhome>/devteam/sources/ponytail-marketplace/ponytail`, detached at the manifest commit.
Compare all tracked paths and bytes, including hidden manifests, hooks, assets and `LICENSE`, before native registration.
Keep this immutable source outside active skill/plugin discovery and separate from plugin runtime data.
Set `PONYTAIL_MARKETPLACE` to its parent `ponytail-marketplace` directory.
Create only the team-owned native registration file `$PONYTAIL_MARKETPLACE/.agents/plugins/marketplace.json` with these exact fields:

```json
{
  "name": "team-ponytail",
  "plugins": [{
    "name": "ponytail",
    "source": {"source": "local", "path": "./ponytail"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
  }]
}
```

This registration metadata is outside the unchanged upstream repository; it is not a rewritten plugin manifest.
After ownership/collision checks and installation approval, use the bound Team-Codex process:

```sh
env HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" PONYTAIL_DEFAULT_MODE=full "$CODEX_BINARY" plugin marketplace add "$PONYTAIL_MARKETPLACE"
env HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" PONYTAIL_DEFAULT_MODE=full "$CODEX_BINARY" plugin add ponytail@team-ponytail
```

Read back native marketplace/plugin registration, resolved local source, installed plugin root and complete original file/byte inventories at the pinned commit.
Check project/personal registrations for shadowing; preserve unrelated bindings.
On an existing team, include retirement of the exact old team-owned Ponytail binding in the approved companion scope and backup.
Use only the installed native removal/replacement interface; do not leave competing enabled copies or delete personal plugins.
If this CLI cannot register the exact local source or replace its old binding safely, report the concrete missing capability and keep Ponytail setup/update incomplete.
Do not fall back to moving `main` or treat successful command exit as pin verification.
Native source evidence: Codex `rust-v0.167.1`, `codex-rs/cli/src/marketplace_cmd.rs`, `codex-rs/cli/src/plugin_cmd.rs`, and `codex-rs/core-plugins/src/marketplace.rs` at the manifest CLI commit.

- **Team-Codex default.** `hooks/ponytail-config.js` reads the same default. Supply `PONYTAIL_DEFAULT_MODE=full` in the `env` prefix with HOME/CODEX_HOME on every call via the Coder SOUL binding. This takes precedence over inherited XDG without editing personal files. SessionStart selects the mode. `hooks/ponytail-runtime.js` writes it to `.ponytail-active` under actual `PLUGIN_DATA`, also per project where applicable. `/ponytail full` is a process-local mode change.
- **Readback.** Verify actual plugin root and native registration, `/hooks` approval for original SessionStart, SubagentStart and UserPromptSubmit, default sources, process binding, data root and existing mode record. Record missing approvals. A SOUL clause or slash change alone cannot prove persistence. Skip injection conversations and worker, resume and child experiments.
- **Recovery.** Revert only own plugin registration, hook approval and associated mode files. Preserve shared runtimes and personal plugins.

<a id="caveman"></a>
<a id="caveman-writing-skills"></a>
## Former Caveman delivery

For existing teams only, follow [CAC migration](update.md#cac-migration) within the approved companion update to reconcile legacy Caveman bindings.
Use the recorded installation evidence and prior manifest to identify owned assets.
See [historical sources](upstream-sources.md#caveman) for attribution.

<a id="find-skills"></a>
Original [vercel-labs/skills](https://github.com/vercel-labs/skills): copy complete `skills/find-skills/` and MIT `LICENSE` to `<CODEX_PROCESS_HOME>/.agents/skills/find-skills/`.
Use the manifest's `find-skills.source_revision` for new and reused copies.
Compare the complete companion set with the selected source and verify native discovery/loading.
Do not run a synthetic search during setup.
Later `npx skills` use can download packages; search results do not authorize installation.
Route component suggestions through Coder to Planner instead of installing automatically.

<a id="codex-agents"></a>
## Six unchanged upstream custom agents

- **Source.** Select exactly six [VoltAgent originals](https://github.com/VoltAgent/awesome-codex-subagents) at the [manifest](../manifest.json) `codex-custom-agents.source_revision` for setup and updates. Compare reused sources against that pin. Preserve MIT `LICENSE`, original bytes, revision and hashes outside discovery. Skip other agent packages.
- **Delivery.** Keep all six TOMLs unchanged, including `model`, `model_reasoning_effort` and instructions. Keep the main-process matrix separate. Resolve unavailable original models, unsupported reasoning, or conflicting customer limits during preparation. Report unavailable capability and preserve original settings. After ownership and collision checks, write originals under their basenames in `CODEX_HOME/agents/`.
- **Readback.** Compare complete installed bytes with the pinned originals, including model and reasoning fields. Record revision, actual targets and matching hashes privately. Check native inventory, discovery, configuration/access and project or same-name shadowing in the bound Team-Codex context. Skip model probes, calls and generated test artifacts.
- **Authority and recovery.** Keep parent provider, approval and MCP inheritance. A TOML sandbox field does not isolate the helper. The Hermes Reviewer remains independent. Restore only recorded own files after hash comparison. Preserve unrelated agents and local edits. [Native Custom Agents reference](https://developers.openai.com/codex/subagents.md).

<a id="hindsight"></a>
## Hindsight am vorhandenen Dienst

Use the complete original `hindsight-integrations/hermes` subtree and applicable parent licenses and notices. Set `HINDSIGHT_REVISION` from manifest `hindsight.source_revision` for native admission. [Upstream adapter](https://github.com/vectorize-io/hindsight/tree/main/hindsight-integrations/hermes).

```sh
hermes -p "$PROFILE" plugins install vectorize-io/hindsight/hindsight-integrations/hermes --ref "$HINDSIGHT_REVISION"
hermes -p "$PROFILE" memory setup
hermes -p "$PROFILE" config get memory.provider
```

- **Service and bank.** Use the confirmed existing service (`local_external`). Create or reuse only the explicitly authorized shared project bank. Reuse the existing own bank on resume. Preserve the service without provisioning an embedded server, upgrading or restarting it for the adapter pin. Read back native fields, `memory.provider=hindsight` and actual bank identity.
- **Adapter.** The source shorthand selects the complete subtree at the pinned commit. Retain root `LICENSE` separately if omitted. Work within authorized profile-local integration and PM scope. Disclose and approve shared adapter/SDK dependency effects before admission or update. Per assigned role, verify original subtree bytes, source/commit, native registration and effective provider.
- **Historical source evidence.** Adapter 1.2.3 required Hermes >=0.21.4, Python >=3.11, `hindsight-client>=0.10.1,<1` and `hindsight-embed>=0.10.1,<1`. Use the pinned adapter and its authorized dependency scope for delivery.
- **Profile configuration.** The adapter reads `<Rollenhome>/hindsight/config.json`, then legacy shared config, then environment fallback. After native memory setup, use the file tool to merge the required nonsecret fields into the profile JSON. Preserve other entries, parse and read back. Use this native reader without adding a runtime or `memory.hindsight.*` YAML keys.

```json
{
  "mode": "local_external",
  "api_url": "BESTAETIGTER_DIENST",
  "bank_id": "BESTAETIGTE_NEUE_BANK",
  "memory_mode": "hybrid",
  "auto_recall": true,
  "recall_prefetch_method": "recall",
  "recall_tags": ["scope:shared", "role:planner"],
  "recall_tags_match": "any_strict",
  "auto_retain": true,
  "retain_every_n_turns": 2,
  "retain_tags": ["role:planner"],
  "observation_scopes": "per_tag",
  "recall_types": ["observation", "world", "experience"],
  "reflect_tags": ["scope:shared", "role:planner"],
  "reflect_tags_match": "any_strict"
}
```

Use confirmed service and bank values. Set all three tag lists per role with its own `role:planner`, `role:coder` or `role:reviewer`. Supply any secret through protected native `HINDSIGHT_API_KEY` only and keep it out of the record and template.

- **Readback.** Use the established service interface for availability and bank ownership. Read back provider, profile JSON and the effective bank and role fields at each consumer. Check competing `apiKey`/`api_key`, bank templates, legacy, environment and CWD discovery and overrides without exposing secrets.
- **Semantics.** Keep `recall_prefetch_method=recall` and distinct reflect tags and matching. `per_tag` preserves role consolidation and `any_strict` excludes untagged matches. Untagged observations lack `scope:shared`. Access control remains separate from tags. Promote confirmed shared knowledge only during authorized role work.
- **Boundary and recovery.** Skip adapter function and SDK forwarding research, retain/recall/reflect, synthetic conversations and consolidation experiments during setup. Report an unsupported binding as incomplete without patching. For recovery, natively disable or reset the own memory binding and revert only own JSON changes. Preserve bank contents unless their deletion is authorized.

Quellen: [Hermes Memory Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers),
[geprüfter Katalogadapter](https://github.com/vectorize-io/hindsight/blob/d952b6e655fccab4581ee0722b51c5f103873d12/hindsight-integrations/hermes/__init__.py),
[Recall](https://hindsight.vectorize.io/developer/api/recall#tags),
[Reflect](https://hindsight.vectorize.io/developer/api/reflect#tags).

<a id="mattermost"></a>
## Mattermost geführt — ausschließlich Planner

Use the established [Hermes Mattermost recipe](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/mattermost) for the supported target version.
Consume the preparation decisions and perform only the disclosed target-dependent interactions later.
If the installed interface is incompatible, report that concrete recipe limitation instead of recurring source/UI research.

1. **Channel.** Reuse the confirmed server/team and create-versus-reuse decisions.
   Guide authorized channel creation in the user's UI, or reuse the recorded own channel.
   Resolve the actual channel ID through channel name → **View Info**; name/slug is not an ID.
   Read back team and type (public O / private P).
2. **Bot.** Keep a bot already bound to this setup. If absent, let an admin enable System Console → Integrations → Bot Accounts → Enable Bot Account Creation if needed. Guide the user through menu → Integrations → Bot Accounts → Add Bot Account. Use a dedicated Planner bot with **Member** privileges. Have the user store its token directly in protected storage. Keep it out of chat.
3. **Membership.** Add the bot to the confirmed team and project channel through channel name → **Add Members**.
   Verify actual bot ID/username and membership.
   Resolve the human User ID through Avatar → Profile and match the already authorized identity.
   Do not confuse human ID with bot ID or display name, or reopen a confirmed choice.
   Add only users explicitly authorized during preparation.
4. **Access.** Run `hermes -p "$PLANNER" gateway setup` and select Mattermost. The user enters server and bot token through protected native input or puts the token directly in the resolved private Planner secret config. Keep tokens out of shell arguments. Bind only Planner.
5. **DM identity.** Open the human–Planner bot DM. Read the distinct DM channel ID from actual channel metadata. Verify type D and both participants. If the UI omits the ID, use a supported authorized metadata lookup with protected client credentials. Never format a live token into a `curl -H ...TOKEN` command. Verify the DM identifier independently of project channel, bot and user IDs.
6. **Profile config.** The inspected adapter reads these four nonsecret settings from `platforms.mattermost.extra`. Read existing `extra` privately. Merge these fields into `MATTERMOST_EXTRA_JSON`, preserving other entries and replacing the sample channel with the confirmed ID.

   ```json
   {
     "require_mention": true,
     "free_response_channels": ["BESTAETIGTE_PROJEKTKANAL_ID"],
     "allowed_channels": ["BESTAETIGTE_PROJEKTKANAL_ID"],
     "reply_mode": "off"
   }
   ```

   Preserve the `reply_mode` string using JSON. `config set` can coerce bare `off` to a boolean. Check existing `extra` for misplaced secrets before using the command. If present, use the protected native editor to change only the four fields. Keep CLI arguments free of secrets.

   ```sh
   hermes -p "$PLANNER" config set platforms.mattermost.extra "$MATTERMOST_EXTRA_JSON"
   hermes -p "$PLANNER" config get platforms.mattermost.extra.require_mention
   hermes -p "$PLANNER" config get platforms.mattermost.extra.free_response_channels
   hermes -p "$PLANNER" config get platforms.mattermost.extra.allowed_channels
   hermes -p "$PLANNER" config get platforms.mattermost.extra.reply_mode
   ```

   Use the native wizard/secret resolver for `MATTERMOST_URL`, `MATTERMOST_TOKEN`, `MATTERMOST_ALLOWED_USERS` and `MATTERMOST_HOME_CHANNEL`. Restrict `MATTERMOST_ALLOWED_USERS` to the confirmed human ID and ensure `MATTERMOST_ALLOW_ALL_USERS` cannot bypass it. Keep nonsecret settings in the native route without blanket `.env` duplication. Record the step 5 DM ID. Wait until step 8 to set and read back Home. Send no Home message during configuration.
7. **Readback.** Read effective configuration and supported source precedence for
   adapter `extra` versus `MATTERMOST_REQUIRE_MENTION`, `MATTERMOST_FREE_RESPONSE_CHANNELS`,
   `MATTERMOST_ALLOWED_CHANNELS`, `MATTERMOST_REPLY_MODE`; protected URL/token availability,
   native gateway user authorization and Home configuration.
   Resolve conflicting values without config/environment dumps or recurring reader-source inspection.
   Channel allowlisting precedes mention handling; DMs bypass channel checks, not human authorization.
   Check additional grants, including `extra.group_allowed_chats`, bot access and global allow-all/user grants.
   They must not extend the confirmed channel/user permissions.
   Membership alone is not Planner authorization. Resolve a real conflict before activation.
   Do not weaken permissions or use synthetic authorization events to complete setup.
8. **Activation and Home.** Use the existing authorized multi-profile gateway only after complete accepted role/binding/policy delivery.
   Read back the intended Planner profile, full context loading and adapter routing before the disclosed Home action.
   Use supported profile-local admission/activation without a second owner, global migration or central restart.
   If Create already hot-admitted the Planner, record that early effect and verify current routing/context; do not claim a first start.
   Then ask the authorized human to send `/sethome` in the separate human–bot DM.
   This native command requires a MessageEvent from the running Planner adapter.
   Read back `MATTERMOST_HOME_CHANNEL` or the native Home binding: it must equal the metadata-confirmed DM ID without an extra Home thread.
   Do not use the project channel ID as a Home fallback.
   If adapter or Home readback is missing, keep this binding incomplete.
   Do not run mention/free-response/DM reply matrices, synthetic rejection cases, or artificial wake chains.
9. **Later subscriptions.** Keep the normal task [subscription recipe](setup.md#later-normal-task-subscriptions).
   It applies to authorized operational tasks, not a setup test card.
   Home binding does not establish task delivery. Do not claim live wake behavior from configuration.
   Keep direct conversations at their authorized access path and asynchronous reports in the project channel.
   Do not introduce extra status channels, threads, or a registry.

Revert only own Planner adapter activation and recorded config, Home and allowlist changes. Rotate the token only on user request. Preserve bot, channel, bank and messages without deletion approval. Keep Mattermost exclusive to Planner. Use ordinary native messaging without an additional historical thread acceptance check.

## Codeanalyse und Quellenstand

Apply exactly the confirmed alternative, `codebase-memory` or `graphify`, to Planner, Reviewer and Team-Codex.
Read only that branch of [Code analysis](code-analysis.md) as setup instructions.
For CBM deliver the complete official Codex subagents alongside the six [unchanged VoltAgent helpers](#codex-agents).
Verify setup targets, native discovery and connection/configuration readbacks without analysis experiments.
Keep provenance in [Sources](upstream-sources.md).

Static source research on 18 October 2026 inspected Superpowers `bb92a77741419a4ab5f06e711a283343f1ada0c3`, Ponytail `09c434ab73ca43761c5d8b0c5d341926c2fba710`, Caveman `bad48a0e1df55e05e3f52249afa35ecc1909ee76`, find-skills `13e4063a1cf913f5606d57d42ab83a86f5001e04` and VoltAgent `16f880a2a0486f880da75d2baffcd68af4cc4811`. These revisions identify the original routes inspected. Use the manifest for current pins and native readbacks for delivery.
