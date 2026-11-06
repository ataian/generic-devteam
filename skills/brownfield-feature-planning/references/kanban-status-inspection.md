# Kanban status inspection

Use this reference for read-only triage of handoff, completion and blocker notifications.
Recheck current state because the board and workers can advance after a notification.
Keep diagnosis separate from authorization to change a task, repository or runtime.

## Read and reduce before output truncation

1. Use native `kanban_show(task_id=..., board=...)` for the exact task.
2. Use native `kanban_list(board=...)` for relevant dependency state.
3. Set the board explicitly on every call.
4. Stop extraction when native reads supply the required evidence.
5. Use `read_file` with bounded pagination for saved JSON, reports and spillover text.
6. Do not introduce Python execution or a scratch export for a routine read or acknowledgment.
7. Use authorized CLI/Python extraction only for a missing native projection or a substantial machine-validated batch.
8. Parse complete subprocess stdout inside that execution context before returning reduced fields.
9. Keep any scratch export local to the inspecting session rather than making it an inter-agent handoff dependency.
10. Keep assignments, questions and results on the existing Kanban card.
11. Report nonzero subprocess exits or malformed full JSON as read failures, not an empty board.
12. After a presentation or parser failure, re-read the existing result or exact target instead of repeating a write or release.
13. Do not relax parsing or reconstruct truncated content.
14. Do not bypass denied access or actions through another tool or command form.
15. Use an otherwise permitted native read if only the original command form was unsuitable.

Inspect actual top-level and nested keys before reusing a response schema.
Treat fields omitted by CLI JSON as unknown rather than empty claims or satisfied dependencies.
If parent-satisfaction metadata is absent, read each exact parent and require completion before relying on its gate.
If claim metadata is absent, inspect native state or available run status, end time and provenance.
If comment IDs are absent, verify one exact-task entry matching the author and distinctive posted body.
Do not repeat a successful comment or transition to repair its readback parser.

### Conditional CLI extraction

Use this read-only pattern only under the extraction conditions above.
Replace board and task variables with verified identifiers.
Keep dynamic values in argument-array elements.

```python
import json
import subprocess


def read_json(board, verb, *args):
    completed = subprocess.run(
        ["hermes", "kanban", "--board", board, verb, *args, "--json"],
        check=True, capture_output=True, text=True, timeout=30,
    )
    return json.loads(completed.stdout)


snapshot = read_json(board, "show", task_id)
runs = snapshot["runs"]
if any("id" not in run for run in runs):
    raise ValueError("Inspect run identity schema before selecting latest run")
ordered_runs = sorted(runs, key=lambda run: run["id"])
handoffs = [run for run in ordered_runs if run.get("outcome") == "review_requested"]
print(json.dumps({
    "task": {
        key: snapshot["task"].get(key)
        for key in ("id", "title", "status", "assignee", "current_run_id")
    },
    "latest_run": ordered_runs[-1:],
    "implementation_handoff": handoffs[-1:],
    "parents": snapshot.get("parents"),
}, ensure_ascii=False))
```

Select the latest run by native monotonic run ID rather than array order.
Reduce large run metadata further before returning it.
Do not use an extraction snapshot instead of a fresh state check before a consequential transition.
If output capture still truncates the payload, redirect full CLI stdout to the active profile's private scratch workspace.
Persist justified multi-task batches and compare their exact IDs and counts with the intended set.
If a machine-validated reload is needed, read raw file bytes within the already-authorized execution context.
Do not parse the line-numbered `read_file` presentation as JSON.

```python
from pathlib import Path
import json

batch = json.loads(Path(batch_path).read_text(encoding="utf-8"))
if set(batch) != set(expected_task_ids):
    raise ValueError("Persisted batch does not contain the exact intended targets")
```

## Determine the phase, not just the status label

1. Read the notified task's current run and event provenance before reporting its phase.
2. Identify the claimed role from the run's `profile` and review origin rather than `running` alone.
3. On handoff, verify reviewer assignment and the implementer's `review_requested` provenance.
4. Read the latest implementation handoff separately from the latest reviewer run.
5. Do not discard an earlier handoff because the new review run has an empty summary.
6. On completion, classify the deliverable before applying its gate.
7. For coding/product completion, require the completed independent-reviewer run, verdict, reviewed commit and test evidence.
8. For explicitly authorized bounded operator completion, require the operator's own completed run, original ownership and fulfilled result contract.
9. Do not substitute operator completion for later coding/product review.
10. Read the board to verify that only the intended immediate successor is ready or running.
11. Verify that later descendants remain parent-gated.
12. Leave successor advancement to the dispatcher.

