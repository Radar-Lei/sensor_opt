---
quick_id: 260531-ftf
slug: apply-gpt-pro-round1-manuscript-revisions
status: complete
date: 2026-05-31
---

# Summary

Completed in this round:
- Replaced the manuscript Figure 1 reference with the user-specified framework image.
- Moved secondary comparison and mechanism tables out of the main body and into the appendix.
- Cropped the main optimization figure so the body now shows objective descent only, while the full accepted-step mix remains in the appendix.
- Unified the main claim wording around `21 pre-registered non-BiOpt baselines in the tested regimes`.
- Softened conclusion language so the bounded exact benchmark is not presented as a full-network guarantee.
- Searched the whole project tree, not just `paper/`, and confirmed the latest audited experiment evidence lives under `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/` with key updates on 2026-05-30, so no rerun was needed for this revision pass.
- Reconciled the manuscript math with the audited local implementation: clarified selection-mask notation, switched the paper-facing posterior certificate to the normalized full-state posterior trace used by code and evidence, defined the smooth-L1/Huber scaling explicitly, aligned the CVaR notation with `cvar_tail_fraction`, and described the relaxed initializer as deterministic active-pool finite-difference projected updates.
- Recompiled `paper/main.pdf` successfully after the math-consistency patch while keeping Figure 1 on the current JPG version.

Residual follow-up:
- The PDF still emits duplicate destination warnings from the Elsevier float/hyperref stack; this does not block compilation but should be cleaned before final submission packaging.
- Additional appendix wording can still be de-audited further if the manuscript needs one more presentation pass, but it is not required for the current user-requested revision scope.
