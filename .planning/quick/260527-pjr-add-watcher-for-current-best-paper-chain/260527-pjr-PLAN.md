---
quick_id: 260527-pjr
slug: add-watcher-for-current-best-paper-chain
status: completed
---

# Quick Task 260527-pjr: Add watcher for current best paper chain refresh

## Tasks

1. Add a watcher script that monitors Stage16 sweep completion progress and reruns the current-best paper-chain refresh whenever a new seed writes `metrics.csv`.
2. Make the watcher stop automatically once the expected number of Stage16 seed outputs is present.
3. Record the watcher entry point in `.planning/STATE.md`.
