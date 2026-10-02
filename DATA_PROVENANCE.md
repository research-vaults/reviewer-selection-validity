# Provenance and redistribution boundaries

Project code computes statistics from scholarly-review and citation data. OpenReview supplies review-score/decision metadata; Semantic Scholar supplies citation metadata. We retain attribution to both providers and do not purport to relicense their content.

Source policies checked October 2, 2026:

[OpenReview Terms](https://openreview.net/legal/terms) distinguish metadata from article and comment licenses and preserve access restrictions. [Semantic Scholar API terms](https://api.semanticscholar.org/license/) contain restrictions on sharing API data. Accordingly, this release excludes row-level API responses, citation outcomes, titles, abstracts and raw review material. Readers must obtain eligible local inputs separately. See [Semantic Scholar](https://www.semanticscholar.org/?utm_source=api) for the citation source.

The JSON files in `results/` contain project-computed aggregate statistics and analysis settings, not source-record dumps. Paper identifier arrays and embedding row-index maps were omitted from the export. Retained numerical fields are unchanged from the corrected analysis. No model calls or human ratings were newly generated for this release.

Human individual-level ratings, recruitment/consent records and model response logs are not released. Aggregate human/scorer outcomes remain where relevant, including unfavorable portability results. Their inclusion does not certify an individual-level redistribution permission or general validity of a model scorer.

Code and documentation are covered by the included MIT license to the extent the project holds the rights. Dependencies are installed separately and retain their respective licenses. No third-party template, vendored library, image, paper or repository is bundled. Aggregate scientific findings are not a new license to underlying API data. This is a conservative release boundary, not legal advice or a guarantee covering every downstream use.
