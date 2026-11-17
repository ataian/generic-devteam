# Review: Docker development environment skill — `SPEC_2.9.1_Dev-Environment_v2.md`

**Verdict: CHANGES_REQUESTED**
**Reviewer:** Fujiko (independent document review, Kanban task `t_75ff0f1c`)
**Review round:** 1 — artifact lens (cold read of the deliverable, then comparison against the handoff narrative)
**Date:** 2026-11-17
**Scope:** document review only. No implementation, no profile change, no commit, no routing to Anjin. Mariko remains the author.

The design itself is sound and clearly better than v1: one Planner skill, two audience-specific guides, integrated Compose database, PostgreSQL branch templates, bounded runtime authority in all three SOULs. The required corrections are three narrow text defects — one unanchored role surface, one missing update surface with a verified test break, and one permission carve-out that exceeds the confirmed customer list.

---

## 1. Frozen inputs and hash comparison

Checked before review and re-checked immediately before delivery (2026-11-17T02:41+01:00):

| File | Recorded (frozen-inputs.json) | Observed | Result |
| --- | --- | --- | --- |
| `docs/SPEC_2.9.1_Dev-Environment_v2.md` | `c920b2d9…ac741dc` | `c920b2d9…ac741dc` | match |
| `templates/roles/coder.SOUL.md.template` | `f0fde663…7be80d` | `f0fde663…7be80d` | match |
| `templates/roles/reviewer.SOUL.md.template` | `a595fcba…ab2800` | `a595fcba…ab2800` | match |
| `templates/roles/planner.SOUL.md.template` | `769070f6…3bfc9` | `769070f6…3bfc9` | match |

No drift. `git rev-parse HEAD` in `/home/mariko/projects/generic-devteam` = `94ded22fa58b1c41956985c3edd562c443bae7af`, matching the baseline in the specification. `git status` shows only the two untracked discussion drafts. TAS checkout at `fe3a7d251518b793fedaec3041558c2840b4c796`, clean working tree. An empty Git diff is not used as evidence anywhere in this report.

## 2. What was verified positively

- **All six ALT blocks match exactly once at the stated source line** (regex extraction + occurrence count, script `check_alts.py`): R1 planner:12, R2 coder:77, R3 coder:24, R4 reviewer:86, R5 reviewer:43, R6 planner:104. Every replacement is reconciled in place; nothing is appended beside a superseded rule.
- **R1 preserves the single-source intent** that `test_brownfield_planning.py:155` protects: the replaced sentence survives as the narrowed "For other resources, …" rule instead of a second competing statement.
- **The proposed replacements, applied to a temporary copy, render coherent role texts** (`combined_{planner,coder,reviewer}.SOUL.md.template`, 144/121/124 lines): exactly one authority paragraph per role, the Reviewer still forbids self-implementation, `restart services` is gone, source-read-only and one-shot external-allowance rules survive.
- **Delivery mechanics named in section 5 exist and behave as claimed**: `references/update_team.py:259` iterates `manifest['own_skills']` and copies the complete tree from `git ls-tree` (so `targets.hermes = [planner]` alone is sufficient delivery); `references/setup.md:309` resolves skill copying through `upstream-sources.md#bundled-components`; the owned-skill schema (`status`, `targets`, `origin`, `changes`, `origin_ref`, `skill_path`, `transport`) fits a plain owned skill without a recipe.
- **Candidate static form** (independently re-checked, `check_skill_block.py`): valid frontmatter, `name: dev-environment` (15 chars, valid), description 49 chars, one fenced candidate block, no absolute paths, no project-specific identifiers inside the block, `AGENTS.md` ×3 and `HOWTO-human.md` ×1 in the intended author-only place.
- **Reachability of the guide chain** holds: root `AGENTS.md` pointer → `docker/dev/AGENTS.md` is read by Coder (template:16), Reviewer (template:21) and Planner (template:17); Team-Codex gets the path explicitly through R3 rather than relying on nested auto-loading, consistent with spec section 4.
- **No new approval gate is introduced**: step 3 of the skill routes implementation through the existing accepted-plan handoff; step 2 settles choices "through the existing planning process".

## 3. Blocking findings

### B1 — The Planner role row promises exact replacements that do not exist for two of its three additions

