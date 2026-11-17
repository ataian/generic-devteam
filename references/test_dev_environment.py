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
            "absent, usable, or incomplete/incompatible; an inspection failure is not absence",
            "Default to `docker/dev/` under the code repository root.",
            "Preserve working layout, local inputs and data.",
            "A documentation-only task preserves the current database and reports this gap",
            "preserve reusable parts and name the precise missing capability",
            "Missing host capabilities are prerequisites to resolve with the operator",
            "Additional third-party services or simulators belong to separately agreed project-specific work.",
            "this skill adds no separate approval process",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, text)

    def test_guides_and_root_pointer_keep_audience_separation(self):
        text = self.text()
        guides = text.split("5. **Write the two guides.**", 1)[1].split("6. **Verify and hand over.**", 1)[0]
        for clause in ("`docker/dev/AGENTS.md`", "`docker/dev/HOWTO-human.md`",
                       "standalone instructions for a human using Linux without agents",
                       "Keep the agent guide self-contained for ordinary work.",
                       "root AGENTS.md pointer requiring the agent guide for development planning, implementation and review",
                       "Require its container commands for builds, tests and development servers.",
                       "both audiences can follow their own guide, with no unresolved command placeholders"):
            self.assertIn(clause, guides)
        self.assertIn("Agent instructions contain no pointer to the human guide and no instruction prohibiting its reading.", text)

    def test_integrated_database_and_branch_clone_preservation_contract(self):
        text = self.text()
        self.assertIn("include the compatible database service and persistent storage in the same development Compose project", text)
        branch = text.split("## PostgreSQL branch databases\n", 1)[1].split("## Acceptance cases", 1)[0]
        for clause in (
            "project's agreed schema and permitted data source",
            "the application does not target the template",
            "collision handling for branch-name normalization and database identifier limits",
            "createdb --template=<template> --owner=<role> <branch_database>",
            "Check source sessions, privileges and target absence before creation",
            "Coordinate unknown or external connections rather than terminating them.",
            "Reuse an existing target only when its recorded branch binding matches",
            "Verify the actual database and role before migrations, seeding or write tests.",
            "Returning to a branch reuses its database and state rather than cloning again.",
            "Reset only explicitly selected disposable branch/test state",
            "without altering the baseline or another branch",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, branch)
        self.assertIn("operational data requires a separate explicit authorization", text)
        acceptance = text.split("## Acceptance cases\n", 1)[1]
        self.assertIn("Change one, then verify the baseline and the other branch remain unchanged.", acceptance)
        self.assertIn("naming collision and a connected-template failure", acceptance)

    def test_runtime_operations_keep_source_and_external_boundaries(self):
        text = self.text()
        scope = text.split("## Operating scope\n", 1)[1].split("## Procedure", 1)[0]
        for clause in (
            "start, stop, restart, rebuild and recreate these resources without further customer approval",
            "generate synthetic data and reset disposable development state",
            "Coordinate disruptive operations with other team users of the same runtime",
            "Preserve source work, credentials, operational data, unrelated resources and the PostgreSQL baseline",
            "Host administration, shared infrastructure and external effects retain their existing authorization boundaries.",
            "development operations, not publication or deployment",
            "the Reviewer operates the runtime without repairing product code",
        ):
            self.assertIn(clause, scope)
        self.assertIn("Routine pause/resume retains state", text)
        self.assertIn("Verify reuse of the tool container and retained dependencies/caches without rebuilding or reinstalling.", text)

    def test_demo_handoff_requires_access_and_honest_evidence(self):
        text = self.text()
        for clause in (
            "verify application readiness and provide the concrete browser URL and SSH local-forward command when needed",
            "confirmed SSH access and actual loopback ports",
            "disclose any untested client-side access",
            "Leave the demonstrated application running for customer use",
            "Publish development listeners only on loopback by default.",
            "A version command, running container or skipped test is not that evidence.",
            "required missing evidence prevents a readiness claim",
        ):
            self.assertIn(clause, text)


if __name__ == "__main__":
    unittest.main()
