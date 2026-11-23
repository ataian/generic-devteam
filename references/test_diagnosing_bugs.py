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
        "Use direct fix only if concrete evidence supports both symptom and cause, the affected flow and required "
        "correction are clear, and a focused test or reproducible check can demonstrate the exact bug and its "
        "correction.",
        "Demonstrate the error, fix the cause, then verify.",
        "Verify resolution of the original symptom and passing required regression, acceptance and risk checks.",
        "Do not generate alternatives, build a separate harness, or further minimize an already simple case to satisfy a checklist.",
    )),
    "first targeted investigation leaves two competing causes": ("SKILL.md", (
        "Cause still unclear after the initial investigation, or plausible causes need distinguishing.",
        "Switch before attempting guessed fixes, as soon as uncertainty is evident or any trigger applies:",
        "Read [the full method](references/method.md) completely.",
    )),
    "intermittent state/timing/environment failure": ("SKILL.md", (
        "Intermittent failure or dependence on state, timing or environment.",
    )),
    "performance regression": ("SKILL.md", (
        "Performance regression requiring measurement and isolation.",
    )),
    "apparent fix leaves symptom or bug recurs": ("SKILL.md", (
        "Original symptom survives an apparent fix or recurs.",
        "Reuse completed investigation, repros and checks.",
        "Deepening within accepted scope requires no new Planner or customer approval.",
    )),
    "ordinary implementation develops unexplained test regression": ("SKILL.md", (
        "Trigger: bug or diagnosis task, or an unexplained test failure or regression during ordinary implementation.",
    )),
    "clear cause but material security/data-integrity risk": ("SKILL.md", (
        "Both paths retain required security, data-integrity, acceptance and independent-review checks.",
        "Risk alone does not require extended cause exploration. Ticket and diff size do not select the path.",
    )),
    "handoff with a required check unavailable": ("SKILL.md", (
        "Use compact bullets within task conventions.",
        "Cause: confirmed cause, if established.",
        "Checked: meaningful verification and retrievable original evidence.",
        "Open: remaining uncertainty and any failed, unavailable, or incomplete required checks with their consequences.",
        "Keep the existing handoff and independent review.",
        "No separate diagnosis dossier is required.",
    )),
    "ambiguous cause needs discriminating probes": ("references/method.md", (
        "Remaining ambiguity: rank competing falsifiable hypotheses by evidence and state each prediction.",
        "Probe to distinguish predictions, changing one variable at a time.",
        "Prefer a debugger or REPL, then targeted boundary instrumentation, over indiscriminate logging.",
        "Ask through existing routing only for needed customer knowledge, decisions or permissions.",
    )),
    "rare failure and slow necessary integration check": ("references/method.md", (
        "Intermittent failure: record reproduction rates and controlled conditions before and after the fix.",
        "A single green run is insufficient,",
        "Aim for seconds while keeping necessary slow integration checks.",
        "Performance: establish a baseline and measure/profile, compare or bisect before claiming cause or "
        "improvement.",
    )),
    "no loop; protected production artifact required": ("references/method.md", (
        "No reproducible loop: report attempts and missing evidence. Use provisional hypotheses only to guide safe "
        "evidence collection.",
        "Claims of confirmed cause or fix require supporting evidence.",
        "Request required environment/access, redacted artifacts or production-instrumentation permission through "
        "existing routing.",
        "Missing reproduction grants no additional access or operational authority.",
    )),
    "chain bug cannot be locked down by single-caller test": ("references/method.md", (
        "at a seam that exercises the real failure, including multi-caller or chain behavior as needed.",
        "\n2. Run the regression red before fixing the evidenced cause within scope, then green afterward.",
        "\n3. Rerun the original unminimized scenario.",
        "Document any missing suitable seam or required access precisely. Keep explicit acceptance and safety checks.",
        "A missing seam gives no waiver or authority to redesign architecture.",
    )),
    "human reproduction and task-owned cleanup": ("references/method.md", (
        "Use human-assisted repro only as a necessary last resort, through existing communication and "
        "protected-input facilities.",
        "Never collect passwords or tokens as observations.",
        "Remove only task-owned temporary artifacts and instrumentation within existing ownership and approval limits.",
        "any useful repro as regression coverage or in a clearly designated debug area when justified.",
        "Use existing commit, handoff or task conventions for confirmed cause and meaningful verification.",
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
            "If missing or unreadable, report its path and stop the affected diagnosis.",
        ))
        require(self.text("references/method.md"), (
            "Read relevant accepted glossary definitions and ADRs. Distinguish required behavior from observed code.",
            "Build and run a red/green feedback loop for the exact symptom. Use existing project tools by default.",
            "A no-crash assertion alone is insufficient.",
            "Improve speed, specificity and determinism.",
            "Reproduce the reported failure and capture decisive evidence.",
            "Minimize only where it reduces diagnostic uncertainty. Remove one input, step, caller or dependency "
            "at a time while preserving the same failure.",
        ))
        for option in ("unit", "integration", "e2e", "HTTP", "CLI", "browser", "trace replay", "harness", "property/fuzz", "bisection", "differential"):
            self.assertIn(option, self.text("references/method.md"))

    def test_secrets_scope_and_existing_native_guards_remain_binding(self):
        require(self.text("SKILL.md"), (
            "Probes: stay within scope, resource limits, operational permissions and native safeguards.",
            "Redact credentials and PII before returning output or captured artifacts.",
            "Data: use protected input/data paths. Never expand secret environment values into commands or logs.",
        ))
        require(self.text("references/method.md"), (
            "Use existing project tools by default.",
            "Production instrumentation and load testing require existing operational permission.",
            "Preserve the user's dirty tree. Use an isolated authorized work area for destructive bisection.",
            "Tag temporary instrumentation for safe cleanup.",
            "If a code or fixture mutation forces red, first compare it with a pristine copy to verify the mutation.",
        ))

    def test_coder_explicit_routing_and_validation_survive_renderer(self):
        template = (ROOT / "templates/roles/coder.SOUL.md.template").read_text()
        fields = role_fields(template, "coder")
        values = {key: "sample" for key in fields}
        values.update(CODEX_BINARY="/fixture/bin/codex", CODEX_PROCESS_HOME="/fixture/process-home",
                      CODEX_HOME="/fixture/codex-home")
        output = render_role(template, values, "coder")
        self.assertEqual(output, re.sub(r"\{\{([A-Z0-9_]+)\}\}", lambda m: values[m[1]], template))
        require(output, (
            "For bug/diagnosis tasks, require the literal `$diagnosing-bugs` cue in each Codex task and resume, never as a shell variable.",
            "Pass the exact symptom, accepted context, and verification criteria; require the skill for unexplained failures or regressions emerging during implementation too.",
            "Validate diagnosis against the original symptom and actual evidence; do not automatically repeat the full method.",
            "On restart or resume, include current state, relevant delta, remaining work and standing constraints.",
            "In every actual task, restart and resume prompt, require a compact result: `Change:` outcome, "
            "`Checked:` actual result, checked state and decisive evidence, `Open:` failures, unrun checks and material limits.",
            "Never use `kanban_complete` to close your own implementation.",
            "Preserve explicit customer financial/resource caps, configured limits, provider quotas, operational permissions, and native failure-loop guards.",
        ))
        self.assertNotIn("$caveman", output)
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
