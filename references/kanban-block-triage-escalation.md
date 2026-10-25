# Kanban-Automatik: Block → `triage`, Auto-Decompose und was abschaltbar ist

Diese Datei gehört zum Setup, nicht zur Fehlerbehebung danach. Lies sie, bevor die
erste Kette freigegeben wird: die Maßnahme, um die es geht, ist eine Zeile
Konfiguration vor dem Start — und Stunden Arbeit, wenn sie fehlt.

## 1. Was eine Karte ohne Zutun nach `triage` bringt

Kein Agent verschiebt eine Karte dorthin. `_route_block()` in
`hermes_cli/kanban_db.py` zählt Blocks mit **derselben** `kind` und schreibt beim
Erreichen von `BLOCK_RECURRENCE_LIMIT` den Status `triage` mit Event
`block_loop_detected` — nicht `blocked`. Dashboard, CLI und `kanban_block` können
`triage` nur bei der Erzeugung setzen; die Eskalation ist Kernelverhalten.

| Fakt | Folge |
|---|---|
| Das Limit ist eine feste Modulkonstante (Wert 2) | Kein Config-Key, keine Umgebungsvariable, kein Board-Feld, kein Task-Flag erreicht es |
| Der Zähler vergleicht `kind`; eine andere Art beginnt wieder bei 1 | Die Art einmal zu wechseln kauft genau einen weiteren `blocked`, mehr nicht |
| Eine fehlende `kind` zählt als eigene Art (`None == None`) | Ein untypisierter Block ist kein Ausweg |
| `unblock` erhält `block_kind`/`block_recurrences` absichtlich | Eine entblockte Karte, die gleichartig erneut blockiert, geht direkt nach `triage` |
| Nur `complete_task` löscht sie (`block_kind=NULL`, `block_recurrences=0`) | Es gibt keinen Betreiberbefehl zum Zurücksetzen des Zählers — keinen per SQL erfinden |
| Der Zähler gilt **pro Karte**, nicht pro Problem | Ein Problem, das fünf verschiedene Karten je einmal blockiert, eskaliert nie, so oft es auch wiederkehrt |

## 2. Warum `triage` die gefährliche Spalte ist

Bei aktiviertem Auto-Decomposer läuft `auto_decompose_tick()` **vor** dem Dispatch,
in jedem Tick, über **alle** Boards, nimmt bis zu `auto_decompose_per_tick` Karten aus
`triage` und ruft den Decomposer mit `author="auto-decomposer"`. Eine Eskalation,
die in `triage` landet, erzeugt damit Karten und Parent-Kanten auf einem Plan, für
den niemand eine Änderung freigegeben hat. Die Spalte für menschliche Aufmerksamkeit
ist zugleich die Arbeitsqueue des Decomposers — diese Kopplung ist Absicht, nicht
Fehler, und sie ist der Grund für die Maßnahme in Abschnitt 3.

## 3. Was tatsächlich abschaltbar ist

| Ziel | Schalter | Reichweite |
|---|---|---|
| Verhindern, dass aus `triage` **Karten entstehen** | `kanban.auto_decompose: false` | **Global** — alle Boards; wird jeden Tick neu gelesen, kein Gateway-Neustart nötig |
| Das **Routing** nach `triage` verhindern | existiert nicht | — |
| Opt-out pro Board | existiert nicht | `boards/<slug>/board.json` trägt Slug, Name, Beschreibung, Icon, Farbe, default_workdir, project_id, created_at, archived — keine Orchestrierungseinstellungen |

Bei `false` bleibt eine Karte, die `triage` erreicht, ohne automatische Zerlegung
liegen. Der Planner klärt die Blockursache innerhalb seines Mandats und koordiniert
die weitere Bearbeitung nach den bestehenden Rollen- und Freigaberegeln. Der Status
allein ist kein Zerlegungsauftrag. Nur für eine ausdrücklich beauftragte Zerlegung
gibt es den manuellen Weg (`hermes kanban --board <slug> decompose <tid>` oder den
Detail-Drawer im Dashboard). Das Dashboard schreibt dieselben globalen Keys — es
gibt keine lokale Variante, die man anbieten könnte.

## 4. Was `false` garantiert und was nicht

- **Kein automatischer Ersatz.** Der Tick ruft `auto_decompose_tick()` nur bei
  aktivem Flag; einen automatischen Specifier-Lauf gibt es nicht. Die manuellen
  Funktionen `decompose` / `specify` sind kein vorgeschriebener Weg zur Klärung
  eines wiederholten Blocks; diese übernimmt der Planner.
- **Reichweite ist das Hermes-Home, nicht die Maschine und nicht der Verbund.** Pro
  Home läuft ein Gateway und liest dessen `config.yaml`. Eine Profilkopie des Keys
  ist ruhend, solange unter diesem Profil kein Gateway läuft — entweder mitgesetzt
  oder ausdrücklich als ruhend benannt. Andere Homes brauchen eigene Entscheidung.
