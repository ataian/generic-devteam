"""Static instruction/package contracts, not model behavior or live discovery.

Run: python3 -B -m unittest discover -s references -p 'test_diagnosing_bugs.py' -v
"""
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from render_text import render_role, role_fields
from test_retro import YAML_SAFE_LOAD

ROOT = Path(__file__).resolve().parents[1]
SKILL = "skills/diagnosing-bugs/"
FILES = {"SKILL.md", "README.md", "LICENSE", "NOTICE.md", "references/method.md"}
REVISION = "4ae2317ddb22b046e26455e4f9c9b3aaaf62212d"

# Bind concrete diagnostic conditions to operative guidance, not fixture labels.
SCENARIOS = {
    "simple evidenced boundary error with exact failing test": ("SKILL.md", (
        "Use the direct-fix path only when all three conditions hold:",
        "Concrete evidence supports both the symptom and its cause.",
        "The affected flow and required correction are clear.",
        "A focused test or reproducible check can demonstrate the exact bug and its correction.",
        "Demonstrate the error, correct its cause, and run relevant verification.",
        "Do not generate alternatives, build a separate harness, or further minimize an already simple case to satisfy a checklist.",
    )),
    "first targeted investigation leaves two competing causes": ("SKILL.md", (
        "The cause remains unclear after the first targeted investigation.",
        "Multiple plausible causes need distinguishing.",
        "Switch as soon as uncertainty is evident, before guessed fix attempts.",
        "Read [the full method](references/method.md) completely when any full-diagnosis trigger applies.",
    )),
    "intermittent state/timing/environment failure": ("SKILL.md", (
        "The failure is intermittent or depends on state, timing, or environment.",
    )),
    "performance regression": ("SKILL.md", (
        "A performance regression needs measurement and isolation.",
    )),
    "apparent fix leaves symptom or bug recurs": ("SKILL.md", (
        "An apparent fix leaves the original symptom unresolved, or the failure recurs.",
        "Reuse completed investigation, repros, and checks instead of restarting.",
        "Technical deepening within accepted scope needs no new Planner or customer approval.",
    )),
    "ordinary implementation develops unexplained test regression": ("SKILL.md", (
        "Use for bug/diagnosis tasks and unexplained test failures or regressions found during ordinary implementation.",
    )),
    "clear cause but material security/data-integrity risk": ("SKILL.md", (
        "Preserve required security, data-integrity, acceptance, and independent-review checks on both paths.",
        "Risk alone does not require prolonged cause exploration; ticket or diff size does not select the path.",
    )),
    "ambiguous cause needs discriminating probes": ("references/method.md", (
        "Where ambiguity remains, rank competing falsifiable hypotheses by evidence and state each prediction.",
        "Use each targeted probe to distinguish those predictions; change one variable at a time.",
        "Prefer a debugger or REPL, then targeted boundary instrumentation, over indiscriminate logging.",
        "Ask through existing routing only when customer knowledge, a decision, or permission is needed.",
    )),
    "rare failure and slow necessary integration check": ("references/method.md", (
        "For intermittent failures, record reproduction rates and controlled conditions before and after the fix.",
        "A single green run does not establish resolution.",
        "Optimize toward seconds without dropping necessary slow integration checks.",
        "For performance regressions, establish a baseline and measure/profile, compare, or bisect before declaring cause or improvement.",
    )),
    "no loop; protected production artifact required": ("references/method.md", (
        "Without a reproducible loop, label hypotheses provisional and use them only to guide safe evidence collection.",
        "Do not claim a confirmed cause or fix without supporting evidence.",
        "Request required environment/access, redacted artifacts, or production-instrumentation permission through existing routing.",
        "Missing reproduction grants no additional access or operational authority.",
    )),
    "chain bug cannot be locked down by single-caller test": ("references/method.md", (
        "Use a regression seam that exercises the real failure pattern, including multi-caller or chain behavior when needed.",
        "Run the regression red before the fix, then green afterward.",
        "Rerun the original unminimized scenario after the fix.",
        "Document a missing suitable seam or required access precisely; preserve explicit acceptance and safety checks.",
        "A missing seam neither waives a required check nor authorizes architecture redesign.",
    )),
    "human reproduction and task-owned cleanup": ("references/method.md", (
        "Use human-assisted reproduction only as a necessary last resort through existing communication and protected-input facilities.",
        "Never collect passwords or tokens as observations.",
        "Remove only task-owned temporary artifacts and instrumentation within existing ownership and approval limits.",
        "Retain a useful repro as regression coverage or in a clearly designated debug area when justified.",
        "State confirmed cause and meaningful verification in existing commit, handoff, or task conventions.",
    )),
}


