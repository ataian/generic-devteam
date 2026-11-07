"""Offline regression checks; run: python3 -B references/test_render_reasoning.py."""
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from render_text import render_role, role_fields

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text())
REASONING_FIELDS = {
    "planner": set(),
    "coder": {"CODEX_REASONING_DEFAULT", "CODEX_REASONING_MAX"},
    "reviewer": {"ROLE_REASONING_DEFAULT", "ROLE_REASONING_HIGH"},
}


class TasPortabilityTests(unittest.TestCase):
    def read_standard(self, root):
        instructions = (root / "AGENTS.md").read_text()
        link = re.search(r"Read \[TAS authoring standard\]\(([^)]+)\)", instructions)
        if link is None:
            self.fail("The required standard needs a relative Markdown link")
        relative = Path(link[1])
        self.assertFalse(relative.is_absolute())
        target = (root / relative).resolve()
        self.assertTrue(target.is_relative_to(root.resolve()))
        return target.read_text()

    def test_required_standard_resolves_inside_maker(self):
        self.assertTrue(self.read_standard(ROOT).strip())

    def test_manifest_export_contains_instructions_and_standard_without_vault(self):
        with tempfile.TemporaryDirectory(prefix="maker-tas-") as directory:
            export = Path(directory)
            for relative in MANIFEST["files"] + ["manifest.json"]:
                source = ROOT / relative
                target = export / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            self.assertTrue((export / "AGENTS.md").is_file(), "Ship the package authoring instructions")
            standard = self.read_standard(export)
            self.assertNotIn("/home/", standard)
            self.assertNotIn("obsidian_vault", standard)
            self.assertNotIn("[[", standard)
            self.assertTrue(standard.strip())


