# PLAN 3.1.0 — Updater: Sollwerte setzen, Lernungen melden (v2)

**Ziel:** Ein Team-Update setzt die vom Maker festgelegten Profileinstellungen auf ihren Sollwert und
meldet die vom Team gelernten Textänderungen in SOULs und Skills, damit der User je Ziel entscheidet,
ob sie erhalten bleiben oder der Maker-Text gilt. Kein Zustand über Läufe, kein Diff-Archiv als
Lesegrundlage; der Abschlussbericht ist Ablage.

**Nicht Ziel:** keine Änderung an SOUL- oder Skill-Texten, an Rollenverhalten, Auto-Load, Plugins,
Hermes, CBM, Hindsight; kein Kartenbudget (Planner, `kanban-phase-release.md` Schritte 3 und 4).

**Anlass:** Lauf 11 (SG1). Der Warteabgleich wurde mit „bereits belegt" abgewählt (`b15b353a`), lokale
Rollentexte werden ersatzlos überschrieben (`update.md:106`, `:113`).

**v2 nach Review `REVIEW_3.1.0_Updater-Settings-und-Lernpflege_v1.md` (Fujiko, 2026-11-25).**
Änderungen gegen v1 sind mit **[F<n>]** markiert; die Zuordnung steht in Abschnitt 9.

---

## 1. Ist-Stand

| Punkt | Fundstelle |
|---|---|
| Sollwerte der Wartekonfiguration: Setup setzt sie bereits, das Update verlangt eine Freigabe | `setup.md:103-113` (Prosa `:103`, `:105`; Kommandos `:108-110`; Readbacks `:111-113`), `update.md:282` |
| Kein maschinenlesbarer Sollwert | `manifest.json` trägt `name`, `version`, `recovery_launcher`, `stage`, `files`, `role_templates`, `own_skills`, `upstream_components` (`:2-5`) — kein `settings` **[F19]** |
| Dateihelfer schreibt keine Konfiguration | `update_team.py:3`; `update.md:8` |
| Abweichungen werden gemeldet und dann ersetzt | `update.md:106`, `:110` (letzter Satz), `:113`; `update_team.py:705-708` |
| `apply` schreibt jedes Ziel; einzige Übersprung-Bedingung ist `merged == before_hash` | `update_team.py:789-794` |
| `installed_hash` speist die Retirement-Klassifikation | `update_team.py:607`, `:613` → `candidate_state` (`:555-578`); `update.md:294-295` |
| `prepare` rendert altes **und** neues Manifest | `update_team.py:636`, `:683` (alt), `:650`, `:684` (neu) |
| Proposal-Integritätsliste | `update_team.py:756` |
| Test bindet `setup.md` an die SOUL-Zahl, nicht an ein Manifest | `test_render_reasoning.py:672-704` |
| Vertragstests pinnen die Sätze aus `update.md:106`/`:113` und den Schrittnamen | `test_build_evidence.py:104`, `:111-120`; `test_render_reasoning.py:710-712` |

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

Aufgenommen, weil der Maker sie unbedingt vorschreibt: `kanban.auto_subscribe_on_create: false`
(`setup.md:94`, kein Kundenentscheid) **[F15]**. Bewusst draußen: `model.*`, `agent.reasoning_effort`,
`terminal.cwd`, `memory.provider`, Mattermost-Bindung (Kundenentscheidungen);
`security.protected_instruction_files` (in `setup.md:123-126` als wirksamer Wert und Schutz
beschrieben, nicht als Einstellung); `skills.creation_nudge_interval` (eigener
autorisierungspflichtiger Schritt, `update.md:118`).

Kein `maker_version` im Block — das Proposal führt ihn bereits als eigenen Schlüssel
(`update_team.py:715`) **[F11]**.

### A2 `references/update_team.py`

- `settings` aus dem **Ziel**-Manifest lesen (derselbe `blob(repo, commit, 'manifest.json')`-Zugriff wie
  `role_templates`, `:650`/`:684`); das Manifest des alten Commits bleibt unberührt **[F3]**.
- Fehlt `settings` im Ziel-Manifest, bricht der Lauf mit klarer Meldung ab — nur dort, nicht an einer
  gemeinsamen Ladestelle.
- Ins Proposal einen Block `settings` schreiben (Rolle → Schlüssel → Sollwert). Keine Istwerte, keine
  CLI-Aufrufe, keine Schreibzugriffe auf `config.yaml`.
- Die Integritätsliste in `apply` (`:756`) um `'settings'` erweitern **[F4]**.

### A3 `references/update.md`

- **`:8`**: Satz bleibt (Dateihelfer ändert keine Konfiguration) und bekommt eine Abgrenzung: der
  Settings-Abgleich in „Activity and application" ist **Pflichtschritt dieser Prozedur**, kein
  „separate approved step" **[F10]**.
- **`:117`**: Ausnahme ausdrücklich formulieren: der Settings-Abgleich braucht keine
  Umfangsentscheidung; er läuft mit den Rechten des ausführenden Agenten. Verweigert die Laufzeit das
  Kommando oder läuft die Freigabe ab, bleibt der Schritt `pending` und wird berichtet — nicht
  stillschweigend übersprungen **[F10][F12][F13]**.
