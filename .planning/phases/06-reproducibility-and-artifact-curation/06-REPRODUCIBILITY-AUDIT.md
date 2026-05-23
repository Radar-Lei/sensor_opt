# Phase 6 Reproducibility Audit

This audit maps REPRO-01 through REPRO-05 to the committed TRACE-SL reproducibility artifacts created or consumed in Phase 6. It is a manuscript-facing handoff map: paper-visible numbers should come from curated aggregate result directories or generated paper-source tables, not from local raw traffic datasets.

## Requirement Map

| Requirement | Status gate | Primary artifacts | Validation evidence |
|---|---|---|---|
| REPRO-01 | Provenance manifest completeness | `TRC-23-02333/trace_sl_results/reproducibility_manifest.json`; `TRC-23-02333/trace_sl_results/REPRODUCIBILITY_MANIFEST.md` | `validate_phase6_reproducibility.py` checks curated Stage 12/13/14 directories, launcher defaults, Python/package metadata, git provenance, seeds, budgets, and candidate counts. |
| REPRO-02 | Raw-data hygiene | `git ls-files -- TRC-23-02333/dataset/`; paper-visible docs under `TRC-23-02333/trace_sl_results/` and this audit | Validator fails if any raw dataset path is tracked, or if paper-visible docs use local raw datasets as evidence rather than as ignored/local launcher inputs. |
| REPRO-03 | Curated result-directory documentation | `TRC-23-02333/trace_sl_results/README.md`; manifest Stage 12/13/14 inventory | Validator requires README references to present curated Stage 12, Stage 13, Stage 14 robustness, Stage 14 candidate-sensitivity directories plus manifest and `paper_sources/`. |
| REPRO-04 | Paper-source provenance | `TRC-23-02333/trace_sl_results/paper_sources/*.csv`; `TRC-23-02333/trace_sl_results/paper_sources/*.md` | Validator requires nonempty generated CSV/Markdown artifacts and `source_stage`, `source_dir`, `source_csv` provenance columns on CSV rows. |
| REPRO-05 | Smoke and aggregate consistency | Phase 4/5 validators; Stage 12/13/14 launchers; Stage 12/14 aggregate CSVs | Validator runs Phase 4 and Phase 5 validators, `bash -n` for Stage 12/13/14 launchers, four `DRY_RUN=1` smoke launchers, and aggregate checks for `gls_map`, `validation_swap_selected`, baseline rows, robustness conditions, and candidate counts 50/100/200/500. |

## Curated Artifact Boundaries

Paper-visible evidence is restricted to committed aggregate artifacts under these curated directories and to generated paper-source outputs:

- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/`
- `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/`
- `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/`
- `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/`
- `TRC-23-02333/trace_sl_results/paper_sources/`

Lower-power external or supporting directories remain documented with their caveats in the results README and manifest. They are not promoted to core evidence by this Phase 6 audit.

## Launcher Smoke Coverage

The final validator performs syntax checks and dry-run command construction for:

1. Stage 12 PeMS7_228 baseline portfolio: `scripts/run_stage12_pems7_228.sh`
2. Stage 13 candidate sensitivity: `scripts/run_stage13_candidate_sensitivity_pems7_228.sh`
3. Stage 14 robustness/stress tests: `scripts/run_stage14_pems7_228_robustness.sh`
4. Stage 14 candidate sensitivity: `scripts/run_stage14_candidate_sensitivity_pems7_228.sh`

Dry runs use `DRY_RUN=1`, `PYTHON_BIN=python`, explicit small environment overrides, and do not execute full experiments.

## Raw-Data Hygiene

Raw traffic datasets remain ignored local inputs. The reproducibility manifest may record launcher `DATA_ROOT` defaults and raw-dataset policy metadata, but raw datasets are not evidence artifacts and must not be committed. The Phase 6 validator checks tracked raw dataset paths with git and fails REPRO-02 if any are found.

## Stage 14 Caveats

Stage 14 robustness remains bounded stress-test evidence for the specified PeMS7_228 perturbations and candidate budgets. It should be described as usefulness under evaluated sensor failure, observation noise, missingness, cost proxy, chronological split, and candidate-pool settings, not as universal deployment robustness.
