# Herkunft und Lieferstand

## Aktueller Paketumfang

Die eigenen Skillbäume und ihre Begleitdateien sind enthalten. Der exakte
Bestand steht in [manifest.json](manifest.json), Rollen und Quellen in
[upstream-sources.md](references/upstream-sources.md). Rollen-SOULs und installierte
Skills tragen den Arbeitsprozess unabhängig vom Makerpaket.
Die Makerseite [native-workflow.md](references/native-workflow.md) beschreibt
Einrichtung und Prüfung der Arbeitsbindungen sowie den Render-/Kontextvertrag
für die drei enthaltenen Rollen-SOULs. Der [Maker](SKILL.md), das geführte
[Setup](references/setup.md), allgemeine [Integrationsrezepte](references/integrations.md),
eine private Protokollvorlage und reine Textvalidierung sind enthalten.
Beide [Codeanalysewege](references/code-analysis.md) sind als Einrichtungsrezepte
enthalten. CBM umfasst seine offizielle Codex-Integration einschließlich Unteragenten.
Normal setup verifies configuration, file delivery and the versioned installation baseline. Live behavior is not guaranteed. No external runtime or original upstream skill copy is exported in this Maker.

## Eigene Texte und übernommene Skills

Neue Makertexte wurden im Auftrag von Max durch Mariko (Hermes Agent) für
Generic Devteam verfasst. Für sie gilt die vollständige [MIT-Lizenz](LICENSE),
`Copyright (c) 2026 generic-devteam contributors`. Diese Notice bezeichnet die
neue Paketfassung; sie behauptet keine historische Rechtekette. Paketversion,
Planversionen und spätere Zielprojektversionen sind unabhängig.

| Anteil | Herkunft und tatsächliche Behandlung |
|---|---|
| Paketvertrag, Textrenderer und Dokumentation | Neu aus bestätigtem Auftrag; MIT dieses Pakets. |
| Drei Rollen-SOUL-Vorlagen | Aus vorhandenen Rollen-SOULs im ausdrücklich bestätigten Auftrag abgeleitet und danach revidiert zu einem knappen englischen Regeltext; Reviewer als maßgebliche Nutzerfassung integriert. Persönliche Bindungen durch deklarierte Felder ersetzt; die beauftragte Bereinigung der Coder-Modellpolicy ist enthalten. Private Quellen sind keine Paketprüfungsabhängigkeit. |
| `screenshot-to-code` 1.0.0 | Kanonisches eigenständiges Paket, Autorenfeld `Max, Mariko (Hermes Agent)`. Alle sechs Dateien bytegleich und ohne Transportumbenennung. Eigene vollständige [Lizenz](skills/screenshot-to-code/LICENSE) mit `Copyright (c) 2026 screenshot-to-code contributors` unverändert. |
| `minimal-change-engineering` 1.0.0 | Übernommene, vom Nutzer bearbeitete Skillfassung. MIT-Angabe im Frontmatter; keine separate Lizenz-/Notice-Datei im Skillbaum. Der historische Autoren-/Auditverweis im Skill ist dadurch nicht zusätzlich belegt. |
| `brownfield-feature-planning` 1.0.1 | Im Auftrag von Max durch Mariko (Hermes Agent) aus der übernommenen Nutzerfassung in TAS überarbeitet. Generischer Planungskern und bedingt geladene Fachreferenzen; Recovery-Skripte unverändert. Bestehende MIT-Angabe im Frontmatter; keine separate Lizenz-/Notice-Datei im Skillbaum. |
| `plan-versioning-semver` 1.0.0 | Übernommene, vom Nutzer bearbeitete Skillfassung, Autorenfeld `Mariko`. Kein Lizenzfeld und keine separate Lizenz-/Notice-Datei im Skillbaum. |
| `project-lib-versioning` 1.0.0 | Übernommene, vom Nutzer bearbeitete Skillfassung. MIT-Angabe im Frontmatter; keine separate Lizenz-/Notice-Datei im Skillbaum. Der historische Autoren-/Auditverweis im Skill ist dadurch nicht zusätzlich belegt. |
| `retro` 0.1.0 | Owned process/environment retrospective adapted from Matt Pocock's method, with full-process token economy. The complete [skill NOTICE](skills/retro/NOTICE.md) records the original revision and adaptations; its [MIT license](skills/retro/LICENSE) retains the original copyright and permission notice. No upstream runtime installation. |
| `prototype` 0.1.0 | Owned Planner-only clarification adaptation of Matt Pocock's logic/UI method. The [skill NOTICE](skills/prototype/NOTICE.md) records the exact source and approved differences; its complete [MIT license](skills/prototype/LICENSE) retains the original copyright and permission notice. Direct planning aids in planning `docs/`, not product implementation or an upstream runtime installation. |
| `diagnosing-bugs` 0.1.0 | Owned proportional diagnosis adaptation of Matt Pocock's complete method at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`. Team-Codex only; compact classifier and conditionally required method. The [skill NOTICE](skills/diagnosing-bugs/NOTICE.md) records source companions and justified differences; its complete [MIT license](skills/diagnosing-bugs/LICENSE) retains Matt's original copyright/permission. No upstream runtime installation or automatic synchronization. |

