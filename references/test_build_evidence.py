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
        self.assertEqual(item["targets"], {"hermes": ["reviewer"], "codex": ["team-codex"]})
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
        codex = (ROOT / "templates/team-codex-AGENTS.md").read_text()
        self.assertIn("use the literal `$build-evidence` cue for the affected mode", codex)
        self.assertIn("the reference owns selector derivation and the isolation-checker limit", codex)
        self.assertNotIn("$build-evidence", coder)
        self.assertNotIn("the reference owns selector derivation", coder)
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
            "\\\"$DEMO_ENTRYPOINT user\\\"",
            "Never grant an `env *` wrapper.",
            "never as an argument and never in a grant",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, setup)
        record = (ROOT / "templates/setup-record.md").read_text()
        for text in (setup, record, update):
            self.assertIn("confirmed_bindings.command_allowlists", text)
        legacy = next(row for row in update.splitlines() if row.startswith("   | Pre-`2.14.0` command grants"))
        self.assertIn("[setup grant recipe](setup.md#project-command-grants)", legacy)
        self.assertIn("four Docker entries", legacy)
        self.assertIn("keep it unresolved for the operator", legacy)
        self.assertIn("do not narrow the wildcard grants to specific verbs", legacy)
        self.assertIn("### Project command grants", setup)
        self.assertIn("Reconcile the profile settings", update)
        for text in (setup, update):
            self.assertIn("A role does not extend its own list", text)
            self.assertNotIn("docker volume ls", text)
            self.assertNotIn("env * docker *", text)
        self.assertIn("Treat a baseline missing any required Docker entry as obsolete", update)
        self.assertIn('hermes -p "$PROFILE" config get command_allowlist', setup)

    def test_docker_grants_decode_to_both_clis_and_all_subcommands(self):
        """Decode the setup grant example; this evaluates the list, never a Docker command."""
        setup = (ROOT / "references/setup.md").read_text()
        grant = next(line for line in setup.splitlines() if "config set command_allowlist" in line)
        encoded = grant.split('config set command_allowlist "', 1)[1].rsplit('"', 1)[0]
        entries = json.loads(encoded.replace('\\"', '"'))
        self.assertIn("$DEV_ENTRYPOINT check", entries)
        self.assertIn("$DEMO_ENTRYPOINT user", entries)
        for entry in ("docker", "docker *", "docker-compose", "docker-compose *"):
            with self.subTest(entry=entry):
                self.assertIn(entry, entries)
        self.assertEqual([e for e in entries if e.startswith("docker")],
                         ["docker", "docker *", "docker-compose", "docker-compose *"])
        self.assertNotIn("env *", entries)
        for clause in (
            "Independently grant `docker`, `docker *` (including `docker compose *`), `docker-compose` "
            "and `docker-compose *` in all three profiles.",
            "Keep the Docker grants regardless of project scripts or demo choice.",
            "They are not project-scoped and can affect other workloads; existing deny rules remain binding.",
        ):
            self.assertIn(clause, setup)
        record = (ROOT / "templates/setup-record.md").read_text()
        self.assertIn("all operations on any daemon accessible to the CLI", record)
        self.assertIn("including an alternate context or remote daemon", record)
        self.assertIn("existing deny rules", record)

    def test_requested_demo_reference_owns_retirement_and_the_coder_refuses_state(self):
        reference = (ROOT / "skills/dev-environment/references/requested-demo.md").read_text()
        for clause in (
            "Inspect the project’s demo state, including stopped remnants.",
            "Verified absence completes this step; an inspection failure does not.",
            "Before removal, verify exclusive ownership of the old demo’s containers, volumes, network and private runtime directory.",
            "A stopped runtime is not retired.",
            "stop before committing the plan or writing any ticket",
            "Do not apply and revert a planned product fix to bypass this prerequisite.",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, reference)
        handover = (ROOT / "skills/demo-handover/SKILL.md").read_text()
        self.assertIn("If build or start refuses existing state, stop and report the refusal; "
                      "do not purge, rename or bypass it.", handover)
        self.assertNotIn("teardown verb", handover)
        self.assertNotIn("A demonstration runtime is not permanent", handover)
        self.assertIn("At most one demonstration runtime exists; use the last independently reviewed commit.",
                      handover)
        planner = (ROOT / "templates/roles/planner.SOUL.md.template").read_text()
        self.assertNotIn("retire a running demonstration runtime", planner)
        self.assertNotIn("teardown verb", planner)
        self.assertIn("Without an explicit demo request, proceed to step 6 without demo work.", planner)
        no_branch = planner.split("Without an explicit demo request,", 1)[1].split("If requested,", 1)[0]
        self.assertNotIn("record", no_branch)
        self.assertNotIn("readback", no_branch)
        dev = (ROOT / "skills/dev-environment/SKILL.md").read_text()
        self.assertNotIn("## Demonstration lifecycle", dev)
        self.assertIn("- A requested demo handover has its own card; it is not a development-environment acceptance case.", dev)
        release = (ROOT / "skills/brownfield-feature-planning/references/kanban-phase-release.md").read_text()
        self.assertNotIn("repairs the demo teardown command", release)
        self.assertNotIn("demo", release.lower())

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
        inspection = (ROOT / "skills/brownfield-feature-planning/references/kanban-status-inspection.md").read_text()
        for clause in (
            "Subscribe on the project board:",
            "kanban --board <board> notify-subscribe <task>",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, release)
        self.assertIn("On handoff, verify reviewer assignment and implementer `review_requested` provenance.", inspection)
        self.assertIn("Before reopening, verify prior handoff and required continuation.", recovery)
        self.assertIn("hermes kanban --board <board> reopen-review <task>", recovery)
        self.assertIn("Do not hardcode a coder.", recovery)


if __name__ == "__main__":
    unittest.main()
