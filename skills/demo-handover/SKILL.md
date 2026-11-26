---
name: demo-handover
description: Use on a released demo handover card.
version: 1.0.0
author: Max, Mariko (Hermes Agent)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [demo, handover, teardown]
    related_skills: []
---

# Demo handover

Trigger: a released demo handover card, not a code card. The demonstration user's password stays in the role instructions; this skill carries the runtime procedure.

- At most one demonstration runtime exists; use the last independently reviewed commit. Preserve review evidence and unrelated resources.
- Start the runtime at the reviewed commit. If build or start refuses existing state, stop and report the refusal; do not purge, rename or bypass it.
- Create the demonstration user with the project’s documented command. Supply its password only through the documented environment variable.
- Seed data that exercises the changed acceptance criteria.
- Record the reviewed commit, the URL, the login name and the exact data-creation command on the card.
