# CONTROL

## Status Contract

status_file: `.planning/goals/trace-biopt-trb-p0/PLAN.md`
attempt_log: `.planning/goals/trace-biopt-trb-p0/ATTEMPTS.md`
durable_notes: `.planning/goals/trace-biopt-trb-p0/NOTES.md`
update_memory_after: each edit/check cycle
check_control_before: phase change, strategic pivot, expensive step

## Human Priorities

primary_priority: submission-quality wording and contract consistency
secondary_priority: preserve current evidence chain and avoid unnecessary artifact churn

## Scope Knobs

allowed_files:
- `TRACE_BIOPT_SPEC.md`
- `TRACE_BIOPT_THEORY.md`
- `paper/sections/*.tex`
- `paper/tables/table_theory.tex`
- `figures/table_theory.tex`
- generated paper/evidence artifacts produced by `scripts/refresh_current_best_trace_biopt_paper_chain.sh`
- `.planning/goals/trace-biopt-trb-p0/*.md`

protected_files:
- Figure 1 image assets
- Figure 1 manuscript/caption content
- unrelated model/training code
- dependency manifests and environment configuration

max_blast_radius: P0 manuscript/contract synchronization plus directly relevant refresh outputs

## Resource Knobs

max_runtime_per_step: none
max_parallel_jobs: use normal local shell parallelism only
network_allowed: false unless final refresh or existing repo command requires it
external_api_allowed: false

## Decision Gates

require_approval_for:
- changing Figure 1
- adding a Figure 1 AI-generation disclosure
- running new large experiments
- changing dependencies
- adding global optimality or approximation claims
- editing unrelated model/training code
- expanding beyond P0 sync and final refresh verification

## Latest Human Nudge

Keep Figure 1 exactly as it is. Do not modify it and do not say in the article that it is AI-generated.
