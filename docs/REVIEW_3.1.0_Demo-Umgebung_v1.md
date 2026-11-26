# REVIEW 3.1.0 — Optionale Demo, vollständige Docker-Freigabe

**Gegenstand:** `docs/PLAN_3.1.0_Demo-Umgebung_v4.md`, SHA-256 `995f0c7fb755fd73e059c980b89808bac224e88e42bec38b8f23ca9105bf1d7a`
**Basis:** Maker-Repo `generic-devteam`, HEAD `8add46c01a31dd3f149819fd29305c5d16fa05c8`; Arbeitsbaum bis auf untracked Pläne leer (`git diff HEAD` = SHA-256 `e3b0c442…b855`).
**Prüfumfang:** nur Plan, getrackte Maker-Quellen (`references/`, `skills/`, `templates/`, `SKILL.md`, `manifest.json`) und Tests an diesem HEAD; CAC-Notation/-Contract aus `/home/mariko/projects/cac/`. Keine Tests, kein Docker, keine Agenten, keine Änderungen außer dieser Datei.

---

## 0 Urteil

**CHANGES_REQUESTED**

Hauptgründe:

1. **`references/setup.md:136` NEU widerspricht sich selbst** — der beibehaltene Satz erlaubt `*` nur für skriptvalidierte Argumente, der neue Satz verlangt genau `docker *`. Der Umsetzende muss den Widerspruch raten.
2. **Der Abräumzweig verliert seine geladene Prozedur.** `planner.SOUL.md.template:75` NEU verpflichtet zum Abräumen, aber die Kriterien (Eigentum, Container/Volumes/Netz/Verzeichnis weg) stehen nach dem Edit nur noch in `dev-environment:47`, dessen Ladebedingung (`planner.SOUL.md.template:45`, nur Docker-Environment-Aufträge) einen Demo-Ja-Plan nicht abdeckt. Der gestrichene `planner:74` enthielt Prozedur, Verifikation und Readback. Plan Zeile 8 und Abnahme §4.4 (Zeile 197) sagen mehr zu, als der operative Text hergibt.
3. **`kanban-phase-release.md:21` NEU verliert den Failure-Exit** „keep the release blocked". Eskalation ohne Sperrfolge ist keine äquivalente Pflicht (CAC: Obligation Strength und Failure Exit erhalten).

Die politischen Entscheidungen selbst (alle Docker-Kommandos frei, Demo nur auf Kundenwunsch, kein Aufräumen ohne Wunsch, neuer Demo-Skill erst später) sind im Plan korrekt und vollständig abgebildet. Sie sind nicht Gegenstand der Beanstandung.

---

## 1 Abdeckung der Anforderungen