def require(text, clauses):
    for clause in clauses:
        assert clause in text, "Missing operative instruction: " + clause


def scenario_contract(root, filename, clauses):
    path = root / SKILL / filename
    assert path.is_file(), "Missing diagnosis instruction: " + str(path)
    require(path.read_text(), clauses)


def delivery_contract(root):
    manifest = json.loads((root / "manifest.json").read_text())
    item = manifest["own_skills"].get("diagnosing-bugs")
    assert item is not None, "Missing owned diagnosis delivery"
    assert item["targets"] == {"codex": ["team-codex"]}, "Wrong diagnosis consumer"
    assert item["transport"] == {"SKILL.md": "SKILL.md"}
    assert "diagnosing-bugs" not in manifest["upstream_components"]
    for key in ("skill_path", "license_path", "notice_path"):
        assert (root / item[key]).is_file(), "Missing diagnosis asset: " + key
    paths = list((root / SKILL).rglob("*"))
    assert not any(p.is_symlink() for p in paths), "Symlink in diagnosis package"
    actual = {p.relative_to(root / SKILL).as_posix() for p in paths if p.is_file()}
    assert actual == FILES, "Incomplete diagnosis tree"
    assert {SKILL + name for name in FILES} <= set(manifest["files"]), "Missing diagnosis inventory"


