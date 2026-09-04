# Fair Swarm Scaling Report v0.8

## Purpose

Re-check the previous v0.7/"5.5" work with a stricter, fairer benchmark and extend the scaling test through 4x4 and 4x4x4.

## Legacy audit findings

The previous benchmark was useful as a prototype but was not fully fair enough for scaling claims:

1. Mesh-only shard `notes` contained answer-direction hints (e.g. "preserve conflict", "avoid decoy"), while Reference-1 did not receive equivalent hints.
2. Reference-1 often received full noisy input while mesh nodes received already-cleaned shards, so input difficulty was asymmetric.
3. Different topology sizes were executed through different specialized functions; wall-clock speed was therefore not a strict same-engine comparison.
4. The old strict scorer gave zero recall credit when a case had no `required_paths`/`required_terms`, effectively creating an unintended penalty.
5. The old self-test could return PASS while the actual hardened level assessment still contained hard-gate failures.
6. Negative/quoted action wording (e.g. "do not delete") could be mistaken for an execution request.

v0.8 leaves legacy files intact as historical evidence and adds a new unified benchmark rather than rewriting the old reports.

## v0.8 fairness rules

- Same unified engine for all topologies.
- Every topology receives exactly the same total source atoms.
- Mesh input is a lossless partition of the same full input; no gold hints are injected.
- Only task/request/action fields can create mutation intent; source/log/policy mentions alone do not.
- Explicit read-only review overrides quoted/negative action words unless a separate explicit request/action field asks for the action.
- Same scoring function for every topology.
- Speed uses warmup + 7 repeated in-process runs with the same engine.
- Speed is reported, not used as an absolute machine-independent truth.

## Difficulty tiers

| Tier | Objective structure |
|---|---|
| L1 | One dominant signal; <=2 evidence sources; no meaningful noise/decoy |
| L2 | 2-3 sources; decoy path, negative action wording, stale PASS/current FAIL, or dead-end memory |
| L3 | Multi-source combination plus ~100-line noise, idempotency crash, multilingual injection, or policy precedence |
| L4 | ~500-line noise/60 decoy paths, quoted side-effect text, competing hypotheses, authority conflict, or 4-piece evidence chain |
| L5 | ~1200-line noise/120 decoy paths, outcome-unknown external effect, adversarial fake gold hint, 3-path chain, or mixed authority ambiguity |

Each tier contains 5 fixed cases (25 total).

## Tested structures

1. Reference-1 (1 node)
2. 2x2 (4 nodes)
3. 2x2x2 (8 nodes)
4. 3x3 (9 nodes)
5. 3x3x3 (27 nodes)
6. 4x4 (16 nodes)
7. 4x4x4 (64 nodes)

All mesh nodes use neighbor-only message passing. No shared blackboard is used. Each node receives topology metadata (dimensions, coordinate, neighbors, readout, distance, round).

## Final repeated result (7 repeats)

| Structure | Avg score | L1 | L2 | L3 | L4 | L5 | Avg messages | Median run ms | Avg compression |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Reference-1 | 92.46 | 91.67 | 95.78 | 95.83 | 92.84 | 86.19 | 0.00 | 0.1318 | 2.688 |
| 2x2 | 92.06 | 91.67 | 95.78 | 95.83 | 92.84 | 84.19 | 20.72 | 0.5089 | 2.871 |
| 2x2x2 | 92.06 | 91.67 | 95.78 | 95.83 | 92.84 | 84.19 | 48.64 | 0.9442 | 3.109 |
| 3x3 | 92.02 | 91.67 | 95.78 | 95.83 | 88.39 | 88.42 | 53.52 | 1.2835 | 2.936 |
| 3x3x3 | 91.61 | 91.67 | 95.78 | 95.83 | 88.34 | 86.42 | 196.92 | 3.8575 | 3.449 |
| 4x4 | 92.46 | 91.67 | 97.78 | 95.83 | 92.84 | 84.19 | 97.16 | 2.1275 | 3.034 |
| 4x4x4 | 92.44 | 91.67 | 95.78 | 95.74 | 92.84 | 86.16 | 466.28 | 12.4390 | 4.132 |

All variants: 0 illegal edges, 0 source-ref violations, 0 side-effect execution violations in the new harness.

## Interpretation

- Current deterministic swarm does **not** show a reliable quality scaling gain over Reference-1.
- 4x4 reaches the same overall score as Reference-1, but at much higher message/runtime cost.
- 4x4x4 is the strongest non-reference topology on the combined L3-L5 slice, but it still does not beat Reference-1 materially and costs ~94x Reference median runtime in this local benchmark.
- Score differences of 1-2 points are often caused by which evidence reaches readout first after deterministic partition/routing; they are not proof of emergent intelligence.
- Larger structures currently add transport/cross-check capacity, not new reasoning capability. To test the user's emergence hypothesis, the next meaningful change is to give each node a genuinely local reasoning/update function (or small Qwen worker) while preserving the same fair benchmark.

## Current maturity assessment

**4.5 / 10**

Reason: the scaffold now has a fair multi-level benchmark, topology awareness, lossless partitioning, 4x4/4x4x4 scaling, hard safety gates, and standardized speed measurement. It does not reach Level 5 because scaling has not produced a repeatable quality gain over Reference-1 on harder levels.
