---
title: "PyData Global 2026"
event_type: conference
location: "Virtual"
start_date: 2026-12-09
end_date: 2026-12-10
image: pydata-global-2026.jpg
website: https://pydata.org/global2026/
description: "PyData Global 2026 is a 2-day virtual event for the international community of data scientists, data engineers, and developers of data analysis tools to share ideas and learn from each other."
people:
  - Emil Hvitfeldt
  - Isabella Velásquez
  - Rich Iannone
software:
  - Great Tables
languages:
- Python
---

We are honored to sponsor PyData Global and engage with the vibrant Python data community! Our team has several great talks lined up. Check out where you can find us below:

Emil Hvitfeldt will give a talk on "Preprocessing as a Contract: Selecting Columns by Role, Type, and Provenance."

<details><summary>Read the abstract here.</summary>
Every preprocessing pipeline eventually contains a literal list of column names, and that list is the quietest bug in your codebase. It is a copy of the schema that drifts the moment someone adds a column upstream: the new feature is silently never imputed, never scaled, and the model trains anyway. It cannot name the columns your own steps create, because one-hot encoding produces however many indicators the training split happened to contain. It cannot express "whatever survived the variance filter", which differs by construction between cross-validation folds.

This talk works through a mixed-type housing dataset where the requirements are ordinary and the scikit-learn solution is not: impute, one-hot encode, run PCA over the dummies plus a subset of the numerics, then normalize everything numeric including the new components. In ColumnTransformer that becomes nested transformers, three hand-maintained column lists, and a step that is simply not expressible. We then rebuild it with a new open source library, as a flat sequence of steps that select columns by role, type, and provenance against a schema that updates after every step.

You will leave able to spot which of your pipelines are one upstream column away from a silent bug, and with a vocabulary for fixing them.
</details>

Rich Iannone will give a talk on “How Your Docs Are Already Your API: Making Python Libraries AI-Readable."

<details><summary>Read the abstract here.</summary>
AI coding agents are the fastest-growing consumers of your library's docs. However, most Python packages make them work far too hard to use documentation effectively. Indeed an agent can likely find your docs, but it has to: (1) scrape rendered HTML, (2) guess at page structure, (3) use extra tokens dealing with navigational elements, and (4) still piece together how your API fits together from those collected fragments. The risk here is hallucinated parameters, incorrect understanding of API patterns, and the generation of code that's of lower quality.
</details>
