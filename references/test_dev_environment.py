"""Static development-environment contracts, not Docker or agent behavior tests."""
import json
from pathlib import Path
import unittest

from test_brownfield_planning import local_links

try:
    from ruamel.yaml import YAML
    yaml_load = YAML(typ="safe").load
except ImportError:
    import yaml
    yaml_load = yaml.safe_load

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills/dev-environment"


class DevelopmentEnvironmentTests(unittest.TestCase):
    def text(self):
        path = PACKAGE / "SKILL.md"
        self.assertTrue(path.is_file(), "Missing owned development-environment skill")
        return path.read_text()

    def test_complete_planner_only_skill_and_portable_metadata(self):
        text = self.text()
        manifest = json.loads((ROOT / "manifest.json").read_text())
        self.assertIn("dev-environment", manifest["own_skills"])
        entry = manifest["own_skills"]["dev-environment"]
        self.assertEqual(entry["targets"], {"hermes": ["planner"]})
        self.assertEqual(entry["skill_path"], "skills/dev-environment/SKILL.md")
        self.assertEqual(entry["transport"], {"SKILL.md": "SKILL.md"})
        self.assertEqual([p for p in manifest["files"] if p.startswith("skills/dev-environment/")],
                         ["skills/dev-environment/SKILL.md"])
        self.assertEqual({p.name for p in PACKAGE.iterdir()}, {"SKILL.md"})
        self.assertNotIn("dev-environment", manifest["upstream_components"])
        header, body = text[4:].split("\n---\n", 1)
        meta = yaml_load(header)
        self.assertEqual(meta["name"], "dev-environment")
        self.assertEqual(meta["license"], "MIT")
        self.assertEqual(meta["platforms"], ["linux"])
        self.assertLessEqual(len(meta["description"]), 60)
        self.assertNotIn("disable-model-invocation", meta)
        self.assertNotRegex(body, r"/home/|/workspace/|\bMTB\b|\bSG1\b|check_candidate_skill")
        local_links(PACKAGE)

    def test_absent_usable_and_incomplete_paths_preserve_scope(self):
        text = self.text()
        for clause in (
            "Reuse a working toolchain and entrypoint",
            "If absent, plan the tools under `docker/dev/`",
            "If incomplete, fix only the gap within the accepted scope",
            "Preserve local inputs and data",
            "Documentation-only adoption authorizes no rebuild",
            "Resolve missing Docker access with the operator",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, text)

    def test_only_guide_carries_environment_specific_operations(self):
        text = self.text()
        for clause in (
            "Guide: one short `docker/dev/AGENTS.md`, or the actual guide path in an adopted layout.",
            "Content: only environment-specific changes to the coder's workflow.",
            "Use one line per operation with a short label and exact invocation.",
            "State non-obvious targets or destructive effects where relevant.",
            "Loader: root `AGENTS.md` requires the guide by repository-relative path when a task uses the environment.",
        ):
            self.assertIn(clause, text)
        self.assertNotIn("Caveman", text)
        self.assertNotIn("HOWTO-human.md", text)

    def test_optional_database_targets_only_development_state(self):
        text = self.text()
        for clause in ("add a project-compatible database to development Compose only if needed for coding",
                       "verify the dev target before writes",
                       "If branch databases are agreed", "preserve its state on return",
                       "Reset only the selected disposable state"):
            self.assertIn(clause, text)

    def test_tools_see_working_tree_and_deployment_stays_separate(self):
        text = self.text()
        for clause in ("Do not install these tools on the host", "not an agent sandbox",
                       "Bind-mount the current checkout directly", "without staging, copying or synchronizing",
                       "optionally start the app from source", "starting and stopping them is part of your development and demonstration authority"):
            self.assertIn(clause, text)

    def test_acceptance_exercises_edit_and_new_test(self):
        acceptance = self.text().split("## Verify the developer workflow\n", 1)[1]
        for clause in ("Reviewer follows the guide", "runs a real project build",
                       "one reversible source change and a new, untracked targeted test",
                       "Rerun the selected test after the edit.",
                       "Its result must reflect the change without staging files or rebuilding the tool image.",
                       "any unverified capability on the existing task"):
            self.assertIn(clause, acceptance)
        self.assertNotIn("demonstration", acceptance.lower())


if __name__ == "__main__":
    unittest.main()
