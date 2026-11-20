# Board configuration for setup

- **Target.** Identify the existing dispatcher home, board DB and selected profiles before writes. Require effective `kanban.auto_decompose=false` before task release.
- **Boundary.** Preserve cards, edges, claims and history. Skip fan-out experiments, graph repairs, counter resets and kernel patches.
- **Recovery.** Native repeated-block routing to `triage` continues. The state alone grants no authority to decompose or create cards. Copy and bind the complete Planner recovery skill through [Setup](setup.md#bind-the-planner-recovery-invocation). Later recovery follows that skill's approval and claim rules.

## Set the homes and the readback that counts

Write only in the actual dispatcher home or selected profile, when effective `false` is missing and the management layer is supported and authorized.

```sh
hermes config set kanban.auto_decompose false              # home that dispatches
hermes -p <ROLE> config set kanban.auto_decompose false    # each profile copy
hermes config get kanban.auto_decompose                     # read back both forms
```

- Use `-p <profile>` for config commands even if top-level `--help` omits it. Do not edit YAML by hand.
- Read effective values for the dispatcher owner and selected profiles. Inspect or change unrelated profiles only for a concrete authorized shared effect.
- Accept an effective `false` from a supported authorized layer. Otherwise back up and change only the authorized setting. Verify the exact delta. Preserve central restrictions.
- **No restart.** Each tick calls `_resolve_auto_decompose_settings()` in `gateway/kanban_watchers_common.py`. Unreadable config falls back to `(False, 3)`.
- Run the dispatcher resolver with the gateway's interpreter and installation directory to prove the effective binding:

  ```sh
  cd "$HERMES_HOME" && HERMES_HOME="$HERMES_HOME" <gateway-python> -c "
  import sys; sys.path.insert(0, '<installation-directory>')
  from hermes_cli.config import load_config
  from gateway.kanban_watchers_common import _resolve_auto_decompose_settings
  print(_resolve_auto_decompose_settings(load_config))"
  ```

  `(False, N)` is the next tick's gate. If the file says `false` but the result is `(True, N)`, resolve the effective source.

## Interpreter and result

- **Interpreter.** Use `packages.venv.environment/bin/python` from the active installed PM generation's runtime facts, the actual gateway installation directory and its home. Avoid `/proc/<PID>/exe` because it can resolve to the base executable and lose venv dependencies. Skip CLI bootstrap for this query if it triggers PM synchronization.
- **Readback.** Require `(False, N)` from the intended valid source. An unreadable file can produce the safe fallback without proving the binding. Report effective values for owner and selected profiles without a live task or restart.
- **Failure.** Report the exact unsupported interface or resolver. Keep setup free of investigation and patches. Record the configuration result separately from future agent or decomposer behavior.
