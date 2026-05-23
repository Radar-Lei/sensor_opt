---
phase: 06-reproducibility-and-artifact-curation
verified: 2026-05-23T12:00:00Z
status: passed
score: 5/5 must-haves verified
overrides_applied: 0
gaps: []
human_verification: []
---

# Phase 6: Reproducibility and Artifact Curation Verification Report

**Phase Goal:** Make every paper-visible number traceable to curated scripts, summaries, and non-sensitive artifacts while keeping raw datasets local.
**Verified:** 2026-05-23T12:00:00Z
**Status:** passed
**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|---|---|---|
| 1 | REPRO-01 / Roadmap SC1: Scripts/configs record seeds, budgets, candidate counts, package versions where feasible, and provenance for table regeneration. | VERIFIED | Final validator reports `REPRO-01 PASS`. Manifest JSON has schema `trace-sl-reproducibility-provenance-v1`, package metadata, git provenance, Stage 12/13/14 curated inventories, seeds/budgets, candidate defaults, and launcher commands. |
| 2 | REPRO-02 / Roadmap SC2: Raw traffic datasets remain ignored/local and are not committed or used as paper-visible evidence. | VERIFIED | `git ls-files -- TRC-23-02333/dataset/` returned no paths. Manifest records `tracked_raw_dataset_path_count: 0`. Dataset path mentions in docs are local input / raw-data hygiene context only; final validator reports `REPRO-02 PASS`. No raw dataset contents were read during verification. |
| 3 | REPRO-03 / Roadmap SC3: Documentation and manuscript-facing references point only to curated, present, reproducible result directories. | VERIFIED | `TRC-23-02333/trace_sl_results/README.md` references Stage 12, Stage 13, Stage 14 robustness, Stage 14 candidate sensitivity, `reproducibility_manifest.json`, `REPRODUCIBILITY_MANIFEST.md`, and `paper_sources/`. Final validator reports `REPRO-03 PASS`. |
| 4 | REPRO-04 / Roadmap SC4: Paper tables/figures are generated from committed result artifacts rather than manually copied values. | VERIFIED | `scripts/generate_trace_sl_paper_sources.py` verifies source CSVs are tracked under `trace_sl_results` before reading them. Generated paper-source CSVs are nonempty and each includes `source_stage`, `source_dir`, and `source_csv`. Source aggregate CSVs checked during verification are tracked by git. Final validator reports `REPRO-04 PASS`. |
| 5 | REPRO-05 / Roadmap SC5: Smoke/validation scripts check key commands and required aggregate layout/method rows. | VERIFIED | Final validator reports `REPRO-05 PASS`, including Phase 4 validator, Phase 5 validator, `bash -n` for all four launchers, DRY_RUN smoke for Stage 12, Stage 13 candidate sensitivity, Stage 14 robustness, and Stage 14 candidate sensitivity, plus aggregate row checks for `gls_map`, `validation_swap_selected`, required baselines, robustness conditions, and candidate counts 50/100/200/500. |

