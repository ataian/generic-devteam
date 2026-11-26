# Fujiko: unabhängiges Planreview, Runde 2

Target: `/home/mariko/projects/generic-devteam/docs/PLAN_3.1.0_Demo-Umgebung_v5.md` sha256 `87b77b280fba97691e4901c76dd5e77ea3936e92994fc0bf91f05afeabdecff2`. Previous findings (criterion, not target): `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.0_Demo-Umgebung_v1.md` sha256 `95c4b8c4e9c2c7a6d3e1b7ffdc1288716f390444314a09f901b8d5d7a8b307b0`. Repo `/home/mariko/projects/generic-devteam` HEAD `8add46c01a31dd3f149819fd29305c5d16fa05c8`; `git diff HEAD | sha256sum`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Verify fingerprints before verdict. Do not edit the plan.

Max, verbatim (later decision supersedes earlier ordering):
> ziel ist, ich will dass das devteam alle docker befehle ausführen darf. das beinhaltet auch docker compose *  warum willst du das beschränken?   3) nein nicht davon getrennt. nur wenn der user eine neue demo haben will muss vorher auch die aktuelle entfernt werden. ohne demo wunsch auch kein aufräumen! er kann auch nix auf einer nicht vorhandenen karte "belegen". ich will keine solche "demo muss" regeln mehr in der soul. es wird einen neuen demo-skill geben der diese sachen regelt. für die jetzt geplante version: planner fragt user willste demo? sagt user ja -> aufräumen und demo-karte schreiben.  sagt user nein -> keine karte, kein aufräumen, kein check ob existiert, dann ist alles um demo für das devteam komplett irrelevant, sie werden es nichtmal anschauen, weil NIX mit der demo gemacht werden wird.  5) wie gesagt, ALLE docker befehle sollen freigegeben sein. docker-compose, "docker compose", und "docker".

> agreed, skill nur bei demo wunsch laden. das aufräumen ist planner aufgabe nicht die des reviewers. und wenn der user eine demo will und das aufräumen scheitert, dann kann der plan nicht losgehen, das problem muss der planner dann mit dem user direkt lösen. oder welche eskalation meinst du? workflow soll sein: wenn keine demo gewünscht, gibt es keine arbeiten bzgl demo weder aufräumen, prüfen,testen,laden,sichten,ticket,whatever. wenn demo gewünscht, räumt der planner die alte demo als ERSTES weg wenn sie noch existiert, bevor er irgendwelche tickets schreibt. das soll im prozess zwingend der erste step nach "annahme des plans durch den user" sein, das passt da hin oder? der reviewer braucht nix bzgl. demo zu machen. er soll am ende nur prüfen, ob die demo läuft und funktioniert.

Read only these two docs, tracked Maker sources/instructions/tests and `/home/mariko/projects/cac/SKILL.md` plus its required references. No other docs, reviews, histories, live profiles or secrets. No builds/tests, Docker, delegation, Kanban, commits, configuration or implementation. Read-only checks and in-memory substitution of plan blocks allowed. Only output file: `/home/mariko/projects/generic-devteam/docs/REVIEW_3.1.0_Demo-Umgebung_v2.md`.

| Prior ID | Check |
|---|---|
| K1 | Script wildcard vs Docker grants |
| K2 | Planner load path, verification and evidence before tickets |
| W1 | Failure exit, circular prerequisite |
| W2 | Reach and disclosure location |
| W3 | SemVer and role-template authorization |
| W4 | Reviewer only verifies final demo |
| W5 | Coder skill description in upstream sources |
| M1 | Three profiles vs Team-Codex |
| M2 | Current vs legacy baseline; listing tests |
| M3 | Bare CLI invocations |
| M4 | Document and operative text audiences |
| M5 | Removal of mandatory dev-script name |
| §6.5 | Start refusal in Coder path |
| §6.6 | Verification before any ticket, no invented card evidence |

For each previous finding: erledigt / teilweise / nicht erledigt; cite plan and Maker file:line. Confirm resolved findings; do not invent issues. Treat the author's mapping as a claim. Check new failures across delivery/inventory/transport, all affected test pins, role ownership, ordinary dev jobs vs requested-demo load, exact post-acceptance ordering before step 6 or *any* ticket, the negative and blocked branches, final functional review only, and both Docker commands in setup/update. Verify if implementation can follow v5 alone. Preserve operator decisions. German report for Max: 0 verdict APPROVED or CHANGES_REQUESTED and reasons (max five sentences); then tables for old findings, new material findings, verified anchors and limits. Return path. No changes beyond report.
