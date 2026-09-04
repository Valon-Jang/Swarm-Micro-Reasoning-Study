# Calibrated L1-L5 + Scale-to-4 Report v0.9

## Difficulty calibration (Reference-1)

| Level | Target | Reference score | Pass |
|---|---:|---:|---|
| L1 | 90-100 | 100.00 | PASS |
| L2 | 70-85 | 79.90 | PASS |
| L3 | 50-65 | 65.00 | PASS |
| L4 | 30-45 | 39.72 | PASS |
| L5 | 10-30 | 24.16 | PASS |

## Topology results

| Topology | Nodes | Avg quality | L3-L5 avg | Median output ms | Avg messages | Hard failures |
|---|---:|---:|---:|---:|---:|---:|
| reference_1 | 1 | 61.76 | 42.96 | 0.1333 | 0.0 | 0 |
| grid_2x2 | 4 | 61.43 | 42.41 | 0.5141 | 20.7 | 0 |
| cube_2x2x2 | 8 | 61.43 | 42.41 | 0.9476 | 48.6 | 0 |
| grid_3x3 | 9 | 61.67 | 42.81 | 1.3012 | 53.5 | 0 |
| cube_3x3x3 | 27 | 61.34 | 42.26 | 3.8580 | 196.9 | 0 |
| grid_4x4 | 16 | 61.94 | 42.41 | 2.4066 | 97.2 | 0 |
| cube_4x4x4 | 64 | 61.76 | 42.96 | 12.6351 | 466.3 | 0 |

## Difficulty x topology

| Topology | L1 | L2 | L3 | L4 | L5 |
|---|---:|---:|---:|---:|---:|
| reference_1 | 100.00 | 79.90 | 65.00 | 39.72 | 24.16 |
| grid_2x2 | 100.00 | 79.90 | 65.00 | 39.72 | 22.52 |
| cube_2x2x2 | 100.00 | 79.90 | 65.00 | 39.72 | 22.52 |
| grid_3x3 | 100.00 | 79.90 | 65.00 | 38.45 | 24.99 |
| cube_3x3x3 | 100.00 | 79.90 | 65.00 | 38.45 | 23.34 |
| grid_4x4 | 100.00 | 82.45 | 65.00 | 39.72 | 22.52 |
| cube_4x4x4 | 100.00 | 79.90 | 65.00 | 39.72 | 24.16 |

## Interpretation

- Difficulty calibration succeeded: Reference-1 falls from 100.00 at L1 to 24.16 at L5.
- No topology shows a material repeatable quality gain over Reference-1 on L3-L5.
- grid_3x3 has the highest L5 score (24.99), only +0.83 over Reference-1.
- grid_4x4 improves L2 to 82.45 but loses on one adversarial L5 case.
- cube_4x4x4 matches Reference-1 hard-level quality while requiring much more runtime/messages.
- Hard safety failures are 0 across all evaluated topologies.
- Current deterministic nodes are evidence routers, not independent reasoners; scaling alone does not create new causal inference.

## Speed note

Runtime is end-to-end packet production time for the same unified engine. Each case/topology was warmed up and measured 7 times. Median values are used for the main table; p95 remains sensitive to long-noise cases.
