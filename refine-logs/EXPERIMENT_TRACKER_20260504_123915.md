# Experiment Tracker

**项目**: TRACE-SL  
**日期**: 2026-05-04

| ID | Block | Run | Status | Decision |
|---|---|---|---|---|
| A1 | Estimator | Historical mean / neighbor average baseline | TODO | Required baseline |
| A2 | Estimator | GSP reconstruction on PeMS7_228 | TODO | First transparent estimator |
| A3 | Estimator | Flow-constrained GLS/MAP on PeMS7_228 | TODO | AMPL-compatible estimator |
| A4 | Estimator | Kalman/RTS smoother feasibility check | TODO | Dynamic estimator |
| B1 | Certificate | 200 random layouts certificate-error correlation | TODO | Validate objective |
| B2 | Certificate | Trace/logdet/condition/coherence diagnostics | TODO | Pick main certificate |
| C1 | OR Layout | A-optimal/D-optimal layout model | TODO | Main OR baseline |
| C2 | OR Layout | Coverage/correlation/facility-location MIP | TODO | Strong baseline |
| C3 | OR Layout | Greedy/local search | TODO | Search baseline |
| D1 | RL | Behavior cloning from add/swap trajectories | GATED | Only after OR layouts pass |
| D2 | RL | Cross-budget warm-start test | GATED | Keep RL only if useful |
| E1 | Insight | Budget marginal value curves | TODO | TS narrative |
| E2 | Insight | Regime-specific layout analysis | TODO | Optional extension |

