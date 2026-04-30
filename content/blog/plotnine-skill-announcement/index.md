---
title: A Plotnine Skill for AI Coding Agents
date: 2026-04-30T00:00:00.000Z
people:
  - Hassan Kibirige
description: >
  An installable skill that helps coding Agents produce consistent, runnable
  plotnine code. It is usable from any Agent that supports the Agent Skills
  standard.
image: hero.jpg
image-alt: >-
  The plotnine hex logo on the left — a UFO over a starry sky beaming a violet
  tractor beam onto small data-visualization icons, labelled 'plotnine'. The
  beam extends across a dark, starlit canvas to three minimalist robot faces
  representing AI agents getting progressively happier. Wordmark on the right
  reads 'plotnine skill — for AI coding agents.'
topics:
  - Visualization
  - Artificial Intelligence
software:
  - plotnine
languages:
  - Python
source: plotnine
tags:
  - AI
  - Agent Skills
---


We now have a [plotnine skill](https://github.com/has2k1/plotnine-skill) for AI Agents.
If you write plotnine and use AI coding assistants day-to-day, this is for you.
It targets the [Agent Skills](https://agentskills.io) standard, so it works across any Agent that supports skills (Claude Code, Codex, and others) and helps an Agent produce consistent, runnable plotnine code.

## Install

Install once:

``` sh
uvx skillsmd add has2k1/plotnine-skill
```

or

``` sh
npx skills add has2k1/plotnine-skill
```

With either option, you will be prompted to choose the specific agents you wish to configure.

## Try it

Once installed, simply ask your Agent to use plotnine and create a plot. For example:

> Use plotnine to create a scatter plot of bill_length_mm vs bill_depth_mm from the penguins dataset, colored by species, with a colorblind-safe palette and a smoothed trend line per species.

Compare the results for the above prompt *with* skill and *without* skill.

<div class="panel-tabset">
<ul id="tabset-1" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-1-1">With Skill</a></li>
<li><a href="#tabset-1-2">No Skill</a></li>
</ul>
<div id="tabset-1-1">

<img src="index_files/figure-markdown_strict/penguins-skill-output-1.png" id="penguins-skill" width="768" height="480" />

``` python
from plotnine import ggplot, aes, geom_point, geom_smooth, scale_color_brewer, labs
from plotnine.data import penguins

(
    ggplot(
        penguins.dropna(),
        aes(x="bill_length_mm", y="bill_depth_mm", color="species"),
    )
    + geom_point(size=2, alpha=0.7)
    + geom_smooth(method="lm", se=True, alpha=0.2)
    + scale_color_brewer(type="qual", palette="Set2")
    + labs(
        x="Bill Length (mm)",
        y="Bill Depth (mm)",
        title="Penguin Bill Dimensions by Species",
        color="Species",
    )
)
```

</div>
<div id="tabset-1-2">

<img src="index_files/figure-markdown_strict/penguins-no-skill-output-1.png" id="penguins-no-skill" width="768" height="480" />

``` python
from plotnine import aes, geom_point, geom_smooth, ggplot, scale_color_brewer
from plotnine.data import penguins

p = (
    ggplot(penguins, aes(x="bill_length_mm", y="bill_depth_mm", color="species"))
    + geom_point(alpha=0.7)
    + geom_smooth(method="lm", se=True)
    + scale_color_brewer(type="qual", palette="Dark2")
)
                       
p.save("scatter_penguins.png", width=8, height=6, dpi=100)
```

</div>
</div>

Note that even without a skill, the Agent (Claude Code Opus 4.6) generates readable and idiomatic code.
The differences then map directly to some of the aspects that the skill enforces. In this case they are:

1.  **Accessibility** --- axis labels with units (where possible) and a real title
2.  **Data Completeness** --- `penguins.dropna()` means that the smoother isn't quietly skipping rows.

As Agents are prone to doing, without a skill the Agent was presumptuous and generated code to save the plot to a file.
The skill makes that experience tighter with fewer surprises, fewer fixes after the fact.

## What is next?

We want this skill to rock, hard, and this is only the beginning.
The vibes may seem good but, with intent, we want to build a sense of where the skill reliably helps and where it does not, so that performance and improvements are grounded in more formal evidence rather than vibes.

Your feedback can help. If you try it, tell us how it performs; the prompts it handled poorly, those were it was surprisingly exceptional, and even those where it was good but it can be exceptional.
The show is still going on, and we will be glad to see what you show us at [the repo](https://github.com/has2k1/plotnine-skill/issues).
