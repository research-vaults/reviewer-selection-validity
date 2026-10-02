# Reviewer Selection-Target Validity

Analysis code and aggregate results for **The Selection-Target Problem in AI-Assisted Science: Reviewer Novelty and Later Scientific Uptake**.

[Read the matching research draft (1 October 2026)](https://odysseus-personal-website.vercel.app/materials/papers/selection-target.pdf) | Code and aggregate-results release: **2 October 2026**

The study compares Technical Novelty and Significance (TNS), Empirical Novelty and Significance (ENS), and Recommendation scores with later citation uptake. In the corrected matched population, year-and-acceptance-adjusted correlation is .009 for TNS and .188 for ENS. We separately assess fixed-budget selection yield and sensitivity to missing citation outcomes. These observational analyses concern uptake, not intrinsic scientific value or the causal benefit of deploying a selector.

## Version and scope

The linked 19-page research draft incorporates the corrected analysis on **3,443** title-and-author-matched papers with all three reviewer scores and a **4,867**-paper score-observed population for missing-outcome bounds. It develops the earlier AI for Meta-Science workshop paper; it is not the original submitted workshop attachment or a main-track accepted paper. The earlier workshop snapshot used a 3,839-paper joint comparison and reported conditional TNS/ENS correlations of .017/.192. Those values are superseded here by .009/.188 on the corrected population. Do not mix the versions.

The public PDF was checked on 2 October 2026: SHA-256 `51c76b7e04c24767294674ec9fcf9a2ca6d238810c73c53c519b57218ba128a4`. Its scientific text matches the 30 September corrected research manuscript. The external URL may later be updated; this date and hash identify the version corresponding to the released results.

## Quick start

Python 3.11 or newer:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_release.py
python -m unittest discover -s tests -v
```

Expected output: the verifier reports `status: PASS` for 15 manifested files and the unit suite reports six passing tests. Tests cover rank residualization, fractional allocation of tied scores, and missing-outcome endpoints against independent enumeration. After dependency installation, these small CPU-only checks run offline in seconds without empirical data, API keys or model calls. A GPU is unnecessary.

## Replay the empirical results with eligible local inputs

Supply `verified_link_rows.csv` and `score_observed_population.json` in a directory outside this checkout, using the schema in [INPUTS.md](INPUTS.md):

```sh
python scripts/replay_results.py --data-dir ../eligible-selection-inputs
```

Expected output is JSON with `status: PASS`, `current_joint_rows: 3443`, `selection_panels: 6`, and `bound_endpoints: 24`. The script compares cumulative and fixed-horizon raw/adjusted point estimates, six 10%-budget panels and all 24 bound endpoints against saved results. It does not write to the release.

This command was tested locally against retained eligible inputs and completed in about two seconds on a CPU, without API calls; runtime depends on hardware. A public checkout alone cannot reproduce the empirical values because the input rows are not distributed. The replay does not reconstruct matching, citation histories, bootstrap intervals, secondary model fits or historical provider state. Fresh API queries cannot be assumed to recover the original snapshots exactly.

## Paper results and commands

| Matching research-draft result | Available evidence and replay |
|---|---|
| Figure 1 / Table 2: matched reviewer-score associations | `scripts/replay_results.py --data-dir ...` recomputes point estimates from eligible inputs; intervals are saved in `results/corrected_results.json`. |
| Table 3 / Tables 8–9: 10%-budget selection | The same command recomputes six panels; saved bootstrap intervals are not regenerated. |
| Table 4: missing-outcome bounds | The same command recomputes 24 bound endpoints in `results/missing_outcome_bounds.json`. |
| Tables 10–12: direct pool contrasts and budget sensitivity | Frozen outputs in `results/decision_pool_comparisons.json`; not recomputed by this package. |
| Reviewer-composition and secondary profile analyses | Frozen aggregate files in `results/`, including adverse scorer-portability results; detailed coverage in [RESULTS.md](RESULTS.md). |

`MANIFEST_SHA256.json` covers the complete release file inventory. Integrity checks and synthetic tests are not empirical replication.

## Data and rights

This compact release contains code and aggregate results, not the underlying dataset. Row-level API-derived outcomes, source texts, individual human ratings and provider logs are excluded pending redistribution/consent clearance. [INPUTS.md](INPUTS.md) specifies required inputs and unreproduced construction steps; [DATA_PROVENANCE.md](DATA_PROVENANCE.md) explains source attribution and restrictions. Project code/documentation retain the [MIT licence](LICENSE); this does not relicense OpenReview or Semantic Scholar data or the externally hosted manuscript.

## Citation

For scientific claims, cite the linked manuscript using its displayed bibliographic information and identify it as the **1 October 2026 research draft**, not the original workshop snapshot. For code, cite this repository URL, the **2 October 2026** release date and the commit used. The public paper link identifies the work; this repository is not an anonymous-review package.
