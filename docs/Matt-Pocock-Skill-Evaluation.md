# Matt Pocock skills: Maker evaluation

## Scope and result

Static source assessment. No skills installed, foreign scripts executed, role templates changed, or live teams updated.

Upstream checkout: `/home/mariko/archive/mattpocock-evaluation-20261112/skills`.
Inspected upstream commit: `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.
Maker baseline: current local working tree in `/home/mariko/projects/generic-devteam`, branch `v3`, based on `fcdfdde37a6400ee57cf5aa15577155a4339438b`, with pre-existing local changes. This is not a claim about an untouched released Maker or installed live Planner profiles.

The collection contains **39 skills**: 20 Engineering, 7 Productivity, 8 In-progress, and 4 Misc. The plugin manifest lists exactly the 27 Engineering/Productivity skills. The other 12 were assessed too; they are not silently treated as promoted plugin assets.[41] In-progress is explicitly beta in `skills/in-progress/README.md`. Misc is explicitly frozen and unmaintained.[42]

**Recommendation:** retain Maker's role boundaries and native dispatcher. Add domain modelling to the existing Planner interview. Select a few standalone upstream helpers. Adapt useful diagnosis, design, testing, and review ideas into their existing owners rather than importing a competing development process. No wholesale replacement is justified by this source comparison.

Benefits below are reasoned integration judgments, not measured improvements in runtime quality, cost, or token use.

## 1. Current grilling versus upstream

Maker's `manifest.json`, `upstream_components.grill-me.source_revision`, already points at the exact inspected upstream HEAD. Both `grilling/SKILL.md` and `grill-me/SKILL.md` match that pinned Git object byte-for-byte. There is no upstream revision delta to apply.

The Planner template already requires the original `grilling` for every new plan, gives it precedence for requirement clarification, retains Superpowers for design/approval, and uses Brownfield planning for source analysis. See `templates/roles/planner.SOUL.md.template:26–35` and `references/integrations.md:189–216`.

| Current upstream behaviour | Maker assessment |
|---|---|
| Design tree; ask the full currently answerable frontier together | Already supplied by the mandatory original skill.[34] |
| Defer questions whose answers depend on unresolved prerequisites | Already supplied.[34] |
| Number questions, recommend answers, make yes accept the recommendation | Already supplied. Preserve required native question interfaces and existing role communication rules.[34] |
| Research facts in fresh-context helpers; continue independent questions meanwhile | Already supplied; not a new implementation role.[34] |
| Finish when the frontier is empty and the customer confirms shared understanding | Already supplied. Shared understanding is not acceptance of the later implementation plan.[34] |
| Actively sharpen domain terms and maintain glossary/ADRs | Not part of `grilling`; this is the meaningful addition.[5] |

This verifies the Maker source recipe, not whether every installed Planner currently has the required files or loads them effectively.

## 2. Proposed domain-model integration

Matt already provides the exact conceptual composition: `grill-with-docs` calls `grilling` and `domain-modeling`. It is a seven-line router, not a separate interview methodology.[6]

### Smallest useful change

1. Keep the current Planner entry and original `grilling`. Add the complete original `domain-modeling` tree to the Planner's assigned upstream assets. Preserve `GLOSSARY-FORMAT.md`, `ADR-FORMAT.md`, metadata and applicable licensing. Use the same explicitly selected upstream commit.
2. Extend the existing interview with active domain modelling when terms, relationships, or consequential model decisions need clarification. Loading it alongside the interview is sufficient; a separate required `grill-with-docs` invocation adds no capability. Offer that router only if a human-facing command is useful.
3. Read existing glossary/context-map and ADR conventions before proposing document locations. Challenge overloaded terms, compare assertions with actual code, and test boundaries with concrete scenarios. Separate observed behaviour from desired behaviour.[5]
4. Capture resolved terms immediately in the authorized planning document area. Create documents lazily. Keep the glossary strictly about domain vocabulary: concise definitions and avoided synonyms, not implementation or acceptance requirements.[5]
5. Offer an ADR only when the decision is hard to reverse, surprising without context, and the result of a real trade-off. Mark an unaccepted decision as proposed; do not turn a drafted ADR into customer acceptance.[5]
6. Keep requirements, scope, acceptance criteria and phase gates in the versioned accepted plan. Bind related glossary/ADR state to the handoff baseline. Coder and Reviewer consume that language; a glossary is not an independent executable specification.
7. Preserve the current customer/Planner/Coder authority split. Domain questions belong in the interview; ordinary in-scope implementation choices remain with the Coder. No second approval ceremony, dispatcher, tracker, or mandatory document bundle.

### Ownership

- **Planner:** active domain clarification and authorized glossary/ADR maintenance during planning.
- **Hermes-Coder / Team-Codex:** use accepted vocabulary; surface contradictions through existing Coder → Planner routing. No silent product-model rewrite.
- **Independent Reviewer:** read relevant accepted definitions and decisions, verify implementation against requirements, return contradictions through the Coder. Do not invoke a mutating domain-document workflow from the read-only role.

### Likely Maker change locations, not an implementation plan

`manifest.json`; `references/upstream-sources.md`; `references/integrations.md`; `templates/roles/planner.SOUL.md.template`; targeted pointers in `skills/brownfield-feature-planning/SKILL.md`; relevant verification/tests and user-facing documentation.

Only add consumer pointers to Coder/Reviewer where needed. Do not duplicate the domain-modelling procedure across SOUL templates. A package edit and live-team rollout remain separate work.

## 3. Role shortlist

**Modes:** Upstream = candidate for unchanged selective acquisition plus explicit role integration; Improve = transfer useful ideas into our existing method; Conditional = only for a separately commissioned task. These are recommendations, not installations.

| Owner | Skill | Mode | Small reason |
|---|---|---|---|
| Planner | `domain-modeling` | Upstream, high priority | Turns ambiguous business language into shared, durable definitions.[5] |
| Planner | `to-questionnaire` | Upstream, optional | Gets missing answers from an absent domain expert without grilling the wrong person.[37] |
| Planner | `to-tickets` | Improve | Demoable vertical outcomes and expand–migrate–contract; retain native Maker release gates.[17] |
| Planner | `codebase-design` | Improve | Evaluate complexity hidden by an interface and locality of changes; avoid imposing a new global vocabulary.[3] |
| Planner | `improve-codebase-architecture` | Conditional | Useful candidate survey for an actual architecture assignment, not another feature-planning gate.[9] |
| Planner | `retro` | Improve | Distinguish missing/wired-badly automation from judgment rules; retain existing retrospective ownership.[13] |
| Hermes-Coder | `diagnosing-bugs` | Improve, primarily through Team-Codex | Ask for a symptom-specific reproduction and verify the original scenario after the fix.[4] |
| Hermes-Coder | `handoff` | Upstream, optional | Useful for genuine session transfer; not an extra report for every ticket.[35] |
| Team-Codex | `diagnosing-bugs` | Improve, high priority | Tight feedback loop, minimized repro, falsifiable hypotheses and targeted probes.[4] |
| Team-Codex | `tdd` | Improve | Independent expected values and small red/green slices; avoid categorical restrictions on necessary tests.[15] |
| Team-Codex | `prototype` | Conditional | A clickable state-model demo can resolve a specific design uncertainty.[11] |
| Team-Codex / authorized PR author | `pr` | Upstream, optional | Compact before/after evidence, reversibility and blast radius.[10] |
| Independent Reviewer | `code-review` | Improve | Separate requirements compliance from standards compliance; not a replacement for `sdlc-review`.[2] |
| Independent Reviewer | `tdd` | Improve, test-quality lens only | Check whether assertions can disagree with the implementation, not merely repeat it.[15] |
| Maker maintainer, not a new team role | `writing-for-agents` | Upstream reference, high priority | Better trigger pointers, information hierarchy and completion criteria complement TAS.[39] |
| Maker maintainer | `retro`, `software-factory` | Improve / reference only | Environment failure analysis and orchestration questions; no competing runtime model.[13][25] |

No new general-purpose skill is needed for the Hermes-Coder merely to duplicate its existing orchestration duties. No candidate establishes a reason to replace Brownfield planning, native Kanban, the Codex launcher, independent `sdlc-review`, or the existing TAS authority/evidence contracts.

## 4. Complete inventory and dispositions

### Engineering — 20 skills

| Skill | Decision | Reason / integration limit |
|---|---|---|
| `ask-matt` | Skip | Routes among Matt's own workflows, not Maker's fixed owners and process.[1] |
| `code-review` | Improve Reviewer | Two useful axes; its report aggregation is not Maker's independent evidence-backed verdict or native transitions.[2] |
| `codebase-design` | Improve Planner / Team-Codex | Useful depth/interface/locality heuristics. Original vocabulary mandates and companion test-deletion guidance are not safe global defaults.[3] |
| `diagnosing-bugs` | Improve Team-Codex, supervised by Coder | Strong reproduction/minimization discipline. Original hard prerequisites and fixed hypothesis count are too rigid for universal use.[4] |
| `domain-modeling` | Upstream Planner addition | Primary recommendation; agree document authority/location and retain original companion formats.[5] |
| `grill-with-docs` | Optional explicit entry only | Merely composes the two primitives; unnecessary as another required phase.[6] |
| `implement` | Skip | Thin duplicate of existing implementation/testing/review orchestration.[7] |
| `implement-spec` | Skip | Adds integration-branch/worktree/frontier workers and its own completion mechanism, conflicting with Maker ownership and gates.[8] |
| `improve-codebase-architecture` | Conditional Planner survey | New evaluation lens, not a new graph engine. Only for an explicit architecture task; brings additional dependencies/reporting.[9] |
| `pr` | Optional upstream helper | Useful PR-body template. Repository-specific template and publication permissions remain binding.[10] |
| `prototype` | Conditional Team-Codex assignment | Strong interactive logic/state exploration. Isolate throwaway work; production adoption still requires normal implementation and review.[11] |
| `research` | Optional, low priority | Clean primary-source/cited-file helper; adds little beyond existing factual investigation and delegation.[12] |
| `retro` | Improve existing retrospective | Good automation-versus-judgment distinction. Reject the claim that independent review needs no exploration.[13] |
| `setup-matt-pocock-skills` | Skip | Would introduce another tracker/label/agent-document configuration system instead of Maker's bindings.[14] |
| `tdd` | Improve implementation and test review | Keep independent expected values and real red/green evidence; not blanket customer approval for each test seam or a ban on internal/persistence checks.[15] |
| `to-spec` | Improve synthesis only | Reuse decided requirements without reinterview. Original tracker publication, label release and omission of file paths do not fit Maker handoff.[16] |
| `to-tickets` | Improve current phase planning | Demoable slices and expand–contract are useful; do not copy acceptance criteria into competing cards or bypass independent gates.[17] |
| `triage` | Skip as team default | External backlog classification is not Maker's blocked-work recovery. A second label/state machine is not needed.[18] |
| `wayfinder` | Ideas only, no workflow import | Useful distinction between concrete questions and unformulated uncertainty; its maps, ticket types and execution/publication paths compete with Maker.[19] |
| `wizard` | Improve operator guidance only | Human-only steps are useful; template secret handling and external-write verification need review before any real adoption.[20] |

### Productivity — 7 skills

| Skill | Decision | Reason / integration limit |
|---|---|---|
| `grill-me` | Keep existing upstream | Explicit wrapper already supplied by Maker; no new interview capability.[33] |
| `grilling` | Keep existing upstream | Current source already pinned; retains frontier/rounds/factual-investigation discipline.[34] |
| `handoff` | Optional upstream helper | Reference existing artifacts and redact sensitive data. Not another mandatory Kanban report or a channel for biasing the independent fresh-context pass.[35] |
| `teach` | Separate training work only | Maintains a teaching workspace; not a development role capability.[36] |
| `to-questionnaire` | Optional upstream Planner helper | Useful for missing external expertise; creation is not authorization to send.[37] |
| `wait-what` | Optional human command, low priority | Re-explanation convenience, not new domain capability. Its ASD-STE100 instruction is not a replacement for TAS.[38] |
| `writing-for-agents` | Upstream maintainer reference | Complements TAS with pointer, hierarchy and completion design. Include `SKILL-MECHANICS.md`; verify harness-specific invocation semantics separately.[39] |

### In-progress — 8 skills

These are beta source material, not promoted plugin assets; do not count them as stable default dependencies.[41]

| Skill | Decision | Reason / integration limit |
|---|---|---|
| `chief-of-staff` | Skip | Proactive environment/process changes and alternate implementation steering exceed the Planner mandate.[21] |
| `claude-handoff` | Skip | Starts a Claude-specific background workflow; generic handoff already covers the transferable need.[22] |
| `loop-me` | Conditional workflow-design reference | Trigger/checkpoint/brief questions can help a commissioned workflow redesign; not a substitute for approved plans.[23] |
| `setup-ts-deep-modules` | Conditional TS project work | Enforceable import boundaries may be useful, but package structure, dependencies, checks and tests are substantial project changes.[24] |
| `software-factory` | Maintainer reference only | Useful orchestration questions; its runner, memory and PR/human-merge model are not the Hermes-Kanban/Hindsight contract.[25] |
| `writing-beats` | Skip for Maker | Interactive article composition, not development coordination.[26] |
| `writing-fragments` | Skip for Maker | Raw editorial fragments, not accepted requirements or durable evidence.[27] |
| `writing-shape` | Skip for Maker | Paragraph-by-paragraph article shaping adds an unrelated authoring workflow.[28] |

### Misc — 4 skills

Upstream explicitly freezes this bucket and declines its maintenance requests.[42]

| Skill | Decision | Reason / integration limit |
|---|---|---|
| `git-guardrails-claude-code` | Skip | Claude Bash-hook implementation, not a verified Hermes/Codex safety boundary.[29] |
| `migrate-to-shoehorn` | Specific TS migration only | Library-specific test migration, not a general role addition.[30] |
| `scaffold-exercises` | Skip for Maker | Course/exercise project conventions, not the team workflow.[31] |
| `setup-pre-commit` | Specific repo task only | Prescribes a particular JS toolchain; prefer existing repository checks and explicit project need.[32] |

## 5. Important conflicts and non-goals

- **Read-only Reviewer:** consume glossary/ADRs; do not give this role an active document-mutating domain workflow.
- **Test policy:** `tdd` restricts tests to customer-approved public seams and excludes direct persistence checks. `codebase-design/DEEPENING.md` permits internal seams but also directs deletion of old shallow unit tests. Adopt useful ideas, not categorical loss of risk-based coverage.[15][3]
- **Review quality:** the two-axis split does not replace source/caller inspection, runtime evidence, high-risk fresh-context checks or exact-commit approval.[2]
- **Planning versus release:** `to-spec` publishes `ready-for-agent` immediately; `implement-spec` owns a competing task graph. Neither replaces accepted plans and native Maker transitions.[16][8]
- **Upstream means unchanged source:** keep our integration rules separate. If useful content requires removing contradictory upstream mandates, classify it as an improvement to our method, not an unchanged upstream installation.
- **No automatic maintenance:** `retro` and maintainer references remain explicitly commissioned work, not a new learning daemon or recurring repair mandate.[13]
- **No full plugin import, no second tracker setup, no live profile rollout, no platform repair, no pushes or deployments.**

## Verification and adoption boundary

Verified here: upstream checkout revision; equality with the Maker grill pin and selected Git-object bytes; complete 39-skill inventory; plugin membership; current Maker source role contracts; full skill-text review split across three independent workstreams, with substantive companion review and parent checks of material recommendations.

Not verified here: live Planner delivery/loading, end-to-end skill behaviour, installer behaviour, improved engineering outcomes, native discovery of new candidates, or safe runtime execution of bundled scripts.

No installation commands are proposed by this assessment. A later adoption scope must name exact assets, target harness/profile, native discovery checks, permissions, and a backup-backed per-target rollback before any installation. Existing Maker and live-team files are unchanged by this report.

## Sources

[1] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/ask-matt/SKILL.md — ask-matt
[2] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/code-review/SKILL.md — code-review
[3] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/codebase-design/SKILL.md — codebase-design
[4] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/diagnosing-bugs/SKILL.md — diagnosing-bugs
[5] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/domain-modeling/SKILL.md — domain-modeling
[6] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/grill-with-docs/SKILL.md — grill-with-docs
[7] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/implement/SKILL.md — implement
[8] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/implement-spec/SKILL.md — implement-spec
[9] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/improve-codebase-architecture/SKILL.md — improve-codebase-architecture
[10] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/pr/SKILL.md — pr
[11] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/prototype/SKILL.md — prototype
[12] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/research/SKILL.md — research
[13] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/retro/SKILL.md — retro
[14] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/setup-matt-pocock-skills/SKILL.md — setup-matt-pocock-skills
[15] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/tdd/SKILL.md — tdd
[16] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/to-spec/SKILL.md — to-spec
[17] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/to-tickets/SKILL.md — to-tickets
[18] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/triage/SKILL.md — triage
[19] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/wayfinder/SKILL.md — wayfinder
[20] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/wizard/SKILL.md — wizard
[21] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/chief-of-staff/SKILL.md — chief-of-staff
[22] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/claude-handoff/SKILL.md — claude-handoff
[23] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/loop-me/SKILL.md — loop-me
[24] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/setup-ts-deep-modules/SKILL.md — setup-ts-deep-modules
[25] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/software-factory/SKILL.md — software-factory
[26] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/writing-beats/SKILL.md — writing-beats
[27] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/writing-fragments/SKILL.md — writing-fragments
[28] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/writing-shape/SKILL.md — writing-shape
[29] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/git-guardrails-claude-code/SKILL.md — git-guardrails-claude-code
[30] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/migrate-to-shoehorn/SKILL.md — migrate-to-shoehorn
[31] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/scaffold-exercises/SKILL.md — scaffold-exercises
[32] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/setup-pre-commit/SKILL.md — setup-pre-commit
[33] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grill-me/SKILL.md — grill-me
[34] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grilling/SKILL.md — grilling
[35] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/handoff/SKILL.md — handoff
[36] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/teach/SKILL.md — teach
[37] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/to-questionnaire/SKILL.md — to-questionnaire
[38] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/wait-what/SKILL.md — wait-what
[39] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/writing-for-agents/SKILL.md — writing-for-agents
[41] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/.claude-plugin/plugin.json — .claude-plugin/plugin.json
[42] https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/.out-of-scope/frozen-misc-skills.md — .out-of-scope/frozen-misc-skills.md
