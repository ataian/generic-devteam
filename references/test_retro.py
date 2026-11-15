"""Static package and instruction contracts, not model-behavior or runtime tests.

Run: python3 -B -m unittest discover -s references -p 'test_retro.py' -v
Uses an already available safe YAML parser; never installs dependencies.
"""
from pathlib import Path
import re
import unittest

try:
    from ruamel.yaml import YAML
    YAML_SAFE_LOAD = YAML(typ="safe").load
except ImportError:
    import yaml
    YAML_SAFE_LOAD = yaml.safe_load


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills/retro"
EXPECTED_FILES = {
    "SKILL.md", "README.md", "LICENSE", "NOTICE.md", "references/method.md",
}
REVISION = "4ae2317ddb22b046e26455e4f9c9b3aaaf62212d"

# Each scenario binds a human request/condition to operative shipped guidance.
# This checks instruction coverage, not an agent's response to the request.
SCENARIOS = {
    "machen wir Retro": ("SKILL.md", (
        "Start only on an explicit user request.",
        "Never start automatically after completion or a notification.",
    )),
    "Retrospektive zum letzten Lauf": ("SKILL.md", (
        "Default to the current conversation when the user names no other target.",
        "If the target is ambiguous and retrieval cannot resolve it, ask one scope question.",
    )),
    "/retro session <historical-id>; compressed context": ("SKILL.md", (
        "Locate the named session, ticket, or project through narrow read-only searches.",
        "Include relevant original Coder, Reviewer, and Codex records when available.",
        "Label compressed, missing, inaccessible, or summary-only evidence as gaps.",
        "Do not reconstruct missing events or infer historical instructions from current templates.",
    )),
    "Smooth run; no useful candidate": ("SKILL.md", (
        "Return no changes when the sources support no useful candidate.",
        "Use categories as lenses, not finding quotas.",
    )),
    "Did delivery fulfill the accepted product scope?": ("SKILL.md", (
        "Route product acceptance, delivery-scope verdicts, and code-review requests to their assigned workflow.",
        "Use product defects and failed checks only as evidence of process friction.",
    )),
    "Save tokens by dropping independent review and readbacks": ("references/method.md", (
        "Evaluate total work, not just shorter prose or fewer calls.",
        "Repeated readbacks, independent Coder-versus-Reviewer checks, and pre/post-state checks are not automatically waste.",
        "Preserve required evidence, safety, and meaningful independent review.",
        "Separate measured usage or savings from hypotheses.",
    )),
    "Mechanical violation; existing check is unwired": ("references/method.md", (
        "Read the repository's check scripts and CI workflows before proposing a new check.",
        "Prefer wiring or repairing an existing check over reinventing it.",
        "Route mechanical violations to deterministic checks in the repository's existing language and tooling.",
    )),
    "User asks for retro, not maintenance": ("SKILL.md", (
        "Keep findings as proposals until the user explicitly selects changes and authorizes their implementation scope.",
        "Keep native `/refine` skill-and-memory maintenance separate; do not invoke or improvise it automatically.",
    )),
}


def require_clauses(text, clauses):
    for clause in clauses:
        assert clause in text, f"Missing operative instruction: {clause}"


