# Result roles and reproduction limits

This release preserves both favorable and unfavorable findings. The primary corrected cohort has 3,443 papers. Conditional citation-rank associations are approximately .009 for TNS and .188 for ENS. The 2023 10%-budget comparison has precision .323 for TNS and .424 for ENS; Recommendation is an important competing criterion, not an omitted rival.

The missing-outcome analysis concerns 4,867 score-observed papers, not the full source population. Bounds are deterministic identification intervals conditional on fixed scores, thresholds and missingness setup; they are not confidence intervals or causal effects. Direct all-versus-accepted contrasts remain unresolved. Statistical non-significance is not evidence of equivalence.

| Saved file | Recomputed by the included empirical replay | Frozen output only |
|---|---|---|
| `corrected_results.json` | Raw and partial primary/fixed-horizon correlations; six selection precision panels | Bootstrap CIs, profile fits, temporal text baselines, human and area sensitivities |
| `missing_outcome_bounds.json` | 24 pairwise bound endpoints across six pools | Source recovery and raw matching history |
| `decision_pool_comparisons.json` | Not recomputed | 36 budget/threshold panels, 12 direct pool contrasts, resampling uncertainty |
| `same_reviewer_analysis.json` | Not recomputed | Same-reviewer/first-author-cluster sensitivity |
| `scorer_portability.json` | Not recomputed | Cross-scorer fits and CIs |

The secondary profile is not model-independent: the corrected pilot's GPT-4o-mini fitted TO7 correlation is about .135 versus Sonnet .518 and reviewer labels .242. The release does not obscure this failure or claim a model-capacity explanation. No provider responses or hidden model state are required for the primary reviewer-score analyses.

Exact arrays, sample counts, interval definitions and bootstrap settings are retained in the corresponding JSON where available. This compact code release does not certify the entire paper's reproducibility, the quality of original linkage, or deployment suitability. The synthetic tests exercise algorithmic invariants; passing them does not establish empirical validity.
