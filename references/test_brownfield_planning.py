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
            ("operator-script-acceptance.md", 31000), ("kanban-status-inspection.md", 26000),
            ("kanban-phase-release.md", 26000), ("kanban-triage-recovery.md", 29000),
        ):
            with self.subTest(reference=name):
                self.assertLessEqual(core + (SKILL / "references" / name).stat().st_size, ceiling)
        # The original 55–80 kB target is advisory. Retained recovery, privacy,
        # and receipt conditions justify this explicit bounded allowance.
        self.assertLessEqual(sum(p.stat().st_size for p in SKILL.rglob("*") if p.is_file()), 90000)


if __name__ == "__main__":
    unittest.main()
