"""Offline regression checks; run: python3 -B references/test_render_reasoning.py."""
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from render_text import render_role, role_fields

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text())
REASONING_FIELDS = {
    "planner": set(),
    "coder": {"CODEX_REASONING_DEFAULT", "CODEX_REASONING_MAX"},
    "reviewer": {"ROLE_REASONING_DEFAULT", "ROLE_REASONING_HIGH"},
}


class TasPortabilityTests(unittest.TestCase):
    def read_standard(self, root):
        instructions = (root / "AGENTS.md").read_text()
        link = re.search(r"Read \[TAS authoring standard\]\(([^)]+)\)", instructions)
        if link is None:
            self.fail("The required standard needs a relative Markdown link")
        relative = Path(link[1])
        self.assertFalse(relative.is_absolute())
        target = (root / relative).resolve()
        self.assertTrue(target.is_relative_to(root.resolve()))
        return target.read_text()

    def test_required_standard_resolves_inside_maker(self):
        self.assertTrue(self.read_standard(ROOT).strip())

    def test_manifest_export_contains_instructions_and_standard_without_vault(self):
        with tempfile.TemporaryDirectory(prefix="maker-tas-") as directory:
            export = Path(directory)
            for relative in MANIFEST["files"] + ["manifest.json"]:
                source = ROOT / relative
                target = export / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            self.assertTrue((export / "AGENTS.md").is_file(), "Ship the package authoring instructions")
            standard = self.read_standard(export)
            self.assertNotIn("/home/", standard)
            self.assertNotIn("obsidian_vault", standard)
            self.assertNotIn("[[", standard)
            self.assertTrue(standard.strip())


