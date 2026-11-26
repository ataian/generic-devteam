# PLAN 3.1.0 — Updater: Sollwerte setzen, Lernungen melden (v4)

**Ziel:** Ein Team-Update setzt die vom Maker festgelegten Profileinstellungen auf ihren Sollwert und
meldet die vom Team gelernten Textänderungen in SOULs und Skills, damit der User je Ziel entscheidet,
ob sie erhalten bleiben oder der Maker-Text gilt. Kein Zustand über Läufe; der Abschlussbericht ist
Ablage.

**Nicht Ziel:** keine Änderung an SOUL- oder Skill-Texten, Rollenverhalten, Auto-Load, Plugins, Hermes,
CBM, Hindsight; kein Kartenbudget (Planner, `kanban-phase-release.md` Schritte 3 und 4).

**v4 nach `REVIEW_3.1.0_..._v3.md`:** M1–M5 eingearbeitet. N1–N11 und F1–F19 bleiben erledigt;
Zuordnung in §9–§11.

---

## 1. Ist-Stand (Fundstellen gegen HEAD `6667c34`)

| Punkt | Fundstelle |
|---|---|
| Setup setzt die Wartewerte bereits, das Update verlangt eine Freigabe | `setup.md:103-113` (Prosa `:103`/`:105`, Kommandos `:108-110`, Readbacks `:111-113`), `update.md:282` |
| Kein maschinenlesbarer Sollwert | `manifest.json`: `:2-5` (`name`, `version`, `recovery_launcher`, `stage`), `:6` (`files`), `:84` (`role_templates`), `:172` (`own_skills`), `:378` (`upstream_components`); kein `settings` |
| Dateihelfer schreibt keine Konfiguration | `update_team.py:3`; `update.md:8` |
| Abweichung wird gemeldet und ersetzt | `update.md:106` (drei Aussagen: authoritative · `adaptations` + Version · Konfliktsatz), `:110` letzter Satz, `:113` (inkl. Satz über fehlende Baseline); `update_team.py:705-708` |
| `apply` schreibt jedes Ziel; einzige Übersprung-Bedingung `merged == before_hash` | `update_team.py:789-794` |
| `apply` baut das Proposal neu und vergleicht schlüsselweise, `merged` inbegriffen | `update_team.py:754`, `:756-758`; `merged` entsteht in `prepare` `:705`, in `entries` `:712` |
| `installed_hash` speist die Retirement-Klassifikation | `update_team.py:607`, `:613` → `candidate_state` (`:536-578`); `update.md:294-295` |
| `prepare` schreibt je Aufruf ein neues Proposal | `update_team.py:721-723` |
| `prepare` lädt altes **und** neues Manifest | `:636` (über `desired`), `:683` (alt); `:650`, `:684` (neu) |
| Proposal-Integritätsliste | `update_team.py:756` |
| Vertragstests | `test_build_evidence.py:104` (Schrittname), `:114-117` (vier Klauseln); `test_render_reasoning.py:710-712` (Schrittname/Position), `:1293` (`update.md:110`) |
| Der einzige dokumentierte `plan`-Aufruf | `update.md:103` |
| Skip-Fall | `update.md:259` |

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

