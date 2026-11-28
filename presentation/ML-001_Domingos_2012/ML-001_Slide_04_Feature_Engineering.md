# Slide 04 — Feature Engineering Is the Key

## Slide content

- Transform raw data into informative features.
- Use domain knowledge to construct and select features.
- Consider interactions, not only individual feature relevance.
- Repeat: train → evaluate → refine features.
- Too many candidate features can increase computation and overfitting.

**Example: XOR (exclusive OR)**

| x₁ | x₂ | Class y = XOR(x₁, x₂) |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Takeaway:** Two individually uninformative features may become informative together.

## Speaker notes (not displayed on the slide)

Domingos argues that the way we describe examples can be more important than the choice of learning algorithm. Raw observations are not always suitable inputs. We may need to clean them, transform them, or construct new features using knowledge of the problem.

Consider exclusive OR, or XOR, the example used in Section 8. The class is one when exactly one of the two binary inputs is one. Assume all four combinations occur equally often. If we look only at the first input, half the examples in either group belong to class zero and half to class one. The same happens with the second input. Neither feature alone tells us anything about the class. Yet together they determine it perfectly.

A feature selection method that scores each input separately using information gain could discard both useful inputs. A suitable interaction feature, such as an indicator that the two values differ, makes the relationship easy for a simple classifier to express. This is an illustration of feature construction, not a suggestion to use the unknown target as an input.

Searching every possible feature combination is not necessarily a solution: it can be computationally expensive and increase the risk of overfitting. Feature design therefore requires experimentation, domain knowledge, and reliable validation. Training the model is just one part of that iterative process.

## Visual plan (for later generation; not slide text)

### Primary visual — XOR and feature interactions

- Use two small panels: a two-by-two input grid and a feature transformation.
- Grid axes: horizontal x₁ (0, 1), vertical x₂ (0, 1). Plot four points: (0,0) and (1,1) as class 0; (0,1) and (1,0) as class 1. Use two contrasting colors and distinct marker shapes. Label both classes.
- Show the engineered input z = 1 if x₁ differs from x₂, and 0 otherwise. In the transformed one-dimensional view, both class-0 examples lie at z=0 and both class-1 examples lie at z=1. Separate them with a dashed threshold at z=0.5. Offset overlapping markers slightly or annotate counts of two.
- Caption: Individually uninformative inputs can be useful jointly (balanced XOR example).
- Optional annotations: individual information gains = 0 bits; joint information gain = 1 bit, assuming equal frequency of all four combinations. These are mathematical properties of the example, not measured experimental results.

### Alternative visual — Iterative feature engineering

Raw data → Clean and construct features → Train model → Evaluate → Refine features (feedback arrow to feature construction).

Use only one dominant visual on the slide; the XOR figure is recommended. No invented performance metrics or project-specific dataset results.

### Original source visual and snapshot instructions

**Original article visual:** No dedicated XOR figure. The XOR discussion is on [PDF page 6](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf#page=6), left column, Section 8. Generate the truth table/feature-space illustration from the specifications above. Caption: “Illustration of the XOR example discussed in Domingos (2012), Section 8.” Figure 3 on the same page belongs to Section 9; do not label it as an XOR figure.

## Academic reference

Domingos, P. (2012). *A Few Useful Things to Know about Machine Learning*. Communications of the ACM, 55(10), 78–87. Section 8, author-hosted PDF pages 5–6.

[Original article](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf)

The XOR concept comes from the article. The two-input truth table, balanced-frequency assumption, numerical information gains, and proposed visual are teaching elaborations, not figures or experimental results reproduced from the paper.
