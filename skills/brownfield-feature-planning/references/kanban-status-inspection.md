# Kanban status inspection

Use for read-only triage of handoff, completion and blocker notifications when the board and worker can advance between the notification and the response.

## Read and reduce before output truncation

1. Use native `kanban_show(task_id=..., board=...)` for the exact task and `kanban_list(board=...)` for dependency state. Always set the board explicitly. If these supply the required evidence, stop there; do not add a scratch export and code-execution step to every routine status read.
2. Use the CLI/Python recipes below only when a missing native projection or a substantial batch justifies extraction and that execution context is authorized. Consume the full subprocess stdout within Python, parse there, then print only the required fields. Passing a large CLI response through a terminal tool and calling `json.loads` on that tool's displayed text can parse a truncated prefix instead of the actual JSON. Keep exported scratch files local to the inspecting session; publish the actual assignment/result on Kanban and link durable project reports, so another worker does not need access to a different profile's scratch directory.
3. Keep failures honest: a nonzero subprocess exit or malformed full JSON is not an empty board. Raise/report it and retry a structured read; do not infer success or perform compensating writes.
4. For ordinary inspection of persisted JSON or spillover, use `read_file` with bounded pagination and read the needed fields as text; no JSON decoder or code-execution permission is needed. Only if a justified machine-validated batch requires parsing, consume raw bytes inside its already-authorized execution context: line-number prefixes and pagination in the human-facing `read_file` presentation are not JSON payload. Do not create that execution dependency for a routine task read. Re-read the existing result after a presentation mismatch; do not repeat board writes or releases.

For a complete batch stored in your own scratch workspace, a raw-file reload within an authorized Python execution context is:

```python
from pathlib import Path
import json

batch = json.loads(Path(batch_path).read_text(encoding="utf-8"))
if set(batch) != set(expected_task_ids):
    raise ValueError("Persisted batch does not contain the exact intended targets")
```

This reload reads an existing artifact; it is not permission to rerun a denied command through Python or another tool.

Reusable read-only recipe (replace board and task arguments with verified identifiers; keep dynamic values as argument-array elements):

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
# Check the actual projection rather than manufacturing an empty run list.
runs = snapshot["runs"]
if any("id" not in run for run in runs):
    raise ValueError("Inspect run identity schema before selecting latest run")
