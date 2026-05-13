---
title: "CVaR Policy Gradient"
type: concept
created: 2026-05-13
updated: 2026-05-13
sources: []
tags: [reinforcement-learning, optimization]
---
# CVaR Policy Gradient

CVaR Policy Gradient methods optimize the Conditional Value at Risk in an RL context by estimating gradients analytically from trajectory samples. Originally introduced in [[Optimizing the CVaR via Sampling]], they often suffer from structural vanishing gradients due to pathological tail-flattening, a problem mitigated by heuristics like those discussed in [[A Simple Mixture Policy Parameterization for Improving Sample Efficiency of CVaR]].

Mentioned in: [[A Simple Mixture Policy Parameterization for Improving Sample Efficiency of CVaR]]
