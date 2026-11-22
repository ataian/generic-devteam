"""Static contracts for P8 build evidence, grants and managed-file authority."""
import json
from pathlib import Path
import unittest

from test_brownfield_planning import local_links

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/build-evidence"
MANIFEST = json.loads((ROOT / "manifest.json").read_text())


class BuildEvidenceTests(unittest.TestCase):
    def test_complete_role_skill_tree_and_targets(self):
        item = MANIFEST["own_skills"]["build-evidence"]
        self.assertEqual(item["targets"], {"hermes": ["coder", "reviewer"], "codex": ["team-codex"]})
        self.assertEqual(item["skill_path"], "skills/build-evidence/SKILL.md")
        self.assertNotIn("build-evidence", MANIFEST["upstream_components"])
        inventory = {path.relative_to(ROOT).as_posix()
                     for path in SKILL.rglob("*") if path.is_file()}
        self.assertEqual(inventory, {
            "skills/build-evidence/SKILL.md",
            "skills/build-evidence/references/jfr-observer.md",
            "skills/build-evidence/references/portless-testcontainers.md",
            "skills/build-evidence/references/production-build-selectors.md",
        })
        self.assertTrue(inventory.issubset(set(MANIFEST["files"])))
        local_links(SKILL)

    def test_reference_carries_mode_specific_rules(self):
        selectors = (SKILL / "references/production-build-selectors.md").read_text()
        for clause in (
            "MUI emits `data-testid` only when `process.env.NODE_ENV !== 'production'`",
            "No hit means no such anchor exists.",
            "A development-mode fixture, a component test mount or a synthetic page proves only that mode.",
            "Derive selectors from rendered DOM at the target build mode or from the component source.",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, selectors)
        containers = (SKILL / "references/portless-testcontainers.md").read_text()
        for clause in (
            "Do not bind a fixed host port, container name, volume name or network name for a test run.",
            "Read the suite's isolation checker before changing fixture counts",
            "Canary proof:",
            "Never use global prune, fixed-name removal",
            "Clean up by invocation ownership and verify absence.",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, containers)
        observer = (SKILL / "references/jfr-observer.md").read_text()
        for clause in (
            "`jdk.SocketRead`, `jdk.SocketWrite`,",
            "synthetic loopback connect to a closed port",
            "native clients that bypass JDK checks",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, observer)
        for path, text in ((SKILL / "SKILL.md", (SKILL / "SKILL.md").read_text()),
                           (SKILL / "references/production-build-selectors.md", selectors),
                           (SKILL / "references/portless-testcontainers.md", containers),
                           (SKILL / "references/jfr-observer.md", observer)):
            with self.subTest(path=path):
                for marker in ("rollout-", "t_83a3536e", "DIAGNOSE_", "codex/carter", "codex/daniel"):
                    self.assertNotIn(marker, text)

    def test_role_rules_and_grant_ownership(self):
        coder = (ROOT / "templates/roles/coder.SOUL.md.template").read_text()
        planner = (ROOT / "templates/roles/planner.SOUL.md.template").read_text()
        reviewer = (ROOT / "templates/roles/reviewer.SOUL.md.template").read_text()
        self.assertIn("Command grants come from Maker setup or update; never change your own `command_allowlist`", coder)
        self.assertIn("require the literal `$build-evidence` cue", coder)
        self.assertIn("the reference owns selector derivation and the isolation-checker limit", coder)
        self.assertIn("load `build-evidence` via `skill_view` and its reference for that mode", reviewer)
        self.assertIn("never change this profile's `command_allowlist`", planner)
        self.assertIn("never change this profile's `command_allowlist`", reviewer)
        self.assertIn("Create and release the cards through Brownfield's phase release procedure", planner)
        self.assertNotIn("Give every Coder card `--max-runtime 8h`", planner)

    def test_setup_and_update_grant_scoped_commands_and_read_back(self):
        setup = (ROOT / "references/setup.md").read_text()
        update = (ROOT / "references/update.md").read_text()
        for clause in (
            'DEV_ENTRYPOINT=\'<absolute development entrypoint from the project guide>\'',
            "\\\"$DEV_ENTRYPOINT check\\\"",
            "\\\"$DEV_ENTRYPOINT test-selected *\\\"",
            "\\\"$DEV_ENTRYPOINT test-all\\\"",
            "\\\"$DEMO_ENTRYPOINT retire *\\\"",
            "\\\"$DEMO_ENTRYPOINT user\\\"",
            "Never grant `docker compose *`, `docker *`, `docker-compose *` or an `env *` wrapper",
            "never as an argument and never in a grant",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, setup)
        self.assertIn("setup-time entrypoint list", update)
        self.assertIn("Reconcile `terminal.timeout` to `14400` on the Coder and Reviewer profiles and read it back", update)
        for text in (setup, update):
            self.assertIn("A role does not extend its own list", text)
            self.assertNotIn('"docker *"', text)
            self.assertNotIn("env * docker *", text)
        self.assertIn('hermes -p "$PROFILE" config get command_allowlist', setup)

    def test_managed_files_are_authoritative_and_adaptations_carry_path_and_version(self):
        update = (ROOT / "references/update.md").read_text()
        for clause in (
            "Managed SOUL and skill targets are authoritative",
            "reported under `adaptations` with the target path and the installed Maker version",
            "A missing managed target, or an unmanaged same-name file at a new target, remains a conflict",
            "Inspect every `adaptations` entry with its path and installed Maker version.",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, update)

    def test_release_and_recovery_guidance_is_maker_owned(self):
        release = (ROOT / "skills/brownfield-feature-planning/references/kanban-phase-release.md").read_text()
        recovery = (ROOT / "skills/brownfield-feature-planning/references/kanban-triage-recovery.md").read_text()
        for clause in (
            "Set the independent Reviewer profile explicitly on every implementation card and read it back.",
            "Subscribe on the project board:",
            "kanban --board <board> notify-subscribe <task>",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, release)
        self.assertIn("Before reopening, verify prior handoff and required continuation.", recovery)
        self.assertIn("hermes kanban --board <board> reopen-review <task>", recovery)
        self.assertIn("Do not hardcode a coder.", recovery)

    def test_demo_lifecycle_is_narrow_and_uses_project_verbs(self):
        dev = (ROOT / "skills/dev-environment/SKILL.md").read_text()
        for clause in (
            "A demonstration runtime is not permanent. At most one acceptance demo exists",
            "Retire it through the project's teardown verb.",
            "Do not compose container, volume, network or directory removal yourself",
            "If the build or start verb refuses existing runtime state, stop and report the exact refusal.",
            "Judge readiness from the project's status and version output, not from container uptime.",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, dev)


if __name__ == "__main__":
    unittest.main()
