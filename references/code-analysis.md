# Set up code analysis

Configure only the **Graphify or CBM** branch confirmed in [Setup](setup.md) for Planner, Reviewer and Team-Codex.
Use during authorized setup or the approved [upstream companion update](update.md#required-upstream-companion-update), including restoration of missing selected assets and bindings.
Preserve analysis assets during [required skill retirement](update.md#required-skill-retirement).
Use the pinned [sources and licenses](upstream-sources.md#code-analysis-exactly-one-alternative).

## Shared preparation

1. **Runtime.** Check path, version, skills and integration through established interfaces. Read manifest `source_revision` and release for complete original assets. Preserve existing/shared runtimes. Include the exact official first install and effects in upfront setup scope if absent. Report any incompatibility and obtain an update/defer decision. Before any runtime change on an existing team, obtain explicit approval of actual versions, paths and shared effects.
2. **Targets.** Reuse confirmed absolute role homes, `CODEX_HOME`, `CODEX_PROCESS_HOME` and ownership. Compare paths/options with the selected version. Preserve symlinks, local edits, project rules, foreign profiles and personal Codex config. Resolve conflicts and back up affected own config before authorized writes. After partial failure, read actual state before retrying.
3. **Corpus.** Reuse confirmed repository scope, roots, cache/output locations and watcher decision. Keep repositories separate. During setup, skip test workspaces and index/query/update experiments, including indexing secrets or project content.
4. **Hooks.** Use approved profile-local installation and activation scope. Disclose required target hook approval during preparation and perform it after final configuration.

<a id="graphify"></a>
## Graphify

### 1. Provide runtime and complete skills

Use the compatible existing Graphify runtime and its actual Python interpreter.
Read the manifest's `graphify.source_revision`, `source_release`, complete `asset_bundles` and legal hashes.
If absent and first installation is in the approved setup scope, use the official `graphifyy` release from that pinned source through the established package route.
Verify source/release provenance and installed path/version without indexing or a runtime qualification campaign.
Do not run an unversioned install or change a reused runtime to match an asset pin.

Require runtime/skill compatibility before copying the complete original bundles from the pinned source:

| Consumer | Original main file → `SKILL.md` | References → `references/` | Target directory |
|---|---|---|---|
| Planner and Reviewer | `graphify/skill-claw.md` | `graphify/skills/claw/references/` complete | `<ROLE_HOME>/skills/graphify/` |
| Team-Codex | `graphify/skill-codex.md` | `graphify/skills/codex/references/` complete | `<CODEX_PROCESS_HOME>/.agents/skills/graphify/` |

Compare full file sets and bytes with the source, including `LICENSE`, `LICENSE-MIT` and `NOTICE`. Deliver the original, complete skill.
Graphify's `graphify/install.py` maps Hermes to claw. Use the explicit profile targets above because the general installer can select personal homes and project instructions.

### 2. Bind and read back

- **Setup.** Verify native discovery/loading of the original `graphify` skill in Planner, Reviewer and Team-Codex. Bind the confirmed output CWD, corpus and runtime interpreter without generating a graph. Keep separate outputs per repository. The skill/CLI route needs no extra MCP service. Add a watcher only if its need and effects were confirmed during preparation.
- **Project use.** Retain the full original query, update, export, hook and merge references. Use `/graphify <CORPUS>`, `graphify query ...`, and `/graphify <CORPUS> --update` only for an explicitly authorized project task. Semantic document/image processing requires approved data/provider scope.

<a id="codebase-memory"></a>
## Codebase-memory-mcp (CBM)

### 1. Provide the shared runtime

Use the compatible existing original binary and record its exact path/version.
Read the manifest's `codebase-memory.source_revision` and `source_release` as the required asset source.
If absent and first installation is in the approved setup scope, use the matching official platform release and verify provenance/checksums.
Preserve an existing/shared binary unless its concrete change was approved; do not repair the daemon or cache to enforce an asset pin.
Retain its `LICENSE` and `THIRD_PARTY_NOTICES.md` provenance and use the existing runtime for profile-local client integration.

CBM uses one account-wide coordinated daemon, runtime and cache. Compare the existing build, cache and rendezvous area. Separate `HOME` and `CODEX_HOME` do not isolate the daemon or authorize updates.

Team-Codex `HOME` derives `<team-home>/.cache/codebase-memory-mcp` while the account daemon uses `<owner-home>/.cache/codebase-memory-mcp`.
When the roots differ, startup fails for every tool, even if the same call works in the parent:
`… the active account daemon uses a different cache directory (active cache <hash>;
requested cache <hash>)` (exit 1). Verify each root by comparing its path's SHA256 to the corresponding hash.

Bind the cache in the Team-Codex configuration, not in per-call environment overrides.
Team-Codex has its own `devteam/codex-home/config.toml`.
Declare the MCP server and canonical account cache there as a static literal:

```toml
[mcp_servers.codebase-memory-mcp]
command = "…/codebase-memory-mcp"
args = []

[mcp_servers.codebase-memory-mcp.env]
CBM_CACHE_DIR = "<account daemon cache directory>"
```

Set `CBM_CACHE_DIR` only in literal TOML `env`, as written by `codex mcp add --env KEY=VALUE`.
Omit `env_vars` from this entry. It passes through caller values, and an unset value triggers a `codex doctor` MCP warning. Duplicate-key precedence is unverified.
No socket binding is needed for the uid-based `/tmp/cbm-daemon-<uid>`.
`CODEX_HOME` resolves per-team config independently of process `HOME`. All teams bind the same account cache. Omit the cache override from routine Coder invocations.

Write the entry before hook approval. A later `config.toml` change invalidates the file-bound `[hooks.state.…]` trust hashes and requires renewed confirmation through `/hooks`.

If foreign or incomplete config causes a run to fail, a process-local `CBM_CACHE_DIR` in its `env` prefix is a one-run workaround. Setup still requires the TOML entry. Preserve the daemon, cache, indexes and permissions. Skip daemon stop/restart, second caches and global `export`. The warning `daemon.private_dir_group_writable_ancestor mode=0775` occurs in working contexts too.

### 2. Run the official client integration

Before running a reused binary's integration writer, verify that its generated skill, pointer, hooks and Codex agents match the pinned source contract.
Use the manifest's static source-derived evidence as source evidence, not proof of installed output.
Compare all generated original assets and applicable release legal files, not only the two recorded static hashes.
If the installed writer would produce a different asset revision, preserve it and report the exact mismatch before any write.
Use compatible pinned original client assets only through a verified supported delivery route, or defer pending the required runtime-change decision.
Do not silently update/downgrade the binary, accept different assets as current, or patch upstream bytes.

Deliver the complete original integration. CBM's Codex subagents supplement VoltAgent within Codex. Preserve Hermes team roles.
Before running, require existing role and Team-Codex homes. Use confirmed absolute `ROLE_HOME`, `CODEX_HOME`, `CODEX_PROCESS_HOME` and `CBM_BIN_DIR`. The latter contains the original binary actually used.

```sh
# Run for Planner and Reviewer with their respective ROLE_HOME.
HERMES_HOME="$ROLE_HOME" \
  "$CBM_BIN_DIR/codebase-memory-mcp" install \
  --clients=hermes --skip-binary --dir="$CBM_BIN_DIR"

# Run once for the separate Team-Codex context.
HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" \
  "$CBM_BIN_DIR/codebase-memory-mcp" install \
  --clients=codex --skip-binary --dir="$CBM_BIN_DIR"
```

`--clients=…` limits detection to existing client homes. Set `--dir` to the directory containing the binary you invoke. `--skip-binary` alone can still encounter binary conflicts. Compare adapted skill/agent files and resolve conflicts before proceeding. Avoid blanket `--force`.

**Immediately after installation and before hook approval**, bind the canonical cache in the generated team `config.toml`:

```toml
[mcp_servers.codebase-memory-mcp]
command = "<CBM_BIN_DIR>/codebase-memory-mcp"
args = []

[mcp_servers.codebase-memory-mcp.env]
CBM_CACHE_DIR = "<account daemon cache directory>"
```

The call form was statically checked against official CBM
[v0.12.1, `src/cli/cli.c`](https://github.com/DeusData/codebase-memory-mcp/blob/v0.12.1/src/cli/cli.c).
This is the manifest asset source, not a forced installed-runtime version.
For a different existing runtime, verify options, target resolution and pinned generated-asset compatibility before execution.

### 3. Check result, working context and hooks

| Context | Expected original integration |
|---|---|
| Planner and Reviewer | `skills/codebase-memory/SKILL.md`, MCP entry in `config.yaml`, shell hook `hooks.pre_llm_call` |
| Team-Codex | MCP in `config.toml`, activation pointer in `AGENTS.md`, `skills/codebase-memory/SKILL.md` |
| Team-Codex subagents | `agents/codebase-memory-scout.toml`, `agents/codebase-memory.toml` (Verify), `agents/codebase-memory-auditor.toml` |
| Team-Codex hooks | `SessionStart` and `SubagentStart`; existing `hooks.json`, otherwise native TOML storage |

- For each Hermes role, including Reviewer, read back its MCP command, environment/cache, repository CWD, original shellhook and native skill discovery/loading.
- Read back installer output and files; exit status alone does not suffice.
  Preserve other MCP entries, hooks, instructions and the VoltAgent helpers.
  Read back the activation pointer. Preserve it when applying [Team-Codex instructions](integrations.md#team-codex-instructions) after integration writes.
- Bind the actual session/MCP CWD to the respective repository. With profile home
  and binary path, the installer does not yet define an analysis root.
- Read back the `CBM_CACHE_DIR` literal in the team TOML `[mcp_servers.codebase-memory-mcp.env]` for MCP and hook configuration.
  Do not rely on caller environment inheritance. Bind Hermes MCP `env` too if its derived default differs from the shared account cache.
  Read back actual native connection/configuration status in the bound context through the established non-indexing interface.
  Do not create projects or run index/query/update experiments.
- Make required target adjustments through the supported native configuration;
  see [Hermes MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
  and [Shellhooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#shell-hooks).
  Keep original hook commands; do not add own indexing hooks.
- Obtain the disclosed native hook approval in the selected target context; Codex uses `/hooks`.
  Read back approval and configuration state after the final cache/configuration write.
  Do not start a worker to test hook behavior; definitions and approval do not prove execution.

### 4. Later project operation

Deliver the complete original `codebase-memory` skill and references.
Reserve native `list_projects`, `index_repository`, `index_status`, query and watcher/update paths for authorized project tasks. Keep indexing, graph queries, incremental updates and watcher experiments outside setup. Do not add routine reindexing on every call, message, commit or review handoff.

<a id="funktionspruefung"></a>
## Setup output boundary

- **Readback.** Selected integration, full files, native discovery, runtime/MCP command, CWD/roots, cache literal, hooks and approval state.
- **Incomplete.** Missing required Reviewer assets, configuration or native discovery keep setup or an authorized team update incomplete. Report the exact failed binding. Preserve the selected alternative.
- **Evidence.** Record configured and delivered state. Graph accuracy and live hooks require separate evidence.

## Resume, updates and rollback path

On resume, compare actual and logged targets first.
For tool updates, check versions and effects on shared runtimes, skills and hook approval. Normal index updates are separate.
Rollback only documented own entries to backed-up values. Preserve shared binaries, foreign config and indexes. Obtain separate data-deletion approval.
