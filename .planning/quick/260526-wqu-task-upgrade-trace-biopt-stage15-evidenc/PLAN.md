# Quick Plan: TRACE-BiOpt Stage15 Evidence Configuration

## Goal

Upgrade the Stage15 TRACE-BiOpt evidence launcher after seed-25 all-budget
diagnostics exposed Seattle 20 percent and 30 percent failures under the
smaller search budget.

## Tasks

- Record the Seattle high-budget failure and identify whether objective weights
  or solver search budget caused it.
- Keep TRACE-BiOpt as one objective, and expose deterministic dataset-prefixed
  solver-budget overrides in the Stage15 launcher.
- Verify the launcher with DRY_RUN, unit tests, and a seed-25 all-budget
  evidence run.
- Update TRACE-BiOpt specification and theory evidence gates with the new
  evidence status.

