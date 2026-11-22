# Lesson 10 — Normalized histograms with shared bins

## Research question
How do product-related page-visit distributions differ between purchasing and non-purchasing sessions when we compare percentages rather than raw counts?

## Why normalization?
The UCI dataset has 10,422 non-purchasing sessions and 1,908 purchasing sessions. Raw histogram heights are affected by this imbalance. The previous two-panel histogram also used independently determined bin boundaries, complicating comparison.

## Reproducible experiment
Append after the Lesson 9 code in `src/01_explore_dataset.py`, where `no_purchase`, `purchase`, `figures_dir`, and `plt` are already defined:

```python
import numpy as np

bins = np.arange(0, 211, 10)
no_purchase_weights = np.ones(len(no_purchase)) * 100 / len(no_purchase)
purchase_weights = np.ones(len(purchase)) * 100 / len(purchase)

fig, ax = plt.subplots(figsize=(11, 5))
ax.hist(no_purchase, bins=bins, weights=no_purchase_weights,
        alpha=0.6, label="No Purchase", color="steelblue")
ax.hist(purchase, bins=bins, weights=purchase_weights,
        alpha=0.6, label="Purchase", color="darkorange")
ax.set_title("Product Page Visits by Purchase Outcome")
ax.set_xlabel("Product Pages Visited")
ax.set_ylabel("Percentage of Sessions")
ax.legend()
plt.tight_layout()
output_path = figures_dir / "product_pages_normalized.png"
plt.savefig(output_path, dpi=150)
plt.close(fig)
print(f"Normalized histogram saved to: {output_path}")
```

Run: `python src/01_explore_dataset.py`.

## Observed output
The learner ran the experiment and shared the generated plot titled **Product Page Visits by Purchase Outcome**. Both groups were shown on one set of axes with shared 10-page bins, overlapping blue (no purchase) and orange (purchase) bars, and a percentage y-axis.

- The 0–10 page bin was approximately **35%** of non-purchasing sessions versus **12%** of purchasing sessions (visual estimates, not exact computed bin counts).
- Purchasing sessions had higher percentages in several moderate and higher page-count bins, notably around 20–40 pages.
- The distributions overlap substantially: page count alone cannot perfectly classify purchases.
- Both groups have long right tails.

These visual observations agree with earlier descriptive results: no-purchase mean/median **28.71/16**, purchase mean/median **48.21/29**.

## Interpretation and limitations
Each bar's height is a percentage **of its entire outcome group**, not of only the sessions displayed. Bins run from 0 through 210, so values above 210 are omitted from the plot but retained in the data. The visible bars therefore need not sum to 100% per group. Overlap is expected, and association does not establish causation. The plot is exploratory evidence, not model performance or proof that extra browsing causes purchases.

## Next
Review feature roles and potential leakage, then introduce stratified train/test splitting and preprocessing without using the test set to fit transformations.
