# Main-Agent Maker wrapper

Before setup or update, ensure the Main-Agent has this wrapper or a local adaptation.

## Bootstrap prompt

```text
Create a small wrapper skill for setting up new teams and updating existing teams with https://github.com/ataian/generic-devteam.
Clone the Maker into your projects directory if it is not already there.
At the start of each invocation, run `git pull --ff-only` in that checkout.
Then read its current `SKILL.md` and follow the Maker procedure for the requested setup or update.
```
