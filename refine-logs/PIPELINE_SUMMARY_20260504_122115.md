# Pipeline Summary

**Problem**: 有限传感器预算下选择交通网络节点，使 CDSTE 利用已观测节点估计全网交通状态。  
**Final Method Thesis**: 用 OR relaxation/dual/local-search guidance 训练离线 RL policy，在昂贵 CDSTE objective 下快速产生高质量、可解释的传感器布局。  
**Final Verdict**: READY  
**Date**: 2026-05-04

## Final Deliverables

- Proposal: `refine-logs/FINAL_PROPOSAL.md`
- Experiment plan: `refine-logs/EXPERIMENT_PLAN.md`
- Experiment tracker: `refine-logs/EXPERIMENT_TRACKER.md`
- Idea report: `idea-stage/IDEA_REPORT.md`

## Contribution Snapshot

- Dominant contribution: OR-structured learning for sensor layout under expensive neural traffic-state estimation。
- Supporting contribution: budget marginal value and layout interpretability via dual/surrogate diagnostics。
- Rejected complexity: new estimator architecture, LLM/VLM components, mobile sensor relocation as main task。

## Must-Prove Claims

- DOPPLER improves CDSTE full-network estimation vs strong baselines。
- OR guidance is necessary and improves sample/search efficiency。
- Layout decisions are interpretable enough for Transportation Science。

## First Runs to Launch

1. PeMS7_228 fixed-layout CDSTE evaluation harness。
2. AMPL coverage/correlation MIP baselines。
3. Random/centrality/OR baseline variance study at 20% budget。

## Main Risks

- OR surrogate weakly correlates with CDSTE objective: use as candidate generator and learn residual。
- RL does not beat local search: reposition around amortized transfer/search-cost efficiency。
- CDSTE run cost too high: use frozen/short-run proxy before full retraining。

## Next Action

Proceed to implementation of the layout evaluation harness and OR baselines.

