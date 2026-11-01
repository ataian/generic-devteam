# Board configuration for setup

Identify the existing dispatcher home, board DB and selected team profiles before writes.
Require effective `kanban.auto_decompose=false` before task release.
The switch is global to its Hermes home and is read each tick; it does not disable native repeated-block routing to `triage`.
A `triage` state alone authorizes neither decomposition nor new cards.
Preserve existing cards, edges, claims and history during setup.
Do not run fan-out experiments, repair task graphs, reset counters, or patch the kernel.
Copy and bind the complete existing Planner recovery skill through [Setup](setup.md#bind-the-planner-recovery-invocation).
Later recovery uses that installed skill under its own approval and claim rules.

## 5. Setzen: welche Homes, und der Rücklese-Nachweis, der wirklich zählt

Execute writes below only where effective `false` is missing and the change is authorized at a supported management layer.
Use the selected actual dispatcher home or role profile; do not target unrelated profiles.

```sh
hermes config set kanban.auto_decompose false              # Home, das dispatcht
hermes -p <ROLLE> config set kanban.auto_decompose false    # jede Profilkopie
hermes config get kanban.auto_decompose                     # beide Formen zurücklesen
```

- `-p <profil>` ist der Profilselektor für Config-Befehle, auch wenn die
  Top-Level-`--help` ihn nicht aufführt — daraus nicht ableiten, die Form sei nicht
  unterstützt, und nicht von Hand YAML editieren.
- Identify the actual dispatcher owner and selected team profiles. Read their effective values; do not inventory or modify unrelated profiles without a concrete authorized shared effect.
- Accept an already effective `false` on a supported authorized management layer. Otherwise back up and change only the authorized setting; read back the exact delta. Do not override central restrictions.
- **Kein Neustart.** `_resolve_auto_decompose_settings()`
  (`gateway/kanban_watchers_common.py`) wird jeden Tick frisch gerufen; ein Neustart
  ändert nichts. Bei unlesbarer Config liefert es `(False, 3)`, fällt also sicher
  auf aus.
- **Dort nachweisen, wo der Dispatcher liest, nicht dort, wo geschrieben wurde.**
  Denselben Resolver mit dem Interpreter und Installationsverzeichnis des Gateways
  aufrufen:

  ```sh
  cd "$HERMES_HOME" && HERMES_HOME="$HERMES_HOME" <gateway-python> -c "
  import sys; sys.path.insert(0, '<installationsverzeichnis>')
  from hermes_cli.config import load_config
  from gateway.kanban_watchers_common import _resolve_auto_decompose_settings
  print(_resolve_auto_decompose_settings(load_config))"
  ```

  `(False, N)` ist das Gate, das der nächste Tick auswertet — das ist das
  angekommene Schreiben. `(True, N)` heißt: der Dispatcher liest etwas anderes als
  die Datei sagt.


## Interpreter and result

Use `packages.venv.environment/bin/python` from the active installed PM generation's runtime facts.
Do not use `/proc/<PID>/exe` as the venv interpreter; it can resolve to the base executable and lose dependencies.
Use the actual gateway installation directory and home in the resolver recipe above.
Do not bootstrap the ordinary Hermes CLI solely to query the resolver if that would trigger PM synchronization.
Require `(False, N)` with the intended valid configuration source; a safe fallback after unreadable configuration does not prove a correct binding.
Read back the owner and selected profile effective values; no live task or gateway restart is required.
If the supported resolver/interface is unavailable, report that concrete limitation rather than investigating or patching it during setup.
Configuration evidence does not guarantee future agent or decomposer behavior.