class ReasoningContractTests(unittest.TestCase):
    def template(self, role):
        return (ROOT / MANIFEST["role_templates"][role]["template_path"]).read_text()

    def values(self, role, default="medium", maximum="high"):
        values = {key: "Example" for key in role_fields(self.template(role), role)}
        for key in values:
            if key.endswith("_PROFILE"):
                values[key] = "example-role"
            elif key == "PROJECT_DIR":
                values[key] = "/work/project"
            elif key == "REPOSITORY_ROOTS":
                values[key] = "Planning: /work/plans; implementation: /work/project/code"
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
            "Supply the reasoning level selected for this task under the existing matrix",
            "Default-level example with a quoted TOML string:",
            "For a higher selected level, pass that selected value instead.",
            'model_reasoning_effort=\'"low"\'',
        ]:
            self.assertTrue(text in result, text)
        self.assertNotIn("if the worker guard prohibits them", result)
        self.assertNotIn("{{", result)

    def test_reviewer_renders_risk_escalation_and_separate_critical_pass(self):
        """Static rendered instruction contract, not measured agent behavior."""
        result = render_role(self.template("reviewer"), self.values("reviewer", "low", "medium"), "reviewer")
        for text in [
            "Use the configured default reasoning `low` for normal changes.",
            "You can upgrade to `medium` at any time.",
            "If HIGH risk is known before review, start at `medium`.",
            "If you discover a serious risk during normal review, recheck affected areas and prior conclusions at `medium` before the verdict.",
            "Keep the configured model and provider unchanged.",
            "If the change affects material security, data-integrity, transaction, or concurrency invariants, obtain a separate pass before the verdict even when the main review finds no defect.",
            "Use a fresh context at `medium` through an existing permitted review path.",
            "Omit the Coder's narrative and the main review's findings until this pass forms its own assessment.",
            "Apply the same model/provider, reasoning, access, approval, and read-only limits to this pass.",
            "Verify new findings and resolve contradictions before the verdict.",
            "Repeat the independent pass for affected material security, data-integrity, transaction, or concurrency invariants when its previous evidence is no longer valid.",
            "Reuse its evidence only while the checked inputs and relevant dependencies, configuration, and test conditions remain valid.",
            "A new commit alone does not invalidate every prior result.",
            "Do not add another full review or duplicate a test suite solely because a task is HIGH risk.",
            "If required high-reasoning verification or a permitted fresh context is unavailable, report the capability blocker.",
            "For high-risk verdicts report:",
            "separate-pass coverage or valid reused evidence",
            "Do not manufacture extra rounds or postpone baseline duties for a round's emphasis.",
            "The separate pass is not another correction round.",
            "Perform the checks that this change requires before you deliver the verdict.",
        ]:
            self.assertIn(text, result)
        self.assertNotIn("{{", result)
        self.assertNotIn("Reasoning Stufe", result)

    def test_reviewer_uses_original_sdlc_sequencing_without_claiming_blindness(self):
        """Static SOUL contract; upstream's read-order tension is not repaired here."""
        result = render_role(self.template("reviewer"), self.values("reviewer"), "reviewer")
        for text in [
            "Use the installed original `sdlc-review` for review entry, sequencing, per-round lenses, baseline duties, and native outcomes.",
            "Keep its automatic dispatcher integration unchanged.",
            "Apply all baseline duties before every verdict, including acceptance evidence, relevant checks, and all prior requested changes.",
            "Treat the narrative as a claim, not evidence.",
            "Do not describe a read as blind if its context already contains the Coder's explanation or prior findings.",
            "Resolve a conflict with the approved model or reasoning settings before relying on the affected verification.",
            "Preserve confirmed local overrides; do not change model or provider to repair a stale instruction.",
        ]:
            self.assertIn(text, result)
        self.assertNotIn("Read the task and latest handoff through", result)
        self.assertNotIn("as review lenses", result)
        for key in ('"review_outcome":"approved"', '"reviewer_checks":["<actual-check>"]',
                    '"reviewed_commit":"<exact-commit>"'):
            self.assertIn(key, result)
        self.assertIn("`kanban_comment`, then call `kanban_request_changes", result)
        self.assertIn('kanban_block(kind="capability"', result)

    def test_reviewer_avoids_failed_retries_and_redundant_evidence_work(self):
        """Static contract retains verification while removing proven waste paths."""
        result = render_role(self.template("reviewer"), self.values("reviewer"), "reviewer")
        for text in [
            "Inspect existing validation commands for included test and build phases before selecting checks.",
            "Read existing result artifacts instead of rerunning a successful check only to obtain a clearer summary.",
            "Check existing runtime paths, inputs, and permitted access before starting a custom probe or review helper.",
            "After a deterministic argument or permission error, correct the call or use an existing permitted path before retrying.",
            "Do not repeat an unchanged failed call or bypass a native guard.",
            "Read complete large task records and logs locally; return only decision-relevant fields and necessary evidence to context.",
            "Preserve requirements, prior decisions, open findings, errors, and warnings.",
            "Run checks affected by changes or insufficient evidence; retain required independent checks and explicit final-state acceptance tests.",
        ]:
            self.assertIn(text, result)

    def test_card_output_contract_reaches_each_rendered_role(self):
        """Persistent card text stays concise without unsafe truncation."""
        for role in ("planner", "coder", "reviewer"):
            text = render_role(self.template(role), self.values(role), role)
            with self.subTest(role=role):
                self.assertIn("Apply these rules to card descriptions, comments, and handoffs.", text)
                self.assertIn("Preserve requirements, conditions, open findings, and necessary evidence without a fixed character limit.", text)
                self.assertIn("Reference an existing entry only if the recipient can retrieve it unambiguously.", text)
        coder = self.template("coder")
        self.assertIn("Persisted Kanban text uses short complete sentences, not chat fragments.", coder)
        self.assertIn("$caveman", coder)
        self.assertIn("Never use `kanban_complete` to close your own implementation.", coder)
        self.assertIn("Report your decision and next action without retelling the Coder or Reviewer report.", self.template("planner"))
        self.assertIn("Describe each finding fully once.", self.template("reviewer"))

    def test_correction_contract_preserves_evidence_and_independent_verdict(self):
        for role in ("coder", "reviewer"):
            text = render_role(self.template(role), self.values(role), role)
            with self.subTest(role=role):
                self.assertIn("Reuse evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid.", text)
                self.assertIn("Keep the original executor and checked state; distinguish reused evidence from newly executed checks.", text)
                self.assertIn("Run checks affected by changes or insufficient evidence; retain required independent checks and explicit final-state acceptance tests.", text)
        self.assertIn("On resume, reconcile the current assignment, working tree, and blockers; continue unfinished work instead of repeating completed preparation.", self.template("coder"))
        reviewer = self.template("reviewer")
        self.assertIn("On a correction return, compare against the previously reviewed state and assess the delta, affected dependencies, and prior open findings independently.", reviewer)
        self.assertIn("Deliver a verdict against the exact reviewed commit", reviewer)

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
        values = self.values("coder")
        values["PLANNER_PROFILE"] = "confirmed-planner"
        text = render_role(self.template("coder"), values, "coder")
        self.assertIn("Route the same task to `confirmed-planner` through native `kanban_request_review`.", text)
        self.assertIn("Send one TIMER request to `confirmed-planner` through `kanban_create`.", text)
        self.assertIn("Check `confirmed-planner` against the native profile registration before routing a task or TIMER request.", text)
        self.assertNotIn("setup record", text)
        self.assertIn("Resume after `kanban_request_changes` and reread the baseline.", text)
        missing = dict(values)
        del missing["PLANNER_PROFILE"]
        with self.assertRaises(ValueError):
            render_role(self.template("coder"), missing, "coder")
        for bad in ("Display Name", "other/profile", "wrong\nprofile"):
            with self.subTest(profile=bad), self.assertRaises(ValueError):
                render_role(self.template("coder"), dict(values, PLANNER_PROFILE=bad), "coder")
        self.assertNotIn("Budgetfragen", text)
        self.assertNotIn("Budgetfreigaben", text)

    def test_planner_renders_confirmed_workspace_and_separate_repository_roots(self):
        values = self.values("planner")
        values.update(PROJECT_DIR="/work/client's project",
                      REPOSITORY_ROOTS="Planning: /work/plans; implementation: /work/client's project/backend, /work/frontend")
        text = render_role(self.template("planner"), values, "planner")
        self.assertIn("`/work/client's project`", text)
        self.assertIn("`Planning: /work/plans; implementation: /work/client's project/backend, /work/frontend`", text)
        self.assertNotIn("setup record", text)
        self.assertIn("actual Git root", text)
        self.assertIn("`terminal.cwd`, board, and ticket bindings", text)
        for field in ("PROJECT_DIR", "REPOSITORY_ROOTS"):
            missing = dict(values)
            del missing[field]
            with self.subTest(field=field), self.assertRaises(ValueError):
                render_role(self.template("planner"), missing, "planner")
        for bad in ("relative/path", "~/work", "/work/../other", "/work//code", "/work/."):
            with self.subTest(path=bad), self.assertRaises(ValueError):
                render_role(self.template("planner"), dict(values, PROJECT_DIR=bad), "planner")

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

    def test_planner_renders_platform_repair_authorization_boundary(self):
        """Static rendered instruction contract, not a live agent-behavior test."""
        text = render_role(self.template("planner"), self.values("planner"), "planner")
        scope = text.split("## Evidence and scope\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn(
            "Treat repairs to the agent platform or shared toolchain as separate scope "
            "unless the customer explicitly included them in the approved assignment.", scope)
        self.assertIn(
            "Obtain that authorization before planning repair work, creating repair tasks, "
            "or delegating repairs.", scope)
        self.assertIn(
            "You can resolve minor, locally correctable implementation details", text)
        self.assertIn(
            "Use only an authorized native one-time resume mechanism.", text)

    def test_planner_renders_safe_continuation_without_optional_platform_gate(self):
        """Static rendered instruction contract, not a live agent-behavior test."""
        text = render_role(self.template("planner"), self.values("planner"), "planner")
        scope = text.split("## Evidence and scope\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn(
            "If an existing authorized procedure permits safe project continuation, "
            "do not make an optional platform improvement an additional prerequisite.", scope)
        self.assertIn("Never waive required safety or verification gates to save cost.", scope)
        self.assertIn("Start successors only after independent review reaches `done`.", text)

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


