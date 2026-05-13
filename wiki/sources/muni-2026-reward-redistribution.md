---
title: "Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity"
type: source
created: 2026-05-13
updated: 2026-05-13
sources: [raw/papers/2602.03778v1.pdf]
tags: [cvar, dynamic-programming, bellman-operator, reward-shaping]
---
# Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity

**Citation**: Muni, A., Taboga, V., Derman, E., Bacon, P.-L., & Delage, E. (2026). Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity. arXiv:2602.03778v1.

## Abstract
Because the static [[CVaR]] of a return depends on entire trajectories, it lacks a recursive decomposition. Previous state-augmentation solutions (e.g., Bäuerle & Ott, 2011; Chow et al., 2015) resulted in sparse rewards and degenerate fixed points. This work proposes a novel formulation of the static CVaR objective via state augmentation (tracking accumulated return) that features dense per-step rewards and a contracting [[Bellman Operator]] on the full space of bounded value functions ($L_\infty$).

## Key Claims & Methodology
- **State Augmentation**: To overcome the fundamental lack of Markovian recursive separability in static CVaR, the authors build on the method of augmenting the state space with a continuous "budget" variable (representing accumulated return). 
- **A New Bellman Operator**: Early augmented MDP methods concentrate the CVaR objective at the terminal state, creating a sparse learning signal. Muni et al. develop a novel reward redistribution mechanism for the augmented MDP, establishing a contracting [[Bellman Operator]]. This produces dense per-step feedback and guarantees contracting properties without restricting the value functions to a specialized class.
- **Discretization and Algorithms**: Because the augmented budget variable is continuous, the authors propose a discretization strategy. They introduce two primary algorithms relying on discretization of augmented states:
  - Risk-averse Value Iteration (model-based)
  - Risk-averse Q-learning (model-free)
Both algorithms come with theoretical convergence proofs and bounded approximation errors relative to the discretization granularity.

## Links
- [[CVaR]]
- [[Bellman Operator]]
- [[CVaR Decomposition]]
