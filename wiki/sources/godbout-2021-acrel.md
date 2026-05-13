---
title: "ACReL: Adversarial Conditional value-at-risk Reinforcement Learning"
type: source
created: 2026-05-13
updated: 2026-05-13
sources: [raw/papers/2109.09470v2.pdf]
tags: [cvar, reinforcement-learning, adversarial-rl]
---
# ACReL: Adversarial Conditional value-at-risk Reinforcement Learning

**Citation**: Godbout, M., Heuillet, M., Raparthy, S. C., Bhati, R., & Durand, A. (2021). ACReL: Adversarial Conditional value-at-risk Reinforcement Learning. arXiv:2109.09470v2.

## Abstract
In safety-critical domains, normal expected-return Reinforcement Learning can lead to failures due to uncertainties. While [[CVaR]] handles risk-aversion, typical methods lack theoretical guarantees. This paper proposes ACReL, a formulation scaling CVaR RL into a max-min adversarial game. The policy player maximizes returns while a learned adversary dynamically perturbs state transitions to minimize returns safely bounded by a finite cumulative budget.

## Key Claims & Theory
- **Addressing Sample Inefficiency**: The traditional empirical gradients of [[CVaR]] are heavily sample inefficient (from averaging only over the subset of tail samples). ACReL frames CVaR optimization from a different perspective: a max-min adversarial Stackelberg game. Instead of isolated tail sampling, the adversary actively shapes the environment to *create* the worst-case states systematically over time, effectively solving sample gathering bottlenecks via adversarial generation.
- **The Adversary's Mechanics**: The adversary is trained to minimize the agent's collected rewards by distributing a perturbation factor over the underlying transition kernel. It cannot perturb to impossible states, but only up-weigh reachable adverse states subject to a finite trajectory-level budget ($\eta$).
- **Equilibrium implies CVaR-optimality**: A key theoretical contribution is that nearing the game's equilibrium point yields a policy increasingly close to the targeted CVaR-optimal policy, where risk tolerance $\alpha$ is inversely tied to the adversary's cumulative budget.

## Methodology & Restrictions
- The game follows an asymmetric setup. At time step $t$, the agent selects an action without model knowledge. Then, the adversary observes the non-perturbed transition kernel $P_t$ and the residual budget $\eta_t$, outputting a valid perturbed kernel $\hat{P}_t$ which dictates the actual next state.
- **Model Access Asymmetry**: A highly restrictive feature is that the adversary has full access to the environment transition model $P(\cdot|s,a)$ to calculate its perturbations. The agent is model-free, but training the overall system dictates that an environment model (or simulator) must be accessible.

## Limitations & Open Questions
- Extremely dependent on simulated or model-known environments for the adversary to compute valid perturbations.

## Links
- [[CVaR]]
- [[Reinforcement Learning]]
- [[Adversarial RL]]
- [[Stackelberg Game]]
