# Swarm Scale 1–10 Research Snapshot v1.1

## Critical definition

The tested system is **not a 10 MB Qwen model**. It is a deterministic swarm micro-reasoning kernel kept under a 10 MB design budget. No Qwen weights or learned neural model are attached. Therefore these results measure topology/routing effects on rule-based evidence processors, not Qwen language-model intelligence.

Current node capability: regex/heuristic evidence extraction, fixed risk classification, simple local pass-vs-failure conflict derivation, source-ref preservation, topology-aware neighbor routing, and a single readout packet. There is no learned semantic generation, training, pheromone learning, or persistent inter-run memory.

## Difficulty calibration (Reference-1)

| Level | Score |
|---|---:|
| L1 | 100.00 |
| L2 | 79.90 |
| L3 | 65.00 |
| L4 | 39.72 |
| L5 | 24.16 |

## Scale results

| Topology | Nodes | Overall | L3–L5 | L5 | Median ms | Avg messages | Hard fail |
|---|---:|---:|---:|---:|---:|---:|---:|
| reference_1 | 1 | 61.76 | 42.96 | 24.16 | 0.1366 | 0.0 | 0 |
| grid_2x2 | 4 | 61.43 | 42.41 | 22.52 | 0.4988 | 20.7 | 0 |
| cube_2x2x2 | 8 | 61.43 | 42.41 | 22.52 | 0.9578 | 48.6 | 0 |
| grid_3x3 | 9 | 61.67 | 42.81 | 24.99 | 1.2741 | 53.5 | 0 |
| cube_3x3x3 | 27 | 61.34 | 42.26 | 23.34 | 3.8310 | 196.9 | 0 |
| grid_4x4 | 16 | 61.94 | 42.41 | 22.52 | 2.1044 | 97.2 | 0 |
| cube_4x4x4 | 64 | 61.76 | 42.96 | 24.16 | 12.7042 | 466.3 | 0 |
| grid_5x5 | 25 | 61.83 | 43.08 | 24.53 | 4.2128 | 160.9 | 0 |
| cube_5x5x5 | 125 | 61.76 | 42.96 | 24.16 | 29.4964 | 903.8 | 0 |
| grid_6x6 | 36 | 61.76 | 42.96 | 24.16 | 7.4086 | 239.1 | 0 |
| cube_6x6x6 | 216 | 61.73 | 42.06 | 22.52 | 72.8409 | 1607.3 | 0 |
| grid_7x7 | 49 | 61.38 | 42.33 | 23.34 | 9.6804 | 317.2 | 0 |
| cube_7x7x7 | 343 | 61.59 | 42.69 | 23.34 | 133.2761 | 2473.8 | 0 |
| grid_8x8 | 64 | 61.50 | 42.53 | 22.88 | 16.3151 | 421.6 | 0 |
| cube_8x8x8 | 512 | 61.66 | 42.81 | 23.71 | 251.9902 | 3952.8 | 0 |
| grid_9x9 | 81 | 61.53 | 42.58 | 25.35 | 21.5805 | 532.8 | 0 |
| cube_9x9x9 | 729 | 61.45 | 42.46 | 23.71 | 430.5670 | 5189.4 | 0 |
| grid_10x10 | 100 | 61.03 | 41.76 | 22.88 | 28.7639 | 630.0 | 0 |
| cube_10x10x10 | 1000 | 61.59 | 42.69 | 23.34 | 605.3890 | 6813.6 | 0 |

## Findings

- Best overall score: `grid_4x4`.
- Best L3–L5 average: `grid_5x5`.
- Best L5 score: `grid_9x9` = 25.35; Reference-1 = 24.16.
- 10x10x10: overall 61.59, hard L3–L5 42.69, L5 23.34, median 605.389 ms, messages 6813.6.
- 10x10x10 median runtime / Reference-1 = 4431.8x.
- 10x10x10 node count / 5x5x5 = 8.0x; median runtime ratio = 20.5x; message ratio = 7.5x.
- All tested structures kept hard safety/edge/source gates clean.
- No topology through 10x10x10 produced the >=3 point L3–L5 gain required for Level 5 maturity.
- Current evidence therefore does not support emergent reasoning from topology scaling alone at this node capability.

## Interpretation boundary

This does **not** show that a Qwen swarm cannot improve with scale. It shows that increasing the number of the current deterministic nodes does not create new causal reasoning. The current node can mostly extract, route, retain, and weakly reconcile evidence; it cannot generate the calibrated causal-link relations required by L3–L5 except where fixed heuristics already encode them. A real small Qwen/LLM worker would be a different experimental condition and must be benchmarked separately.

## Measurement notes

- Same 25 calibrated L1–L5 cases and same scoring/routing contract were retained.
- Structures 2–5 use the retained v1.0 7-repeat timing result; structures 6–10 use the new v1.1 3-repeat timing result. Quality scores are deterministic under the current engine; timing repeat count affects speed stability only.
- The initial monolithic scale-1–10 run exceeded a 120-second execution limit. The 6–10 run was therefore isolated without changing benchmark semantics; the 3-repeat 6–10 benchmark completed in 162.45 seconds wall time.
