# Original integrations in the confirmed target context

Execute these recipes only during an authorized setup or the approved [upstream companion update](update.md#required-upstream-companion-update).
Consume the complete preparation dataset from [Setup](setup.md); do not reopen confirmed choices.
Read the manifest's exact `source_revision` for each independent component under [Sources](upstream-sources.md#fremdkomponenten).
Use complete pinned source trees and compatible installed runtimes, without a newest-upstream search.
Record source/revision, complete file inventory/hashes, licenses/notices, targets and exact readbacks.
Historical research anchors are provenance, not installation pins or behavioral evidence.
Check ownership and preserve local edits before writes.
Obtain authorized profile-local installation, hook and shared PM effects before activation.
Inspect existing binaries, owners, consumers, paths and versions before proposing runtime installation or replacement.
Include an absent Codex or selected analysis runtime's exact first-installation target in the complete upfront setup scope.
That accepted scope needs no repeated version question for each file or role.
Preserve existing/shared installations during new team setup; obtain explicit approval for a concrete required change.
For a team update, obtain advance explicit approval for any full plugin update, CBM/Graphify runtime change or Team-Codex CLI change.
Disclose actual targets, versions, shared consumers and PM dependency-generation effects together before that approval.
Use the supported native PM path only within that approved scope; do not hide bootstrap repair in plugin admission.
Keep Hermes and its distribution skills outside Maker pinning, installation, upgrades and repair.
Keep the Hindsight service untouched; its independently pinned adapter can change only within the approved plugin scope.
If pinned assets cannot work with the preserved runtime, report the concrete mismatch and obtain an update/defer decision.
Do not change the runtime silently or claim dependent outputs current while they remain deferred.
Do not copy private profile components or invent replacement plugins.

<a id="installation-output"></a>
## Installation output

Capture verbose noninteractive installation stdout and stderr in a mode-0600 log inside the existing mode-0700 private setup area before returning output to the model.
Keep protected login, credential entry, and device codes outside these logs.
Preserve the command's exit status independently of output filtering.
Inspect the captured result for failure, scanner verdicts, warnings, and required user actions.
Return the component, target, exit status, relevant findings, and log path.
If a scanner blocks installation, read its findings and present their concrete scope before requesting the existing approval.
Do not infer approval from a compact summary or retry with an override without authorization.
If the result is unclear, read the relevant log sections before deciding the next action.

For native plugin inventory, check the installed command help and use `hermes -p "$PROFILE" plugins list --plain --no-bundled` when supported.
Return only the requested profile's installed component status and source bindings.
If these options are unavailable, filter captured native inventory results without changing the inventory check.

<a id="project-tools"></a>
## Project tools

Keep confirmed workspace and repository boundaries, including nested checkouts and multiple repositories.
Read project instructions only as needed to establish binding and ownership.
Do not install build dependencies or qualify project toolchains during team setup.
Project preparation belongs to a later explicit project task.

<a id="hermes-base"></a>
## Vorhandene Hermes-Basisskills

Original: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent).
Resolve the complete distribution tree `skills/autonomous-ai-agents/codex` for Coder and `skills/devops/sdlc-review` for Reviewer.
Reuse the natively managed distribution skills and their canonical license/companion files; verify the actual subpaths.
Keep the native distribution's category-relative paths and existing management; do not install private distribution copies through Maker.
If a skill is missing from native discovery, report the prerequisite; do not repair the shared distribution or install a flattened private replacement.

Später je Rolle Katalog, Hauptskill und alle benötigten Referenzen im tatsächlichen
Profil laden, Quellpfad/Revision nachweisen. `codex` bleibt unverändert; konkrete
Teamhomes und Arbeitsgrenzen stehen in der personalisierten Coder-SOUL und der
nativen Zielkonfiguration; ihre Einrichtung beschreibt [native-workflow.md](native-workflow.md).
`sdlc-review` ist eigenständige fachliche Reviewfähigkeit, nicht im Maker nachgebaut.

<a id="team-codex"></a>
## Team-Codex: Binary, Homes, Anmeldung, Modell und Reasoning

