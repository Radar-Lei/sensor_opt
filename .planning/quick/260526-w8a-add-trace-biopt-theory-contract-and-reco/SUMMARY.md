---
status: complete
completed: "2026-05-26"
quick_id: "260526-w8a"
slug: "add-trace-biopt-theory-contract-and-reco"
---

# Summary

Added the TRACE-BiOpt theory contract and recorded the completed 3-seed
weak-point dominance evidence.

Changes:

- Added `TRACE_BIOPT_THEORY.md` with scoped theorem statements for MAP closed
  form/stability, posterior trace Bayes risk, uniform size-k layout
  generalization, exchange optimality certificate, and CVaR robustness.
- Updated `TRACE_BIOPT_SPEC.md` to link the theory contract and current
  3-seed 10% weak-point evidence.
- Updated `.planning/STATE.md` with the new quick task and remaining all-budget
  Stage15 evidence gate.

Evidence:

- `TRC-23-02333/trace_sl_results/stage15_biopt_weak_points_3seed/combined/TRACE_BIOPT_DOMINANCE.md`
  shows TRACE-BiOpt beating the best non-BiOpt baseline on PeMS7_1026,
  PeMS7_228, and Seattle at 10% budget across seeds 25, 26, and 27.

Remaining work:

- Run all planned budgets and enough seeds for paired tests.
- Generate Stage15 claim contracts before final TR-B dominance wording.