Die eigenen Skills liegen als fertige Bäume unter `skills/` und werden beim Setup
einschließlich aller vorhandenen Begleitdateien unverändert kopiert. Die Paketlizenz
ersetzt keine fehlenden Herkunftsbelege oder separaten Lizenztexte übernommener
Bestandteile. Diese Notice dokumentiert den tatsächlichen Bestand und behauptet
keine neue Rechtekette.
Autorenprüfung und Integrationschecks sind kein unabhängiger Review.

## Bounded planning adaptations: to-spec and to-tickets

Planner synthesis and Brownfield migration planning adapt selected methods from [mattpocock/skills](https://github.com/mattpocock/skills) at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`:
- `skills/engineering/to-spec/SKILL.md` and `agents/openai.yaml`.
- `skills/engineering/to-tickets/SKILL.md` and `agents/openai.yaml`.

Adaptations retain domain vocabulary, accepted ADRs, user-facing problem/solution, concrete test seams, analogous tests, meaningful scope boundaries, and prototype-derived decisions.
Wide mechanical changes use conditional Expand–Migrate–Contract with verified intermediate states and native dependencies/review gates.
Existing story-first cards, accepted-plan authority, concrete technical context, Coder discretion, and role writing scope remain intact.
Neither original skill is installed or bundled. Their tracker publication, extra approvals, one-seam ideal, blanket prefactoring, path/code ban, integration-branch fallback, and final integration ticket are not adopted.

New adaptation text uses this package's MIT license. The original root MIT notice follows:

> MIT License
>
> Copyright (c) 2026 Matt Pocock
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

## Bounded review adaptation: code-review

The [Reviewer SOUL](templates/roles/reviewer.SOUL.md.template#proportional-investigation) adapts Matt Pocock's complete `skills/engineering/code-review/` method from [mattpocock/skills](https://github.com/mattpocock/skills) at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.
Source read: `SKILL.md`, `agents/openai.yaml`, and root MIT `LICENSE`.
The full original copyright and permission notice is retained above and applies to this source too.
New adaptation text uses this package's MIT license.

Retained: parallel fresh-context Spec and standards perspectives, distinct axes, documented conventions over smell heuristics, and no ritual manual duplication of mechanically enforced rules.
Adapted: direct small-review path; broader technical correctness; mandatory accepted-plan and exact implementation-state binding; Reviewer validation, coverage and native verdict ownership; coordinated checks and correction evidence reuse.
A qualified HIGH technical helper can satisfy the existing critical-invariant pass; all existing independence, coverage, model/provider and permission conditions remain mandatory.
The original's tracker discovery/setup, optional missing Spec, committed three-dot diff restriction, fixed word budget, verbatim report aggregation and automatic refactoring suggestions are not adopted.
No original `code-review` skill, OpenAI agent metadata, helper profile, or competing review workflow is delivered.
The method travels in the existing rendered Reviewer SOUL; native `sdlc-review` remains unchanged and automatically preloaded.
There is no automatic upstream synchronization or claim of measured review-quality/token improvements.

## Fremdkomponenten und technische Grenzen

TAS is an external authoring dependency from [ataian/tas](https://github.com/ataian/tas), identified in the manifest and [source recipe](references/upstream-sources.md#tas).
The Maker ships no normative TAS copy and assigns no TAS team-role installation; the complete upstream package retains its own MIT and third-party notices.
Matt Pocock's `to-questionnaire` is an unchanged Planner-only upstream asset in the existing pinned Matt component, not an owned adaptation or bundled Maker copy. Preserve its complete tree and the original root MIT license through the integration recipe.

Fremdkomponenten sind Bezugsidentitäten mit dokumentierten Zielrezepten, keine
mitexportierten Installationen. Ihre konkreten Bezugsstände behalten eigene
Lizenzen/Notices; unsere MIT-Lizenz lizenziert sie nicht um. Rechercheidentitäten
in nativen Rezepten sind keine Installationspins oder Runtimegarantien.
For the two Caveman writing skills, `source_revision` pins the original release in the `caveman` component.
`caveman-review.source_component` reuses that source identity.
Their upstream texts remain unchanged; role SOULs extend their prose scope and preserve the review workflow.

The manifest stage `setup-recipe` describes a recipe package, not qualified live-team behavior. General timeout/retry/rate-limit investigation and synthetic behavioral experiments are outside normal setup scope.

## Dateivertrag

`files` ist die sortierte, duplikatfreie Liste aller regulären Paketdateien außer
`manifest.json`. Symlinks, Bytecode und interne Evidenz gehören nicht hinein.
Exclude repository-only `docs/`, `HERMES.md`, `.git/`, `.gitignore`, and `vortrag/` from package accounting and installation. Check the remaining package file inventory completely.
`own_skills.targets` nennt direkte Zielrollen/Harnesse; Auftragspflichten an Codex
sind keine zusätzliche Skillinstallation. `status: included` meint vorhandene
Dateien, nicht aktivierte Fähigkeiten. `skill_path`, `license_path`, `notice_path`
und `origin_ref` sind paketrootrelativ; `license_path: null` bedeutet, dass kein
separater Lizenztext im jeweiligen Skillbaum vorhanden ist. `notice_path` verweist
auf die tatsächliche Herkunftsbeschreibung, nicht auf eine erfundene Begleitdatei.
Die Transportabbildung eigener Skills erhält `SKILL.md`; kopiert wird immer der
vollständige Skillbaum ohne Rendering. `source_sha256` beim Screenshot enthält
die kanonischen Dateiidentitäten. Die Paketprüfung braucht keinen privaten Quellbaum.

`role_templates` enthält genau Planner, Coder und Reviewer; `targets` bindet jede
Vorlage an ihr eigenes Hermes-Profil. `template_path`, `origin_ref`, `license_path`
und `notice_path` sind paketrootrelativ. `transport` bezeichnet das spätere
Renderziel `SOUL.md` in diesem Profil, nicht eine Aktivierung im Bauprojekt.
`render_fields` enthält die sortierte eindeutige Menge der tatsächlich vorkommenden
deklarierten Rollenfelder; Mehrfachvorkommen sind erlaubt. Herkunft, Validierung
und Kontextgrenzen stehen in der Makerreferenz. Technische Werte stammen aus
denselben bestätigten Daten wie die Zielkonfiguration.

`upstream_components.subpaths` sind originalrepositoryrelative Pfade; `.` meint
den Repositoryroot. `recipe_status: pending` ist ein offener Folgeauftrag, kein
Setupnachweis. `recipe_status: documented` bedeutet ein vorhandenes Rezept,
nicht dessen erfolgreiche Ausführung.
Render role fields from confirmed setup values.
Bind only the recovery launcher through `references/bind_recovery.py`.
Keep all other skill bytes unchanged.

Analysemetadaten im Manifest: `reviewed_revision` ist ein Rechercheanker,
`asset_bundles.source_to_target` bildet die vollständigen Graphify-Originalbäume
auf relative Skillziele ab; `sha256` bezieht sich auf gelesene Originalbytes.
`legal_files` sind beim Bezug unverändert beizulegende Rechtstexte. CBM-
`release_members` ist eine Packagerableitung, kein geprüfter Archivinhalt;
`asset_evidence` benennt ausdrücklich statische Ableitung statt Installeroutput.
Code-analysis setup checks installed assets, bindings and connection/configuration readbacks, without an artificial index/query/update project. Graphify retains Apache-2.0 and its MIT history/NOTICE; CBM retains MIT and release THIRD_PARTY_NOTICES. No relicensing is implied.

## Verification boundary

[Setup-output verification](references/verification.md) covers actual setup files, effective configuration,
availability, generated bindings and the versioned installation baseline.
Report **Team configured; setup outputs verified** only when those outputs are complete.
Configuration and file evidence do not prove live behavior or project readiness.
[Development verification](references/development-verification.md) is separately triggered by Maker authoring/review or commissioned qualification.
This notice does not claim an independent review, live rollout, or export of the current revision.