Original: [openai/codex](https://github.com/openai/codex),
[Konfigurationsorte](https://developers.openai.com/codex/config-advanced.md),
[Skills](https://developers.openai.com/codex/skills.md),
[Authentifizierung](https://developers.openai.com/codex/auth.md).
Read `codex-cli.source_release` and `codex-cli.source_revision` from the manifest as the defined CLI target.
Resolve the actual binary path, installed version/source, ownership and shared consumers before writes.
Reuse a compatible matching or newer CLI; do not upgrade or downgrade it merely to match the target release.
Record the reuse decision and available required interfaces separately from exact asset-pin verification.
If absent, include the official target release for the actual platform in upfront setup approval.
Verify release provenance and artifact checksums before an approved first installation through the established native package route.
Any existing/shared binary replacement needs concrete approval; do not install a separate Codex per role.
At team-update time, obtain advance explicit approval for every CLI change, including a move to the manifest target.
If the preserved CLI lacks a required interface, report that capability and defer dependent outputs until approval or a supported compatible route.

Im tatsächlich aufgelösten Coderhome zwei eindeutig diesem Team zugeordnete
Verzeichnisse anlegen: `devteam/codex-home` und `devteam/user-home`.
`CODEX_HOME` zeigt auf ersteres, `CODEX_PROCESS_HOME` auf letzteres.
Nur der Codex-Prozess erhält HOME und CODEX_HOME; der Hermes-Prozess behält sein Profilhome.
Keine globale Shell-/Service-Env ändern.

### Git-Identität im Team-Prozess-HOME (Pflicht vor dem ersten Auftrag)

Git liest seine Benutzerkonfiguration relativ zu `HOME`, nicht zu `CODEX_HOME`.
Ein frisches `devteam/user-home` übernimmt deshalb die persönliche `.gitconfig`
nicht. Codexlogin und GitHub-Zugriff ersetzen keine Git-Autor-/Committeridentität.

1. Die bereits ausdrücklich bestätigte Commitidentität aus dem Setupauftrag oder
   einem bekannten autorisierten Git-Kontext samt Herkunft übernehmen. Nur wenn
   Name/E-Mail oder die Erlaubnis zur Übernahme fehlen, diese klären. Keine Identität
   aus Profilnamen, Login, Commit-Historie oder Beispieldaten erfinden.
2. Pflichtziel ist eine eigene reguläre Datei `$CODEX_PROCESS_HOME/.gitconfig`
   mit `user.name` und `user.email`. Vor Anlage Eigentum, Symlinks und Bestand
   prüfen. Eine passende vorhandene Datei wiederverwenden; bei Abweichungen erst
   klären und vor einer genehmigten gezielten Änderung den Vorzustand sichern.
   Keine vollständige persönliche `.gitconfig`, Includes, Credentials oder
   Credentialhelper kopieren/verlinken. Persönliche und Repo-Konfiguration erhalten.
3. Bei **noch nicht vorhandenem**, geprüftem Ziel die bestätigten Werte als
   `GIT_USER_NAME` und `GIT_USER_EMAIL` verwenden (nichtleere einzeilige Rohwerte):

   ```sh
   (umask 077
    git config --file "$CODEX_PROCESS_HOME/.gitconfig" user.name "$GIT_USER_NAME" &&
    git config --file "$CODEX_PROCESS_HOME/.gitconfig" user.email "$GIT_USER_EMAIL")
   ```

   Beide Schreibaufrufe müssen gelingen. Dateiinhalt gezielt rücklesen und Modus
   0600 prüfen. Keine Identitätsvariablen als dauerhaften Ersatz verwenden: sie
   fehlen sonst beim nächsten Start oder vorgeschalteten Git-Preflight wieder.
4. Read back the team file and effective Git identity under the actual bound process environment.
   Use an existing authorized repository context, or the team process home when no repository exists.
   Set `IDENTITY_CWD` to that confirmed existing path; do not create a test repository.
   Use the same process binding for every readback:

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

   Require the own regular team `.gitconfig` at mode 0600 with the exact confirmed identity.
   Verify source and both effective author/committer values without making a commit.
   Resolve inherited `GIT_CONFIG_*`, XDG, include, or repository overrides if they conflict.
   Do not remove global configuration or hide conflicts with identity environment overrides.
   On resume, reuse confirmed identity and read back the affected binding.
   Record provenance, path, mode and results privately; a failed binding keeps Team-Codex setup incomplete.

Grundform für jeden Team-Codex-Aufruf:

```sh
env HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" PONYTAIL_DEFAULT_MODE=full "$CODEX_BINARY" login --device-auth
```

Das ist ausschließlich der reguläre Login bei passender Kontounterstützung;
sonst den aktuellen offiziellen regulären Login im **gleichen Teamkontext**
verwenden. Nutzer durch den geschützten Login führen, keine Tokens in Chat,
Argumente oder Protokolle übernehmen. Hermesauth beweist keinen Codexzugang;
keine pauschale Authdateikopie und kein Authproxy.

Use the same process-local HOME/CODEX_HOME binding for every later Codex task through the unchanged Hermes `codex` skill.
Do not add another wrapper.
Set `CODEX_HOME/config.toml` to the confirmed native `model` and `model_reasoning_effort`.
If a custom provider route was confirmed, retain its supported `model_provider` and definition.
Preserve unrelated entries. The Coder reads the configured model; reasoning defaults to `CODEX_REASONING_DEFAULT`.
Keep `CODEX_REASONING_MAX` in the existing Coder SOUL policy, without a new technical maximum key.
A default does not limit CLI overrides. Check supported levels and access through native availability/configuration readbacks, without higher-reasoning experiments.

Place skills at `CODEX_PROCESS_HOME/.agents/skills/<name>/` and the unchanged [VoltAgent originals](#codex-agents) at `CODEX_HOME/agents/`.
Read back effective config/skill roots, including compatible `CODEX_HOME/skills`, project/ancestor `.agents/skills`, project configuration, admin/system sources and inherited overrides.
Separate homes reduce personal skill inheritance; they are not a sandbox.
Preserve personal Codex files and project tool paths after the HOME change.
Do not copy personal state to repair a binding.

<a id="diagnosing-bugs"></a>
## Owned diagnosing-bugs — Team-Codex

Use the complete owned `skills/diagnosing-bugs/` tree from the selected Maker revision, including `references/method.md`, README, NOTICE, and full MIT license.
Before writing, check native names/commands and all resolved skill candidates for `diagnosing-bugs`, including user, project/ancestor, config, admin, and system roots.
Reuse the same managed skill through the normal update comparison; resolve unrelated same-name collisions with the user before replacing or shadowing a target.
After the existing ownership, local-edit, backup, and authorization checks, copy it to `<CODEX_PROCESS_HOME>/.agents/skills/diagnosing-bugs/`.
Keep every skill byte unchanged; use the existing whole-tree setup/update mapping, not another installer.

Before role personalization, compare complete file sets and bytes and read back one unambiguous native discovery entry plus full `SKILL.md` and `references/method.md` content.
Use the actual bound Team-Codex HOME/CODEX_HOME and established read-only discovery/loading interface, without a model call or bug experiment.
After role delivery, read back the Coder's literal `$diagnosing-bugs` task/resume clause, emerging-regression instruction, and original-evidence validation.
Keep its literal `$caveman` clause, process binding, native handoff, and independent-review requirements intact.
Record saved-tree, discovery, and call-policy evidence separately in the existing private setup/update record.
These checks establish delivery and invocation policy, not actual diagnosis behavior or adoption by an already running conversation.
For rollback, use the existing guarded file-update procedure; newly added files remain retained until separately authorized removal.

<a id="prototype"></a>
## Owned prototype — Planner only

Use the complete owned `skills/prototype/` tree, including `LOGIC.md`, `UI.md`, NOTICE, and full MIT license.
Before writing, inspect native names/commands and all resolved Planner skill candidates for `prototype` collisions.
Reuse the same managed skill through the existing update comparison; resolve unrelated same-name targets before replacing or shadowing them.
After existing ownership, local-edit, backup, and authorization checks, copy the complete tree unchanged to `<PLANNER_HOME>/skills/prototype/`.
Use the normal `own_skills.targets` whole-tree mapping; no additional installer or upstream runtime component is needed.
Before role personalization, compare the complete saved tree and read back one unambiguous native skill entry, full `SKILL.md`, `LOGIC.md`, and `UI.md`.
After SOUL delivery, read back the Planner's direct-authoring exception and conditional grilling trigger.
During updates, reconcile local rules that would send these aids through Codex or product-development gates within the approved update scope.
Withhold the dependent Planner clauses if required delivery/loading or a local-rule conflict remains unresolved, including legacy SOUL-only updates.
Record these results in the existing private setup/update record; do not build a demonstration as an installation check.
Saved bytes and discovery establish delivery, not live behavior or an already running conversation's adoption.
Use the existing guarded file-update rollback; added files remain retained until separately authorized removal.

<a id="superpowers"></a>
## Superpowers — nur Planner

Original: [obra/superpowers](https://github.com/obra/superpowers), vollständiges
Repository mit `.hermes-plugin/plugin.yaml`, `.hermes-plugin/__init__.py`, gesamtem
`skills/`-Baum und MIT-`LICENSE`. Aktuelle native Originalroute:

```sh
hermes -p "$PLANNER" plugins install obra/superpowers --ref "$SUPERPOWERS_REVISION" --enable
```

Set `SUPERPOWERS_REVISION` from the manifest's `superpowers.source_revision`, not a branch, tag or catalog default.
The installed native `plugins install --ref` accepts an immutable 40-character commit.
For an approved replacement, the native pin-moving route is `plugins install <source> --force --ref <commit>`.
Use it only after the companion backup, drift, shared-PM and scanner-approval checks; `--force` can also accept caution findings.
If the installed interface cannot enforce the pin, stop that component without updating Hermes.

Nach Aufnahme die native Pluginregistrierung und alle Originaldateien im Planner
prüfen. Im neuen tatsächlichen Plannerkontext Bootstrap `using-superpowers/SKILL.md`
**und** `references/hermes-tools.md` sowie profilrichtige Skillreferenzen belegen.
Keine zusätzlichen Superpowers-Installationen in Coder, Reviewer oder Team-Codex.
Bei fehlenden Pfaden/Versionskonflikt Teilstand erhalten und klären, keine eigenen
Pluginpfadpatches. Rückweg: nur eigene Plannerregistrierung nativ deaktivieren/
entfernen, ursprüngliche fremde Plugin-/PM-Bestände bewahren.

<a id="grill-me"></a>
## grill-me / grilling / domain-modeling / to-questionnaire — Planner only

Original: [mattpocock/skills](https://github.com/mattpocock/skills).
These four skills are fixed Planner equipment, not an additional setup choice.

1. Use the manifest's existing `grill-me.source_revision` outside active discovery.
   Check complete assets and provenance without searching for the newest upstream revision.
   Keep complete `skills/productivity/grill-me/`, `skills/productivity/grilling/`, `skills/engineering/domain-modeling/`, and `skills/productivity/to-questionnaire/` trees from that same revision.
   Include every `agents/openai.yaml` and all companion files, including `GLOSSARY-FORMAT.md` and `ADR-FORMAT.md`.
   Check required skill references for delivery completeness. Report a changed or missing asset contract instead of inventing a replacement.
2. After target/collision checks and setup approval, copy the unchanged trees into the actual resolved Planner home's `skills/grill-me/`, `skills/grilling/`, `skills/domain-modeling/`, and `skills/to-questionnaire/` respectively.
   Include the original root `LICENSE` in each target tree and preserve other applicable legal files.
   Record source, resolved revision, complete file inventories/hashes, and actual target paths in the private setup record.
   Preserve local adaptations; reuse matching complete originals.
   Acquire only these selected skills, without additional plugin or Node installation, catalog import, or upstream setup-skill execution.
3. Preserve `grill-me` metadata, including `disable-model-invocation: true`; its explicit user entry calls `grilling`.
   The Planner SOUL loads `grilling` directly for each new plan and conditionally loads `domain-modeling` during that interview.
   Map upstream "Skill tool" calls to Hermes `skill_view`.
   `grill-with-docs` only routes to those two skills; do not install it or add another interview phase.
   Keep domain-document authority and conditional use in the delivered Planner SOUL, without a runtime dependency on the Maker.
   Surface any upstream source-format or location conflict with existing project conventions before document writes; preserve upstream skill bytes and resolve the conflict within authorized planning boundaries.
   On an explicit questionnaire request, load the original `to-questionnaire` through Hermes `skill_view`.
   Use it for one recipient who holds missing expertise; it is optional during planning, not another mandatory interview.
   Preserve its metadata without treating `disable-model-invocation` as a verified Hermes access control.
   Drafting does not authorize sending the questionnaire or accepting its answers as product scope; retain existing communication and plan-acceptance gates.
4. Compare complete file sets and bytes with the selected source, including legal files.
   Verify native discovery and complete loading of all four main files and required companions through established readbacks.
   After role delivery, read back the Planner SOUL's grilling precedence, conditional domain load, document authority, and existing plan-acceptance gate.
   Do not run a planning interview, explicit skill invocation experiment, or resume conversation during setup.

Restore only recorded own skill targets from their preserved pre-change state within the applicable authorization.
Removal of new files requires deletion approval; preserve other skills, profiles, and global configuration.

<a id="ponytail"></a>
## Ponytail — Coder und Team-Codex separat

Original: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail),
[Original-Installationsanleitung](https://github.com/DietrichGebert/ponytail/blob/main/INSTALL.md).
Ganzes Repository mit `plugin.yaml`, `__init__.py`, `.codex-plugin/plugin.json`,
Skills, Hooks/Runtime-JavaScript und MIT-Lizenz beziehen. Node im Codex-Worker-PATH
ist Voraussetzung der Originalhooks, nicht aus einer SOUL ableitbar.

```sh
hermes -p "$CODER" plugins install DietrichGebert/ponytail --ref "$PONYTAIL_REVISION" --enable
```

Set `PONYTAIL_REVISION` from the manifest's `ponytail.source_revision` for both harnesses.

Only for the author's documented root-`plugin.json`/manifest-gate conflict, read the original instructions at the pinned commit.
If that supported route applies, place the complete unchanged pinned repository at the confirmed `<Coderhome>/plugins/ponytail`.
Then use profile-scoped `hermes -p "$CODER" plugins enable ponytail` within the same approved plugin/PM scope.
Verify native registration and exact source bytes; do not patch manifests or bypass trust/scanner decisions.
For another error or an unsupported route, preserve the partial state and report the concrete blocker.

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

Native Hookfreigabe über `/hooks` für die tatsächlichen Originaldefinitionen
prüfen: SessionStart, SubagentStart und UserPromptSubmit. Keine Hookfreigabe als
vorausgesetzt melden. Pluginroot, Datenroot (`PLUGIN_DATA`, `.ponytail-active`)
und tatsächliche Moduswahl erfassen. Hermes-Default `full` kann durch Env oder Userdefaults verdrängt werden; ein
Slashwechsel ist prozesslokal. Konkreter Originalleser in `__init__.py`:
`PONYTAIL_DEFAULT_MODE` → `defaultMode` aus
`$XDG_CONFIG_HOME/ponytail/config.json` (falls gesetzt), sonst
`$HOME/.config/ponytail/config.json` → eingebautes `full`.
Prüfe diese Quellen im tatsächlichen Coder-Prozess, ohne dessen HOME zu verändern.
If no conflicting override is effective, use the built-in persistent default and read back its configuration.
Do not start a conversation to prove injection.
If a shared override conflicts, do not change global user defaults as a setup side effect.
Use only the supported authorized profile-local process binding for `PONYTAIL_DEFAULT_MODE=full`.
If the shared owner cannot supply that binding, report the concrete capability conflict.
Do not invent a YAML key or patch the plugin.

Team-Codex liest denselben Default über `hooks/ponytail-config.js`. Übergib für
**jeden Team-Codex-Aufruf** zusätzlich prozesslokal `PONYTAIL_DEFAULT_MODE=full`
in der `env`-Präfixliste neben HOME/CODEX_HOME; die Coder-SOUL enthält diese
dauerhafte Prozessbindung. So überschreibt
ein geerbtes XDG-Konfigurationsverzeichnis nicht still den Teamdefault, ohne
persönliche Dateien zu ändern. Der originale SessionStart-Hook setzt den aktiven
Modus, `hooks/ponytail-runtime.js` schreibt ihn unter dem tatsächlichen
`PLUGIN_DATA` nach `.ponytail-active` (gegebenenfalls zusätzlich projektbezogen).
`/ponytail full` ist der originale Moduswechsel, nicht allein der Persistenzbeleg.
Read back native plugin/hook registration, default sources, process binding and any existing mode record. Do not start worker, resume, or child experiments. A SOUL word alone does not establish plugin configuration.
Rückweg: eigene Pluginregistrierung/Hookfreigabe und zugeordnete Modusdateien
gezielt zurücknehmen; keine gemeinsamen Runtimes oder persönlichen Plugins löschen.

<a id="caveman"></a>
## Caveman writing skills

Use the original [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) release and exact revision in the manifest's `caveman.source_release` and `caveman.source_revision`.
Use that same revision for `caveman-review`, whose `source_component` is `caveman`.
Fetch the complete `skills/caveman/` and `skills/caveman-review/` trees outside active discovery.
Keep their `SKILL.md`, `README.md`, and root `LICENSE`, `LICENSE-MIT`, and `NOTICE` unchanged.
Compare reused copies against this source; an older skill with the same name is not sufficient.
Install only these writing skills; exclude Read less, CLI/engine, hooks, proxy, routing, cloud features, `ultracave`, and `megacave`.

| Consumer | Skill trees | Activation |
|---|---|---|
| Planner | `<Plannerhome>/skills/caveman/` | `skills.auto_load`: `caveman` |
| Coder | `<Coderhome>/skills/caveman/` | `skills.auto_load`: `caveman` |
| Reviewer | `<Reviewerhome>/skills/caveman/`, `<Reviewerhome>/skills/caveman-review/` | `skills.auto_load`: `caveman`; SOUL loads `caveman-review` for findings |
| Team-Codex | `<CODEX_PROCESS_HOME>/.agents/skills/caveman/` | Literal `$caveman` in each task and resume |

Resolve each home from confirmed native bindings before copying complete trees and legal files.
For each Hermes role, read `skills.auto_load` and merge `caveman` without duplicates or loss of existing entries.
Set the merged JSON list through `hermes -p "$PROFILE" config set skills.auto_load "$AUTO_LOAD_JSON"`.
Read it back with `hermes -p "$PROFILE" config get skills.auto_load`.
Preserve local adaptations; resolve collisions before replacing any installed copy.

Before role personalization, verify complete source/target file sets and bytes, autoload configuration, and native skill discovery/loading without a style conversation.
After writing the personalized SOULs, perform the following readbacks in setup section 6, step 6.
Read back each personalized SOUL's Caveman use and persisted-prose scope.
Read back the Reviewer's `caveman-review` load trigger and separation of formatting from review procedure.
Read back the Coder's per-task `$caveman` clause and propagation of scope and clarity safeguards, including restart/resume.
These SOUL clauses extend upstream style to authored tickets, documentation, and other persisted prose; preserve technical payload and safety exceptions.
The upstream skills remain unchanged. Their use must not depend on reloading this Maker.
Record source revision, inventories, hashes, target paths, and loading evidence in the existing private setup record.
For rollback, restore only recorded own skill trees and autoload changes after checking current drift; preserve unrelated entries and obtain required deletion approval.

<a id="find-skills"></a>
Original [vercel-labs/skills](https://github.com/vercel-labs/skills): copy complete `skills/find-skills/` and MIT `LICENSE` to `<CODEX_PROCESS_HOME>/.agents/skills/find-skills/`.
Use the manifest's `find-skills.source_revision` for new and reused copies.
Compare the complete companion set with the selected source and verify native discovery/loading.
Do not run a synthetic search during setup.
Later `npx skills` use can download packages; search results do not authorize installation.
Route component suggestions through Coder to Planner instead of installing automatically.

<a id="codex-agents"></a>
## Six unchanged upstream custom agents

Obtain exactly the six original agent files listed in the [manifest](../manifest.json) from
[VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents).
Use the exact `codex-custom-agents.source_revision` from that manifest for setup and updates.
Preserve the MIT `LICENSE` and original source bytes, revision, and hashes outside active agent discovery.
Do not install other agent packages as part of this step.

Keep all six TOMLs unchanged, including `model`, `model_reasoning_effort`, and instructions.
The Team-Codex main-process model and reasoning matrix do not override these specialist settings.
Resolve unavailable original models, unsupported reasoning, or conflicting customer limits during preparation.
Preserve the originals and report the affected capability; do not substitute model or reasoning values.
Compare reused sources against the pinned revision; older originals are not sufficient.
Write the unchanged files to `CODEX_HOME/agents/` under their original basenames after ownership and collision checks.

Compare complete installed bytes with the pinned originals, including model and reasoning fields.
Record the matching source/target hashes, actual targets, and source revision in the existing private setup record.
Read back the installed inventory, native discovery, and configuration/access availability in the actual Team-Codex context.
Check project-scoped or same-name agents for shadowing of these originals.
Keep provider, approval, and MCP inheritance from the parent; an agent TOML sandbox field is not a separate security boundary.
Do not add model probes, specialist calls, or generated test artifacts to setup.
No helper replaces the independent Hermes Reviewer.
For recovery, restore only the recorded own files after hash comparison; preserve unrelated agents and local edits.
Native reference: [Custom Agents](https://developers.openai.com/codex/subagents.md).

<a id="hindsight"></a>
## Hindsight am vorhandenen Dienst

Original [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight/tree/main/hindsight-integrations/hermes),
vollständiger Unterbaum `hindsight-integrations/hermes` samt benötigten übergeordneten
Originallizenzen/Notices. Use the manifest's `hindsight.source_revision` as `HINDSIGHT_REVISION` for native admission:

```sh
hermes -p "$PROFILE" plugins install vectorize-io/hindsight/hindsight-integrations/hermes --ref "$HINDSIGHT_REVISION"
hermes -p "$PROFILE" memory setup
hermes -p "$PROFILE" config get memory.provider
```

Use the confirmed existing service (`local_external`) and create or reuse the explicitly authorized shared project bank.
Read back `memory.provider=hindsight`, native setup fields and actual bank identity.
Reuse the existing own bank on resume; do not provision an embedded server.
The researched adapter 1.2.3 required Hermes >=0.21.4, Python >=3.11, `hindsight-client>=0.10.1,<1` and `hindsight-embed>=0.10.1,<1`.
These are historical source facts, not an installation mandate.
Use the complete pinned adapter and the authorized profile-local integration/PM scope.
The native source shorthand selects the complete `hindsight-integrations/hermes` subtree at that exact repository commit.
Preserve the root `LICENSE` separately if native subtree delivery omits it.
Read back installed original subtree bytes, source/commit, native registration and effective provider in each assigned role.
Adapter and SDK dependency changes can affect shared Hermes PM state; disclose and approve those effects before admission or update.
Do not update, provision or restart the Hindsight service to enforce the adapter pin.

Der Originaladapter liest profilbezogen `<Rollenhome>/hindsight/config.json`,
dann legacy geteilte Konfiguration, dann Envfallback. Erstelle/merge deshalb nach
nativer Memoryeinrichtung die **profilbezogene JSON-Datei** mit dem Dateitool,
erhalte fremde Einträge, parse/rücklese sicher; nicht erfundene
`memory.hindsight.*`-YAML-Schlüssel setzen. Dieser JSON-Weg ist der Original-
Konfigurationsleser, keine zweite Runtime. Erforderliche nichtgeheime Felder je Rolle:

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

Die drei Rollen erhalten in **allen drei Taglisten** jeweils `role:planner`,
`role:coder` oder `role:reviewer`. Dienst/Bank durch echte bestätigte Werte ersetzen.
Geheimnis nötigenfalls geschützt über natives `HINDSIGHT_API_KEY`; nicht in Record
oder diese JSON-Vorlage. Prüfe konkurrierende `apiKey`/`api_key`, Banktemplates,
Legacy-/Env-/CWD-Bankdiscovery und effektive Bankauswahl ohne Secrets auszugeben.
Explizite Rollenfelder und Bank müssen tatsächlich beim Verbraucher ankommen.

Check service availability and bank ownership through the established service interface.
Read back `memory.provider`, the profile JSON, effective bank, role tags and override sources without secrets.
Do not inspect adapter functions or research SDK forwarding during setup.
Keep `recall_prefetch_method=recall`; preserve separate reflect tags and match semantics.
`per_tag` preserves role consolidation; `any_strict` excludes untagged matches.
An untagged observation is not `scope:shared` knowledge. Tags are not ACLs.
Promoting confirmed shared knowledge later remains an operational role task, not setup prepopulation.
Do not perform retain/recall/reflect, synthetic conversation, or consolidation experiments.
A missing/incompatible supported configuration is a concrete setup limitation, not permission for a plugin fix.

Rückweg: eigenes Memorybinding nativ deaktivieren/gezielt zurücksetzen; eigene
JSON-Feldänderungen zurücknehmen. Bankinhalte bleiben ohne Löschfreigabe erhalten.

Quellen: [Hermes Memory Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers),
[geprüfter Katalogadapter](https://github.com/vectorize-io/hindsight/blob/d952b6e655fccab4581ee0722b51c5f103873d12/hindsight-integrations/hermes/__init__.py),
[Recall](https://hindsight.vectorize.io/developer/api/recall#tags),
[Reflect](https://hindsight.vectorize.io/developer/api/reflect#tags).

<a id="mattermost"></a>
## Mattermost geführt — ausschließlich Planner

Use the established [Hermes Mattermost recipe](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/mattermost) for the supported target version.
Consume the preparation decisions and perform only the disclosed target-dependent interactions later.
If the installed interface is incompatible, report that concrete recipe limitation instead of recurring source/UI research.

1. Reuse the confirmed server/team and create-versus-reuse decisions.
   Guide authorized channel creation in the user's UI, or reuse the recorded own channel.
   Resolve the actual channel ID through channel name → **View Info**; name/slug is not an ID.
   Read back team and type (public O / private P).
2. Bei fehlender eigener Botidentität: Admin muss nötigenfalls System Console →
   Integrations → Bot Accounts → Enable Bot Account Creation freigeben. Nutzer
   über Menü → Integrations → Bot Accounts → Add Bot Account führen. Eigener
   Planner-Bot, Rolle **Member** genügt; keine Adminrechte für den Bot verlangen.
   Token direkt geschützt sichern lassen, niemals in Chat abfragen. Bestehenden
   eindeutig diesem Setup zugeordneten Bot erhalten.
3. Add the bot to the confirmed team and project channel through channel name → **Add Members**.
   Verify actual bot ID/username and membership.
   Resolve the human User ID through Avatar → Profile and match the already authorized identity.
   Do not confuse human ID with bot ID or display name, or reopen a confirmed choice.
   Add only users explicitly authorized during preparation.
4. `hermes -p "$PLANNER" gateway setup` aufrufen, Mattermost auswählen, Nutzer
   Server/Bot-Token über den nativen geschützten Eingabeweg eingeben lassen.
   Alternativ legt der Nutzer den Token direkt in die aufgelöste private Planner-
   Secretkonfiguration, nie als Shellargument. Allein Planner erhält diese Anbindung.
5. Direktgespräch zwischen Mensch und Planner-Bot öffnen. Die **andere** DM-Kanal-ID
   aus den tatsächlichen Kanalobjekten bestimmen. Falls die UI keine DM-ID zeigt,
   unterstützten autorisierten Lookup der Kanalmetadaten nutzen, Secret im Client
   schützen; keinen `curl -H ...TOKEN`-Befehl mit echtem Wert erzeugen. DM-Typ D
   und beide Teilnehmer prüfen. DM-ID ist weder Projektkanal-, Bot- noch User-ID.
6. Nichtgeheimes Verhalten explizit über native Profilkonfiguration setzen. Der
   gelesene Adapter verwendet `platforms.mattermost.extra` für die vier folgenden
   Werte. Lies vorhandenes `extra` geschützt und erhalte alle anderen Einträge.
   Merge diese vier Felder als JSON-Daten in `MATTERMOST_EXTRA_JSON` (hier nur
   Strukturbeispiel, Kanalwert durch die bestätigte echte ID ersetzen):

   ```json
   {
     "require_mention": true,
     "free_response_channels": ["BESTAETIGTE_PROJEKTKANAL_ID"],
     "allowed_channels": ["BESTAETIGTE_PROJEKTKANAL_ID"],
     "reply_mode": "off"
   }
   ```

   `reply_mode` muss ein **String** bleiben: einzelne untypisierte `off`-Werte
   können von `config set` als bool coerced werden. Das JSON-Mapping erhält den
   Stringtyp; nicht das ganze vorhandene `extra` durch das Beispiel ersetzen.
   Vorher auf versehentlich dort gespeicherte Secrets prüfen; bei solchen Werten
   keine argumentbasierte Gesamtausgabe, sondern den geschützten nativen Editor
   für genau diese Felder verwenden. Keine Secrets in CLI-Argumenten.

   ```sh
   hermes -p "$PLANNER" config set platforms.mattermost.extra "$MATTERMOST_EXTRA_JSON"
   hermes -p "$PLANNER" config get platforms.mattermost.extra.require_mention
   hermes -p "$PLANNER" config get platforms.mattermost.extra.free_response_channels
   hermes -p "$PLANNER" config get platforms.mattermost.extra.allowed_channels
   hermes -p "$PLANNER" config get platforms.mattermost.extra.reply_mode
   ```

   Nativer Wizard/Secretresolver verwendet außerdem `MATTERMOST_URL`,
   `MATTERMOST_TOKEN`, `MATTERMOST_ALLOWED_USERS` und `MATTERMOST_HOME_CHANNEL`.
   `MATTERMOST_ALLOWED_USERS` auf die bestätigte menschliche User-ID begrenzen;
   `MATTERMOST_ALLOW_ALL_USERS` darf die Begrenzung nicht aufheben. Die in Phase 5
   aus Kanalmetadaten bestimmte DM-ID zunächst für die spätere Homebindung
   festhalten; in dieser Konfigurationsphase keine Home-Nachricht senden.
   Native Wizardroute für die Konfiguration verwenden, nicht pauschal nichtgeheime
   Einstellungen in `.env` duplizieren. Home setzen und rücklesen folgt in Phase 8.
7. Read back effective configuration and its supported source precedence:
   adapter `extra` versus `MATTERMOST_REQUIRE_MENTION`, `MATTERMOST_FREE_RESPONSE_CHANNELS`,
   `MATTERMOST_ALLOWED_CHANNELS`, `MATTERMOST_REPLY_MODE`; protected URL/token availability,
   native gateway user authorization and Home configuration.
   Resolve conflicting values without config/environment dumps or recurring reader-source inspection.
   Channel allowlisting precedes mention handling; DMs bypass channel checks, not human authorization.
   Check additional grants, including `extra.group_allowed_chats`, bot access and global allow-all/user grants.
   They must not extend the confirmed channel/user permissions.
   Membership alone is not Planner authorization. Resolve a real conflict before activation.
   Do not weaken permissions or use synthetic authorization events to complete setup.
8. Use the existing authorized multi-profile gateway only after complete accepted role/binding/policy delivery.
   Read back the intended Planner profile, full context loading and adapter routing before the disclosed Home action.
   Use supported profile-local admission/activation without a second owner, global migration or central restart.
   If Create already hot-admitted the Planner, record that early effect and verify current routing/context; do not claim a first start.
   Then ask the authorized human to send `/sethome` in the separate human–bot DM.
   This native command requires a MessageEvent from the running Planner adapter.
   Read back `MATTERMOST_HOME_CHANNEL` or the native Home binding: it must equal the metadata-confirmed DM ID without an extra Home thread.
   Do not use the project channel ID as a Home fallback.
   If adapter or Home readback is missing, keep this binding incomplete.
   Do not run mention/free-response/DM reply matrices, synthetic rejection cases, or artificial wake chains.
9. Keep the later normal task [subscription recipe](setup.md#later-normal-task-subscriptions).
   It applies to authorized operational tasks, not a setup test card.
   Home binding does not establish task delivery. Do not claim live wake behavior from configuration.
   Keep direct conversations at their authorized access path and asynchronous reports in the project channel.
   Do not introduce extra status channels, threads, or a registry.

Rückweg: nur eigene Planner-Adapteraktivierung und dokumentierte Config-/Home-/
Allowliständerungen zurücknehmen; Tokenrotation nur gezielt nach Nutzerauftrag.
Bot, Kanal, Bank und Nachrichten nicht ungefragt löschen. Coder/Reviewer erhalten
keine Mattermost-Konfiguration. Normale native Nachrichtenübermittlung genügt;
keine historische besondere Thread-Abnahme hinzufügen.

## Codeanalyse und Quellenstand

Apply exactly the confirmed alternative, `codebase-memory` or `graphify`, to Planner, Coder, Reviewer and Team-Codex.
Read only that branch of [Code analysis](code-analysis.md) as setup instructions.
For CBM deliver the complete official Codex subagents alongside the six [unchanged VoltAgent helpers](#codex-agents).
Verify setup targets, native discovery and connection/configuration readbacks without analysis experiments.
Keep provenance in [Sources](upstream-sources.md).

Statische Recherche vom 18.10.2026: Superpowers `bb92a77741419a4ab5f06e711a283343f1ada0c3`,
Ponytail `09c434ab73ca43761c5d8b0c5d341926c2fba710`, Caveman
`bad48a0e1df55e05e3f52249afa35ecc1909ee76`, find-skills
`13e4063a1cf913f5606d57d42ab83a86f5001e04`, VoltAgent
`16f880a2a0486f880da75d2baffcd68af4cc4811`. Diese Identitäten belegen die gelesenen
Originalwege, nicht erfolgreiche Installation oder eine dauerhafte Versionsliste.