class ReviewerEquipmentTests(unittest.TestCase):
    """Static package contracts; no target integration or model calls."""

    template = ReasoningContractTests.template
    values = ReasoningContractTests.values

    def test_default_equipment_retains_other_roles_and_sdlc(self):
        expected = {
            "brownfield-feature-planning": {"hermes": ["planner"]},
            "minimal-change-engineering": {"hermes": ["planner"]},
            "plan-versioning-semver": {"hermes": ["planner"]},
            "project-lib-versioning": {"hermes": ["planner", "coder"]},
            "screenshot-to-code": {"hermes": ["planner", "coder"], "codex": ["team-codex"]},
        }
        self.assertEqual({name: item["targets"] for name, item in MANIFEST["own_skills"].items()}, expected)
        upstream = MANIFEST["upstream_components"]
        for name in ("graphify", "codebase-memory"):
            self.assertEqual(upstream[name]["targets"], {
                "hermes": ["planner", "coder"], "codex": ["team-codex"],
            })
        self.assertEqual(upstream["sdlc-review"]["targets"], {"hermes": ["reviewer"]})
        self.assertEqual(upstream["sdlc-review"]["subpaths"], ["skills/devops/sdlc-review"])
        for name, item in MANIFEST["own_skills"].items():
            self.assertTrue((ROOT / item["skill_path"]).is_file(), name)
        self.assertIn("Use the installed `sdlc-review` skill for the detailed review checklist.", self.template("reviewer"))

    def test_english_contract_at_each_consumer(self):
        for role in ("planner", "coder", "reviewer"):
            text = render_role(self.template(role), self.values(role), role)
            with self.subTest(role=role):
                communication = text.split("## Communication\n", 1)[1].split("\n## ", 1)[0]
                self.assertIn("Use direct, plain technical English instructions according to ASD-STE100 plain-language principles.", communication)
                self.assertNotIn("TAS", text)
                self.assertIn("Use English for role communication, tickets, handoffs, findings, technical project documentation, and agent instructions.", text)
                self.assertIn("Preserve exact identifiers, quotations, error messages, and deliberately localized product text.", text)
                self.assertNotIn("user's requested language", text)
        for relative in ("SKILL.md", "references/setup.md", "references/tas-authoring-standard.md"):
            text = (ROOT / relative).read_text()
            with self.subTest(source=relative):
                self.assertIn("English for development communication and artifacts", text)
                self.assertIn("deliberately localized product text", text)
                self.assertNotIn("user's or project's language", text)
                self.assertNotIn("follows the user or project setting", text)

    def test_optional_graph_does_not_remove_structural_verification(self):
        text = render_role(self.template("reviewer"), self.values("reviewer"), "reviewer")
        for clause in (
            "Verify affected structure directly in source, callers, dependencies, contracts, and tests.",
            "You can use an already available authorized graph for a concrete structural question.",
            "Graph access is optional; an unavailable or stale graph alone does not block review.",
            "Graph findings replace neither source review nor tests, and missing edges do not prove a missing dependency.",
            "If a decision-relevant evidence gap remains unresolved, report the technical blocker.",
        ):
            self.assertIn(clause, text)
        self.assertNotIn("Use the approved structural analysis integration", text)
        self.assertNotIn("minimal-change-engineering", text)
        self.assertNotIn("screenshot-to-code", text)
        self.assertNotIn("project-lib-versioning", text)
        self.assertIn("Use the approved structural analysis integration and its original skill.", self.template("planner"))
        self.assertIn("Use the approved analysis integration and its original skill for structural analysis.", self.template("coder"))

    def test_scope_library_ui_and_finding_contracts_reach_reviewer(self):
        text = render_role(self.template("reviewer"), self.values("reviewer"), "reviewer")
        for clause in (
            "Flag unrelated scope or unnecessary complexity when it causes concrete risk or violates accepted requirements.",
            "Do not demand a smaller diff or alternative design solely by preference.",
            "For changed project libraries, verify SemVer and the release policy against the accepted change set and baseline.",
            "Verify affected consumer dependency chains, effective artifact resolution, and relevant builds/tests.",
            "Do not require another bump if the intended version step is already fulfilled.",
            "For visual acceptance, independently view the specified source and actual render at the reviewed state.",
            "Compare relevant viewports, zoom/DPR, source page/crop, data, fonts, content, layout, typography, assets, and required interactions/accessibility under comparable conditions.",
            "Respect accepted deviations and scope.",
            "Record actual visual evidence and missing checks; build success, DOM text, or an image path alone does not prove visual acceptance.",
            "Account for every prior open finding before approval.",
            "Write one coherent finding per list item.",
            "Include the location, failure condition, impact, and correction target.",
            "Use a multi-line reproduction or small code snippet when needed.",
            "Distinguish observed defects, unverified risks, and optional improvements.",
        ):
            self.assertIn(clause, text)
        self.assertNotIn("Write one finding per line.", text)

    def test_equipment_recipes_use_positive_assignments(self):
        analysis = (ROOT / "references/code-analysis.md").read_text()
        self.assertIn("| Planner and Coder | `graphify/skill-claw.md`", analysis)
        self.assertIn("| Planner and Coder | `skills/codebase-memory/SKILL.md`", analysis)
        self.assertIn("# Run for Planner and Coder with their respective ROLE_HOME.", analysis)
        self.assertNotIn("Jede Hermes-Rolle", analysis)
        sources = (ROOT / "references/upstream-sources.md").read_text()
        for name, targets in (
            ("minimal-change-engineering", "Hermes-Planner"),
            ("project-lib-versioning", "Planner and Coder"),
            ("screenshot-to-code", "Planner, Coder and Team-Codex"),
        ):
            row = next(line for line in sources.splitlines() if "]" in line and f"[{name}]" in line)
            self.assertTrue(row.endswith("| " + targets + " |"), row)
        for component in ("codebase-memory", "graphify"):
            row = next(line for line in sources.splitlines() if f'id="{component}"' in line)
            self.assertTrue(row.endswith("| Planner, Coder and Team-Codex |"), row)
        for relative in ("references/code-analysis.md", "references/integrations.md",
                         "references/setup.md", "references/native-workflow.md", "references/verification.md"):
            text = (ROOT / relative).read_text()
            with self.subTest(source=relative):
                self.assertIn("Planner, Coder and Team-Codex", text)
                for obsolete in ("Reviewer receives neither", "Do not install it in Reviewer by default",
                                 "Do not install analysis components in Reviewer by default",
                                 "no default Reviewer integration", "Reviewer has no default analysis",
                                 "Preserve existing local Reviewer adaptations"):
                    self.assertNotIn(obsolete, text)

    def test_retirement_has_exact_skill_scope_and_fixed_release_gate(self):
        """Prose contract only; this does not execute a target retirement."""
        update = (ROOT / "references/update.md").read_text()
        self.assertIn("## Required Reviewer skill retirement (1.1.22)\n", update)
        section = update.split("## Required Reviewer skill retirement (1.1.22)\n", 1)[1].split("\n## ", 1)[0]
        rows = re.findall(r"^\| `([^`]+)` \| `([^`]+)` \|$", section, re.M)
        expected = ("minimal-change-engineering", "project-lib-versioning", "screenshot-to-code",
                    "graphify", "codebase-memory")
        self.assertEqual(rows, [(name, f"<reviewer home>/skills/{name}/") for name in expected])
        self.assertIn("pre-update version below `1.1.22` to a target version at or above `1.1.22`", section)
        self.assertIn("This includes teams on `1.1.21`", section)
        self.assertIn("Keep this introduction release fixed on later Maker releases.", section)
        for name in expected:
            item = MANIFEST["own_skills"].get(name) or MANIFEST["upstream_components"][name]
            self.assertNotIn("reviewer", item["targets"]["hermes"])
        for clause in (
            "This migration overrides local-adaptation preservation only for these five Reviewer skill trees.",
            "Include learned files, references, hidden files, and local additions.",
            "Keep the native `sdlc-review` skill and its automatic integration unchanged.",
            "Preserve all other adaptations and all Planner, Coder and Team-Codex assets.",
            "Preserve shared runtimes, caches, indices, MCP entries, hooks, and unrelated integrations.",
            "Do not copy retired methods into SOUL or other skills.",
        ):
            self.assertIn(clause, section)

    def test_retirement_requires_preapply_pending_state_and_verified_resume(self):
        update = (ROOT / "references/update.md").read_text()
        self.assertIn("## Required Reviewer skill retirement (1.1.22)\n", update)
        section = update.split("## Required Reviewer skill retirement (1.1.22)\n", 1)[1].split("\n## ", 1)[0]
        for clause in (
            "Before invoking `apply`, capture the installed package version and exact Maker commit",
            "Save the pre-update version, target release/commit, and retirement status `pending`",
            "Read back this private record before file application.",
            "Resume a pending retirement on later updates even if `installation.json` already reports `1.1.22` or a later version.",
            "Never infer migration completion from version alone.",
            "For legacy or unknown versions, resolve the source evidence or explicitly reconcile these five identities within the approved scope.",
            "Do not silently skip an unknown version.",
            "Run the pending retirement after successful file application and before reporting a complete team update.",
            "Treat already absent skills as successful no-ops after native readback.",
            "Keep failed or interrupted retirement `pending`, with the concrete blocker and next action.",
            "If retirement is withheld or fails, report `files updated; team update incomplete`.",
        ):
            self.assertIn(clause, section)
        self.assertIn("Before file application, complete the pre-apply record and approval steps", update)
        procedure = section.split("\n1. **", 1)[1].split("\nThe file-updater rollback", 1)[0]
        steps = re.findall(r"(?:^|\n)[1-5]\. \*\*([^*]+)\*\*(.*?)(?=\n[1-5]\. \*\*|\Z)",
                           "1. **" + procedure, re.S)
        self.assertEqual([title for title, _ in steps], [
            "Before file application:", "Read-only discovery:", "Approve the full update scope once:",
            "After successful file application:", "Verify and persist the result:",
        ])
        self.assertIn("Before invoking `apply`, capture the installed package version and exact Maker commit", steps[0][1])
        self.assertIn("retirement status `pending`", steps[0][1])
        preflight = steps[1][1]
        for clause in (
            "Keep this discovery strictly read-only.",
            "Do not remove trees or change exclusions or bindings during discovery.",
            "Inspect native discovery roots and every resolved source path for the five exact skill identities.",
            "Record source ownership, aliases, symlinks, and shared/external sources before selecting any removal path.",
            "determine the supported Reviewer-specific exclusion or unbinding from the installed interface without applying it.",
            "Record the concrete Reviewer-specific obsolete bindings for scope approval.",
        ):
            self.assertIn(clause, preflight)
        self.assertNotRegex(preflight, r"(?im)^\s*(?:If [^\n]*, )?(?:use|apply|reconcile|remove|exclude|unbind)\b")
        approval = steps[2][1]
        self.assertIn("the concrete paths and Reviewer-specific exclusions/unbindings found during read-only discovery", approval)
        self.assertIn("Include the concrete Reviewer-specific obsolete bindings from that inventory.", approval)
        self.assertIn("add the approved exact reconciliation scope to the existing private record before file application", approval)
        postapply = steps[3][1]
        ordered = (
            "Run the pending retirement after successful file application",
            "Save the complete discovered local trees and affected Reviewer-specific bindings",
            "Compare the complete backup inventory and file bytes/hashes with the source before removal.",
            "Save backup location, source inventory, verification, and unaffected-role inventories",
            "Continue only if file application, the complete backup, and backup comparison succeeded.",
            "Recheck the inspected source bytes and bindings immediately before any removal, exclusion, or binding change; stop on concurrent drift.",
            "Remove only the verified Reviewer-local trees",
            "Apply only the inspected, supported Reviewer-specific exclusions/unbindings",
            "Reconcile only the inventoried Reviewer-specific obsolete bindings within the approved update scope.",
        )
        positions = [postapply.index(clause) for clause in ordered]
        self.assertEqual(positions, sorted(positions))
        between_drift_and_removal = postapply.split(ordered[5], 1)[1].split(ordered[6], 1)[0]
        self.assertFalse(between_drift_and_removal.strip(), "Drift check must immediately precede retirement writes")
        for clause in (
            "Resolve the exact Reviewer home from confirmed bindings and native profile inventory.",
            "Inspect native discovery roots and every resolved source path for the five exact skill identities.",
            "Do not delete guessed paths or follow links into shared assets.",
            "determine the supported Reviewer-specific exclusion or unbinding",
            "If no supported isolation is available, stop this reconciliation with a concrete blocker.",
            "outside all native discovery roots",
            "Compare the complete backup inventory and file bytes/hashes with the source before removal.",
            "Recheck the inspected source bytes and bindings immediately before any removal, exclusion, or binding change",
            "Report each concrete retained instruction or autoload reference that would recreate or require a retired skill.",
            "Reconcile only the inventoried Reviewer-specific obsolete bindings within the approved update scope.",
            "Verify absence of all five identities through native Reviewer discovery and source resolution.",
            "Verify preservation of unaffected roles and assets against the pre-removal inventory.",
            "Mark retirement `complete` only after these readbacks pass",
            "The file-updater rollback does not restore this prose poststep's removed trees or bindings.",
            "Restore complete trees, modes, and Reviewer-specific bindings from the external backup",
        ):
            self.assertIn(clause, section)
        self.assertIn("Include these exact removals and the local-adaptation override once in the target update scope and approval.", section)
        self.assertIn("Within that approved update, retirement is mandatory, not an optional second choice.", section)
        self.assertIn("Outside this explicit retirement, retain generic obsolete files and local adaptations.", update)
        self.assertNotIn("Preserve existing installations unless a separate concrete reconciliation is authorized.", update)
        for relative in ("README.md", "references/code-analysis.md", "templates/setup-record.md"):
            self.assertIn("#required-reviewer-skill-retirement-1122", (ROOT / relative).read_text())


