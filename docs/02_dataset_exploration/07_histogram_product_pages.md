# Lesson 9 — Visualizing product-page visit distributions

**Status:** Histogram code executed in GitHub Codespaces; researcher supplied a screenshot of the generated two-panel histogram. The image was visually reviewed in the lesson.

## Research question
What is the shape of the `ProductRelated` distribution for purchasing and non-purchasing sessions?

## Code executed
```python
import matplotlib.pyplot as plt
from pathlib import Path

figures_dir = Path("figures")
figures_dir.mkdir(exist_ok=True)

no_purchase = df.loc[df["Revenue"] == False, "ProductRelated"]
purchase = df.loc[df["Revenue"] == True, "ProductRelated"]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(no_purchase, bins=40, color="steelblue")
axes[0].set_title("No Purchase")
axes[0].set_xlabel("Product Pages Visited")
axes[0].set_ylabel("Number of Sessions")
axes[1].hist(purchase, bins=40, color="darkorange")
axes[1].set_title("Purchase")
axes[1].set_xlabel("Product Pages Visited")
axes[1].set_ylabel("Number of Sessions")
fig.suptitle("Distribution of Product Page Visits")
plt.tight_layout()
output_path = figures_dir / "product_pages_histogram.png"
plt.savefig(output_path, dpi=150)
plt.close(fig)
print(f"\nHistogram saved to: {output_path}")
```

## Observed histogram findings
- Both distributions are **strongly right-skewed**: most sessions are concentrated at relatively low product-page counts, with long right tails.
- Unusually large counts occur in both groups; they are **potential** outliers, not automatically erroneous observations.
- These visual patterns are consistent with previously observed means exceeding medians.

## Supporting measured statistics
| Statistic | No purchase | Purchase |
|---|---:|---:|
| Count | 10422 | 1908 |
| Mean | 28.71 | 48.21 |
| Median | 16 | 29 |
| Q3 | 35 | 57 |
| P95 | 97 | 159 |
| Maximum | 705 | 534 |

Purchasing sessions show higher product-page counts at the reported percentiles, but this is an **association**, not evidence of causation.

## Important chart limitations
- Histogram vertical axes show **raw session counts**; groups have different sample sizes (10,422 versus 1,908).
- The two `bins=40` calls independently divide each group's range, producing **different bin widths**. Therefore bar heights are not directly comparable across panels as rates.
- A better comparison would use **shared bin boundaries** and normalized proportions or densities, with a considered strategy for displaying long tails.

## Analytical thinking
1. **Question:** Are the distributions symmetric?
2. **Evidence:** The observed two-panel histogram and earlier descriptive statistics.
3. **Analysis:** Identify concentration of values and tail direction.
4. **Interpretation:** Strong right skew makes medians and percentiles valuable.
5. **Challenge:** Investigate extreme values; improve comparability before drawing conclusions from bar heights.

## Next experiment (not yet executed)
Create histograms with common bin edges and normalized vertical axes, or use a log-scaled x-axis where appropriate. Compare within-group proportions rather than raw counts.

## Review questions
1. Why do long right tails tend to pull means above medians?
2. Why are the two panels' raw bar heights not directly comparable?
3. Does a high product-page count prove a session will result in a purchase?
