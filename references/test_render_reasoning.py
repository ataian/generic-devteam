"""Offline regression checks; run: python3 -B references/test_render_reasoning.py."""
import json
from pathlib import Path
import re
import unittest

from render_text import render_role, role_fields

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text())
REASONING_FIELDS = {
    "planner": set(),
    "coder": {"CODEX_REASONING_DEFAULT", "CODEX_REASONING_MAX"},
    "reviewer": {"ROLE_REASONING_DEFAULT", "ROLE_REASONING_HIGH"},
}


class ReasoningContractTests(unittest.TestCase):
    def template(self, role):
        return (ROOT / MANIFEST["role_templates"][role]["template_path"]).read_text()

    def values(self, role, default="medium", maximum="high"):
        values = {key: "Example" for key in role_fields(self.template(role), role)}
        for key in values:
            if key.endswith("_PROFILE"):
                values[key] = "example-role"
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
            'model_reasoning_effort=\'"low"\'',
        ]:
            self.assertTrue(text in result, text)
        self.assertNotIn("if the worker guard prohibits them", result)
        self.assertNotIn("{{", result)

    def test_reviewer_uses_concrete_values_and_an_independent_second_pass(self):
        result = render_role(self.template("reviewer"), self.values("reviewer", "low", "medium"), "reviewer")
        for text in [
            "Use the configured default reasoning `low` for normal changes.",
            "You can upgrade to `medium` at any time.",
            "A required second pass is a separate run at reasoning `medium` with the unchanged model and provider.",
            "Do not restate the first reasoning.",
            "Perform the second pass and produce the high-risk evidence block.",
        ]:
            self.assertTrue(text in result, text)
        self.assertNotIn("{{", result)
        self.assertNotIn("Reasoning Stufe", result)

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
        text = self.template("coder")
        self.assertIn("Route the same task to the verified Planner profile through native `kanban_request_review`.", text)
        self.assertIn("The Planner profile identifier comes from the setup record", text)
        self.assertIn("Resume after `kanban_request_changes` and reread the baseline.", text)
        self.assertNotIn("Budgetfragen", text)
        self.assertNotIn("Budgetfreigaben", text)

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


if __name__ == "__main__":
    unittest.main()
