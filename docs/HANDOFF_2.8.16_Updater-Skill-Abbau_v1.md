# Baustelle 2 — Updater baut nicht mehr zugewiesene Skills ab

| Feld | Wert |
|---|---|
| Datum | 2026-11-15 |
| Basis | Maker 2.8.16, Commit `bef909a`, HEAD `0931b49`, Branch `v3` |
| Zweck | Vorgabe für den Updater festhalten, bevor Text entsteht |
| Stand | beschlossen, nicht umgesetzt, eigenes Plandokument nötig |

## 1. Ziel

Ein Team-Update soll ein vorhandenes Team auf den Stand bringen, den ein frisch angelegtes Team hätte — auch wenn der Maker Skills entfernt. Teams werden nicht gelöscht und neu angelegt. Die einzige Grenze: zwischenzeitlich vom Team gemachte eigene Anpassungen dürfen nicht ungefragt überschrieben oder zurückgesetzt werden.

## 2. Befund (Stand 2.8.16)

Hinzufügen ist automatisch, Entfernen ist handgebaut pro Release.

- `references/update_team.py:546` rechnet je Eintrag `obsolete = sorted(set(stored) - new_targets)`. Der Helfer weiß also bereits, welche verwalteten Skill-Kopien nicht mehr zugewiesen sind.
- `references/update_team.py:598` und `:635` legen sie als `retained_obsolete` ab; `apply` löscht nichts.
- `references/update.md:164` — „lists removed source files and deassigned managed skill copies as `obsolete` and retains them on disk".
- `references/update.md:166` — „Outside this explicit retirement, retain generic obsolete files and local adaptations."
- `references/update.md:144` — neue Dateien und neue eigene Skills werden ohne eigenen Schritt ausgeliefert.
- Die einzige tatsächliche Löschung ist `references/update.md:402-486` „Required Reviewer skill retirement (1.1.22)": fest an eine Release-Grenze gebunden („Apply it when an existing team crosses from a pre-update version below `1.1.22` to a target version at or above `1.1.22`"), Tabelle mit exakt drei Reviewer-Identitäten (`:417-421`), Pflichtbestandteil des Update-Scopes, keine optionale zweite Wahl.
- Textänderungen an einer vorhandenen Kopie überschreibt der Updater nicht still: `references/update.md:142` (3-Wege-Merge, Stopp bei Konflikt), `:126` (unbekannte Baseline wird jeden Update als `baseline unknown; withheld` gemeldet und ferngehalten).

Damit fehlt genau ein Bindeglied: `obsolete` wird erkannt und gemeldet, aber es gibt keine allgemeine Regel, die daraus einen Abbauauftrag macht. Jede Löschung braucht derzeit einen neuen, release-gebundenen Abschnitt.

## 3. Entscheidung

1. Der Updater bekommt eine allgemeine Abbau-Regel, die bei jedem Team-Update greift, nicht pro Release. §1.1.22 geht darin auf.
2. Löschkandidaten sind ausschließlich die im geprüften Proposal als `obsolete` ausgewiesenen vom Maker verwalteten Skill-Kopien. Team-eigene Skills, die der Maker nicht kennt, sind nie Kandidat.
3. Eine Rückfrage reicht: Löschungen stehen namentlich mit Identität und aufgelöstem Pfad im Update-Scope und werden mit diesem einmal freigegeben. Sie sind Pflichtbestandteil; ohne sie ist das Update unvollständig und wird nicht als erledigt gemeldet.
4. Zustandsklassen entscheiden über die Behandlung:
   - `pristine` — nach vollständigem Baum-Backup außerhalb aller Discovery-Roots löschen.
   - `locally modified` oder `extra files` — liegen lassen, Diff berichten; Löschung nur auf eine eigene ausdrückliche Entscheidung für genau diesen Baum.
   - `unknown baseline` — liegen lassen und melden, wie heute bei `baseline unknown; withheld`.
5. Die inhaltlichen Schutzmechaniken aus 1.1.22 bleiben erhalten und gelten allgemein: Identität gegen `manifest.json` auflösen statt Pfade raten, Symlinks und geteilte Quellen prüfen, Rollen-spezifisches Unbinding und Autoload-Verweise berichten, Blocker statt Raten, wenn keine Isolierung möglich ist, Rücklesung nach dem Abbau.
6. Unverändert bleibt: Anpassungen, die keine Skill-Kopien sind, und alle nicht verwalteten Dateien werden nicht angefasst.

## 4. Umsetzungsskizze (noch nicht beauftragt)

- `references/update_team.py`: `obsolete` wird je Eintrag von einer Namensliste zu Datensätzen (Identität, Rollen-Home, aufgelöster Pfad, Zustand, Zustandsgrund). Zustand wird gegen die gespeicherte Baseline ermittelt. Reine Klassifikation, `apply` löscht weiterhin nichts.
- `references/update.md`: §„Required Reviewer skill retirement (1.1.22)" wird durch die allgemeine Regel ersetzt; die 1.1.22-Identitäten bleiben als erster Anwendungsfall erwähnt, nicht als eigener mechanischer Abschnitt. `:164`/`:166` werden auf die neue Regel umgestellt, damit keine Gegenaussage stehen bleibt.
- `references/test_update_team.py`: Regressionen für die drei Zustandsklassen und für die unveränderte `retained_obsolete`-Meldung.
- Version: eigenes Plandokument und eigener Versionsschritt, nicht im selben Satz wie die Punkte 1 und 2 dieser Besprechung.

## 5. Offene Punkte bei der Umsetzung

- Bump-Klasse: Verhaltensänderung des Updaters, kein reiner Fix — MINOR naheliegend, MAJOR nur wenn fremde Teams den bisherigen „nichts wird gelöscht"-Zustand als Vertrag betrachten.
- Ob der Helfer den Zustand schon im Proposal ausweist oder erst im Abbauschritt ermittelt, ist eine Aufwandsfrage; das Proposal ist die natürliche Stelle, weil dort schon Baseline und lokaler Stand verglichen werden.
- Die 1.1.22-Nennung von `project-lib-versioning` (Reviewer-Rückbau) berührt sich mit Punkt 2 dieser Besprechung (Löschung des Skills aus dem Maker). Reihenfolge beim Umsetzen festlegen.
