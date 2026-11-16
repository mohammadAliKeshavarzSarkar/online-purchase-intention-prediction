# Lesson 1 — Classification, imbalance, and baselines

**Status:** Completed concept lesson  
**Project:** Online purchase intention prediction

## Learning objectives
- Explain binary classification and the target variable.
- Identify an imbalanced target distribution.
- Understand why accuracy alone can mislead.

## Concepts
**Binary classification** predicts one of two classes. In our project, `Revenue=True` means a shopping session resulted in a purchase; `Revenue=False` means it did not.

**Class imbalance** occurs when one outcome is substantially more common than the other.

**Accuracy** is the fraction of all predictions that are correct:

`Accuracy = (TP + TN) / (TP + TN + FP + FN)`

A **majority-class baseline** always predicts the most frequent class. It provides a minimum comparison point, not necessarily a useful model.

## Teaching example (hypothetical)
Suppose 1,000 sessions contain 850 non-purchases and 150 purchases. A model that predicts *No Purchase* for every session has 85% accuracy but finds zero buyers.

## Actual project observation
The UCI dataset loaded in GitHub Codespaces contained:
- 12,330 shopping sessions
- 10,422 sessions with `Revenue=False`
- 1,908 sessions with `Revenue=True`

Therefore, a majority-class predictor would have approximately **84.5% accuracy on this complete dataset**. This is a calculated baseline, **not** a trained or evaluated model result.

## Research implication
We will not select models by accuracy alone. We will assess precision, recall, F1-score and additional metrics using held-out evaluation data.

## Review
1. What does each row represent?
2. Why is 84.5% accuracy insufficient evidence of good purchase prediction?
3. What is the positive class in this study?

## Takeaway
A seemingly high accuracy can conceal a model that never identifies the minority class.