**Severity:** blocking (design precision, affects review question 4 and 6).
**Location:** `docs/SPEC_2.9.1_Dev-Environment_v2.md:227` (table row), `:236–238` (invocation clause), `:240–244` (ticket-authoring clause), `:252` (single-match discipline).

**Evidence.** R1 and R6 are the only anchored Planner replacements. The Planner invocation clause (`:238`) and the ticket-authoring clause (`:242`) are quoted proposals with no source anchor, no ALT block, no NEU block and no target line — yet the table claims "Exact replacements below" for the planner row, and `:409` promises "Every ALT block in R1–R6 matches its current role template exactly once at the stated source line".

**Concrete effect.** The implementer must choose the insertion point inside `planner.SOUL.md.template` without a recorded decision. Three competing homes exist: "Role and authority" (`:4–13`), "Planning workflow" step 7, which owns ticket-body structure (`:77`), and "Communication" (`:127–135`). Placement is behaviourally decisive: only `:77` makes the guide requirement bind ticket authoring; the same sentence in Communication is a style note. Requirement 28 ("skill, project instructions, role SOULs … must agree") then becomes unverifiable, because the Planner half of the agreement has no prescribed text position. This is the only row in the table whose verification column cannot be satisfied as written.

**ALT (`:227`):**

```text
| `templates/roles/planner.SOUL.md.template` | Add skill invocation and conditional guide use; distinguish assigned development operation from external approvals and include demo access in handoff. | Exact replacements below. |
```

**NEU:**

```text
| `templates/roles/planner.SOUL.md.template` | Add skill invocation (R7) and conditional ticket-guide requirement (R8); distinguish assigned development operation from external approvals and include demo access in handoff (R1, R6). | Exact replacements R1, R6, R7, R8 below; each ALT matches once at its stated line. |
```

plus two new anchored blocks in the same style, for example:

```text
#### R7: `templates/roles/planner.SOUL.md.template:33`

ALT:
   During grilling, load the owned `prototype` with `skill_view(name="prototype")` when a small interactive aid can clarify the customer's wishes or uncertainty.

NEU:
   During grilling, load the owned `prototype` with `skill_view(name="prototype")` when a small interactive aid can clarify the customer's wishes or uncertainty.
   When asked to create, adopt or revise a project's Docker development environment, load the owned `dev-environment` with `skill_view(name="dev-environment")`.

#### R8: `templates/roles/planner.SOUL.md.template:77`

ALT:
   Structure concise bullets as goal/context, acceptance criteria, technical implementation, verification, and dependencies plus exact plan/phase/commit binding.

NEU:
   Structure concise bullets as goal/context, acceptance criteria, technical implementation, verification, and dependencies plus exact plan/phase/commit binding.
   When the project already has a development environment, include its agent-guide path in each relevant ticket and require that guide for the ticket's builds, tests and development servers. Without an environment, omit the requirement; do not block ordinary work or require setup.
```

Both proposed anchors were checked against the current template: each matches exactly once (indentation omitted above; `check_r7_r8.py`). The author may pick another anchor, but the target line must be stated and must match once.

**Preserved requirements:** 19 (Planner makes the guide binding in relevant tickets; absence adds no blocker), 28 (agreement across surfaces), 4 of the review questions. **Implementation check:** `grep -c` each new ALT (exactly 1), render all three SOULs, and assert the guide clause appears under "Planning workflow" step 7 in the rendered Planner SOUL.

### B2 — The changeset surface list omits a test that R1 provably breaks

**Severity:** blocking (verified regression in the required package suite).
**Location:** `docs/SPEC_2.9.1_Dev-Environment_v2.md:232` (test surface row), broken assertion at `references/test_brownfield_planning.py:165`.

**Evidence.** `references/test_brownfield_planning.py:165` asserts the R1 ALT phrase word for word against `templates/roles/planner.SOUL.md.template`:

```python
"Do not infer permission to mutate a resource from permission to inspect it.",
...
    with self.subTest(soul_clause=soul_clause):
        self.assertIn(soul_clause, soul)
```

I ran the focused test at the frozen baseline: `python3 -B -m unittest test_brownfield_planning.BrownfieldPackageTests.test_plan_separates_binding_scope_from_coder_discretion` → `OK`. I then applied R1 exactly as specified to a temporary copy (`simulate_r1.py`): `assertIn` returns **False**. `templates/AGENTS.md:15` requires `python3 -B -m unittest discover -s references -p 'test_*.py'` before committing, and `:19` states that contract tests assert phrases word for word.

