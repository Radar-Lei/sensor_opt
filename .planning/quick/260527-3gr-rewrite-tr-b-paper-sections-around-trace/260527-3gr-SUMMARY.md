---
quick_id: 260527-3gr
slug: rewrite-tr-b-paper-sections-around-trace
status: complete
completed_at: 2026-05-27T02:44:00+08:00
---

# Quick Task 260527-3gr Summary

Rewrote the main TR-B paper source around TRACE-BiOpt as the primary method.

## Completed

- Updated title, abstract, highlights, introduction, problem statement, method/theory, experiments, ablation routing, discussion, conclusion, and appendix.
- Added `paper/tables/table_trace_biopt_dominance.tex` with the Stage15 ten-seed best-baseline dominance table.
- Reframed old TRACE-SL pool/validation-swap material as historical diagnostic evidence or a pre-registered comparator, not the main method.
- Added theorem-level method support: MAP closed form/stability, posterior trace Bayes risk, all-layout validation generalization, and exchange certificate.
- Preserved claim caveats: dominance is against pre-registered non-BiOpt baselines in tested regimes; PeMS7_1026 30% remains directional.

## Verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from `paper/` completed and produced `paper/main.pdf`.
- `pytest -q TRC-23-02333/test_transparent_estimator_eval.py TRC-23-02333/test_summarize_trace_sl_rcss.py scripts/test_generate_trace_biopt_dominance.py scripts/test_generate_trace_biopt_claim_contract.py tests/test_stage12_runtime_fast_paths.py tests/test_stage12_runtime_trace_cache.py` passed: 58 tests, 13 subtests.
- Checked `trace_biopt_best_baseline_delta.csv` has 9/9 dominance rows and `trace_biopt_claim_contract.json` has aggregate status `supported_directional`.
- Updated `paper/PAPER_CLAIM_AUDIT.md` and `.json` with a local deterministic Stage15 paper-to-evidence audit: no numeric mismatch found, verdict `WARN` because a fresh external zero-context audit is still pending.
- `git diff --check` passed.

## Remaining Caveats

- PDF has non-fatal underfull/overfull layout warnings and one existing BibTeX empty-pages warning.
- Full submission assurance still requires paper claim audit, citation audit, proof audit, and external verifier gates.
