# Slide 03 — Generalization: The Fundamental Goal

## Slide content

- Learning patterns rather than memorizing examples
- Training data versus unseen data
- Independent test set
- Test-set contamination through repeated tuning
- Cross-validation within training data

**Key question:** Can the model predict correctly on examples it has never seen?

## Speaker notes (not displayed on the slide)

A classifier that remembers the training examples can look successful without being useful. Think of a student who memorizes practice questions but cannot solve unfamiliar examination questions. Similarly, a spam filter must recognize new messages rather than just remember old ones.

Suppose a hypothetical classifier correctly labels every one of its training emails but only half of a new group. Another classifier correctly labels three quarters of each group. The second is more useful on this held-out sample, despite its lower training accuracy.

Domingos recommends reserving test examples until the model has been chosen. If we repeatedly change the model based on its test results, the test set loses its independence. Cross-validation provides a way to compare settings using the training portion: we rotate which subset is held out and average the validation scores.

The broader challenge is that the true goal is performance on future data, which we cannot directly optimize during training. A better training score is not necessarily a better future predictor.

## Visual plan (for later generation; not slide text)

- Main diagram: dataset branches into development data (80%) and final test data (20%). Inside development data, show five folds, with one validation fold rotating and the other four used to train. Average the five validation scores, select settings, refit on development data, then evaluate once on the untouched test set. Percentages and fold count are illustrative choices, not requirements from Domingos.
- Optional grouped bar chart: x-axis Model A and Model B; y-axis accuracy (0–100%). Training and held-out accuracy series: A = 100%, 50%; B = 75%, 75%. Label as a hypothetical comparison from the paper's overfitting discussion (Section 5), not experimental measurements. Use consistent colors for training and held-out bars.
- If space is limited, use only the split diagram and explain the numerical comparison orally.

### Original source visual and snapshot instructions

**Original article visual:** No dedicated train/test chart in Section 3. Use the custom split diagram. The 100/50 versus 75/75 accuracy example is in [PDF page 3](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf#page=3), Section 5, right column below Figure 1. If generating the grouped bars, caption them “Illustrative values from Domingos (2012), Section 5; chart created for this presentation.” Do not label them as measured results or as an original article figure.

## Academic reference

Domingos, P. (2012). *A Few Useful Things to Know about Machine Learning*. Communications of the ACM, 55(10), 78–87. Section 3 (PDF page 2); numerical comparison from Section 5 (PDF page 3), author-hosted version.

[Original article](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf)

The student analogy and split diagram are teaching illustrations, not original figures from the article.