**Concrete effect.** An implementation that follows section 5 exactly leaves a red suite, and the cheapest visible repair is to revert R1's wording — which would undo the reconciliation the design needs. Section 8's "All existing Maker integration targets named in section 5 exist" is true but insufficient: existence is not coverage.

**ALT (`:232`):**

```text
| `references/test_render_reasoning.py`, `references/test_update_team.py` | Extend the exact role matrix and delivery/update coverage. | Existing tests enumerate own-skills targets and exercise manifest-driven mapping. |
```

**NEU:**

```text
| `references/test_render_reasoning.py`, `references/test_update_team.py`, `references/test_brownfield_planning.py` | Extend the exact role matrix and delivery/update coverage. Update the Planner clause in `test_plan_separates_binding_scope_from_coder_discretion:165` to the R1 NEU wording; keep the `assertNotIn` check on the brownfield skill unchanged. | Existing tests enumerate own-skills targets and exercise manifest-driven mapping; `test_brownfield_planning.py:165` currently pins the R1 ALT phrase word for word and fails after R1. |
```

**Preserved requirements:** TAS single-source-of-truth for role boundaries (the test exists to keep that rule out of the planning skill), `AGENTS.md:15/19`. **Implementation check:** run the full suite after applying R1–R8; `test_brownfield_planning` must stay green and `assertNotIn` must still pass.

### B3 — R4 grants the Reviewer an in-environment deployment permission the customer did not confirm

**Severity:** blocking (permission widening in a role template; review question 3 explicitly asks for deployment clauses).
**Location:** `docs/SPEC_2.9.1_Dev-Environment_v2.md:312` (ALT) → `:319` (NEU); source `templates/roles/reviewer.SOUL.md.template:86`.

**Evidence.** The original prohibition is a flat list: "Do not push, deploy, restart services, or change host configuration from a review task." R4 correctly removes `restart services` (now covered by assigned-runtime authority) but additionally rewrites `deploy` into `deploy outside the assigned development environment`. No other role or skill surface makes that distinction.

**Concrete effect.** Two problems, both practical. (a) It infers a permission from a prohibition's scope: deploying into the development environment becomes allowed by implication, although the confirmed list (requirement 26) names only start, stop, restart, rebuild, recreate and disposable-state reset. (b) It contradicts the same paragraph's own classification, "Local test and demo runs are development operations, not publication or deployment" (`:318`): if such runs are not deployment, the carve-out has no referent and only creates room for a Reviewer to claim deploy authority. Minimal-change discipline gives the smaller, correct diff: delete only the removed operation, leave `deploy` prohibited.

**ALT (`:319`):**

```text
- Never self-implement, self-approve, or extend product scope. Do not push, deploy outside the assigned development environment, operate unrelated services, or change host configuration from a review task.
```

**NEU:**

```text
- Never self-implement, self-approve, or extend product scope. Do not push or deploy, operate unrelated services, or change host configuration from a review task. Operating assigned development services is permitted only under the authority above.
```

**Preserved requirements:** 26 (enumerated runtime operations), 27 (demo access without claiming deployment), Reviewer independence and no-self-repair; external publication/deployment gates stay closed. **Implementation check:** grep the rendered Reviewer SOUL for `deploy` and assert the only occurrence is the prohibition; grep for `restart services` and assert zero occurrences.

## 4. Nonblocking recommendations

**N1 — R6's "Name only what deviated" now excludes what the same bullet requires.**
`:345`/`:351`. The bullet orders "Name only what deviated from the plan: …" and then mandates the demo URL. An agent compressing the report can legitimately read the URL as prohibited content. Add a scope separator: `… and include demo access in the handoff.` → `Beyond that, for a running customer demonstration, include the verified browser URL and concrete SSH local-forward command when needed; disclose any untested client-side access.` Effect: keeps the compression rule and the new obligation in separate scopes.

