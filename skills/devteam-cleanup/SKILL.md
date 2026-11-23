---
name: devteam-cleanup
description: "Use when the customer asks the team to clean up a finished delivery."
version: 1.0.0
author: Max, Mariko (Hermes Agent)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [devteam, cleanup, maintenance]
    related_skills: [brownfield-feature-planning]
---

# Devteam cleanup

## When to use

Use when the customer asks for cleanup (`/devteam-cleanup`, "clean up", "räum auf", or equivalent).

No step in the delivery flow requires cleanup. Accepted review is not customer acceptance, and corrections may continue on the same branch.

## What cleanup covers

- Candidates: delivery artifacts the customer no longer needs. Include scratch scripts and temporary directories in role workspaces, throwaway delivery containers and images, stray files outside the repository and the implementation branch subject to step 4.
- Protected: accepted plan, specification, commits, review verdicts, card history, evidence paths, Hindsight entries and customer repositories outside the delivery workspace.

## Procedure

1. Inspect the card, its runs, named branch, workspace and working tree. Record each candidate's path, size, age and removal reversibility.
2. Show the customer the candidate list and planned keeps with reasons before removing anything.
3. Remove only approved items, smallest reversible first. Order: temporary directories, generated role-workspace caches, then throwaway containers.
4. Delete the implementation branch only if the customer states the work is accepted and merged, or explicitly releases the branch. Keep the commit reachable via the accepted branch or remote.
5. Recheck the same candidates after removal. Report each as removed, kept or awaiting a decision, with counts, freed space and reasons for every keep.

Completion criterion: the final report marks every candidate removed or kept. Kept items must be untouched.

## Boundaries

- Ask when ownership, purpose or reversibility is unclear. Leave foreign files untouched.
- Never remove a branch that is neither merged nor explicitly released. Never rewrite or force-push history.
- Never remove evidence referenced by a review or a card comment.
- Report a removal that fails; do not retry with broader deletion.
