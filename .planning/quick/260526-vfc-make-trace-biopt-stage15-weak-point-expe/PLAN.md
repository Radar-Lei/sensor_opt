---
status: in_progress
created: "2026-05-26"
quick_id: "260526-vfc"
slug: "make-trace-biopt-stage15-weak-point-expe"
---

# Make TRACE-BiOpt Stage15 Weak-Point Experiments Fast and Diagnosable

Task: Make TRACE-BiOpt Stage15 weak-point experiments fast and diagnosable
without changing the single-objective method boundary.

Evidence from the first run:

- `scripts/run_stage15_biopt_weak_points.sh` reached PeMS7_1026 10% budget.
- It stayed at `budget_start` for more than two minutes before manual
  termination, so the current TRACE-BiOpt objective search lacks sufficient
  progress visibility and is too heavy for rapid weak-point iteration.

Scope:

1. Add TRACE-BiOpt progress records inside forward and exchange refinement.
2. Add a faster deterministic active-set/seed option that still uses the same
   TRACE-BiOpt objective and no baseline-pool selection.
3. Make weak-point script defaults produce quick diagnostic evidence first.
4. Run focused tests and a lightweight weak-point diagnostic.

Out of scope:

- Claiming final dominance before multi-seed Stage15 evidence exists.
- Adding baselines into TRACE-BiOpt as candidate starts.
