# Lesson 12 — PageValues and potential data leakage

## Question
Is PageValues associated with purchase outcome, and would it be legitimately available at prediction time?

## Executed experiment
The researcher appended the following analysis to `src/02_prepare_data.py` and supplied the terminal output.

```python
analysis_df = X.copy()
analysis_df['Revenue'] = y
print(analysis_df.groupby('Revenue')['PageValues'].agg(['count', 'mean', 'median', 'min', 'max']).round(3))
print(analysis_df.groupby('Revenue')['PageValues'].apply(lambda values: (values > 0).mean() * 100).round(2))
print(analysis_df['PageValues'].corr(analysis_df['Revenue'].astype(int)))
```

## Observed results

| Revenue | Count | Mean | Median | Min | Max | Positive PageValues (%) |
|---|---:|---:|---:|---:|---:|---:|
| False | 10422 | 1.976 | 0.000 | 0.0 | 246.759 | 11.44 |
| True | 1908 | 27.265 | 16.758 | 0.0 | 361.764 | 80.61 |

Pearson (point-biserial) correlation: **0.4925692952512103**. Mean ratio approximately 13.8; positive-value proportion difference 69.17 percentage points. Association is not causation or proof of leakage.

## Interpretation and limitations
PageValues may be legitimately predictive if calculated from historical information available at prediction time, but may leak the outcome if calculated using the current transaction. Its exact construction is not established by this experiment. The dataset contains session aggregates, so early-session prediction is not established. The exploratory analysis used all rows, including the test partition; this limits claims of independent validation. Avoid further test-driven feature selection or tuning. Fit transformations and feature selection inside training folds.

## Proposed modeling comparison (not yet executed)
Compare the 17-feature benchmark with a 16-feature configuration excluding PageValues, using identical training cross-validation conditions. Treat this as a sensitivity/ablation study, not proof of leakage or a guarantee that the remaining features are safe. Report both configurations transparently and avoid selecting the winner using test results.

## Next
Identify categorical and numerical feature roles and introduce encoding.
