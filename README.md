# Swarm Micro-Reasoning Scaling Study

A controlled scaling study of a **Qwen-ready, <=10 MB-budget deterministic swarm micro-reasoning kernel** using neighbor-only message passing from **1 node to 1,000 nodes**.

## Result in one sentence

**Topology scaling alone did not produce emergent reasoning at the tested node capability.**

The best hard-task gain over the single-node reference was too small to pass the predefined promotion gate, while runtime and message cost increased sharply.

## Important terminology

This repository does **not** contain a 10 MB Qwen model.

The tested system is a deterministic system-intelligence scaffold intended to host or surround a future small Qwen worker. There are no Qwen weights, learned parameters, hidden-state inference, or LLM token generation in the current experiment.

See [`docs/EXPERIMENT_DEFINITION.md`](docs/EXPERIMENT_DEFINITION.md).

## Broader research program

The larger question is not merely whether a particular grid topology works. It is:

> Can very small reasoning units, each aware that it is part of a larger collective and restricted to local interaction, form system-level intelligence that is meaningfully stronger than the individual unit?

This repository records the **first baseline** for that broader program. Local node capability was intentionally held almost fixed and weak so that topology scale could be isolated as the primary independent variable.

## Research question for this baseline

> If many weak nodes know their position in a mesh and can exchange evidence only with adjacent nodes, does reasoning quality emerge from topology scale alone?

Tested structures included Reference-1, square grids, and 3D cubes up to `10x10x10`.

## Research context

This question has substantial prior lineage in cellular automata, swarm/collective intelligence, LLM multi-agent scaling, and communication-topology research. The present study does **not** claim to invent swarm intelligence or agent topology. Its narrower contribution is a mechanistic topology-only baseline: fixed weak local processors were scaled from one node to 1,000 while quality, communication cost, and runtime were measured together.

The literature reviewed for this project suggests that useful collective gains often depend on variables deliberately absent from this first baseline: evolved or learned local update rules, semantic node reasoning, heterogeneous agents, task-aware topology, state-aware transmission, or persistent stigmergic environments.

See [`docs/RELATED_WORK.md`](docs/RELATED_WORK.md) for the detailed literature review and positioning.

## Headline results

| Topology | Nodes | Overall | L3-L5 | L5 | Median ms | Avg messages |
|---|---:|---:|---:|---:|---:|---:|
| Reference-1 | 1 | 61.76 | 42.96 | 24.16 | 0.1366 | 0.0 |
| 5x5 grid | 25 | 61.83 | **43.08** | 24.53 | 4.2128 | 160.9 |
| 9x9 grid | 81 | 61.53 | 42.58 | **25.35** | 21.5805 | 532.8 |
| 10x10x10 cube | 1,000 | 61.59 | 42.69 | 23.34 | 605.3890 | 6,813.6 |

Promotion gate: **>= +3 points on L3-L5 vs Reference-1, with zero hard failures.**

Best observed L3-L5 gain: **+0.12**. The hypothesis did not pass.

## Why it failed

The current node can move and label evidence, but it has little ability to create new semantic or causal relations. Scaling therefore increased **transport capacity** much more than **transformation capacity**.

At 1,000 nodes, the system was about **4,432x slower** than Reference-1 while hard-task quality was slightly lower.

The full analysis is in [`docs/WHY_SCALING_FAILED.md`](docs/WHY_SCALING_FAILED.md).

## What was learned

- Neighbor-only message passing remained structurally safe through 1,000 nodes.
- Topology awareness helped control message flooding.
- 2D grids showed small, inconsistent specialization signals.
- 3D cubes were much more expensive and did not consistently improve quality.
- Adding more copies of the same deterministic evidence processor does not create a new causal-reasoning primitive.
- The next useful independent variable is **local node reasoning capability**, not more nodes.

## Repository map

```text
README.md
├─ docs/
│  ├─ EXPERIMENT_DEFINITION.md
│  ├─ RELATED_WORK.md
│  ├─ RESULTS_SCALE_1_10.md
│  ├─ WHY_SCALING_FAILED.md
│  └─ METHODOLOGY_AND_LIMITATIONS.md
├─ src/
│  ├─ swarm_mesh_kernel.py
│  ├─ swarm_fair_scale_v0_8.py
│  ├─ swarm_calibrated_L1_L5_v0_9.py
│  ├─ swarm_scale_5_v1_0.py
│  └─ swarm_scale_6_10_targeted_v1_1.py
├─ results/
│  └─ scale1_10_research_snapshot_v1_1.json
├─ schemas/
├─ fuel/
└─ history/
```

## Reproduce

Python 3.12+ is recommended. The deterministic baseline has no third-party runtime dependency.

```bash
python src/swarm_mesh_kernel.py --self-test
python src/swarm_calibrated_L1_L5_v0_9.py --help
python src/swarm_scale_6_10_targeted_v1_1.py --help
```

The exact final scale snapshot is retained under `results/`.

## Research boundary

This result should **not** be interpreted as evidence that Qwen or LLM swarms cannot benefit from scale. A real semantic/Qwen worker changes the independent variable and requires a separate benchmark run.
