# Maker wrapper

Before setup or update, ensure you have this wrapper or a local adaptation in your own agent profile.

## Bootstrap prompt

```text
Create a small wrapper skill for setting up new teams and updating existing teams with https://github.com/ataian/generic-devteam.
Clone the Maker into your projects directory if it is not already there.
At the start of each invocation, run `git pull --ff-only` in that checkout.
Then read its current `SKILL.md` and follow the Maker procedure for the requested setup or update.
Also trigger the wrapper for team rename and migration assessments.
For those assessments, read the Maker's setup and role-binding references, compare actual and intended bindings, and derive the required steps and approvals; do not treat the file updater as a migration tool.
```