Aufgenommen, weil `setup.md:79`/`:94` sie unbedingt für alle drei Rollen setzt (Readback `:99`). Die
Werte gelten für **alle Profile des Blocks**, den Planner eingeschlossen **[M3]**. Draußen:
`model.*`, `agent.reasoning_effort`, `terminal.cwd`, `memory.provider`, Mattermost-Bindung
(Kundenentscheidungen); `security.protected_instruction_files` (`setup.md:123` „if needed and
authorized", `:126` ein `config set` — autorisierungsgebunden, zentral erfüllbar);
`skills.creation_nudge_interval` (eigener Schritt, `update.md:118`). Kein `maker_version` im Block.

### A2 `references/update_team.py`

- `settings` aus dem **Ziel**-Manifest lesen (`:650`/`:684`). Fehlt `settings` dort, bricht der Lauf
  ab; fehlt es im alten Manifest, ist das kein Fehler.
- Proposal-Block `settings` (Rolle → Schlüssel → Sollwert), keine Istwerte, keine CLI-Aufrufe.
- Integritätsliste `:756` um `'settings'` und `'keep'` erweitern. **`keep` steht in jedem Proposal**,
  auch leer und sortiert — sonst liefert der Schlüsselvergleich `KeyError` statt der Drift-Meldung
  **[F-N1]**.

### A3 `references/update.md` — Zielwortlaute

- **`:8`**: Satz bleibt; Ergänzung: „The settings reconciliation in Activity and application is a
  mandatory step of this procedure, not a separate approved step."
- **`:88`** (frei änderbar): „Note the settings for every profile of this team from
  `manifest.json → settings`; they are reconciled in Activity and application and need no scope
  decision." **[M3]**
- **`:103`** und **`:106`** — Behalt-Entscheidung verankern **[M2]**: Der erste `plan`-Aufruf
  (`:103`) liefert das Proposal mit den `adaptations`. Nach der Entscheidung wird **erneut** geplant:
  `plan --keep <pfad>` (ein Pfad je behaltenem Ziel) und **dieses** Proposal wird angewendet. Der
  erste Aufruf ist die Inspektionsvorlage; das zweite Proposal trägt den Behalt-Zustand, und nur es
  darf `apply` erhalten. Wird das erste angewendet, ersetzt der Maker-Text die Lernung — dieser Satz
  gehört als Warnung in `:106`.
- **`:117`**: „Runtime configuration and integration changes need their applicable authorization,
  except the settings reconciliation: it is a mandatory step of this procedure, runs with the
  executing agent's permissions, and stays `pending` when the runtime refuses."
- **`:106`** — Aussage (c) **bleibt wörtlich stehen** **[M1]**: „A missing managed target, or an
  unmanaged same-name file at a new target, remains a conflict and stops application."
- **`:110`** letzter Satz → „A current managed target is not obsolete: its local edit is an
  adaptation that the approved decision either replaces or retains."
- **`:113`** → „Inspect every `adaptations` entry with its path and installed Maker version. Local
  SOUL or skill text survives the update only when the approved decision retains it; otherwise the
  Maker output replaces it. A locally modified file with no recorded baseline remains unknown and is
  not an adaptation." (Der letzte Satz bleibt **[M4]**, weil `legacy_skills_unknown` ihn trägt:
  `update_team.py:135`, `:636`, `:673`, `:719`.)
- **`:282`** — Schritt heißt künftig **„Reconcile the profile settings"** (der Name deckt jetzt auch
  den Kanban-Wert) **[M3]**:
  1. nur bei `--activity-decision proceed`; bei `skip` bleibt das Team unverändert (`:259`)
  2. je Profil aus `settings` und Schlüssel `hermes -p <profil> config get` lesen
  3. **Vergleich normalisiert:** Sollwert und Ausgabe werden als Text verglichen, nach Trim und
     ohne Beachtung der Groß-/Kleinschreibung bei booleschen Werten (`true`/`false`) **[M5]**;
     Abweichung heißt: die normalisierten Texte sind ungleich
  4. bei Abweichung den alten Wert für den Bericht notieren und auf Soll setzen
  5. alle Schlüssel zurücklesen, im privaten Setup-Record festhalten (`templates/setup-record.md:42`)
  6. Ist → Soll im Bericht ausweisen
  Ist ein Profil nicht vorhanden, schlägt `config get` fehl oder ist der Wert kein Skalar, gilt das
  `pending`-Muster aus `:127`.
- **Neuer Schritt „Write the run report"** in „Activity and application", nach dem Settings-Abgleich;
  Datei, Ort, Modus und Inhalt wie §4.

### A4 `references/setup.md`

`:103-113` bleibt im Wortlaut (genau **eine** Zeile `config set terminal.timeout`,
`test_render_reasoning.py:681`) und erhält eine Quellenzeile: die Werte stehen in
`manifest.json → settings`; bei Abweichung gilt das Manifest.