| Anforderung (Max) | Plan-Stelle | Befund |
|---|---|---|
| Alle Docker-Kommandos, inkl. `docker compose *` | §3, `setup.md:143,154`, `update.md:93` | gedeckt; Matcher bestätigt `docker *` ⊇ `docker compose …` |
| `docker-compose` zusätzlich | `setup.md:154`, `update.md:93`, §4.5 | gedeckt |
| Keine Beschränkung auf Projekt-Stack | `setup.md:139` ALT ersetzt, Plan:143,190 | gedeckt, Offenlegung unpräzise (W2) |
| Demo nur bei ausdrücklichem Ja | `planner:23,75`, `kanban-phase-release:21` | gedeckt |
| Aufräumen vor neuer Demo-Karte | `planner:75`, `dev-environment:47`, `kanban:21` | Reihenfolge gedeckt, Prozedur nicht geladen (K2) |
| Nein: keine Prüfung/Aufräumen/Karte/Nachweis | Plan:9, `planner:74` NEU | gedeckt; alle Demo-Pflichternen entfernt |
| Keine „Demo muss"-Regeln in der SOUL | Plan:59,203 | teilweise; `reviewer.SOUL.md:86` behält Replacement-Satz (W4) |
| Neuer Demo-Skill nicht Lieferumfang | Plan:11,203–205 | gedeckt |
| Drei Rollen (Setup/Update) | `setup.md:136` („all three profiles"), `update.md:87`, `setup-record.md:26` | gedeckt; Wortlaut „every role" unscharf (M1) |
| Bestehende Baselines | `update.md:87` NEU, `update.md:93` NEU | gedeckt (Definitionssatz + Tabellenzeile) |
| Beide Compose-Schreibweisen getestet | §4.5, Plan:198 | gedeckt; Volumes-/Netz-Listings fehlen (M2) |

**Belegt positiv:** Die 15 ALT-Blöcke sitzen auf den genannten Zeilen; jede geprüfte Schlüsselpassage existiert genau einmal (Zeilennummern und Wortlaut stimmen). Die Testpins sind vollständig adressiert: `test_render_reasoning.py:117,144–168`, `test_build_evidence.py:92,100–102,137–155`, `test_update_team.py:491–501`. Die drei „unattended guard refuses it"-Sätze (`planner:74`, `demo-handover:19`, `dev-environment:48`) werden alle entfernt — es bleibt keine falsche Behauptung stehen. Kein neuer Rendererparameter, kein neues `settings`-Feld; Passwortschutz, Kartenbindung und Abschlussbericht bleiben erhalten.

---

## 2 Fundstellen

### Kritisch (blockierend)

**K1 — `references/setup.md:136` NEU: Selbstwiderspruch.**
Behalten: „grant each reviewed command as written, with a `*` only for a script-validated argument such as a commit SHA or test selector." Neu: „Grant `docker *` (including `docker compose *`) and `docker-compose *` in every role." `docker *` ist kein skriptvalidiertes Argument. CAC verlangt eindeutige, nicht ratbare Anweisungen. Fix: Ausnahme explizit machen (z. B. „… or one of the two Docker grants below"), ohne die beiden Muster zu verengen.

**K2 — `planner.SOUL.md.template:75` NEU vs. Plan:8 und §4.4 (Plan:197).**
Plan Zeile 8: „Ist sicheres Abräumen nicht möglich, keine vorzeitige Demo-Karte." §4.4: „bei unklarem Eigentum oder Fehler keine Demo-Karte." Operativ steht nur „retire any previous demo, then add a final `Demo handover` card" — ohne Verb, ohne Eigentumsprüfung, ohne Weg bei Fehler, ohne Readback. Die Kriterien liegen nach dem Edit ausschließlich in `skills/dev-environment/SKILL.md:47`, geladen nur über `planner.SOUL.md.template:45` („For requests to create, adopt or revise a project's Docker development environment") — ein Demo-Ja ist das nicht. Der gestrichene `planner:74` trug Prozedur, „containers, volumes, network and private runtime directory are gone" und „record the readback on the card". Ergebnis: Abnahme §4.4 prüft ein Verhalten, das kein geladener Text definiert. Fix: Ladebedingung in `planner:45` um den Demo-Fall erweitern **oder** die Prozedur einzeilig in `planner:75` halten; Readback verorten (Plan oder Demo-Karte).

### Wichtig

**W1 — `skills/brownfield-feature-planning/references/kanban-phase-release.md:21` NEU.**
ALT: „… escalate the circular prerequisite to the operator and keep the release blocked." NEU: „… escalate a circular cleanup prerequisite to the operator before creating the demo card." Der Failure-Exit (Freigabe bleibt gesperrt, keine Karte) entfällt; „circular" wird nicht mehr definiert. CAC-Verstoß (Failure Exit, Bedingung).

**W2 — Reichweiten-Offenlegung (`setup.md:143` NEU, Plan:143).** „host-wide reach" untertreibt: `docker *` erlaubt auch `docker -H ssh://…`, `docker context use` und `DOCKER_HOST=…` (entfernte/alternative Daemons) sowie `docker run --privileged -v /:/host`, `docker system prune -a --volumes`. Beleg: die Laufzeit führt genau diese Formen als prompt-pflichtige Muster (`tools/approval_detection.py:590–604`), der Allowlist-Treffer geht ihnen jedoch voraus (`tools/approval.py:1297` vor `:1307`). Zusätzlich: `templates/setup-record.md` hat keinen definierten Ort/Feld für diese Notiz (Abschnitte 36–47 nennen nur generische Readbacks). Fix: Reichweite präzisieren (lokal und via Daemon-Redirect) und Ablageort nennen.

**W3 — Versionsklasse (Plan:4,199).** `3.1.0 → 3.1.1` ist PATCH; `AGENTS.md:4-5` verlangt „MINOR for compatible functionality". Vollfreigabe plus neuer Demo-Trigger ist Funktionalität, kein Fix. Entweder 3.2.0 oder eine ausdrückliche PATCH-Begründung. Zusätzlich: `AGENTS.md:8` verlangt für Rollen-Template-Edits eine eigene Autorisierung; Plan:4 nennt nur „separate Umsetzungsfreigabe" — die Freigabe muss den Template-Edit ausdrücklich umfassen (kein Rollout, das sagt der Plan korrekt).

**W4 — `templates/roles/reviewer.SOUL.md.template:86` bleibt unverändert.** Der Satz „Replacing it includes retiring the previous one after verifying exclusive ownership … and verifying they are gone" ist nach diesem Plan die einzige normative Replacement-Regel, obwohl Planner, `demo-handover:18` und `dev-environment:47` sie verlieren und das Abräumen allein beim Planner liegt. `test_render_reasoning.py:151` hält sie fest. Kein harter Widerspruch (der Reviewer prüft den Endzustand), aber eine bewusst konservierte Regel, die Max für die SOUL ausgeschlossen hat — Entscheidung dokumentieren oder auf die reine Prüfaussage („exactly one runtime at the reviewed commit exists") kürzen.

