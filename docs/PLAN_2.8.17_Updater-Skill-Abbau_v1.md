# PLAN 2.8.17 — Updater baut nicht mehr zugewiesene Skills ab

| Feld | Wert |
|---|---|
| Datum | 2026-11-16 |
| Basis | Maker 2.8.17, Branch `v3`, HEAD `442a699` |
| Quelle | `docs/HANDOFF_2.8.16_Updater-Skill-Abbau_v1.md` (Baustelle 2) |
| Zielversion | 2.8.18 (MINOR) |
| Nicht enthalten | `project-lib-versioning` (in 2.8.17 erledigt), Rollout einzelner Teams, Änderungen an installierten Profilen, Löschung durch `apply` |

Alle Zeilenangaben sind am 2026-11-16 gegen HEAD `442a699` mit `grep -n` neu abgeleitet.

## 1. Befund und Belege

`update_team.py` kennt die Kandidaten bereits, klassifiziert sie aber nicht und löscht nichts.

| Stelle | Heutiger Inhalt | Wirkung |
|---|---|---|
| `references/update_team.py:546` | `obsolete = sorted(set(stored) - new_targets)` | reine Namensliste der Ziele, die das alte Maker-Quellpaket ausgeliefert hat und der neue Stand nicht mehr erzeugt |
| `references/update_team.py:550` | `'entries': entries, 'obsolete': obsolete, …` | die Liste steht im Proposal, ohne Rolle, Pfad oder Zustand |
| `references/update_team.py:588` | `for key in ('entries', 'obsolete', …)` | `apply` vergleicht das frische Proposal gegen das geprüfte; jedes Feld darin ist damit ein Drift-Schutz |
| `references/update_team.py:598`, `:635`, `:658` | `retained_obsolete: proposal['obsolete']` | Journal, Installation Record und Ergebnis führen die Reste fort |
| `references/update.md:164` | „lists removed source files and deassigned managed skill copies as `obsolete` and retains them on disk" | Gegenaussage zu jedem Abbau |
| `references/update.md:166` | „Outside this explicit retirement, retain generic obsolete files and local adaptations." | bindet die Ausnahme an genau einen Abschnitt |
| `references/update.md:402` | `## Required Reviewer skill retirement (1.1.22)` | der einzige Löschweg, fest an eine Release-Grenze gebunden |
| `references/update.md:415`-`:421` | „these exact Reviewer skill identities" plus Zwei-Zeilen-Tabelle | zwei Identitäten, nicht drei; `:442` und `:468` sprechen weiter von „three" |
| `references/code-analysis.md:5` | „covers only the three unrelated retired skills" | dritte falsche „three"-Stelle, unabhängig vom Umbau zu korrigieren |
| `references/update_team.py:3` | „No … deletion." | Modulzusage; bleibt nach diesem Plan wahr |
| `references/update_team.py:481`-`:489` | Prüfung jeder gespeicherten Kopie gegen exakte Maker-Quelle und Baseline | jeder `obsolete`-Eintrag hat eine verifizierte Baseline |
| `references/update_team.py:628` | `managed.append({… 'baseline': …, 'installed_hash': digest(merged)})` | `installed_hash` ist der einzige gespeicherte Zustandsanker für eine lokale Kopie |
| `references/update_team.py:686`-`:690` | Rollback prüft Ziel gegen Rollen-Home und `skills/`- bzw. `.agents/skills/`-Präfix | dieselbe Pfadprüfung ist für die Klassifikation wiederverwendbar |
| `references/update_team.py:363` | `record['schema'] != SCHEMA` → Fehler | ein `SCHEMA`-Bump würde jedes installierte Team unlesbar machen |

