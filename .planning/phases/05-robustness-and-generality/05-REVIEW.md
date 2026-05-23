---
phase: 05-robustness-and-generality
reviewed_at: 2026-05-23T03:50:02Z
status: pass
counts:
  critical: 0
  warning: 0
  info: 0
  total: 0
---

# Phase 05 Robustness and Generality Final Re-Review

复审范围：验证最新提交 `8539753 fix(05): restrict candidate caveat scope` 是否关闭上一轮剩余 ROBUST-06 caveat 作用域问题，并简要复查 candidate launcher 的 stale seed 汇总风险。未修改源码；仅更新本报告。

本轮轻量验证已运行：

- `python -m py_compile .planning/phases/05-robustness-and-generality/validate_phase5_robustness.py .planning/phases/05-robustness-and-generality/test_validate_phase5_robustness.py` 通过。
- `python .planning/phases/05-robustness-and-generality/test_validate_phase5_robustness.py` 通过（10 tests）。
- `python .planning/phases/05-robustness-and-generality/validate_phase5_robustness.py --project-root /home/samuel/projects/sensor_opt` 对当前真实 artifacts 返回 ROBUST-01..06 PASS。
- 额外临时负例：valid candidate-count caveat + raw dataset doc offender 仍返回 nonzero，并报告 `curated evidence docs reference raw dataset paths`。
- `DRY_RUN=1 SEEDS="25 26" CANDIDATE_COUNTS="50 100" PYTHON_BIN=python bash scripts/run_stage14_candidate_sensitivity_pems7_228.sh` 确认 per-count summary 与 top-level summary 均显式传本次 seed dirs。
- 复查 `scripts/run_stage14_candidate_sensitivity_pems7_228.sh`：已使用 `count_seed_dirs` / `completed_input_roots` 传入 summarizer，未再依赖 candidate root 下的 `seed_*` glob；stale seed warning 可关闭。

## Resolved Findings

### CR-01 / ROBUST-06 caveat scope: resolved

`.planning/phases/05-robustness-and-generality/validate_phase5_robustness.py` 现在将 `candidate_counts(...)` 的 candidate-count coverage gaps 作为结构化 `coverage_errors` 返回，只有这些 missing candidate counts coverage gaps 会进入 caveat 匹配逻辑。schema/semantic errors 仍通过 `context.fail(...)` 保留，不会被 valid caveat 清除。

已验证 caveat 不能覆盖以下非 coverage 错误：

- missing core candidate artifact：`test_valid_candidate_count_caveat_does_not_hide_missing_core_artifact` 覆盖，测试通过。
- missing `runtime_seconds` schema：`test_valid_candidate_count_caveat_does_not_hide_runtime_schema_error` 覆盖，测试通过。
- `combined_metrics.csv` 无 `method == gls_map` candidate rows：`test_valid_candidate_count_caveat_does_not_hide_missing_gls_rows` 覆盖，测试通过。
- raw-data hygiene：临时合成负例验证 valid caveat 存在时仍 FAIL。

### Candidate launcher stale seed warning: resolved

`scripts/run_stage14_candidate_sensitivity_pems7_228.sh` 的 summary 调用现在只传入本轮构造的 seed 目录：

- per-count summary 使用 `--input-root "${count_seed_dirs[@]}"`。
- top-level summary 使用 `--input-root "${completed_input_roots[@]}"`。

DRY_RUN 输出确认不会把 `candidates_<count>` 根目录交给 summarizer 去 glob 历史 `seed_*`，因此 stale seed contamination 风险已关闭。

## Remaining Findings

None.
