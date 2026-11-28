# Lesson 7 — Mean, median, spread, and possible outliers

**Status:** Experiment executed successfully in GitHub Codespaces; output supplied by researcher.

## Research question
Do average product-page visits accurately describe a typical purchasing or non-purchasing session?

## Concepts
- **Mean:** arithmetic average; sensitive to unusually large or small values.
- **Median:** middle value of sorted observations; resistant to extreme values.
- **Minimum and maximum:** smallest and largest observed values.
- **Standard deviation (`std`):** absolute spread of observations around the mean.
- **Outlier:** an unusually extreme observation, which is not necessarily erroneous.

### Teaching example (hypothetical)
Product-page counts `[2, 3, 4, 5, 100]` have mean `22.8` and median `4`. The large value increases the mean.

## Code executed
```python
print("\nPRODUCT PAGE VISITS — SUMMARY STATISTICS")
product_stats = (
    df.groupby("Revenue")["ProductRelated"]
    .agg(["count", "mean", "median", "min", "max", "std"])
)
print(product_stats.round(2))
```

## Actual results
| Revenue | Count | Mean | Median | Min | Max | Std |
|---|---:|---:|---:|---:|---:|---:|
| False | 10422 | 28.71 | 16.0 | 0 | 705 | 40.74 |
| True | 1908 | 48.21 | 29.0 | 0 | 534 | 58.27 |

## Interpretation
- In both groups, **mean exceeds median**, consistent with a right-skewed distribution; a histogram or boxplot can help inspect shape.
- Purchasing sessions have a higher mean (**48.21 vs. 28.71**) and median (**29 vs. 16**) number of product-page visits.
- The highest individual product-page count (**705**) occurred in the non-purchase group, even though that group has the lower mean.
- Purchasing sessions have a larger **absolute** standard deviation (**58.27 vs. 40.74**). This alone does not establish greater *relative* variability.
- Extreme values are not automatically mistakes and should not be removed without a justified rule.

## Analytical thinking framework
1. **Question:** Does the mean describe a typical session?
2. **Evidence:** Product-page counts and purchase outcome.
3. **Analysis:** Compare mean, median, min, max, and standard deviation within each group.
4. **Interpretation:** Differences between mean and median suggest possible skew.
5. **Challenge:** Examine distribution shape, long tails, and whether observations are valid. Avoid causal claims.

## Next step (not yet executed)
Visualize distributions or calculate quantiles (e.g., 25th, 50th, 75th, and 95th percentiles) before deciding how to handle unusually high page counts.

## Review questions
1. Why is the mean higher than the median in both groups?
2. Does a maximum of 705 imply a data error?
3. Can a group have a higher mean while another group has the largest individual value?
4. What does a standard deviation of 58.27 describe?

## Key takeaway
**Compare mean and median before deciding what a typical observation looks like. Extreme observations deserve investigation, not automatic deletion.**
