# Slide 02 — Representation, Evaluation and Optimization

## Slide content

**Learning = Representation + Evaluation + Optimization**

| Component | Main question | Examples |
|---|---|---|
| Representation | What models are possible? | Decision trees, logistic regression, neural networks |
| Evaluation | Which candidate is better? | Information gain, likelihood, accuracy |
| Optimization | How do we find a good candidate? | Greedy search, gradient descent |

**Decision tree:** Tree structure (representation) + Information gain (evaluation) + Greedy search (optimization)

## Speaker notes (not displayed on the slide)

Domingos organizes learning algorithms around three choices. Representation defines the hypothesis space: the set of models the learner can express. Evaluation assigns a score to candidates, while optimization searches for a high-scoring candidate. The score used during training need not be the same as the metric used to assess the finished model.

Consider a spam filter. A decision tree could test whether particular words appear in an email. As a small hypothetical example, suppose the learner considers two words. Testing the first produces groups that are almost entirely spam or almost entirely non-spam; testing the second leaves both groups mixed. Information gain favors the first split. Greedy search chooses the best available split now and continues recursively. It does not guarantee the globally best tree.

The important point is that choosing the model type alone is not enough. We must also decide how to score and search for candidate models.

## Visual plan (for later generation; not slide text)

- Main diagram: three equal columns labeled Representation, Evaluation and Optimization, each with its question and one icon. Link them to the same decision-tree learner, rather than implying three mandatory sequential stages.
- Supporting illustration: two candidate binary word splits. For a balanced hypothetical dataset of 10 spam and 10 non-spam emails, split A separates them into (9 spam, 1 non-spam) and (1 spam, 9 non-spam); split B produces (5 spam, 5 non-spam) in each branch. Show counts, not invented performance measurements. Highlight split A as the greedy choice. Information gain is approximately 0.531 bits versus 0 bits.
- Keep the three-component framework dominant; the small split diagram is optional if the slide becomes crowded.

### Original source visual and snapshot instructions

**Preferred original visual — Table 1:** [PDF page 2](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf#page=2), top of page. Crop the table and its title only. Preserve column headings and legible entries; the columns are independent lists, not row-by-row combinations. Use it as the main visual if readable; otherwise keep the simplified three-component diagram and use the original table as a backup. Credit: Domingos (2012), Table 1. **Speaking cue:** Point to the three columns and give the decision-tree combination. 

**Optional original algorithm — Algorithm 1:** [PDF page 2](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf#page=2), right column immediately below Table 1. Crop the boxed pseudocode only. Explain the two stopping conditions, the information-gain choice, and recursion if asked. Credit: Domingos (2012), Algorithm 1.

**Optional supplementary figure — Figure 3:** [PDF page 6](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf#page=6), upper right. It compares decision boundaries that may give similar predictions in regions populated by data. This belongs to Section 9, not Section 2. Reserve it for questions. Credit: Domingos (2012), Figure 3.

## Academic reference

Domingos, P. (2012). *A Few Useful Things to Know about Machine Learning*. Communications of the ACM, 55(10), 78–87. Section 2, Table 1 and Algorithm 1 (PDF pages 1–2, author-hosted version).

[Original article](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf)

The numerical spam example is a teaching illustration, not experimental data from the article.