**N2 — The synthetic-data permission is stated three times in the candidate.**
`:105` ("The team may generate synthetic data and reset disposable development state…"), `:124` ("The team may generate synthetic data for development, tests and demonstrations."), `:173` ("Synthetic seed data may be generated by the team."). One permission, three authorities; step 2's copy also reads as a contract-stage precondition that the scope rule does not have. Keep `:105` as the single permission and reduce step 2 to `For PostgreSQL, establish the template's initialization and permitted data source; operational data requires a separate explicit authorization.`, and drop the sentence at `:173`.

**N3 — `check_candidate_skill.py` is unreproducible evidence.**
`:408`. The named checker is not present in the Maker package, the TAS checkout, or anywhere under `/home/mariko/projects` (`find` over the tree). The claim is a claim. I re-verified its five content items independently (§2) and they hold; the report should either name the script's path or inline the checks so the next reader can repeat them.

**N4 — The draft's own boundary sentence reads against its container authority.**
`:31` — "This draft does not authorize changes to SG1, another team profile, containers, host configuration, publication or deployment." A draft that proposes container lifecycle authority for the team should say what it means: `This draft is a proposal: it grants no installation, host or profile change, publication or deployment.` Nonblocking, but it is the kind of sentence a reader quotes out of context.

**N5 — The shared authority paragraph has no agreement guard.**
`:252` justifies the identical paragraph in R1, R2, R4 (verified byte-identical in the combined copies). Requirement 28 makes their agreement a customer requirement, and section 5 proposes no test for it. A static test asserting the paragraph is identical across the three templates is cheap and survives later edits. Nonblocking.

**N6 — Step 2 does not name the existing clarification path.**
`:120` "discuss unresolved stack choices and development/test needs with the customer" versus `planner.SOUL.md.template:31` (grilling is mandatory per new plan; "do not substitute a self-made interview"). The skill can be read as authorizing a parallel interview route. Name the existing path: `settle unresolved stack choices through the existing customer clarification path`.

**N7 — `Select the branch` is overloaded (nit).**
`:130` uses "branch" for a construction decision path while `:182` uses it for Git branches and `:170` for PostgreSQL branch databases. `Choose the construction path` removes the ambiguity without changing behaviour.

**N8 — Two terms for one actor (nit).**
`:137` "Have the Coder/Team-Codex implement"; `:142` "Have the implementation team produce both documents". Use `Coder/Team-Codex` in both.

## 5. Evidence limits

- **No execution evidence of the design**: no Docker build, container, PostgreSQL clone, generated team or live agent behaviour was exercised — correctly out of scope per the assignment, but it means this report says nothing about whether the environment skill works.
- **Full package suite not run**: `python3 -B -m unittest discover -s references -p "test_*.py"` exceeded the 180 s terminal window. Only the one affected test was executed (green at baseline). Baseline greenness of the whole suite is inferred from `templates/AGENTS.md:15`, not measured here; irrelevant to B2, whose assertion was reproduced directly.
- **v1→v2 claims not verifiable**: both drafts are untracked, so "the uncommitted first discussion draft is retained unchanged" and "the v1-to-v2 diff was inspected" cannot be checked against a recorded baseline.
- **Section 8 self-review and the earlier "independent read-only text review"** are treated as claims, as the assignment requires. Section 6's SG1/MTB source inspection was not repeated; those files are not requirements for this review.
- **No external helper was used**; the whole pass is a single independent read plus scripted checks.

## 6. Requirement coverage

| Customer requirement (assignment §"Confirmed customer requirements") | Where satisfied | Status |
| --- | --- | --- |
| 1 Planner construction/adoption skill; Coder implements; Reviewer checks | §5 table, skill steps 4/6, R1–R3 | met |
| 2 Host agents/Git/Docker on Linux; toolchains in reusable containers | skill Prerequisites, Construction criteria Toolchain/Reuse, acceptance Reuse | met |
| 3 Compact `docker/dev/AGENTS.md` + standalone `HOWTO-human.md`; root pointer; no human-guide pointer in agent instructions | step 5, §4, acceptance Audience separation | met |
| 4 DB engine inside the development Compose project; no MTB external Compose as the design | Construction criteria Database, `:380`, adopt path `:132` | met (external-DB adoption path is a bounded exception worth one sentence to Max) |
| 5 PostgreSQL template cloning per branch, reuse, template preserved, target verified before writes | PG section steps 1–4, acceptance PostgreSQL branches | met |
| 6 Synthetic data allowed; template data source is project contract; no implicit operational import | `:25`, skill step 2, PG step 1 | met (see N2) |
| 7 Third-party services/simulator construction excluded | `:25`, `:29`, `:35`, skill Prerequisites | met |
| 8 Runtime autonomy without repeated permission; source/data/host boundaries preserved | Operating scope, R1/R2/R4, acceptance Runtime autonomy | met |
| 9 Demo may be left running with real URL and SSH forward; no untested client claim | step 6, R6, acceptance Demonstration | met (see N1) |
| 10 Skill, project instructions, role SOULs, Team-Codex handoff, helper permissions agree; missing environment blocks nothing | R1–R5, R3 handoff, `:361`, `:395` | met (see B1, N5) |
| — Additional gates or framework machinery | §2 rejected alternatives | none added |

## 7. TAS assessment of the proposed instruction text

- **Actor / action / condition / outcome**: satisfied. Every procedure step carries a checkable `Done:` criterion; acceptance cases carry decisive negative anchors ("a version command, running container or skipped test is not that evidence").
- **Placement**: correct in principle — role authority in the SOULs, procedures and acceptance in the skill, repository specifics in the project guide. The Planner additions are the one placement that is not pinned (B1).
- **Single source of truth**: one violation (N2); the role-paragraph repetition is justified at `:252` and needs only an agreement guard (N5).
- **Contradiction check**: one residual internal contradiction (N1) and one authority widening (B3). Nothing else surfaced in the combined role texts.
- **Pointers**: all required targets are named with a trigger and a reachable path; the root pointer requires the read rather than offering a link.
- **Scope discipline**: the design rejects the generator/wrapper alternative and keeps MTB mechanisms out; it correctly leaves versions, ports, service names and test harness to the team.

## 8. Verdict

**CHANGES_REQUESTED** — the design is approvable, but three text defects must be corrected before implementation planning, because each of them would otherwise be inherited by the implementation changeset:

1. **B1** anchor the two new Planner clauses as R7/R8 (or state their exact target lines) and stop claiming exact replacements that do not exist.
2. **B2** add `references/test_brownfield_planning.py` to the update surfaces and update its Planner assertion to the R1 wording.
3. **B3** keep `deploy` prohibited for the Reviewer; remove only `restart services`.

N1–N8 are recommended, not required. Nothing here questions the design direction; no additional test infrastructure, no executed Docker scenarios and no project-specific Compose files were demanded.

---

## Kurzfazit für Max (Deutsch)

Der Entwurf v2 ist inhaltlich gut: ein Planner-Skill, zwei getrennte Anleitungen, Datenbank im Entwicklungs-Compose, PostgreSQL-Branch-Klone, klare Laufzeit-Befugnis in allen drei Rollen. Keine neuen Genehmigungsrunden, kein unnötiges Framework. Alle vier Eingabedateien sind hashgleich geblieben, alle sechs Ersetzungsblöcke passen genau einmal an der genannten Zeile.

Drei Punkte müssen vor der Umsetzungsplanung nachgebessert werden. Erstens: Die Planner-Zeile in Abschnitt 5 verspricht exakte Ersetzungen, aber zwei der drei Planner-Regeln (Skill-Aufruf, Guide-Pflicht im Ticket) haben keinen Anker und keine Zeilenangabe — der Umsetzer müsste selbst raten, wo sie hingehören. Zweitens: Der vorhandene Pakettest `test_brownfield_planning.py:165` prüft den Planner-Satz wortgleich; nach R1 schlägt er fehl — die Datei fehlt in der Änderungsliste. Nachgestellt: Test vorher grün, nach R1 rot. Drittens: R4 erlaubt dem Reviewer beim Umbau "deploy outside the assigned development environment" — damit wäre Einsatz in die Entwicklungsumgebung stillschweigend erlaubt, obwohl die Kundenliste das nicht nennt und derselbe Absatz lokale Läufe ausdrücklich nicht als Deployment zählt.

Urteil: CHANGES_REQUESTED, aber nur wegen dieser drei Textstellen. Restliche Hinweise (doppelte Synthetic-Data-Regel, "Name only what deviated" versus Demo-URL, nicht nachprüfbarer `check_candidate_skill.py`, Abschnitt-31-Formulierung) sind Empfehlungen.

*Reviewed by Fujiko — report delivered; specification verdict kept separate from card completion.*
