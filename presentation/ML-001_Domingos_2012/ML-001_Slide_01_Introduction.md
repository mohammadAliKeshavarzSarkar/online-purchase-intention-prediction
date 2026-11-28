# A Few Useful Things to Know about Machine Learning

**Pedro Domingos | 2012 | University of Washington**  
*Communications of the ACM*

## Slide content

### Machine learning: learning from examples

- Learning from data instead of manually defining every rule
- Classification: predicting a discrete class from input features
- Generalizing to previously unseen examples

### Applications

Web search · Spam filtering · Recommendation systems · Fraud detection

### Purpose of the article

- Present twelve practical lessons in machine learning
- Highlight common pitfalls and important design decisions
- Share practical knowledge beyond standard textbooks

**Central question:** What makes a machine learning system successful beyond choosing an algorithm?

---

## Speaker notes (not displayed on the slide)

Machine learning offers an alternative to writing every rule manually. Instead, we use examples to learn a model that can make predictions about new data.

Domingos illustrates this through classification. Consider a spam filter: the input features can indicate which words appear in an email, while the output is its class, spam or not spam. By learning from previously labeled emails, the classifier aims to correctly classify messages it has never encountered before.

The article brings together twelve lessons from machine learning practice. Its purpose is to explain important considerations and common mistakes that are not always adequately covered in textbooks.

The question guiding this presentation is: what matters beyond selecting an algorithm?

---

## Visual plan (for later generation; not slide text)

**Recommended visual:** A simple left-to-right diagram comparing traditional programming with machine learning.

- Traditional programming: manually written rules + input data → predictions.
- Machine learning (training): labeled examples → learning algorithm → learned classifier.
- Machine learning (prediction): unseen email → learned classifier → Spam / Not spam.

**Design notes:** Use minimal icons for rules, labeled emails, the classifier, and the prediction. Keep training and prediction visually separate. Place the diagram beside the main introduction bullets; avoid decorating it with invented metrics.

**Alternative:** A small grid of application icons (search, email, recommendations, fraud detection) if the comparison diagram is too large.

**Chart requirement:** No quantitative chart is necessary for this introductory slide; the diagram is more informative. This is an illustrative visual plan, not a figure reproduced from the article.

---

**Source:** Domingos, P. (2012). *A Few Useful Things to Know about Machine Learning*. Communications of the ACM, 55(10), 78–87. Abstract and Section 1 (Introduction).

[Author-hosted article PDF](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf)
