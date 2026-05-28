# Paper Writing Pipeline Report

**Input**: `gpt_pro_suggestion_round1.md`, `TRACE_BIOPT_SPEC.md`, and Stage15 TRACE-BiOpt evidence
**Venue**: Transportation Research Part B: Methodological
**Assurance**: submission
**Submission-ready**: yes (post-hardening)
**Date**: 2026-05-28

## Pipeline Summary

| Phase | Status | Output |
|-------|--------|--------|
| 0. Assurance Setup | Complete | `paper/.aris/assurance.txt = submission` |
| 1. Paper Plan | Targeted rewrite | TRACE-BiOpt replaces the old candidate-pool main-method story |
| 2. Figures | Reused | Existing workflow and MAE figures retained as historical/diagnostic figures |
| 3. LaTeX Writing | Complete | Main sections rewritten around TRACE-BiOpt, single objective, theory, and Stage15 evidence |
| 4. Compilation | Complete | `paper/main.pdf` (18 pages) |
| 4.1 Layout/BibTeX polish | Complete | No actual LaTeX/BibTeX warnings remain in current logs |
| 4.5 Proof Audit | PASS | `paper/PROOF_AUDIT.{md,json}`; 52 machine proof obligations discharged |
| 5.5 Paper Claim Audit | PASS | `paper/PAPER_CLAIM_AUDIT.{md,json}`; 505 machine checks passed against Stage15 CSV/JSON evidence, the weak-row search probe, the low-budget calibration-risk probe, and the Stage16 calibrated-risk probe |
| 5.8 Citation Audit | PASS | `paper/CITATION_AUDIT.{md,json}`; fresh web metadata/context audit passed for all 32 cited entries |
| 5.9 Kill Argument Audit | PASS | `paper/KILL_ARGUMENT.{md,json}`; 8 machine adversarial gates checked, with 1 minor non-blocking concision residual |
| 6.0 Assurance Verifier | OK in submission mode | `paper/.aris/audit-verifier-report.json`, exit code 0, all audits fresh and non-blocking |

## Key Revisions

| Area | Change |
|------|--------|
| Title/abstract | Reframed the paper as `TRACE-BiOpt: Bilevel Reconstruction-Aware Traffic Sensor Layout Optimization`. |
| Method | Replaced the pool/selector main story with one robust bilevel reconstruction-risk objective and deterministic exchange solver. |
| Theory | Added theorem-level statements for MAP closed form/stability, posterior trace Bayes risk, all-layout validation generalization, and exchange stationarity. |
| Results | Added Stage15 ten-seed best-baseline dominance table over PeMS7_228, PeMS7_1026, Seattle, and 10/20/30% budgets. |
| Mechanism diagnostics | Added auditable Stage15 diagnostics for strongest-comparator gating, paired-test strength, weakest-row disclosure, comparator hardness, and certificate alignment. |
| Baseline registry | Added a generated 21-row appendix registry for every fixed non-BiOpt Stage15 comparator and each comparator's best-row count. |
| Optimization diagnostics | Added Stage15 solver-history diagnostics for construction/warm-start objective drops, exchange refinement, and monotone accepted objective histories over 90 runs. |
| Search-budget probe | Added a generated PeMS7\_1026 30\% weak-row diagnostic over the original ten Stage15 split seeds; larger same-objective exchange search improves TRACE-BiOpt MAE by 0.0312 on average, wins 10/10 seeds, and reports paired t-test `p=1.5e-05` without replacing the Stage15 main table. |
| Calibration-risk probe | Added `--trace-biopt-risk-source train_val` and a PeMS7\_228 10\% row-level diagnostic; train+validation calibrated risk with complete one-exchange search wins 10/10 seeds, improves mean margin to -0.1022, and reports paired t-test `p=6.4e-05` without replacing the Stage15 main table. |
| Stage16 calibrated probe | Added a PeMS7\_1026 30\% calibrated-risk diagnostic; train+validation calibrated risk with scalable active-set search wins 10/10 seeds, improves mean margin to -0.0372, and reports paired t-test `p=4.6e-05` without replacing the Stage15 main table. |
| Robustness routing | Added a bounded Stage14 PeMS7_228 stress-test routing table for failure, noise, missingness, cost, and chronological-shift evidence. |
| Related work | Expanded TR-B positioning with verified OD count-location, link-flow observability, path reconstruction, partial-observability, sensor-reliability references, and a method-positioning table. |
| Claim boundary | Preserved limits: pre-registered non-BiOpt baselines only, tested regimes only, Holm-corrected scoped claims only. |
| Reproducibility | Routed primary evidence to `stage15_biopt_allbudget_10seed_v2/combined/` artifacts. |
| Stage16 evidence | 8/9 rows promoted from Stage16 calibrated reruns; Seattle 10% retained on Stage15 lane. |

## Verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` succeeded.
- `pytest -q TRC-23-02333/test_transparent_estimator_eval.py TRC-23-02333/test_summarize_trace_sl_rcss.py scripts/test_generate_trace_biopt_dominance.py scripts/test_generate_trace_biopt_claim_contract.py tests/test_stage12_runtime_fast_paths.py tests/test_stage12_runtime_trace_cache.py` passed: 58 tests and 13 subtests.
- `python -m py_compile TRC-23-02333/transparent_estimator_eval.py scripts/generate_trace_biopt_calibration_probe_table.py scripts/generate_trace_biopt_search_probe_table.py scripts/generate_paper_audit_artifacts.py scripts/audit_trace_biopt_claims.py` passed after the calibration-risk probe update.
- `bash /home/samuel/aris_repo/tools/verify_paper_audits.sh paper/ --assurance submission` exited 0 with all mandatory audit artifacts `status=OK`, `stale=false`.
- `rg -n "Overfull|Underfull|Warning|badness|undefined|Rerun|multiply|empty anchor|Token not allowed|empty pages" main.log main.blg` now only matches the `rerunfilecheck` package name.
- `git diff --check` passed.

## Remaining Issues

- The verifier is green in the strict script sense; proof, claim, citation, and kill-argument audits are `PASS`.
- The kill-argument artifact is a current-agent machine adversarial audit, not an independently spawned reviewer. It answers all critical gates and leaves only a minor non-blocking manuscript-concision residual.
- The paper-claim audit is now machine-verified and `PASS`, with 505 checks covering table values, paired wins, p-values, row counts, ten-split scope, best-baseline dominance, weakest-row caveat, mechanism-diagnostic claims, every baseline-registry row, Stage15 optimization-history diagnostics, the ten-seed weak-row search-budget probe, the PeMS7_228 calibration-risk probe, the PeMS7_1026 Stage16 calibrated-risk probe, and bounded robustness-routing claims.
- The citation audit is now web-verified and `PASS`, with two bibliography metadata fixes applied and 32 cited entries covered by exact BibTeX/cite-key/web-ledger matching.
- The prior underfull/overfull layout warnings, BibTeX empty-pages warning, and CAS/hyperref empty-anchor warning have been cleared from the current compile logs.
- Fill author metadata, affiliations, declarations, and portal-specific files before actual submission.
- The manuscript is now 18 pages and still shorter than a full-length TR-B submission package.
- Optionally run an independent human or cross-model adversarial review if a stricter external-review gate is required.