class TicketDocumentationTests(unittest.TestCase):
    """Static instruction contracts, not live agent-behavior tests."""

    def setUp(self):
        self.root = ROOT / "skills/brownfield-feature-planning"
        self.skill = (self.root / "SKILL.md").read_text()
        self.release = (self.root / "references/kanban-phase-release.md").read_text()
        self.status = (self.root / "references/kanban-status-inspection.md").read_text()
        self.recovery = (self.root / "references/kanban-triage-recovery.md").read_text()
        self.operator = (self.root / "references/operator-script-acceptance.md").read_text()

    def test_normal_handoff_uses_git_baseline_and_native_card(self):
        self.assertIn("Keep the accepted plan and phase plan in the agreed versioned project location.", self.skill)
        self.assertIn("Record ticket documentation directly on the existing Kanban card.", self.skill)
        self.assertIn("Keep product documentation in its owning repository.", self.skill)
        self.assertIn("Read the accepted specification and plan at their approved Git revisions.", self.release)
        self.assertIn("Verify that every plan reference resolves to its approved revision.", self.release)
        self.assertIn("Verify every notification binding against the intended destination.", self.release)
        self.assertIn("Unblock descendants in reverse order and phase one last.", self.release)

    def test_partial_creation_resumes_from_persisted_cards(self):
        self.assertIn("approved plan path, plan commit and phase identifier", self.release)
        self.assertIn("including archived cards", self.release)
        self.assertIn("Reuse exact matching cards and create only missing phases.", self.release)
        self.assertIn("Read each returned exact card before further writes.", self.release)
        self.assertIn("Stop release on any unresolved mismatch", self.release)

    def test_partial_release_preserves_completed_transitions(self):
        self.assertIn("Before the first release, require every card to be blocked.", self.release)
        self.assertIn("On partial release, verify current runs and dependency gates for already released cards.", self.release)
        self.assertIn("Preserve completed release transitions.", self.release)
        self.assertIn("On resume, apply this order only to pending initial releases.", self.release)
        self.assertNotIn("Every card is still blocked", self.release)
        self.assertNotIn("attachment verification", self.skill)

    def test_correction_updates_existing_assignment_and_plan_reference(self):
        self.assertIn("Update both bodies to reference the exact approved amended plan revision.", self.release)
        self.assertIn("Replace contradictory active body instructions through the supported edit operation.", self.recovery)
        self.assertIn("Preserve the existing card, authorized scope, history, valid dependencies, review provenance and counters.", self.recovery)
        self.assertIn("Keep independent review and required safety checks.", self.skill)

    def test_evidence_reuse_preserves_required_final_state_gates(self):
        self.assertIn("Reuse evidence only while its checked inputs and relevant dependencies, configuration, and test conditions remain valid.", self.skill)
        self.assertIn("A new commit alone does not invalidate every prior result.", self.skill)
        self.assertIn("Keep evidence on the existing card and in original run outputs, not in a separate summary or evidence register.", self.skill)
        self.assertIn("If acceptance explicitly requires an integrated run on the final state", self.status)
        self.assertIn("Do not count targeted tests as that required full acceptance run.", self.status)
        self.assertNotIn("If full acceptance ran on an earlier tree, retain the exact-final-commit gap", self.status)

    def test_operator_blocker_keeps_evidence_and_ownership_on_card(self):
        self.assertIn("Route the handoff to the existing card's authorized owner.", self.status)
        self.assertIn("restart impact", self.status)
        self.assertIn("rollback", self.status)
        self.assertIn("Append actual receipt and explicit assessment to the existing acknowledgment card.", self.operator)
        self.assertIn("Record the repaired boundary, evidence, intended owner, remaining file/verification/commit/review work and unchanged exclusions on the existing card.", self.recovery)
        self.assertIn("Read back the body and resumption comment before release.", self.recovery)
        self.assertIn("Do not complete, reclaim, redispatch, or overwrite it.", self.operator)
        self.assertIn("Verify process exit separately from `ended_at` or board `done`.", self.recovery)
        self.assertIn("Keep orders, results, and assessments on existing Kanban cards", self.operator)

    def test_removed_file_duties_do_not_survive_in_loaded_procedures(self):
        retrospective = (self.root / "references/project-retrospectives.md").read_text()
        self.assertIn("Record a ticket retrospective on the existing card.", retrospective)
        text = "\n".join((self.skill, self.release, self.status, self.recovery, self.operator, retrospective))
        for obsolete in (
            "durable manifest", "repository manifest commit", "existing manifest",
            "central receipt record", "central resumption decision",
            "central feature collection and its index", "README index",
            "Attach the accepted plan and specification as real files",
            "attach the amended plan to both tasks",
            "For an operator handoff, write a durable file",
        ):
            with self.subTest(obsolete=obsolete):
                self.assertNotIn(obsolete, text)


if __name__ == "__main__":
    unittest.main()