**Score:** 5/5 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|---|---|---|---|
| `scripts/generate_trace_sl_repro_manifest.py` | Deterministic provenance manifest generator | VERIFIED | Substantive parser/inventory/environment/git provenance implementation; unit tests pass. Inventories curated CSV/JSON/Markdown artifacts and excludes raw dataset evidence paths. |
| `TRC-23-02333/trace_sl_results/reproducibility_manifest.json` | Machine-readable provenance inventory | VERIFIED | Contains Stage 12/13/14 and supporting stage inventories, package metadata, git provenance, launcher defaults, raw-data policy, and zero tracked raw dataset paths. |
| `TRC-23-02333/trace_sl_results/REPRODUCIBILITY_MANIFEST.md` | Human-readable provenance inventory | VERIFIED | Renders manifest with raw-data hygiene, environment, git provenance, curated result stages, launcher defaults, and required artifact inventory. |
| `scripts/generate_trace_sl_paper_sources.py` | Deterministic paper-source table generator | VERIFIED | Reads committed aggregate CSVs only, checks tracked source status, fails on missing required layout labels, writes provenance columns. Review fixes are present. |
| `TRC-23-02333/trace_sl_results/paper_sources/` | Generated manuscript-facing CSV/Markdown sources | VERIFIED | Nonempty generated CSVs: core performance 24 rows, paired deltas 33 rows, robustness 72 rows, candidate/runtime 68 rows, certificate correlations 12 rows; all have provenance columns. |
| `.planning/phases/06-reproducibility-and-artifact-curation/validate_phase6_reproducibility.py` | Final REPRO-01..05 validator | VERIFIED | Substantive fail-closed checks for manifest, raw-data hygiene, docs, paper sources, Phase 4/5 validators, launchers, DRY_RUN commands, and aggregate rows. |
| `.planning/phases/06-reproducibility-and-artifact-curation/test_validate_phase6_reproducibility.py` | Validator regression tests | VERIFIED | Six tests pass, including required four-launcher DRY_RUN coverage and failed Stage 14 timing regression. |
| `.planning/phases/06-reproducibility-and-artifact-curation/06-REPRODUCIBILITY-AUDIT.md` | Human-readable REPRO evidence/caveat map | VERIFIED | Maps REPRO-01..05 to manifest, paper sources, validators, launcher dry-runs, aggregate checks, and raw-data boundary. |
| `TRC-23-02333/trace_sl_results/README.md` | Synchronized result-stage documentation | VERIFIED | Documents curated stage inventory, manifest/paper-source handoff, core evidence directories, lower-power/supporting caveats, and raw dataset non-evidence boundary. |

### Key Link Verification

| From | To | Via | Status | Details |
|---|---|---|---|---|
| `generate_trace_sl_repro_manifest.py` | Stage 12/13/14 launchers | launcher parsing | WIRED | `CURATED_STAGE_ENTRIES` includes Stage 12, Stage 13 candidate sensitivity, Stage 14 robustness, and Stage 14 candidate sensitivity launchers; `parse_shell_defaults()` extracts defaults without sourcing. |
| `generate_trace_sl_repro_manifest.py` | `reproducibility_manifest.json` / `.md` | JSON/Markdown writers | WIRED | CLI writes stable JSON and Markdown via `write_json()` and `write_markdown()`. |
| `generate_trace_sl_paper_sources.py` | committed aggregate CSVs | tracked-source checks and CSV readers | WIRED | `assert_source_is_tracked()` requires aggregate CSVs under `trace_sl_results`; verified source CSVs are tracked. |
| `generate_trace_sl_paper_sources.py` | `paper_sources/` | CSV/Markdown writers | WIRED | Outputs five required CSVs plus core Markdown and README, with provenance columns on every CSV row. |
| `validate_phase6_reproducibility.py` | Phase 4 and Phase 5 validators | subprocess REPRO-05 gate | WIRED | Final validator output includes `Phase 4 validator passed` and `Phase 5 validator passed`. |
| `validate_phase6_reproducibility.py` | DRY_RUN launchers | `required_smoke_commands()` | WIRED | Includes Stage 12 PeMS7_228, Stage 13 candidate sensitivity, Stage 14 robustness, and Stage 14 candidate sensitivity with `DRY_RUN=1`. |

### Data-Flow Trace (Level 4)

