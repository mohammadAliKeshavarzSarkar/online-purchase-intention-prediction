# Lesson 11 — Training and testing split

**Status:** Executed successfully in the researcher's GitHub Codespaces virtual environment; output supplied by the researcher.

## Research question
How should we reserve unseen observations to evaluate a future classifier, while preserving the dataset's imbalanced target distribution?

## Experiment code
```python
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split

dataset = fetch_ucirepo(id=468)
X = dataset.data.features
y = dataset.data.targets["Revenue"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("TRAINING AND TESTING SETS")
print("\nTraining features:", X_train.shape)
print("Testing features:", X_test.shape)
print("\nTraining target distribution:")
print(y_train.value_counts())
print(y_train.value_counts(normalize=True) * 100)
print("\nTesting target distribution:")
print(y_test.value_counts())
print(y_test.value_counts(normalize=True) * 100)
```

## Actual output
- Training features: **(9864, 17)**
- Testing features: **(2466, 17)**
- Training targets: False **8,338** (84.529603%); True **1,526** (15.470397%).
- Testing targets: False **2,084** (84.509327%); True **382** (15.490673%).

Total observations: 9,864 + 2,466 = **12,330**.

## Interpretation
- The split is 80% training and 20% testing.
- The target proportions are very similar in the two partitions and closely match the original dataset's proportions.
- `stratify=y` preserves the class distribution approximately across the partitions. Small differences occur because observations are indivisible.
- `random_state=42` makes the split reproducible with the same data and library behavior; 42 is a seed, not a sample count.
- No classifier has been trained yet. This experiment only creates the partitions.

## Important methodological rules
- Fit learned preprocessing steps (for example, imputers, scalers, and encoders) on the training data only; apply the fitted transformations to the test data.
- Do not use the test set to select features, tune hyperparameters, or make modeling decisions. Use training data and, where appropriate, cross-validation for those tasks.
- Inspect feature availability and potential target leakage before model training. A stratified split does not itself prevent leakage.
- Keep the test set as a final, held-out evaluation.

## Next
Investigate feature meaning, prediction timing, and potential target leakage—especially whether each feature would genuinely be available when the intended prediction is made.
