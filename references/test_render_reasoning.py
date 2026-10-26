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
            'Team-Codex: Standard `low`, Obergrenze `high`.',
            'LOW/LOW oder MEDIUM/LOW → Reasoning low.',
            'HIGH complexity oder HIGH failure impact → Reasoning höchstens high.',
            'HIGH+HIGH → Reasoning high.',
            'model_reasoning_effort=\'"low"\'',
        ]:
            self.assertTrue(text in result, text)
        self.assertNotIn("höchstes unterstütztes Reasoning", result)

    def test_reviewer_headings_and_second_pass_use_concrete_values(self):
        result = render_role(self.template("reviewer"), self.values("reviewer", "low", "medium"), "reviewer")
        for text in [
            '### Reasoning Stufe low — Default',
            '### Reasoning Stufe medium — verpflichtend bei hohem Risiko',
            '### Reasoning Stufe medium — hohe Prüftiefe Second Pass',
            'Re-Read auf Reasoning medium',
            'unabhängiger Second Pass auf medium',
        ]:
            self.assertTrue(text in result, text)
        self.assertNotIn("Reasoning high", result)
        self.assertNotIn("bestätigten Obergrenze", result)

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
        self.assertIn("Behebbare Aufruf- und Argumentfehler", text)
        self.assertIn("innerhalb des freigegebenen Auftrags und Budgets", text)
        self.assertIn("tatsächlich nicht verfügbar", text)
        self.assertIn('kanban_block(kind="capability"', text)
        self.assertNotIn("Netzwerk — egal was", text)
        self.assertNotIn("Ohne Codex KEINE Arbeit", text)
        self.assertNotIn("Implementierung, Tests und Debugging laufen über Codex", text)

    def test_coder_handoff_verification_matches_its_purpose(self):
        text = self.template("coder")
        self.assertIn("Beim Implementierungsabschluss", text)
        self.assertIn("bei Klärungen die Plannerprofilkennung", text)
        self.assertNotIn("Nach jedem `kanban_request_review`", text)
        self.assertNotIn("schlägt der Handoff STILL fehl", text)

    def test_coder_routes_budget_decisions_to_planner(self):
        text = self.template("coder")
        self.assertIn("Entscheidungen und Freigaben einschließlich Budgetfragen", text)
        self.assertIn("dieselbe Karte per `kanban_request_review`", text)
        self.assertIn("Der Planner antwortet und gibt mit `kanban_request_changes` zurück.", text)

    def test_nonplaceholder_bytes_preserved(self):
        for role in MANIFEST["role_templates"]:
            source = self.template(role)
            values = self.values(role)
            output = render_role(source, values, role)
            expected = re.sub(r"\{\{([A-Z0-9_]+)\}\}", lambda m: values[m[1]], source)
            self.assertTrue(expected == output, role)


if __name__ == "__main__":
    unittest.main()
