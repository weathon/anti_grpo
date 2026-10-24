---
name: colab-kernel-state-over-local-pid
description: "When monitoring Colab runs launched via `colab exec`, judge run status by the VM kernel's real execution_state, not by the local process"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 633c3b2a-955b-59f2-a8f0-e17a02d84f5f
  modified: 2026-10-23T07:35:57.670Z
---

When monitoring a Colab run started with a backgrounded local `colab exec`, decide whether the run is alive / finished by the kernel's actual execution_state from the Jupyter API (`/api/kernels` on the session URL with the runtime proxy token), not by whether the local `colab exec` PID is still alive and not by `colab status`.

**Why:** On 2026-10-23 the neutral VM's setup finished at 00:21 (kernel idle, 0 connections) while the local `colab exec` client had lost its websocket and kept hanging, with its log frozen mid-install; it looked stuck for 12+ minutes. Separately, `colab status` reported IDLE while the kernel was actually busy training.

**How to apply:** In every monitoring check (and in cron prompts), query the kernel's execution_state directly; treat "local PID alive" and "local log progress" as unreliable. A dead local PID with a busy kernel means only the local connection dropped (do not restart); a live local PID with an idle kernel means the cell already finished or failed (inspect the kernel). Related: [[colab-cli-workflow]].
