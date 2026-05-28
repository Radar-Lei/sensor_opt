# Quick Plan: TRACE-BiOpt Continuous Relaxation Initializer

## Goal

Close the method gap from `gpt_pro_suggestion_round1.md` by adding a
deterministic continuous-relaxation plus top-k rounding initializer to
TRACE-BiOpt while keeping baselines outside the method.

## Tasks

- Add capped-simplex projection for `s in [0,1]^n` with `sum_i s_i = k`.
- Define a relaxed TRACE-BiOpt objective using fractional observation weights
  in the same lower-level GLS/MAP reconstruction.
- Add `relaxed_rounding` as a TRACE-BiOpt initializer and feed its rounded
  layout into the existing single-objective exchange refinement.
- Expose CLI and Stage15 launcher controls for relaxed iterations, step size,
  finite-difference epsilon, and active coordinate pool.
- Add regression tests and update method/theory docs with the evidence
  boundary.