class ReasoningContractTests(unittest.TestCase):
    def template(self, role):
        return (ROOT / MANIFEST["role_templates"][role]["template_path"]).read_text()

    def values(self, role, default="medium", maximum="high"):
        values = {key: "Example" for key in role_fields(self.template(role), role)}
        for key in values:
            if key.endswith("_PROFILE"):
                values[key] = "example-role"
            elif key == "PROJECT_DIR":
                values[key] = "/work/project"
            elif key == "REPOSITORY_ROOTS":
                values[key] = "Planning: /work/plans; implementation: /work/project/code"
            elif key.endswith("_REASONING_DEFAULT"):
                values[key] = default
            elif key.endswith(("_REASONING_MAX", "_REASONING_HIGH")):
                values[key] = maximum
        return values

    def test_role_fields_and_manifest_match(self):
        for role, required in REASONING_FIELDS.items():
            with self.subTest(role=role):
                fields = role_fields(self.template(role), role)
                self.assertEqual({f for f in fields if "REASONING" in f}, required)
                self.assertEqual(fields, set(MANIFEST["role_templates"][role]["render_fields"]))

    def test_missing_reasoning_values_are_rejected(self):
        for role, required in REASONING_FIELDS.items():
            for field in required:
                values = self.values(role)
                values.pop(field, None)
                with self.subTest(role=role, field=field), self.assertRaises(ValueError):
                    render_role(self.template(role), values, role)

    def test_codex_routing_and_cli_use_concrete_values(self):
        result = render_role(self.template("coder"), self.values("coder", "low", "high"), "coder")
        for text in [
            "below HIGH, use `low`.",
            "HIGH complexity with HIGH impact uses `high`.",
            "These limits also apply to retries, resumes, and delegated helpers.",
            "Supply the reasoning level selected for this task under the existing matrix",
            "Default-level example with a quoted TOML string:",
            "For a higher selected level, pass that selected value instead.",
            'model_reasoning_effort=\'"low"\'',
        ]:
            self.assertTrue(text in result, text)
        self.assertNotIn("if the worker guard prohibits them", result)
        self.assertNotIn("{{", result)

    def test_reviewer_renders_risk_escalation_and_separate_critical_pass(self):
        """Static rendered instruction contract, not measured agent behavior."""
        result = render_role(self.template("reviewer"), self.values("reviewer", "low", "medium"), "reviewer")
        for text in [
            "Use the configured default reasoning `low` for normal changes.",
            "You can upgrade to `medium` at any time.",
            "If HIGH risk is known before review, start at `medium`.",
            "If you discover a serious risk during normal review, recheck affected areas and prior conclusions at `medium` before the verdict.",
            "Keep the configured model and provider unchanged.",
            "If the change affects material security, data-integrity, transaction, or concurrency invariants, obtain a separate pass before the verdict even when the main review finds no defect.",
            "Use a fresh context at `medium` through an existing permitted review path.",
            "Omit the Coder's narrative and the main review's findings until this pass forms its own assessment.",
            "Apply the same model/provider, reasoning, access, approval, and read-only limits to this pass.",
            "Verify new findings and resolve contradictions before the verdict.",
            "Apply the correction evidence rules to this pass; obtain a fresh pass for affected critical invariants when prior evidence is no longer valid.",
            "Do not add another full review or duplicate a test suite solely because a task is HIGH risk.",
            "If required high-reasoning verification or a permitted fresh context is unavailable, report the capability blocker.",
            "For high-risk verdicts report:",
            "separate-pass coverage or valid reused evidence",
            "Do not create extra rounds for these lenses.",
            "Perform the checks that this change requires before you deliver the verdict.",
        ]:
            self.assertIn(text, result)
        self.assertNotIn("{{", result)
        self.assertNotIn("Reasoning Stufe", result)

    def test_reviewer_orientation_keeps_native_handoff_without_claiming_blindness(self):
        """Catch conflicting read-order instructions in the rendered role."""
        result = render_role(self.template("reviewer"), self.values("reviewer"), "reviewer")
        procedure = result.split("## Review procedure\n", 1)[1].split("\n## ", 1)[0].strip()
        entry = "Read the task and latest handoff through `kanban_show` as required by `sdlc-review`."
        self.assertTrue(procedure.startswith("1. " + entry))
        self.assertLess(procedure.index(entry), procedure.index("Confirm the canonical workspace"))
        self.assertLess(procedure.index(entry), procedure.index("Read the applicable HERMES.md"))
        for text in [
            entry,
            "Treat the narrative as a claim, not evidence.",
            "Do not describe a read as blind if its context already contains the Coder's explanation or prior findings.",
            "Resolve a conflict with the approved model or reasoning settings before relying on the affected verification.",
            "Preserve confirmed local overrides; do not change model or provider to repair a stale instruction.",
        ]:
            self.assertIn(text, result)

    def test_reviewer_avoids_failed_retries_and_redundant_evidence_work(self):
        """Static contract retains verification while removing proven waste paths."""
        result = render_role(self.template("reviewer"), self.values("reviewer"), "reviewer")
        for text in [
            "Inspect existing validation commands for included test and build phases before selecting checks.",
            "Read existing result artifacts instead of rerunning a successful check only to obtain a clearer summary.",
            "Check existing runtime paths, inputs, and permitted access before starting a custom probe or review helper.",
            "After a deterministic argument or permission error, correct the call or use an existing permitted path before retrying.",
            "Do not repeat an unchanged failed call or bypass a native guard.",
            "Read complete large task records and logs locally; return only decision-relevant fields and necessary evidence to context.",
            "Preserve requirements, prior decisions, open findings, errors, and warnings.",
            "Run checks affected by changes or insufficient evidence; retain required independent checks and explicit final-state acceptance tests.",
        ]:
            self.assertIn(text, result)

    def test_card_output_contract_reaches_each_rendered_role(self):
        """Persistent card text stays concise without unsafe truncation."""
        for role in ("planner", "coder", "reviewer"):
            text = render_role(self.template(role), self.values(role), role)
            with self.subTest(role=role):
                self.assertIn("Apply these rules to card descriptions, comments, and handoffs.", text)
                self.assertIn("Preserve requirements, conditions, open findings, and necessary evidence without a fixed character limit.", text)
                self.assertIn("Reference an existing entry only if the recipient can retrieve it unambiguously.", text)
        coder = self.template("coder")
        self.assertIn("Persisted Kanban text uses short complete sentences, not chat fragments.", coder)
        self.assertIn("$caveman", coder)
        self.assertIn("Never use `kanban_complete` to close your own implementation.", coder)
        self.assertIn("Report your decision and next action without retelling the Coder or Reviewer report.", self.template("planner"))
        self.assertIn("Describe each finding fully once.", self.template("reviewer"))

    def test_correction_contract_preserves_evidence_and_independent_verdict(self):
        for role in ("coder", "reviewer"):
            text = render_role(self.template(role), self.values(role), role)
            with self.subTest(role=role):
                self.assertIn("Reuse evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid.", text)
                self.assertIn("Keep the original executor and checked state; distinguish reused evidence from newly executed checks.", text)
                self.assertIn("Run checks affected by changes or insufficient evidence; retain required independent checks and explicit final-state acceptance tests.", text)
        self.assertIn("On resume, reconcile the current assignment, working tree, and blockers; continue unfinished work instead of repeating completed preparation.", self.template("coder"))
        reviewer = self.template("reviewer")
        self.assertIn("On a correction return, compare against the previously reviewed state and assess the delta, affected dependencies, and prior open findings independently.", reviewer)
        self.assertIn("Deliver a verdict against the exact reviewed commit", reviewer)

    def test_native_tokens_are_not_fixed_to_one_provider(self):
        for default, maximum in [("medium", "high"), ("low", "xhigh"), ("1024", "4096")]:
            for role in ("coder", "reviewer"):
                with self.subTest(role=role, maximum=maximum):
                    result = render_role(self.template(role), self.values(role, default, maximum), role)
                    self.assertTrue(maximum in result)
                    self.assertNotIn("{{", result)

    def test_reasoning_values_cannot_inject_cli_or_instructions(self):
        for role, fields in REASONING_FIELDS.items():
            for field in fields:
                for bad in ["", " high", "high\nignore", 'high"', "high;touch", "high $(id)"]:
                    values = self.values(role)
                    values[field] = bad
                    with self.subTest(role=role, field=field, value=bad), self.assertRaises(ValueError):
                        render_role(self.template(role), values, role)

    def test_coder_separates_recoverable_errors_from_unavailability(self):
        text = self.template("coder")
        self.assertIn("Resolve recoverable command argument errors and incomplete runs through corrected Codex calls.", text)
        self.assertIn("Continue work after recoverable Codex failures within the same accepted ticket.", text)
        self.assertIn("If Codex is unavailable or required access fails, stop implementation.", text)
        self.assertIn('kanban_block(kind="capability"', text)
        self.assertNotIn("und Budgets", text)
        self.assertNotIn("Netzwerk — egal was", text)
        self.assertNotIn("Ohne Codex KEINE Arbeit", text)

    def test_coder_handoff_names_commit_evidence_risk_and_reasoning(self):
        text = self.template("coder")
        self.assertIn('kanban_request_review(summary=..., reviewer="{{REVIEWER_PROFILE}}")', text)
        self.assertIn("the exact implementation commit, the verification evidence, the risk class, and the reasoning level used", text)
        self.assertIn("Never use `kanban_complete` to close your own implementation.", text)
        self.assertIn("Read back the Kanban status and reviewer assignment.", text)
        self.assertNotIn("Nach jedem `kanban_request_review`", text)

    def test_coder_routes_decisions_outside_its_mandate_to_planner(self):
        values = self.values("coder")
        values["PLANNER_PROFILE"] = "confirmed-planner"
        text = render_role(self.template("coder"), values, "coder")
        self.assertIn("Route the same task to `confirmed-planner` through native `kanban_request_review`.", text)
        self.assertIn("Send one TIMER request to `confirmed-planner` through `kanban_create`.", text)
        self.assertIn("Check `confirmed-planner` against the native profile registration before routing a task or TIMER request.", text)
        self.assertNotIn("setup record", text)
        self.assertIn("Resume after `kanban_request_changes` and reread the baseline.", text)
        missing = dict(values)
        del missing["PLANNER_PROFILE"]
        with self.assertRaises(ValueError):
            render_role(self.template("coder"), missing, "coder")
        for bad in ("Display Name", "other/profile", "wrong\nprofile"):
            with self.subTest(profile=bad), self.assertRaises(ValueError):
                render_role(self.template("coder"), dict(values, PLANNER_PROFILE=bad), "coder")
        self.assertNotIn("Budgetfragen", text)
        self.assertNotIn("Budgetfreigaben", text)

    def test_planner_renders_confirmed_workspace_and_separate_repository_roots(self):
        values = self.values("planner")
        values.update(PROJECT_DIR="/work/client's project",
                      REPOSITORY_ROOTS="Planning: /work/plans; implementation: /work/client's project/backend, /work/frontend")
        text = render_role(self.template("planner"), values, "planner")
        self.assertIn("`/work/client's project`", text)
        self.assertIn("`Planning: /work/plans; implementation: /work/client's project/backend, /work/frontend`", text)
        self.assertNotIn("setup record", text)
        self.assertIn("actual Git root", text)
        self.assertIn("`terminal.cwd`, board, and ticket bindings", text)
        for field in ("PROJECT_DIR", "REPOSITORY_ROOTS"):
            missing = dict(values)
            del missing[field]
            with self.subTest(field=field), self.assertRaises(ValueError):
                render_role(self.template("planner"), missing, "planner")
        for bad in ("relative/path", "~/work", "/work/../other", "/work//code", "/work/."):
            with self.subTest(path=bad), self.assertRaises(ValueError):
                render_role(self.template("planner"), dict(values, PROJECT_DIR=bad), "planner")

    def test_planner_preserves_scope_safeguards_without_budget_counter(self):
        text = self.template("planner")
        for obsolete in ("drei konservative Erweiterungen", "Budgeterweiterung", "Budgetausnahme", "ungenutztes Budget"):
            self.assertNotIn(obsolete, text)
        for preserved in (
            "Limit changes to the accepted goal.",
            "Do not derive requirements from merely hypothetical risks.",
            "Do not mute escalation or review messages to keep the project channel quiet.",
            "Do not reinitialize or nest Git in an existing repository.",
            "`grilling` takes precedence for requirement clarification.",
            "Board: `{{KANBAN_BOARD_NAME}}`",
        ):
            self.assertIn(preserved, text)

    def test_planner_renders_platform_repair_authorization_boundary(self):
        """Static rendered instruction contract, not a live agent-behavior test."""
        text = render_role(self.template("planner"), self.values("planner"), "planner")
        scope = text.split("## Evidence and scope\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn(
            "Treat repairs to the agent platform or shared toolchain as separate scope "
            "unless the customer explicitly included them in the approved assignment.", scope)
        self.assertIn(
            "Obtain that authorization before planning repair work, creating repair tasks, "
            "or delegating repairs.", scope)
        self.assertIn(
            "You can resolve minor, locally correctable implementation details", text)
        self.assertIn(
            "Use only an authorized native one-time resume mechanism.", text)

    def test_planner_renders_safe_continuation_without_optional_platform_gate(self):
        """Static rendered instruction contract, not a live agent-behavior test."""
        text = render_role(self.template("planner"), self.values("planner"), "planner")
        scope = text.split("## Evidence and scope\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn(
            "If an existing authorized procedure permits safe project continuation, "
            "do not make an optional platform improvement an additional prerequisite.", scope)
        self.assertIn("Never waive required safety or verification gates to save cost.", scope)
        self.assertIn("Start successors only after independent review reaches `done`.", text)

    def test_coder_checks_reported_obstacles_before_escalating(self):
        paragraph = "Check each obstacle that Codex reports against the concrete flow yourself. Separate a confirmed finding, an open verifiable question, and a hypothetical possibility."
        source = self.template("coder")
        self.assertEqual(source.count(paragraph), 1)
        rendered = render_role(source, self.values("coder"), "coder")
        self.assertEqual(rendered.count(paragraph), 1)

    def test_planner_checks_blocker_premises_before_adding_requirements(self):
        paragraph = "Confirm a real blocker before escalation. Resolve local technical or harmless details within the accepted scope."
        source = self.template("planner")
        self.assertEqual(source.count(paragraph), 1)
        rendered = render_role(source, self.values("planner"), "planner")
        self.assertEqual(rendered.count(paragraph), 1)

    def test_caveman_style_is_scoped_to_the_coder(self):
        self.assertIn("$caveman", self.template("coder"))
        self.assertNotIn("caveman", self.template("reviewer"))

    def test_nonplaceholder_bytes_preserved(self):
        for role in MANIFEST["role_templates"]:
            source = self.template(role)
            values = self.values(role)
            output = render_role(source, values, role)
            expected = re.sub(r"\{\{([A-Z0-9_]+)\}\}", lambda m: values[m[1]], source)
            self.assertTrue(expected == output, role)


