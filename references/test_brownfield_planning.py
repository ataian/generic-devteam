"""Static package/instruction checks; these do not test live agent behavior."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/brownfield-feature-planning"


def local_links(root):
    """Validate shipped Markdown targets, including explicit and heading anchors."""
    for source in root.rglob("*.md"):
        text = source.read_text()
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-z]+:", link):
                continue
            path, _, fragment = link.partition("#")
            target = (source.parent / path).resolve() if path else source
            assert target.is_relative_to(root.resolve()), (source, link)
            assert target.is_file(), (source, link)
            if fragment:
                body = target.read_text()
                headings = re.findall(r"^#{1,6}\s+(.+)$", body, re.M)
                anchors = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
                anchors.update(re.findall(r'<a\s+(?:id|name)="([^"]+)"', body))
                assert fragment in anchors, (source, link)


def core_contract(text):
    for requirement in (
        "Keep accepted product decisions binding when revising a plan.",
        "Record ticket documentation directly on the existing Kanban card.",
        "Do not create implementation tickets before explicit plan acceptance.",
        "Keep independent review and required safety checks.",
        "Load a reference only when its trigger applies.",
        "Do not infer permission to mutate a resource from permission to inspect it.",
    ):
        assert requirement in text, requirement


class BrownfieldPackageTests(unittest.TestCase):
    def test_compact_core_has_operative_instructions(self):
        text = (SKILL / "SKILL.md").read_text()
        core_contract(text)
        self.assertLessEqual(len(text.encode()), 14000)
        for heading in ("## When to use", "## Planning procedure", "## Conditional references", "## Verification"):
            self.assertIn(heading, text)
        # Prevent a return to giant single-line incident histories.
        self.assertLess(max(map(len, text.splitlines())), 500)

    def test_core_contract_detects_missing_rule_not_just_heading(self):
        text = (SKILL / "SKILL.md").read_text()
        core_contract(text)
        for line in (
            "Keep independent review and required safety checks.",
            "Do not create implementation tickets before explicit plan acceptance.",
            "Do not infer permission to mutate a resource from permission to inspect it.",
        ):
            with self.subTest(rule=line), self.assertRaises(AssertionError):
                core_contract(text.replace(line, ""))

    def test_complete_skill_tree_is_in_manifest(self):
        manifest = json.loads((ROOT / "manifest.json").read_text())
        actual = {str(p.relative_to(ROOT)) for p in SKILL.rglob("*") if p.is_file()}
        declared = {p for p in manifest["files"] if p.startswith("skills/brownfield-feature-planning/")}
        self.assertEqual(actual, declared)
        self.assertFalse(any(p.is_symlink() for p in SKILL.rglob("*")))
        self.assertEqual(manifest["own_skills"]["brownfield-feature-planning"]["targets"], {"hermes": ["planner"]})

    def test_references_are_reachable_and_links_resolve(self):
        main = (SKILL / "SKILL.md").read_text()
        names = {
            "data-discovery.md", "replacement-imports.md", "operator-script-acceptance.md",
            "kanban-phase-release.md", "kanban-status-inspection.md",
            "kanban-triage-recovery.md", "project-retrospectives.md",
        }
        self.assertEqual({p.name for p in (SKILL / "references").glob("*.md")}, names)
        for name in names:
            self.assertIn("references/" + name, main)
        local_links(SKILL)

    def test_project_specific_choices_are_not_generic_defaults(self):
        texts = "\n".join(p.read_text() for p in SKILL.rglob("*.md"))
        for old in (
            "with `01`", "offer checkboxes with one batch-add action",
            "disabled control with tooltip", "PropertiesLauncher", "~/.m2/settings.xml",
            "Save reusable process lessons in this skill",
        ):
            with self.subTest(obsolete=old):
                self.assertNotIn(old, texts)

    def test_specialist_scenarios_retain_operative_gates(self):
        scenarios = {
            "data-discovery.md": (
                "Do not silently turn its search results into an allowlist.",
                "Encode and test the exact approved normalization rule, including its limits.",
                "When disabled, require no optional datastore, connection attempt, migration, import, or dependent UI.",
            ),
            "replacement-imports.md": (
                "Resolve replacement targets only through the importer-owned mapping.",
                "Under agreed strict rejection, fail the whole import and preserve the prior snapshot.",
                "Mutate the populated source database only when expressly authorized.",
                "Do not blindly call current upload validation or disable all validation.",
            ),
            "operator-script-acceptance.md": (
                "The independent reviewer chooses/assesses separate rechecks and owns the verdict.",
                "Freeze the tested tree during each operator run and refresh resource inventory before mutation.",

            ),
            "kanban-triage-recovery.md": (
                "Require an ended previous writer and no parallel repository writer before continuation.",
                "The script rejects signature drift but does not prove semantic equivalence.",
                "Do not hardcode a coder or bypass an unresolved `CHANGES_REQUESTED` verdict.",
            ),
        }

        for name, requirements in scenarios.items():
            text = (SKILL / "references" / name).read_text()
            for requirement in requirements:
                with self.subTest(reference=name, requirement=requirement):
                    self.assertIn(requirement, text)

        status = (SKILL / "references/kanban-status-inspection.md").read_text()
        self.assertIn("Do not substitute operator completion for later coding/product review.", status)

    def test_proposal_chain_budgets(self):
        core = (SKILL / "SKILL.md").stat().st_size
        # Bounded allowances, not assertions about token/monetary savings.
        for name, ceiling in (
            ("data-discovery.md", 25000), ("replacement-imports.md", 28000),
            ("operator-script-acceptance.md", 32000), ("kanban-status-inspection.md", 26000),
            ("kanban-phase-release.md", 26000), ("kanban-triage-recovery.md", 29000),
        ):
            with self.subTest(reference=name):
                self.assertLessEqual(core + (SKILL / "references" / name).stat().st_size, ceiling)
        # The original 55–80 kB target is advisory. Retained recovery, privacy,
        # receipt conditions, and story/card contracts justify this bounded allowance.
        self.assertLessEqual(sum(p.stat().st_size for p in SKILL.rglob("*") if p.is_file()), 93000)


    def test_plan_separates_binding_scope_from_coder_discretion(self):
        text = (SKILL / "SKILL.md").read_text()
        for clause in (
            "Distinguish binding requirements and architectural constraints from implementation suggestions.",
            "Expected file lists are guidance unless explicitly marked as hard boundaries.",
            "Leave execution-time technical decisions within the accepted goal and constraints to the Coder.",
            "Record consequential in-scope decisions on the existing ticket.",
            "For an authorized binding amendment, update the versioned plan and affected current and future ticket bindings before release.",
            "Preserve already-reviewed history and verify the returning worker's applicable baseline.",
        ):
            self.assertIn(clause, text)

    def test_story_decomposition_precedes_phase_and_ticket_mapping(self):
        text = (SKILL / "SKILL.md").read_text()
        phases = text.split("### 4. Build reviewable phases\n", 1)[1].split("\n### 5.", 1)[0]
        for clause in (
            "Cut work by actor, desired behaviour, and benefit before mapping stories to phases and tickets.",
            "Give each slice an observable, independently verifiable outcome across the relevant layers.",
            "Do not disguise database/API/UI layer tasks as stories by adding an actor prefix.",
            "Justify necessary foundations by the stories they enable and their verification gate.",
            "Choose phase and ticket boundaries for reviewability and real dependencies, not a one-story/one-phase/one-ticket rule.",
        ):
            self.assertIn(clause, phases)
        self.assertLess(phases.index("Cut work by actor"), phases.index("Give each phase"))
        self.assertIn("apply the Planner's caller-contract and abstraction checks", text)

    def test_phase_release_keeps_story_content_exact_bindings_and_recovery(self):
        release = (SKILL / "references/kanban-phase-release.md").read_text()
        for clause in (
            "Write a concise actor-behaviour-benefit title, not a technical task label.",
            "Surface incompatible native title constraints instead of truncating user meaning.",
            "Goal/context: state the outcome and necessary context.",
            "Acceptance criteria: list concrete observable success conditions.",
            "Technical implementation: include necessary interfaces, affected areas, and constraints; label suggestions separately.",
            "Verification: state the checks needed to establish these criteria, including relevant failure cases.",
            "Dependencies and binding: name blockers, absolute accepted plan/phase paths, exact Git commits, phase identifier, and planning repository root.",
            "Keep criteria and implementation context concise; align excerpts with the authoritative accepted plan.",
            "Make the card understandable without opening the full plan; leave implementation discretion with the Coder.",
            "Do not repeat the whole plan, routine team procedures, or successful-test catalogues.",
            "Match persisted cards to the planned ticket identity, approved plan path, plan commit and phase identifier.",
            "Reuse exact matching cards and create only missing planned tickets.",
            "Check each story, criterion, technical constraint and exception against its phase scope, gate, commit boundary and reviewer binding.",
            "--initial-status blocked", "idempotency key", "explicit completion contract",
            "Read each returned exact card before further writes.",
            "Leave later advancement to the dispatcher and independent review gates.",
        ):
            self.assertIn(clause, release)
        for obsolete in ("create only missing phases", "complete accepted phase list", "Write a short goal"):
            self.assertNotIn(obsolete, release)

    def test_domain_clarification_uses_planner_workflow(self):
        text = (SKILL / "SKILL.md").read_text()
        self.assertIn("Use the Planner's `domain-modeling` workflow.", text)

    def test_integrated_acceptance_uses_existing_phase_and_reviewer(self):
        text = (SKILL / "SKILL.md").read_text()
        self.assertIn("Assign each acceptance criterion to an implementation ticket and its existing independent Reviewer.", text)
        self.assertIn("Place combined-behavior checks in the phase where integrated behavior becomes available.", text)
        self.assertIn("Use existing results for the Planner's final customer report, not a new technical review or closing ticket.", text)

    def test_progress_policy_preserves_explicit_and_native_limits_only(self):
        text = (SKILL / "SKILL.md").read_text()
        release = (SKILL / "references/kanban-phase-release.md").read_text()
        for clause in (
            "Work until the acceptance criteria are met.",
            "Correct recoverable failures independently.",
            "Escalate the concrete obstacle when no justified next approach remains.",
            "Preserve explicit customer financial/resource caps, configured limits, provider quotas, operational permissions, and native failure-loop guards.",
        ):
            self.assertIn(clause, text)
        self.assertNotIn("who may authorize an extension", text)
        self.assertNotIn("retry allowances", text)
        self.assertIn("Set explicit customer limits and required native runtime/retry fields without inventing discretionary attempt budgets.", release)
        for source in (text, release):
            self.assertNotIn("Use native run logs for detailed execution output.", source)
            self.assertIn("Native run outputs remain available evidence, not an authored run-log duty.", source)

    def test_recovery_screens_current_blocker_and_keeps_customer_return_in_execution(self):
        text = (SKILL / "references/kanban-triage-recovery.md").read_text()
        for clause in (
            "Triage means blocked work in this team; never deliberately send work there.",
            "Check an actual Coder escalation for an overlooked in-scope solution before involving the customer.",
            "Record the correction and resume the Coder without a customer round.",
            "Record a sufficient customer answer and its scope on the existing ticket.",
            "Use `kanban_comment(task_id=..., body=...)` and read back the posted decision before resumption.",
            "An old answer must not clear a newer blocker.",
            "Leave an already-active or completed task unchanged.",
            "A Mattermost wake is not an active Reviewer run; use ordinary unblock or guarded triage recovery instead of request-changes.",
            "Preserve native counter semantics, including resets performed by legitimate native transitions.",
        ):
            self.assertIn(clause, text)
        self.assertNotIn("Resolve routine technical decisions within the planner's existing mandate", text)
        self.assertNotIn("answered planner question", text)

    def test_workflow_migration_orders_old_ownership_before_new_authority(self):
        """Static update recipe contract; native migration fixtures are separate."""
        update = (ROOT / "references/update.md").read_text()
        heading = "## Workflow migration (2.0.0)\n"
        self.assertIn(heading, update)
        section = update.split(heading, 1)[1].split("\n## ", 1)[0]
        steps = re.findall(r"(?:^|\n)[1-7]\. \*\*([^*]+)\*\*(.*?)(?=\n[1-7]\. \*\*|\Z)", section, re.S)
        self.assertEqual([title for title, _ in steps], [
            "Inspect before authority changes:", "Settle active old-contract work:",
            "Resolve parked legacy cards:", "Reconcile local authority:",
            "Review and apply files:", "Read back the same cards:",
            "Verify subsequent instruction loading:",
        ])
        for clause in (
            "pre-update version below `2.0.0` to a target at or above `2.0.0`",
            "Resume an unfinished migration even after installation metadata advances.",
            "Resolve unknown legacy provenance instead of assuming completion.",
        ):
            self.assertIn(clause, section)
        for clause in (
            "Let active workers finish under their existing contract or obtain a separately scoped transition decision.",
            "Do not mix old and new loaded roles on one active handoff.",
            "For an active legacy Planner review run, let that owner use the established native `kanban_request_changes` return to its original Coder.",
            "This is a migration-only completion, not the route for new questions.",
        ):
            self.assertIn(clause, steps[1][1])
        for clause in (
            "Require no active run or competing claim.",
            "Resolve the actual blocker and use ordinary unblock or guarded triage recovery to restore its source phase first.",
            "If clarification is complete and Coder continuation is required, use the guarded review-reopen procedure",
            "Preserve pending independent review and unresolved `CHANGES_REQUESTED` findings.",
            "Do not reopen pending review indiscriminately.",
        ):
            self.assertIn(clause, steps[2][1])
        for clause in (
            "Reconcile old Planner-review clarification routes and fixed discretionary retry approvals within the approved update mandate.",
            "Preserve explicit customer financial/resource caps, operational permissions, native guards, and unrelated local adaptations.",
            "Obtain a customer decision only for genuinely conflicting explicit mandates.",
        ):
            self.assertIn(clause, steps[3][1])
        self.assertIn("Recheck current runs and claims immediately before application; defer if the settled state changed.", steps[4][1])
        self.assertIn("Keep the same card and its history.", steps[5][1])
        self.assertIn("For the next Coder handoff, bind the independent Reviewer explicitly; retain historical Planner provenance.", steps[5][1])
        self.assertIn("Verify effective loading in subsequent execution contexts separately from saved file bytes.", steps[6][1])
        self.assertIn("Do not restart a gateway or session merely because files changed.", steps[6][1])
        self.assertLess(update.index(heading), update.index("## Activity and application\n"))
        self.assertIn("Before applying workflow authority changes, complete steps 1–4", update)

    def test_technical_review_interruption_does_not_require_coder_rework(self):
        text = (SKILL / "references/kanban-triage-recovery.md").read_text()
        for clause in (
            "For a technical interruption during review, restore unfinished review with its existing provenance.",
            "Use a Coder return only for substantive findings, questions, or required implementation continuation.",
            "Keep capability failures and verified quota pauses blocked until their actual cause is resolved.",
        ):
            self.assertIn(clause, text)


if __name__ == "__main__":
    unittest.main()
