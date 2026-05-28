---
status: in_progress
created: "2026-05-26"
quick_id: "260526-v7m"
slug: "implement-trace-biopt-as-a-single-bileve"
---

# Implement TRACE-BiOpt Single-Method Entry Point

Task: Implement TRACE-BiOpt as a single bilevel reconstruction-aware sensor layout method from `gpt_pro_suggestion_round1.md`.

Scope for this quick task:

1. Add a method specification artifact that states TRACE-BiOpt is one objective and one deterministic solver, not a candidate pool or baseline selector.
2. Add reusable TRACE-BiOpt objective and local-exchange search logic to the existing transparent estimator pipeline.
3. Add CLI/script entry points so Stage15 weak-point and all-baseline runs can include `trace_biopt` as a first-class layout type.
4. Add focused tests that verify deterministic behavior, objective terms, and non-pool semantics.
5. Run the relevant fast tests and record what remains for full experiments.

Out of scope for this quick task:

- Claiming empirical dominance before Stage15 multi-seed weak-point and full baseline experiments complete.
- Rewriting the TR-B manuscript around TRACE-BiOpt before code-level evidence exists.
