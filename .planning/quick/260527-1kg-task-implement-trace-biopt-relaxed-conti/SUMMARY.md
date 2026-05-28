# Quick Summary: TRACE-BiOpt Continuous Relaxation Initializer

## Completed

- Added `project_capped_simplex` for deterministic projection onto the capped
  budget simplex.
- Added `trace_biopt_relaxed_objective`, which evaluates relaxed sensor weights
  through fractional GLS/MAP observation weights, hidden Huber reconstruction
  risk, posterior trace, scenario CVaR trace, and spatial redundancy.
- Added `trace_biopt_initializer=relaxed_rounding`, which runs projected
  finite-difference relaxation, applies top-k rounding, and then uses the same
  TRACE-BiOpt exchange refinement as the discrete initializers.
- Exposed relaxed initializer controls in `transparent_estimator_eval.py` and
  `scripts/run_stage15_biopt_weak_points.sh`.
- Updated `TRACE_BIOPT_SPEC.md`, `TRACE_BIOPT_THEORY.md`, and planning state
  to distinguish implemented relaxed-rounding capability from the current
  `auto`-initializer dominance evidence.

## Verification

- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py`
- `pytest -q TRC-23-02333/test_transparent_estimator_eval.py`

## Remaining

- Run Stage15 evidence with `TRACE_BIOPT_INITIALIZER=relaxed_rounding` before
  making any relaxed-initializer-specific dominance claim.
