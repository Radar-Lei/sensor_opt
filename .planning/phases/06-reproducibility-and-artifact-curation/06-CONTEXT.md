# Phase 06 Context: Reproducibility and Artifact Curation

## Source Inputs Read

- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/STATE.md`
- `.planning/PROJECT.md`
- `.planning/phases/04-core-experiment-evidence/04-VERIFICATION.md`
- `.planning/phases/05-robustness-and-generality/05-VERIFICATION.md`
- `.planning/phases/05-robustness-and-generality/05-REVIEW.md`
- `TRC-23-02333/trace_sl_results/README.md`
- `scripts/run_stage12_pems7_228.sh`
- `scripts/run_stage13_candidate_sensitivity_pems7_228.sh`
- `scripts/run_stage14_pems7_228_robustness.sh`
- `scripts/run_stage14_candidate_sensitivity_pems7_228.sh`
- `.planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py`
- `.planning/phases/05-robustness-and-generality/validate_phase5_robustness.py`

## Decisions

- **D-01:** Phase 6 must curate, validate, and generate from existing Phase 4/5 committed artifacts; it must not regenerate raw experimental evidence.
- **D-02:** Raw traffic datasets must remain ignored/local, must not be committed, and must not be cited as paper-visible evidence.
- **D-03:** The implementation should be minimal, deterministic, and artifact-backed; no long experiment reruns are required for this phase.
- **D-04:** Phase 6 must include a final validator covering REPRO-01 through REPRO-05.
- **D-05:** Paper table/figure source material must be generated from committed result artifacts where feasible; manuscript rendering can consume generated CSV/Markdown sources in the paper-writing phase.
- **D-06:** Provenance capture should avoid new dependencies and record Python/package versions where available, git commit/status, launchers, seeds, budgets, candidate counts, and curated result directory inventory.
- **D-07:** Repository documentation and manuscript-facing references should point only to curated, present, reproducible result directories and generated paper-source artifacts.
- **D-08:** Research was skipped; planning is based on the roadmap, requirements, project state, Phase 4/5 verification material, existing launchers, and existing validators.

## Deferred Ideas

- Long experiment reruns or raw evidence regeneration.
- Committing raw traffic datasets or making them paper-visible evidence.
- Full manuscript figure rendering/layout work; Phase 6 produces deterministic source CSV/Markdown artifacts for later rendering.
- Adding new package dependencies, lockfile tooling, containers, or external services.

## Claude's Discretion

- Split work into parallel Wave 1 generation plans and a Wave 2 final validation/documentation plan.
- Use small Python CLI scripts with the existing repository style: standard library plus pandas only where already used.
- Generate human-readable Markdown alongside machine-readable CSV/JSON where this improves paper handoff without duplicating numbers manually.

## Source Coverage Audit

| Source | ID | Feature / Requirement | Plan | Status | Notes |
|---|---|---|---|---|---|
| GOAL | — | Make every paper-visible number traceable to curated scripts, summaries, and non-sensitive artifacts while keeping raw datasets local. | 06-01, 06-02, 06-03 | COVERED | Manifest, paper-source generation, docs sync, and final validator jointly close the goal. |
| REQ | REPRO-01 | Scripts, configs, and summaries encode seeds, budgets, candidate counts, package versions where feasible, and enough provenance for table regeneration. | 06-01, 06-03 | COVERED | Provenance manifest plus final validator checks required fields. |
| REQ | REPRO-02 | Raw traffic datasets remain ignored and uncommitted; paper-visible artifacts use summaries/checksums/non-sensitive metadata only. | 06-01, 06-03 | COVERED | Raw-data git hygiene and doc/evidence citation scan. |
| REQ | REPRO-03 | Repository documentation and paper narrative cite only curated, present, reproducible result directories. | 06-01, 06-03 | COVERED | Manifest inventories curated dirs; docs update and validator enforce present curated paths. |
| REQ | REPRO-04 | Paper-ready tables and figures are generated from committed result artifacts rather than manually copied numbers. | 06-02, 06-03 | COVERED | Generated CSV/Markdown paper-source tables and source-data files. |
| REQ | REPRO-05 | Smoke tests or validation scripts check key commands and required aggregate layout/method rows. | 06-03 | COVERED | Final validator calls existing Phase 4/5 validators, launcher dry-runs, generated-source checks, and layout/method row checks. |
| CONTEXT | D-01 | Curate/validate/generate from existing Phase 4/5 committed artifacts; no raw experiment regeneration. | 06-01, 06-02, 06-03 | COVERED | All tasks operate on committed aggregate artifacts and dry-run launchers. |
| CONTEXT | D-02 | Raw datasets remain ignored/local and not cited as evidence. | 06-01, 06-03 | COVERED | Git tracked-file scan plus documentation evidence scan. |
| CONTEXT | D-03 | Minimal, deterministic, artifact-backed; no long reruns. | 06-01, 06-02, 06-03 | COVERED | Scripts read existing CSV/JSON/Markdown and use dry-run smoke checks only. |
| CONTEXT | D-04 | Include final validator for REPRO-01..05. | 06-03 | COVERED | Plan 06-03 creates and tests `validate_phase6_reproducibility.py`. |
| CONTEXT | D-05 | Generate paper table/figure sources from committed artifacts. | 06-02, 06-03 | COVERED | Plan 06-02 creates generator and outputs; Plan 06-03 validates them. |
| CONTEXT | D-06 | Capture package/provenance without new dependencies. | 06-01, 06-03 | COVERED | Standard-library metadata capture and validation. |
| CONTEXT | D-07 | Docs/manuscript-facing references only cite curated present reproducible result directories. | 06-03 | COVERED | README sync and final validator. |
| CONTEXT | D-08 | Use roadmap/requirements/Phase 4/5 verification because research skipped. | 06-01, 06-02, 06-03 | COVERED | Plans reference this context and existing verification artifacts. |

## Dependency Graph

| Plan | Needs | Creates | Wave |
|---|---|---|---|
| 06-01 | Existing Phase 4/5 result artifacts and launchers | Reproducibility manifest script plus JSON/Markdown manifest | 1 |
| 06-02 | Existing Phase 4/5 aggregate CSV artifacts | Paper-source generation script plus CSV/Markdown paper-source outputs | 1 |
| 06-03 | Outputs from 06-01 and 06-02 plus existing Phase 4/5 validators | Final REPRO-01..05 validator/tests and documentation synchronization | 2 |

Same-wave plans have no planned file overlap.
