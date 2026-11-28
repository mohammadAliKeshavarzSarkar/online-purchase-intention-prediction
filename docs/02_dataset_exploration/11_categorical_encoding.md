# Lesson 13 — Categorical encoding

**Status:** Training-category inspection and one-hot transformation completed.

## Concept and real-world meaning

Numerical features measure quantities, such as number of product pages or browsing duration. Categorical features describe identities or groups. Integer storage does not make a category a measurable quantity: browser code 4 is not twice browser code 2, and the original browser names are not established by this inspection.

Month describes the calendar month, VisitorType describes new/returning/other visitors, Browser and OperatingSystems identify software categories, Region identifies geographic categories, TrafficType identifies traffic-source categories, and Weekend indicates whether a session occurred on a weekend.

## Research question

How should nominal and binary features be represented numerically without imposing a fictitious ordering, and how many columns will the transformation create?

## One-hot encoding: worked example (hypothetical)

Each binary column asks whether the current session belongs to its corresponding category.

| VisitorType | New | Returning | Other |
|---|---:|---:|---:|
| New_Visitor | 1 | 0 | 0 |
| Returning_Visitor | 0 | 1 | 0 |
| Other | 0 | 0 | 1 |

Zero means this session is not a member of that category, not that the category is unimportant or that the customer did not buy. One indicates membership. All columns together represent the original category. For known, single-label categories with full encoding, exactly one column is active within each original feature. With unknown-category handling set to ignore, an unseen category instead produces an all-zero block. Multiple original categorical features each have their own block. Revenue is the separate purchase target and must not enter X.

## Executed training-data inspection

The researcher appended this code to src/02_prepare_data.py and supplied the terminal output:

```python
categorical_features = [
    "Month", "VisitorType", "Browser", "OperatingSystems",
    "Region", "TrafficType", "Weekend"
]
print("\nCATEGORICAL FEATURE ANALYSIS")
for feature in categorical_features:
    print(f"\nFeature: {feature}")
    print("Data type:", X_train[feature].dtype)
    print("Number of unique categories:", X_train[feature].nunique())
    print("Unique categories:", X_train[feature].unique())
    print("Category distribution:")
    print(X_train[feature].value_counts())
```

dtype describes storage, nunique counts distinct categories, unique lists their labels, and value_counts counts training sessions per category. Inspect training data to avoid using the test set to design preprocessing.

## Observed results

Training shape (9864, 17); test shape (2466, 17). The supplied output reports:

| Feature | dtype | Categories | Counts (label: count) |
|---|---|---:|---|
| Month | str | 10 | May: 2703; Nov: 2360; Mar: 1538; Dec: 1391; Oct: 444; Sep: 368; Jul: 344; Aug: 342; June: 228; Feb: 146 |
| VisitorType | str | 3 | Returning_Visitor: 8443; New_Visitor: 1347; Other: 74 |
| Browser | int64 | 13 | 2: 6361; 1: 1959; 4: 596; 5: 382; 6: 140; 10: 135; 8: 107; 3: 83; 13: 52; 7: 36; 12: 7; 11: 5; 9: 1 |
| OperatingSystems | int64 | 8 | 2: 5275; 1: 2063; 3: 2050; 4: 383; 8: 67; 6: 17; 5: 5; 7: 4 |
| Region | int64 | 9 | 1: 3782; 3: 1951; 4: 937; 2: 924; 6: 643; 7: 606; 9: 413; 8: 337; 5: 271 |
| TrafficType | int64 | 20 | 2: 3135; 1: 1934; 3: 1654; 4: 866; 13: 581; 10: 370; 6: 350; 8: 268; 5: 215; 11: 195; 20: 156; 7: 35; 9: 33; 15: 33; 19: 13; 14: 12; 18: 9; 16: 3; 12: 1; 17: 1 |
| Weekend | bool | 2 | False: 7578; True: 2286 |

## Expected dimensionality (calculated before transformation)

Full one-hot encoding of all seven gives 10 + 3 + 13 + 8 + 9 + 20 + 2 = 65 columns; adding 10 numerical features gives 75. Our proposed approach uses one column for Weekend (False=0, True=1) and full encoding for the other six: 63 encoded columns + 10 numerical + 1 binary = 74 total. Rows stay unchanged. Encoding does not add new raw information.

