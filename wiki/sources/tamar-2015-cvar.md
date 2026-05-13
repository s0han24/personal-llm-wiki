---
title: "Optimizing the CVaR via Sampling"
type: source
created: 2026-05-13
updated: 2026-05-13
sources: [raw/papers/1404.3862v4.pdf]
tags: [cvar, reinforcement-learning, gradient-estimation, importance-sampling]
---
# Optimizing the CVaR via Sampling

**Citation**: Tamar, A., Glassner, Y., & Mannor, S. (2015). Optimizing the CVaR via Sampling. *AAAI Conference on Artificial Intelligence*. arXiv:1404.3862v4.

## Abstract
Conditional Value at Risk (CVaR) is a prominent risk measure. This paper develops a new formula for the gradient of the CVaR in the form of a conditional expectation. Based on this, a sampling-based estimator for the CVaR gradient is proposed, extending the likelihood-ratio method. The authors analyze the estimator's bias, prove convergence for a corresponding stochastic gradient descent algorithm, and apply it to a reinforcement learning domain (Tetris).

## Key Claims & Theory
- Introduces a new CVaR gradient estimation formula expressed as a conditional expectation, applicable when the tunable parameters control the distribution of outcomes (e.g., in [[Reinforcement Learning]]).
- Extends the traditional likelihood-ratio method (policy gradient) to optimizing the [[CVaR]] of the payoff.
- High sample inefficiency arises at low quantiles: when $\alpha$ is close to 0, the empirical CVaR estimator suffers from high variance because the gradient is effectively averaged only over $\alpha N$ samples (the worst-case tail). 
- To mitigate this severe sample inefficiency, the paper incorporates an [[Importance Sampling]] procedure.

## Methodology: Model-Based Importance Sampling
- To address the variance issue, the authors use variance reduction via Importance Sampling (IS).
- In the RL context, finding a suitable sampling distribution requires modifying the trajectory distribution, which is achieved by modifying the underlying MDP transition probabilities. 
- **Model-Based Requirement**: Because it changes transition dynamics rather than just the policy, this approach requires access to a simulator of the modified MDP. This characterizes it as a *model-based* importance sampling procedure.

## Limitations & Open Questions
- The reliance on a modified MDP simulator for importance sampling restricts its applicability in model-free environments.
- The base algorithm exhibits severe sample inefficiency without IS.
- Does not extensively explore if or how such objective could be modeled securely without direct access to the environment simulator.

## Links
- [[CVaR]]
- [[CVaR Gradient Estimation]]
- [[Importance Sampling]]
- [[Likelihood-Ratio Method]]
