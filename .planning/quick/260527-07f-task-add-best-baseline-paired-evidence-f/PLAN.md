# Quick Plan: TRACE-BiOpt Best-Baseline Paired Evidence

## Goal

Make the Stage15 TRACE-BiOpt dominance artifact compare against the actual
best pre-registered non-BiOpt baseline in each dataset-budget group, then run
the explicit evidence launcher over all planned budgets for seeds 25, 26, and
27.

## Tasks

- Update paired comparison generation so every non-BiOpt layout can be the
  paired baseline, including validation-swap and RCSS selected layouts.
- Attach paired-test statistics for the selected best baseline to
  `TRACE_BIOPT_DOMINANCE.md` and its CSV source.
- Run `stage15_biopt_allbudget_3seed_v2` for PeMS7_1026, Seattle, and
  PeMS7_228 at 10, 20, and 30 percent budgets.
- Record the resulting evidence and remaining significance limits in the
  TRACE-BiOpt spec, theory contract, and GSD state.
