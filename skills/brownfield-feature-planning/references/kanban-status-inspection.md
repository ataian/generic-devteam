# Kanban status inspection

Trigger: handoff, completion, or blocker notification. Recheck current state. The board and workers may have advanced. Read-only diagnosis grants no task, repository, or runtime change authority.

## Read and reduce before output truncation

1. Read exact task with `kanban_show(task_id=..., board=...)`. Use `kanban_list(board=...)` for relevant dependencies. Set the board on every call. Stop extraction when native reads supply the evidence.
2. Use bounded `read_file` pagination for saved JSON, reports, and spillover. Routine reads and acknowledgments need no Python or scratch export.
3. Use authorized CLI/Python extraction only for a missing native projection or a substantial machine-validated batch. Parse complete subprocess stdout in that execution context before returning selected fields. Keep scratch exports local to the inspecting session. Put assignments, questions, and results on the existing card.
4. Report nonzero subprocess exits or malformed full JSON as read failures, not an empty board. If presentation or parsing fails, re-read the existing result/exact target. Do not repeat writes, comments, or releases. Never relax parsing or reconstruct truncated content.
5. Do not bypass denied access/actions through another tool or command form. If only the command form is unsuitable, use a permitted native read.

Inspect actual top-level and nested keys before reusing a schema. Omitted CLI JSON fields are unknown. Handle missing metadata by field:

- Parent satisfaction: read each exact parent and require completion before relying on its gate.
- Claim: inspect native state or available run status, end time, and provenance.
- Comment ID: verify one exact-task entry matching author and distinctive posted body. Do not repeat a successful comment or transition to repair readback parsing.

### Conditional CLI extraction

Use this read-only pattern only under the extraction conditions above. Use verified board/task identifiers and keep dynamic values in argument-array elements.

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

- Select latest run by native monotonic run ID. Array order is insufficient. Reduce large metadata before returning it. Recheck fresh state before consequential transitions.
- If capture still truncates, redirect full CLI stdout to active-profile private scratch. For justified multi-task batches, persist and compare exact IDs and counts to the intended set.
- For machine-validated reload, read raw file bytes within the already-authorized execution context. Never parse line-numbered `read_file` output as JSON.

```python
from pathlib import Path
import json

batch = json.loads(Path(batch_path).read_text(encoding="utf-8"))
if set(batch) != set(expected_task_ids):
    raise ValueError("Persisted batch does not contain the exact intended targets")
```

## Determine the phase, not just the status label

1. Read current run and event provenance on the notified task before reporting phase. Determine claimed role from run `profile` and review origin. The `running` label alone is insufficient.
2. On handoff, verify reviewer assignment and implementer `review_requested` provenance. Read the latest implementation handoff separately from the latest reviewer run. An empty review summary does not erase the earlier handoff.
3. On completion, classify delivery and apply its gate:
   - Coding/product: require completed independent-reviewer run, verdict, reviewed commit, and test evidence.
   - Explicitly authorized bounded operator work: require the operator's own completed run, original ownership, and fulfilled result contract. Later coding/product review still applies.
4. Read the board. Verify that only the intended immediate successor is ready/running and later descendants remain parent-gated. Leave advancement to the dispatcher.

- Attribute checks to the actual implementer, operator, or independent reviewer. A Planner report does not establish Planner execution. A reviewer-supplied check closes only its gap with reviewer provenance. Preserve earlier reports as historical observations with their original executor and outcome.
- Explicit final-state integrated run: keep the gate open until the required run is evidenced and assessed by the reviewer. Targeted tests cannot satisfy a required full run.
- Otherwise, require reviewer assessment of valid prior results and reruns for changed inputs and their effects. Preserve unrelated resources when reporting leftover-resource caveats.

## Diagnose the current blocker

1. Read latest blocking event, actor, reason, run outcome, relevant worker log, and Git state. Inspect dispatcher diagnostics only if they can change the next safe action.
2. Classify failure, deliberate coordination stop, or supported dependency wait. For an intentionally parked duplicate, acknowledge the hold. Do not invent diagnosis, decomposition, or retry. Do not reuse an old failure/capacity diagnosis for a different blocker.
3. Inspect the applicable boundary:
   - Startup: trace parent command, child argv, interpreter, working directory, and module resolution. Distinguish launcher startup, worker startup, coding-harness acceptance, and completed implementation. Check the inner harness result even if its wrapper succeeded.
   - Stopped review: check preserved provenance and active retries before intervening. Leave active retry with its owner. Truncated reviewer output proves neither verdict nor code defect.
   - Aborted execution: inspect HEAD, partial changes, missing deliverables, and relevant writers. A timeout proves neither termination nor security denial. Treat apparent success from interrupted runs as provisional until backed by acceptance evidence.
   - Guard: identify exact attempted action and available guard evidence. Distinguish file access, code execution, authentication, and execution-service availability. Without the concrete prompt or trace, report cause unknown.
4. Inspect runtime context only as needed for the failed boundary. Capability in another profile/session proves no capability here. Preserve mandated STOP/no-fallback rules.

For unresolved blockers, report actor, next safe action, observed evidence, impact, and resumption condition to the existing card's authorized owner. For operator repair, include scope, restart impact, non-secret verification, and rollback. Diagnosis grants no shared gateway, profile, infrastructure, or approval-policy changes.

## Check dependency handoffs before relying on silence

1. Read waiting card's latest run, terminal event kind, exact open parent, existing operator/acknowledgment prerequisite, and actual edge direction. Verify an assigned next action can resolve the prerequisite.
2. When delivery matters, read `hermes kanban --board <board> notify-list <task> --json`. Inspect installed notifier selection/wake policy only as needed for the actual event kind. Recheck behavior rather than inferring delivery from status.
3. Distinguish subscription configuration, event cursor, ping cursor, actual message delivery, and coordinator acceptance. `notify+wake` does not prove every transition triggers a coordinator turn.
4. If uncovered, report the concrete coordination gap through the existing authorized mechanism. Do not promise automatic continuation, relabel a genuine wait as an error, or add a diagnostic graph/watcher.

## Report the observed boundary

- Lead with completed work, active execution, or idle waiting. Include last real deliverable, unfinished work, next responsible role, and any genuinely required owner decision.
- Report `ready` until an intended-profile claim proves `running` with its actual run identity. A clarification, acknowledgment, or rewritten specification is no execution evidence.
- Distinguish implementation, independent review, downstream gates, and product acceptance.
- Treat subscribed notifications as board events. Do not assume human authorship, continuous log monitoring, or an aggregate completion hook.

If operator-result receipt or canonical session correlation is required, load the [operator-executed verification contract](operator-script-acceptance.md#operator-executed-verification-contract).
If the owner authorizes scope or graph changes, load [phase release](kanban-phase-release.md#narrow-scope-without-stopping-the-accepted-delivery).
If a blocker is resolved or a run was interrupted, load [safe resumption](kanban-triage-recovery.md#resume-after-a-blocker-or-interrupted-run).
