# Scale-5 Pair Report v1.0

Benchmark basis: calibrated L1-L5 v0.9, unchanged cases/scoring/partitioning/engine. Added only `grid_5x5` and `cube_5x5x5`.

## Calibration (Reference-1)

- L1: 100.00
- L2: 79.90
- L3: 65.00
- L4: 39.72
- L5: 24.16

All five levels remain inside their target bands.

## Scale-5 results (7 timing repeats)

- grid_5x5: 25 nodes, avg quality 61.83, L3-L5 avg 43.08, L5 24.53, median 4.2128 ms, 160.9 avg messages, hard failures 0.
- cube_5x5x5: 125 nodes, avg quality 61.76, L3-L5 avg 42.96, L5 24.16, median 29.4964 ms, 903.8 avg messages, hard failures 0.
- Reference-1: avg quality 61.76, L3-L5 avg 42.96, L5 24.16, median 0.1331 ms.

## Interpretation

`grid_5x5` is the highest L3-L5 average in this deterministic benchmark (43.08), but the gain over Reference-1 is only +0.12 points and is not enough to establish scaling intelligence. The L5 gain is +0.37 points and comes from a trade-off: it improves `mixed_authority_ambiguity` while degrading `causal_chain_three_paths`.

`cube_5x5x5` exactly matches Reference-1 quality while costing about 221.6x the Reference median execution time and averaging 903.8 neighbor messages. It also roughly doubles messages versus cube_4x4x4 without a quality gain.

Maturity remains Level 4.5/10. Level 5 still requires a repeatable >=3 point L3-L5 gain over Reference with hard failures at zero.
