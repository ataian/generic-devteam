"""Static pinned-environment skill contracts, not Docker or agent behavior tests."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text())

PINS = {
    "disposable-demo": {
        "repo": "https://github.com/ataian/disposable-demo",
        "revision": "2c6331d1fc73ae25744d11399feafc19f798c13b",
        "subpaths": [
            "SKILL.md",
            "README.md",
            "scripts/demo.sh",
            "scripts/demo_state.py",
            "scripts/demo_accounts.py",
            "templates/AGENTS.md",
            "templates/compose.yaml",
            "templates/init.example.sql",
            "templates/realm.example.json",
            "templates/seed.example.sql",
            "tests/smoke.md",
        ],
        "references": ("SKILL.md", "README.md", "tests/smoke.md"),
    },
    "dev-environment": {
        "repo": "https://github.com/ataian/dev-environment",
        "revision": "3205d3a70fe6ad65c191d07172e106895b75fa04",
        "subpaths": [
            "SKILL.md",
            "references/install.md",
            "references/toolchain.md",
            "scripts/dev.sh",
            "scripts/dev-runner.py",
            "scripts/run-in-tools.sh",
        ],
        "references": ("SKILL.md", "references/install.md", "references/toolchain.md"),
    },
}


def read(name):
    return (ROOT / name).read_text()


def section(text, start, end):
    """Return the text between two exact markers, excluding both."""
    assert start in text, start
    assert end in text, end
    return text.split(start, 1)[1].split(end, 1)[0]


class PinnedEnvironmentDeliveryTests(unittest.TestCase):
    """Written state only; native loading and runtime remain separate evidence."""

    def test_manifest_declares_both_components_for_all_hermes_roles(self):
        for name, pin in PINS.items():
            with self.subTest(component=name):
                entry = MANIFEST["upstream_components"][name]
                self.assertEqual(entry["original_repo"], pin["repo"])
                self.assertEqual(entry["source_revision"], pin["revision"])
                self.assertEqual(entry["subpaths"], pin["subpaths"])
                self.assertEqual(entry["targets"], {
                    "hermes": ["planner", "coder", "reviewer"],
                })
                self.assertEqual(entry["recipe_ref"], f"references/integrations.md#{name}")
                self.assertEqual(entry["recipe_status"], "documented")
                self.assertEqual(entry["legal_files"], [],
                                 "Neither pin supplies a license file; record the empty inventory.")

    def test_selected_paths_exclude_repository_planning_files(self):
        for name, pin in PINS.items():
            with self.subTest(component=name):
                for path in pin["subpaths"]:
                    self.assertNotEqual(path, "AGENTS.md")
                    self.assertNotEqual(path, "HERMES.md")
                    self.assertNotEqual(path, ".gitignore")
                    self.assertFalse(path.startswith(("docs/", ".hermes/")))
                    self.assertFalse(path.startswith("tests/test_"))
                self.assertNotIn("HERMES.md", pin["subpaths"])
        self.assertFalse(
            any(path.startswith("tests/") for path in PINS["dev-environment"]["subpaths"]),
            "dev-environment ships no tests/ files; disposable-demo keeps tests/smoke.md",
        )
        self.assertIn("tests/smoke.md", PINS["disposable-demo"]["subpaths"])

    def test_recipes_copy_selected_paths_with_git_modes_and_load_references(self):
        recipe = read("references/integrations.md")
        for name, pin in PINS.items():
            with self.subTest(component=name):
                self.assertIn(f'<a id="{name}"></a>', recipe)
                section = recipe.split(f'<a id="{name}"></a>', 1)[1].split("\n<a id=", 1)[0]
                for clause in (
                    pin["repo"],
                    pin["revision"],
                    "never a branch tip, working copy or republished copy",
                    "<ROLE_HOME>/skills/",
                    "pinned Git objects",
                    "100755",
                    "native discovery",
                    "delivery incomplete",
                    "guarded file-update rollback",
                ):
                    self.assertIn(clause, section)
                for reference in pin["references"]:
                    self.assertIn(f"`{reference}`", section)
        dev = recipe.split('<a id="dev-environment"></a>', 1)[1].split("\n<a id=", 1)[0]
        self.assertIn("no second Codex skill installation", dev)
        self.assertNotIn("demo-handover", recipe.split('<a id="disposable-demo"></a>', 1)[1]
                         .split('<a id="prototype"></a>', 1)[0])

    def test_recipe_preamble_preserves_complete_trees_and_names_the_subpath_exception(self):
        recipe = read("references/integrations.md")
        preamble = recipe.split('<a id="', 1)[0]
        self.assertIn("Use complete original trees", preamble)
        self.assertIn(
            "Exception: when an `upstream_components` entry selects `subpaths`, "
            "deliver exactly those paths unchanged",
            preamble,
        )

    def test_setup_acquires_fixed_commits_and_delivers_to_every_profile(self):
        setup = section(
            read("references/setup.md"),
            "1. **Copy skills.**",
            "2. **Verify configuration.**",
        )
        for clause in (
            "fixed `source_revision`",
            "never a branch tip, working copy or development path",
            "`upstream_components.disposable-demo`",
            "`upstream_components.dev-environment`",
            "[disposable-demo](integrations.md#disposable-demo)",
            "[dev-environment](integrations.md#dev-environment)",
            "every profile named by `targets`",
            "compare bytes and Git executable bits",
            "Do not install repository planning files.",
        ):
            self.assertIn(clause, setup)

    def test_setup_readback_names_both_skills_in_every_profile(self):
        setup = section(
            read("references/setup.md"),
            "6. **Read back every target.**",
            "### Bind the planner recovery invocation",
        )
        self.assertIn("`disposable-demo` and `dev-environment` in every assigned profile", setup)
        self.assertIn("`disposable-demo` and `dev-environment` in Planner, Coder and Reviewer profiles", setup)
        self.assertIn("In the Planner profile load `references/install.md` and "
                      "`references/toolchain.md` from the installed `dev-environment` skill; "
                      "either unresolved reference leaves delivery incomplete.", setup)
        self.assertNotIn("requested-demo.md", setup)
        self.assertNotIn("demo-handover", setup)
        for preserved in (
            "all three original Planner skill trees",
            "required `grilling` load",
            "conditional `domain-modeling` load",
            "separate plan acceptance",
            "default/max values and process binding",
            "compact task/resume instructions and propagation to fresh delegation",
        ):
            with self.subTest(clause=preserved):
                self.assertIn(preserved, setup)

    def test_readme_keeps_the_environment_creation_offer(self):
        readme = read("README.md")
        self.assertIn(
            "Setup may offer environment creation as a first task; neither setup nor updates execute it.",
            readme,
        )
        self.assertIn("also receive the pinned [disposable-demo]", readme)

    def test_sources_and_notice_record_provenance_and_permission_boundary(self):
        sources = read("references/upstream-sources.md")
        notice = read("NOTICE.md")
        for obsolete in ("own-demo-handover", "own-dev-environment", "skills/demo-handover",
                         "skills/dev-environment", "references/requested-demo.md"):
            with self.subTest(obsolete=obsolete):
                self.assertNotIn(obsolete, sources)
                self.assertNotIn(obsolete, json.dumps(MANIFEST["own_skills"]))
                self.assertNotIn(obsolete, json.dumps(MANIFEST["files"]))
        self.assertNotIn('id="demo-handover"', read("references/integrations.md"))
        self.assertIn(
            "Follow the [disposable-demo](integrations.md#disposable-demo) and "
            "[dev-environment](integrations.md#dev-environment) recipes.",
            sources,
        )
        for name, pin in PINS.items():
            with self.subTest(component=name):
                self.assertIn(f'<a id="{name}"></a>', sources)
                self.assertIn(pin["repo"], sources)
                self.assertIn(pin["revision"], notice)
                self.assertIn(pin["repo"], notice)
                self.assertIn(f"`{name}` skill 0.1.0", notice)
        self.assertEqual(notice.count("not the source repository"), 2)
        self.assertIn("GitHub provenance", notice)
        self.assertIn("no license file", notice)
        self.assertIn("Documented integration intent/evidence", notice)
        self.assertIn("is not a license", notice)
        self.assertIn("establishes no redistribution right", notice)
        self.assertIn("Redistribution remains unconfirmed", notice)
        for unsupported in ("authorizes delivery", "grants no wider rights", "documented permission scope",
                            "Uses this package's MIT license"):
            with self.subTest(unsupported=unsupported):
                self.assertNotIn(unsupported, notice)

    def test_setup_and_update_link_both_acquisition_recipes(self):
        for name in ("setup.md", "update.md"):
            text = read(f"references/{name}")
            with self.subTest(file=name):
                self.assertIn("[disposable-demo](integrations.md#disposable-demo)", text)
                self.assertIn("[dev-environment](integrations.md#dev-environment)", text)

    def test_package_versions_match(self):
        skill = read("SKILL.md")
        self.assertIn(f"version: {MANIFEST['version']}", skill.splitlines())

    def test_role_contracts_route_environment_work_and_keep_no_retired_skill(self):
        planner = read("templates/roles/planner.SOUL.md.template")
        coder = read("templates/roles/coder.SOUL.md.template")
        reviewer = read("templates/roles/reviewer.SOUL.md.template")
        for text in (planner, coder, reviewer):
            self.assertNotIn("requested-demo", text)
            self.assertNotIn("demo-handover", text)
            self.assertNotIn("owned `dev-environment`", text)
        self.assertIn("account for it in the plan", planner)
        self.assertIn("apply its installer to the actual project root", planner)
        self.assertIn("reuse a suitable existing environment instead of recreating it per ticket", planner)
        self.assertIn("route execution to the documented project container commands", coder)
        self.assertIn("route execution to the documented project container commands", reviewer)

        # Planner demo decision: retire on both answers, stop on unknown ownership.
        self.assertIn("previous skill-managed project demo will be removed", planner)
        self.assertIn("Retire the previous demo on both answers without another permission request.", planner)
        self.assertIn("Unknown ownership or an unreachable engine: stop and report", planner)
        self.assertIn("No plus verified absence", planner)
        self.assertIn("one final `Demo handover` card", planner)
        self.assertIn("dependent on the last reviewed implementation", planner)
        self.assertIn("Keep the card blocked and not eligible for automatic promotion.", planner)
        self.assertIn("operator-approved canonical `docker_host`", planner)
        self.assertIn("independently recorded `docker_daemon_id`", planner)
        self.assertIn("write the exact reviewed commit on the card, read it back, then release it", planner)
        self.assertIn("branch HEAD is not a substitute", planner)

        # Local Maker-only direct owner handover; the pinned upstream rule stays untouched.
        for clause in (
            "Direct owner handover for this team only",
            "the installed upstream `disposable-demo` skill prohibits credentials in chat",
            "you are the handover operator instead of its private-editor-only route",
            "one row per intended demo user with username, role and effective provisioned password",
            "`<project>/demo/.runtime/accounts.json`",
            "private handover record path the Coder recorded on the card",
            "No file-pointer-only handover.",
            "Do not send tokens, bootstrap/service credentials or non-demo accounts",
            "keep passwords off cards and out of review evidence",
            "report the blocked handover",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, planner)

        # Coder build/provision contract and failure exit.
        for clause in (
            "build the required application images from the recorded reviewed revision",
            "Build failure stops the card.",
            "Use the installed `disposable-demo` skill",
            "provision required accounts and roles through the project's authentication mechanism",
            "missing or conflicting binding stops installation",
            "No demo build verb",
            "do not substitute stale images, silently purge or hand over a partial demo",
            "put its path, never the passwords, on the card",
            "do not repeat the interview",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, coder)

        # Reviewer verifies observed state without replaying the customer route.
        for clause in (
            "compare running service image IDs, readiness, the responding loopback URL, expected data",
            "Report each failed criterion.",
            "Do not restart the playbook, rerun Cypress or replay the customer's walkthrough.",
            "Normal implementation review remains unchanged.",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, reviewer)
        # The blocked chat-credential route leaves the existing handover clause intact.
        self.assertNotIn("one row for each intended demo user", planner)


if __name__ == "__main__":
    unittest.main()
