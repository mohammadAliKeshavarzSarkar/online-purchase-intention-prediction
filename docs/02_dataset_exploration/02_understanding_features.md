# Lesson 4 — Understanding features and data types

**Status:** Concept lesson introduced; practical feature analysis pending.

## Learning objectives
- Distinguish features from the prediction target.
- Identify numerical, categorical, and Boolean variables.
- Understand why numeric-looking category codes must not automatically be treated as continuous quantities.

## Features and target
A **feature** describes an observation and is used as an input to a predictive model. The **target** is what the model aims to predict.

In our UCI Online Shoppers Purchasing Intention dataset, each row is a shopping session. The 17 input features are conventionally denoted `X`; the target `Revenue` is denoted `y`. `Revenue=True` means the session resulted in a purchase.

## Data types
| Type | Examples from this dataset | Interpretation |
|---|---|---|
| Numerical | `ProductRelated`, `ProductRelated_Duration`, `BounceRates`, `ExitRates` | Counts, durations, or rates |
| Categorical | `Month`, `VisitorType`, `Browser`, `OperatingSystems`, `Region`, `TrafficType` | Labels or category codes |
| Boolean | `Weekend` | True/False indicator |
| Target (Boolean) | `Revenue` | Purchase outcome to predict |

**Important:** `Browser=4` does not imply twice the quantity of `Browser=2`. A column stored as integers may represent categories.

## Why types matter
Preprocessing depends on meaning, not just storage type. Numerical features can often be passed to models directly or scaled. Categorical features may require encoding (such as one-hot encoding). We will implement preprocessing later and avoid learning transformations from test data.

## Hypothetical illustration
Two fictional sessions might have 2 vs. 35 product-page visits and 40 vs. 900 seconds on product pages. These are *teaching examples*, not observations from our executed dataset.

## Practical analysis — next action, not yet executed
Append this code to `src/01_explore_dataset.py` and run it in Codespaces:

```python
print("\nDATA TYPES")
print(df.dtypes)

print("\nVISITOR TYPES")
print(df["VisitorType"].value_counts())

print("\nAVERAGE PRODUCT PAGES BY PURCHASE OUTCOME")
print(df.groupby("Revenue")["ProductRelated"].mean())
```

Run:

```bash
python src/01_explore_dataset.py
```

**Awaiting actual output.** Do not infer whether buyers browse more product pages until the data is examined. Association also does not prove causation.

## Review questions
1. Why is `Revenue` the target rather than an input feature?
2. Why is `OperatingSystems` categorical even if its values are integers?
3. Which type is `Weekend`?
4. What would comparing the mean `ProductRelated` by `Revenue` tell us, and what would it not prove?

## Key takeaway
**A feature's meaning determines its type; the way it is stored in a CSV or DataFrame does not always tell the whole story.**

## Actual experiment results — Codespaces

The researcher ran the feature inspection script and reported these results:

- `ProductRelated`: `int64`; `BounceRates`: `float64`; `Month` and `VisitorType`: `str`; `Weekend` and `Revenue`: `bool`. `OperatingSystems` is stored as `int64` but semantically categorical.
- Visitor types: Returning_Visitor **10,551**; New_Visitor **1,694**; Other **85**.
- Mean `ProductRelated` for `Revenue=False`: **28.714642**.
- Mean `ProductRelated` for `Revenue=True`: **48.210168**.

Purchase sessions averaged **19.50 more product-page visits**, about **67.9% more** relative to non-purchase sessions. This is an association, not proof of causality or early-session predictive availability. Means may be influenced by outliers.

**Next question (not yet tested):** How does the purchase rate differ by visitor type?
