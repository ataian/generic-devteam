# PLAN 3.1.0 — Updater: Sollwerte setzen, Lernungen melden

**Ziel:** Ein Team-Update soll zwei Dinge selbst tun und am Ende darüber berichten:
(1) die vom Maker festgelegten Profileinstellungen auf ihren Sollwert **setzen** (heute nur Prosa,
im letzten Lauf übersprungen); (2) die vom Team über die Zeit **gelernten Textänderungen** in SOULs
und Skills melden und je Ziel vom User entscheiden lassen, ob sie in diesem Lauf erhalten bleiben
oder durch den Maker-Text ersetzt werden. Kein Zustand, keine Liste, kein Diff-Archiv für spätere
Läufe — die nächste Session erkennt dieselben Abweichungen von selbst wieder.

**Nicht Ziel:** keine Änderung an SOUL- oder Skill-Texten, an Rollenverhalten, Auto-Load, Plugins,
Hermes, CBM, Hindsight; kein Kartenbudget (das setzt und prüft der Planner, siehe
`skills/brownfield-feature-planning/references/kanban-phase-release.md` Schritte 3 und 4).

**Anlass:** Lauf 11 (SG1, Maker 3.0.4). Der Warteabgleich wurde beim Update mit „bereits belegt"
abgewählt (`b15b353a`), und lokale Rollentexte werden ersatzlos überschrieben
(`update.md:106`, `:113`; `update_team.py`: `merged, conflict = new, False`).

---

## 1. Ist-Stand, auf dem der Plan aufsetzt

