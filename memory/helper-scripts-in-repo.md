---
name: helper-scripts-in-repo
description: "Put monitoring/helper scripts in the project directory (git-tracked), never in the session scratchpad"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 9a35b5cc-468d-5a7c-a6d1-7e9df0a94d09
  modified: 2026-10-24T06:31:11.333Z
---

Write helper scripts (monitoring, wandb readers, VM checks, analysis) inside `/raid/wg25r/anti_design` (e.g. `tools/`) and commit them; do not use the session scratchpad.

**Why:** the user wants them tracked by git; on 2026-10-23 the scratchpad disappeared with a new session and all monitoring scripts were lost.

**How to apply:** create/edit under `/raid/wg25r/anti_design/tools/`, commit after each edit. Downloaded logs and images (wandb grids, run logs) also go inside the project directory and get committed (user override of the "don't commit bulk results" rule, 2026-10-23). Related: [[colab-kernel-state-over-local-pid]].
