# Rollenkorrekturen aus Lauf 8 — Maker 2.11.2 → 2.12.0

**Status:** umgesetzt im Arbeitsbaum, Suite läuft. Kein Commit, kein Push, kein Rollout.
**Basis:** Maker 2.11.2, `953f6dd5b7bf21e96676dccc13ebfcde39e95416`.
**Anlass:** Auswertung `ANALYSE-ECOG5UKE-2026-11-20.md` (Projekt `devteam-tokenprofiling`), Entscheidungen von Max am 2026-11-21.

Zwei Changesets, wie entschieden: A = Regeltext ohne neue Rechte, B = Berechtigungen. Beide sind
Textänderungen am Maker; das Setzen der Grants passiert in einem späteren Setup- oder Update-Lauf,
nicht hier.

---

## A1 — „andere Teammitglieder" gibt es nicht

**Beobachtung.** `docker/dev/AGENTS.md` gehört dem Team; es gibt keine zweite Nutzergruppe. Jack hat
den Satz als Eingriff in fremde Nutzung gelesen und deshalb den Kunden gefragt, ob er die Demo stoppen
darf (14:24:49), statt den Branch anzulegen. Zusätzlich fehlte die Handlung, die du erwartest: eine
neue Entwicklung stoppt oder entfernt die alte Demo.

**Ort.** `templates/roles/{planner,coder,reviewer}.SOUL.md.template`, je eine Zeile
(`When the project has an assigned development environment, …`).

ALT (wörtlich, je Datei genau einmal):

```
… for development tests. Coordinate disruptive operations with other team users. Respect existing boundaries …
```

NEU:

```
… for development tests. The development and demonstration runtime belongs to this team; starting new
development stops or removes the previous demonstration run. Respect existing boundaries …
… Running the app from source grants no deployment authority. The agent runtime may still gate an
individual command; setup grants the team's regular commands, so a denial is a blocker to report, not a
customer question.
```

**Erhalten bleibt:** die Kundenseite der Freigabe (kein Kunden-OK für Dev-Betrieb), die Grenzen
(Quellbesitz, Betriebsdaten, Host-Administration, geteilte Infrastruktur, externe Wirkung), kein
Deployment-Recht.

**Test.** `references/test_render_reasoning.py::test_rendered_development_authority_agrees_and_keeps_role_boundaries`
prüft die Klauseln wörtlich; die Klauselliste ist im selben Changeset angepasst.

---

## A2 — Branch wird angelegt, nicht delegiert