- **`:282`** (Name des Schritts bleibt, damit `test_render_reasoning.py:710-712` gültig bleibt):
  1. je Profil und Schlüssel `hermes -p <profil> config get` lesen,
  2. gegen `manifest.json → settings` stellen,
  3. bei Abweichung alten Wert für den Bericht notieren, auf Soll setzen,
  4. alle Schlüssel zurücklesen und im privaten Setup-Record festhalten (wie bisher),
  5. Ist → Soll im Bericht ausweisen (Abschnitt 4).
  Fehlt ein Profil, schlägt `config get` fehl oder liefert keinen Skalar (`timeouts.tools` ist ein
  Objekt, `setup.md:103`), gilt das `pending`-Muster aus `update.md:127`: Dateien bleiben aktualisiert,
  der Lauf meldet „settings not reconciled: <Grund>" **[F13]**.
- **`:110`** letzter Satz: „… its local edit is an adaptation that the approved scope **either replaces
  or retains**." **[F10]**

### A4 `references/setup.md`

`:103-113` bleibt im Wortlaut (insbesondere genau **eine** Zeile `config set terminal.timeout`,
`test_render_reasoning.py:681` **[F9]**) und erhält eine Quellenzeile: die Werte stehen in
`manifest.json → settings`; bei Abweichung gilt das Manifest.

---

## 3. Teil B — Lernungen melden und entscheiden

### B1 `references/update.md` (`:106`, `:113`)

1. Je verwaltetes SOUL-/Skill-Ziel lokal gegen die Pristine-Baseline stellen.
2. Jede Abweichung melden: Pfad, installierte Maker-Version und **was die Rolle ergänzt oder geändert
   hat** — inhaltlich, nicht als Hash. Reine Formatierungsunterschiede werden benannt und ohne
   Entscheidung durch den Maker-Text ersetzt.
3. Entscheidung je Ziel: **behalten** oder **Maker-Text**.
4. `behalten` heißt: das Ziel wird in diesem Lauf nicht geschrieben; die Bytes im Profil bleiben.

Kein Eintrag in `installation.json`, der die Entscheidung für spätere Läufe festhält.

### B2 `references/update_team.py`

- Neues wiederholbares Argument `--keep <absoluter Zielpfad>` in `apply` (`:905-912`).
- **Zulässig nur für Ziele, die in `adaptations` stehen** — sonst entsteht beim Folgelauf eine
  Phantom-Abweichung **[F5]**. Unbekannter oder nicht abweichender Pfad bricht mit Meldung ab.
- **Wirkung im Apply:** für ein behaltenes Ziel wird `merged := lokale Bytes` gesetzt, nicht nur der
  Write „übersprungen". Dann greift `:793` von selbst (kein Write), und der Readback `:798-800` stimmt
  **[F1]**. Ein Skip ohne diese Zuweisung scheitert am Readback, nachdem andere Ziele bereits
  geschrieben sind.
- **Buchführung für behaltene Ziele:** `baseline` = neuer Maker-Blob (wie heute, `:795`), aber
  `installed_hash` = `digest(new)` — **nicht** `digest(merged)` **[F2]**. Sonst gilt die behaltene Datei
  in `candidate_state` (`:555-578`) als `pristine`, und `update.md:294` erlaubt ihre Entfernung.
- Journal: `kept`-Liste mit Pfad und Grund; `files[]` bleibt vollständig, je Ziel zusätzlich
  `kept: true` (`:763-778` unverändert in der Struktur).
- Rollback unverändert (`:846-863` liest nur `journal['files']`).

### B3 Tests

- `test_update_team.py`: Proposal enthält `settings`; `--keep` auf ein `adaptations`-Ziel schreibt
  nichts, Readback läuft durch, Journal führt `kept`; `--keep` auf ein unverändertes Ziel bricht ab;
  zweites Proposal meldet dasselbe Ziel erneut; Ziel-Manifest ohne `settings` bricht ab.
- `test_render_reasoning.py`: die vier gepinnten Sätze aus `update.md:106`/`:113` auf die neue Fassung
  umstellen; `:710-712` (Schrittname und Position) unverändert lassen; Manifest-Wert ==
  `setup.md`-Wert == SOUL-Zahl; **zusätzlich** die beiden `timeouts.tools`-Werte gegen die
  `config set`-Zeilen `setup.md:109-110` binden **[F8][F14]**.
- `test_build_evidence.py`: `:104` und `:111-120` auf die neue Fassung der Sätze umstellen — sonst wird
  die volle Suite rot **[F8]**.

---

## 4. Bericht je Lauf

Datei `runs/<run-id>/report.md`, Kopie nach `devteam/reports/update-<JJJJ-MMTT>-<maker-version>-<run-id>.md`
(Verzeichnis 0700, Datei 0600, `update.md:49`) **[F6][F18]**.

