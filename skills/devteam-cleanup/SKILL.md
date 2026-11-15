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

Use when the customer asks for cleanup: `/devteam-cleanup`, "clean up", "räum auf", or an equivalent instruction naming cleanup.

No step in the delivery flow requires cleanup. Accepted review is not customer acceptance, and corrections may continue on the same branch.

## What cleanup covers

Candidates are artifacts the delivery produced that the customer no longer needs: scratch scripts and temporary directories in the role workspaces, throwaway containers and images created for the delivery, stray files outside the repository, and — only under the condition below — the implementation branch.

Never cleanup scope: the accepted plan, the specification, commits, review verdicts, card history, evidence paths, Hindsight entries, and the customer's repositories outside the delivery workspace.

## Procedure

1. Read the card, its runs, the named branch, the workspace and the working tree. List every candidate with its path, size, age and whether removal is reversible.
2. Present that list to the customer before any removal. Name what you intend to keep and why.
3. Remove only the items the customer approved, smallest reversible first: temporary directories, then generated caches in the role workspace, then throwaway containers.
4. Delete the implementation branch only when the customer states that the work is accepted and merged, or explicitly releases the branch. Keep the commit reachable through the accepted branch or the remote.
5. Read the same candidates again after removal. State each one as removed, kept, or awaiting a decision.
6. Report counts, freed space and every kept item with its reason.

Completion criterion: every candidate from step 1 appears in the final report as removed or kept, and no kept item was touched.

## Boundaries

- Ask instead of deciding when an item's owner, purpose or reversibility is unclear; foreign files stay untouched.
- Never remove a branch that is neither merged nor explicitly released, and never rewrite or force-push history.
- Never remove evidence referenced by a review or a card comment.
- Report a removal that fails; do not retry with broader deletion.
