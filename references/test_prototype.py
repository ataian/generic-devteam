"""Static clarification contracts, not tests of a demo or live model behavior."""
import json
from pathlib import Path
import unittest

from render_text import render_role, role_fields
from test_brownfield_planning import local_links

try:
    from ruamel.yaml import YAML
    yaml_load = YAML(typ="safe").load
except ImportError:
    import yaml
    yaml_load = yaml.safe_load

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills/prototype"
FILES = {"SKILL.md", "LOGIC.md", "UI.md", "NOTICE.md", "LICENSE"}
CONTRACT = (
    "Owner: the Planner writes and adjusts the demo directly during grilling, before final plan acceptance when "
    "useful.",
    "Demo only: no Coder, Team-Codex, delegation, Kanban ticket, automated tests, test suite, independent review "
    "or extra approval round.",
    "Product work retains accepted-plan, Codex, testing and independent-review requirements.",
    "Files: the Planner's existing planning `docs/` beside the plan, even across repositories.",
    "Exclude the product directory, application routes, build configuration and production assets.",
    "No required commit, throwaway branch, publication, separate report or cleanup ritual.",
    "Carry only the clarified decision into the product plan. The demo provides no evidence of production correctness "
    "or approval of new scope.",
)


def require_contract(text):
    for clause in CONTRACT:
        assert clause in text, clause


class PrototypeTests(unittest.TestCase):
    def text(self, name="SKILL.md"):
        return (PACKAGE / name).read_text()

    def test_complete_planner_only_package_and_export_inventory(self):
        manifest = json.loads((ROOT / "manifest.json").read_text())
        self.assertEqual({p.name for p in PACKAGE.iterdir() if p.is_file()}, FILES)
        entry = manifest["own_skills"]["prototype"]
        self.assertEqual(entry["targets"], {"hermes": ["planner"]})
        self.assertEqual(entry["skill_path"], "skills/prototype/SKILL.md")
        self.assertEqual(entry["transport"], {"SKILL.md": "SKILL.md"})
        self.assertEqual({p for p in manifest["files"] if p.startswith("skills/prototype/")},
                         {"skills/prototype/" + name for name in FILES})
        self.assertNotIn("prototype", manifest["upstream_components"])
        for path in PACKAGE.rglob("*"):
            self.assertFalse(path.is_symlink())
            if path.is_file():
                self.assertNotRegex(path.read_text(), r"/home/|/workspace/|/tmp/")
        local_links(PACKAGE)

    def test_metadata_and_conditional_branch_loading(self):
        header, body = self.text()[4:].split("\n---\n", 1)
        meta = yaml_load(header)
        self.assertEqual(meta["name"], "prototype")
        self.assertEqual(meta["license"], "MIT")
        self.assertTrue(meta["description"].startswith("Use when"))
        self.assertLessEqual(len(meta["description"]), 60)
        self.assertNotIn("disable-model-invocation", meta)
        for clause in ("read its branch before building", "[LOGIC.md](LOGIC.md)", "[UI.md](UI.md)",
                       "continue verbal clarification", "synthetic data, in-memory state",
                       "No real mutations, sensitive data, live services or dependency installations.",
                       "Open it with available local preview or browser tools and try the relevant controls",
                       "without building preview infrastructure",
                       "Simplify if construction grows into a development project",
                       "Resume grilling from that result without separate prototype acceptance"):
            self.assertIn(clause, body)

    def test_direct_clarification_scenarios_and_missing_clause_mutations(self):
        text = self.text()
        require_contract(text)
        for clause in CONTRACT:
            with self.subTest(removed=clause), self.assertRaises(AssertionError):
                require_contract(text.replace(clause, ""))

    def test_logic_and_ui_preserve_decision_methods_without_product_writes(self):
        logic = self.text("LOGIC.md")
        ui = self.text("UI.md")
        for clause in ("single self-contained HTML", "domain language", "free-play buttons",
                       "guided scenarios", "Each step performs the actual demo action",
                       "in-memory examples", "Do not lift demo logic into product code automatically."):
            self.assertIn(clause, logic)
        for clause in ("For competing layouts, vary information hierarchy, layout and primary actions.",
                       "Colour alone is insufficient.", "not a quota", "?variant=",
                       "focused text inputs", "local stubs",
                       "Represent that context in the demo and keep the real application untouched",
                       "No application route", "Keep variants and switcher in planning `docs/`"):
            self.assertIn(clause, ui)

    def test_rendered_planner_trigger_keeps_product_gates(self):
        manifest = json.loads((ROOT / "manifest.json").read_text())
        path = manifest["role_templates"]["planner"]["template_path"]
        text = (ROOT / path).read_text()
        values = {key: "synthetic" for key in role_fields(text, "planner")}
        values["PROJECT_DIR"] = "/synthetic/workspace"
        rendered = render_role(text, values, "planner")
        for clause in ('skill_view(name="prototype")', "During grilling", "write isolated throwaway",
                       "without Coder, Codex, tickets, automated tests, independent review, or extra approval rounds",
                       "Product implementation retains the normal workflow and gates",
                       "Do not create implementation tickets before acceptance.",
                       "Assign implementation to", "If a prototype clarified a decision"):
            self.assertIn(clause, rendered)
        for role in ("coder", "reviewer"):
            self.assertNotIn('skill_view(name="prototype")', (ROOT / manifest["role_templates"][role]["template_path"]).read_text())
        self.assertIn('skill_view(name="prototype")', (ROOT / "skills/brownfield-feature-planning/SKILL.md").read_text())

    def test_delivery_dependency_and_setup_boundaries(self):
        recipe = (ROOT / "references/integrations.md").read_text().split("## Owned prototype — Planner only\n", 1)[1].split("\n<a id=", 1)[0]
        for clause in ("collisions", "complete tree unchanged", "<PLANNER_HOME>/skills/prototype/",
                       "Before role personalization", "After SOUL delivery", "legacy SOUL-only",
                       "Withhold the dependent Planner clauses", "do not build a demonstration"):
            self.assertIn(clause, recipe)
        for name in ("setup.md", "update.md", "verification.md", "native-workflow.md"):
            self.assertIn("integrations.md#prototype", (ROOT / "references" / name).read_text())

    def test_provenance_covers_complete_original_and_approved_differences(self):
        notice = self.text("NOTICE.md")
        self.assertIn("4ae2317ddb22b046e26455e4f9c9b3aaaf62212d", notice)
        for source in ("SKILL.md", "LOGIC.md", "UI.md", "agents/openai.yaml"):
            self.assertIn("skills/engineering/prototype/" + source, notice)
        for clause in ("Planner writes directly", "planning `docs/`", "No Coder/Team-Codex",
                       "No tickets, test/review pipeline", "do not lift prototype logic"):
            self.assertIn(clause, notice)
        for clause in ("Copyright (c) 2026 Matt Pocock", "Permission is hereby granted, free of charge",
                       "The above copyright notice and this permission notice shall be included",
                       'THE SOFTWARE IS PROVIDED "AS IS"'):
            self.assertIn(clause, self.text("LICENSE"))


if __name__ == "__main__":
    unittest.main()
