---
title: "Wiki Log"
type: log
---

# Wiki Log

Append-only chronological record of all operations.
Each entry starts with `## [YYYY-MM-DD]` for easy grep filtering.

Usage examples:
```bash
# Last 5 entries
grep "^## \[" wiki/log.md | tail -5

# All ingests
grep "^## \[" wiki/log.md | grep "ingest"

# All lint passes
grep "^## \[" wiki/log.md | grep "lint"
```

---

## [YYYY-MM-DD] init
- Wiki initialized with AGENTS.md schema, index.md, log.md, overview.md
- Raw source directories created: raw/papers, raw/articles, raw/notes, raw/assets
- Wiki directories created: wiki/sources, wiki/entities, wiki/concepts, wiki/analyses
- Notes: ready for first ingest

## [2026-05-13] ingest | Optimizing the CVaR via Sampling
- Summary: wiki/sources/tamar-2015-cvar.md
- Pages updated: [[overview.md]], [[index.md]]
- Pages created: [[CVaR]], [[CVaR Gradient Estimation]], [[Importance Sampling]], [[Likelihood-Ratio Method]], [[Reinforcement Learning]]
- Contradictions flagged: none
- Notes: User emphasized highlighting the structural sample inefficiency of empirical CVaR estimators and the reliance on model-based Importance Sampling.

## [2026-05-13] ingest | ACReL: Adversarial Conditional value-at-risk Reinforcement Learning
- Summary: wiki/sources/godbout-2021-acrel.md
- Pages updated: [[overview.md]], [[index.md]]
- Pages created: [[Adversarial RL]], [[Stackelberg Game]]
- Contradictions flagged: none
- Notes: Discussed sample inefficiency framing via adversarial perturbation bounds. Noted the limitation on the adversary needing theoretical model state transition access while the agent operates model-free.

## [2026-05-13] ingest | A Simple Mixture Policy Parameterization for Improving Sample Efficiency of CVaR
- Summary: wiki/sources/luo-2024-mixture-policy.md
- Pages updated: [[overview.md]], [[index.md]]
- Pages created: [[CVaR Policy Gradient]]
- Contradictions flagged: none
- Notes: User requested a brief explanation of the mixture policy without diving deep into the experimental Mujoco setups, emphasizing how it prevents pathological gradient vanishing in CVaR-PG.

## [2026-05-13] ingest | Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach
- Summary: wiki/sources/chow-2015-risk-sensitive.md
- Pages updated: [[overview.md]], [[index.md]]
- Pages created: [[CVaR Decomposition]], [[Distributionally Robust Optimization]], [[Bellman Operator]]
- Contradictions flagged: Flagged the known flaw in Chow et al.'s proposed Bellman Operator, while preserving validity of dual static representation and DRO translations.
- Notes: Human explicitly required separating the true theoretical contributions (static duality, DRO framing) from the disproved artifacts (Bellman Operator execution flaws).

## [2026-05-13] ingest | Return Capping: Sample-Efficient CVaR Policy Gradient Optimisation
- Summary: wiki/sources/mead-2025-return-capping.md
- Pages updated: [[overview.md]], [[index.md]]
- Pages created: [[VaR]]
- Contradictions flagged: none
- Notes: User explicitly requested to keep this summary extremely brief and focused purely on the return capping mechanic addressing CVaR sample inefficiency.

## [2026-05-13] ingest | On the Fundamental Limitations of Dual Static CVaR Decompositions in Markov Decision Processes
- Summary: wiki/sources/godbout-2026-fundamental-limitations.md
- Pages updated: [[overview.md]], [[index.md]]
- Pages created: none
- Contradictions flagged: Detailed confirmation of the discrepancy between static CVaR evaluation and DP conditional derivations, reinforcing the earlier flagged discrepancy with Chow et al. 2015.
- Notes: User emphasized explaining the exact criticism of Chow et al. (the failure of the state augmentation technique resulting in the CVaR evaluation gap).

## [2026-05-13] ingest | Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity
- Summary: wiki/sources/muni-2026-reward-redistribution.md
- Pages updated: [[overview.md]], [[index.md]]
- Pages created: none
- Contradictions flagged: none
- Notes: User emphasized highlighting the specific augmented Bellman operator, the use of continuous state discretization, and the resulting VI / Q-learning algorithms.

## [2026-05-13] ingest | Policy Gradient for Coherent Risk Measures
- Summary: wiki/sources/chow-2015-policy-gradient.md
- Pages updated: [[overview.md]], [[index.md]]
- Pages created: [[Actor-Critic]], [[Coherent Risk Measures]]
- Contradictions flagged: none
- Notes: Human asked to briefly cover the difference between dynamic and static CVaR alongside the algorithms presented.

## [2026-05-13] lint
- Orphans: 0
- Stubs: 6
- Contradictions unresolved: 1
- Action taken: Generated lint report; waiting for human input on fixing index.md tables and stubs.