## Interpretation and limitations

Browser 9 and TrafficType 12 and 17 each occur in only one training session. Such rare categories provide limited learning evidence and may be absent from individual cross-validation training folds. Keep them for the initial benchmark; do not infer usefulness from frequency alone. Category names for integer codes are not known. One-hot encoding does not guarantee improved accuracy. Fit the encoder only on training data, and within each training fold for cross-validation. Use handle_unknown="ignore" to accommodate unseen categories. The full training split's category count is not guaranteed to match each fold.

## Executed one-hot transformation

The researcher ran the following continuation of `src/02_prepare_data.py` in Codespaces and supplied the terminal output.

```python
from sklearn.preprocessing import OneHotEncoder

one_hot_features = [
    "Month", "VisitorType", "Browser",
    "OperatingSystems", "Region", "TrafficType"
]
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
X_train_encoded = encoder.fit_transform(X_train[one_hot_features])
X_test_encoded = encoder.transform(X_test[one_hot_features])
encoded_feature_names = encoder.get_feature_names_out(one_hot_features)

print("\nONE-HOT ENCODING RESULTS")
print("Training shape:", X_train_encoded.shape)
print("Testing shape:", X_test_encoded.shape)
print("\nEncoded feature names:")
print(encoded_feature_names)

encoded_df = pd.DataFrame(
    X_train_encoded,
    columns=encoded_feature_names,
    index=X_train.index
)
print("\nVISITOR TYPE — BEFORE AND AFTER ENCODING")
visitor_comparison = pd.concat([
    X_train[["VisitorType"]],
    encoded_df[[
        "VisitorType_New_Visitor",
        "VisitorType_Other",
        "VisitorType_Returning_Visitor"
    ]]
], axis=1)
print(visitor_comparison.head(10).to_string())
```

### Why these operations?

- fit_transform learns category identities from training data and applies the learned mapping.
- transform applies that same mapping to testing observations without learning new rules.
- handle_unknown="ignore" gives an all-zero block for an unseen category rather than raising an error.
- sparse_output=False returns a dense array for this small teaching experiment; the default numeric output is floating-point.
- get_feature_names_out preserves the meaning of each generated column.
- index=X_train.index preserves row identities for the side-by-side pandas concatenation.

### Observed output (2026-11-28)

| Block | Predicted shape | Observed shape |
|---|---|---|
| Training | (9864, 63) | (9864, 63) |
| Testing | (2466, 63) | (2466, 63) |

The 63 named columns comprise 10 Month, 3 VisitorType, 13 Browser, 8 OperatingSystems, 9 Region, and 20 TrafficType indicators.

Actual first ten training observations (shortened indicator names for readability):

| Original index | VisitorType | New | Other | Returning |
|---:|---|---:|---:|---:|
| 4263 | Returning_Visitor | 0.0 | 0.0 | 1.0 |
| 5905 | Returning_Visitor | 0.0 | 0.0 | 1.0 |
| 9434 | Returning_Visitor | 0.0 | 0.0 | 1.0 |
| 3505 | Returning_Visitor | 0.0 | 0.0 | 1.0 |
| 2067 | Returning_Visitor | 0.0 | 0.0 | 1.0 |
| 10113 | Returning_Visitor | 0.0 | 0.0 | 1.0 |
| 9335 | New_Visitor | 1.0 | 0.0 | 0.0 |
| 1868 | New_Visitor | 1.0 | 0.0 | 0.0 |
| 4322 | New_Visitor | 1.0 | 0.0 | 0.0 |
| 265 | Returning_Visitor | 0.0 | 0.0 | 1.0 |

The displayed examples confirm the category-membership interpretation. A row with known categories across all six features has six ones and 57 zeros, not just one active value across the whole row. This follows from the encoding rules; a dataset-wide row-sum check was not executed in the reported output.

## Completion and next step

The six-feature categorical transformation succeeded and matched the predicted dimensionality. Weekend and ten numerical features are not yet combined with the encoded block; the planned 74-column complete representation remains an expectation. No classifier has been trained, and these results do not establish predictive performance. The next lesson introduces numerical feature scaling, followed by a unified preprocessing pipeline. Any later cross-validation must fit preprocessing separately inside each training fold.
