---
phase: 09-ablation-and-evidence-classification
status: issues_found
review_depth: standard
files_reviewed: 9
findings:
  critical: 3
  warning: 3
  info: 0
  total: 6
created: 2026-05-25
---

# Phase 09: Code Review Report

**Depth:** standard  
**Files Reviewed:** 9  
**Status:** issues_found

## Summary

审查了 Phase 9 ablation/evidence contract 生成器、测试与生成产物。发现多处 fail-closed 证据策略缺口：生成器会信任 gate 布尔值和 git index，而不是验证已提交的十 split 聚合证据；核心 ablation 行也不会拒绝低于 required split count 的输入。

## Critical Issues

### CR-01: git “tracked” 校验接受 staged 未提交证据，违反 committed aggregate evidence 策略

**File:** `scripts/generate_trace_sl_ablation_evidence_contracts.py:139-151`

**Issue:** `is_git_path_tracked()` 使用 `git ls-files --error-unmatch`，这会把仅 `git add`、尚未提交到 `HEAD` 的文件当作可用证据。注释和 README 声称仅读取 committed aggregate CSVs，但当前实现允许未提交/可变证据进入 contract，证据可复现性不 fail-closed。

**Fix:** 改为验证文件存在于 `HEAD`，并可选拒绝 dirty 输入，例如使用 `git cat-file -e HEAD:<relative>` 或 `git ls-tree HEAD -- <relative>`；测试 fixture 需要创建初始 commit，而不是只 `git add`。

### CR-02: 外部 EVID-03/EVID-04 完成状态只信任 gate 顶层布尔值，未校验 split count 和聚合产物

**File:** `scripts/generate_trace_sl_ablation_evidence_contracts.py:488-558`

**Issue:** `pems_complete` / `seattle_complete` 直接来自 gate 顶层字段；即使 gate 声称 complete 但 `actual_split_count < required_split_count`、缺少 Stage12 聚合 CSV，代码仍会把 PeMS7_1026/Seattle 标记为 `requirement_complete=True` 和 core eligible。这违反 fail-closed evidence policy。

**Fix:** completion 应同时满足：gate 布尔为 true、dataset actual split count 等于 required split count、required aggregate artifacts 存在且已提交到 `HEAD`、paired evidence 可用；任一条件失败均强制 `blocked/conditional`。

### CR-03: ablation contract 不拒绝 split 数不足的核心 Stage12 行

**File:** `scripts/generate_trace_sl_ablation_evidence_contracts.py:401-410`

**Issue:** `_actual_split_count()` 的结果被写入行，但 `validate_ablation_rows()` 没有要求 `actual_split_count == required_split_count`；随后所有行都被标记为 `evidence_status="completed"`。如果源 `gls_map_layout_summary.csv` 某布局只有 1 或 5 split，也会生成 completed held-out evidence。

**Fix:** 在 `validate_ablation_rows()` 中强制所有非随机折叠后的 `actual_split_count` 等于 `REQUIRED_SPLIT_COUNT`；不足时抛出 `AblationEvidenceValidationError`。

## Warnings

### WR-01: 非布尔 gate 值会被 Python truthiness 误判为 true

**File:** `scripts/generate_trace_sl_ablation_evidence_contracts.py:420-423`

**Issue:** `bool(gate.get(...))` 会把字符串 `"false"`、`"0"` 等非空值转换为 `True`，可能意外打开 EVID gate。

**Fix:** 对 gate 字段做严格类型校验：字段必须是 JSON boolean；缺失或类型不匹配时 fail closed。

### WR-02: 重复 budget/layout 或 paired rows 时结果依赖源 CSV 行顺序

**File:** `scripts/generate_trace_sl_ablation_evidence_contracts.py:232-237,359-363`

**Issue:** paired lookup 中重复键会被后者覆盖；layout row 使用 `selected.iloc[0]` 静默选第一行。若上游聚合产生重复行，生成 contract 会非确定性/顺序依赖。

**Fix:** 在构建前按 `(budget, layout_type)` 和 `(budget, baseline)` 检查唯一性；发现重复直接报错。

### WR-03: metadata `source_artifacts` 混入分号拼接的伪路径

**File:** `scripts/generate_trace_sl_ablation_evidence_contracts.py:618-623`

**Issue:** 生成的 JSON metadata 中包含类似 `gls_map_layout_summary.csv;gls_map_paired_delta_tests.csv` 的字符串。这不是实际文件路径，后续若按 artifact path 校验会失败，也削弱 provenance 可机器检查性。

**Fix:** 将 `source_artifacts` 规范化为真实路径列表；多来源行应拆成两个独立路径或使用 `source_artifacts: [ ... ]` 数组字段。
