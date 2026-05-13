---
title: "CVaR Gradient Estimation"
type: concept
created: 2026-05-13
updated: 2026-05-13
sources: []
tags: [gradient, optimization]
---
# CVaR Gradient Estimation

Estimating the gradient of the [[CVaR]] objective involves expressing it as a conditional expectation. In sampling-based approaches, it faces severe sample inefficiency because the gradient is effectively averaged only over the $\alpha N$ samples in the tail, causing high variance.

Mentioned in: [[Optimizing the CVaR via Sampling]]