Entscheidung aus dem Handoff, hier übernommen: `apply` löscht weiterhin nichts. Der Helfer klassifiziert und meldet; die Entfernung bleibt ein Prosa-Nachschritt im bereits freigegebenen Update-Scope. Damit bleiben `update_team.py:3`, `:508` („Do not prune backups or obsolete files automatically") und die Rollback-Zusage (`:478`) wahr.

## 2. Versionsentscheidung

MINOR: 2.8.17 → 2.8.18.

Begründung, aus dem Paket belegt: `AGENTS.md:6` — „Use a MINOR bump for compatible functionality. Use a PATCH bump for a compatible fix, documentation change, recipe change, or script extraction." Hier kommen neue Felder und eine neue Klassifikation im Helfer hinzu; das ist Funktionalität, keine Rezeptänderung. Der naheliegende Präzedenzfall, der Reviewer-Rückbau, ist in `1.1.22` als PATCH gelandet (belegt in `docs/PLAN_2.8.17_Plan-Review-Findings_v1.md:15`-`:17`) — damals war es reine Prosa ohne Helferänderung, deshalb trägt er diese Änderung nicht.

Kein MAJOR: keine gespeicherte Struktur bricht. Der Installation Record behält `retained_obsolete` als flache Pfadliste, `SCHEMA` bleibt 1 (`update_team.py:363`), und das Proposal ist ein Lauf-Artefakt, das `apply` ohnehin neu erzeugt (`:586`-`:590`).

Betroffene Felder: `manifest.json:3` und `SKILL.md:4` gemeinsam auf 2.8.18.

## 3. Änderung 1 — Klassifikation in `references/update_team.py`

**Beobachtung:** `obsolete` ist eine Pfadliste (`:546`); der Zustand einer lokalen Kopie wird nirgends ermittelt, obwohl Baseline (`:487`) und Installationshash (`:628`) vorliegen.

**Ort:** `prepare()` zwischen `:546` und `:552`, neue reine Helferfunktion daneben; `apply()` nur in den drei Fortschreibungszeilen `:598`, `:635`, `:658`.

**Datenform.** `obsolete` wird je Kandidat ein Datensatz:

```json
{
  "kind": "tree",
  "role": "reviewer",
  "skill": "screenshot-to-code",
  "root": "/home/x/.hermes/profiles/daniel/skills/screenshot-to-code",
  "targets": ["…/SKILL.md", "…/references/visual-check.md"],
  "state": "pristine",
  "findings": []
}
```

Sortierung `(role, skill, kind, targets[0])`, `targets` sortiert — das Feld geht in den Drift-Vergleich von `apply` (`:588`) ein und muss zwischen zwei Läufen bytegleich sein.

**Kandidatenart.** `kind: tree`, wenn alle verwalteten Ziele einer Skill-Wurzel obsolete sind; `kind: file`, wenn nur ein Teil obsolete ist und der Skill der Rolle zugewiesen bleibt. Beides ist eine „vom Maker verwaltete Skill-Kopie" im Sinn der Entscheidung; ohne die zweite Art bliebe eine in neuer Version entfernte Referenzdatei für immer im Team liegen, und das Ziel „Stand eines frisch angelegten Teams" wäre verfehlt.

**Wurzelableitung.** Nicht aus dem Zielpfad raten, sondern aus dem gespeicherten Eintrag: `source` ist `skills/<name>/<rel>`. Geprüft wird, dass `source` diesem Muster folgt und `target == <role home>/(.agents/skills|skills)/<name>/<rel>` gilt — dieselbe Prüfung wie im Rollback (`:686`-`:690`). Passt es nicht, ist der Kandidat `indeterminate` mit Blocker, kein Löschvorschlag. SOUL-Ziele können nicht obsolete werden (vier feste Rollen, `:235`-`:252`); trifft die Gruppierung dennoch eines, bricht `prepare()` mit `ValueError`.

**Zustände.** Je Kandidat in dieser Vorrangfolge, alle Abweichungen zusätzlich in `findings`:

| `state` | Bedingung | `findings`-Beispiel |
|---|---|---|
| `indeterminate` | ein Pfad ist nicht sicher lesbar: Symlink, Hardlink (`read()` wirft, `:108`), Nicht-Reguläres, fehlende Berechtigung, Wurzel außerhalb der Skill-Präfixe | `blocked: …/SKILL.md (symlink)` |
| `locally-modified` | ein verwaltetes Ziel existiert und weicht von `installed_hash` ab, oder ein Teil des Baums fehlt | `modified: …/SKILL.md`, `missing: …/references/x.md` |
| `extra-files` | eine Baumwurzel enthält eine reguläre Datei, die kein verwaltetes Ziel ist (gelernte Referenzen, lokale Zusätze, versteckte Dateien) | `extra: …/references/local-learning.md` |
| `absent` | jedes verwaltete Ziel fehlt bereits | leer |
| `pristine` | jedes verwaltete Ziel existiert und stimmt mit `installed_hash` überein, keine Zusatzdatei | leer |

Dateimodus wird nicht klassifiziert: `managed` speichert keinen Modus (`:628`), nur der Lauf-Journal-Eintrag führt ihn.

**Fortschreibung.** `retained_obsolete` bleibt in Journal, Record und Ergebnis die flache, sortierte Pfadliste, abgeleitet aus den Kandidaten (`:598`, `:635`, `:658`). Grund: `load_record` prüft das Feld nicht, aber der Record soll seine Form behalten; die Klassifikation wird über den im Journal vermerkten Proposal-Pfad (`:599`) gelesen.

**Nebenwirkung, gewollt.** Weil der Zustand in `obsolete` steht, macht jede lokale Änderung an einem Kandidaten zwischen Freigabe und `apply` das Proposal ungültig („Proposal/source/target drift; prepare and review again", `:590`). Die Freigabe hat den Zustand benannt; sie darf nicht auf einem inzwischen veränderten Baum vollstreckt werden.

**Voraussetzung:** keine; reine Standardbibliothek wie der Rest der Datei.

**Aufwand:** S — rund 70 Zeilen Helfer plus drei Zeilen Fortschreibung.

## 4. Änderung 2 — `references/update.md`: allgemeine Regel

**Beobachtung:** `:402`-`:483` ist der einzige Löschweg, release-gebunden; `:164`/`:166` behaupten das Gegenteil einer allgemeinen Regel.

**Ort:** Abschnitt `:402`-`:483` wird ersetzt, `:164`-`:166`, `:17`, `:343`, `:366`, `:521` werden nachgezogen.

### 4.1 Neuer Abschnitt (ersetzt `:402`-`:483`)

```markdown
## Required skill retirement

A team update removes the managed skill copies the Maker no longer produces, so that an updated
team holds the skill set a fresh team receives. Teams are updated, not recreated. Local work the
team added is the only boundary: it is never overwritten or reset unasked.

`update_team.py` deletes nothing. It reports every candidate in the reviewed proposal with its
identity, resolved root, managed targets, and local state. Complete the removal after file
application inside the same approved scope; a pristine candidate left in place keeps the team
update incomplete.

Candidates are the entries the proposal reports as obsolete: managed copies of an earlier Maker
source that the target no longer produces. A skill the team created itself is never a candidate,
and neither is a file the Maker does not manage. A candidate is one retired skill tree, or one
retired file inside a tree that stays assigned.

| State | Meaning | Handling |
|---|---|---|
| `pristine` | every managed file matches its recorded installation hash; a tree holds no unmanaged file | back up outside all native discovery roots, then remove |
| `locally-modified` | a managed file differs from its recorded hash, or part of the tree is already missing | retain and report the findings; removal needs a separate decision for that exact candidate |
| `extra-files` | a tree holds a file the Maker does not manage | retain and report the findings; removal needs a separate decision for that exact tree |
| `indeterminate` | a path cannot be resolved safely: symlink, hard link, shared source, unreadable path, or a mapping outside the recorded skill roots | retain and report the blocker |
| `absent` | every managed file is already gone | treat as a successful no-op after native readback |

A tree that carries a retired identity the installation record does not manage as a skill keeps
its unknown baseline: retain it and report it, and never remove it from a guess.

Resolve each identity against [the manifest](../manifest.json) and, where the manifest no longer
carries it, from the recorded source mapping in the installation record. Inspect native discovery
roots and every resolved source path for aliases, symlinks, and shared sources. Where a shared
source serves another role, apply only a supported role-specific unbinding; stop with a concrete
blocker when no isolation is available. Report each concrete retained instruction or autoload
reference that would recreate or require a retired skill. Keep the native `sdlc-review` skill, its
automatic integration, and the CBM/Graphify skills and bindings unchanged.

The retirement introduced in `1.1.22` for `minimal-change-engineering` and `screenshot-to-code` in
Reviewer homes is the first instance of this rule, not a separate mechanism; a pending one resumes
as an ordinary candidate. Keep every other adaptation and every Planner, Coder and Team-Codex
asset.

1. **Before file application:** Read the existing private setup/update record and any pending
   retirement evidence.
   Before invoking `apply`, capture the installed package version and exact Maker commit from the
   installation record and available setup evidence.
   Save the pre-update version, target release/commit, and retirement status `pending` in the
   existing private `devteam/setup.md` progress/update section.
   Keep the original pre-update evidence on resume; do not replace it with advanced installation
   metadata.
   For missing provenance, record the unresolved evidence for the exact candidate scope below.
   Read back this private record before file application.
   Do not create a central registry or change the file-helper record schema.
2. **Read-only discovery:** Read the proposal's obsolete entries and resolve each candidate's
   root, managed targets, state, and findings against the confirmed role homes and the native
   profile inventory.
   Keep this discovery strictly read-only.
   Do not remove trees or change exclusions or bindings during discovery.
   Inspect native discovery roots and every resolved source path for ownership, aliases, symlinks,
   and shared/external sources.
   Record every unmanaged file in a candidate tree and every candidate the record does not manage.
   Do not follow links into shared assets.
   If a shared or external source serves other roles, determine the supported role-specific
   exclusion or unbinding from the installed interface without applying it.
   If no supported isolation is available, stop this reconciliation with a concrete blocker.
   Report each concrete retained instruction or autoload reference that would recreate or require
   a retired skill.
   Record the concrete role-specific obsolete bindings for scope approval.
   Do not remove unrelated bindings or expand into general MCP/hook cleanup.
3. **Approve the full update scope once:** Include the exact `pristine` candidates, their resolved
   paths and backup destinations, the retained candidates with their findings, and the concrete
   role-specific exclusions/unbindings found during read-only discovery in the target update scope
   and approval.
   Include the complete-tree backups, native readbacks, and the concrete role-specific obsolete
   bindings from that inventory.
   For missing provenance, add the approved exact reconciliation scope to the existing private
   record before file application.
   This authoring procedure grants no live deletion permission.
   Within that approved update, retiring every `pristine` candidate is mandatory, not an optional
   second choice.
   A retained `locally-modified`, `extra-files`, `indeterminate`, or unknown-baseline candidate is
   reported, not resolved inside the same scope.
   If the scope is withheld, record the incomplete step instead of claiming a complete team update.
4. **After successful file application:** Run the pending retirement after successful file
   application and before reporting a complete team update.
   Save every candidate's complete local tree and affected role-specific bindings to a protected
   external backup outside all native discovery roots, including inherited and project roots.
   Preserve modes, link metadata, and the full file inventory without dereferencing links into
   shared assets.
   Compare the complete backup inventory and file bytes/hashes with the source before removal.
   Save backup location, source inventory, verification, and unaffected-role inventories in the
   existing private record.
   Continue only if file application, the complete backup, and backup comparison succeeded.
   Recheck the inspected source bytes and bindings immediately before any removal, exclusion, or
   binding change; stop on concurrent drift.
   Remove only the verified `pristine` candidates, without following links or deleting shared
   sources.
   Apply only the inspected, supported role-specific exclusions/unbindings for shared sources and
   obsolete references.
   Reconcile only the inventoried role-specific obsolete bindings within the approved update scope.
   Treat already absent skills as successful no-ops after native readback.
5. **Verify and persist the result:** Verify absence of every removed candidate through native
   discovery and source resolution.
   Use an established fresh discovery/readback interface; stale session catalogs and missing files
   alone do not establish absence.
   Verify preservation of unaffected roles and assets against the pre-removal inventory.
   Read back affected role-specific bindings and the preserved native `sdlc-review`
   source/integration.
   Mark retirement `complete` only after these readbacks pass, with exact paths, backup evidence,
   and the file-update run/revision.
   Read back the saved completion evidence.
   Keep failed or interrupted retirement `pending`, with the concrete blocker and next action.
   If retirement is withheld or fails, report `files updated; team update incomplete`.
   On resume, read pending state, backup, journal, and actual discovery before continuing only
   unfinished work.

The file-updater rollback does not restore this prose poststep's removed trees or bindings.
For an authorized restoration, first check current targets for later edits and review the saved
backup and binding scope.
Restore complete trees, modes, and role-specific bindings from the external backup without
overwriting later work or shared assets.
Verify restored bytes and native discovery separately from the guarded file-helper rollback below.
Record restoration and renewed `pending` status in the existing private record; do not retain a
completion claim for restored skills.
Do not restart workers or sessions, or claim that running contexts unloaded these skills.
```

Was gegenüber `:402`-`:483` **wörtlich erhalten** bleibt, damit der bestehende Prosa-Vertrag nicht schwächer wird (der Testumbau hängt daran): die fünf Schritt-Titel in dieser Reihenfolge, „Keep this discovery strictly read-only.", „Do not remove trees or change exclusions or bindings during discovery.", „Do not delete guessed paths or follow links into shared assets." (hier als „Do not follow links into shared assets."), „If no supported isolation is available, stop this reconciliation with a concrete blocker.", „outside all native discovery roots", „Compare the complete backup inventory and file bytes/hashes with the source before removal.", „Continue only if file application, the complete backup, and backup comparison succeeded.", „Recheck the inspected source bytes and bindings immediately before any removal, exclusion, or binding change; stop on concurrent drift.", „Reconcile only the inventoried … obsolete bindings within the approved update scope.", „Treat already absent skills as successful no-ops after native readback.", „Mark retirement `complete` only after these readbacks pass", „If retirement is withheld or fails, report `files updated; team update incomplete`."

Entfallen und im Plan bewusst zurückgezogen:

- Das Release-Gate (`:405`-`:413`, „pre-update version below `1.1.22`") und die „Resume a pending retirement … even if `installation.json` already reports `1.1.22`"-Regel. Die allgemeine Regel greift bei jedem Update; ein offener 1.1.22-Rückbau erscheint als gewöhnlicher Kandidat. Grund: eine Releasenummer ist kein Zustandsbeweis — dieselbe Aussage, die `:409` schon für den Einzelfall festhielt.
- Die Zwei-Zeilen-Tabelle (`:417`-`:421`) als eigener mechanischer Abschnitt. Die Identität kommt künftig aus dem Proposal (`root`, `targets`), nicht aus einer handgepflegten Tabelle; die beiden `1.1.22`-Identitäten bleiben als erster Anwendungsfall im Text genannt.
- „Reviewer-specific" als Geltungsbereich. Die Regel gilt je Rolle, auch für Team-Codex unter `.agents/skills/`.

### 4.2 Nachzuziehende Stellen

| Stelle | ALT | NEU |
|---|---|---|
| `:17` | `…and [Reviewer skill retirement](#required-reviewer-skill-retirement-1122) use separate approved prose steps…` | `…and [skill retirement](#required-skill-retirement) use separate approved prose steps…` |
| `:164` | `The file helper lists removed source files and deassigned managed skill copies as \`obsolete\` and retains them on disk.` | `The file helper lists removed source files and deassigned managed skill copies as \`obsolete\` with role, identity, resolved root, and local state, and deletes nothing.` |
| `:165` | `Complete the [required Reviewer skill retirement](…) after file application for affected teams.` | `Complete the [required skill retirement](#required-skill-retirement) after file application for affected teams.` |
| `:166` | `Outside this explicit retirement, retain generic obsolete files and local adaptations.` | `Retain obsolete files that are not managed skill copies, and retain local adaptations.` |
| `:343` | `Complete the fixed \`1.1.22\` retirement procedure when applicable; this workflow migration does not replace it.` | `Complete the [required skill retirement](#required-skill-retirement) for the affected team; this workflow migration does not replace it.` |
| `:366` | `…complete the pre-apply record and approval steps in [required Reviewer skill retirement](…).` | `…complete the pre-apply record and approval steps in [required skill retirement](#required-skill-retirement).` |
| `:521` | `Read back the required retirement status and native evidence for affected teams…` | unverändert; deckt die allgemeine Regel weiter |

Nicht geändert: `:508` („Do not prune backups or obsolete files automatically") — bleibt wahr, weil `apply` nichts löscht.

### 4.3 Verbraucher des Ankers

`#required-reviewer-skill-retirement-1122` → `#required-skill-retirement`, je Stelle:

- `README.md:114` — Satz umstellen: „The file helper retains obsolete copies." wird zu „The file helper classifies obsolete copies and deletes nothing."; Linktext „required version-gated Reviewer skill retirement" → „required skill retirement".
- `references/code-analysis.md:5` — „covers only the three unrelated retired skills" → „covers the retired skill copies of all roles; it changes no analysis asset".
- `templates/setup-record.md:111` — Linktext und Anker.

Die falsche Zahl „three" in `:442` und `:468` verschwindet mit dem Abschnitt; `code-analysis.md:5` ist die dritte Fundstelle und wird mitkorrigiert.

**Voraussetzung:** TAS-Standard gelesen (getan); keine weiteren.

**Aufwand:** M — rund 90 Zeilen Prosa, sechs Nachzüge, drei Ankerstellen.

## 5. Änderung 3 — Tests

**Beobachtung:** `references/test_update_team.py:885` prüft die Retention als Liste; `:897`-`:963` baut den Reviewer-Rückbau als Fixture und erwartet `set(proposal['obsolete']) == managed_previous` (`:952`) sowie `set(record['retained_obsolete']) == managed_previous` (`:957`). `references/test_render_reasoning.py:840` und `:866` sind Wortlaut-Verträge über den 1.1.22-Abschnitt, `:945` prüft `:166`, `:948` den Anker in drei Dateien.

**Ort und Umfang:**

`references/test_update_team.py`

| Test | Änderung |
|---|---|
| `:885` `test_obsolete_file_is_retained_and_reported` | erweitert: der entfernte Referenzdatei-Kandidat ist `kind: file`, `state: pristine`; `apply` lässt ihn liegen; `retained_obsolete` bleibt die flache Pfadliste |
| `:897` `test_reviewer_deassignment_retains_installed_skills` | Fixture bleibt (lokale Anpassung + gelernte Datei); Erwartung wird `kind: tree`, `state: locally-modified`, `findings` nennen `modified:` und `extra:`; zusätzlich ein zweiter Baum ohne lokale Änderung, der `pristine` meldet |
| neu | `test_pristine_obsolete_tree_is_classified_without_deletion` — deassignter, unveränderter Baum: `state: pristine`, `root`, `targets` sortiert, `findings` leer, `apply` löscht nichts, Record unverändert flach |
| neu | `test_obsolete_classification_is_stable_across_preparations` — zweimal `prepare()` auf unverändertem Baum liefert identische `obsolete`-Datensätze (Grundlage des Drift-Vergleichs) |
| neu | `test_local_edit_after_approval_invalidates_proposal` — Proposal erzeugen, danach einen Kandidaten lokal ändern, `apply` → `ValueError` mit „Proposal/source/target drift" |
| neu | `test_symlink_in_obsolete_tree_is_indeterminate` — Symlink im Baum: `state: indeterminate`, `findings` nennen den Pfad, `apply` läuft durch und löscht nichts |
| neu | `test_partially_missing_obsolete_tree_is_locally_modified` — eine verwaltete Datei des Baums fehlt: `state: locally-modified`, `findings` nennen `missing:` |
| neu | `test_obsolete_mapping_outside_skill_roots_is_refused` — direkter Aufruf der Klassifikationsfunktion mit einem gespeicherten Eintrag, dessen Ziel nicht unter `skills/<name>/` liegt: Blocker statt Löschvorschlag |

`references/test_render_reasoning.py`

| Test | Änderung |
|---|---|
| `:840` `test_retirement_has_exact_skill_scope_and_fixed_release_gate` | umbenannt (`…general_scope_and_identity_resolution`): neuer Abschnittstitel vorhanden, alter fehlt; die fünf Zustände namentlich; die beiden `1.1.22`-Identitäten im Text genannt; Manifest-Prüfung (Reviewer-Ziele fehlen) bleibt; Tabellenzeilen-Assertion entfällt, weil die Tabelle zurückgezogen ist |
| `:866` `test_retirement_requires_preapply_pending_state_and_verified_resume` | Wortlaut auf die allgemeine Fassung umgestellt; alle heute geprüften Pflichtsätze und die Reihenfolge der fünf Schritte bleiben Assertions, insbesondere „drift check immediately precedes retirement writes" (`:924`), `Within that approved update, … is mandatory, not an optional second choice.` und `Read back the required retirement status` |
| `:945` | Assertion auf den neuen `:166`-Satz |
| `:948` | Anker `#required-skill-retirement` in `README.md`, `references/code-analysis.md`, `templates/setup-record.md` |

Keine Assertion entfällt ohne gleich starke Prüfung: die Tabellen-Assertion (`:845`) wird durch die Kandidaten-Assertions in `test_update_team.py` (Root, Targets, Zustand) ersetzt; die Identitäts-Auflösung wird damit erstmals maschinell geprüft statt nur im Text behauptet.

**Voraussetzung:** Änderungen 1 und 2 im Arbeitsbaum (die Tests lesen `update.md` und rufen `prepare()`).

**Aufwand:** M — fünf neue Testfälle plus zwei Umbauten.

## 6. Reihenfolge der Umsetzung

1. Änderung 1 (`update_team.py`, drei Fortschreibungszeilen) und die zugehörigen `test_update_team.py`-Fälle — danach `python3 -B -m unittest references.test_update_team` grün.
2. Änderung 2 (`update.md`) und Änderung 3 letzter Teil (`test_render_reasoning.py`) im selben Schritt, weil der Test den Abschnitt wörtlich liest.
3. Anker-Sweep (`:17`, `:165`, `:343`, `:366`, `README.md:114`, `code-analysis.md:5`, `setup-record.md:111`).
4. Versionsfelder gemeinsam (`manifest.json:3`, `SKILL.md:4` → 2.8.18).
5. Suite einmal am Ende.

## 7. Entschieden in der Planbesprechung (2026-11-16)

1. **Kandidatenart `file` — angenommen.** Eine in neuer Maker-Version entfernte einzelne Referenzdatei innerhalb eines weiter zugewiesenen Skills ist ebenfalls eine verwaltete Kopie und wird als `kind: file` geführt. Ohne diese Art bliebe sie dauerhaft im Team und das Ziel „Stand eines frisch angelegten Teams" wäre verfehlt.
2. **`unknown baseline` — bleibt Prosa.** Der Helfer klassifiziert nur verwaltete Kopien; für sie ist die Baseline immer verifiziert (`references/update_team.py:487`). Ein Baum mit zurückgezogener Identität, den der Record nicht als Skill verwaltet, wird gemeldet und nie gelöscht. Die Helferklasse für „nicht sicher lesbar" heißt `indeterminate`. Eine Liste zurückgezogener Identitäten im Helfer ist damit nicht beauftragt.
3. **1.1.22-Gate — entfällt ersatzlos.** Offene Rückbauten erscheinen als gewöhnliche Kandidaten; ein Team, dessen Record diese Bäume nie verwaltet hat, fällt in den Meldepfad aus Punkt 2. Kein Sonderfall für die beiden Identitäten im Abschnitt.
4. **Rollout.** Welche Teams wann aktualisiert werden, ist nicht Teil dieses Changesets; nach dem Maker-Commit bleiben die Waisen in fremden Profilen, bis deren nächstes Update läuft. Wird beim Abschluss offen benannt, nicht mitgelöst.

## 8. Verifikation

1. `python3 -B -m unittest discover -s references -p 'test_*.py'` im Parent — Erwartung `OK (skipped=1)`, Testzahl 212 plus die neuen Fälle; ein Lauf in einem `delegate_task`-Kind (`skipped=16`) zählt nicht als Beleg.
2. `grep -rn "required-reviewer-skill-retirement-1122" --include=*.md --include=*.py . | grep -v '^./docs/'` → keine Treffer.
3. `grep -n "## Required skill retirement" references/update.md` → genau einmal; `grep -c "1.1.22" references/update.md` nennt nur noch die Erst-Anwendung im neuen Abschnitt.
4. `grep -rn "obsolete" references/update.md references/update_team.py` — jede verbliebene Zeile gegen die neue Regel gelesen, keine Gegenaussage.
5. `python3 -c "import json;m=json.load(open('manifest.json'));print(m['version'])"` und `grep -n '^version: ' SKILL.md` → beide 2.8.18.
6. `git diff --check`, `git status --porcelain`, `git diff --stat`; nur `references/update.md`, `references/update_team.py`, `references/test_update_team.py`, `references/test_render_reasoning.py`, `references/code-analysis.md`, `templates/setup-record.md`, `README.md`, `manifest.json`, `SKILL.md` und das neue Plandokument verändert.
7. `SCHEMA` bleibt 1: `grep -n "^SCHEMA = " references/update_team.py`.
8. Keine Löschung durch den Helfer: `grep -n "unlink\|rmtree\|os.remove" references/update_team.py` → genau ein Treffer, der Temp-Datei-Aufräumer in `atomic()` (`:178`); jeder weitere Treffer ist ein Befund.
9. ALT-Vorprüfung, am 2026-11-16 ausgeführt: alle neun ALT-Zeichenketten aus 4.2 und 4.3 sind per `grep -F` je genau einmal getroffen (`update.md` sechsmal, `README.md`, `references/code-analysis.md`, `templates/setup-record.md` je einmal).

## 9. Nicht angefasst

- `apply()`-Semantik außer den drei Fortschreibungszeilen; keine Löschung, kein neuer Schreibpfad im Helfer.
- `SCHEMA` (`:26`) und die Form des Installation Record.
- Die vier Rollen-Templates und alle Skills unter `skills/`.
- `references/update.md:508` und der Rollback-Abschnitt.
- `docs/`-Historie, `vortrag/`, installierte Profile, Gateways, Dispatcher.

## 10. Umsetzung (2026-11-16)

Umgesetzt im Checkout, Version 2.8.18, Suite `Ran 219 tests`, `OK (skipped=1)`.

| Datei | Änderung |
|---|---|
| `references/update_team.py` | `skill_placement`, `tree_entries`, `candidate_state`, `obsolete_candidates`, `obsolete_targets`; `prepare()` liefert `obsolete` als Datensätze; `apply()`/Journal/Record schreiben die flache Pfadliste (+129 Zeilen) |
| `references/update.md` | Abschnitt `## Required skill retirement` ersetzt den 1.1.22-Abschnitt; `:17`, `:164`-`:166`, `:343`, `:366` nachgezogen |
| `references/test_update_team.py` | sieben neue Fälle (inkl. `absent`), zwei bestehende erweitert; Fixture-Helfer `deassigned_reviewer_skill` |
| `references/test_render_reasoning.py` | zwei Wortlaut-Verträge auf die allgemeine Regel umgestellt, Verbraucher-Test auf den neuen Abschnitt |
| `README.md`, `references/code-analysis.md`, `templates/setup-record.md` | neuer Anker `#required-skill-retirement`; „three unrelated retired skills" korrigiert |
| `SKILL.md`, `manifest.json` | 2.8.17 → 2.8.18 |

Abweichungen vom Plan, beide zugunsten der bestehenden Verträge:

1. Die geplante Sammelzeile „Keep the native `sdlc-review` skill, its automatic integration, and the CBM/Graphify skills and bindings unchanged." wurde durch die zwei Originalsätze ersetzt (`sdlc-review`-Zeile und „Preserve CBM/Graphify skills and bindings; restore the selected Reviewer integration through the approved upstream companion update."). Grund: der Test `test_selected_reviewer_analysis_restoration_covers_current_and_retired_teams` prüft den zweiten Satz wörtlich; eine Sammelzeile hätte den Vertrag ohne Ersatz gelöscht.
2. Die Grenzzeile „Preserve shared runtimes, caches, indices, MCP entries, hooks, and unrelated integrations; do not copy retired methods into SOUL or other skills." bleibt erhalten und ist wieder Assertion, nachdem sie in der ersten Fassung des neuen Abschnitts fehlte.

Nicht umgesetzt und weiterhin offen: Rollout (Punkt 7.4). Kein Profil, kein Gateway, keine laufende Sitzung angefasst.