class DiagnosisContracts(unittest.TestCase):
    def text(self, filename):
        path = ROOT / SKILL / filename
        self.assertTrue(path.is_file(), "Missing diagnosis instruction: " + str(path))
        return path.read_text()

    def test_static_proportional_scenarios(self):
        for scenario, (filename, clauses) in SCENARIOS.items():
            with self.subTest(scenario=scenario):
                scenario_contract(ROOT, filename, clauses)

    def test_complete_owned_tree_has_exact_team_codex_assignment(self):
        delivery_contract(ROOT)

    def test_metadata_remains_implicitly_callable_and_portable(self):
        text = self.text("SKILL.md")
        self.assertTrue(text.startswith("---\n"))
        header, body = text[4:].split("\n---\n", 1)
        meta = YAML_SAFE_LOAD(header)
        self.assertEqual(meta["name"], "diagnosing-bugs")
        self.assertEqual(meta["license"], "MIT")
        self.assertEqual(meta["version"], "0.1.0")
        self.assertIn("bug", meta["description"])
        self.assertIn("regression", meta["description"])
        self.assertLessEqual(len(meta["description"]), 60)
        self.assertNotIn("disable-model-invocation", meta)
        self.assertTrue(body.strip())
        for p in (ROOT / SKILL).rglob("*"):
            if p.is_file():
                self.assertNotRegex(p.read_text(), r"/home/|/workspace/|/tmp/")
        self.assertFalse(self.text("references/method.md").startswith("---"))

    def test_full_method_pointer_and_original_symptom_signal(self):
        require(self.text("SKILL.md"), (
            "If the required reference is missing or unreadable, report its path and stop the affected diagnosis.",
        ))
        require(self.text("references/method.md"), (
            "Read relevant accepted glossary definitions and ADRs; distinguish desired behavior from observed code.",
            "Build and run a symptom-specific red/green-capable feedback loop with available project tools.",
            "Assert the exact symptom, not merely absence of a crash.",
            "Improve loop speed, specificity, and determinism.",
            "Reproduce the actual reported failure and capture decisive evidence.",
            "Minimize where it reduces diagnostic uncertainty: remove one input, step, caller, or dependency at a time while preserving the same failure.",
        ))
        for option in ("unit", "integration", "e2e", "HTTP", "CLI", "browser", "trace replay", "harness", "property/fuzz", "bisection", "differential"):
            self.assertIn(option, self.text("references/method.md"))

    def test_secrets_scope_and_existing_native_guards_remain_binding(self):
        require(self.text("SKILL.md"), (
            "Keep all probes within existing scope, resource limits, operational permissions, and native safeguards.",
            "Redact credentials and PII before returning outputs or captured artifacts.",
            "Use protected input/data paths; do not expand secret environment values into commands or logs.",
        ))
        require(self.text("references/method.md"), (
            "Use available project tools instead of installing a new framework by default.",
            "Production instrumentation and load testing require their existing operational permission.",
            "Preserve the user's dirty tree; use an isolated authorized work area for destructive bisection.",
            "Tag temporary instrumentation for safe cleanup.",
            "If red is forced by a code or fixture mutation, compare with a pristine copy to verify that mutation first.",
        ))

    def test_coder_explicit_routing_and_validation_survive_renderer(self):
        template = (ROOT / "templates/roles/coder.SOUL.md.template").read_text()
        fields = role_fields(template, "coder")
        values = {key: "sample" for key in fields}
        output = render_role(template, values, "coder")
        self.assertEqual(output, re.sub(r"\{\{([A-Z0-9_]+)\}\}", lambda m: values[m[1]], template))
        require(output, (
            "For bug/diagnosis tasks, require the literal `$diagnosing-bugs` cue in each Codex task and resume, never as a shell variable.",
            "Pass the exact symptom, accepted context, and verification criteria; require the skill for unexplained failures or regressions emerging during implementation too.",
            "Validate diagnosis against the original symptom and actual evidence; do not automatically repeat the full method.",
            "The literal `$caveman` token belongs in every new Codex prompt, also after a restart or resume.",
            "Never use `kanban_complete` to close your own implementation.",
            "Preserve explicit customer financial/resource caps, configured limits, provider quotas, operational permissions, and native failure-loop guards.",
        ))
        self.assertNotIn("## Phase 1", template)
        for role in ("planner", "reviewer"):
            self.assertNotIn("$diagnosing-bugs", (ROOT / f"templates/roles/{role}.SOUL.md.template").read_text())

    def test_source_notice_and_full_mit_license(self):
        notice = self.text("NOTICE.md")
        require(notice, (REVISION, "https://github.com/mattpocock/skills",
                         "skills/engineering/diagnosing-bugs/SKILL.md", "agents/openai.yaml",
                         "scripts/hitl-loop.template.sh", "not automatic upstream synchronization"))
        license_text = self.text("LICENSE")
        require(license_text, ("Copyright (c) 2026 Matt Pocock", "Permission is hereby granted, free of charge",
                               "The above copyright notice and this permission notice shall be included",
                               'THE SOFTWARE IS PROVIDED "AS IS"', "SOFTWARE."))

    def test_delivery_loading_and_updates_use_existing_paths(self):
        for relative in ("references/setup.md", "references/native-workflow.md", "references/integrations.md",
                         "references/update.md", "references/verification.md", "references/upstream-sources.md"):
            with self.subTest(source=relative):
                self.assertIn("diagnosing-bugs", (ROOT / relative).read_text())
        recipe = (ROOT / "references/integrations.md").read_text()
        require(recipe, ("<CODEX_PROCESS_HOME>/.agents/skills/diagnosing-bugs/", "all resolved skill candidates",
                         "complete file sets and bytes", "native discovery", "references/method.md",
                         "After role delivery", "$diagnosing-bugs", "without a model call or bug experiment"))
        update = (ROOT / "references/update.md").read_text()
        require(update, ("New owned skills", "same existing whole-tree mapping", "legacy", "diagnosing-bugs",
                         "Read back its complete saved tree, unambiguous Codex discovery, and the Coder's explicit call policy separately.",
                         "Saved files and discovery do not establish actual diagnosis behavior."))

    def test_export_relative_links_and_contract_mutations(self):
        manifest = json.loads((ROOT / "manifest.json").read_text())
        with tempfile.TemporaryDirectory(prefix="maker-diagnosis-") as directory:
            export = Path(directory)
            for relative in manifest["files"] + ["manifest.json"]:
                target = export / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            delivery_contract(export)
            for path in (export / SKILL).rglob("*.md"):
                for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
                    if re.match(r"[a-z]+:", link):
                        continue
                    target = (path.parent / link).resolve()
                    self.assertTrue(target.is_relative_to((export / SKILL).resolve()), (path, link))
                    self.assertTrue(target.is_file(), (path, link))
            # Remove actual instructions with headings intact, then run the same contract.
            for scenario, (filename, clauses) in SCENARIOS.items():
                path = export / SKILL / filename
                original = path.read_text()
                for clause in clauses:
                    path.write_text(original.replace(clause, "", 1))
                    with self.subTest(scenario=scenario, removed=clause), self.assertRaisesRegex(AssertionError, "Missing operative instruction"):
                        scenario_contract(export, filename, clauses)
                path.write_text(original)
            path = export / "manifest.json"
            candidate = json.loads(path.read_text())
            candidate["own_skills"]["diagnosing-bugs"]["targets"] = {"hermes": ["coder"]}
            path.write_text(json.dumps(candidate))
            with self.assertRaisesRegex(AssertionError, "Wrong diagnosis consumer"):
                delivery_contract(export)
            path.write_text(json.dumps(manifest))
            (export / SKILL / "references/method.md").unlink()
            with self.assertRaisesRegex(AssertionError, "Incomplete diagnosis tree"):
                delivery_contract(export)


if __name__ == "__main__":
    unittest.main()