---

## 3. Teil B — Lernungen melden und entscheiden

### B1 Ablauf (verankert in `update.md:103`/`:106`, siehe A3)

1. Je verwaltetes SOUL-/Skill-Ziel lokal gegen die Pristine-Baseline stellen.
2. Jede Abweichung melden: Pfad, installierte Maker-Version und **was die Rolle ergänzt oder geändert
   hat** — inhaltlich, nicht als Hash. Reine Formatierungsunterschiede werden benannt und ohne
   Entscheidung durch den Maker-Text ersetzt.
3. Einordnung: **überflüssig** (der neue Maker-Text enthält die Regel jetzt selbst), **Widerspruch**
   (Lernung gegen eine neuere Maker-Regel), **Kandidat** (sonst). Prosa für die Session, kein Code.
4. Entscheidung je Ziel: **behalten** oder **Maker-Text**.
5. `behalten` heißt: dieses Ziel wird in diesem Lauf nicht geschrieben.

Kein Eintrag in `installation.json`, der die Entscheidung für spätere Läufe festhält.

### B2 `references/update_team.py` — `--keep` am `plan`-Parser

- Neues wiederholbares Argument `--keep <absoluter Zielpfad>` am `plan`-Parser; `prepare` bekommt die
  Liste und prüft jeden Pfad gegen `adaptations` (`:707`) — ein Pfad ohne Abweichung bricht ab
  (sonst Phantom-Abweichung im Folgelauf).
- `prepare` setzt für behaltene Ziele `merged := lokale Bytes` (`:705`) und schreibt `keep` sortiert
  ins Proposal (`:714-720`). Damit enthält das geprüfte Proposal den Behalt-Zustand.
- `apply` liest `keep` aus dem Proposal, reicht es an den Rebuild weiter
  (`prepare(proposal['repo'], home, proposal['maker_commit'], keep)`, `:754`) und vergleicht `keep`
  mit (`:756`). Kein neues Argument an `apply`, keine Abschwächung der Integritätsprüfung.
- Write-Pfad unverändert: `:793` überspringt (weil `digest(merged) == before_hash`), Readback
  `:798-800` stimmt, Journal `:763-778` führt je Ziel `kept: true`, Rollback `:846-863` bleibt gültig.
- Buchführung: `baseline` = neuer Maker-Blob (`:795`), `installed_hash` = `digest(new)`.

### B3 Tests

- `test_update_team.py`: `settings` im Proposal; `keep` in jedem Proposal (auch leer, sortiert);
  `plan --keep` auf ein `adaptations`-Ziel setzt `merged` auf die lokalen Bytes; `apply` mit diesem
  Proposal läuft durch, Ziel byte-gleich, Journal `kept`; `--keep` auf ein unverändertes Ziel bricht
  ab; zweites Proposal meldet dasselbe Ziel erneut; Ziel-Manifest ohne `settings` bricht ab;
  **Regressionsfall:** Bestandsteam mit altem Manifest ohne `settings` plant erfolgreich.
- `test_build_evidence.py`: `:114-117` **bleibt unverändert** — die vier Klauseln sind mit A3
  weiterhin erfüllt (a wörtlich, b als Teilphrase, c bleibt, d wörtlich in `:113`) **[M1]**.
  `:104` wird auf den neuen Schrittnamen umgestellt.
- `test_render_reasoning.py`: `:710-712` auf den neuen Schrittnamen und die unveränderte Position
  umstellen; `:1293` auf die neue Fassung von `update.md:110`; Manifest-Wert == `setup.md`-Wert ==
  SOUL-Zahl; beide `timeouts.tools`-Werte gegen `setup.md:109-110` binden.

---

## 4. Bericht je Lauf

Datei `runs/<run-id>/report.md`, Kopie nach
`devteam/reports/update-<JJJJ-MMTT>-<maker-version>-<run-id>.md` (Verzeichnis 0700, Datei 0600).

