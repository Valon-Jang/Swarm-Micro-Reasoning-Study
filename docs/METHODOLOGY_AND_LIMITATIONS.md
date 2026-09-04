# Methodology and limitations

## Experimental question

Does increasing the size of a topology-aware, neighbor-only swarm improve hard reasoning quality when every node has the same fixed deterministic capability?

## Topologies

Reference-1 and paired 2D/3D structures were tested up to:

- 10x10 grid: 100 nodes
- 10x10x10 cube: 1,000 nodes

Nodes know their coordinate, immediate neighbors, readout node, current round, total node count, and distance to readout. Nodes cannot read a shared blackboard.

## Benchmark

The final benchmark uses 25 calibrated tasks across five difficulty levels. Difficulty is calibrated against Reference-1 rather than assigned by label alone.

Reference calibration:

- L1: 100.00
- L2: 79.90
- L3: 65.00
- L4: 39.72
- L5: 24.16

Harder levels increasingly require combining distributed evidence and constructing causal links rather than merely finding keywords.

## Promotion gate

The topology-scaling hypothesis is considered promoted only if a topology produces at least a **+3 point improvement on the L3–L5 average** versus Reference-1 while keeping hard failures at zero.

No topology passed this gate.

## Safety and integrity gates

The study tracks:

- side-effect violations,
- hallucinated source references,
- illegal non-neighbor edges,
- prompt-injection obedience.

The final scale study kept these hard gates clean.

## Timing

The benchmark also records median artifact-generation/runtime cost. Timing repeats differ between retained 1–5 results and new 6–10 results, so timing should be interpreted as an engineering scale signal rather than a rigorous microbenchmark across machines.

## Important limitations

- No Qwen weights or other neural model are attached.
- The node is deterministic and heuristic-driven.
- There is a single readout node.
- The benchmark is synthetic and designed around evidence/reasoning tasks relevant to the kernel.
- Results should not be generalized to learned multi-agent systems without a separate experiment.
- The current package budget is <=10 MB by design, but the package does not intentionally fill the budget.