| Punkt | Fundstelle |
|---|---|
| Sollwerte stehen nur als Prosa | `references/setup.md:103-111`, `references/update.md:282` |
| Kein maschinenlesbarer Sollwert im Manifest | `manifest.json` (nur `files`, `role_templates`, `own_skills`, `upstream_components`) |
| Dateihelfer schreibt keine Konfiguration | `references/update_team.py:3`; `references/update.md:8` |
| Update verlangt für Settings eine eigene Freigabe | `references/update.md:282` („obtain authorization") |
| Abweichungen werden gemeldet und dann ersetzt | `references/update.md:106`, `:113`; `adaptations` = `{path, version, state}` |
| `apply` schreibt jedes Ziel, kein Ausschluss | `update_team.py` (`for entry in proposal['entries']` … `atomic(entry['target'], merged, …)`) |
| Ein Test bindet `setup.md` an die SOUL-Zahl, nicht an ein Manifest | `references/test_render_reasoning.py:672-700` |

---

## 2. Teil A — Sollwerte

### A1 `manifest.json`

Neuer Block; nur Werte, die dem Maker gehören:

```json
"settings": {
  "coder":    { "terminal.timeout": 14400,
                "timeouts.tools.sequential_call": 15000,
                "timeouts.tools.concurrent_batch": 15000 },
  "reviewer": { "terminal.timeout": 14400,
                "timeouts.tools.sequential_call": 15000,
                "timeouts.tools.concurrent_batch": 15000 }
}
```

Bewusst nicht enthalten: `model.*`, `agent.reasoning_effort`, `terminal.cwd`, `kanban.*`,
`memory.provider`, Mattermost-Bindung (Kundenentscheidungen) sowie
`skills.creation_nudge_interval` (bleibt eigener, autorisierungspflichtiger Schritt nach
`update.md:118`).

### A2 `references/update_team.py`

- `settings` aus dem Manifest lesen, ins Proposal als `settings` schreiben (Sollwerte je Profil,
  plus `maker_version`). Keine Istwerte — der Helfer ist stdlib + Git.
- Keine Schreibzugriffe auf `config.yaml`, keine CLI-Aufrufe. Die Dateitransaktion bleibt wie sie ist.
- Ein Manifest ohne `settings` bricht mit klarer Meldung ab; kein stiller Default.

### A3 `references/update.md`

- `:8` neu formulieren: der Dateihelfer ändert keine Konfiguration; der **Update-Ablauf** setzt sie.
- `:282` ersetzen durch einen Pflichtschritt ohne Ermessensspielraum:
  1. je Profil die drei Schlüssel mit `hermes -p <profil> config get` lesen,
  2. gegen `manifest.json → settings` stellen,
  3. bei Abweichung den alten Wert für den Bericht notieren und auf Soll setzen,
  4. alle drei zurücklesen,
  5. Ist → Soll je Schlüssel im Bericht ausweisen (Abschnitt 4).
  Der Schritt ist nicht über den Umfang abwählbar; `--dependency-decision` gilt weiter nur für
  abhängige Dateien.
- Hinweis aufnehmen: der Lauf braucht die `config set`-Berechtigung, sonst hängt der Schritt an
  einem Freigabedialog.

### A4 `references/setup.md`

`:103-111` bleibt im Wortlaut, erhält eine Quellenzeile: die Werte stehen in
`manifest.json → settings`; bei Abweichung gilt das Manifest.

---

## 3. Teil B — Lernungen melden und entscheiden

### B1 `references/update.md`

`:106` und `:113` so umschreiben, dass die Entscheidung Teil des Ablaufs ist:

1. Je verwaltetes SOUL-/Skill-Ziel lokal gegen die Pristine-Baseline stellen.
2. Jede Abweichung melden: Pfad, installierte Maker-Version und **was die Rolle ergänzt oder
   geändert hat** — die inhaltliche Beschreibung, nicht der Hash. Reine Formatierungs- oder
   Umschreibungsunterschiede ohne Bedeutungsänderung werden als solche benannt und ohne
   Entscheidung durch den Maker-Text ersetzt.
3. Entscheidung des Users je Ziel: **behalten** oder **Maker-Text**.
4. `behalten` heißt: dieses Ziel wird in diesem Lauf nicht geschrieben. Alles andere wird
   geschrieben wie bisher.

Kein Eintrag in `installation.json`, der die Entscheidung für spätere Läufe festhält. Die
nächste Update-Session stellt denselben Vergleich erneut an und meldet dieselbe Abweichung wieder
— gewollt.

### B2 `references/update_team.py`

- Neues wiederholbares Argument `--keep <absoluter Zielpfad>` für `apply`. Jeder Pfad muss in
  `entries` vorkommen; unbekannter Pfad bricht ab.
- `apply` überspringt gekennzeichnete Ziele beim Schreiben. Für sie gilt:
  `installed_hash` = lokaler Hash, `baseline` = neuer Maker-Blob. Damit ist der nächste Vergleich
  korrekt und die Abweichung bleibt sichtbar (kein Zustand, nur die vorhandene Buchführung).
- Journal: Liste `kept` mit Pfad und Hash; `files[]` führt das Ziel mit `kept: true`.
- Alles andere unverändert: Backups, Drift-Prüfung, Readback, Rollback.

### B3 Tests

- `references/test_update_team.py`:
  - Proposal enthält `settings` mit den drei Schlüsseln je Rolle.
  - `--keep` verhindert das Schreiben, Ziel bleibt byte-gleich, `kept` erscheint im Journal.
  - ein zweites Proposal nach `--keep` meldet dasselbe Ziel erneut als `adaptation`.
  - Manifest ohne `settings` bricht mit Meldung ab.
- `references/test_render_reasoning.py`:
  - `test_wait_window_matches_the_configured_terminal_timeout` erweitern: Manifest-Wert ==
    `setup.md`-Wert == SOUL-Template-Zahl.
  - die drei `config set`-Zeilen bleiben in `setup.md` vorhanden.

---

## 4. Bericht je Update-Lauf

Neues Artefakt, nur Ablage, keine Lesegrundlage für den Updater:

- Datei `runs/<run-id>/report.md`, zusätzlich Kopie nach `devteam/reports/update-<JJJJ-MMTT>-<maker-version>.md` (Modus 0600).
- Inhalt:
  1. Maker-Alt → Neu (Version, Commit), Team, Zeitraum.
  2. **Ziele:** je Datei `ersetzt` / `behalten` / `unverändert`.
  3. **Lernungen:** je behaltenem Ziel Pfad, installierte Version und der geänderte Text
     (Diff gegen die Baseline) — damit die Entscheidung nachvollziehbar bleibt.
  4. **Settings:** je Profil und Schlüssel `Ist → Soll` und ob gesetzt wurde.
  5. Offene Punkte und Abweichungen (Konflikte, übersprungene Schritte) sowie die
     `obsolete`-Liste mit lokalem Zustand je Pfad — dieselbe Meldung, die der Helfer schon
     erzeugt, damit auch das Verschwinden von Dateien im Bericht steht.
- Der Bericht wird vom Update-Ablauf geschrieben, nicht vom Helfer ausgewertet.

---

## 5. Version, Doku, Rollout, Rückweg

- **Version 3.1.0** (MINOR): `manifest.json`, `README.md`, `NOTICE.md`, Versionszeile in `SKILL.md`.
- **Rollout:** ein Update-Lauf je Team. Bei SG1 sind die Settings bereits korrekt → drei Reads,
  keine Schreibzugriffe; `--keep` wird voraussichtlich nicht gebraucht (offen sind derzeit nur
  Jacks zwei Sätze und Daniels/Carters je ein Satz aus der Nacht — die Entscheidung fällt im Lauf).
- **Rückweg:** Manifest-Block und Codeänderung zurücknehmen = alter Zustand. Settings-Änderungen
  sind über die im Bericht notierten Ist-Werte reversibel; Berichte bleiben als Historie liegen.
- **Risiko:** `config set` ohne Berechtigung hängt am Dialog → im Rollout vorab prüfen.
  Ein `--keep` auf einem Ziel, dessen Baseline sich im Folgelauf ändert, wird erneut gemeldet
  (gewollt) und kann dann erneut entschieden werden.

---

## 6. Prüfschritte

1. `python3 references/test_update_team.py` und `references/test_render_reasoning.py`, danach die
   volle Suite (Stand 3.0.4: 269 Tests).
2. Proposal-Probe gegen ein Testteam: `settings` und erwartete `adaptations` sichtbar, keine
   Schreibziele außerhalb des verwalteten Satzes.
3. Erster echter Lauf: `report.md` enthält die drei Abschnitte, die Settings-Zeile zeigt
   `14400 → 14400` und `keine Änderung`.

## 7. Offene Punkte

- `skills.creation_nudge_interval` (Planner, Soll 0) bleibt nach dieser Fassung draußen; ein
  Aufnehmen würde die bestehende Festlegung „eigener autorisierungspflichtiger Schritt" ändern.
- Ob der Planner-`terminal.timeout` (180) ebenfalls Sollwert werden soll — heute schreibt Setup
  ihn nicht vor.