1. Kopfzeile: Maker alt → neu (Version, Commit), Team, Datum.
2. Ziele: je Datei `ersetzt` / `behalten` / `unverändert`.
3. Lernungen: je behaltenem Ziel Pfad, installierte Version und der geänderte Text (Diff gegen die
   Baseline); `DEMO_PASSWORD` als `<DEMO_PASSWORD>` maskiert.
4. Settings: je Profil und Schlüssel `Ist → Soll`, ob gesetzt, bei `pending` der Grund.
5. `obsolete`-Liste mit lokalem Zustand je Pfad.

Kein Bericht bei `--activity-decision skip`.

---

## 5. Grenzen (bewusst)

- **Je Datei, nicht je Learning:** `--keep` wirkt auf eine Datei (`update_team.py:335-336`); zwei
  Sätze einer SOUL sind nur gemeinsam behaltbar, eine Teilauswahl verlangt das Bearbeiten der Datei
  vor dem Lauf.
- **Ein behaltenes Ziel trägt später den Maker-Fortschritt mit:** die Baseline wandert auf den neuen
  Maker-Text; welche Zeilen aus der neuen Fassung stammen, zeigt der Maker-Diff
  (`git diff <alt>..<neu>`), nicht der Bericht — dafür wird kein Zustand geführt.
- **Rechte des Ausführenden:** das Update läuft mit den Rechten des Agenten, der es durchführt.
  Verweigert die Laufzeit `config set`, wartet der Schritt, wird bestätigt oder als `pending`
  berichtet. Eine Allowlist-Ergänzung ist optional und nicht Teil dieses Plans.

---

## 6. Version, Rollout, Rückweg

- **3.1.0** (MINOR): `manifest.json`, `SKILL.md:4`.
- **Rollout:** ein Update-Lauf je Team; bei SG1 sind die Wartewerte gesetzt → Reads ohne Schreibzugriff.
- **Rückweg:** Manifest-Block und Codeänderung zurücknehmen; gesetzte Werte über die im Bericht
  notierten Ist-Werte.

## 7. Prüfschritte

1. `test_update_team.py`, `test_build_evidence.py`, `test_render_reasoning.py`, danach die volle Suite.
2. Proposal-Probe: `plan` → `plan --keep` auf ein Testziel → `apply` mit dem zweiten Proposal;
   Bericht mit fünf Abschnitten.
3. Erster echter Lauf: Settings-Zeile `14400 → 14400`, „keine Änderung"; `kept` leer.

## 8. Nicht angefasst

SOUL- und Skill-Templates, `render_text.py` (gehasht geprüft, `:631-635`), Rollenverhalten, Plugins,
CBM/Graphify, Hindsight.

---

## 9. Zuordnung v1-Befunde

F1–F19 erledigt; Stand je Befund unverändert zu v3 (§9 dort), F16/F17 als Grenze in §5.

## 10. Zuordnung v2-Befunde

N1–N11 erledigt; Stand unverändert zu v3 (§10 dort). `keep` steht jetzt in jedem Proposal.

## 11. Zuordnung v3-Befunde

| Befund | Erledigt in |
|---|---|
| M1 Konfliktsatz in `:106` weggeschnitten, B3-Änderung an `:114-117` unnötig | §2 A3 (`:106`, Aussage c bleibt), §3 B3 (keine Änderung an `:114-117`) |
| M2 Behalt-Entscheidung in `update.md` nicht verankert, zwei `plan`-Aufrufe | §2 A3 (`:103`/`:106`), §7 Nr. 2 |
| M3 Planner in `settings`, Prozedur nur Coder/Reviewer | §2 A1, A3 (`:88`, Schrittname „Reconcile the profile settings") |
| M4 Satz über fehlende Baseline in `:113` verloren | §2 A3 (Satz bleibt) |
| M5 Vergleichsregel Ist ↔ Soll fehlt | §2 A3 Nr. 3 (normalisierter Textvergleich) |
