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

## Broader research program
The broader question is whether very small reasoning units, when they know they are part of a larger collective and interact locally, can form system-level intelligence stronger than the individual unit.

The scale 1–10 experiment in this repository is only the first controlled baseline for that program. It deliberately removes or freezes many mechanisms that prior work suggests can matter: learned local update rules, semantic reasoning, heterogeneity, task-aware graph design, state-aware transmission, and persistent stigmergic environments.

## Research meaning of the current experiment
The scale 1–10 experiment measures whether connection topology and local message passing alone can improve a fixed deterministic node capability. It is a topology/system-intelligence baseline, not a general test of swarm intelligence and not a test of Qwen model scaling.

A future experiment that attaches an actual semantic/Qwen worker changes the independent variable and must be labeled separately. Subsequent controlled interventions should test local reasoning capability, node diversity, adaptive transmission, and persistent environment/memory one at a time.

See `RELATED_WORK.md` for the literature review and positioning.
