---
title: "A Simple Mixture Policy Parameterization for Improving Sample Efficiency of CVaR"
type: source
created: 2026-05-13
updated: 2026-05-13
sources: [raw/papers/2403.11062v3.pdf]
tags: [cvar, policy-gradient, optimization]
---
# A Simple Mixture Policy Parameterization for Improving Sample Efficiency of CVaR

**Citation**: Luo, Y., Pan, Y., Wang, H., Torr, P., & Poupart, P. (2024). A Simple Mixture Policy Parameterization for Improving Sample Efficiency of CVaR Optimization. *RLC 2024*. arXiv:2403.11062v3.

## Abstract
This paper addresses the sample inefficiency and vanishing gradient issues inherent in [[CVaR Policy Gradient]] methods. The authors propose a simple mixture policy parameterization that combines a risk-neutral policy with an adjustable risk-averse policy, allowing all collected trajectories to be used for policy updating. This approach prevents extreme tail-flattening that causes optimization to stall in traditional algorithms.

## Key Claims & Methodology
- Identifies cases in vanilla [[CVaR Policy Gradient]] (e.g. Tamar et al., 2015) where the gradient updates stall. Due to discarding $1-\alpha$ fraction of the samples and the return function becoming excessively flat in the low quantiles, policy updates vanish.
- Introduces a structural alteration to exploration: the policy $\pi$ is formulated as a mixture $w\pi_{rn} + (1-w)\pi_{ra}$, where $\pi_{rn}$ is a fixed/separately-trained risk-neutral policy and $\pi_{ra}$ is the learned risk-averse component.
- The inclusion of $\pi_{rn}$ stimulates higher global returns and prevents the extreme pathological tail flattening that halts plain [[CVaR Policy Gradient]] learning.
- By retaining the influence of all samples through the mixed policy objective, sample efficiency improves dramatically over traditional tail-only sampling methods.

## Experimental Overview
While the paper evaluates on standard Mujoco environments, the main takeaway is that introducing a heuristic mixture component enables CVaR optimization where traditional algorithms completely fail to converge due to the identified tail-flattening pathologies.

## Links
- [[CVaR]]
- [[CVaR Policy Gradient]]
- [[CVaR Gradient Estimation]]
