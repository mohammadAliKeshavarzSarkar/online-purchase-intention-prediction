# Lesson 3 — Loading and validating the UCI dataset

**Status:** Executed successfully in GitHub Codespaces (reported by the researcher, November 2026)

## Learning objectives
- Retrieve a public dataset programmatically.
- Inspect dimensions, columns, class counts and missing values.
- Separate observed results from interpretations.

## Environment
- GitHub Codespaces, default image
- Python 3.14.2
- pip 26.2.2
- Installed successfully: `pandas==3.1.1`, `ucimlrepo==0.0.7` (and `numpy==2.5.5` as a dependency)

## Data source
UCI Online Shoppers Purchasing Intention Dataset, dataset ID **468**.

Official source: https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

Dataset DOI: https://doi.org/10.24432/C5F88Q

## Code executed
```python
import pandas as pd
from ucimlrepo import fetch_ucirepo

dataset = fetch_ucirepo(id=468)
X = dataset.data.features
y = dataset.data.targets
df = pd.concat([X, y], axis=1)

print(df.shape)
print(df.columns.tolist())
print(df.head().to_string())
print(df["Revenue"].value_counts())
print(df.isnull().sum())
```

Run from the repository root using `python src/01_explore_dataset.py`.

## Actual output (reported from Codespaces)
- Shape: **(12330, 18)** — 17 input columns and one target.
- Columns: `Administrative`, `Administrative_Duration`, `Informational`, `Informational_Duration`, `ProductRelated`, `ProductRelated_Duration`, `BounceRates`, `ExitRates`, `PageValues`, `SpecialDay`, `Month`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`, `VisitorType`, `Weekend`, `Revenue`.
- Target counts: `False=10422`; `True=1908`.
- Missing values: **zero reported for every column**.

The initial terminal command errors were caused by repeated commands being pasted together; corrected commands ran successfully.

## Interpretation
The target is imbalanced, so accuracy by itself is not a sufficient measure of purchase detection.

**Important limitation:** Features summarize completed shopping sessions. We must not claim that every feature would be available for early, real-time prediction. In particular, we will inspect the interpretation and potential timing implications of `PageValues`.

## Next lesson (not yet executed)
Identify numerical, categorical and Boolean features, then compare `ProductRelated` across purchase outcomes.

## Review
1. Why does `(12330, 18)` not mean 18 input features?
2. What does `Revenue=True` represent?
3. What can we conclude from zero missing values, and what can we *not* conclude?

## Takeaway
We have verified that the dataset loads successfully and confirmed its structure and class imbalance; model training has not yet begun.
