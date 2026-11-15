"""Static package contracts for the owned devteam-cleanup skill.

Run: python3 -B -m unittest discover -s references -p 'test_devteam_cleanup.py' -v
Uses an already available safe YAML parser; never installs dependencies.
"""
from pathlib import Path
import unittest

try:
    from ruamel.yaml import YAML
    YAML_SAFE_LOAD = YAML(typ="safe").load
except ImportError:
    import yaml
    YAML_SAFE_LOAD = yaml.safe_load


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = __import__("json").loads((ROOT / "manifest.json").read_text())
SKILL = ROOT / "skills/devteam-cleanup/SKILL.md"


class DevteamCleanupSkillTests(unittest.TestCase):
    """The skill stays customer-invoked, reversible, and outside the delivery flow."""

    def test_manifest_binding_targets_planner_only(self):
        item = MANIFEST["own_skills"]["devteam-cleanup"]
        self.assertEqual(item["status"], "included")
        self.assertEqual(item["targets"], {"hermes": ["planner"]})
        self.assertEqual(item["transport"], {"SKILL.md": "SKILL.md"})
        self.assertTrue(SKILL.is_file())
        self.assertIn("skills/devteam-cleanup/SKILL.md", MANIFEST["files"])

    def test_frontmatter_name_and_trigger_are_explicit(self):
        text = SKILL.read_text()
        header = YAML_SAFE_LOAD(text.split("---", 2)[1])
        self.assertEqual(header["name"], "devteam-cleanup")
        self.assertIn("customer asks the team to clean up", header["description"])
        self.assertIn("Use when the customer asks for cleanup", text)

    def test_skill_stays_outside_the_delivery_flow(self):
        text = SKILL.read_text()
        self.assertIn("No step in the delivery flow requires cleanup.", text)
        self.assertIn("Accepted review is not customer acceptance", text)

    def test_branch_and_evidence_protection_is_stated(self):
        text = SKILL.read_text()
        self.assertIn("neither merged nor explicitly released", text)
        self.assertIn("Never remove evidence referenced by a review or a card comment.", text)
        self.assertIn("Completion criterion:", text)


if __name__ == "__main__":
    unittest.main()
