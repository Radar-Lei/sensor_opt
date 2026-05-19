# Final Proposal

**项目名**: TRACE-SL - Transparent Reconstruction-Aware Sensor Layout via OR-guided RL  
**日期**: 2026-05-04  
**目标期刊**: Transportation Science  
**最终判定**: READY FOR NON-DL PILOT  
**Supersedes**: `refine-logs/FINAL_PROPOSAL_20260504_122115.md`

## Problem Anchor

在有限传感器预算下选择固定节点/路段集合，使部署后仅观测这些位置的交通状态时，能够用透明的优化/滤波/信号重构模型估计全网状态。

主估计器必须满足：

- 可写成显式目标函数、约束或状态空间模型。
- 可输出不确定性或可观测性 certificate。
- 可解释 sensor layout 为什么有效。
- 不依赖深度神经网络作为主预测机制。

## Method Thesis

Full-network traffic state estimation should be treated as an inverse problem rather than a black-box imputation problem. Sensor placement should optimize the recoverability of that inverse problem. OR models provide exact/relaxed layout objectives and certificates; RL, if used, only amortizes repeated add/swap search over budgets, networks, and traffic regimes.

## Dominant Contribution

**Transparent reconstruction-aware sensor layout**：把传感器布局和可解释全网状态重构直接耦合。论文贡献不是新 DL estimator，而是一个能解释、能给 bound/certificate、能支持预算决策的 OR+RL sensor planning framework。

## Estimator Layer

### Estimator A: Graph Signal Reconstruction

每个时间步解：

```text
min_x  ||H_S x - y_S||^2_R + lambda x^T L x + gamma ||x - m_t||^2_Q
```

- `H_S`: sensor selection matrix。
- `L`: road graph Laplacian 或 learned correlation Laplacian。
- `m_t`: time-of-day historical prior。
- Certificate: smoothing energy, posterior linear-system condition number, leave-sensor-out residual。

### Estimator B: Flow-Constrained GLS / MAP

```text
min_x  ||H_S x - y_S||^2_R + ||x - mu_t||^2_{Sigma_t^{-1}}
s.t.   B x ≈ q_t
       0 <= flow <= capacity
       speed-flow consistency bounds
```

- 适合 AMPL/amplpy。
- Certificate: posterior covariance trace, flow-balance residual, active constraints。

### Estimator C: Dynamic Kalman / RTS Smoother

```text
x_{t+1} = A_r x_t + w_t
y_t     = H_S x_t + v_t
```

- `A_r` 可按 regime `r` 估计，或来自 linearized CTM/graph VAR。
- Layout objective: A-optimal `tr(P_t(S))`, D-optimal `logdet(P_t(S))`, observability Gramian rank/condition。
- Certificate: posterior covariance and Kalman gain interpretation。

### Estimator D: Compressed Sensing / Sparse Basis

```text
x_t = Psi alpha_t
min_alpha ||H_S Psi alpha_t - y_S||^2 + lambda ||alpha_t||_1
```

- `Psi`: temporal dictionary、graph Fourier basis、PCA basis。
- Layout objective: coherence minimization / recovery error。
- Certificate: measurement coherence, sparsity diagnostics。

## Layout Optimization Layer

1. Exact/relaxed OR baselines:
   - A-optimal design: minimize posterior trace。
   - D-optimal design: maximize information logdet。
   - E-optimal / condition-number minimization。
   - coverage/correlation/facility-location MIP。
   - compressed-sensing coherence minimization。

2. RL policy, only if needed:
   - State: current sensor set, budget left, uncertainty map, residual map, dual/reduced-cost features, observability metrics。
   - Action: add sensor, remove sensor, swap sensor。
   - Reward: reduction in transparent reconstruction risk/certificate, not DL validation loss。
   - Training: imitate exact/greedy/local-search trajectories, then improve with offline RL。

## Explicitly Rejected Complexity

- 不使用 CDSTE/GNN/diffusion 作为主 estimator。
- 不追求 deep imputation SOTA。
- 不用 LLM/VLM。
- 不把 RL 放到 state estimation 内部。

## Success Criteria

- 透明 estimator 在 PeMS7_228/Seattle 上能用 10%-30% sensors 达到合理全网 MAE/RMSE。
- OR-designed layouts 显著优于 random/topology-only。
- TRACE-SL 的 certificate 与 empirical hidden error 有稳定相关性。
- 若 RL 加入，它要在大规模/跨预算场景下减少求解时间或提高 warm-start quality。

