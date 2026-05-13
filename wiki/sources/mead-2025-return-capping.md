---
title: "Return Capping: Sample-Efficient CVaR Policy Gradient Optimisation"
type: source
created: 2026-05-13
updated: 2026-05-13
sources: [raw/papers/2504.20887v2.pdf]
tags: [cvar, policy-gradient, optimization, sample-efficiency]
---
# Return Capping: Sample-Efficient CVaR Policy Gradient Optimisation

**Citation**: Mead, H., Costen, C., Lacerda, B., & Hawes, N. (2025). Return Capping: Sample-Efficient CVaR Policy Gradient Optimisation. *ICML 2025*. arXiv:2504.20887v2.

## Abstract
Traditional CVaR Policy Gradient algorithms discard a significant portion ($1-\alpha$) of sample trajectories, leading to severe sample inefficiency. This paper proposes a reformulation where all trajectories are retained for training, but their maximum registered return is capped at a specific threshold. If configured correctly, optimizing this Return Capping objective yields the same optimal policy as static CVaR optimization while utilizing all trajectory data.

## Key Claims & Methodology
- Standard [[CVaR Policy Gradient]] methods sort sample trajectories by return and outright discard the top $1-\alpha$ fraction, calculating the gradient only from the worst-case $\alpha$ tail. This wastes massive amounts of data and prevents the policy from learning from successful trajectories.
- The paper solves this sample inefficiency by introducing **Return Capping**. Instead of discarding the non-tail trajectories, they are included in the gradient calculation but their returns are artificially truncated (capped) at a designated threshold (the $\alpha$-quantile [[VaR]] equivalent).
- The authors mathematically prove that optimizing this capped-return expectation is equivalent to optimizing the original static CVaR objective, provided the cap is set correctly.
- This preserves the learning signal from high-performing behaviors (up to the cap limit) and dramatically improves the algorithm's sample efficiency.

## Links
- [[CVaR]]
- [[CVaR Policy Gradient]]
- [[VaR]]