**Beobachtung.** `planner.SOUL` verlangte die Branch-Anlage bereits (Zeile 71 der installierten Fassung,
CAC-Fassung unverändert übernommen). Jack hat sie trotzdem unterlassen und die Bedingung in den
Kartenbody geschrieben („Coordinate the documented branch switch before editing or testing"); Run 56
blockierte nach 62 s, 10 min 15 s Stillstand, 350 744 Token.

**Ort.** `templates/roles/planner.SOUL.md.template`, Schritt 7.

ALT:

```
Before card release, create the branch from the confirmed start commit, record its name on the card and
read back name and status.
```

NEU:

```
Before card release, create the branch from the confirmed start commit and check it out in the assigned
checkout; stop the previous demonstration runtime first. Record its name on the card and read back name
and status. Do not leave branch preparation to the Coder or to text on the card.
```

**Erhalten bleibt:** Kundenbestätigung von Branch und Startcommit, unabhängige Prüfung der Basis,
Rücklesung von Name und Status.

---

## A3 — Versionspflicht je Branch

**Beobachtung.** Jack hat die Arbeit als „pre-release addition" deklariert und die Version nicht erhöht;
der Kunde musste die Regel im Lauf liefern (14:16:04: „should be an increment to current, so
20.24.0-SNAPSHOT"). Die Skill-Fassung im Maker klassifiziert nur MAJOR/MINOR/PATCH und sagt nichts über
die Pflicht je Branch.

**Ort.** `skills/plan-versioning-semver/SKILL.md`, Abschnitt „Application and library versions".

NEU (angehängt):

```
Every change on its own branch increments the application version once, from the version checked out at
the start branch, in the same commit as the change. A `-SNAPSHOT` suffix is a version like any other;
treating the work as a pre-release addition is not an exemption. Name the class (`MAJOR`/`MINOR`/`PATCH`)
when proposing the branch, and name the version fields the project actually carries.
```

**Erhalten bleibt:** die drei SemVer-Klassen und die unabhängige Behandlung eigener Bibliotheken.

---

## A4 — Ticket trägt keine Rollenpflichten

**Beobachtung.** Der Kartenbody wiederholte den Ablauf („Carter implements through Team-Codex … Do not
self-close, spawn a substitute reviewer, push or deploy") und verlangte Plan **und** SPEC als Lektüre.
Die Planner-SOUL verbot Routinearbeiten im Body bereits („Omit team setup and routine procedures from the
body"); die Formulierung deckte eine Wiederholung von Rollenpflichten nicht ab. Die SPEC ist inhaltlich
deckungsgleich mit dem Plan: 0 von 16 SPEC-Zeilen stehen wörtlich im Plan, 76 % Wortüberlappung.

**Ort.** `templates/roles/planner.SOUL.md.template`, Schritt 7.

ALT:

```
Set assignee, reviewer, workspace, dependencies, and required runtime fields natively. Omit team setup and
routine procedures from the body.
```

NEU:

```
Set assignee, reviewer, workspace, dependencies, and required runtime fields natively. Omit team setup,
routine procedures and restatements of role duties or workflow from the body. Bind the plan; omit a
separate specification read when the plan carries the requirement.
```

**Erhalten bleibt:** Body-Pflichten (Ergebnis, Kriterien, Schnittstellen, Grenzen, Verifikation,
Abhängigkeiten, Bindung an Plan/Pfad/Commit).

---

## A5 — Kommandoform in allen drei Rollen

**Beobachtung.** Sechs Verweigerungen, alle beim Reviewer: dreimal `python3 -c`, zweimal
`docker compose stop` (im `trap`), einmal die `--rm`-Kombination. Der Coder trug eine Regel, die
weiter ging als der Guard (auch Shell-Variablen und Ketten verboten — im Widerspruch zum eigenen
Projekt-Guide), der Reviewer und der Planner trugen keine. Jacks eigener `config set` lief in einen
Freigabedialog-Timeout, weil sein Prüfskript `python3 -c` enthielt (16:05:20 → 16:10:23).

**Ort.** `templates/roles/coder.SOUL.md.template` (Ersatz der bestehenden Zeile),
`templates/roles/reviewer.SOUL.md.template` (Schritt 7),
`templates/roles/planner.SOUL.md.template` (neue Zeile neben der Dev-Umgebungszeile).

NEU, Coder:

```
Never pass code through an inline `-c`/`-e` interpreter or a heredoc: the worker guard blocks both in
unattended runs. Put multi-step work in a script file and run it. Shell variables and `;` chains are
allowed only in the form the project agent guide prints; an approved command inside a compound line never
matches, so ask for a script entrypoint instead.
```

NEU, Reviewer (Satz am Ende von Schritt 7):

```
Never pass verification code through an inline `-c`/`-e` interpreter or a heredoc; put multi-step checks
in a script file. An approved command inside a compound line never matches, so a denial there is a tooling
finding for the Planner, not a workaround you invent.
```

NEU, Planner:

```
Never pass code through an inline `-c`/`-e` interpreter or a heredoc; put multi-step checks in a script file.
```

**Erhalten bleibt:** Verbot von Umgehungen; „If a required operation is denied, report it without
bypassing guards" bleibt in Kraft.

---

## B1 — Grants bei Einrichtung und Update

**Beobachtung.** `command_allowlist` war in allen drei Profilen leer; `approvals.single_query_mode: deny`
sperrt Worker-Kommandos. Der Maker hat diesen Layer bisher nicht angefasst.

**Ort.** `references/setup.md` (neuer Block nach der Schutz-Einstellung), `references/update.md`
(neuer Punkt „Command grants" in Schritt 4).

Grants je Profil:

```
["docker *","docker-compose *","env * docker *","env * docker-compose *"]
```

**Grenze, die im Text steht:** ein Grant greift nur auf eine **einfache** Kommandozeile. `;`, `&&`, `|`,
Heredoc oder `$`-Expansion in doppelten Anführungszeichen schalten die Allowlist-Prüfung ab
(`tools/approval_floors.py::_has_allowlist_shell_operator`); deshalb der Entrypoint-Zwang aus B2.
`approvals.single_query_mode`, `unattended_mode`, `cron_mode` bleiben `deny`.

**Erhalten bleibt:** der Hardline-Blocklist und die Nutzer-Denyliste; ein Grant ist keine Umgehung,
sondern eine Vorwegnahme der Antwort „immer erlauben" für eine definierte Kommandoklasse.

---

## B2 — Ein Entrypoint je Dev-Umgebung

**Ort.** `skills/dev-environment/SKILL.md`, Abschnitt „Hand over one operating guide" (neue Zeile) und
Abschnitt „Build for repeated edits" (Permissions-Zeile).

NEU:

```
Entrypoint: give the guide one script with verbs (`docker/dev/dev.sh up|stop|test|reset …`) and let every
operation be that single simple command line. A compound command line or `$` expansion inside double quotes
never matches an agent grant, so a verb per line keeps both the guide and the runtime allowlist small.
```

**Beobachtung dazu:** `docker/dev/AGENTS.md` druckt heute `export COMPOSE_ENV_FILES="$PWD/…"; docker compose
stop …` — genau die Form, die kein Grant treffen kann. Deshalb mussten Grants im Lauf als projektspezifische
Literale gesetzt und nach dem Lauf widerrufen werden.

---

## Verifikation

| Prüfung | Stand |
|---|---|
| Betroffene Einzeltests (`test_render_reasoning`, `test_dev_environment`, `test_brownfield_planning`) | grün |
| Gesamtsuite `python3 -B -m unittest discover -s references -p 'test_*.py'` | `Ran 243 tests in 364.825s` — `OK (skipped=1)`, der bekannte native Delegated-Child-Skip |
| ALT-Blöcke je Datei genau einmal | durch `patch` erzwungen (eindeutige Fundstelle) |
| Versionen | `SKILL.md` 2.11.2 → 2.12.0, `manifest.json` 2.12.0, `dev-environment` 0.2.0 → 0.3.0, `plan-versioning-semver` 1.3.0 → 1.3.1 |

## Nicht angefasst

- Hermes-Kern (`--rm`-Falschpositiv, CBM-Doppelpayload) — von Max abgelehnt; das Falschpositiv ist über
  einen Grant lösbar, siehe B1.
- Dev-Guide-Größe (Punkt 5 der Besprechung).
- Wake-Filter für `changes_requested`: die Kartensubscription kennt heute keinen Ereignisfilter; das wäre
  eine Hermes-Änderung und ist damit nicht Teil dieses Changesets.
- Laufende Teamprofile: kein `config set` in diesem Durchgang.

## Offene Folgearbeit

1. Team-Update für SG1 auf 2.12.0, damit SOUL-Änderungen und Grants wirksam werden.
2. Entscheidung, ob `docker *` als Grant-Klasse bleibt oder auf `docker compose *` verengt wird.

---

# Nachtrag: Korrekturen nach CAC-Review (2.12.0 → 2.13.0)

Max hat die Texte aus 2.12.0 als nicht CAC-konform beanstandet. Ursache: die Zeilen wurden
geschrieben, ohne CAC an der Schreibstelle erneut zu lesen. Ein unabhängiger Prüfsubagent hat danach
den gesamten Textdiff seit `953f6dd` gegen die vier CAC-Dateien geprüft (read-only, ohne Änderungen).

## Übernommen

| Befund | Änderung |
|---|---|
| Bedingung fehlte: die Dev-Zeile behauptete Runtimes für Projekte ohne Umgebung | "When the project has an assigned development environment or a demonstration runtime, this team owns both runtimes." |
| "No customer approval for …" war ein Verbot statt einer Erlaubnis | "… need no further customer approval." |
| Demo-Stopp war unbedingt | "Before card release: when a demonstration runtime is running, stop it." |
| "read back both with branch status" ohne Bezug | "… read back the card fields and the branch's git status." |
| Bericht verlor `verified`, `when needed` und die Offenlegung ungetesteter Zugriffe | alle drei wieder aufgenommen |
| "start branch" war ein neuer Begriff neben "start commit" | "from the version at the confirmed start commit" |
| SemVer ohne Adressat und ohne Ziel | "On its own branch, each change MUST increment …" + "When proposing the branch, name the class …" |
| Coder-Schritt 13 stand hinter "no further project changes until native return" | "On a released demo handover card: …" |
| Karte nannte keinen Bearbeiter, Felder unscharf | `assigned to {{CODER_PROFILE}}`, "the exact implementation commit, the URL and the exact data-creation command" |
| "Report criteria that stay invisible in the demo" | "Report each criterion the demo cannot demonstrate." |
| Entrypoint-Bullet wiederholte den Nachbarbullet | ein Satz, Verben ausgeschrieben |
| Berechtigungsbullet im Skill wiederholte die Rollen-SOULs | auf die ursprüngliche Fassung zurückgeführt |
| `dev-environment` 0.2.0 → 0.4.0 waren zwei MINOR in einem Changeset | 0.3.0 |
| "under separate authorization" bei Built-Image-Demos gestrichen | wieder aufgenommen; die Handover-Karte ist die Autorisierung |

## Abgelehnt, mit Grund

- **B2, Wiederaufnahme von "Coordinate disruptive operations with other team users"** — genau die
  Zeile, die Fehler 3 ausgelöst hat. Es gibt keine anderen Nutzer der Dev-/Demoumgebung; sie wieder
  einzuführen macht den Beschluss rückgängig.
- **B3, Wiederherstellung der Ticket-Zeile (planner:70)** — von Max ausdrücklich gestrichen; die
  Pflicht steht jetzt in allen drei Rollen-SOULs. Die Sorge des Prüfers (Arbeit blockieren, wenn keine
  Umgebung existiert) deckt die neue Bedingung "When the project has an assigned …".
- **B1, Wiederaufnahme des Verbots von Shell-Variablen und Ketten** — der Projekt-Guide druckt selbst
  `export …; docker compose …`. Ein Verbot stellt die Rolle gegen ihre eigene Anleitung; verboten
  bleiben nur Inline-Interpreter und Heredoc, die der Guard tatsächlich blockiert.
- N12 (Glossar-Mini-Sprache), N6-Zusatzverschiebung — reine Geschmacksfragen ohne Bedeutungsverlust.

## Offen aus dem Review

- Doppelte Handover-Definition in `planner.SOUL:72` und `skills/dev-environment` ("data that exercises
  the changed criteria" / "seed data for the changed criteria"). Der Planner lädt den Skill; eine der
  beiden Stellen sollte die Definition allein tragen. Vorschlag: der Skill beschreibt das Verfahren,
  die SOUL nur die Karte.
