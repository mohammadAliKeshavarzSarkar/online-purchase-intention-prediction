# Lesson 5 — Purchase rates and analytical thinking

**Status:** Experiment executed in GitHub Codespaces; results supplied by researcher.

## Learning objectives
- Distinguish group counts from group rates.
- Calculate a conditional purchase rate.
- Practice an analytical reasoning framework.
- Distinguish observed associations from causal claims.

## Dataset access
Official UCI dataset: https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

Dataset DOI: https://doi.org/10.24432/C5F88Q

Dataset ID in `ucimlrepo`: `468`.

To save a local CSV from the combined DataFrame (`df`) while running the script from the repository root:

```python
from pathlib import Path
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)
df.to_csv(data_folder / "online_shoppers_intention.csv", index=False)
```

The project's Git configuration ignores dataset files in `data/`; check before committing.

## Question
Do returning-visitor sessions have a higher purchase rate than new-visitor sessions?

## Evidence and calculation
Use `VisitorType` to define groups and `Revenue` as the purchase indicator.

`Purchase rate = purchasing sessions in group / total sessions in group × 100`

Executed code:

```python
purchase_rates = df.groupby("VisitorType")["Revenue"].agg(["count", "sum", "mean"])
purchase_rates["purchase_rate_percent"] = purchase_rates["mean"] * 100
print(purchase_rates.round(2))
```

## Actual results from Codespaces
| Visitor type | Sessions | Purchases | Purchase rate |
|---|---:|---:|---:|
| New_Visitor | 1,694 | 422 | 24.91% |
| Other | 85 | 16 | 18.82% |
| Returning_Visitor | 10,551 | 1,470 | 13.93% |

## Interpretation
- Returning visitors contributed more purchases **in total** (1,470 vs. 422).
- New visitors had a higher **within-group purchase rate** (24.91% vs. 13.93%).
- These findings are not contradictory: groups have different sizes.
- The `Other` category has only 85 sessions, so its rate is based on a much smaller sample.

## Analytical thinking framework
1. **Question:** What exactly do we want to know?
2. **Evidence:** Which variables and measurements answer it?
3. **Analysis:** What calculation or chart is appropriate?
4. **Interpretation:** What does the result actually establish?
5. **Challenge:** What confounding factors, biases, timing constraints, or alternative explanations remain?

## Caveats
These are associations within this dataset, not evidence that being a new visitor causes a purchase. Month, traffic source, and other variables may differ between groups. Sessions are not necessarily unique customers. We should not generalize these rates to all online stores.

## Review questions
1. Why can returning visitors have more purchases but a lower purchase rate?
2. Why should we compare rates rather than only raw counts?
3. What variables might explain some of the difference between visitor types?
4. How would you test whether the pattern persists across months?

## Key takeaway
**Counts answer “how many?” Rates answer “what proportion?” Good analysis starts with a clear question and challenges its own interpretation.**