Attribute each test result to the implementer, operator or independent reviewer who produced it.
Do not imply that the planner executed another role's tests.
If a reviewer supplies a missing check, close only that gap with the reviewer's provenance.
Preserve earlier reports as historical observations rather than retroactively changing their executor or outcome.
If full acceptance ran on an earlier tree, retain the exact-final-commit gap until the reviewer records the missing integrated run.
Do not count targeted tests as the missing full acceptance run.
Preserve unrelated resources when reporting leftover-resource caveats.

## Diagnose the current blocker

1. Read the latest blocking event, actor, reason, run outcome, relevant worker log and current Git state.
2. Inspect dispatcher diagnostics if they can change the next safe action.
3. Distinguish a failed operation from a deliberate coordination stop or a supported dependency wait.
4. If a duplicate was intentionally parked, acknowledge its existing hold rather than inventing a diagnosis, decomposition or retry.
5. Do not apply an old failure or capacity diagnosis to a different current blocker.
6. For startup failures, trace parent command, child argv, interpreter, working directory and module resolution.
7. Distinguish launcher startup, worker startup, coding-harness acceptance and completed implementation.
8. Inspect the inner harness result even if its wrapper exited successfully.
9. Do not infer a completed verdict or a code defect from truncated reviewer output.
10. If review stopped, inspect preserved review provenance and any active retry before proposing intervention.
11. Leave an active retry with its owner.
12. If execution aborted, inspect HEAD, partial changes, missing deliverables and relevant writer processes.
13. Do not infer process termination or a security denial from a timeout.
14. Treat success-looking reports from interrupted runs as provisional until supported by actual acceptance evidence.
15. If a guard blocked an operation, identify the exact attempted action and available guard evidence.
16. Distinguish file access, code execution, authentication and execution-service availability.
17. State that the cause is unknown when the concrete prompt or trace is unavailable.
18. Inspect runtime context only where needed to explain the failed boundary.
19. Do not infer worker capability from a successful operation in another profile or session.
20. Preserve mandated STOP/no-fallback rules when proposing the next action.

For an unresolved blocker, report the responsible actor, next safe action, observed evidence, impact and resumption condition.
Route the handoff to the existing card's authorized owner.
If an operator repair is needed, identify its scope, restart impact, non-secret verification and rollback.
Do not treat diagnosis as permission to change the shared gateway, profile, infrastructure or approval policy.

## Check dependency handoffs before relying on silence

1. Read the waiting card's latest run, terminal event kind and exact open parent.
2. Read its existing operator or acknowledgment prerequisite and actual edge direction.
3. Verify that an assigned next action can resolve the blocked prerequisite.
4. Read `hermes kanban --board <board> notify-list <task> --json` when delivery matters to the handoff.
5. Inspect the installed notifier's event-selection and wake policy only as needed for that event kind.
6. Recheck current behavior rather than assuming that a status label implies a notification.
7. Distinguish subscription configuration, event cursor, ping cursor, actual message delivery and coordinator acceptance.
8. Do not treat `notify+wake` as proof that every transition triggers a coordinator turn.
9. If the handoff is uncovered, report the concrete coordination gap through the authorized existing mechanism.
10. Do not promise automatic continuation, relabel a genuine wait as an error or create a diagnostic graph or watcher.

## Report the observed boundary

1. Report completed work, active execution or idle waiting first.
2. Name the last real deliverable, unfinished work, next responsible role and any genuinely required owner decision.
3. Report `ready` until an intended-profile claim proves `running` with its actual run identity.
4. Do not describe a posted clarification, acknowledgment or rewritten specification as resumed execution.
5. Keep implementation, independent review, downstream gates and product acceptance distinct.
6. Treat subscribed notifications as board events rather than necessarily human-authored instructions.
7. Do not infer continuous log monitoring or an aggregate completion hook from the event stream.

If operator-result receipt or canonical session correlation is required, load the [operator-executed verification contract](operator-script-acceptance.md#operator-executed-verification-contract).
If the owner authorizes scope or graph changes, load [phase release](kanban-phase-release.md#narrow-scope-without-stopping-the-accepted-delivery).
If a blocker is resolved or a run was interrupted, load [safe resumption](kanban-triage-recovery.md#resume-after-a-blocker-or-interrupted-run).
