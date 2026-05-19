# Refinement Report

## User Constraint

下游 full-network state estimation 不想使用太黑箱的 DL。

## Refinement

将主 idea 从 **DOPPLER: Dual-guided Offline RL for CDSTE Sensor Layout** 改为 **TRACE-SL: Transparent Reconstruction-Aware Sensor Layout via OR-guided RL**。

## What Changed

- 主 estimator: CDSTE -> GSP / GLS / Kalman / compressed sensing / flow-constrained optimization。
- 主 reward/objective: CDSTE validation error -> transparent reconstruction risk and certificates。
- RL role: main solver -> optional amortized add/swap search policy。
- First pilot: GPU CDSTE harness -> CPU transparent estimator harness。

## Why Better

- 更符合用户偏好。
- 更符合 Transportation Science 对 OR rigor、可解释性和管理 insight 的期待。
- 降低深度模型训练成本和黑箱审稿风险。

