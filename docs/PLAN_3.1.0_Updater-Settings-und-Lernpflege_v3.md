# PLAN 3.1.0 — Updater: Sollwerte setzen, Lernungen melden (v3)

**Ziel:** Ein Team-Update setzt die vom Maker festgelegten Profileinstellungen auf ihren Sollwert und
meldet die vom Team gelernten Textänderungen in SOULs und Skills, damit der User je Ziel entscheidet,
ob sie erhalten bleiben oder der Maker-Text gilt. Kein Zustand über Läufe; der Abschlussbericht ist
Ablage.

**Nicht Ziel:** keine Änderung an SOUL- oder Skill-Texten, Rollenverhalten, Auto-Load, Plugins, Hermes,
CBM, Hindsight; kein Kartenbudget (Planner, `kanban-phase-release.md` Schritte 3 und 4).

**v3 nach `REVIEW_3.1.0_..._v2.md` (Fujiko, 2026-11-25):** N1–N11 eingearbeitet, F16/F17 als Grenze
korrigiert. Zuordnung in §9 und §10.

---

## 1. Ist-Stand (Fundstellen gegen HEAD `6667c34`)

| Punkt | Fundstelle |
|---|---|
| Setup setzt die Wartewerte bereits, das Update verlangt eine Freigabe | `setup.md:103-113` (Prosa `:103`/`:105`, Kommandos `:108-110`, Readbacks `:111-113`), `update.md:282` |
| Kein maschinenlesbarer Sollwert | `manifest.json` — Schlüssel an `:2-5` (`name`, `version`, `recovery_launcher`, `stage`), `:6` (`files`), `:84` (`role_templates`), `:172` (`own_skills`), `:378` (`upstream_components`); kein `settings` |
| Dateihelfer schreibt keine Konfiguration | `update_team.py:3`; `update.md:8` |
| Abweichung wird gemeldet und ersetzt | `update.md:106`, `:110` (letzter Satz), `:113`; `update_team.py:705-708` |
| `apply` schreibt jedes Ziel; einzige Übersprung-Bedingung `merged == before_hash` | `update_team.py:789-794` |
| `apply` baut das Proposal neu und vergleicht schlüsselweise, `merged` inbegriffen | `update_team.py:754`, `:756-758`; `merged` entsteht in `prepare` bei `:705`, landet in `entries` bei `:712` |
| `installed_hash` speist die Retirement-Klassifikation | `update_team.py:607`, `:613` → `candidate_state` (`:536-578`); `update.md:294-295` |
| `prepare` lädt altes **und** neues Manifest | `:636` (über `desired`, `:290`), `:683` (alt); `:650`, `:684` (neu) |
| Proposal-Integritätsliste | `update_team.py:756` |
| Vertragstests | `test_build_evidence.py:104` (Schrittname), `:114-117` (vier Sätze aus `:106`/`:113`); `test_render_reasoning.py:710-712` (Schrittname/Position), `:1293` (`update.md:110` wörtlich) |
| Skip-Fall | `update.md:259` („leave the team unchanged") |

---

## 2. Teil A — Sollwerte

### A1 `manifest.json`

```json
"settings": {
  "planner":  { "kanban.auto_subscribe_on_create": false },
  "coder":    { "kanban.auto_subscribe_on_create": false,
                "terminal.timeout": 14400,
                "timeouts.tools.sequential_call": 15000,
                "timeouts.tools.concurrent_batch": 15000 },
  "reviewer": { "kanban.auto_subscribe_on_create": false,
                "terminal.timeout": 14400,
                "timeouts.tools.sequential_call": 15000,
                "timeouts.tools.concurrent_batch": 15000 }
}
```

Aufgenommen, weil `setup.md:79`/`:94` sie unbedingt für alle drei Rollen setzt (Readback `:99`).
Draußen: `model.*`, `agent.reasoning_effort`, `terminal.cwd`, `memory.provider`,
Mattermost-Bindung (Kundenentscheidungen); `security.protected_instruction_files` (in `setup.md:123`
ausdrücklich „if needed and authorized", zentral erfüllbar — `:126` ist ein `config set`, also eine
Einstellung, aber autorisierungsgebunden) **[N7]**; `skills.creation_nudge_interval` (eigener
autorisierungspflichtiger Schritt, `update.md:118`). Kein `maker_version` im Block — das Proposal
führt ihn bei `:715`.

### A2 `references/update_team.py`

- `settings` aus dem **Ziel**-Manifest lesen (`:650`/`:684`); das alte Manifest bleibt unberührt.
  Fehlt `settings` im Ziel-Manifest, bricht der Lauf ab; fehlt es im alten, ist das kein Fehler.
- Proposal-Block `settings` (Rolle → Schlüssel → Sollwert). Keine Istwerte, keine CLI-Aufrufe.
- Integritätsliste `:756` um `'settings'` erweitern (in v3 zusätzlich um `'keep'`, siehe B2).

### A3 `references/update.md` — Zielwortlaute

- **`:8`**: Satz bleibt; Ergänzung: „The settings reconciliation in Activity and application is a
  mandatory step of this procedure, not a separate approved step."
- **`:88`** (frei änderbar, kein Test): „Note the Coder and Reviewer settings for the reconciliation
  in Activity and application; the values come from `manifest.json → settings` and need no scope
  decision." **[N3]**
- **`:117`**: „Runtime configuration and integration changes need their applicable authorization,
  except the settings reconciliation: it is a mandatory step of this procedure, runs with the
  executing agent's permissions, and stays `pending` when the runtime refuses."
- **`:282`** (Schrittname bleibt, `test_build_evidence.py:104` und `test_render_reasoning.py:710-712`):
  1. nur bei `--activity-decision proceed`; bei `skip` bleibt das Team unverändert (`:259`) **[N4]**
  2. je Profil und Schlüssel `hermes -p <profil> config get` lesen
  3. gegen `manifest.json → settings` stellen
  4. bei Abweichung den alten Wert für den Bericht notieren und auf Soll setzen
  5. alle Schlüssel zurücklesen, im privaten Setup-Record festhalten (`templates/setup-record.md:42`)
  6. Ist → Soll im Bericht ausweisen
  Ist ein Profil nicht vorhanden, schlägt `config get` fehl oder ist der Wert kein Skalar, gilt das
  `pending`-Muster aus `:127` („files updated; team update incomplete") **[F13]**. Der Typ von
  `timeouts.tools` wird nicht aus einer Doku-Stelle abgeleitet; die Prüfung „kein Skalar" genügt
  **[N8]**.
- **`:106`** → „Managed SOUL and skill targets are authoritative: a locally modified text file is
  reported under `adaptations` with the target path and the installed Maker version. The approved
  decision replaces it with the new Maker output or retains the local text for this run." **[N6]**
- **`:110`** letzter Satz → „A current managed target is not obsolete: its local edit is an
  adaptation that the approved decision either replaces or retains." **[N6]**
- **`:113`** → „Inspect every `adaptations` entry with its path and installed Maker version. Local
  SOUL or skill text survives the update only when the approved decision retains it; otherwise the
  Maker output replaces it." **[N6]**
- **Neuer Schritt „Write the run report"** in „Activity and application", nach dem Settings-Abgleich:
  Datei, Ort, Modus und fünf Abschnitte wie in §4 **[N5]**.

### A4 `references/setup.md`

`:103-113` bleibt im Wortlaut (genau **eine** Zeile `config set terminal.timeout`,
`test_render_reasoning.py:681`) und erhält eine Quellenzeile: die Werte stehen in
`manifest.json → settings`; bei Abweichung gilt das Manifest.

---

## 3. Teil B — Lernungen melden und entscheiden

### B1 Ablauf (steht in `update.md`)

1. Je verwaltetes SOUL-/Skill-Ziel lokal gegen die Pristine-Baseline stellen.
2. Jede Abweichung melden: Pfad, installierte Maker-Version und **was die Rolle ergänzt oder geändert
   hat** — inhaltlich, nicht als Hash. Reine Formatierungsunterschiede werden benannt und ohne
   Entscheidung durch den Maker-Text ersetzt.
3. Einordnung für die Entscheidung, drei Fälle: **überflüssig** (der neue Maker-Text enthält die Regel
   jetzt selbst), **Widerspruch** (die Lernung steht gegen eine neuere Maker-Regel), **Kandidat**
   (sonst). Das ist Prosa für die Session, kein Code.
4. Entscheidung je Ziel: **behalten** oder **Maker-Text**.
5. `behalten` heißt: dieses Ziel wird in diesem Lauf nicht geschrieben.

Kein Eintrag in `installation.json`, der die Entscheidung für spätere Läufe festhält.

### B2 `references/update_team.py` — `--keep` gehört in `prepare`, nicht in `apply`

Grund: `apply` erzeugt das Proposal neu und vergleicht alle Schlüssel einschließlich `entries`
(`:754`, `:756-758`); `merged` ist Teil von `entries` (`:712`). Ein `--keep`, das erst beim Schreiben
wirkt, lässt den Vergleich scheitern **[N1]**.

- Neues wiederholbares Argument `--keep <absoluter Zielpfad>` am **`plan`**-Parser.
- `prepare` prüft jeden Pfad gegen `adaptations` (`:707`); ein Pfad ohne Abweichung bricht mit Meldung
  ab (sonst Phantom-Abweichung im Folgelauf) **[F5]**.
- `prepare` setzt für behaltene Ziele `merged := lokale Bytes` und schreibt die Entscheidung als
  sortierte Liste `keep` ins Proposal. Damit enthält das geprüfte Proposal den Behalt-Zustand.
- `apply` liest `keep` aus dem Proposal, reicht es an den Rebuild weiter und vergleicht `keep` mit
  (`:756`). Kein neues Argument an `apply`, kein Ausschluss aus der Integritätsprüfung.
- Wirkung im Write-Loop unverändert: `:793` überspringt, weil `digest(merged) == before_hash`;
  Readback `:798-800` stimmt; Journal `:763-778` führt je Ziel `kept: true`; Rollback `:846-863`
  bleibt gültig.
- Buchführung: `baseline` = neuer Maker-Blob (`:795`), `installed_hash` = `digest(new)` — **nicht**
  `digest(merged)` **[F2]**.

### B3 Tests

- `test_update_team.py`: `settings` im Proposal; `plan --keep` auf ein `adaptations`-Ziel setzt
  `merged` auf die lokalen Bytes und führt `keep` im Proposal; `apply` mit diesem Proposal läuft
  durch, Ziel byte-gleich, Journal `kept`; `--keep` auf ein unverändertes Ziel bricht ab; zweites
  Proposal meldet dasselbe Ziel erneut; Ziel-Manifest ohne `settings` bricht ab; **Regressionsfall:**
  ein Bestandsteam, dessen aufgezeichnetes altes Manifest kein `settings` hat, plant erfolgreich
  **[N11]**.
- `test_build_evidence.py:114-117`: die vier Sätze auf die Fassung aus A3 umstellen (dort stehen sie,
  nicht in `test_render_reasoning.py`) **[N10]**; `:104` bleibt unverändert, weil der Schrittname
  bleibt.
- `test_render_reasoning.py`: `:710-712` unverändert; **`:1293`** auf die neue Fassung von
  `update.md:110` umstellen **[N2]**; Manifest-Wert == `setup.md`-Wert == SOUL-Zahl; beide
  `timeouts.tools`-Werte gegen `setup.md:109-110` binden.

---

## 4. Bericht je Lauf

Datei `runs/<run-id>/report.md`, Kopie nach
`devteam/reports/update-<JJJJ-MMTT>-<maker-version>-<run-id>.md` (Verzeichnis 0700, Datei 0600,
`update.md:49`).

1. Kopfzeile: Maker alt → neu (Version, Commit), Team, Datum.
2. Ziele: je Datei `ersetzt` / `behalten` / `unverändert`.
3. Lernungen: je behaltenem Ziel Pfad, installierte Version und der geänderte Text (Diff gegen die
   Baseline). `DEMO_PASSWORD` wird als `<DEMO_PASSWORD>` maskiert.
4. Settings: je Profil und Schlüssel `Ist → Soll`, ob gesetzt, bei `pending` der Grund.
5. `obsolete`-Liste mit lokalem Zustand je Pfad.

Kein Bericht bei `--activity-decision skip`: dann entsteht kein Run-Verzeichnis.

---

## 5. Grenzen (bewusst, keine offenen Punkte)

- **Je Datei, nicht je Learning:** `--keep` wirkt auf eine Datei (`update_team.py:335-336`). Zwei
  Sätze in einer SOUL sind nur gemeinsam behaltbar; eine Teilauswahl verlangt, die Datei vor dem Lauf
  zu bearbeiten — dann ist die Abweichung wieder eine. **[F16, offengelegt]**
- **Ein behaltenes Ziel trägt später den Maker-Fortschritt mit:** die Baseline wandert auf den neuen
  Maker-Text, der Folgelauf zeigt Lernung und neue Maker-Regeln als eine Abweichung. Welche Zeilen aus
  der neuen Maker-Fassung stammen, zeigt sich am Maker-Diff (`git diff <alt>..<neu>`), nicht am
  Bericht — dafür wird kein Zustand geführt. **[F17, korrigiert]**
- **Rechte des Ausführenden:** das Update läuft mit den Rechten des Agenten, der es durchführt.
  Verlangt die Laufzeit für `config set` eine Freigabe, wartet der Schritt, wird bestätigt oder als
  `pending` berichtet. Eine Allowlist-Ergänzung ist optional und nicht Teil dieses Plans.

---

## 6. Version, Rollout, Rückweg

- **3.1.0** (MINOR): `manifest.json`, `SKILL.md:4`; `README.md`/`NOTICE.md` führen keine Paketversion.
- **Rollout:** ein Update-Lauf je Team; bei SG1 sind die Wartewerte gesetzt → Reads ohne Schreibzugriff.
- **Rückweg:** Manifest-Block und Codeänderung zurücknehmen; gesetzte Werte über die im Bericht
  notierten Ist-Werte; Berichte bleiben liegen.

## 7. Prüfschritte

1. `test_update_team.py`, `test_build_evidence.py`, `test_render_reasoning.py`, danach die volle Suite.
2. Proposal-Probe: `plan --keep` auf ein Testziel, `apply` mit demselben Proposal, Bericht mit fünf
   Abschnitten.
3. Erster echter Lauf: Settings-Zeile `14400 → 14400`, „keine Änderung"; `kept` leer.

## 8. Nicht angefasst

SOUL- und Skill-Templates, `render_text.py` (gehasht geprüft, `:631-635`), Rollenverhalten, Plugins,
CBM/Graphify, Hindsight.

---

## 9. Zuordnung v1-Befunde

| Befund | Stand in v3 |
|---|---|
| F1 / F2 (`merged := lokal`, `installed_hash = digest(new)`) | §3 B2 |
| F3 / F4 (Manifest-Nur-Ziel, Integritätsliste) | §2 A2 |
| F5 (`--keep` nur `adaptations`) | §3 B2 |
| F6 / F7 (0700, Maskierung) | §4 |
| F8 / F10 (`update.md`-Stellen, Vertragstests) | §2 A3, §3 B3 |
| F9 (eine `config set terminal.timeout`-Zeile) | §2 A4 |
| F11 (Umfang) | §2 A1, §4 |
| F12 / F13 (Berechtigung, `pending`) | §2 A3, §5 |
| F14 (`timeouts.tools` gebunden) | §3 B3 |
| F15 (`kanban.auto_subscribe_on_create`) | §2 A1 |
| F16 / F17 (Granularität, Maker-Fortschritt) | §5, korrigiert |
| F18 (`<run-id>`, Skip, Readback-Ort) | §2 A3, §4 |
| F19 (Fundstellen) | §1 |

## 10. Zuordnung v2-Befunde

| Befund | Erledigt in |
|---|---|
| N1 `--keep` unvereinbar mit dem Proposal-Rebuild | §3 B2 — Argument an `plan`, `keep` im Proposal, `apply` rebuildet damit |
| N2 `test_render_reasoning.py:1293` pinnt `:110` | §1, §3 B3 |
| N3 `update.md:88` widerspricht der Ausnahme | §2 A3 (Zielwortlaut) |
| N4 Pflichtschritt vs. `skip` | §2 A3 Nr. 1 |
| N5 Bericht nicht in der Prozedur verankert | §2 A3 (neuer Schritt) |
| N6 Ersatzwortlaut für `:106`/`:113` fehlt | §2 A3 |
| N7 Begründung zu `security.protected_instruction_files` | §2 A1 |
| N8 Beleg „`timeouts.tools` ist ein Objekt" | §2 A3 (Prüfung „kein Skalar") |
| N9 `manifest.json:2-5` zu eng | §1 (alle Schlüsselstellen einzeln) |
| N10 B3 ordnet die vier Sätze der falschen Testdatei zu | §3 B3 |
| N11 Regressionsfall altes Manifest ohne `settings` | §3 B3 |
