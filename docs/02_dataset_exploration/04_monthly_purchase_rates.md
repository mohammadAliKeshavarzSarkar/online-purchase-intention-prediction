# Lesson 6 — Monthly purchase rates by visitor type

**Status:** Experiment completed in GitHub Codespaces; actual terminal output provided by researcher.

## Research question
Does the new-versus-returning visitor purchase-rate difference persist within months?

## Analytical thinking
1. **Question:** Does visitor-type association with purchases remain when comparing sessions in the same month?
2. **Evidence:** `Month`, `VisitorType`, `Revenue`.
3. **Analysis:** Group by month and visitor type; count sessions and purchases; compute purchase rates.
4. **Interpretation:** Compare within-month rates, considering denominators.
5. **Challenge:** Small samples, seasonality, unobserved confounding, and absence of causal identification.

## Code executed
```python
monthly_rates = (
    df.groupby(["Month", "VisitorType"])["Revenue"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)
monthly_rates["purchase_rate_percent"] = monthly_rates["mean"] * 100
print(monthly_rates[["Month", "VisitorType", "count", "sum", "purchase_rate_percent"]].round(2).to_string(index=False))
```

## Actual output (purchase rates in %)
| Month | Visitor type | Sessions | Purchases | Purchase rate |
|---|---|---:|---:|---:|
| Aug | New_Visitor | 72 | 21 | 29.17 |
| Aug | Returning_Visitor | 361 | 55 | 15.24 |
| Dec | New_Visitor | 335 | 75 | 22.39 |
| Dec | Other | 62 | 13 | 20.97 |
| Dec | Returning_Visitor | 1330 | 128 | 9.62 |
| Feb | New_Visitor | 1 | 0 | 0.00 |
| Feb | Returning_Visitor | 183 | 3 | 1.64 |
| Jul | New_Visitor | 54 | 11 | 20.37 |
| Jul | Returning_Visitor | 378 | 55 | 14.55 |
| June | New_Visitor | 30 | 7 | 23.33 |
| June | Other | 1 | 0 | 0.00 |
| June | Returning_Visitor | 257 | 22 | 8.56 |
| Mar | New_Visitor | 232 | 36 | 15.52 |
| Mar | Returning_Visitor | 1675 | 156 | 9.31 |
| May | New_Visitor | 319 | 88 | 27.59 |
| May | Returning_Visitor | 3045 | 277 | 9.10 |
| Nov | New_Visitor | 419 | 128 | 30.55 |
| Nov | Other | 22 | 3 | 13.64 |
| Nov | Returning_Visitor | 2557 | 629 | 24.60 |
| Oct | New_Visitor | 124 | 28 | 22.58 |
| Oct | Returning_Visitor | 425 | 87 | 20.47 |
| Sep | New_Visitor | 108 | 28 | 25.93 |
| Sep | Returning_Visitor | 340 | 58 | 17.06 |

## Findings
- New-visitor sessions had a higher observed purchase rate in **9 of 10** represented months; February was the exception.
- **February new visitors:** 0 purchases from **1 session**; this 0% rate is extremely unstable and should not be interpreted as evidence of a general pattern.
- **May:** 27.59% new vs. 9.10% returning.
- **October:** 22.58% new vs. 20.47% returning.
- **November:** 30.55% new vs. 24.60% returning; returning visitor rate is substantially higher than in May.
- January and April are not represented in the supplied output.

## Interpretation and limitations
These are **descriptive associations** from complete shopping sessions. Grouping by month is an exploratory check, not proof of confounding or causality. Differences in traffic source, promotions, visitor intent, and other factors may matter. A session is not necessarily a unique customer. Some month-category combinations have very small samples.

## Review questions
1. Why is a 0% rate from one session weak evidence?
2. How do counts and rates tell different stories?
3. Which month shows a relatively small gap between new and returning visitor rates?
4. What additional factors could help explain these patterns?

## Key takeaway
**Always check the denominator behind a percentage, and challenge whether a pattern remains consistent across relevant groups.**
