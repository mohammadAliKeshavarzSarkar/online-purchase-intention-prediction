# ML-001 — Class Presentation Speech

Domingos, P. (2012). *A Few Useful Things to Know about Machine Learning*. Communications of the ACM, 55(10), 78–87.

This is a concise delivery script for the seven existing slides, independent of our purchasing-intention dataset. The individual slide files retain the longer study notes and visual specifications. The examples are either attributed to the article or identified as illustrations.

## Slide 01 — Introduction

Today I am presenting an article by Pedro Domingos, published in 2012, about practical lessons in machine learning.

Instead of manually programming every decision, machine learning uses examples to build models. A spam filter, for instance, can learn from labeled emails to classify unfamiliar messages.

Domingos discusses twelve lessons that help researchers understand what makes learning successful beyond choosing an algorithm. I will focus on five: the components of learning, generalization, feature engineering, overfitting, and the distinction between correlation and causation.

## Slide 02 — Representation, Evaluation and Optimization

Domingos describes learning through three connected components. Representation defines the models we can express. Evaluation tells us which candidate is preferable. Optimization searches for a good candidate.

Consider a decision tree for spam detection. Its representation is a tree of questions about input features. Information gain can score possible splits, and greedy search selects the best available split at each step.

If one word separates spam and normal emails much more clearly than another, information gain favors that split. However, choosing the best immediate split does not guarantee the best possible tree.

The criterion used during learning may also differ from the metric used to evaluate the finished model.

## Slide 03 — Generalization

The fundamental goal is to perform well on unseen examples, not just the training data.

Imagine a student memorizing practice questions without understanding the subject. A classifier can make a similar mistake.

Domingos gives a hypothetical comparison: one classifier achieves 100 percent training accuracy and 50 percent test accuracy, while another achieves 75 percent on both. The second performs better on unseen examples.

We should therefore reserve an independent test set. Cross-validation within the training data helps us compare settings without repeatedly tuning the model using the final test set.

## Slide 04 — Feature Engineering

Domingos emphasizes the importance of designing meaningful inputs. Sometimes improving the features is more valuable than changing the algorithm.

Consider XOR, the exclusive OR function. The output is one when two binary inputs differ and zero when they are equal.

Assuming all four combinations are equally frequent, neither input alone provides information about the class. Together, however, they determine it perfectly.

A method that evaluates features individually could therefore discard both useful inputs. Constructing an interaction feature can make the problem easier to learn.

This is why feature engineering requires domain knowledge, experimentation and careful validation rather than simply generating as many features as possible.

## Slide 05 — Overfitting

A flexible model can capture accidental patterns in the training data rather than relationships that persist.

Domingos uses a dartboard analogy to explain bias and variance. Darts clustered away from the center represent systematic error, or bias. Darts scattered widely represent high variance, meaning predictions are sensitive to the training sample.

A very restrictive classifier may miss important patterns, while a complex tree may memorize rare combinations of words in emails.

Overfitting can occur even with correctly labeled data. Cross-validation and regularization can help control model complexity, but excessive validation tuning can itself overfit. Greater flexibility is not automatically better.

## Slide 06 — Correlation and Causation

Finding an association does not establish a causal relationship.

Domingos discusses the example of beer and diapers being purchased together. A supermarket might hypothesize that placing them next to each other will increase sales, but the association alone cannot establish this effect.

Observational data describes existing behavior. Experimental data allows researchers to investigate the consequences of deliberate changes.

For example, randomly assigning visitors to different website versions and comparing a defined outcome can help estimate the effect of a design change.

Predicting what happens and understanding what happens because of our actions are different tasks.

## Slide 07 — Conclusion

The central lesson of this article is that machine learning is more than selecting an algorithm. It requires meaningful features, appropriate learning methods, reliable evaluation and critical interpretation.

We should ask not only whether a model works, but also why it works, under what conditions it works, and how much confidence we can place in its predictions.

Thank you for your attention.

---

[Original article PDF](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf)

Delivery note: Use the primary visual specified in each slide file. The optional examples and longer technical notes are for preparation and questions; they do not need to be read aloud. Rehearse with the visuals to confirm the actual duration.