- **Das Routing bleibt**, die Spalte füllt sich also weiter von selbst und nichts
  räumt sie mehr automatisch.
- **Bestehende Kinder und Kanten bleiben** — der Schalter zieht nichts zurück.
- **Andere Erzeuger sind nicht betroffen:** Cronjobs, die Karten anlegen, und
  Worker, die selbst `kanban_create` rufen, sind bewusste Agentenhandlungen.
- **Abnahme über Verhalten:** keine neuen `kanban auto-decompose [...]`-Zeilen im
  Gateway-Log und keine neuen Kinder/Kanten. `config get` beweist nur das
  Schreiben — für das Gate, das der nächste Tick tatsächlich auswertet, gehört der
  Resolver-Nachweis aus Abschnitt 5 dazu.

## 5. Setzen: welche Homes, und der Rücklese-Nachweis, der wirklich zählt

```sh
hermes config set kanban.auto_decompose false              # Home, das dispatcht
hermes -p <ROLLE> config set kanban.auto_decompose false    # jede Profilkopie
hermes config get kanban.auto_decompose                     # beide Formen zurücklesen
```

- `-p <profil>` ist der Profilselektor für Config-Befehle, auch wenn die
  Top-Level-`--help` ihn nicht aufführt — daraus nicht ableiten, die Form sei nicht
  unterstützt, und nicht von Hand YAML editieren.
- **Erst alle Kopien aufzählen:** Owner-`config.yaml` und `profiles/*/config.yaml`
  durchsuchen; jede auf `true` stehende Profilkopie einzeln setzen oder als ruhend
  benennen.
- Vorher sichern und danach diffen: die Änderung muss in jeder Datei genau diese
  eine Zeile sein.
- **Kein Neustart.** `_resolve_auto_decompose_settings()`
  (`gateway/kanban_watchers_common.py`) wird jeden Tick frisch gerufen; ein Neustart
  ändert nichts. Bei unlesbarer Config liefert es `(False, 3)`, fällt also sicher
  auf aus.
- **Dort nachweisen, wo der Dispatcher liest, nicht dort, wo geschrieben wurde.**
  Denselben Resolver mit dem Interpreter und Installationsverzeichnis des Gateways
  aufrufen:

  ```sh
  cd "$HERMES_HOME" && HERMES_HOME="$HERMES_HOME" <gateway-python> -c "
  import sys; sys.path.insert(0, '<installationsverzeichnis>')
  from hermes_cli.config import load_config
  from gateway.kanban_watchers_common import _resolve_auto_decompose_settings
  print(_resolve_auto_decompose_settings(load_config))"
  ```

  `(False, N)` ist das Gate, das der nächste Tick auswertet — das ist das
  angekommene Schreiben. `(True, N)` heißt: der Dispatcher liest etwas anderes als
  die Datei sagt.

## 6. Wenn es trotzdem passiert ist: unerwünschten Fan-out zusammenführen

1. Wurzel lesen: Status, `parents`, `children`, Events (`block_loop_detected` trägt
   `kind`/`recurrences`/`limit`) und je Kind `created_by` — `auto-decomposer`
   markiert die, die niemand beauftragt hat.
2. Rein lesende Nachweiskarten behalten; sie dokumentieren Zustand und kosten nichts.
3. Unerwünschte Ausführungs-/Reviewkarten einzeln archivieren. Keine Parent-Kanten
   entfernen, keine Zähler zurücksetzen, keine Historie löschen.
4. **Erwarte, dass die Ursprungskarte promoviert.** Ein archivierter Parent hält sein
   Kind nicht mehr in `todo`, die Wurzel kann also auf `ready` gehen und im nächsten
   Tick beansprucht werden. Nach jedem Archivieren den Status zurücklesen.
5. Ist der Stopp gewollt, die Karte über den nativen Blockweg
   (`blocked`/`needs_input`) mit echtem Grund anhalten und den Status zurücklesen.
   `promote`/`unblock` gehören nicht dazu.
6. Den tatsächlich gelesenen Graphzustand berichten, nicht den beabsichtigten.

## 7. Nie den Kernel patchen

Die Installation ist ein Git-Checkout, den der Updater ersetzt, und Updates kommen
laufend. Eine gepatchte Konstante oder ein von Hand ergänzter Config-Key ist beim
nächsten Update weg. Quellcode zu lesen dient der **Diagnose** — es ist der Beleg,
dass kein Schalter existiert. Fehlt einer, das klar sagen und benennen, was eine
echte Änderung kostet (ein Upstream-Feature), statt einen lokalen Patch als Lösung
anzubieten.
