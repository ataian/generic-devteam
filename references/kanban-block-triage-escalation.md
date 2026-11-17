# Board configuration for setup

Identify the existing dispatcher home, board DB and selected team profiles before writes.
Require effective `kanban.auto_decompose=false` before task release.
The switch is global to its Hermes home and is read each tick; it does not disable native repeated-block routing to `triage`.
A `triage` state alone authorizes neither decomposition nor new cards.
Preserve existing cards, edges, claims and history during setup.
Do not run fan-out experiments, repair task graphs, reset counters, or patch the kernel.
Copy and bind the complete existing Planner recovery skill through [Setup](setup.md#bind-the-planner-recovery-invocation).
Later recovery uses that installed skill under its own approval and claim rules.

## Set the homes and the readback that counts

Execute writes below only where effective `false` is missing and the change is authorized at a supported management layer.
Use the selected actual dispatcher home or role profile; do not target unrelated profiles.

```sh
hermes config set kanban.auto_decompose false              # home that dispatches
hermes -p <ROLE> config set kanban.auto_decompose false    # each profile copy
hermes config get kanban.auto_decompose                     # read back both forms
```

- `-p <profile>` is the profile selector for config commands even when the top-level
  `--help` does not list it. Do not infer from that omission that the form is unsupported,
  and do not edit YAML by hand.
- Identify the actual dispatcher owner and selected team profiles. Read their effective values; do not inventory or modify unrelated profiles without a concrete authorized shared effect.
- Accept an already effective `false` on a supported authorized management layer. Otherwise back up and change only the authorized setting; read back the exact delta. Do not override central restrictions.
- **No restart.** `_resolve_auto_decompose_settings()`
  (`gateway/kanban_watchers_common.py`) is called fresh on every tick; a restart changes
  nothing. With unreadable configuration it returns `(False, 3)`, so it falls back to off
  safely.
- **Prove it where the dispatcher reads, not where the write happened.**
  Call the same resolver with the gateway's interpreter and installation directory:

  ```sh
  cd "$HERMES_HOME" && HERMES_HOME="$HERMES_HOME" <gateway-python> -c "
  import sys; sys.path.insert(0, '<installation-directory>')
  from hermes_cli.config import load_config
  from gateway.kanban_watchers_common import _resolve_auto_decompose_settings
  print(_resolve_auto_decompose_settings(load_config))"
  ```

  `(False, N)` is the gate the next tick evaluates — that is the write that arrived.
  `(True, N)` means: the dispatcher reads something other than what the file says.


## Interpreter and result

Use `packages.venv.environment/bin/python` from the active installed PM generation's runtime facts.
Do not use `/proc/<PID>/exe` as the venv interpreter; it can resolve to the base executable and lose dependencies.
Use the actual gateway installation directory and home in the resolver recipe above.
Do not bootstrap the ordinary Hermes CLI solely to query the resolver if that would trigger PM synchronization.
Require `(False, N)` with the intended valid configuration source; a safe fallback after unreadable configuration does not prove a correct binding.
Read back the owner and selected profile effective values; no live task or gateway restart is required.
If the supported resolver/interface is unavailable, report that concrete limitation rather than investigating or patching it during setup.
Configuration evidence does not guarantee future agent or decomposer behavior.
