---
title: "Policy Gradient for Coherent Risk Measures"
type: source
created: 2026-05-13
updated: 2026-05-13
sources: [raw/papers/NIPS-2015-policy-gradient-for-coherent-risk-measures-Paper.pdf]
tags: [cvar, policy-gradient, coherent-risk, actor-critic]
---
# Policy Gradient for Coherent Risk Measures

**Citation**: Chow, Y., Tamar, A., Ghavamzadeh, M., & Mannor, S. (2015). Policy Gradient for Coherent Risk Measures. *NIPS 2015*.

## Abstract
This paper generalizes risk-sensitive policy gradient methods in Reinforcement Learning beyond single specific risk-measures (like variance or CVaR) to the entire class of Coherent Risk Measures. It provides sampling-based gradient algorithms for both Static Risk Measures (evaluating the total trajectory return) and time-consistent Dynamic Risk Measures (evaluating risk recursively per step). 

## Key Claims & Methodology
- **Dynamic vs Static Risk**: The paper explicitly delineates two types of targeted risk formulations. 
  - **Static Risk** applies a functional directly to the entire full-horizon execution return (e.g. static [[CVaR]]). It accurately reflects the final tail-risk but lacks time consistency and recursive separability.
  - **Dynamic Risk** applies a sequence of coherent risk mappings iteratively over time, ensuring a time-consistent property where optimal remaining trajectories stay optimal. However, this may alter the overall interpretation of the risk target.
- **Static Risk Algorithms**: For optimizing static coherent measures, the approach combines standard sample-based gradient estimation (likelihood-ratio/REINFORCE) with a convex programming subroutine to evaluate the gradient formula via an envelope theorem result.
- **Dynamic Risk Algorithms**: For dynamic (time-consistent Markov) coherent risk measures, the sequence of gradient formulas leverages dynamic programming decompositions. The authors propose an **Actor-Critic style algorithm**, utilizing an explicit parameterization and approximation of the value function to scale to dynamic risk environments.

## Links
- [[CVaR]]
- [[CVaR Policy Gradient]]
- [[Actor-Critic]]
- [[Coherent Risk Measures]]
