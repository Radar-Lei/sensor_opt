---
status: in_progress
created: 2026-05-18
---

实现 TRACE-SL 首轮 CPU pilot。

步骤：
1. 复用 TRC-23-02333 的 PeMS7_228 数据格式，避免修改 CDSTE/DDP 主训练路径。
2. 新增独立脚本评估 historical mean、neighbor average、GSP、GLS 四类透明估计器。
3. 支持 budgets、layout seeds、ridge/lambda 等 CLI 参数，输出 JSON 与 CSV。
4. 先跑小规模 sanity，再跑首轮随机布局 pilot。
5. 写 SUMMARY.md 记录结果、产物和下一步。
