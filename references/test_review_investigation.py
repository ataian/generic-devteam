"""Static rendered instruction/mutation contracts, not executed agent behavior.

Catch loss of proportionality, orphaned correctness, biased helpers, unchecked
aggregation, duplicate investigation, and unqualified critical-pass credit.
Exercise the shipped SOUL through the real renderer and manifest export.
"""
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from render_text import render_role, role_fields

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "templates/roles/reviewer.SOUL.md.template"


class ReviewInvestigationTests(unittest.TestCase):
    def rendered(self, root=ROOT):
        template = (root / SOURCE).read_text()
        values = {key: "Example" for key in role_fields(template, "reviewer")}
        values.update(ROLE_REASONING_DEFAULT="low", ROLE_REASONING_HIGH="medium")
        return render_role(template, values, "reviewer")

    def section(self, text, heading):
        marker = "## " + heading + "\n"
        self.assertIn(marker, text, "Missing operative section: " + heading)
        return text.split(marker, 1)[1].split("\n## ", 1)[0]

    def require(self, text, *patterns):
        for pattern in patterns:
            self.assertRegex(text, pattern)

    def check_entry(self, text):
        section = self.section(text, "Proportional investigation")
        self.require(section,
                     r"Review small, clearly bounded corrections directly",
                     r"multiple substantive behavior cases or technical interactions.*two parallel fresh-context investigations.*both axes have meaningful distinct work",
                     r"complexity, coupling, and independent work.*not line/file counts",
                     r"Reviewer.*sole owner of coverage and the final verdict")

    def check_spec(self, text):
        section = self.section(text, "Proportional investigation")
        self.require(section,
                     r"Spec / requirement fidelity.*complete accepted plan.*assigned ticket criteria",
                     r"missing or changed behavior.*incorrect semantics.*scope drift.*evidence supports claimed fulfillment",
                     r"missing accepted plan.*existing clarification route.*not permission to skip Spec or approve")

    def check_technical(self, text):
        section = self.section(text, "Proportional investigation")
        self.require(section,
                     r"Technical quality / standards.*correctness.*repository rules.*surrounding source and callers.*error paths.*regressions.*architecture.*security.*data integrity.*actual impact",
                     r"Documented conventions outrank smell preferences",
                     r"mechanically enforced rules.*necessary verification")

    def check_binding(self, text):
        section = self.section(text, "Proportional investigation")
        self.require(section,
                     r"both helpers.*same exact implementation commit, working-tree state, and approved plan baseline",
                     r"distinct briefs.*required source/context access.*task-specific risks and permissions",
                     r"neither helper.*other helper's findings.*main Reviewer's provisional conclusions",
                     r"Requirements and neutral reproduction/test evidence.*permitted",
                     r"read-only.*findings, evidence, and gaps only to you",
                     r"must not implement, issue Kanban transitions, or enlarge scope or permissions",
                     r"same model/provider and reasoning policies.*access, approval, operational, and resource limits",
                     r"existing permitted native paths.*supported schema.*effective model/provider and reasoning.*not prompt requests alone")

    def check_synthesis(self, text):
        section = self.section(text, "Proportional investigation")
        self.require(section,
                     r"Validate decisive findings against actual source, requirements, and evidence",
                     r"Resolve disagreements.*concrete coverage gaps",
                     r"Keep both axes distinguishable.*pass on one cannot cancel a defect on the other",
                     r"combined outcome.*not a vote or unchecked aggregation",
                     r"Do not automatically repeat every investigation or add a third full review",
                     r"Coordinate required test/build/runtime evidence at the same code state",
                     r"not a full suite per helper.*independently successful suites.*valid",
                     r"missing required check.*existing routing",
                     r"correction or resume.*affected findings/areas.*all outstanding requests.*still-valid work",
                     r"new commit or correction round alone.*not restart both helpers",
                     r"existing ticket.*source/evidence provenance",
                     r"no new tickets, approval rounds, helper profiles, or mandatory report files")

    def check_critical(self, text):
        section = self.section(text, "Independent review and high risk")
        self.require(section,
                     r"material security, data-integrity, transaction, or concurrency invariants, obtain a separate pass.*even when the main review finds no defect",
                     r"technical-axis helper.*only when every separate-pass condition.*holds",
                     r"explicit coverage of the affected invariants",
                     r"fresh context at `medium`.*same model/provider, reasoning, access, approval, and read-only limits",
                     r"Supply the exact commit, accepted requirements, affected invariants, and relevant source and test access",
                     r"Retain the operational and resource limits above",
                     r"Omit the Coder's narrative and the main review's findings until this pass forms its own assessment",
                     r"Exclude other helpers' findings too",
                     r"Validate actual returned coverage and evidence before crediting.*otherwise obtain the required targeted pass",
                     r"ordinary/default-reasoning helper.*not sufficient",
                     r"required high-reasoning verification or a permitted fresh context is unavailable, report the capability blocker",
                     r"A new commit alone does not invalidate every prior result")

    def test_small_correction_and_substantive_parallel_cases_have_distinct_entry(self):
        self.check_entry(self.rendered())

    def test_missing_spec_cannot_be_waived(self):
        self.check_spec(self.rendered())

    def test_correctness_does_not_fall_between_axes(self):
        self.check_technical(self.rendered())

    def test_helpers_receive_neutral_exact_state_and_role_limits(self):
        self.check_binding(self.rendered())

    def test_synthesis_and_correction_reuse_preserve_accountable_verdict(self):
        self.check_synthesis(self.rendered())

    def test_technical_helper_credit_is_conditional_and_requires_returned_evidence(self):
        self.check_critical(self.rendered())

    def test_baseline_native_outcomes_and_final_state_checks_remain(self):
        text = self.rendered()
        self.require(text,
                     r"installed original `sdlc-review`.*per-round lenses, baseline duties, and native outcomes",
                     r"Keep its automatic dispatcher integration unchanged",
                     r"Apply all baseline duties before every verdict",
                     r"Do not manufacture extra rounds or postpone baseline duties",
                     r"Run checks affected by changes or insufficient evidence; retain required independent checks and explicit final-state acceptance tests",
                     r'"reviewed_commit":"<exact-commit>"',
                     r"kanban_request_changes", r'kanban_block\(kind="capability"',
                     r"already-consumed one-shot allowance does not renew",
                     r"Use it to format findings, including its Auto-Clarity exceptions")

    def test_removing_operative_bodies_fails_contracts_not_only_headings(self):
        text = self.rendered()
        for heading, checker in (
                ("Proportional investigation", self.check_entry),
                ("Proportional investigation", self.check_spec),
                ("Proportional investigation", self.check_binding),
                ("Proportional investigation", self.check_technical),
                ("Proportional investigation", self.check_synthesis),
                ("Independent review and high risk", self.check_critical)):
            with self.subTest(heading=heading, checker=checker.__name__):
                body = self.section(text, heading)
                mutated = text.replace(body, "\n", 1)
                with self.assertRaises(AssertionError):
                    checker(mutated)

    def test_each_critical_credit_condition_is_required_not_just_a_heading(self):
        text = self.rendered()
        for clause in (
                "only when every separate-pass condition below holds",
                "explicit coverage of the affected invariants",
                "fresh context at `medium`", "same model/provider", "reasoning,",
                "access,", "approval,", "read-only limits", "operational and resource limits above",
                "exact commit, accepted requirements", "relevant source and test access",
                "Omit the Coder's narrative", "the main review's findings",
                "Exclude other helpers' findings too",
                "Validate actual returned coverage and evidence before crediting",
                "otherwise obtain the required targeted pass"):
            with self.subTest(removed=clause):
                self.assertIn(clause, text)
                with self.assertRaises(AssertionError):
                    self.check_critical(text.replace(clause, "[removed]"))

    def test_manifest_export_contains_method_in_reviewer_soul_without_new_skill(self):
        manifest = json.loads((ROOT / "manifest.json").read_text())
        self.assertNotIn("code-review", manifest["own_skills"])
        self.assertNotIn("code-review", manifest["upstream_components"])
        self.assertEqual(manifest["role_templates"]["reviewer"]["transport"],
                         {"reviewer.SOUL.md.template": "SOUL.md"})
        with tempfile.TemporaryDirectory(prefix="maker-review-export-") as directory:
            export = Path(directory)
            for relative in manifest["files"] + ["manifest.json"]:
                target = export / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            for checker in (self.check_entry, self.check_spec, self.check_technical,
                            self.check_binding, self.check_synthesis, self.check_critical):
                checker(self.rendered(export))
            self.assertEqual(self.rendered(export), self.rendered())


if __name__ == "__main__":
    unittest.main()
