# Set up code analysis

Configure the **Graphify or CBM** alternative confirmed in [Setup](setup.md) for Planner, Coder, Reviewer and Team-Codex.
For existing teams, restore missing selected analysis assets and bindings through the approved [upstream companion update](update.md#required-upstream-companion-update).
The [required Reviewer skill retirement](update.md#required-reviewer-skill-retirement-1122) covers only the three unrelated retired skills.
Sources and licenses are listed in [Sources](upstream-sources.md#code-analysis-exactly-one-alternative).
Execute this recipe only during authorized target setup or the approved [upstream companion update](update.md#required-upstream-companion-update), not Maker authoring.

## Shared preparation

1. Check the selected existing runtime, version, skills and integration availability through established interfaces.
   Read the selected component's `source_revision` and release from the manifest for its complete original assets.
   Preserve existing/shared runtimes; asset pins do not authorize runtime changes.
   If absent, include the exact official first-installation target and effects in the upfront setup scope.
   If existing assets/runtime cannot satisfy the pin together, report the concrete mismatch and obtain the required update/defer decision.
   At team-update time, obtain advance explicit approval for any runtime change with actual versions, paths and shared effects.
2. Reuse confirmed absolute role homes, `CODEX_HOME`, `CODEX_PROCESS_HOME` and target ownership from preparation.
   Preserve symlinks/local edits and back up affected own configuration before authorized changes.
3. Consume the confirmed repository/corpus scope, roots, cache/output locations and optional watcher decision.
   Keep multiple repositories separate. Do not index secrets or project content during setup.
4. Use the agreed profile-local installation and activation scope.
   Disclose target-dependent hook approval during preparation; execute it only after final configuration.
   Do not create a test workspace or run index/query/update experiments.

Compare the following paths and options with the selected version at target setup.
Existing project rules, foreign profiles and personal Codex configuration stay
outside team setup. Resolve conflicts with existing files before writing;
on partial failures, read the actual state instead of blindly reinstalling.

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
| Planner, Coder and Reviewer | `graphify/skill-claw.md` | `graphify/skills/claw/references/` complete | `<ROLE_HOME>/skills/graphify/` |
| Team-Codex | `graphify/skill-codex.md` | `graphify/skills/codex/references/` complete | `<CODEX_PROCESS_HOME>/.agents/skills/graphify/` |

Include the `LICENSE`, `LICENSE-MIT` and `NOTICE` belonging to the package. Compare
complete file sets and contents with the source; do not build an own skill version.
The Hermes mapping to the claw variant follows from Graphify's `graphify/install.py`.
Its general installer can describe personal default homes and project instructions;
therefore use the explicit targets for this profile-related skill store.

### 2. Bind and read back

Verify native discovery/loading of the original `graphify` skill in Planner, Coder, Reviewer and Team-Codex.
Bind the confirmed output CWD, corpus and runtime interpreter without generating a graph.
For multiple repositories retain separate output locations.
No additional MCP service is required for the normal skill/CLI route.
Do not add a watcher unless its need and effects were confirmed during preparation.
Keep the complete original query, update, export, hook and merge references for later operational tasks.
Later `/graphify <CORPUS>`, `graphify query ...`, and `/graphify <CORPUS> --update` belong to an explicitly authorized project task.
Semantic document/image processing requires its own approved data/provider scope.

<a id="codebase-memory"></a>
## Codebase-memory-mcp (CBM)

### 1. Provide the shared runtime

Use the compatible existing original binary and record its exact path/version.
Read the manifest's `codebase-memory.source_revision` and `source_release` as the required asset source.
If absent and first installation is in the approved setup scope, use the matching official platform release and verify provenance/checksums.
Preserve an existing/shared binary unless its concrete change was approved; do not repair the daemon or cache to enforce an asset pin.
Retain its `LICENSE` and `THIRD_PARTY_NOTICES.md` provenance and use the existing runtime for profile-local client integration.

CBM uses an account-wide coordinated daemon. Consider the existing build, cache and
rendezvous area; a different `HOME` or `CODEX_HOME` does not isolate an own CBM daemon.
All consumers must reach the same compatible runtime and cache context. Do not
update the existing shared runtime in passing.

A deviating process `HOME` changes the **derived** default cache: with the
Team-Codex `HOME`, the client derives `<team-home>/.cache/codebase-memory-mcp`,
while the running account daemon uses `<owner-home>/.cache/codebase-memory-mcp`.
Startup then aborts for every tool with
`… the active account daemon uses a different cache directory (active cache <hash>;
requested cache <hash>)` (exit 1), although the same call works in the parent
context. The two identifiers in the error text are the SHA256 of the respective paths —
that proves the root instead of guessing.

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

`env` carries literal values (exactly how `codex mcp add --env KEY=VALUE` writes them); `env_vars`,
by contrast, only passes through what the caller has in its environment, and therefore **does not**
belong in this entry: a declared but nowhere set variable stays empty and produces in
`codex doctor` an MCP warning that looks like a defect. Both keys are siblings
in the same entry, in case a value from the runtime environment should come later; for CBM
none does today — the daemon socket lies uid-based under `/tmp/cbm-daemon-<uid>`, not
under `HOME`, and needs no binding. `CBM_CACHE_DIR` belongs exclusively in `env` — the
precedence rule for duplication is not proven, so do not build on it. The configuration file
is found through `CODEX_HOME`, not through `HOME`: the binding therefore applies **per team/role**,
independently of which process `HOME` the run starts under. All teams bind **the same**
root; there is exactly one account daemon, so also only one correct one. Thus no
Coder run needs the line in the `env` prefix.

**Order:** write the entry **before** the hook approval is granted. The
`[hooks.state.…]` trust hashes bind to the file content; a subsequently changed
`config.toml` invalidates them and forces a renewed confirmation through `/hooks`.

If the binding fails in a run nonetheless (foreign or incomplete configuration), a
process-local `CBM_CACHE_DIR` in the `env` prefix is a makeshift for this one run — no
setup and no replacement for the entry. No daemon stop/restart, no second cache,
no cache/index deletion, no permission change, no global `export`. The warning
`daemon.private_dir_group_writable_ancestor mode=0775` also appears in working
contexts and is not the cause.

### 2. Run the official client integration

Before running a reused binary's integration writer, verify that its generated skill, pointer, hooks and Codex agents match the pinned source contract.
Use the manifest's static source-derived evidence as source evidence, not proof of installed output.
Compare all generated original assets and applicable release legal files, not only the two recorded static hashes.
If the installed writer would produce a different asset revision, preserve it and report the exact mismatch before any write.
Use compatible pinned original client assets only through a verified supported delivery route, or defer pending the required runtime-change decision.
Do not silently update/downgrade the binary, accept different assets as current, or patch upstream bytes.

Use the complete original integration, **including the CBM's own
Codex subagents**. They complement the VoltAgent helpers inside Codex and
do not change the Hermes team roles.

Before the following calls, the role homes and the Team-Codex home must already
exist. `ROLE_HOME`, `CODEX_HOME`, `CODEX_PROCESS_HOME` and `CBM_BIN_DIR` are
confirmed absolute paths. Under `CBM_BIN_DIR` lies the actually used
original binary `codebase-memory-mcp`.

```sh
# Run for Planner, Coder and Reviewer with their respective ROLE_HOME.
HERMES_HOME="$ROLE_HOME" \
  "$CBM_BIN_DIR/codebase-memory-mcp" install \
  --clients=hermes --skip-binary --dir="$CBM_BIN_DIR"

# Run once for the separate Team-Codex context.
HOME="$CODEX_PROCESS_HOME" CODEX_HOME="$CODEX_HOME" \
  "$CBM_BIN_DIR/codebase-memory-mcp" install \
  --clients=codex --skip-binary --dir="$CBM_BIN_DIR"
```

`--clients=…` limits the detected clients; it does not create their homes.
`--dir` denotes the binary directory, not the profile or repository.
Call the same binary from the same directory: `--skip-binary` alone does not prevent
every target binary conflict. Work without a blanket `--force`; compare existing
adapted skill/agent files and resolve conflicts deliberately.

**Directly afterwards, write the canonical CBM cache into the generated team `config.toml`**
— as a mandatory part of the setup, not as an addendum, and **before** the hook approval
(reason in section 1):

```toml
[mcp_servers.codebase-memory-mcp]
command = "<CBM_BIN_DIR>/codebase-memory-mcp"
args = []

[mcp_servers.codebase-memory-mcp.env]
CBM_CACHE_DIR = "<account daemon cache directory>"
```

Without this literal value the client derives the cache from the deviating team `HOME`
and refuses every call. All teams carry **the same** root — the one
account-wide cache. Add no `env_vars` line: it would stay empty and appear in
`codex doctor` as an MCP warning.

The call form was statically checked against official CBM
[v0.12.1, `src/cli/cli.c`](https://github.com/DeusData/codebase-memory-mcp/blob/v0.12.1/src/cli/cli.c).
This is the manifest asset source, not a forced installed-runtime version.
For a different existing runtime, verify options, target resolution and pinned generated-asset compatibility before execution.

### 3. Check result, working context and hooks

| Context | Expected original integration |
|---|---|
| Planner, Coder and Reviewer | `skills/codebase-memory/SKILL.md`, MCP entry in `config.yaml`, shell hook `hooks.pre_llm_call` |
| Team-Codex | MCP in `config.toml`, activation pointer in `AGENTS.md`, `skills/codebase-memory/SKILL.md` |
| Team-Codex subagents | `agents/codebase-memory-scout.toml`, `agents/codebase-memory.toml` (Verify), `agents/codebase-memory-auditor.toml` |
| Team-Codex hooks | `SessionStart` and `SubagentStart`; existing `hooks.json`, otherwise native TOML storage |

- For each Hermes role, including Reviewer, read back its MCP command, environment/cache, repository CWD, original shellhook and native skill discovery/loading.
- Read back installer output and files; exit status alone does not suffice.
  Other MCP entries, hooks, instructions and the VoltAgent helpers must be preserved.
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

Deliver the complete original `codebase-memory` skill and its references.
Later authorized project tasks use its native `list_projects`, `index_repository`, `index_status`, query and watcher/update paths.
Do not require indexing, graph relationships, incremental updates or watcher experiments to complete setup.
Do not add repeated reindexing on each call, message, commit, or review handoff.

<a id="funktionspruefung"></a>
## Setup output boundary

Read back the chosen integration, complete file set, native discovery, runtime/MCP command,
CWD/roots, cache literal, hooks and approval state.
Missing required Reviewer assets, configuration or native discovery keep setup or an authorized team update incomplete.
A readback proves configuration/delivery, not graph accuracy or live hook behavior.
Report an actual failed binding precisely; do not silently switch alternatives.

## Resume, updates and rollback path

On resume, first compare the logged target state. Distinguish tool updates
from normal index updates; check new versions together with their effects
on the shared runtime, skill files and hook approval. For a rollback,
revoke only the documented own entries deliberately and restore secured
values. Preserve shared binaries, foreign configuration and indexes;
authorize data deletion separately.