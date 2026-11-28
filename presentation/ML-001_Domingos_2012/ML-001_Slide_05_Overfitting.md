# Slide 05 — Overfitting Has Many Faces

## Slide content

- Overfitting: learning accidental patterns rather than reliable relationships.
- Bias: systematic error; variance: sensitivity to the training sample.
- Greater model flexibility does not guarantee better predictions.
- Overfitting can occur even with correct training labels.
- Control complexity with validation and regularization.
- Multiple testing can produce apparently meaningful patterns by chance.

**Key question:** How do we learn useful patterns without memorizing accidental details?

## Speaker notes (not displayed on the slide)

A flexible model may capture patterns that happen to occur in a particular training sample but do not persist in new data. Domingos uses the analogy of throwing darts to explain two sources of error. Imagine the center represents the true relationship, and each dart represents a prediction at the same input from a model trained on a different sample.

If the darts cluster away from the center, there is high bias. If they are scattered widely, there is high variance. Ideally, predictions cluster near the center.

Consider a hypothetical spam filter. A very restrictive model might use just one word and miss many spam messages. A highly flexible tree might create a rule for a rare combination of words that occurred in just a few training emails. That rule may fail on new emails. Even perfectly labeled training examples cannot prevent this problem.

Domingos also compares Naive Bayes and a rule learner in Figure 2. In that experiment, Naive Bayes performs better with small training sets despite its restrictive assumptions. The rule learner overtakes it as more examples become available. This shows why a more expressive model is not automatically the better choice.

We can use cross-validation to select tree complexity and regularization to penalize excessive structure. However, excessive tuning can overfit validation data too. The aim is to balance flexibility and reliability, not simply to make the model as simple as possible.

### Optional discussion — Multiple testing

If a learner tries many candidate rules, some may appear statistically significant purely by chance. This is another way to overfit; adjusting for multiple comparisons or controlling the false discovery rate can help. This point can be discussed if time permits.

## Visual plan (for later generation; not slide text)

### Primary visual — Bias and variance dartboards

Create four identical concentric targets in a 2 × 2 grid, adapted from Figure 1 of the article.

- Columns: Low variance | High variance.
- Rows: High bias | Low bias.
- Top left: tightly clustered darts away from the center.
- Top right: broadly dispersed darts around an off-center location.
- Bottom left: tightly clustered darts near the center.
- Bottom right: broadly dispersed darts centered around the bullseye on average.
- Use the same axis scale, target size and number of darts in every panel. Use cross-shaped markers and emphasize the target center. Label the figure as a conceptual adaptation, not measured results.

### Optional supporting visual — Model flexibility

Create three conceptual classification panels using the same hypothetical two-dimensional sample and class labels. Show a simple boundary that misses the underlying pattern, a suitable boundary, and an excessively complex boundary following isolated points. Label them Underfitting, Appropriate fit, and Overfitting. No invented accuracy values are required. These are teaching illustrations, not original figures from the article.

### Optional research figure — Learning curves

Use the original Figure 2 as the reference: horizontal axis is number of training examples (log scale), vertical axis is test-set accuracy (%). Compare Naive Bayes and C4.5rules. Refer to the published figure rather than inventing numerical data. Curves average 100 runs on synthetic Boolean rule tasks, with error bars of two standard deviations. Do not imply the result holds for all datasets.

## Academic reference

Domingos, P. (2012). *A Few Useful Things to Know about Machine Learning*. Communications of the ACM, 55(10), 78–87. Section 5, Figures 1 and 2 (author-hosted PDF pages 3–4).

[Original article](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf)

The spam-filter scenario and boundary illustration are teaching examples. The dartboard analogy and Naive Bayes comparison come from the article. No purchasing dataset results are included.
