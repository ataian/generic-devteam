# Maker 2.14.2 — Rollentext entlastet, Wartefenster bleibt 4 h

**Status:** umgesetzt, Pakettests grün.
**Vorgänger:** [2.14.1 Lauf-10-Korrekturen](PLAN_2.14.1_Lauf10-Korrekturen_v1.md).

## Befund

2.14.1 hat die Grenzen konfiguriert. Offen blieb der Rollentext: er trug Mechanik, die dort
nichts bewirkt und teils falsch war.

- Der Wait-Absatz verlangte den nativen Wait mit `timeout=14400`, behauptete, der Dispatcher
  hebe die Terminal-Grenze auf die Kartengrenze, und untersagte ein erneutes Warten mit
  anschließendem `capability`-Block. Keine dieser Aussagen ist Rollenverhalten: 188 von 189
  Codex-Hintergrundstarts über neun Profile holen das Ergebnis von selbst ab, weil Schritt 7
  ohne Ergebnis nicht arbeitet; der Tool-Text meldet „still running — not an error" selbst.
- Die Zeile „Read the first stdout line `{"type":"thread.started",…}`" beschrieb einen Pfad,
  den der vorgegebene Hintergrund-Start nicht geht: das Tool-Ergebnis enthält nur die
  Prozess-Session, die Thread-ID steht in der Prozessausgabe.

## Entscheidung

Der Wait-/Block-Absatz fällt ersatzlos aus der Coder-SOUL. Die Thread-ID-Zeile nennt die
Prozessausgabe. Der Planner trägt für den Demo-Teardown denselben Wortlaut wie der Coder —
mit konkretem Verb und Guard-Hinweis —, damit „teardown verb" an keiner Stelle unbestimmt
bleibt. **Die Konfiguration bleibt wie in 2.14.1:** Wartefenster `14400`, Tool-Deadline
`15000`, Kartengrenze `--max-runtime 8h`.

Damit gilt das gewollte Verhalten ohne Textzusatz: Nach vier Stunden läuft das Wartefenster ab,
die Rolle sieht den Zustand des Runs (`Wait window of 14400s elapsed — the process is still
running`) und lässt ihn weiterlaufen; nach acht Stunden beendet der Dispatcher den Worker hart.
Ein Blockieren bei laufendem Codex ist nicht vorgesehen und steht nirgends mehr als Anweisung.

## Änderungen

| Datei | Änderung |
|---|---|
| `templates/roles/coder.SOUL.md.template` | Wait-/Block-Absatz entfernt; Thread-ID aus der Prozessausgabe |
| `templates/roles/planner.SOUL.md.template` | Demo-Teardown mit demselben Wortlaut wie im Coder: konkretes Verb (`demo.sh retire` oder gleichwertig) und der Hinweis, dass der Guard selbst zusammengesetztes Entfernen verweigert |
| `references/setup.md` | ein Satz: das Wartefenster bleibt bewusst unter der Kartengrenze, damit die Rolle nach vier Stunden den Stand liest und weiterlaufen lässt |
| `references/test_render_reasoning.py` | Verträge auf den neuen Rollentext; Assertion verbietet Zeitangaben und „do not wait again" in der Coder-SOUL |

Werte, Rezepte und Freigaben aus 2.14.1 sind unverändert.

## Grenzen

- Der 4-h-Blick ist eine Eigenschaft des Wartefensters, keine Rollenregel; er steht deshalb
  nicht in der SOUL.
- Der Dispatcher beendet den Worker über `worker_pid`, nicht die Prozessgruppe. Ein
  Enkelprozess kann den Kill überleben (in Lauf 10 belegt). Das ist Hermes-Code, nicht
  Maker-Text.
- Bestehende Teams erhalten den neuen Rollentext erst mit einem Team-Update.