---
name: plan-versioning-semver
description: "Use when naming plan files: SemVer PLAN_<v>_<project>.md."
version: 1.0.0
author: Mariko
platforms: [linux]
metadata:
  hermes:
    tags: [planning, semver, naming, docs]
    category: devops
---

# Plan-Dateien SemVer-versionieren

Projekt-Pläne/Spezifikationen werden nach SemVer benannt, damit Features und
Bugfixes an den Dateinamen ablesbar sind.

## Namensschema

```
PLAN_<MAJOR>.<MINOR>.<PATCH>_<Name>.md
```

- **Erste Plan-Datei** (Basis): Projektname hinten dran, z. B.
  `PLAN_1.0.0_Meetingprotokollmaker.md`.
- **Jede weitere** (Feature): Kurzstring (1–2 Wörter) des Features statt
  Projektname, z. B. `PLAN_1.1.0_Audio-Upload.md`, `PLAN_1.2.0_Nous-Portal.md`,
  `PLAN_1.3.0_Auth.md`.

Der Projektname erscheint NUR bei der ersten Datei — danach dient der Name als
Feature-Namensgeber (kurz halten, 1–2 Wörter, damit der Dateiname nicht zu
lang wird).

## SemVer-Bedeutung auf Planspezifikationen

- **MAJOR** — inkompatible Änderung an der Spezifikation (Architektur/Pipeline
  bricht ab, z. B. `video` → `input`-Namensumbenennung).
- **MINOR** — neues, rückwärtskompatibles Feature (neue Plan-Datei pro Feature).
- **PATCH** — rückwärtskompatibler Bugfix an einer bestehenden Spezifikation.

## Regeln

1. Jedes neue Feature bekommt eine **eigene Plan-Datei** mit MINOR-Bump
   (`1.0.0` → `1.1.0` → `1.2.0` …). Bestehende Pläne bleiben unverändert als
   historische Spezifikation eingefroren (nicht umschreiben!).
2. Rename per `git mv` (Historie bleibt erhalten), Commits erkennen die
   Renames automatisch.
3. Interne Verweise auf alte Plan-Namen aktualisieren (AGENTS.md, README.md,
   "Ergänzt …"-Zeilen in den Feature-Plänen).
4. Bugfixes am **App-Code** (z. B. Upload 303→201) ändern NICHT die Version
   der historischen Plan-Dateien — die Pläne dokumentieren den damaligen
   Stand. Die App-Codeversion (falls versioniert) folgt separatem Schema.
5. Bei inkompatibler Spezifikationsänderung: MAJOR-Bump (z. B. `2.0.0`).

## Nach Dateien-Erstellung

- AGENTS.md auf den aktuellen Plan-Namen zeigen lassen (verbindliche
  Spezifikation).
- README.md Struktur-Block auf die versionierten Dateien aktualisieren.

## Standard: Version-API + CHANGELOG

Grundausstattung bei jedem Projekts:

### 1) Version-API

Nur bei Projekten, die eine API anbieten!
Ein öffentlicher Endpoint, der die App-Versionsnummer ausliefert — ohne Auth,
weil die Version für Health-Check/Kompatibilität ohne Key abrufbar sein soll:

```http
GET /api/version
→ {"version": "2.0.0", "name": "<projektname>"}
```

- Einheitliche Quelle für die Versionsnummer (nicht an mehreren
  Orten pflegen).
- Test: Endpoint ist auch mit aktiviertem Auth ohne Key erreichbar (200).

### 2) CHANGELOG.md

Datei im Repo-Root, Keep-a-Changelog-Stil:

```markdown
# Changelog

## [2.0.0] - JJJJ-MM-TT
### Changed
- …

## [1.1.0] - JJJJ-MM-TT
### Added
- …
```

- Pro Release-Version (X.Y.Z) ein Eintrag mit Datum.
- Kategorien: `Added`, `Changed`, `Fixed`, `Removed`.
- Bei jedem Release mitpflegen (Teil der Definition of Done).

### 3) App-Codeversion (SemVer) vs. Plan-Dateiversion

Die App-Codeversion folgt eigenem SemVer-Schema, getrennt von den Plan-Dateien: 
MAJOR bei inkompatibler API-Änderung, 
MINOR bei neuem Feature,
PATCH bei Bugfix. 

Die Plan-Dateien haben als Versionsnummer immer die aktuelle Version des Projekts 
von dem ausgehend die Änderung geplant wird.

Beispiel: 
Für eine App in Version 1.3.0 wird ein Wechsel des API returncodes 303→201 (inkompatibel = MAJOR Bump) geplant.
Die Plan-Dateien erhalten 1.3.0 in ihren Versionsnummern.
Für die App wird bei der Implementierung ein MAJOR-Bump auf 2.0.0 gemacht.
