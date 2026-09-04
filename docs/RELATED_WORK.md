# Related Work and Research Positioning

Reviewed: 2026-09-04.

## Broader research question

The broader research program behind this repository asks:

> Can very small reasoning units, each aware that it is part of a larger collective and restricted to local interaction, form system-level intelligence that is meaningfully stronger than the individual unit?

The experiment in this repository is only the first baseline for that larger question. It intentionally fixes local node capability and scales topology from one node to 1,000 nodes. This isolates a narrow variable:

> Does connection topology and local message passing alone create a new reasoning capability when the underlying node capability is held fixed?

The answer in this baseline was negative. That result should not be generalized to learned, heterogeneous, adaptive, stigmergic, or semantically capable swarms.

## 1. Classical lineage: local interaction to global computation

### Mitchell, Crutchfield, and Hraber (1994) — Evolving cellular automata to perform computations

This work used a genetic algorithm to evolve local cellular-automaton rules for a global density-classification task. It is a direct conceptual ancestor of the question studied here: simple units with local interaction can participate in global computation.

Critical difference from this repository: the cellular-automaton rule itself was evolved. In our first baseline, local node capability and routing behavior were mostly fixed while only the number and geometry of connected nodes were scaled.

Primary source: https://doi.org/10.1016/0167-2789(94)90293-3

## 2. LLM multi-agent scaling: positive evidence and saturation

### Li et al. (2024) — More Agents Is All You Need

The Agent Forest study reported that repeated LLM sampling plus voting can improve performance as the number of instantiated agents increases. This is an important positive scaling result, but its mechanism differs from our local-mesh experiment: independent model samples provide additional answer diversity and voting aggregates them.

Source: https://arxiv.org/abs/2402.05120

### Yang et al. (2026) — Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity

This work reports strong diminishing returns when homogeneous agents are scaled, while heterogeneous agents provide complementary information channels and continue to improve performance. The authors introduce an effective-channel view of agent scaling and report that two diverse agents can match or exceed sixteen homogeneous agents in tested settings.

This is highly consistent with our negative topology-only baseline: nominal node count can rise while effective information diversity remains nearly unchanged.

Source: https://arxiv.org/abs/2602.03794

### Bertalanič and Fortuna (2026) — The Ringelmann Effect in Multi-Agent LLM Systems

This preprint studies effective team size rather than nominal agent count. Across the reported configurations, homogeneous multi-agent scaling frequently approaches a structural ceiling; one reported case finds thirty dense debating agents producing no more answer diversity than one agent on MMLU-Hard. Heterogeneous architecture is identified as the tested intervention that can escape this ceiling.

Source: https://arxiv.org/abs/2606.02646

### Kim et al. (2026) — Capable language models can outgrow the benefits of collaboration

A controlled Nature Machine Intelligence study evaluates 260 multi-agent configurations and finds that collaboration can help or hurt depending on task and architecture. Multi-agent coordination is therefore not a monotonic scaling law in which more agents necessarily imply better reasoning.

Source: https://doi.org/10.1038/s42256-026-01268-y

## 3. Communication topology as a design variable

### Li et al. (2024) — Improving Multi-Agent Debate with Sparse Communication Topology

This study systematically varies communication connectivity in GPT- and Mistral-based debate systems. Sparse communication can match or outperform dense all-to-all debate while reducing computational cost.

This directly supports treating topology as an experimental variable rather than assuming full connectivity is optimal.

Source: https://aclanthology.org/2024.findings-emnlp.427/

### Zhuge et al. (2024) — GPTSwarm: Language Agents as Optimizable Graphs

GPTSwarm represents agent systems as computational graphs whose nodes perform operations or query LLMs and whose edges define information flow. Both node prompts and edge connectivity can be optimized.

The important contrast is that GPTSwarm changes node behavior and graph structure, whereas our first baseline deliberately holds node capability fixed to isolate topology scaling.

Source: https://proceedings.mlr.press/v235/zhuge24a.html

### Zhang et al. (2025) — G-Designer

G-Designer dynamically constructs task-aware multi-agent communication topologies using a graph-based learned design mechanism. It reports improved task performance and large communication-token reductions on some benchmarks.

This supports a key distinction exposed by our experiment: a fixed geometric mesh is not equivalent to a task-adaptive communication graph.

Source: https://proceedings.mlr.press/v267/zhang25cu.html

### Shen et al. (2025) — Understanding the Information Propagation Effects of Communication Topologies in LLM-based Multi-Agent Systems

This work studies how correct and incorrect agent outputs propagate under different topology densities. The reported result is that moderately sparse structures can balance beneficial information diffusion against error propagation better than either extreme.

This is closely related to the message-flooding and signal-loss effects observed while scaling our 2D and 3D meshes.

Source: https://aclanthology.org/2025.emnlp-main.623/

## 4. Beyond topology: state-aware transmission and stigmergy

### Colas et al. (2026) — Discovering Adaptive Transmission Programs for Collective Innovation

This work argues that network topology is state-agnostic: knowing who is connected to whom does not determine what should be transmitted given what agents currently know. The authors evolve state-aware transmission programs and report gains over standard baselines; removing content dependence while preserving topology and timing removes the gains.

This is particularly relevant to the next phase of this project. Our first baseline used mostly fixed routing. A future swarm should condition transmission on local evidence, uncertainty, conflict state, novelty, and the receiving node's role or knowledge.

