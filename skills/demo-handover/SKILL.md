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

- A demonstration runtime is not permanent; at most one exists and shows the last independently reviewed commit. Replacing it includes retiring the previous one after verifying exclusive ownership of its containers, volumes, network and private runtime directory, and verifying they are gone; a stopped runtime is not a retired one. Preserve review evidence and unrelated resources.
- Use the project's documented teardown verb (`demo.sh retire` or equivalent); never compose container, volume, network or directory removal yourself — an unattended guard refuses it.
- Start the runtime at the reviewed commit.
- Create the demonstration user via `demo.sh user`, with the password supplied only through the environment variable the script documents.
- Seed data that exercises the changed acceptance criteria.
- Record the reviewed commit, the URL, the login name and the exact data-creation command on the card.
