---
title: "On the Fundamental Limitations of Dual Static CVaR Decompositions in Markov Decision Processes"
type: source
created: 2026-05-13
updated: 2026-05-13
sources: [raw/papers/2507.14005v2.pdf]
tags: [cvar, dynamic-programming, cvar-decomposition, criticism]
---
# On the Fundamental Limitations of Dual Static CVaR Decompositions in Markov Decision Processes

**Citation**: Godbout, M., & Durand, A. (2026). On the Fundamental Limitations of Dual Static CVaR Decompositions in Markov Decision Processes. arXiv:2507.14005v2.

## Abstract
This paper critiques previous works (notably Chow et al., 2015) that attempted to use Dynamic Programming (DP) techniques on the dual formulation to find static CVaR-optimal policies in Markov Decision Processes (MDPs). By analyzing the policy evaluation step, the authors identify a "CVaR evaluation gap" caused by conflicting risk-assignment constraints, proving that the augmented-state Bellman formulation is fundamentally limited and structurally incapable of producing uniformly optimal policies across all risk levels.

## Key Claims & Methodology
- It has been known that the [[Bellman Operator]] proposed by *Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach* (Chow et al., 2015) can fail. This paper diagnoses exactly why.
- **The Core Criticism**: Chow et al. augmented the state space $X$ with the confidence level $\alpha$ to decompose static CVaR sequentially over time. The flaw arises because static CVaR assigns risk holistically over full trajectories, while the augmented-state DP attempts to assign conditional risk greedily step-by-step.
- **Risk-Assignment Consistency Constraints**: The authors show that the step-by-step dynamic dual minimization and the holistic static return minimization represent two distinct mathematical problems. They define a set of consistency constraints mathematically required for the two problems to yield the same result. The DP approach frequently results in an empty intersection of these constraints.
- **State Augmentation Failure**: Because of the time-inconsistency of CVaR, there exists an inherent limitation where no single Markovian policy running on the augmented $(x,\alpha)$ state space can be simultaneously optimal for all initial risk levels $\alpha$. The time-consistent surrogate objective targeted by the DP deviates strictly from the actual static CVaR target, producing a nonzero "CVaR evaluation gap."

## Links
- [[CVaR Decomposition]]
- [[Bellman Operator]]
- [[Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach]]
