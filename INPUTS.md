# Eligible local inputs

The empirical replay needs two files acquired and held under applicable source permissions. The repository does not include them or offer a substitute synthetic dataset as empirical evidence. Put them outside this checkout and pass `--data-dir`.

## verified_link_rows.csv

One row per member of the corrected joint population; exactly 3,443 rows.

| Column | Definition |
|---|---|
| `forum` | Consistent paper join key; a local pseudonym is sufficient if used in both files |
| `year` | 2022 or 2023 |
| `accepted` | Binary recorded acceptance indicator |
| `tns` | Mean observed Technical Novelty and Significance score |
| `ens` | Mean observed Empirical Novelty and Significance score |
| `recommendation` | Mean observed Recommendation score |
| `cumulative_log_citations` | Natural log of one plus the frozen cumulative citation count |
| `fixed24_log_citations` | Natural log of one plus fixed 24-month citations after removal of identifiable self-citations |

Use the original retained row order for exact numerical replay. No author names, affiliations, reviewer names, prose, emails or credentials are needed.

## score_observed_population.json

A JSON list of 4,867 objects with `forum`, `year`, `accepted`, and `scores`. `scores` contains three numbers in the exact order `[TNS, ENS, Recommendation]`. The 3,443 observed-outcome keys above are a subset; the other 1,424 have unknown outcomes in the analysis. Additional keys are ignored. Keys can be consistently pseudonymized locally; they need not be public identifiers.

## Construction and limitations

The source frame contains 6,409 submissions; the historical export contains 3,886. The corrective analysis requires normalized exact title agreement plus compatible author metadata, yielding 3,483 strict-linked records and 3,443 with all three scores. Fifteen incompatible links are excluded. Score recovery expands the observed-score frame to 4,867; the remaining 1,542 source records lack complete scores. These selection and linkage steps are not reproduced by the compact replay.

Rank residualization uses an intercept, year and acceptance without interpreting adjustment as a causal effect. Historical budget panels rank 10% of each pool and define high uptake by that pool's fixed-horizon upper quartile. Missing-outcome bounds instead fix the year-level observed-outcome threshold and include unknown outcomes in the score-observed frame. Fractional tie weights sum to the reading budget. Do not substitute one population or threshold for the other.

The citation-event harvest is historical and partially dated/identity-resolved; a fresh service query may differ. Do not claim exact empirical reproduction from an independently refreshed dataset. Public access to a record also does not automatically establish redistribution permission. If permissions or the matching history cannot be recovered, report that limitation rather than inventing rows or filling missing outcomes.
