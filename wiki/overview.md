---
title: "Overview"
type: overview
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
tags: []
---

# Overview

*This page is maintained by the LLM. It is a living synthesis of everything in the wiki.
It should be updated on every ingest to reflect how the new source changes the picture.*

---

## Current thesis

*(No sources ingested yet. This section will hold the evolving synthesis — the 1–3 paragraph answer to "what do I currently believe about this research area, and why?")*

---

## Major themes

*(Key recurring ideas across sources will be listed here with links to concept pages.)*

---

## Open questions

*(Questions the current body of sources raises but doesn't answer. Each one is a candidate for the next ingest target.)*

---

## Tensions and contradictions

*(Where sources disagree. Links to the relevant contradiction markers in source/entity/concept pages.)*

---

## Coverage map

*(What's well-covered, what's sparse, what's missing entirely. Useful for deciding what to read next.)*

## Risk-Sensitive Optimization
Risk measures, particularly [[CVaR]], have seen algorithmic improvements extending their applicability to [[Reinforcement Learning]]. Notably, [[Optimizing the CVaR via Sampling]] provides a gradient estimation formula allowing direct CVaR optimization, but reveals that empirical estimators for extreme tail probabilities are heavily sample-inefficient. Model-based [[Importance Sampling]] is necessary to make the gradient descent tractable.

Further, addressing the sample inefficiency of typical empirical CVaR estimators, [[ACReL: Adversarial Conditional value-at-risk Reinforcement Learning]] reformulates the CVaR objective internally as an adversarial Stackelberg game. Rather than calculating tail statistics directly, the method uses an adversary with a constrained transition-perturbation budget to dynamically sculpt worst-case paths. However, this is largely limited by the requirement of full model access for the adversary.

Alternatively, [[A Simple Mixture Policy Parameterization for Improving Sample Efficiency of CVaR]] identifies that standard CVaR gradients can stall entirely due to extreme tail-flattening. It circumvents this by integrating a static risk-neutral term into the policy parameterization, ensuring baseline performance prevents pathological gradient death, serving as a simpler architectural fix compared to complex adversarial training dynamics.

Alternatively, risk modeling can be mapped directly to uncertainty sets under [[Distributionally Robust Optimization]] (DRO). [[Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach]] (Chow et al., 2015) formalizes this by proving optimizing static CVaR equates to bounding worst-case transition deviations via probability risk envelopes. However, readers must be cautious: although the static dual interpretations and broad [[CVaR Decomposition]] logic inform subsequent literature faithfully, the specific dynamic [[Bellman Operator]] proposed to implement it sequentially contains structural errors resulting in sub-optimal or time-inconsistent behavior.

Another direct solution to the structural sample inefficiency of empirical CVaR updates is "Return Capping" ([[Return Capping: Sample-Efficient CVaR Policy Gradient Optimisation]]). Here, instead of discarding the non-tail $1-\alpha$ trajectories, the algorithm retains them but truncates any return above the $\alpha$-quantile ([[VaR]]). By capping instead of discarding, the gradients utilize the full batch while mathematically preserving the exact same optimization target.

Addressing the known flaws in the early dynamic approaches, [[On the Fundamental Limitations of Dual Static CVaR Decompositions in Markov Decision Processes]] explores precisely why the augmented-state [[Bellman Operator]] proposed by Chow et al. fails. The transition from full-trajectory static returns to step-wise conditional bounds introduces a mathematical discrepancy. The evaluation gap stems from an empty intersection of risk-assignment consistency constraints, proving that state-augmentation methods are inherently incapable of discovering a single uniformly optimal policy due to time inconsistency.

Recent breakthroughs have re-attempted the [[CVaR Decomposition]] strategy that earlier failed. Instead of tracking confidence levels, [[Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity]] builds on augmenting the state with the accumulated return budget. Critically, it replaces the terminal sparse-reward evaluation of prior augmented MDPs with a novel reward redistribution scheme. This allows a functionally sound, contracting [[Bellman Operator]] yielding dense signals. Paired with state discretization, this produces viable Value Iteration and Q-learning algorithms with formal guarantees.

Broader foundations for this class of objective optimizations were laid mathematically in [[Policy Gradient for Coherent Risk Measures]], which extended typical policy gradients simultaneously to both Static Risk formulations (evaluating fully realized trajectories) via convex envelope bounds, and Dynamic Risk formulations via [[Actor-Critic]] mechanisms. This foundational distinction effectively catalyzed the divergence of subsequent CVaR methodologies.
