# Why topology scaling failed to create emergent reasoning

## Short answer

The experiment scaled **connectivity**, not **reasoning capability**.

The tested node could extract, label, retain, route, and weakly reconcile evidence, but it could not reliably create new semantic or causal relations. Adding more copies of that same node increased propagation paths and message volume without adding a new transformation that could solve the calibrated L3–L5 reasoning requirements.

This is a negative result for the current deterministic node class, not a negative result for Qwen or LLM swarms in general.

## What "failure" means here

The system did not crash and the safety/edge/source gates stayed clean. The **research hypothesis failed its promotion gate**:

> Scaling topology alone should produce a meaningful improvement on hard reasoning tasks.

The predefined promotion threshold was a **>= 3 point gain on the L3–L5 average over Reference-1**. No tested topology from 2x2 through 10x10x10 reached it.

Reference-1 L3–L5: **42.96**  
Best observed L3–L5: **43.08** at 5x5  
Gain: **+0.12**

The best L5 result was 25.35 at 9x9 versus 24.16 for Reference-1, a **+1.19** gain. This was small, inconsistent across task types, and below the promotion threshold.

## Main causes

### 1. Capability ceiling of the node

Each node is a deterministic evidence processor. Its useful operations are mostly:

- regex/heuristic evidence extraction,
- fixed risk classification,
- simple pass/fail conflict detection,
- source-reference preservation,
- bounded local state,
- neighbor-only routing.

The harder benchmark levels require construction of causal relations such as "A created B, B interacted with C, therefore D is the root cause." That relation is not present in the node's primitive operations unless a heuristic already encodes it.

More nodes therefore replicate the same ceiling.

### 2. Scaling increased transport, not transformation

Topology growth adds paths over which signals can move. It does not automatically add a new operation over those signals.

A useful mental model is:

> more couriers != a better scientist

The mesh became better at moving evidence around, but not substantially better at inventing or validating new causal structure.

### 3. Redundancy saturation

As the number of nodes increased, many nodes rediscovered or forwarded the same high-value signals. The system accumulated communication redundancy faster than novel information.

This is visible in the 10x10x10 result:

- nodes: **1,000**
- average messages: **6,813.6**
- L3–L5: **42.69**
- Reference-1 L3–L5: **42.96**

The mesh did far more work without producing more useful hard-task reasoning.

### 4. Single-readout bottleneck

Only one far-corner readout node emits the final packet. This is useful for a controlled experiment, but it means the system ultimately funnels distributed evidence through one final bounded synthesis point.

If upstream nodes cannot create better abstractions, the readout receives more evidence but not necessarily better intermediate concepts.

### 5. Bounded routing protects efficiency but can discard weak signals

Topology-aware routing and the per-node signal budget prevent uncontrolled flooding. This was necessary: earlier cube experiments showed severe message explosion.

However, aggressive selection means weak but jointly important signals can be lost before they meet another shard that would make them meaningful. Relaxing the limit produces more flooding; tightening it increases information loss. Without stronger local reasoning, topology alone cannot escape this trade-off.

### 6. 3D scaling was especially expensive

Cube topologies created much more communication work without a consistent quality gain.

Reference-1 median runtime: **0.1366 ms**  
10x10x10 median runtime: **605.389 ms**  
Runtime ratio: approximately **4,432x**

Yet hard-task quality slightly decreased.

### 7. No learning or adaptive specialization

The current experiment intentionally excludes:

- learned semantic reasoning,
- neural inference,
- persistent pheromone scores,
- online learning,
- persistent dead-end memory across runs,
- adaptive role formation.

Therefore the network cannot learn that a particular path, node, or reasoning style is repeatedly useful. Every run starts from essentially the same deterministic capability.

### 8. Early apparent gains were partly benchmark artifacts

Earlier prototypes contained evaluation problems that were corrected before the final scale study:

- some mesh shards contained answer-direction hints,
- Reference and mesh sometimes received differently shaped input,
- topology variants used different execution paths for timing,
- some scoring dimensions penalized cases where that dimension was not required,
- negative commands such as "do not delete" could be mistaken for execution intent.

After a fair, shared benchmark and calibrated L1–L5 scoring were introduced, most apparent scaling gains disappeared. This increased confidence in the final negative result.

## What the result does support

The experiment does support several narrower conclusions:

1. Neighbor-only topology can be implemented safely and deterministically from 1 to 1,000 nodes.
2. Topology awareness can reduce message flooding versus topology-blind routing.
3. Some 2D sizes show weak task-specific specialization signals.
4. Those gains are not yet large or stable enough to count as emergent reasoning.
5. The next independent variable should be **node capability**, not node count.

## Next experiment

Keep the same calibrated benchmark and scaling harness, but replace or augment the deterministic node with a very small semantic worker, for example a constrained Qwen worker used only for:

- causal-link proposal,
- contradiction interpretation,
- hypothesis compression,
- ranking of competing explanations.

Then rerun the same scale curve. If the L3–L5 curve changes with topology only after semantic node capability is introduced, that would isolate a more interesting interaction between local reasoning and swarm structure.