Source: https://arxiv.org/abs/2608.24545

### Pal, Wang, and Buehler (2026) — SwarmWorld

SwarmWorld studies initially homogeneous language-model agents that self-organize in a shared spatial environment without predefined roles or a central coordinator. Persistent artifacts and environmental interaction create a stigmergic coordination channel, and roles such as exploration, construction, maintenance, and coordination emerge over time.

This is closer to the broader motivation of this project than the current deterministic baseline because the collective can alter and reuse a persistent environment rather than only forward fixed-schema messages.

Source: https://arxiv.org/abs/2608.26081

## 5. Position of this repository

The ideas of collective intelligence, local interaction, agent graphs, sparse topology, and multi-agent scaling all have substantial prior work. This repository should therefore not be presented as introducing swarm intelligence or multi-agent topology as a new concept.

Among the works reviewed above, however, we did not find an exact match for the following experimental combination:

- extremely weak deterministic micro-nodes rather than full LLM agents;
- explicit topology awareness at every node;
- no node-readable central blackboard;
- neighbor-only local communication;
- regular 2D grid and 3D cube geometries;
- fixed node capability while topology scale is the primary independent variable;
- systematic scaling from one node to 1,000 nodes;
- simultaneous measurement of reasoning quality, message volume, and runtime;
- an explicit test of whether topology scale alone can create a new reasoning capability.

This claim is intentionally narrow: it describes the literature reviewed for this repository as of 2026-09-04, not an exhaustive proof of novelty.

A suitable positioning is:

> A mechanistic topology-only baseline connecting classical emergent computation with modern multi-agent reasoning research.

## 6. Interpretation of the negative result in light of prior work

The observed failure to obtain a meaningful reasoning gain from 1 -> 1,000 fixed nodes is compatible with the broader literature rather than contradictory to it.

The common pattern is:

1. **Agent count alone is weak.** Homogeneous agents can saturate because they add correlated rather than complementary information.
2. **Topology matters but is not sufficient.** Sparse or task-aware graphs can improve information flow and efficiency, but fixed connectivity does not create new semantic operations by itself.
3. **Local transformation capability matters.** Classical cellular automata obtain complex global behavior by having useful local update rules; modern LLM systems obtain gains from semantic reasoning inside the nodes.
4. **Diversity matters.** Different models, prompts, tools, roles, or evidence channels can increase effective information rather than only nominal population size.
5. **State-aware communication matters.** What should be sent depends on what the sender and collective currently know.
6. **Persistent shared environments can matter.** Stigmergic systems provide a coordination mechanism fundamentally different from repeated message forwarding.

The first experiment in this repository increased transport capacity far more than transformation capacity. This explains why message count and runtime rose sharply while hard-task reasoning remained nearly flat.

## 7. Next research step suggested by both this study and prior work

The next experiment should not simply extend the mesh to more nodes. It should introduce one controlled change to local capability while keeping the existing topology benchmark:

- a very small semantic/local reasoning worker;
- then heterogeneous node roles or capabilities;
- then state-aware routing;
- then persistent stigmergic or dead-end memory.

The same 1 -> N scaling curve can then be rerun after each intervention. This would separate four possible sources of collective intelligence:

`node capability -> diversity -> adaptive transmission -> persistent environment`

rather than attributing any improvement merely to population size.

## References

1. Mitchell, M., Crutchfield, J. P., & Hraber, P. T. (1994). *Evolving cellular automata to perform computations: mechanisms and impediments*. Physica D, 75, 361-391. https://doi.org/10.1016/0167-2789(94)90293-3
2. Li, J., Zhang, Q., Yu, Y., Fu, Q., & Ye, D. (2024). *More Agents Is All You Need*. TMLR. https://arxiv.org/abs/2402.05120
3. Li, Y. et al. (2024). *Improving Multi-Agent Debate with Sparse Communication Topology*. Findings of EMNLP 2024. https://aclanthology.org/2024.findings-emnlp.427/
4. Zhuge, M. et al. (2024). *GPTSwarm: Language Agents as Optimizable Graphs*. ICML 2024. https://proceedings.mlr.press/v235/zhuge24a.html
5. Zhang, G. et al. (2025). *G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks*. ICML 2025. https://proceedings.mlr.press/v267/zhang25cu.html
6. Shen, X. et al. (2025). *Understanding the Information Propagation Effects of Communication Topologies in LLM-based Multi-Agent Systems*. EMNLP 2025. https://aclanthology.org/2025.emnlp-main.623/
7. Yang, Y. et al. (2026). *Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity*. https://arxiv.org/abs/2602.03794
8. Bertalanič, B., & Fortuna, C. (2026). *The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size*. https://arxiv.org/abs/2606.02646
9. Kim, Y. et al. (2026). *Capable language models can outgrow the benefits of collaboration*. Nature Machine Intelligence. https://doi.org/10.1038/s42256-026-01268-y
10. Colas, C. et al. (2026). *Discovering Adaptive Transmission Programs for Collective Innovation*. https://arxiv.org/abs/2608.24545
11. Pal, S., Wang, F. Y., & Buehler, M. J. (2026). *SwarmWorld: Stigmergic technological evolution in societies of language-model agents*. https://arxiv.org/abs/2608.26081
