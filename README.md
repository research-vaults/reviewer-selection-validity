# Reviewer Selection-Target Validity

Analysis code and aggregate results for **The Selection-Target Problem in AI-Assisted Science: Reviewer Novelty and Later Scientific Uptake**.

The study compares Technical Novelty and Significance (TNS), Empirical Novelty and Significance (ENS), and Recommendation scores with later citation uptake. It separates adjusted rank association, fixed-budget selection yield, and sensitivity to unobserved citation outcomes. These observational analyses concern uptake, not intrinsic scientific value or the causal benefit of deploying a selector.

## Version and scope

Release `2026-10-02` represents the corrected research analysis on 3,443 linked papers and a 4,867-paper score-observed population. It is **not** the original workshop numerical snapshot. Earlier coefficients and population counts must not be mixed with these results. No manuscript PDF or source is included in this code release.

This is a **code-and-aggregate-results release**, not a complete downloadable dataset or a claim of end-to-end raw-data reproducibility. Row-level API-derived outcomes, source texts, human-rating records and provider response logs are withheld pending redistribution/consent clearance. See [INPUTS.md](INPUTS.md) and [DATA_PROVENANCE.md](DATA_PROVENANCE.md).

## Setup

Python 3.11 or newer:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_release.py
python -m unittest discover -s tests -v
```

The verifier checks exact manifest membership and SHA-256 hashes. The tests exercise rank residualization, fractional allocation of tied scores, and missing-outcome endpoints against independent enumeration. Tests use only synthetic values, not hidden empirical data. Neither command requires an API key or model call.

## Replay the empirical results with eligible local inputs

Supply `verified_link_rows.csv` and `score_observed_population.json` in a directory outside this checkout, using the schema in [INPUTS.md](INPUTS.md):

```sh
python scripts/replay_results.py --data-dir ../eligible-selection-inputs
```

Expected output is JSON with `status: PASS`, `current_joint_rows: 3443`, `selection_panels: 6`, and `bound_endpoints: 24`. The script compares cumulative and fixed-horizon raw/adjusted point estimates, six 10%-budget panels and all 24 bound endpoints against saved results. It does not write to the release.

This command was tested locally against the retained eligible inputs; those inputs are not distributed here. A public checkout alone can run the verifier and synthetic tests, but cannot independently reproduce the empirical values without those data. The replay does not reconstruct matching, citation histories, bootstrap intervals, secondary model fits or provider serving state. Stored uncertainty and secondary results are clearly marked as frozen outputs in [RESULTS.md](RESULTS.md).

## Contents

| Path | Purpose |
|---|---|
| `scripts/replay_results.py` | Offline point-estimate and missing-outcome-bound replay with explicit local inputs |
| `scripts/verify_release.py` | Integrity and membership verification |
| `tests/test_analysis.py` | Synthetic correctness checks independent of empirical inputs |
| `results/corrected_results.json` | Corrected correlations, selection estimates, intervals and secondary analyses |
| `results/missing_outcome_bounds.json` | Finite-population partial-identification intervals |
| `results/decision_pool_comparisons.json` | Budget/threshold family and direct pool comparisons |
| `results/same_reviewer_analysis.json` | Aggregate reviewer-composition sensitivity |
| `results/scorer_portability.json` | Aggregate alternate-scorer results, including unfavorable comparisons |
| `MANIFEST_SHA256.json` | Exact release file inventory |

Source data are credited to [OpenReview](https://openreview.net/) and [Semantic Scholar](https://www.semanticscholar.org/?utm_source=api). Their rights are not replaced by the project code license.

## Public release versus anonymous review

This public repository is not certified anonymous: its account, paper title and public links can connect it to the authors. Reviewer-facing snapshots and conference submissions remain separate and are not changed by this release. Personal contact details and affiliations are not needed in the analysis files.

Intentionally excluded: raw API data, article/reviewer text, individual human ratings, identity/linkage maps, API responses, credentials, manuscripts and old drafts, private reviews, planning records, comparator archives, caches, checkpoints and unrelated projects. No external model call or paid experiment is performed by the documented commands.
