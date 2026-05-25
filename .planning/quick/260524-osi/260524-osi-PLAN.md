---
quick_id: 260524-osi
status: complete
---

# Quick Task 260524-osi Plan

将 Stage12 启动脚本改为受控 seed 级并行，使用 MAX_JOBS 限制每个数据集并发数，保持 THREADS_PER_JOB=1，并继续为每个 seed 写入独立输出目录和独立日志，全部 seed 完成后再统一 summarize，避免资源互抢和输出污染。
