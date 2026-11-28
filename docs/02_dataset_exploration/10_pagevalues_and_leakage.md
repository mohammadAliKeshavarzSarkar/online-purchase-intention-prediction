# Lesson 12 — PageValues and potential data leakage

## Question
Is PageValues associated with purchase outcome, and would it be legitimately available at prediction time?

## Real-world meaning: what is Page Value?

Page Value is a web analytics metric that attributes monetary value to pages associated with conversions. It is not a page count, time spent, or the amount spent by an individual visitor. In legacy Google Analytics, the general formula is (transaction revenue + total goal value) / unique pageviews, with attribution to eligible pages preceding conversions.

### Worked example (hypothetical)

Three customers each visit a shoe product page once. Two buy shoes for $100 each; the third leaves without buying. Assuming no additional goal value, the page's attributed value is ($100 + $0 + $100) / 3 = $66.67 per unique pageview. This does not mean each visitor spends $66.67.

Suppose previously assigned page values are homepage $5, product page $10, and cart $25. A visitor sees all three and leaves without buying. An illustrative session average is (5 + 10 + 25) / 3 = 13.33, while Revenue=False. This explains how nonzero page value and no purchase can coexist.

The UCI dataset describes PageValues as an average page-value measure for pages visited before a transaction. The precise aggregation, attribution window, and whether the current transaction contributed to the recorded value are not established here. The example above is a teaching illustration, not a reconstruction of the dataset's calculation. See the [UCI dataset description](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset).

## What the calculations measure

- Count: number of sessions in each Revenue group.
- Mean: sum of the group's PageValues divided by its session count.
- Median: middle of sorted PageValues (average of the two middle values for an even count).
- Minimum and maximum: smallest and largest recorded PageValues.
- Positive means strictly greater than zero, not a purchase or a favorable outcome. Zero means the recorded metric is zero. The observed minimum is zero in both groups, so there are no negative values.
- Positive percentage: number of PageValues greater than zero divided by the group's session count, multiplied by 100. The expression `(values > 0).mean() * 100` works because True counts as 1 and False as 0.
- Example: [0, 0, 12, 0, 8] gives two positive values out of five, or 40%. This is not a purchase rate.
- In the observed non-purchase group, approximately 88.56% are zero (100 - 11.44). Sorting 10,422 values places both the 5,211th and 5,212th observations among the zeros, explaining the zero median. The purchase group has approximately 19.39% zeros, so its median is positive.
- Pearson correlation with binary Revenue measures association, not purchase probability, model accuracy, or proof of leakage.

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