1. Kopfzeile: Maker alt → neu (Version, Commit), Team, Datum.
2. Ziele: je Datei `ersetzt` / `behalten` / `unverändert`.
3. Lernungen: je behaltenem Ziel Pfad, installierte Version und der geänderte Text (Diff gegen die
   Baseline). Der Wert von `DEMO_PASSWORD` wird im Bericht als `<DEMO_PASSWORD>` maskiert, weil ein
   Bericht zitiert wird und die Bytes sonst im Chat landen **[F7]**.
4. Settings: je Profil und Schlüssel `Ist → Soll` und ob gesetzt wurde; bei `pending` der Grund.
5. `obsolete`-Liste mit lokalem Zustand je Pfad (Meldung des Helfers, `update.md:110`).

Kein Bericht bei `--activity-decision skip`: dann entsteht kein Run-Verzeichnis und nichts wird
geschrieben **[F18]**.

---

## 5. Grenzen dieses Entwurfs (bewusst)

- **Je Datei, nicht je Learning:** `--keep` wirkt auf eine Datei (`update_team.py:335-336` liefert jede
  Skill-Datei einzeln). Zwei Sätze in einer SOUL sind nur gemeinsam behaltbar. Wer nur einen Satz
  behalten will, bearbeitet die Datei vor dem Lauf — dann ist die Abweichung wieder eine **[F16]**.
- **Ein behaltenes Ziel trägt später den Maker-Fortschritt mit:** Die Baseline wandert auf den neuen
  Maker-Text, deshalb zeigt der nächste Diff die Lernung **und** die inzwischen neuen Maker-Regeln als
  eine Abweichung. Der Bericht zeigt den Diff gegen den neuen Maker-Text, damit der Unterschied
  sichtbar bleibt **[F17]**.
- **Rechte des Ausführenden:** das Update läuft mit den Rechten des Agenten, der es durchführt.
  Verlangt die Laufzeit für `config set` eine Freigabe, ist das kein Planfehler; der Schritt wartet,
  wird bestätigt oder als `pending` berichtet. Eine Allowlist-Ergänzung ist optional und nicht Teil
  dieses Plans **[F12]**.

---

## 6. Version, Rollout, Rückweg

- **3.1.0** (MINOR): `manifest.json`, `SKILL.md:4` (beide tragen die Paketversion; `README.md` und
  `NOTICE.md` führen keine Versionszeile **[F19]**).
- **Rollout:** ein Update-Lauf je Team. Bei SG1 sind die Wartewerte bereits gesetzt → Reads ohne
  Schreibzugriff.
- **Rückweg:** Manifest-Block und Codeänderung zurücknehmen; gesetzte Werte über die im Bericht
  notierten Ist-Werte; Berichte bleiben als Ablage liegen.

## 7. Prüfschritte

1. `test_update_team.py`, `test_render_reasoning.py`, `test_build_evidence.py`, danach die volle Suite.
2. Proposal-Probe gegen ein Testteam: `settings` sichtbar, `--keep` nur auf `adaptations`, Bericht
   entsteht mit den fünf Abschnitten.
3. Erster echter Lauf: Settings-Zeile zeigt `14400 → 14400` und „keine Änderung"; `kept` leer.

## 8. Offene Punkte

- `skills.creation_nudge_interval` bleibt beim eigenen autorisierungspflichtigen Schritt
  (`update.md:118`).
- `security.protected_instruction_files` bleibt draußen (Schutzwert, keine Einstellung).

## 9. Zuordnung der Review-Befunde (v1 → v2)

| Befund | Erledigt in |
|---|---|
| F1 `--keep` über `merged := lokale Bytes`, nicht „Skip" | §3 B2 |
| F2 `installed_hash` bleibt `digest(new)` | §3 B2 |
| F3 Manifest-Prüfung nur am Ziel-Commit | §2 A2 |
| F4 `settings` in der Proposal-Integritätsliste | §2 A2 |
| F5 `--keep` nur auf `adaptations` | §3 B2 |
| F6 `devteam/reports/` 0700 | §4 |
| F7 `DEMO_PASSWORD` im Bericht maskieren | §4 Nr. 3 |
| F8 Vertragstests `test_build_evidence.py`/`test_render_reasoning.py` | §3 B3 |
| F9 genau eine `config set terminal.timeout`-Zeile | §2 A4 |
| F10 `update.md:8`, `:110`, `:117` | §2 A3 |
| F11 Umfang: `:8`-Neufassung begrenzt, Bericht-Nr. 1 als Kopfzeile, kein `maker_version` im Block | §2 A1, §3, §4 |
| F12 Berechtigung für `config set` | §2 A3, §5 |
| F13 fehlendes Profil / `config get`-Fehler / Objektwert → `pending` | §2 A3 |
| F14 `timeouts.tools` an `setup.md` gebunden | §3 B3 |
| F15 weitere Maker-Sollwerte (`kanban.auto_subscribe_on_create`) | §2 A1 |
| F16 Granularität je Datei | §5 |
| F17 behaltenes Ziel trägt Maker-Fortschritt | §5 |
| F18 Berichtsname, Skip-Fall, Readback-Ort | §2 A3, §4 |
| F19 drei Fundstellen-Korrekturen | §1 |
