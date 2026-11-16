# Lesson 2 — Precision, recall, and F1-score

**Status:** Completed concept lesson

## Learning objectives
- Distinguish precision from recall.
- Interpret true positives (TP), false positives (FP), and false negatives (FN).
- Calculate F1-score.

## Intuition: spam detection
Imagine 100 emails, of which 20 are truly spam. A detector catches 15 actual spam messages, misses 5, and wrongly flags 5 normal messages.

- **Recall:** Of all actual spam emails, how many did we catch? `15 / (15 + 5) = 75%`.
- **Precision:** Of all emails flagged as spam, how many really were spam? `15 / (15 + 5) = 75%`.

The denominators refer to different groups, even though they happen to be equal in this example.

## Formulas
- `Recall = TP / (TP + FN)`
- `Precision = TP / (TP + FP)`
- `F1 = 2 × Precision × Recall / (Precision + Recall)`

For precision 60% and recall 75%:

`F1 = 2 × 0.60 × 0.75 / (0.60 + 0.75) ≈ 0.667`

The harmonic mean penalizes extreme imbalance between precision and recall. F1 does not directly incorporate true negatives.

## Application to this project
Here, the positive class is **purchase**:
- Recall: What proportion of actual purchasing sessions did we identify?
- Precision: What proportion of predicted purchasing sessions really purchased?

Both are relevant because only about 15.5% of observed sessions resulted in purchases.

## Review
1. A detector finds all 20 spam emails but flags 30 normal emails too. What are recall and precision?
2. What changes when false positives increase but true positives and false negatives stay fixed?
3. Why might F1 be preferable to accuracy on an imbalanced dataset?

## Takeaway
**Recall starts from actual positives; precision starts from predicted positives.**