| Artifact | Data Variable | Source | Produces Real Data | Status |
|---|---|---|---|---|
| `reproducibility_manifest.json` | `curated_result_stages`, `launcher_defaults`, `environment`, `git` | Launcher text, curated result directories, importlib metadata, read-only git commands | Yes | FLOWING |
| `paper_sources/*.csv` | Generated table rows | Tracked aggregate CSVs under Stage 12/13/14 result directories | Yes | FLOWING |
| `validate_phase6_reproducibility.py` output | REPRO-01..05 status rows | Manifest, docs, paper-source CSVs, Phase 4/5 subprocesses, DRY_RUN launchers, aggregate CSV row checks | Yes | FLOWING |

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|---|---|---|---|
| Manifest generator contracts | `python /home/samuel/projects/sensor_opt/scripts/test_generate_trace_sl_repro_manifest.py` | 3 tests OK | PASS |
| Paper-source generator contracts | `python /home/samuel/projects/sensor_opt/scripts/test_generate_trace_sl_paper_sources.py` | 4 tests OK | PASS |
| Final validator contracts | `python /home/samuel/projects/sensor_opt/.planning/phases/06-reproducibility-and-artifact-curation/test_validate_phase6_reproducibility.py` | 6 tests OK | PASS |
| REPRO-01..05 final gate | `python /home/samuel/projects/sensor_opt/.planning/phases/06-reproducibility-and-artifact-curation/validate_phase6_reproducibility.py --project-root /home/samuel/projects/sensor_opt` | REPRO-01 PASS through REPRO-05 PASS | PASS |
| Raw dataset tracked-path hygiene | `git -C /home/samuel/projects/sensor_opt ls-files -- TRC-23-02333/dataset/` | No output | PASS |
| Paper-source provenance/row counts | Python CSV metadata spot-check | 24/33/72/68/12 rows; all required provenance columns present | PASS |

### Probe Execution

| Probe | Command | Result | Status |
|---|---|---|---|
| N/A | N/A | No Phase 6 `probe-*.sh` path declared; validation is via Python validators and DRY_RUN launchers. | SKIPPED |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|---|---|---|---|---|
| REPRO-01 | 06-01, 06-02, 06-03 | Provenance sufficient for table regeneration | SATISFIED | Manifest, paper-source provenance, package metadata, git provenance, launcher defaults; final validator PASS. |
| REPRO-02 | 06-01, 06-03 | Raw datasets ignored/local and not paper evidence | SATISFIED | `git ls-files` raw dataset path scan empty; manifest count 0; final validator PASS. |
| REPRO-03 | 06-01, 06-03 | Docs cite only curated present reproducible result directories | SATISFIED | Results README and manifest reference curated Stage 12/13/14 directories and paper sources; final validator PASS. |
| REPRO-04 | 06-02, 06-03 | Paper tables/figures generated from committed artifacts | SATISFIED | Generator validates tracked aggregate sources and generated nonempty provenance-backed CSV/Markdown outputs; final validator PASS. |
| REPRO-05 | 06-03 | Smoke/validation scripts check key commands and aggregate rows | SATISFIED | Phase 4/5 validators pass; four required DRY_RUN launchers pass; aggregate rows checked; final validator PASS. |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|---|---:|---|---|---|
| `validate_phase6_reproducibility.py` | 171,174,179,265 | `return {}` after recording validation failures or malformed manifest shape | Info | Not a stub; fail-closed helper behavior after `context.fail()`. |
| Paper-visible docs | Various | `TRC-23-02333/dataset/` mentions | Info | Allowed local-input / raw-data-hygiene context; final validator confirms no raw dataset evidence citation. |

### Human Verification Required

None.

### Gaps Summary

No blocking gaps found. The codebase evidence supports REPRO-01 through REPRO-05. Raw datasets are not tracked and were not read as evidence. Phase 4/5 validators are included in REPRO-05. The required Stage 12, Stage 13 candidate sensitivity, Stage 14 robustness, and Stage 14 candidate sensitivity DRY_RUN launchers are covered. Paper-source artifacts are generated from tracked committed aggregate CSV sources with row-level provenance.

### Notes

- ROADMAP marks Phase 6 as `mode: mvp`, but its goal is not in canonical user-story form (`gsd-sdk query user-story.validate` returned `false`). This report therefore verifies the explicit REPRO-01..05 reproducibility contract requested for Phase 6 rather than producing an MVP user-flow coverage table.
- `gsd-sdk query roadmap.analyze --raw` could not locate ROADMAP from the tool CWD, but `/home/samuel/projects/sensor_opt/.planning/ROADMAP.md` was read directly and contains no later phase to defer Phase 6 gaps to.

---

_Verified: 2026-05-23T12:00:00Z_
_Verifier: Claude (gsd-verifier)_
