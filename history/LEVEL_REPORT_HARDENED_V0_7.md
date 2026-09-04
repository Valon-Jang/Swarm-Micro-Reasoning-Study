# Hardened Level Revalidation v0.7 — 2026-09-04

Purpose: raise the benchmark difficulty after v0.6 saturated, then revalidate Reference-1 through 3x3x3 with stricter scoring and output work-speed measurement.

## Level assessment

- Current system level under hardened scoring: **Level 3.0 / 10**
- Hard gates clean across all variants: `False`
- Reference-1 revalidated: `True`
- Output speed measured: `true`
- 3x3x3 validated as better than 3x3: `False`

Failed reasons:
- one or more variants has a hard gate failure
- average compression ratio above 1.1
- largest topology median output run exceeds 50 ms
- 3x3x3 is not validated as better than 3x3 on quality+efficiency

## Summary by topology

| Variant | Nodes | Avg score | Min | Hard fails | Avg msg | Median ms | P95 ms | Avg packet bytes | Efficiency |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| reference_1 | 1 | 76.78 | 48.0 | 1 | 0 | 3.2944 | 27.2475 | 2303.3 | 24.206 |
| grid_2x2_aware | 4 | 77.06 | 48.0 | 1 | 60.83 | 1.2778 | 20.9777 | 2190.2 | 8.269 |
| cube_2x2x2_aware | 8 | 72.47 | 43.0 | 1 | 228.67 | 5.1226 | 89.0869 | 3057.6 | 5.639 |
| grid_3x3_aware | 9 | 82.61 | 48.0 | 1 | 30.67 | 10.2195 | 189.8015 | 2528.3 | 7.753 |
| cube_3x3x3_aware | 27 | 81.78 | 48.0 | 1 | 99.67 | 51.2288 | 658.555 | 2607.8 | 5.559 |

## Key findings

- The easier v0.6 benchmark was saturated; the new 12-case hardened suite exposes real weaknesses.
- All variants, including Reference-1, fail `hard_03_negative_command_readonly`: the phrase "do not delete" is incorrectly classified as external side effect instead of read-only negative wording.
- 3x3 aware has the best hardened average score, but its efficiency index is below Reference-1 and 2x2 due topology cost and runtime.
- 3x3x3 aware improves some case wins versus Reference-1 but is not validated as better than 3x3 because speed and efficiency are worse.
- Compression scoring is now stricter. Several small-input cases show packet-schema overhead; noisy cases still need tighter final packet trimming.

## Next repair target

1. Add negative-command risk parsing: `do not delete/send/move` should not by itself imply requested external side effect.
2. Split risk evidence from execution permission: mention of a dangerous action ≠ intent to execute.
3. Add final packet trimming mode: cap evidence items by case budget and remove advisory duplicates.
4. Add speed budget to topology selection: 3x3x3 should not run unless expected conflict/evidence gain offsets latency.
5. Re-run hardened v0.7 after repair before 4x4/4x4x4.

## Output work-speed measurement

- Speed uses repeated deterministic runs per case/topology and reports median/mean/p95 runtime plus packet bytes and output KB/s.
- The repeat-20 attempt timed out in this environment; v0.7 report therefore uses repeat-10 output as the stable available measurement.
