# Current 10MB-Budget Qwen/Swarm Definition

## Name
10MB-budget deterministic swarm micro-reasoning kernel.

## What it is
A dependency-light system-intelligence scaffold intended to sit before or around a future Qwen worker. The design budget is <=10 MB; the current package is substantially smaller.

## What it is NOT
- Not a 10 MB Qwen neural model.
- No Qwen/model weights are attached.
- No learned parameters are being evaluated.
- No semantic LLM generation is occurring inside nodes.

## Current node capability
- Regex/heuristic extraction of errors, paths, pass/fail, injection-like text, dead-end, duplicate/idempotency and authority signals.
- Fixed read-only/file-write/external-side-effect/unknown risk classification.
- Simple local conflict derivation when success/support and failure/unsupported evidence coexist.
- Per-node evidence store for the current run.
- Topology awareness from explicit node_card: coordinate, neighbors, readout, distance, round, total nodes.
- Neighbor-only message passing; no node-readable shared blackboard.
- Fixed routing toward readout; selected critical signal classes may use one lateral cross-check neighbor.
- Per-node selection budget: 4 signals per round.
- One far-corner readout node emits the final source-backed evidence packet.

## Absent capabilities
- Learned semantic reasoning.
- Neural inference / hidden states / token generation.
- Training or online learning.
- Persistent pheromone score.
- Persistent dead-end memory across benchmark runs.
- Autonomous tool execution.

## Research meaning
The scale 1–10 experiment measures whether connection topology and local message passing alone can improve this fixed deterministic node capability. It is a topology/system-intelligence baseline. A future experiment that attaches an actual Qwen worker changes the independent variable and must be labeled separately.