class TicketDocumentationTests(unittest.TestCase):
    """Static instruction contracts, not live agent-behavior tests."""

    def setUp(self):
        self.root = ROOT / "skills/brownfield-feature-planning"
        self.skill = (self.root / "SKILL.md").read_text()
        self.release = (self.root / "references/kanban-phase-release.md").read_text()
        self.status = (self.root / "references/kanban-status-inspection.md").read_text()
        self.recovery = (self.root / "references/kanban-triage-recovery.md").read_text()
        self.operator = (self.root / "references/operator-script-acceptance.md").read_text()

    def test_normal_handoff_uses_git_baseline_and_native_card(self):
        self.assertIn("Keep the accepted plan and phase plan in the agreed versioned project location.", self.skill)
        self.assertIn("Record ticket documentation directly on the existing Kanban card.", self.skill)
        self.assertIn("Keep product documentation in its owning repository.", self.skill)
        self.assertIn("Read the accepted specification and plan at their approved Git revisions.", self.release)
        self.assertIn("Verify that every plan reference resolves to its approved revision.", self.release)
        self.assertIn("Verify every notification binding against the intended destination.", self.release)
        self.assertIn("Unblock descendants in reverse order and phase one last.", self.release)

    def test_partial_creation_resumes_from_persisted_cards(self):
        self.assertIn("approved plan path, plan commit and phase identifier", self.release)
        self.assertIn("including archived cards", self.release)
        self.assertIn("Reuse exact matching cards and create only missing phases.", self.release)
        self.assertIn("Read each returned exact card before further writes.", self.release)
        self.assertIn("Stop release on any unresolved mismatch", self.release)

    def test_partial_release_preserves_completed_transitions(self):
        self.assertIn("Before the first release, require every card to be blocked.", self.release)
        self.assertIn("On partial release, verify current runs and dependency gates for already released cards.", self.release)
        self.assertIn("Preserve completed release transitions.", self.release)
        self.assertIn("On resume, apply this order only to pending initial releases.", self.release)
        self.assertNotIn("Every card is still blocked", self.release)
        self.assertNotIn("attachment verification", self.skill)

    def test_correction_updates_existing_assignment_and_plan_reference(self):
        self.assertIn("Update both bodies to reference the exact approved amended plan revision.", self.release)
        self.assertIn("Replace contradictory active body instructions through the supported edit operation.", self.recovery)
        self.assertIn("Preserve the existing card, authorized scope, history, valid dependencies, review provenance and counters.", self.recovery)
        self.assertIn("Keep independent review and required safety checks.", self.skill)

    def test_evidence_reuse_preserves_required_final_state_gates(self):
        self.assertIn("Reuse evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid.", self.skill)
        self.assertIn("A new commit alone does not invalidate every prior result.", self.skill)
        self.assertIn("Keep evidence on the existing card and in original run outputs, not in a separate summary or evidence register.", self.skill)
        self.assertIn("If acceptance explicitly requires an integrated run on the final state", self.status)
        self.assertIn("Do not count targeted tests as that required full acceptance run.", self.status)
        self.assertNotIn("If full acceptance ran on an earlier tree, retain the exact-final-commit gap", self.status)

    def test_operator_blocker_keeps_evidence_and_ownership_on_card(self):
        self.assertIn("Route the handoff to the existing card's authorized owner.", self.status)
        self.assertIn("restart impact", self.status)
        self.assertIn("rollback", self.status)
        self.assertIn("Append actual receipt and explicit assessment to the existing acknowledgment card.", self.operator)
        self.assertIn("Record the repaired boundary, evidence, intended owner, remaining file/verification/commit/review work and unchanged exclusions on the existing card.", self.recovery)
        self.assertIn("Read back the body and resumption comment before release.", self.recovery)
        self.assertIn("Do not complete, reclaim, redispatch, or overwrite it.", self.operator)
        self.assertIn("Verify process exit separately from `ended_at` or board `done`.", self.recovery)
        self.assertIn("Keep orders, results, and assessments on existing Kanban cards", self.operator)

    def test_removed_file_duties_do_not_survive_in_loaded_procedures(self):
        retrospective = (self.root / "references/project-retrospectives.md").read_text()
        self.assertIn("Record a ticket retrospective on the existing card.", retrospective)
        text = "\n".join((self.skill, self.release, self.status, self.recovery, self.operator, retrospective))
        for obsolete in (
            "durable manifest", "repository manifest commit", "existing manifest",
            "central receipt record", "central resumption decision",
            "central feature collection and its index", "README index",
            "Attach the accepted plan and specification as real files",
            "attach the amended plan to both tasks",
            "For an operator handoff, write a durable file",
        ):
            with self.subTest(obsolete=obsolete):
                self.assertNotIn(obsolete, text)


if __name__ == "__main__":
    unittest.main()
