# Pipeline Summary

**Problem**: 有限传感器预算下，用非黑箱状态重构模型从 sparse observations 估计全网交通状态。  
**Final Method Thesis**: 传感器布局应优化透明逆问题的可恢复性；OR 负责 formulation/certificate，RL 仅在大规模重复布局搜索中摊销 add/swap 决策。  
**Final Verdict**: READY FOR NON-DL PILOT  
**Date**: 2026-05-04

## Final Deliverables

- Proposal: `refine-logs/FINAL_PROPOSAL.md`
- Experiment plan: `refine-logs/EXPERIMENT_PLAN.md`
- Idea report: `idea-stage/IDEA_REPORT.md`
- Candidates: `idea-stage/IDEA_CANDIDATES.md`

## Contribution Snapshot

- Dominant contribution: transparent reconstruction-aware sensor layout。
- Optional contribution: OR-guided RL for amortized add/swap layout search。
- Explicitly rejected complexity: CDSTE/GNN/diffusion as main estimator。

## Must-Prove Claims

- Transparent GSP/GLS/Kalman/CS estimators can reconstruct full-network state from sparse sensors。
- OR layout improves reconstruction and gives meaningful certificates。
- RL is only retained if it improves search efficiency or transfer。

## First Runs to Launch

1. CPU-only GSP/GLS estimator harness on PeMS7_228。
2. Random layout certificate-error correlation study。
3. AMPL A-optimal/D-optimal layout baseline。

## Main Risks

- Transparent estimators too weak: strengthen priors/dynamics before layout search。
- Certificates weakly predict error: use empirical validation objective or hybrid certificate。
- RL unnecessary: remove from core and make paper OR-only。

## Next Action

Implement the non-DL estimator harness before any RL work.

