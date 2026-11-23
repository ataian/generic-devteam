# Maker 2.14.1 — Korrekturen aus Lauf 10

**Status:** umgesetzt, Pakettests grün.
**Vorgänger:** [2.14.0 Lauf-9-Korrekturen](PLAN_2.14.0_Lauf9-Korrekturen_v1.md). P3 und P6 waren dort richtig
entschieden, aber falsch abgelegt: die Werte standen als Rollentext statt als Konfiguration, und der
Demonstrationszyklus endete beim Planner beim Stoppen statt beim Entfernen.

## Befund Lauf 10

**Wartegrenze.** Karte `t_0c69298a` (Board `sg1`, Carter) blockierte als `capability`, nachdem vier
`process_manage wait` mit `timeout=14400` jeweils nach 420,0 s als `Error executing tool` endeten. Ursache
war keine Codex-Störung, sondern eine Grenze, die die Rolle nicht setzen kann: `_SEQUENTIAL_DEADLINE_EXEMPT_TOOLS`
in `agent/tool_executor.py` befreit nur `delegate_task` und `manage_connections`; für `process_manage` gilt
`timeouts.tools.sequential_call` und ohne Eintrag der Vorgabewert 420 s. `terminal.timeout: 14400` hebt nur die
Klemme innerhalb des Tools, nicht das äußere Deadline. Die SOUL-Zeile versprach „the process exit ends the wait“,
was auf diesem Stand unerfüllbar war. Der Codex-Prozess lief nach dem Block weiter und schrieb in den Checkout.

**Demo-Lebenszyklus.** Die Planner-Zeile verlangte „when a demonstration runtime is running, stop it“. Jack
stoppte die vorige Demo und berichtete das; Container, Volume und Netzwerk blieben erhalten. Coder, Reviewer und
`dev-environment` verlangten dagegen bereits `retire`. Zwei Formen derselben Sache, eine davon zu schwach.

## Entscheidung

1. Wartegrenzen sind Profilkonfiguration, kein Rollentext. `terminal.timeout 14400` bleibt das Wartefenster;
   `timeouts.tools.sequential_call` und `timeouts.tools.concurrent_batch` werden auf `15000` gesetzt, damit das
   Werkzeug länger lebt als sein eigenes Wartefenster und der Wait sein Ergebnis selbst zurückgibt. Die Karte
   behält `--max-runtime 8h` als Hänger-Schutz des ganzen Worker-Laufs.
2. Der Rollentext nennt nur noch das Verhalten: ohne Timeout-Argument warten, bei einem Wartelauf ohne neue
   Ausgabe nicht erneut warten, sondern blockieren. Zahlen und Mechanik stehen nicht mehr in der SOUL.
3. Eine Demonstration wird stillgelegt **und entfernt**, durch das Teardown-Verb des Projekts, mit Nachweis über
   die read-only Auflistungen. „Gestoppt“ ist kein erledigter Zustand; Planner, Coder, Reviewer und der Skill
   tragen dieselbe Formulierung.

## Änderungen

| Datei | Änderung |
|---|---|
| `references/setup.md` | Wartefenster und Tool-Deadline als zwei Konfigurationswerte samt Readback; read-only `docker volume ls` und `docker network ls` in die Freigabeliste |
| `references/update.md` | Abgleich aller drei Werte bei jedem Update |
| `templates/roles/coder.SOUL.md.template` | Timeout-Mechanik aus dem Rollentext entfernt; Verhalten und Blockregel bleiben; Retire-Nachweis im Handover |
| `templates/roles/planner.SOUL.md.template` | Demo vor Kartenfreigabe entfernen und Readback festhalten statt stoppen |
| `templates/roles/reviewer.SOUL.md.template` | gleiche Retire-Formulierung wie Coder |
| `skills/dev-environment/SKILL.md` | „ein gestoppter Lauf ist kein stillgelegter“ im Lebenszyklus |
| `references/test_build_evidence.py`, `references/test_render_reasoning.py` | Verträge auf Konfiguration und Retire-Nachweis umgestellt, neue Freigaben geprüft |

## Grenzen

- Die Zahlen sind gesetzt, nicht gemessen: `15000` ist Wartefenster plus 600 s Luft, damit der Wait vor dem
  Executor zurückkehrt. Ein Lauf mit dieser Konfiguration steht noch aus.
- Bestehende Teams erhalten die Werte erst mit einem Team-Update; 2.14.1 ändert kein laufendes Profil.
- Der Pakettest prüft die Rezept- und Textverträge statisch, nicht das tatsächliche Warten gegen einen
  laufenden Codex-Prozess.