**W5 — `references/upstream-sources.md:30` veraltet.** „demo-handover … retire the previous runtime, start at the reviewed commit, … Coder only." Nach dem Plan räumt der Planner, nicht der Coder. Der Plan listet die Datei nicht. Entweder mitziehen oder als bewusst historisch kennzeichnen.

### Gering

- **M1** „in every role" (`setup.md:143`, Plan:11,133,190) vs. vier gebundene Rollen inkl. `team-codex` (`setup-record.md:25`) und drei Allowlist-Profile (`setup-record.md:26`). Präzisieren: „Planner, Coder, Reviewer".
- **M2** §4.5 (Plan:198): „vollständigen 3.1.0-Baseline … einschließlich bereits korrekter Liste (kein Diff)" ist widersprüchlich — eine vollständige 3.1.0-Baseline ist per Definition nicht korrekt; gemeint ist eine 3.1.1-Liste. Außerdem fehlen `docker volume ls`, `docker network ls`, `docker inspect` im Entscheidungstest, obwohl die Abräum-Verifikation (`dev-environment:47`) darauf beruht und `test_build_evidence.py:149–155` seinen Zweck verliert.
- **M3** Bare `docker` (ohne Argument) matcht `docker *` nicht (fnmatch, `tools/approval_floors.py:191–199`). Funktionell irrelevant (Hilfeausgabe), aber Max nannte „docker" ausdrücklich.
- **M4** `HERMES.md` verlangt technisches Englisch für Entwicklungsartefakte; der Plan ist deutsch. Vermutlich bewusst (Adressat Max), nur relevant, falls die Regel `docs/` einschließt.
- **M5** `dev-environment:39` ändert den Entrypoint-Vertrag des Guides (Beispiel `docker/dev/dev.sh up`, `check`, `stop`, `test`, `reset` entfällt) — nur durch Plan:131 („keine neue Skript- oder Compose-Pflicht") gerechtfertigt. Bestätigen, dass diese Ausweitung gewollt ist.

---

## 3 Umsetzbarkeit

- 6 Dateien, 15 Edits; kein neuer Rendererparameter, keine `settings`-Änderung. `references/render_text.py` bleibt unberührt; alle NEU-Texte nutzen vorhandene Platzhalter (`{{CODER_PROFILE}}`, `{{DEMO_PASSWORD}}`).
- `references/update_team.py` enthält keine Allowlist-Logik (grep ohne Treffer) — die Baseline-Abweichung ist reine Operator-Prosa. Kein Codefall, keine stille Nebenwirkung.
- `hermes approvals test --json --` existiert und führt nichts aus (`hermes_cli/subcommands/approvals.py:46–64`); es wertet die aktive Profilkonfiguration aus, isolierte Testprofile sind also ohne Live-Umstellung machbar. §4.5 ist technisch tragfähig.
- Matcher bestätigt beide Muster: `fnmatch("docker compose down -v","docker *") == True`, `fnmatch("docker-compose down -v","docker-compose *") == True`; zusammengesetzte Zeilen scheitern an `_has_allowlist_shell_operator` (bereits in `update.md:208` offengelegt).
- Bytegrenze unkritisch: `kanban-phase-release.md:21` ALT 350 B, NEU kürzer; `brownfield-feature-planning/SKILL.md` 12722 B < 14500 (`test_brownfield_planning.py:45`).
- Hinweis für den Testumbau: `test_build_evidence.py:152` (`grant.split("docker inspect *",1)[1]`) wirft nach dem Entfall mit `IndexError`, nicht als saubere Assertion — beim Ersetzen berücksichtigen.

---

## 4 Regelkonflikte

- **AGENTS.md SemVer** (W3): PATCH vs. MINOR für neue Funktionalität; Klasse nicht benannt/begründet.
- **AGENTS.md Rollen-Template** (W3): eigener Autorisierungsschritt fehlt in der Freigabeklausel.
- **CAC** (W1): Failure Exit „release blocked" entfällt; Bedingung „circular" unbestimmt.
- **CAC/Eindeutigkeit** (K1): zwei widersprüchliche Regeln im selben Absatz.
- **HERMES.md Sprache** (M4): nur falls auf Planungsdateien anwendbar.
- Kein Konflikt mit `update.md:208` („a grant is not a bypass") — die Neufassung behauptet keinen Bypass; Hardline und `approvals.deny` bleiben vorrangig.

---

## 5 Umfang

Angemessen: vier Rollen-/Skill-Dateien, zwei Referenzen, Testanpassungen; keine Ausweitung auf den neuen Demo-Skill, `soos` oder einen Rendererumbau. Grenzfall ist M5 (`dev-environment:39`), sonst keine Nebenänderungen. Bewusst beibehalten und daher nicht beanstandet: das Demo-Passwort bleibt in allen drei SOULs Pflicht (Plan:195), auch für Teams ohne Demo — toter Ballast, aber ausdrücklich so entschieden.

---

## 6 Lücken

1. W5: veraltete Beschreibung in `upstream-sources.md:30`.
2. Kein Nachweis, dass die Read-only-Listings (`docker volume ls`, `docker network ls`, `docker inspect`) nach dem Grant weiter erlaubt sind — genau sie tragen die Abräum-Verifikation; §4.5 prüft nur `docker ps`.
3. Kein definierter Ablageort für die „host-wide reach"-Notiz (`setup-record.md`).
4. §4.5-Baselinefall widersprüchlich formuliert (M2).
5. `demo-handover` hat nach dem Streichen keinen Zweig „Start verweigert wegen vorhandenem Zustand"; `dev-environment:49` gilt im Planner-Pfad, nicht für den Coder, der das Skill lädt.
6. Der gestrichene Readback aus `planner:74` („record the readback on the card") ist nicht neu verortet — Abräum-Evidenz ist damit ungeklärt (Teil von K2).

---

## 7 Grenzen

- **Keine Laufzeitprüfung.** Das Ja/Nein-Gate ist nur statisch gepinnt; §4.4 ist ein Papierdurchlauf, §4.5 ein Dry-Run. Plan:197 sagt das korrekt („Statische Textprüfungen nicht als beobachteten Teamlauf ausgeben").
- **Politikentscheidung, nicht Beanstandung:** `docker *` entfernt den Approval-Prompt als mechanisches Sicherheitsnetz für Coder und Reviewer. Verbleibende Grenzen sind danach nur SOUL-Text (`coder:52`, `reviewer:87`), Hardline-Blocklist und `approvals.deny`. Das ist Max' Entscheidung; die Offenlegung sollte sie benennen (W2).
- `docker *` deckt weder bare `docker` noch `sudo docker`, `env …`-Wrapper oder zusammengesetzte Zeilen (M3, bereits offengelegt).
- Nicht geprüft: Plan-Vorversionen v1–v3 (außerhalb des Auftrags), Live-Teams, andere `docs/`-Dateien.
- Verifiziert: Plan-Hash, HEAD, leerer `git diff HEAD`, Eindeutigkeit aller ALT-Anker.

*Geschrieben: `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.0_Demo-Umgebung_v1.md`*