class RetroPackageTests(unittest.TestCase):
    def text(self, relative):
        return (PACKAGE / relative).read_text(encoding="utf-8")

    def test_complete_portable_package(self):
        self.assertTrue(PACKAGE.is_dir(), "Missing standalone retro package")
        paths = list(PACKAGE.rglob("*"))
        self.assertFalse(any(p.is_symlink() for p in paths))
        self.assertEqual({p.relative_to(PACKAGE).as_posix() for p in paths if p.is_file()}, EXPECTED_FILES)
        for path in paths:
            if path.is_file():
                text = path.read_text(encoding="utf-8")
                self.assertNotRegex(text, r"/home/|/workspace/|/tmp/")
                self.assertNotIn("Call the Skill tool", text)

    def test_frontmatter_trigger_and_identity(self):
        text = self.text("SKILL.md")
        self.assertTrue(text.startswith("---\n"))
        header, body = text[4:].split("\n---\n", 1)
        meta = YAML_SAFE_LOAD(header)
        self.assertIsInstance(meta, dict)
        self.assertEqual(meta["name"], "retro")
        self.assertEqual(meta["version"], "0.1.0")
        self.assertEqual(meta["license"], "MIT")
        self.assertEqual(meta["platforms"], ["linux", "macos", "windows"])
        self.assertTrue(meta["description"].startswith("Use when"))
        self.assertIn("user requests", meta["description"])
        self.assertLessEqual(len(meta["description"]), 60)
        self.assertTrue(meta["description"].endswith("."))
        self.assertNotIn("disable-model-invocation", meta)
        self.assertTrue(body.strip())
        for trigger in ("/retro", "machen wir Retro", "Retrospektive zum letzten Lauf"):
            self.assertIn(trigger, body)

    def test_required_method_load_is_reachable(self):
        require_clauses(self.text("SKILL.md"), (
            "Read [the adapted method](references/method.md) completely before analysis.",
            "If that reference is missing or unreadable, report its path and stop analysis.",
        ))
        method = self.text("references/method.md")
        self.assertFalse(method.startswith("---"))
        self.assertNotIn("disable-model-invocation", method)
        for lens in ("Navigation", "Automated checks", "Review standards", "Sparse steering", "Tool economy", "No-ops", "Information access", "Token economy"):
            self.assertIn("## " + lens, method)

    def test_all_local_markdown_links_resolve_inside_package(self):
        for path in PACKAGE.rglob("*.md"):
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
                if re.match(r"[a-z]+:", link):
                    continue
                self.assertNotIn("#", link, "Validate anchors if package adds them")
                target = (path.parent / link).resolve()
                self.assertTrue(target.is_relative_to(PACKAGE.resolve()), (path, link))
                self.assertTrue(target.is_file(), (path, link))

    def test_source_identity_and_mit_permission_are_retained(self):
        notice = self.text("NOTICE.md")
        for source in ("skills/engineering/retro/SKILL.md", "docs/engineering/retro.md",
                       "skills/productivity/writing-for-agents/SKILL.md",
                       "skills/productivity/writing-for-agents/SKILL-MECHANICS.md"):
            self.assertIn(source, notice)
        self.assertIn(REVISION, notice)
        self.assertIn("https://github.com/mattpocock/skills", notice)
        license_text = self.text("LICENSE")
        for clause in ("Copyright (c) 2026 Matt Pocock", "Permission is hereby granted, free of charge",
                       "The above copyright notice and this permission notice shall be included",
                       'THE SOFTWARE IS PROVIDED "AS IS"'):
            self.assertIn(clause, license_text)

    def test_text_scenarios_cover_operative_guidance(self):
        for scenario, (path, clauses) in SCENARIOS.items():
            with self.subTest(scenario=scenario):
                require_clauses(self.text(path), clauses)

    def test_mutations_remove_instructions_not_just_headings(self):
        for scenario, (path, clauses) in SCENARIOS.items():
            text = self.text(path)
            require_clauses(text, clauses)
            for clause in clauses:
                with self.subTest(scenario=scenario, removed=clause), self.assertRaisesRegex(AssertionError, "Missing operative instruction"):
                    require_clauses(text.replace(clause, ""), clauses)

    def test_role_and_economy_boundaries(self):
        method = self.text("references/method.md")
        require_clauses(method, (
            "Keep implementation-critical requirements and conventions available to the Coder.",
            "Independent review can require source exploration; a diff alone is not always sufficient.",
            "Reuse an existing suitable standards or contribution document before proposing a new `CODING_STANDARDS.md`.",
            "Ground no-op deletion candidates in observed behavior, not intuition about model defaults.",
        ))
        for topic in ("repeated unchanged source loading", "oversized outputs", "unnecessary carried context",
                      "repeated reconstruction across handoffs", "duplicate analysis and documents", "unproductive retries"):
            self.assertIn(topic, method)

    def test_brownfield_reference_is_only_a_reliable_route(self):
        route = ROOT / "skills/brownfield-feature-planning/references/project-retrospectives.md"
        text = route.read_text()
        require_clauses(text, (
            "Load the standalone `retro` skill only for an explicit user request.",
            "../../retro/SKILL.md", "Report the missing skill if neither path is available.",
        ))
        self.assertTrue((route.parent / "../../retro/SKILL.md").resolve().is_file())
        self.assertNotIn("Compare the delivered artifact with the accepted contract", text)
        self.assertNotIn("## Assess the evidence", text)
        core = (ROOT / "skills/brownfield-feature-planning/SKILL.md").read_text()
        self.assertIn("| Explicit user request for a process retrospective | [Standalone retro routing](references/project-retrospectives.md) |", core)

    def test_short_prioritized_proposals_and_bounded_evidence(self):
        require_clauses(self.text("SKILL.md"), (
            "Return a short severity-ordered list in the requesting conversation unless the user requests another destination.",
            "Observation and exact source; process cause with fact versus hypothesis; proposed change, location, and owner.",
            "Expected benefit and material trade-off; observable success criterion when useful.",
            "Keep each candidate traceable to an original event or inspected configuration.",
            "Read only the relevant event ranges; avoid whole-archive dumps.",
        ))


if __name__ == "__main__":
    unittest.main()
