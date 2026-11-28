"""Static contracts for P8 build evidence, grants and managed-file authority."""
import json
import os
from pathlib import Path
import shlex
import subprocess
import tempfile
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
            "DEMO_ENTRYPOINT='<canonical absolute demonstration entrypoint from the installed demo guide>'",
            "DEV_ENTRYPOINT='<canonical absolute development entrypoint from the installed dev guide>'",
            '"$(entry "$DEV_ENTRYPOINT" check)"',
            '"$(entry "$DEV_ENTRYPOINT" build)"',
            '"$(entry "$DEMO_ENTRYPOINT" start)"',
            '"$(entry "$DEMO_ENTRYPOINT" user)"',
            "Never grant an `env *` wrapper.",
            "A demonstration launcher takes one verb and no operand.",
            "Never translate a test selector into a wildcard",
            "Include `stop` and `purge` only for a profile the operator authorized",
            '"$(entry "$DEV_ENTRYPOINT" test-selected TherapyServiceTest)"',
            '"$(entry "$DEV_ENTRYPOINT" start)"',
            '"$(entry "$DEV_ENTRYPOINT" update)"',
            "Never a selector wildcard.",
            "`purge` is never a fallback for `retire`.",
            "Merge into the approved list without dropping unrelated entries.",
            "never as an argument and never in a grant",
            "Read each profile's current list with `config get command_allowlist --json`",
            "append only missing approved entries",
            "never set a replacement list",
            "Preserve every existing unrelated entry and every existing independently approved Docker entry.",
            'Add `$(entry "$DEMO_ENTRYPOINT" user)` only when `demo.json` declares a `keycloak_service`.',
            "An entry containing `*`, `?` or `[` is matched as a glob even inside quotes",
            "a launcher entry must be exact and free of those characters",
            "Reuse a line the guide already renders.",
            "never by concatenating an unquoted path with a verb",
            "Keep them separate from the launcher entries above",
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
        self.assertIn("add no wildcard selector", legacy)
        self.assertIn("Do not carry over a retired launcher entry", legacy)
        self.assertIn("### Project command grants", setup)
        self.assertIn("Reconcile the profile settings", update)
        for text in (setup, update):
            self.assertIn("A role does not extend its own list", text)
            self.assertNotIn("docker volume ls", text)
            self.assertNotIn("env * docker *", text)
        self.assertIn("Treat a baseline missing any required Docker entry as obsolete", update)
        self.assertIn('hermes -p "$profile" config get command_allowlist --json', setup)
        self.assertIn("a profile grant is not proof of Team-Codex runtime access", setup)

    def test_existing_team_adoption_reconciles_only_verified_launcher_grants(self):
        """Policy contract: a verified 3.1.1 baseline is not current at 4.0.0 adoption."""
        update = (ROOT / "references/update.md").read_text()
        self.assertIn(
            "Treat it as obsolete as well when a `4.0.0` [environment skill adoption]"
            "(#environment-skill-adoption-400) is proposed or pending", update)
        self.assertIn(
            "even though that verified prior baseline already contains all four Docker entries",
            update)
        rows = [row for row in update.splitlines()
                if row.startswith("   | `4.0.0` pinned-environment adoption")]
        self.assertEqual(len(rows), 1, "adoption grant trigger must be one table row")
        row = rows[0]
        for clause in (
            "including a pending resume",
            "even though the baseline already contains all four Docker entries",
            "git show BASELINE:references/setup.md",
            "exact installed demo and dev guides",
            "remove only an obsolete Maker-managed launcher entry outside that set",
            "Keep every unrelated, local and existing Docker entry",
            "this row changes launcher entries only",
            "Add no wildcard to either launcher",
            "exact additions and removals in the update approval",
            "same native `config set command_allowlist` write",
            "compare the whole readback with the approved result",
            "keep the entry and the adoption `pending`",
            "Save the new list under `confirmed_bindings.command_allowlists` "
            "only after the readback matches",
            "file-helper rollback does not restore grants",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, row)
        # The adoption reuses the general gate, delta and readback rule, not a parallel procedure.
        self.assertIn(
            "Report the exact additions, removals and unrelated local grants before approval",
            update)
        self.assertIn("Save a new baseline only after native readback matches the approved result", update)
        self.assertNotIn("test-selected *", row)
        self.assertLess(row.index("exact additions and removals in the update approval"),
                        row.index("same native `config set command_allowlist` write"))
        self.assertLess(row.index("same native `config set command_allowlist` write"),
                        row.index("Save the new list under `confirmed_bindings.command_allowlists`"))
        adoption = update.split("### Environment skill adoption (4.0.0)", 1)[1].split("\n### ", 1)[0]
        self.assertIn("including its [role grant reconciliation](#prepare-and-review-one-team)",
                      adoption)
        self.assertIn("the role grant reconciliation above", adoption)
        self.assertIn("including a pending role grant reconciliation", adoption)

    def grant_section(self):
        setup = (ROOT / "references/setup.md").read_text()
        return setup.split("### Project command grants", 1)[1].split(
            "### Planner Kanban tools", 1)[0]

    def grant_block(self):
        return self.grant_section().split("```sh\n", 1)[1].split("\n```", 1)[0]

    def run_grant_block(self, block, dev, demo, seed=None, extra="", env_extra=None,
                        expect_failure=False):
        """Run the documented merge procedure against a fake native CLI."""
        stub = '''#!/usr/bin/env python3
import json, os, sys
args = sys.argv[1:]
profile = None
if args[:1] == ["-p"]:
    profile = args[1]
    args = args[2:]
if len(args) >= 3 and args[0] == "config":
    action, key = args[1], args[2]
    state = os.path.join(os.environ["GRANT_STATE"], str(profile) + ".json")
    if action == "get" and key == "command_allowlist" and args[3:] == ["--json"]:
        data = open(state).read() if os.path.exists(state) else "[]"
        if os.environ.get("GRANT_TRUNCATE_READBACK") and os.path.exists(state + ".set"):
            data = json.dumps(json.loads(data)[:-1])
        print(data)
        sys.exit(0)
    if action == "set" and key == "command_allowlist" and len(args) == 4:
        with open(state, "w") as stream:
            stream.write(args[3])
        open(state + ".set", "w").close()
        sys.exit(0)
sys.exit(2)
'''
        with tempfile.TemporaryDirectory(prefix="maker-grants-") as raw:
            root = Path(raw)
            bin_dir = root / "bin"
            state_dir = root / "state"
            bin_dir.mkdir()
            state_dir.mkdir()
            hermes = bin_dir / "hermes"
            hermes.write_text(stub)
            hermes.chmod(0o755)
            for profile, entries in (seed or {}).items():
                (state_dir / f"{profile}.json").write_text(json.dumps(entries))
            lines = []
            for line in block.splitlines():
                if line.startswith("DEV_ENTRYPOINT="):
                    line = "DEV_ENTRYPOINT=" + (shlex.quote(dev) if dev else "''")
                elif line.startswith("DEMO_ENTRYPOINT="):
                    line = "DEMO_ENTRYPOINT=" + (shlex.quote(demo) if demo else "''")
                lines.append(line)
            script = root / "grants.sh"
            script.write_text("\n".join(lines) + "\n" + extra)
            environment = os.environ.copy()
            environment["PATH"] = f"{bin_dir}:{environment['PATH']}"
            environment["GRANT_STATE"] = str(state_dir)
            environment["PLANNER_PROFILE"] = "planner"
            environment["CODER_PROFILE"] = "coder"
            environment["REVIEWER_PROFILE"] = "reviewer"
            environment.update(env_extra or {})
            result = subprocess.run(["bash", "-eu", str(script)], env=environment,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.last_grant_returncode = result.returncode
            self.last_grant_stderr = result.stderr.decode() + result.stdout.decode()
            if expect_failure:
                self.assertNotEqual(result.returncode, 0, result.stdout.decode())
            else:
                self.assertEqual(result.returncode, 0, result.stderr.decode())
            return {profile: json.loads((state_dir / f"{profile}.json").read_text())
                    for profile in ("planner", "coder", "reviewer")
                    if (state_dir / f"{profile}.json").exists()}

    def test_project_grant_merge_is_exact_and_preserves_existing_entries(self):
        block = self.grant_block()
        dev = '/opt/dev env/bin/"dev" \\ tool $X'
        demo = "/opt/demo app/bin/demo"
        existing = {
            "coder": ["unrelated-tool run", "docker", "docker *", "docker-compose"],
            "reviewer": ["docker", "docker *", "docker-compose", "docker-compose *", "keep-me"],
        }
        lists = self.run_grant_block(block, dev, demo, existing)
        docker = ["docker", "docker *", "docker-compose", "docker-compose *"]
        demo_commands = [shlex.join([demo, verb]) for verb in ("start", "status", "retire")]
        self.assertEqual(lists["planner"], docker + [f"{shlex.quote(demo)} status",
                                                     f"{shlex.quote(demo)} retire"])
        self.assertEqual(lists["coder"], existing["coder"] + [
            "docker-compose *",
            f"{shlex.quote(demo)} start", f"{shlex.quote(demo)} status",
            shlex.join([dev, "help"]), shlex.join([dev, "build"]),
            shlex.join([dev, "check"]), shlex.join([dev, "test"])])
        self.assertEqual(lists["reviewer"], existing["reviewer"] + [
            f"{shlex.quote(demo)} status", shlex.join([dev, "check"])])
        for role, entries in lists.items():
            with self.subTest(role=role):
                self.assertEqual(len(entries), len(set(entries)))
                self.assertNotIn(f"{shlex.quote(demo)} user", entries)
                self.assertNotIn(f"{demo} status", entries)
        for command in demo_commands:
            with self.subTest(command=command):
                self.assertEqual(shlex.split(command), [demo, command.rsplit(" ", 1)[1]])
        for retired in ("test-all", "test-selected *", "build *", "start *", "retire *",
                        "retire [SHA]", "&&"):
            with self.subTest(retired=retired):
                self.assertNotIn(retired, block)
        setup = (ROOT / "references/setup.md").read_text()
        self.assertNotIn('config set command_allowlist "[\\\"', setup)

    def test_project_grant_entries_match_the_exact_rendered_invocation(self):
        """A path with spaces is quoted once, exactly as the guide renders it.

        Selector fixture: /home/mariko/projects/mtb/de.uke.iam.mtb/docker/dev/AGENTS.md:40-41
        renders `dev.sh test-selected TherapyServiceTest` and the quoted `Class#method` form.
        """
        block = self.grant_block()
        dev = "/fixture/space project/dev/dev.sh"
        demo = "/fixture/space project/demo/demo.sh"
        selector = "TherapyServiceTest#addTherapyNormalizesChildReferenceToRoot"
        exact = shlex.join([dev, "test-selected", selector])
        self.assertEqual(exact, f"'{dev}' test-selected '{selector}'")
        extra = f'merge_grants "$CODER_PROFILE" "$(entry "$DEV_ENTRYPOINT" test-selected {shlex.quote(selector)})"\n'
        lists = self.run_grant_block(block, dev, demo, extra=extra)
        self.assertIn(f"'{dev}' build", lists["coder"])
        self.assertIn(f"'{demo}' start", lists["coder"])
        self.assertEqual(lists["coder"][-1], exact)
        self.assertIn("test-selected 'TherapyServiceTest#addTherapyNormalizesChildReferenceToRoot'",
                      lists["coder"][-1])
        for role, entries in lists.items():
            with self.subTest(role=role):
                for command in entries:
                    if command.startswith("docker"):
                        continue
                    self.assertFalse(any(char in command for char in "*?["), command)

    def test_project_grant_merge_rejects_glob_launcher_entries(self):
        block = self.grant_block()
        dev = "/opt/dev/bin/dev"
        demo = "/opt/demo/bin/demo"
        seed = {"planner": [], "coder": [], "reviewer": []}
        baseline = self.run_grant_block(block, dev, demo, seed)
        for selector in ("*", "Class?", "Class[AB]"):
            with self.subTest(selector=selector):
                extra = (f'merge_grants "$CODER_PROFILE" '
                         f'"$(entry "$DEV_ENTRYPOINT" test-selected {shlex.quote(selector)})"\n')
                lists = self.run_grant_block(block, dev, demo, seed, extra=extra,
                                             expect_failure=True)
                self.assertNotEqual(self.last_grant_returncode, 0)
                self.assertIn("glob metacharacter", self.last_grant_stderr)
                self.assertEqual(lists["coder"], baseline["coder"])

    def test_project_grant_blocks_are_independent_of_docker_and_uninstalled_environments(self):
        block = self.grant_block()
        dev = "/opt/dev/bin/dev"
        demo = "/opt/demo/bin/demo"
        docker = ["docker", "docker *", "docker-compose", "docker-compose *"]
        absent = self.run_grant_block(block, "", "")
        for role in ("planner", "coder", "reviewer"):
            with self.subTest(role=role, state="absent"):
                self.assertEqual(absent[role], docker)
        demo_only = self.run_grant_block(block, "", demo)
        self.assertEqual(demo_only["planner"][-1], f"{shlex.quote(demo)} retire")
        self.assertFalse(any("dev.sh" in entry for entry in demo_only["coder"]))
        dev_only = self.run_grant_block(block, dev, "")
        self.assertFalse(any("demo" in entry for entries in dev_only.values()
                             for entry in entries))
        self.assertEqual(dev_only["reviewer"][-1], shlex.join([dev, "check"]))

    def test_project_grant_readback_is_compared_with_the_prior_merged_list(self):
        block = self.grant_block()
        dev = "/opt/dev env/bin/dev"
        demo = "/opt/demo app/bin/demo"
        seed = {"planner": ["keep-me"]}
        lists = self.run_grant_block(block, dev, demo, seed)
        self.assertEqual(lists["planner"][0], "keep-me")
        self.assertIn(f"{shlex.quote(demo)} status", lists["planner"])
        self.run_grant_block(block, dev, demo, seed, expect_failure=True,
                             env_extra={"GRANT_TRUNCATE_READBACK": "1"})

    def test_conditional_grant_entries_are_opt_in_and_added_once(self):
        block = self.grant_block()
        dev = "/opt/dev/bin/dev"
        demo = "/opt/demo/bin/demo"
        line = 'merge_grants "$CODER_PROFILE" "$(entry "$DEMO_ENTRYPOINT" user)"\n'
        lists = self.run_grant_block(block, dev, demo, extra=line * 2)
        self.assertNotIn(f"{shlex.quote(demo)} user", self.run_grant_block(block, dev, demo)["coder"])
        self.assertEqual(lists["coder"].count(f"{shlex.quote(demo)} user"), 1)
        self.assertEqual(lists["coder"][-1], f"{shlex.quote(demo)} user")
        self.assertIn(line.strip(), self.grant_section())

    def test_grants_keep_the_docker_paragraph_and_matching_rules(self):
        setup = (ROOT / "references/setup.md").read_text()
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

    def test_new_setup_records_one_project_password_choice_without_a_role_secret(self):
        setup = (ROOT / "references/setup.md").read_text()
        for clause in (
            "### Project demo password choice",
            "Ask once during every new team creation, also when demo installation is deferred",
            "Skipping selects the disposable-demo default",
            "Store explicit choices only at `<project>/demo/settings.json`",
            '`{"mode":"shared","value":"…"}`',
            '`{"mode":"random"}`',
            "references/setup_settings.py",
            "mode 0600",
            "excluded from Git",
            "preserves unrelated keys and an existing `password` choice",
            "Never pass the value as an argument, print it, echo it, or write it to a ticket, memory, "
            "Hindsight or profile configuration.",
            "Skipping with no prior setting writes no file",
            "Disclose the exact project writes before the existing setup/update approval",
            "A settings-only `demo/` is neither an installed nor a running demo.",
            "Record the choice mode, completion and location",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, setup)
        grant_paragraph = setup.split("Omit project entries whose entrypoint", 1)[1].split("\n", 1)[0]
        self.assertIn("<project>/demo/settings.json", grant_paragraph)
        self.assertIn("mode `0600`", grant_paragraph)
        self.assertIn("excluded from Git", grant_paragraph)
        self.assertIn("never as an argument and never in a grant", grant_paragraph)
        self.assertNotIn("documented environment variable", grant_paragraph)

        for role, template in MANIFEST["role_templates"].items():
            with self.subTest(role=role):
                self.assertNotIn("DEMO_PASSWORD", template["render_fields"])
                text = (ROOT / template["template_path"]).read_text()
                self.assertNotIn("DEMO_PASSWORD", text)
                self.assertNotIn("{{DEMO_PASSWORD}}", text)
        for relative in ("templates/setup-record.md", "references/native-workflow.md"):
            text = (ROOT / relative).read_text()
            self.assertNotIn("{{DEMO_PASSWORD}}", text)
        record = (ROOT / "templates/setup-record.md").read_text()
        self.assertNotIn("the demonstration password", record)
        self.assertIn("A new record has no demo password value", record)
        self.assertIn("until its 4.0.0 adoption removes it", record)
        workflow = (ROOT / "references/native-workflow.md").read_text()
        self.assertNotIn("| `DEMO_PASSWORD` |", workflow)
        self.assertNotIn("`DEMO_PASSWORD` raw", workflow)
        self.assertIn("A new record has no `DEMO_PASSWORD`", setup)

    def test_environment_adoption_retires_the_setup_value_and_keeps_roles_inactive(self):
        """Static ordering/contract for the 4.0.0 adoption; no helper or team run."""
        update = (ROOT / "references/update.md").read_text()
        setup = (ROOT / "references/setup.md").read_text()
        adoption = update.split("### Environment skill adoption (4.0.0)", 1)[1].split("\n### ", 1)[0]

        order = adoption.split("- **Order:**", 1)[1].split("\n- **", 1)[0]
        markers = (
            "Apply the approved file proposal first",
            "setup-record retirement",
            "Ask the fresh demo setting once",
            "retire the exact old `demo-handover` tree",
            "before installing the same-name pinned",
        )
        positions = [order.index(marker) for marker in markers]
        self.assertEqual(positions, sorted(positions))

        for clause in (
            "Retire the recorded value (once per team)",
            "remove only the `DEMO_PASSWORD` key from `confirmed_values` and, if present, "
            "from `confirmed_bindings`",
            "leave every other key, value, type and order, all surrounding prose, and the file's "
            "mode and ownership unchanged",
            "Never print, echo or otherwise output the removed value",
            "The file helper does not perform this step: its field drop changes only the "
            "installation proposal and `installation.json`.",
            "An absent key is a successful no-op",
            "Setup §6's preserve-existing-keys rule",
            "ordinary setup must preserve the current record and must not reintroduce a key this "
            "4.0.0 adoption removed",
            "no other step retires `DEMO_PASSWORD` from the setup record",
            "keep every affected Hermes role and Team-Codex context inactive",
            "until file application, setup-record retirement, the fresh question, old-target "
            "retirement and pinned installation verify, or their rollback completes",
            "An interruption keeps the window open",
            "do not record inactivity you cannot observe",
            "For the 4.0.0 environment adoption's same-name switch",
        ):
            with self.subTest(clause=clause):
                self.assertIn(clause, update)
        self.assertNotIn(
            "Remove `DEMO_PASSWORD` from active setup values and installation bindings", update)

        self.assertIn("Preserve all existing keys/types", setup)
        self.assertIn("a historical `DEMO_PASSWORD` from an existing record", setup)

    def test_demo_handover_build_and_reviewer_contract_without_owned_references(self):
        """Static role contracts; no Docker, demo or agent run."""
        planner = (ROOT / "templates/roles/planner.SOUL.md.template").read_text()
        coder = (ROOT / "templates/roles/coder.SOUL.md.template").read_text()
        reviewer = (ROOT / "templates/roles/reviewer.SOUL.md.template").read_text()
        for text in (planner, coder, reviewer):
            self.assertNotIn("requested-demo", text)
            self.assertNotIn("demo-handover", text)
        self.assertIn("Retire the previous demo on both answers without another permission request.", planner)
        self.assertIn("Unknown ownership or an unreachable engine: stop and report", planner)
        self.assertIn("No plus verified absence", planner)
        self.assertIn("Never write demo credentials on a card.", planner)
        self.assertNotIn("teardown verb", planner)
        self.assertIn("build the required application images from the recorded reviewed revision", coder)
        self.assertIn("Build failure stops the card.", coder)
        self.assertIn("No demo build verb", coder)
        self.assertIn("do not substitute stale images, silently purge or hand over a partial demo", coder)
        self.assertIn("put its path, never the passwords, on the card", coder)
        self.assertIn("do not repeat the interview", coder)
        self.assertIn("compare running service image IDs, readiness, the responding loopback URL", reviewer)
        self.assertIn("Do not restart the playbook, rerun Cypress or replay the customer's walkthrough.", reviewer)
        release = (ROOT / "skills/brownfield-feature-planning/references/kanban-phase-release.md").read_text()
        self.assertNotIn("repairs the demo teardown command", release)

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
