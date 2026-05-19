# Writing Note: Greedy Layout Is Offline Planning, Not Sequential Deployment

**Date**: 2026-05-18  
**Project**: TRACE-SL  
**Purpose**: Preserve the paper-writing rationale for explaining greedy A/D-optimal and swap local-search layout algorithms in a realistic transportation sensor deployment setting.

## Core Framing

Greedy A-optimal, greedy D-optimal, and swap local search should be framed as **offline planning algorithms**, not as real-world sequential deployment protocols.

The word “greedy” describes the computational construction of a fixed sensor set under a budget constraint. It does **not** mean that an agency physically installs one sensor, waits for new traffic observations, then decides where to install the next sensor.

In practice, the workflow is:

1. Use historical full-network data, existing detector data, simulation data, or archived planning data to calibrate a transparent reconstruction model.
2. Estimate posterior covariance / uncertainty certificates for candidate sensor layouts.
3. Run greedy or local-search heuristics offline to construct a fixed deployment set `S`.
4. Deploy the selected sensor set as a planning decision.
5. In the evaluation protocol, simulate deployment by revealing only observations on `S` and measuring hidden-network reconstruction error.

Thus, the sequential nature of the algorithm is only a **solver mechanism**. The deployed artifact is a fixed layout.

## Suggested Paper Wording

> We use greedy selection and swap local search as offline optimization heuristics for solving the reconstruction-aware sensor placement problem. The sequential nature of these algorithms should not be interpreted as a sequential deployment policy. Rather, the algorithms use historical calibration data to construct a fixed sensor set under a budget constraint before deployment. During deployment simulation, only the selected sensors are observed, and all unobserved locations are used solely for evaluation.

Alternative shorter version:

> Greedy selection is an offline planning heuristic, not a physical deployment protocol: it incrementally constructs a fixed sensor set using pre-deployment calibration data, after which the selected set is evaluated as a static deployment.

## Why This Is Defensible

This is standard in facility location, p-median, optimal design, and sensor placement: heuristics may build a solution sequentially even when the real decision is a one-shot fixed infrastructure deployment.

The relevant comparison is not “can a planner physically act greedily in real time?” but “does the offline heuristic produce a high-quality fixed layout under a realistic deployment budget?”

## Implication for RL Framing

RL should not be framed as controlling real-time sensor installation unless the problem is explicitly dynamic. In TRACE-SL, RL is only defensible as an **amortized optimizer**:

- Greedy / local search are acceptable offline solvers for small and medium networks.
- For large networks, many budgets, many cities, or many traffic regimes, rerunning local search may become expensive.
- An RL add/swap policy may be trained to imitate or warm-start these OR heuristics and produce good candidate layouts faster on new instances.

Therefore the recommended narrative is:

> offline OR planning → fixed sensor layout → deployment simulation → transparent full-network reconstruction evaluation

not:

> sequential physical sensor deployment → online adaptive installation

## Current Experimental Interpretation

The current PeMS7_228 pilot results should be described as evaluating offline layout heuristics:

- Random layouts establish the distribution of uninformed fixed deployments.
- Greedy A-trace tests whether posterior trace is a useful offline design certificate.
- Greedy D-logdet tests whether information-volume design aligns with hidden reconstruction error.
- Swap local search tests whether local refinement of the certificate objective improves the fixed deployment set.

The empirical finding so far is that GLS/MAP posterior trace is a useful certificate, but minimizing certificate value does not perfectly rank layouts by test MAE. This motivates validation-based multistart local search and strict validation/test separation in the next experiments.
