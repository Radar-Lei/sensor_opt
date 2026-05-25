# Phase 8: External Stage12 Evidence - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-25
**Phase:** 08-external-stage12-evidence
**Areas discussed:** Performance-blocked Phase 8 disposition

---

## Area Selection

| Option | Description | Selected |
|--------|-------------|----------|
| Blocked disposition | Phase 8 已执行但未完成 EVID-03/EVID-04：是保持 fail-closed 阻塞，还是允许后续 Phase 9/10 在明确 blocked 前提下继续？ | |
| Rerun strategy | 如何约束下一轮 PeMS7_1026/Seattle 真实补跑：必须完整十 split、允许分批/remote/queue，还是先降低范围只做诊断？ | |
| Evidence threshold | 什么产物才允许把 PeMS7_1026 或 Seattle 从 blocked 改为 complete：split 数、aggregate 文件、git tracking、p-values 缺失标注等。 | |
| Handoff wording | 下游 Phase 9/10 和论文写作应如何引用 Phase 8：external evidence blocked、conditional/supporting、还是明确 forbidden from core claims。 | |

**User's choice:** 主要是运行了一遍发现，太慢了, 16小时都没完成一个seed
**Notes:** This reframed the update around runtime infeasibility rather than ordinary evidence-status wording.

---

## Stage12 Next Strategy

| Option | Description | Selected |
|--------|-------------|----------|
| Fail closed | Phase 8 保持 blocked，不再把当前 Stage12 作为 v1.1 必须完成路径；后续 Phase 9/10 必须在 PeMS7_1026/Seattle excluded/conditional 前提下继续。 | |
| Optimize first | 先新增性能优化/缩减计算计划，只有优化后能完成 ten-split 才重新打开 EVID-03/EVID-04。 | ✓ |
| Remote queue | 保留 Stage12 标准不变，但把下一步定义为使用远程/队列/GPU或CPU服务器跑完整 ten-split。 | |
| Reduced evidence | 降低外部证据门槛，用少 seed 或较小候选数作为 supporting evidence，但不得称为 Stage12 complete。 | |

**User's choice:** Optimize first
**Notes:** Current partial/slow run must not be treated as sufficient evidence.

---

## Optimization Scope

| Option | Description | Selected |
|--------|-------------|----------|
| Runtime only | 只优化工程性能、并行、缓存、增量聚合、作业队列；Stage12 budgets/baseline portfolio/evidence标准不变。 | ✓ |
| Safe knobs | 允许调整候选数、swap pool、scenario count 等计算旋钮，但必须记录为 Stage12-compatible 或 Stage12-lite，不能混淆。 | |
| Pilot shrink | 先做小规模诊断配置找瓶颈，诊断结果只指导优化，不进入 evidence contract。 | |
| You decide | 由规划阶段根据 profiling 结果决定允许哪些改动，但必须保留 fail-closed gate。 | |

**User's choice:** Runtime only
**Notes:** Evidence standard, budgets, and baseline portfolio stay fixed.

---

## Downstream Milestone Routing

| Option | Description | Selected |
|--------|-------------|----------|
| Continue gated | Phase 9/10 可以继续做 ablation/classification/theory，但必须把 PeMS7_1026 和 Seattle 标为 blocked/conditional，不得解锁 v1.1 完成。 | |
| Stop milestone | 暂停 Phase 9/10，先开一个性能优化 phase，等 Stage12 证据完成后再继续 v1.1。 | ✓ |
| Split milestone | 把 v1.1 改成不包含外部 Stage12 完成，另起 v1.2 专门做外部证据优化和补跑。 | |
| You decide | 让后续 planner 根据 roadmap 健康状态选择，但保留所有 fail-closed gate。 | |

**User's choice:** Stop milestone
**Notes:** The milestone should not proceed to Phase 9/10 as normal while Stage12 is computationally blocked.

---

## Performance Gate Before Full Retry

| Option | Description | Selected |
|--------|-------------|----------|
| One seed done | PeMS7_1026 和 Seattle 至少各有一个 full Stage12-compatible seed 在可接受时间内完成，并能正常聚合/追踪，再启动 ten-split。 | ✓ |
| Projected only | 只要 profiling 显示理论上 ten-split 可完成，就允许启动完整运行。 | |
| PeMS first | 先只要求 PeMS7_1026 一个 full seed 通过；Seattle 继续 blocked。 | |
| You decide | 让性能优化计划定义具体阈值，但必须有实测证据而非口头判断。 | |

**User's choice:** One seed done
**Notes:** Both external datasets need an empirical full-seed success before full ten-split retry.

---

## Claude's Discretion

- Choose exact performance profiling and optimization plan later, while preserving runtime-only scope and fail-closed gates.

## Deferred Ideas

- Full PeMS7_1026 and Seattle ten-split Stage12 rerun is deferred until runtime-only optimization proves one full Stage12-compatible seed can complete for each dataset.
- Phase 9/10 continuation is deferred while v1.1 is stopped at the Phase 8 performance blocker.
