# REVIEW — Maker-Plan `PLAN_devteam_v3_codercutter.md` (Revision 2, Coder-Cutter)

Reviewer: Fujiko (independent, review-only; one-shot run in profile `fujiko`, model `deepseek/deepseek-v4.1-flash-1017`, reasoning high, tools `file,terminal`, read-only boundaries in the commission)
Date: 2026-11-23 (CET)
Review object: `docs/v3/PLAN_devteam_v3_codercutter.md`, untracked, sha256 `0032f5a54fe1a7e28e94654ec255ac81104567a373143b3f64a30e380e8ca11a`
Frozen state: HEAD `b5ced6be25d34350830f55f1b181e0e262cde0d1`; `git status --short` = `?? docs/v3/` at handover and before the verdict
CAC criterion: `/home/mariko/projects/cac/SKILL.md`, `references/cac-notation.md`, `references/cac-authoring-contract.md`, read by the reviewer in full

**VERDICT: CHANGES REQUIRED** — 1 blocking, 6 major, 6 minor findings. Two are genuine decisions (F3 password provenance, F5 skill-cue re-homing); the rest restore text that the compaction cut below its binding semantics.

---

## Reviewer report (verbatim)

1. EXACT REVIEWED STATE

Repository: /home/mariko/projects/generic-devteam
HEAD: b5ced6be25d34350830f55f1b181e0e262cde0d1 (merge commit b5ced6b, at HANDOVER and again immediately before this verdict — unchanged)
Branch: develop (the handover brief says `v2/main`; git reports `develop`. Same HEAD either way. The brief's branch name is the only mismatch.)
git status --short at handover: `?? docs/v3/`
git status --short before verdict: `?? docs/v3/`
Plan sha256 at handover: 0032f5a54fe1a7e28e94654ec255ac81104567a373143b3f64a30e380e8ca11a
Plan sha256 before verdict: 0032f5a54fe1a7e28e94654ec255ac81104567a373143b3f64a30e380e8ca11a (identical)
Baseline verified: manifest.json version "2.14.4" (manifest.json:3), coder template 140 lines / 19,652 bytes.
Repository suite at HEAD: `python3 -B -m unittest discover -s references -p 'test_render_reasoning.py'` → 85 tests, OK. `test_update_team.py` did not finish inside 180 s in this read-only run (no result recorded; noted, not used as evidence).

2. VERDICT: CHANGES REQUIRED

The §9.2/§9.3 texts are structurally sound, CAC-close, and render cleanly, but the decided text loses execution-critical invocation literals, drops an ownership actor, contains one unresolvable pointer, and changes one escalation condition. §9.5's consequence list is materially incomplete and would leave a deterministic set of failing tests and stale assertions.

3. FINDINGS

F1 — BLOCKING — plan §9.2 line 294 (Coder SOUL "Session", third bullet)
ALT: "Bindings, process-local: `{{CODEX_BINARY}} exec`; `HOME={{CODEX_PROCESS_HOME}}`, `CODEX_HOME={{CODEX_HOME}}`, `PONYTAIL_DEFAULT_MODE=full`; `--sandbox danger-full-access`; `-c model_reasoning_effort='\"<effort>\"'`; `--json`; `-o <result file>`; prompt on stdin; `exec resume <thread_id>`."
Baseline (templates/roles/coder.SOUL.md.template:36-70) binds two distinct forms: the fresh run with `--sandbox danger-full-access`, the resume with `-c sandbox_mode='\"danger-full-access\"'` because `exec resume` does not accept `--sandbox`. It also binds `background=true`, `pty=true` and the validated workspace as `workdir` (:36), supplies `--model MODEL_ID` in both forms, sets `-c model_reasoning_effort` in both, and states "Read the final message from `RESULT_FILE`; the event stream is not the result." (:52). None of these survive. The merged one-liner cannot say which flags apply to which form, so a resumed turn runs under Codex's default sandbox and the Coder may read the event stream as the result. This also contradicts the plan's own acceptance row §5:197 ("no ... invocation literal disappears") and breaks test_render_reasoning.py:191-195 (`model_reasoning_effort`, "`background=true`, `pty=true`", the `thread.started` sentence).
NEU (replaces that bullet; a `sh` fence also restores shell quoting, see F11):
  - Native `hermes-codex` skill owns the syntax. Invoke with `background=true`, `pty=true` and the validated workspace as `workdir`; bindings stay process-local:
    ```sh
    env HOME={{CODEX_PROCESS_HOME}} CODEX_HOME={{CODEX_HOME}} PONYTAIL_DEFAULT_MODE=full \
      {{CODEX_BINARY}} exec --model MODEL_ID --sandbox danger-full-access \
      -c model_reasoning_effort='\"REASONING\"' --json -o RESULT_FILE - < PROMPT_FILE
    env HOME={{CODEX_PROCESS_HOME}} CODEX_HOME={{CODEX_HOME}} PONYTAIL_DEFAULT_MODE=full \
      {{CODEX_BINARY}} exec resume --model MODEL_ID -c sandbox_mode='\"danger-full-access\"' \
      -c model_reasoning_effort='\"REASONING\"' --json -o RESULT_FILE SESSION_ID - < FOLLOWUP_PROMPT_FILE
    ```
    Read `thread_id` from the `thread.started` line. Read the final message from `RESULT_FILE`; the event stream is not the result.
This costs roughly 250 B; the 5,125-byte figure has to be re-measured (§4 W1's own rule: token reduction is not an excuse to remove an authorization guard). Reason: the text is declared "write exactly this", so an incomplete invocation is an implementation defect, not a wording preference.

F2 — MAJOR — plan §9.2 line 278 (Coder SOUL "Role and authority", second bullet)
ALT: "{{PLANER_NAME}} owns requirements, scope, customer decisions and plan amendments."
Baseline (coder template:7): "The customer owns product scope and external permissions. {{PLANER_NAME}} obtains missing customer decisions and maintains authorized plan amendments." §9.2 transfers product-scope ownership to the Planner. §1's matrix (plan line 23) still says "Planner / customer", and Planner SOUL:8 requires customer approval for scope expansion, so the SOUL text now contradicts both. A fresh Coder reading §9.2 would treat a Planner scope change as authorised without customer approval — the authority weakening §2.1 explicitly forbids. CAC basis: notation §1 ("Preserve ... actor, obligation strength, conditions") and the authoring contract line 10 ("Preserve the actor").
NEU: "The customer owns product scope and external permissions. {{PLANER_NAME}} owns requirements, plan amendments and the customer decisions recorded in the approved plan. {{REVIEWER_NAME}} reviews independently. You approve neither your own implementation nor its completion."

F3 — MAJOR — plan §9.3 line 349 (demo-handover skill, demonstration-user bullet)
ALT: "with the password from the private team record, supplied only through the environment variable the script documents, never as an argument."
The pointer does not resolve for its recipient. The record lives at `<actual planner home>/devteam/setup.md` and `devteam/installation.json` (setup.md:201, setup.md:332, update.md:48); it is not in the Coder home (bind_recovery.py:33-36 requires `roles['planner']['home'] == home`), and deriving the Planner home from the profile ID is forbidden (update.md:24 "without deriving paths from profile names"; baseline coder:124 "Use confirmed paths, never derive paths from project names"). The Coder's render fields contain `PLANNER_PROFILE` but no Planner path (manifest.json:124-139), and the skill is byte-identical so it cannot carry one. Today the literal password sits in the Coder SOUL (render_text.py:26 `LITERAL_FIELDS`; test_update_team.py:418); after this change nothing in the Coder's installed tree carries it. CAC basis: SKILL.md:60 "Verify that every compressed pointer resolves to retrievable evidence for its recipient"; contract line 11 "A pointer replaces detail only if the recipient can retrieve the exact evidence".
NEU: "with the password from the private team installation record kept in the Planner's `devteam/` record, obtained from the Planner on the released card when not already confirmed; supply it only through the environment variable the script documents, never as an argument and never on a card."

F4 — MAJOR — plan §9.2 line 303 (Coder SOUL "Blockers", fourth bullet)
ALT: "Then `kanban_block(kind=\"capability\"|\"transient\", reason=...)` and one TIMER request to {{PLANER_PROFILE}} via `kanban_create`."
Baseline separates the two routes: template:101 capability → block only (access must be repaired); template:102 quota/rate limit → block plus "Send one TIMER request ... Name board, task, reset or uncertainty and requested one-time resume." The compression applies the timed resume to capability blocks too, which arms an automatic resume while the capability is still missing — a behaviour change §3.2 line 98 forbids ("preserve current capability/transient classification ... and authorized timed resume via Planner"). It also drops the required TIMER content. CAC basis: notation §1 "Preserve ... conditions, exceptions"; contract line 10 "Preserve the ... failure exit".
NEU: "- Codex unavailable or required access fails: record the actual error and work state; diagnosing the failure stays allowed. Then `kanban_block(kind=\"capability\", reason=...)`. No model switch, no replacement card.
- Verified quota or rate limit: record original error, reset date/time/zone or uncertainty, and remaining work. Then `kanban_block(kind=\"transient\", reason=...)` and one TIMER request to {{PLANNER_PROFILE}} via `kanban_create`, naming board, task, reset or uncertainty and the requested one-time resume."

F5 — MAJOR — plan §2.2 line 67 / §5 line 193 (missing re-homing of the skill cues)
ALT: "diagnosing-bugs | Team-Codex only | Keep with Team-Codex; remove mandatory Coder invocation/independent diagnosis." and "Versioning and evidence | Codex retains SemVer/changelog rules and `build-evidence`/`diagnosing-bugs`."
The Coder SOUL is the only place in the Maker that puts those skills into a Codex turn: template:27-29 requires the literal `$diagnosing-bugs` / `$build-evidence` cue in every task and resume. Nothing else does: templates/team-codex-AGENTS.md (8 lines) carries no skill requirement, and upstream-sources.md:28 states "Coder passes the literal `$build-evidence` cue for the affected mode". Removing the cue without re-homing it makes the §5 row an unsupported assertion and leaves both skills installed but uninvoked; `plan-versioning-semver` delivered to `targets.codex` has the same problem ("Apply each rule independently wherever its trigger occurs", SKILL.md:12 — but nothing tells Codex to load it).
NEU: add one line to templates/team-codex-AGENTS.md: "- Skills: load `$diagnosing-bugs` for unexplained failures or regressions and `$build-evidence` for build-, browser- or process-dependent evidence in the named mode; load `plan-versioning-semver` for version, changelog or API-contract changes. Independent review stays with the Reviewer." Add the corresponding entry to §9.5.

F6 — MAJOR — plan §9.5 line 372-374 (follow-on list presented as complete, but incomplete)
ALT: "`references/test_render_reasoning.py:140`–`165`: ... `references/test_update_team.py:410`–`427`: ... `references/setup.md:230`: ..."
Deterministic breakage the list does not name (verified against the current sources):
  - test_render_reasoning.py:82-99 loops all three roles and asserts the dev-environment clause set, including "Start, stop, restart, rebuild, recreation, synthetic data generation and reset of disposable state", "source ownership, operational data, host administration, shared infrastructure and external effects" and "Running the app from source grants no deployment authority." §9.2 has none of them.
  - test_render_reasoning.py:104-105 asserts "Outside that development scope, a coding ticket alone does not grant operational approval." and "Tool and system prohibitions remain binding." — both absent from §9.2.
  - test_render_reasoning.py:125-126 splits the coder text on "5. Provide Codex" / "6. Read" — IndexError on the unnumbered §9.2 (also :115, :207-215, :188-190).
  - test_render_reasoning.py:158, :166-183 render `DEMO_PASSWORD` for all three roles; :180-183 pops it from the coder values and expects `ValueError`, which no longer raises once the field is gone (silent loss of the password-validation test, not its removal).
  - test_render_reasoning.py:966-985 pins the exact `own_skills` target matrix; :1082-1095 pins the upstream-sources.md rows ("Planner and Coder"; "Planner, Coder and Reviewer") and code-analysis.md rows.
  - test_build_evidence.py:71 and test_update_team.py:1010 assert the `$build-evidence` cue in the installed Coder SOUL.
  - native-workflow.md:28 still declares `DEMO_PASSWORD` "all three roles".
  - manifest.json:201 (`build-evidence.changes`: "Coder passes the literal `$build-evidence` cue ...") and :252 (`diagnosing-bugs.changes`: "Coder explicitly invokes and validates results") assert removed Coder duties.
NEU: extend §9.5 with those locations, and state for each whether the assertion is moved, inverted, or deleted; for the `DEMO_PASSWORD` validator, retarget it to the planner and reviewer roles rather than letting it pass vacuously.

F7 — MAJOR — plan §9.2 line 305 and :315 (Git/workspace and development-runtime guards reduced below "effective semantics", contradicting §2.1 line 51)
ALT (line 305): "Development environment and demo runtime are the project's: read the project agent guide before the first build, test or run. Outside that scope a coding ticket grants no operational approval; unrelated work goes to {{PLANER_NAME}} as a proposal, and you create no cards."
ALT (line 315): "Never `git add -A`, `reset --hard`, `checkout -- .`, `clean -fd` or `stash` on unrelated work; commit in the correct parent repository, no `git init` or nested repositories."
Lost from template:106-107: "Start, stop, restart, rebuild, recreation, synthetic data generation and reset of disposable state for development tests need no further customer approval" (a permission the Coder needs to operate the environment at all), "Respect existing boundaries on source ownership, operational data, host administration, shared infrastructure and external effects", and "Running the app from source grants no deployment authority" (a privilege guard). Lost from :111: "Stop if changes cannot be separated safely" (the failure exit). Lost from :21: "If the assigned checkout carries a local input that the project's development entrypoint rejects — deployment env files, served config, local credentials — verify in a clean detached worktree at the candidate commit. Leave the local input in place; never delete, rewrite or mask it." Lost from :22: "Before the first Codex call, verify the card's implementation branch exists at the named start commit and is checked out. Return the card to the Planner if either check fails. Never create, rename or rebase that branch." §2.1 line 51 requires exactly these to "keep their effective semantics", and the deletion is not listed in §9.1.
NEU: restore two bullets — in "Blockers": "- The project's development environment and demonstration runtime are yours to operate: read the project agent guide before the first build, test or run, and use its commands. Start, stop, restart, rebuild, recreate, generate synthetic data and reset disposable state for development tests without further customer approval; respect source ownership, operational data, host administration, shared infrastructure and external effects. Running from source grants no deployment authority." — and in "Evidence, Git, memory": "- Verify the implementation branch exists at the named start commit and is checked out; return the card to {{PLANER_NAME}} if not, and never create, rename or rebase it. A local input the entrypoint rejects stays in place: verify in a clean detached worktree, never delete, rewrite or mask it. Stop if changes cannot be separated safely."

F8 — MINOR — plan §5 line 197 and §9.2 line 268 (measurements not reproducible)
ALT: "Rendered SOUL is 50 lines and 5,125 bytes" / "5,300 bytes unrendered, 5,125 bytes rendered with sample bindings, 50 lines (2.14.4: 19,636 bytes, 140 lines)".
Measured now: unrendered 5,300 B ✓; rendered with the repository's own fixture values (test_render_reasoning.py:58-73) 5,141 B and 49 lines; rendered with uniform "Example" 5,142 B / 49 lines. The baseline is 19,652 B, not 19,636 B (wc -c). Every stated number is 16 B low and the line count is one high, so the acceptance criterion "50 lines and 5,125 bytes" cannot be met by the text that follows it. NEU: "Rendered SOUL is 49 lines and 5,141 bytes with the repository fixture bindings (2.14.4: 140 lines, 19,463 bytes rendered / 19,652 bytes unrendered)."

F9 — MINOR — plan §9.2 line 302 (CAC obligation strength and required content)
ALT: "`kanban_comment` with `Question:`, `Why it matters:`, options and recommendation, then `kanban_block(kind=\"needs_input\", reason=...)`"
Baseline requires "`Question:`, `Why it matters:` and paused work" and supplies "facts, options, a recommendation, and the paused work" for binding changes (template:103). The compression makes options/recommendation unconditional (a strength increase) and drops "paused work" (a required field the Planner uses to size the decision). CAC basis: notation §1 "Preserve ... obligation strength ... conditions"; contract line 10.
NEU: "`kanban_comment` with `Question:`, `Why it matters:`, the paused work, and facts, options and a recommendation when the choice is a decision"

F10 — MINOR — plan §9.2 line 270 and §9.5 line 371 (`DEMO_PASSWORD` disposition)
ALT: "`DEMO_PASSWORD` no longer occurs and MUST leave `manifest.role_templates.coder.render_fields` for this role; the Planner keeps it."
The Reviewer also keeps it (manifest.json:157), and native-workflow.md:28 still says "all three roles" — a file §9.5 does not list. NEU: "… MUST leave `manifest.role_templates.coder.render_fields`; Planner and Reviewer keep it. Update `references/native-workflow.md:28` to name two roles and `references/setup.md:234` so setup still supplies the value for them."

F11 — MINOR — plan §9.2 line 294 (shell quoting no longer applied)
The baseline invocation was a ```sh fence, which makes render_text.py:99-100,117 shell-quote `CODEX_BINARY`/`CODEX_PROCESS_HOME`/`CODEX_HOME` via `shlex.quote`, and setup.md:235 relies on that ("Pass raw absolute paths for shell quoting in the invocation block"). §9.2 contains no fenced block (0 fence markers, verified), so the same placeholders now render as raw inline code (render_text.py:122-124) and a confirmed path containing a space produces a broken command line. Restored by the F1 NEU; no separate text change needed, but the fence must not be dropped again.

F12 — MINOR — plan §9.4 line 367 (deviation arithmetic)
ALT: "Cutting further reaches only the `Session` block (1.0 KB)" / section table.
Sound in conclusion, overstated in evidence: the table's §9.2 column is exact (766 / 586 / 1162 / 1371 / 576 / 605 / 145 B, verified by splitting the text), but those blocks sum to 5,211 B against a stated total of 5,125 B, and "Delegate" (586 B) and "Review handoff" (576 B) are prose that could shed bytes without touching a binding. More importantly the stated reason understates the real constraint: a skill is copied byte-identically (setup.md:229, "Keep names and bytes unchanged except the recovery launcher"), so the `Session` block's placeholders could not move into a skill at all — the failure mode is lost bindings, not a missed load. NEU: "Cutting 1 KB reaches only the `Session` block. That block's bindings are render fields; a skill is copied byte-identically and cannot carry them, so moving it would drop the process home, the sandbox flag and the allowlisted binary entirely. The deviation stands on that, not on a missed load."

F13 — MINOR — residual lost process rules (check 1 leftovers that belong to no other role)
Template:10 "Apply existing requirements and applicable customer decisions without asking again." — absent from §9.2 and from Planner/Reviewer text in Coder-scoped form. Template:90 "Do not repeat a failed approach unchanged." — absent. Template:104 "The decision stands for the round." and "Verify recipient." — absent. Template:114-115 (Hindsight scope filter `scope:shared`/`role:coder`; "Keep credentials ... out of memory") — reduced to a bank name. Template:117 ("For persisted value-set, enum, schema or outbound-mapping changes, verify stored data and every export path") — absent although §9.1's removal list does not name it. None of these is individually large; together they are the parts of "escalation, evidence provenance and Git safety" that §3.4 line 121-124 says remain binding. CAC basis: contract line 10 ("Preserve the actor, trigger, obligation, order, exceptions, scope and failure exit"); §1 "every compressed pointer ... plain prose when compression would obscure ... a safety boundary".
NEU (smallest additions): "Apply existing requirements and customer decisions without asking again." / "Do not repeat a failed approach unchanged." / "Verify the recipient; the round's decision stands." / "Recall `scope:shared` or `role:coder` only, keep credentials and raw code out of memory."

Explicit no-finding results:
Check 2 (duplication) — no finding. The only cross-role repetition is the development-environment clause, which also stands in Planner SOUL:12 and Reviewer SOUL:84; it duplicates because each role needs its own resident operational authority (authoring contract line 12: "Keep durable authority in the role instructions"). §9.2 correctly avoids duplicating the native `hermes-codex` manual (line 294 "Native `hermes-codex` skill owns the syntax") and the demo procedure (§9.2 line 306 is a pointer only). No rule duplicated from a skill the Coder still loads.
Check 3 (deviation soundness) — no defect beyond F12. The three stated failure mechanisms are individually coherent against render_text.py (placeholders are literals, not runtime lookups), setup.md:229 (no rendering of skills) and the allowlist rule stated in Planner SOUL:13 and Reviewer SOUL:9. See OPEN QUESTIONS for the approval-dialog step.
Check 8 (renderability) — no finding. `role_fields(text, "coder")` accepts the text and returns exactly the 13 declared fields; every one is legal for `coder` (render_text.py:12-21); `DEMO_PASSWORD` count is 0; no residual braces after rendering; `role_fields == set(manifest.render_fields)` will hold if §9.5 is implemented (setup.md:241, test_render_reasoning.py:80).
Check 5 ("No new generic Orchestrator Skill" vs `demo-handover`) — no contradiction. Plan line 141 already carves the exception out in the same paragraph ("The single exception is `demo-handover` (§9.3)").
Check 5 (§5 negative assertions vs §9.2 text) — no contradiction. §9.2 line 280 ("no diff review, no test replay") and line 278 ("You approve neither your own implementation nor its completion") satisfy the §5:200 prohibitions; the code-analysis prohibition is satisfied by silence.

4. VERIFIED CLAIMS

- §9.2 renders: `render_role` accepts the text for role `coder` with exactly the 13 placeholders `CODEX_BINARY, CODEX_HOME, CODEX_PROCESS_HOME, CODEX_REASONING_DEFAULT, CODEX_REASONING_MAX, HINDSIGHT_BANK_NAME, KANBAN_BOARD_NAME, PLANER_NAME, PLANNER_PROFILE, PROJECT_NAME, REVIEWER_NAME, REVIEWER_PROFILE, ROLE_NAME` — identical to the list declared at plan line 270. `DEMO_PASSWORD` does not occur (grep count 0; rendered output contains none).
- §9.2 section byte figures in §9.4's §9.2 column are exact (766/586/1162/1371/576/605/145 B).
- §9.3's determinism premise is correct: skills are copied with unchanged bytes (setup.md:229) except the recovery launcher, which is bound by a dedicated transform (`references/bind_recovery.py`, `bound-recovery-v1`); `grep -rn '{{' skills/` finds placeholders only in `skills/brownfield-feature-planning/scripts/recover-triage`. So an `own_skills` file cannot carry `{{DEMO_PASSWORD}}`.
- test_render_reasoning.py:140-165 is exactly the demo lifecycle/teardown/password test, including line 158's coder assertion of "create the demonstration user via `demo.sh user` with the password `Example` ...". The plan's proposed relocation is the right home for it.
- test_update_team.py:410-427 covers the applied update; line 414 records `confirmed_values.DEMO_PASSWORD`, lines 415-418 assert the literal password appears exactly once in each of the three SOULs, lines 419-424 assert the lifecycle text and `demo.sh retire` / `demo.sh user` in the Coder SOUL, line 425 asserts the reviewer's login check. The plan's direction is right; its description ("the `DEMO_PASSWORD` count for the Coder home becomes `0`") masks that the assertion is a three-role loop that must be split (F6).
- references/setup.md:230 is the Codex target list and it names its skills explicitly ("currently `screenshot-to-code`, `diagnosing-bugs` and `build-evidence`"). Adding a Codex target therefore requires an explicit edit there; the plan points at the right line but does not say what the list becomes (F6).
- Manifest consequence mechanisms exist: `own_skills.<name>.targets.codex: ["team-codex"]` is used by `build-evidence` (manifest.json:196-198), `screenshot-to-code` (:337-339) and `diagnosing-bugs` (:247-249); `plan-versioning-semver.targets.hermes` currently is `["planner","coder"]` (:281-284); `build-evidence.targets.hermes` is `["coder","reviewer"]` (:192-195); `screenshot-to-code.targets.hermes` is `["planner","coder"]` (:333-336); `role_templates.coder.render_fields` contains `DEMO_PASSWORD` (:130). `targets.codex` is the mechanism that exists.
- `render_text.py` needs no change for the field removal: `DEMO_PASSWORD` is in the all-role `ROLE_FIELDS` (:12-15) and simply stops being required once the template stops using it.
- `references/development-verification.md:11-12` contains the two commands quoted in plan §4 W5.
- §2.1/§9.1 removal declarations are consistent with the dropped blocks wherever they name them (analysis integration, RED evidence, changelog, consumer enumeration, subagent catalogue, CBM binding, polling).

5. OPEN QUESTIONS

- The allowlist step of the §9.4 argument ("a wrong `{{CODEX_BINARY}}` no longer matches its `command_allowlist` entry, which opens an approval dialog that no worker can answer") cannot be verified from this repository: no Hermes core source is present. The role texts only state the consequence class (Planner SOUL:13, Reviewer SOUL:9: request a missing grant from the operator and block the card). The claim is plausible and consistent; it is not proven here.
- §9.4's ponytail argument ("`ponytail` stays bound to Team-Codex in full mode and carries the smallest-correct-change convention") is unverifiable in-repo: the binding exists (manifest.json:475-494, integrations.md:189-215, `PONYTAIL_DEFAULT_MODE=full` in the invocation) but the upstream plugin's content is not vendored. The argument is also unnecessary — the dropped rule (template:122) bound a role that no longer writes code.
- `references/test_update_team.py` did not complete within the 180 s foreground limit of this read-only run; its current pass/fail state at HEAD is therefore unconfirmed. The individual assertions cited in F6 were read directly from the file, so the findings do not depend on that run.
- Whether Codex CLI selects `diagnosing-bugs`, `build-evidence` or `plan-versioning-semver` by description without an explicit `$skill` cue is a native-behaviour question the repository only partly answers (`skills/diagnosing-bugs/README.md:9` and NOTICE.md:24 allow implicit selection for new regressions). F5 is written so that the requirement holds either way.

---

## Marikos Gegenprüfung (2026-11-23, nach dem Lauf)

Unabhängig nachgemessen bzw. gelesen, nicht aus dem Bericht übernommen:

| Befund | Gegenprüfung | Ergebnis |
|---|---|---|
| F1 | `templates/roles/coder.SOUL.md.template` liest `background=true`, `pty=true`, `workdir`, `--model MODEL_ID`, und die Resume-Form mit `-c sandbox_mode='"danger-full-access"'` — drei getrennte Stellen | bestätigt: die einzeilige Zusammenfassung ist nicht ausführbar |
| F2 | 2.14.4 `coder:7` überträgt Produktumfang ausdrücklich dem Kunden | bestätigt: „owns … scope" beim Planner ist eine Autoritätsverschiebung |
| F3 | `references/setup.md:201` legt den Record unter `<actual planner home>/devteam/setup.md`, 0700/0600; `references/bind_recovery.py:33` verlangt `roles['planner']['home'] == home` | bestätigt: aus dem Coder-Home nicht auflösbar |
| F4 | 2.14.4 trennt Capability (Block) und Quota (Block + TIMER) | bestätigt: die Zusammenfassung bewaffnet einen Resume bei fehlender Fähigkeit |
| F6 | `test_render_reasoning.py:82-105` prüft die Development-Authority-Zeile in allen drei Rollen und ihre Wortgleichheit; `:125` teilt den Coder-Text an „5. Provide Codex" | bestätigt: bricht am §9.2-Text |
| F7 | 2.14.4 `:106-107` erlaubt Start/Stop/Rebuild/Reset ohne neue Kundenfreigabe und verbietet Deployment-Autorität; `:21-22` verlangen Worktree- und Branchprüfung | bestätigt: fehlt in §9.2 |
| F8 | `wc -c`: Baseline 19.652 B / 140 Zeilen; gerendert mit den Repository-Fixture-Werten 5.141 B, 50 Zeilen (Zeilen nach `splitlines` 49) | bestätigt: Plan nennt 19.636 / 5.125 — beide Zahlen falsch |
| F11 | `references/render_text.py:99-124` quotet nur innerhalb von ```sh-Zäunen (`shlex.quote`), Inline-Code bleibt roh | bestätigt: §9.2 enthält keinen Zaun |

Nicht nachgeprüft und im Bericht als offen geführt: die Approval-Dialog-Folge eines falschen `CODEX_BINARY` (Hermes-Kern nicht im Repo), der Inhalt des Ponytail-Upstreams, der Gesamtlauf von `test_update_team.py`.

## Entscheidungen (Stand 2026-11-23, nach Max' Antwort)

| Befund | Entscheidung / Umsetzung im Plan | Stand |
|---|---|---|
| F1 | Invocation als `sh`-Block mit beiden Formen (`exec`, `exec resume --model … -c sandbox_mode='"danger-full-access"'`), `background=true`, `pty=true`, `workdir`, `MODEL_ID`, `RESULT_FILE`; Satz „the event stream is not the result" zurück | korrigiert |
| F2 | „The customer owns product scope and external permissions" zurück; Planner erhält fehlende Kundenentscheidungen | korrigiert |
| F3 | **Max entscheidet: das Passwort-Literal bleibt im Coder-SOUL.** Der Skill trägt nur das Verfahren, kein Renderfeld | entschieden, umgesetzt |
| F4 | Capability- und Quota-Route wieder getrennt, TIMER-Inhalt benannt | korrigiert |
| F5 | Skill-Cues in `templates/team-codex-AGENTS.md` verankert (§9.5) | korrigiert |
| F6 | §9.5 um alle betroffenen Test- und Referenzstellen erweitert, je Stelle mit Aussage | korrigiert |
| F7 | Development-Authority-Bullet, Branchprüfung, Worktree- und Trennbarkeitsregel zurück | korrigiert |
| F8 | Zahlen neu gemessen: 19.652 B Baseline, 7.248 B gerendert, 64 Zeilen | korrigiert |
| F9 | `paused work` und die Bedingung für Optionen/Empfehlung zurück | korrigiert |
| F10 | löst sich auf: das Literal bleibt für alle drei Rollen, `native-workflow.md:28` bleibt gültig | entfällt |
| F11 | mit F1 erledigt (Zaun wiederhergestellt, `shlex.quote` greift) | korrigiert |
| F12 | Abweichungsbegründung auf die Byte-Gleichheit von Skills umgestellt | korrigiert |
| F13 | vier Prozesssätze zurück (Entscheidungen anwenden, keinen gescheiterten Ansatz wiederholen, Empfänger prüfen / Entscheidung gilt für die Runde, Hindsight-Scope) | korrigiert |

Nicht wiederhergestellt, sondern ausdrücklich an Team-Codex abgegeben: RED-Nachweis vor der Produktionsänderung und die Prüfung persistierter Wertemengen/Schemata samt Exportpfaden.

Nach der Korrektur ist der Coder-SOUL 7.248 B gerendert (64 Zeilen) statt 5.125 B — der Preis der sechs zurückgeholten Regeln. Der Plan ist damit wieder auf dem Stand `docs/v3/PLAN_devteam_v3_codercutter.md`; eine zweite Reviewrunde auf diesem Stand ist noch nicht gelaufen.
