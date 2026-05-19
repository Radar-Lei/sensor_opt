# Idea Candidates

| # | Idea | Pilot Signal | Novelty | Reviewer Score | Status |
|---|------|--------------|---------|----------------|--------|
| 1 | TRACE-SL: Transparent Reconstruction-Aware Sensor Layout via OR-guided RL | Not launched; CPU pilot ready | 8/10 | 8.5/10 local review | RECOMMENDED |
| 2 | Regime-Aware Sensor Layout for Transparent Reconstruction | Not launched | 7.5/10 | 7.5/10 | BACKUP |
| 3 | Value-of-Information Sensor Layout with Posterior Covariance Certificates | Not launched | 7/10 | 8/10 | BACKUP |
| 4 | Hybrid Transparent Estimator Ensemble | Not launched | 6.5/10 | 6.5/10 | SUPPORTING |

## Active Idea: #1 - TRACE-SL

- Hypothesis: Sensor layouts optimized for transparent reconstruction certificates, such as posterior covariance, graph-smoothness energy, observability condition, and compressed-sensing coherence, will produce accurate and interpretable full-network traffic state estimates without relying on black-box DL.
- Key evidence: recent and classical literature supports GSP, CS, Kalman, GLS, and dynamics observability as transparent estimators; gap remains in unifying them with OR-guided layout search and optional RL amortization.
- Next step: implement CPU-only GSP/GLS estimator harness and certificate-error correlation study.

