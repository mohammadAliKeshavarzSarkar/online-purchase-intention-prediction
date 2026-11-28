# Slide 06 — Correlation Does Not Imply Causation

## Slide content

- Statistical association versus causal relationships
- Prediction versus intervention
- Observational and experimental data
- Confounding variables
- Controlled experiments and A/B testing

**Key question:** If two variables are related, does changing one necessarily affect the other?

## Speaker notes (not displayed on the slide)

One important limitation of machine learning is that discovering a statistical relationship does not necessarily explain why that relationship exists.

Domingos introduces this problem using a famous data mining example involving beer and diapers in a supermarket. Suppose transaction records show that customers frequently purchase these products together. A manager might hypothesize that placing them next to each other would increase sales. However, the association alone does not establish that the change will increase sales.

This introduces the difference between observational and experimental data. Observational data records existing behavior, whereas experimental data allows researchers to manipulate a condition and measure its effect. Domingos also emphasizes that associations can guide further investigation. Certain methods can infer causal information from observational data under restrictive conditions; ordinary predictive learning alone does not establish a causal effect.

Ultimately, predicting what will happen and determining what will happen because of our actions are two different problems.

### Additional speaking example (teaching illustration)

Imagine that ice cream sales and swimming activity increase together. Hot weather could influence both, without ice cream purchases causing swimming. This is a possible common-cause explanation, not a measured finding. A confounding variable can make an observed association misleading as evidence of a causal effect.

### Controlled experiment (article's website example, elaborated)

Randomly assign visitors to two website versions. Group A sees the original design, and group B sees a modified design. Define the outcome before the experiment, such as the purchase rate, and compare it between groups. With valid random assignment, consistent measurement and appropriate analysis, the difference can help estimate the effect of the design change. No actual experimental results are claimed.

## Visual plan (for later generation; not slide text)

### Primary visual — Supermarket association versus intervention

- Show beer and diapers as two simple product icons with an undirected connection labeled “Frequently purchased together”.
- Below, show a proposed change: place the products next to each other.
- End with a question: “Will sales increase?” Use a question mark and label “Further evidence needed”. Do not draw a proven causal arrow between the products.
- Caption: An observed association can motivate an experiment; it does not establish its outcome.
- No numerical chart or invented sales figures. The article discusses this familiar example without reporting transaction counts or experimental measurements.

### Alternative visual — Common cause

- Draw three nodes: Hot weather (top), Ice cream sales (bottom left), Swimming activity (bottom right).
- Draw directed arrows from Hot weather to each bottom node. Connect the bottom nodes with a dashed undirected line labeled “Observed association”.
- Caption: Hypothetical common-cause explanation; not an example from the article.

### Alternative visual — Randomized website experiment

- Show Website visitors → Random assignment → Group A: original website / Group B: modified website → Compare measured outcomes.
- Use two equally sized branches to convey random assignment, not a required numerical allocation.
- Label the outcome as an example, such as purchase rate. Do not display fabricated results. State that a valid experiment is necessary for causal interpretation.
- Keep one dominant diagram on the slide. The supermarket example is recommended; discuss the other examples orally if time allows.

### Original source visual and snapshot instructions

**Original article visual:** No dedicated causal diagram in Section 13. The beer-and-diapers example is on [PDF page 8](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf#page=8), lower left; the randomized website example continues at upper right. Generate the primary supermarket diagram, crediting Domingos (2012), Section 13 as its conceptual source. No sales figures or causal outcomes are supplied by the article.

## Academic reference

Domingos, P. (2012). *A Few Useful Things to Know about Machine Learning*. Communications of the ACM, 55(10), 78–87. Section 13, page 8 of the author-hosted nine-page PDF.

[Original article](https://homes.cs.washington.edu/~pedrod/papers/cacm12o.pdf)

The supermarket example and randomized website assignment come from Section 13. The common-cause illustration and experimental design details are teaching elaborations. No purchasing-intention project data or experimental findings are included.