# Native run IDs are monotonically assigned; do not assume array order.
ordered_runs = sorted(runs, key=lambda run: run["id"])
implementation_handoffs = [
    run for run in ordered_runs if run.get("outcome") == "review_requested"
]
print(json.dumps({
    "task": {
        key: snapshot["task"].get(key)
        for key in ("id", "title", "status", "assignee", "current_run_id")
    },
    "latest_run": ordered_runs[-1:],
    "implementation_handoff": implementation_handoffs[-1:],
    "parents": snapshot.get("parents", []),
}, ensure_ascii=False))
```

Reduce the returned run metadata further if it is large. The code is a read-only extraction pattern, not a substitute for checking live state before a write. Inspect top-level and nested keys before using one response surface as the schema for another: CLI JSON may omit fields exposed by native tools. Treat an omitted CLI field as unknown, not as proof of an empty value or no active run. When parent-satisfaction metadata is omitted, fetch each exact parent and require its completed state before release. When claim metadata is omitted, inspect available run statuses/end times and provenance or use a native read. For comment readback, use a returned comment ID only when the read surface actually exposes it; otherwise match the exact target task, author and distinctive posted body, and require one matching entry. Do not hide schema mismatches behind defaults that manufacture an empty claim or satisfied dependency. After a verification parser fails following a successful comment or transition, re-read the exact target and verify its current state; do not repeat the write to repair the parser.

## Determine the phase, not just the status label

- On handoff, verify reviewer assignment and the `review_requested` provenance. A reviewer claim may change `review` to `running`; an empty latest run summary does not erase the prior implementer's handoff.
- On completion, classify the deliverable before applying its gate. Coding/product completion requires a completed independent-reviewer run and verdict. An explicitly authorized bounded operator completion requires the operator's own completed run, original ownership and fulfilled result contract; it does not substitute for the later coding/product review. Read the board to verify only the intended immediate successor is ready or running and later descendants remain parent-gated. Leave the dispatcher in control.
- On blocker, inspect the latest blocking event, its actor/reason, run outcome, relevant log and current Git state. Distinguish a newly failed operation from notification of a deliberate coordination stop; an intentionally parked duplicate needs acknowledgment of the existing hold, not new diagnosis, decomposition or retry. Historical capacity errors must not authorize retry of a different current blocker.
- Attribute evidence: say the implementer reports a test result, or the reviewer records an independently executed result. Do not imply the planner ran those tests.
- Keep a named final-commit acceptance gap visible until a reviewer supplies the missing integrated execution. Preserve unrelated resources; a leftover-resource caveat is not cleanup authorization.

## Check dependency handoffs before relying on silence

1. Read the waiting card's latest run, actual terminal event kind and exact open parent. Then read the existing operator/acknowledgment successor. Distinguish a supported dependency wait from a failed operation; a waiting consumer cannot advance while its prerequisite remains blocked without an assigned next action.
2. Read `hermes kanban --board <board> notify-list <task> --json` and inspect the installed notifier's event-selection and wake policy only as needed to establish whether this specific handoff can reach its coordinator. Match the actual event kind, not the human-facing status label. Recheck current behavior rather than preserving a negative claim about a particular event across installations.
3. Separate configured subscription, event cursor, ping cursor, actual delivered message and coordinator acceptance. A correctly bound `notify+wake` subscription is not evidence that every transition triggers notification. If the required handoff is uncovered, do not claim automatic continuation, reclassify a genuine wait as an error, create a new diagnostic graph or silently add a watcher. Route the concrete coordination gap through the authorized existing mechanism and state the limitation plainly.
4. On a status inquiry, report completion versus active work versus idle waiting first, followed by the last real deliverable and the specific unfinished team work. Read back any authorized change before reporting that execution resumed; a comment alone is neither a release nor a worker claim.

## Prove result receipt without taking another worker's claim

1. Read the exact operator card, original run/event provenance, complete central result report and existing acknowledgment card. Compare task, run profile, claim/spawn values and real parent direction; a result summary or display name alone is insufficient.
2. Read `hermes kanban --board <board> notify-list <operator-task> --json` and match the intended platform/chat/thread/user/profile/mode. Correlate its cursor and ping with the actual terminal event received in the current conversation. A cursor alone is not proof that a person or agent read and accepted the report; record the actual receipt and explicit assessment. State which destination was observed rather than claiming acknowledgment in every subscribed destination.
3. If numeric event IDs are required but the native projection omits them, use an authorized read-only exact-task query against the verified board database; do not infer IDs from event order or timestamps. A reusable query, bound with a verified task value, is `SELECT id, task_id, kind, run_id, created_at, payload FROM task_events WHERE task_id = ? AND kind IN ('claimed', 'spawned', 'completed') ORDER BY id`. Use a read-only connection, such as `sqlite3.connect('file:' + db_path + '?mode=ro', uri=True)`, and parameterized values. Do not load write handlers or mutate the database to repair missing projection fields. When read access is unavailable, retain the observed kind/time/run/payload tuple and state the numeric-ID limitation.
4. Write a separate central receipt record with the observed event/run/session association, exact report read, bounded acceptance, missing evidence and next step. If the incoming notification exposes no platform post ID, mark it unavailable instead of inventing one. Preserve the operator report's earlier statement that receipt was pending; the new receipt supplements its observation time rather than falsifying history.
5. If the acknowledgment card already has an active run, post the receipt link and verified original provenance to that exact card, then read the comment back. Do not complete, reclaim, redispatch or overwrite the active worker's report. Report the bounded operator result as accepted, the acknowledgment task by its actual status, and the later coding/review/deployment gates as still pending.

This procedure verifies one real communication boundary. Do not promote it into proof of reviewer return, approval-capable execution, complete phase acceptance or a hard deployment gate.

## Narrow scope without stopping the accepted delivery

Use when the owner rejects an expanded side workflow but still wants the original executable delivered. This is not authority to resume a cancelled project, add functionality, bypass a denial or weaken a data-safety gate.

1. Read the exact existing coding card and current board with native tools. Check its run, repository state and relevant writer processes before changing ownership; use current evidence rather than a queued notification. State whether work is running, ready or idle and whether any input is genuinely missing.
2. Recover the agreed instruction when newer documentation has obscured it. Map its commands to the existing implementation and write a bounded remaining-work specification: inputs, executable output, affected files, relevant safety checks, finite verification, commit and independent review. Do not rewrite a working importer or build a new test platform merely to simplify the entry point.
3. Park obsolete runnable successors before releasing the narrowed task: `hermes kanban --board <board> assign <obsolete-task> none`. Replace their active body instructions with the explicit hold and historical-reference status; do not falsely complete them. Temporarily unassign the coding card if necessary to prevent dispatch during graph edits.
4. Update the existing coding body through `hermes kanban --board <board> edit <coding-task> --body <body-text>`, referencing the durable specification and explicitly superseding obsolete attachments. Remove only an abandoned-scope prerequisite using `hermes kanban --board <board> unlink <obsolete-parent> <coding-task>`. Preserve dependencies that still protect the requested mutation; removing an obsolete lifecycle prerequisite does not prove that lifecycle checks passed.
5. Read back the exact body, remaining parents, parked successors and notification route. Confirm the required parents are fulfilled and the previous writer has ended. Restore the intended coding assignee using the supported `assign` command, then release with native `kanban_unblock(task_id=..., board=...)`. Do not reset recurrence counters, reclassify capability failures or manually claim/dispatch.
6. Use a bounded native `kanban_list` filtered by the assignee and status to check dispatcher pickup. Report `ready` until the current card has a real intended-profile claim; report `running` with its actual new run identity after pickup. A rewritten specification or posted comment is not resumed execution. Keep coding, review and verified import results distinct: restarting delivery is progress, not a finished product.

## Resume a blocked card after coordinator acknowledgment

Use when the existing acknowledgment card has actually completed and its deliverable resolves the original blocker. Do not apply this procedure to a still-running acknowledgment or an unresolved execution/security denial.

1. Read the acknowledgment's complete report, original completed run and terminal event, then re-read the blocked target, exact parents and downstream cards. Require the intended owner, fulfilled result contract, satisfied original parents and no active target run. Separate the missing orchestration work from the worker's privileges: if the authorized coordinator already performed subscription/graph setup, the returning worker need not gain those privileges or repeat the probe.
2. Verify actual process end separately from run `ended_at`. Take the PID and process-start identity from the exact original spawn record; inspect with `ps -p <verified-pid> -o pid,ppid,stat,etime,comm` and, if relevant, `ps --ppid <verified-pid> -o pid,ppid,stat,etime,comm`. A board-completed worker can still be running its epilogue and editing its report. If a handoff requires termination, wait only through a supported bounded foreground process check; do not kill/reclaim completed work, infer exit from `done`, or manufacture polling of delegated work whose result requires ending the turn. If the PID may have been reused, compare its recorded start identity rather than treating an unrelated process as the worker.
3. Re-read the final report after the prior worker exits, because its final completion-event evidence may have been appended after the first read. Check current repository HEAD, `git status --short` and `git diff --check`; preserve unrelated uncommitted files and require no parallel repo writer. Keep historical observation records intact rather than rewriting them as current success.
4. Write one central resumption decision and post it to the existing blocked card. Name the fulfilled prerequisite deliverables, the specific repaired boundary, the remaining authorized file/commit/review work and the unchanged exclusions. Explicitly tell the returning worker to reuse completed operator/acknowledgment cards instead of constructing another graph. Read the posted instruction back before release.
5. Attach a stable report snapshot only after its writer has finished. Read `kanban_attachments` before uploading and reuse an existing content-identical accepted snapshot when it already fulfills the contract. After a new upload, read back the returned attachment ID, effective filename and stored path; a duplicate basename may acquire a suffix instead of replacing the earlier attachment. Verify the exact required file exists as a durable board attachment; an `artifacts` declaration, a report link and a platform upload are separate delivery mechanisms, not interchangeable proof of attachment storage. Avoid unnecessary duplicates when a durable central link already fulfills the contract.
6. Use `kanban_unblock(task_id=..., board=...)` only from the authorized orchestrator context after the exact blocker is resolved. Do not re-kind the block, reset recurrence accounting, weaken runtime policies or manually claim/dispatch. Read back the exact target immediately: distinguish the returned `ready` transition from a subsequent actual dispatcher `running` claim, and require the new run's intended profile. Verify unchanged parent sets and that later phases have no active runs and remain gated. Persist this bounded release evidence in the existing manifest; leave implementation and independent review with their owners.

## Correlate native receipt without exposing conversation contents

When a receipt contract requires canonical session evidence beyond the current conversation's actual notification, inspect only the verified session/message metadata and a boolean exact-task/status match. For an authorized read-only session database, use a parameterized query such as `SELECT id, session_id, role, instr(content, ?) > 0 AS exact_notification_match FROM messages WHERE id = ?`, binding the exact notification prefix and the independently observed message-row ID. Read session routing metadata separately to confirm destination/profile. Do not dump general chat content or infer a missing message-row ID.

Keep these evidence layers distinct: native task-event ID, internal notification-row ID, admitted gateway session, external platform post ID and explicit agent acceptance. Correlate actual task/status, checkpoint and routing when no event foreign key is stored; never invent such a relation or treat a missing external post ID as proof that an observed internal receipt failed. State the actual boundary verified and any stronger evidence still unavailable.
