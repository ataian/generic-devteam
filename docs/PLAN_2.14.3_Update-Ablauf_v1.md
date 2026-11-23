# Maker 2.14.3 — Wartekonfiguration im Update-Ablauf richtig verortet

**Status:** umgesetzt, Pakettests grün.
**Vorgänger:** [2.14.2 Rollentext entlastet](PLAN_2.14.2_Rollentext-entlastet_v1.md).

## Befund

Der Abgleich der Wartekonfiguration stand in `references/update.md` als Unterpunkt von
Schritt 1 „Inspect the full scope" — mit Schreibauftrag („Reconcile … and read all three
back"). Damit verlangte das Rezept eine Konfigurationsänderung **vor** dem Freigabe-Gate
(„approve scope and activity" → apply) und widersprach seiner eigenen Reihenfolge. Zusätzlich
führte die Zeile die Zahlen ein zweites Mal neben `setup.md`, sodass ein Wertwechsel an drei
Stellen nachzuziehen war.

## Entscheidung

Schritt 1 nennt die Werte nur noch als Teil des Freigabeumfangs. Gesetzt werden sie in
„Activity and application" als neuer Schritt 4: Werte aus `setup.md` nennen, Freigabe
einholen, nativ setzen, alle drei Keys rücklesen, Readback im privaten Setup-Record
festhalten. Die Zahlen stehen damit nur noch an einer Stelle (`references/setup.md`).

## Änderungen

| Datei | Änderung |
|---|---|
| `references/update.md` | Schreibauftrag aus Schritt 1 entfernt; neuer Schritt 4 in „Activity and application" mit Freigabe → setzen → Rücklesen → festhalten und Zeiger auf `setup.md` |
| `references/test_render_reasoning.py` | Vertrag prüft jetzt die Position: der Abgleich steht im Anwendungsabschnitt **nach** „Apply the reviewed proposal" und nicht im Inspektionsabschnitt |
| `references/test_build_evidence.py` | erwartet den neuen Schrittnamen statt der alten Zahlenzeile |

## Grenzen

- Reine Ablauf- und Textkorrektur; keine Werte, Rollentexte, Freigaben oder Skripte geändert.
- Der Datei-Helfer bleibt unverändert file-only; die Konfiguration setzt weiterhin der
  Operator nativ.
- Bestehende Teams sind nicht betroffen; die Änderung wirkt beim nächsten Team-Update.