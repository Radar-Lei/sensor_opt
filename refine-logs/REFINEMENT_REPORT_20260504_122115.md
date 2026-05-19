# Refinement Report

## Starting Direction

强化学习 + OR 优化交通传感器布局，使已布设节点观测能更准确估计全网交通状态，目标 Transportation Science。

## Refined Direction

Dual-guided Offline RL with AMPL/MIP surrogate and CDSTE evaluation。

## Why This Refinement

- 避开 Xing et al. (2026) 的 Embedding-BO TSLP-NFE 直接重合。
- 避开 INSPIRE-GNN (2025) 的普通 RL/GNN sensor placement 直接重合。
- 利用用户现有 CDSTE 代码和 AMPL 资源。
- 强化 Transportation Science 需要的 formulation、bounds、dual interpretation 和 deployment insight。

## Remaining Open Questions

- AMPL surrogate 的最佳形式是 coverage/correlation/facility-location 还是 null-space observability。
- CDSTE 是否先预训练再固定，还是每个 layout 重新训练。
- RL 用 behavior cloning + reranking 是否足够，还是需要完整 offline RL。

