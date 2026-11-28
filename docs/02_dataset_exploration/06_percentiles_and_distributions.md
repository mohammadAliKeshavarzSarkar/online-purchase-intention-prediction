# Lesson 8 — Percentiles, distributions, and interquartile range

**Status:** Percentile experiment executed in GitHub Codespaces; researcher supplied the output.

## Question
How are product-page visits distributed within purchasing and non-purchasing sessions, beyond their averages?

## Concepts
- A **percentile** is a cutoff at or below which approximately that percentage of observations falls.
- **Q1 (25th percentile)**, **median (50th percentile)**, **Q3 (75th percentile)**, and **P95 (95th percentile)** summarize different parts of a distribution.
- **IQR = Q3 − Q1**, the span of the middle 50% of observations.
- Large gaps between typical and maximum values can suggest a long right tail; they do not establish data errors.

## Code executed
```python
print("\nPRODUCT PAGE VISITS — PERCENTILES")
percentiles = (
    df.groupby("Revenue")["ProductRelated"]
    .quantile([0.25, 0.50, 0.75, 0.95])
    .unstack()
)
percentiles.columns = ["Q1 (25%)", "Median (50%)",
                       "Q3 (75%)", "P95 (95%)"]
print(percentiles.round(2))
```

## Actual results
| Revenue | Q1 (25%) | Median (50%) | Q3 (75%) | P95 (95%) |
|---|---:|---:|---:|---:|
| False | 6.0 | 16.0 | 35.0 | 97.0 |
| True | 15.0 | 29.0 | 57.0 | 159.0 |

Previously observed maximum values: **705** for non-purchasing sessions and **534** for purchasing sessions.

## Analysis
- Purchase sessions have higher product-page counts at every reported percentile.
- Within the purchase group, about 75% of sessions have **57 pages or fewer**; within the non-purchase group, about 75% have **35 or fewer**. These percentages use different group denominators.
- Purchase-group P95 is **159**, compared with **97** in the non-purchase group.
- **IQR, no purchase:** 35 − 6 = **29** pages.
- **IQR, purchase:** 57 − 15 = **42** pages.
- The larger absolute IQR in the purchase group means its middle 50% spans a wider range of page counts.
- High maximums relative to P95 are consistent with long right tails, but distribution shape and validity of extremes still require investigation.
- These are descriptive associations, not evidence that additional browsing *causes* purchases.

## Research reasoning
1. **Question:** Is the average representative?
2. **Evidence:** Observed quartiles and 95th percentiles by outcome.
3. **Analysis:** Compare percentiles and calculate IQR within each group.
4. **Interpretation:** Purchasing sessions generally show higher page counts, with greater absolute spread in the middle half.
5. **Challenge:** Inspect distributions directly; do not assume extremes are invalid or that correlation is causal.

## Next experiment (not yet executed)
Create a histogram or boxplot of `ProductRelated` by `Revenue` to inspect distribution shape and potential outliers. Do not report unexecuted visualizations as observed results.

## Check your understanding
If Q3 for purchasing sessions is 57, approximately what proportion of purchasing sessions have 57 product-page visits or fewer?

**Key takeaway:** Percentiles and IQR reveal information about typical values and spread that a mean alone can hide.
