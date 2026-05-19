# Review Summary

本轮 review 响应用户新增约束：full-network state estimation 不希望使用太黑箱的 DL。

## Verdict

接受该约束，并将主方法从 CDSTE-driven DOPPLER 改为 transparent-estimator-driven TRACE-SL。这个 pivot 更适合 Transportation Science：估计器可解释、可建模、可给 uncertainty/certificate，OR 贡献更清晰。

## Key Review Points

- CDSTE/GNN/diffusion 可作为 optional upper bound comparison，但不能作为主 estimator。
- 首要 pilot 应是 CPU-only GSP/GLS/Kalman/CS reconstruction，而不是 GPU 训练。
- RL 不是默认必要组件；必须通过 search amortization 或 transfer 证明价值。
- 如果 OR-only 已经足够强，应把论文主线改成 OR-only transparent sensor layout。

