---
title: "Updates to tidymodels.org"
date: 2026-06-20
people:
  - Emil Hvitfeldt
description: >
  A look at recent updates to tidymodels.org, including a new search feature and behind-the-scenes infrastructure improvements.
image: "featured.png"
image-alt: ""
topics:
  - Machine Learning
software:
  - tidymodels
languages:
  - R
source: []
hidesubscription: false
---

<!--
- [ ] Add image (1920×1080 PNG or JPG) and image-alt
- [ ] Open a PR against main for a Netlify preview
-->

It has been a busy last couple of months for [tidymodels.org](https://www.tidymodels.org/).
The site got a visual refresh,
the Find pages were rebuilt from scratch,
every article was modernized to use the base pipe and current parsnip and keras APIs,
and, maybe most importantly,
the whole rendering pipeline now keeps itself up to date automatically whenever a tidymodels package hits CRAN.
Here is a roundup of what changed, grouped by theme.

## A rebuilt Find experience

The Find pages were one of the oldest parts of the site,
and they were starting to show their age.
The old DT-based tables were hard to scan and didn't filter cleanly,
so we [rebuilt them from scratch](https://github.com/tidymodels/tidymodels.org/pull/249) as Quarto custom listings backed by generated `items.yml` files.
They now have proper faceted multi-select filter dropdowns,
which makes narrowing down to the model or function you need much faster.

Along the way we filled in coverage that had been missing from search:
[quantile regression models](https://github.com/tidymodels/tidymodels.org/pull/265),
[bonsai](https://github.com/tidymodels/tidymodels.org/pull/230),
and the rest of the tidymodels org packages all made it onto the official package list and into Find.
We also [fixed the parsnip table's horizontal overflow](https://github.com/tidymodels/tidymodels.org/pull/243)
and [split the old `make_function_list.R` into separate generators](https://github.com/tidymodels/tidymodels.org/pull/148) so the underlying data is easier to maintain.

## Automatic re-rendering when packages update

This is the deepest change of the year,
even though it is the least visible.
The site used to require a manual re-render whenever a tidymodels package was updated on CRAN.
That was easy to forget,
and slow when it did happen because every page got re-rendered together.
The pipeline is now much more targeted.

Every article declares its non-tidymodels package dependencies in [`r-packages:` YAML front matter](https://github.com/tidymodels/tidymodels.org/pull/152),
and a build script turns that into a package-to-pages map.
From there, CI knows exactly which pages a given CRAN release could affect.

A scheduled workflow then checks CRAN every weekday morning,
figures out which packages changed and which pages depend on them,
[installs only those packages](https://github.com/tidymodels/tidymodels.org/pull/166),
re-renders only those pages,
and opens a PR for review (or files an issue if anything fails).
Contributors can also trigger renders by [commenting `/render` on a PR](https://github.com/tidymodels/tidymodels.org/pull/163),
which is a big quality-of-life win for anyone who doesn't want to install the full toolchain locally.
You can see the system at work in the steady drip of bot-authored re-render PRs,
including package-specific ones for [broom](https://github.com/tidymodels/tidymodels.org/pull/245),
[parsnip](https://github.com/tidymodels/tidymodels.org/pull/246),
and [bonsai](https://github.com/tidymodels/tidymodels.org/pull/268).

To keep that daily cadence practical,
we also audited the longest-running pages and trimmed render time where we could,
and set up Spark, Java 17, and a cached Keras virtualenv in CI.

## Cleaner, more reproducible output

A surprising amount of churn in rendered output came from things like timestamps and small h2o non-determinism.
We cleaned up the session-info blocks to [remove the date](https://github.com/tidymodels/tidymodels.org/pull/223) and [other noise](https://github.com/tidymodels/tidymodels.org/pull/168),
set reproducible seeds for h2o,
and normalized its output more carefully.
A re-render now produces a meaningful diff instead of being drowned in cosmetic differences.

## Modernized article code

The articles got a top-to-bottom code refresh.
Every `%>%` [became `|>`](https://github.com/tidymodels/tidymodels.org/pull/225),
[deprecated parsnip and recipes functions](https://github.com/tidymodels/tidymodels.org/pull/226) were swapped for their current equivalents,
and [parsnip engine setters were fully specified](https://github.com/tidymodels/tidymodels.org/pull/227) so they don't break when defaults shift.
The keras article was [migrated to the new keras3 engine](https://github.com/tidymodels/tidymodels.org/pull/264),
and the parsnip predictions article, which had been broken for a while,
was [restored from the old parsnip vignette](https://github.com/tidymodels/tidymodels.org/pull/128).

## Code linking with downlit

Function names in code blocks across the site are now hyperlinked to their documentation with [downlit](https://github.com/tidymodels/tidymodels.org/pull/158).
The tricky part was that `library(tidymodels)` doesn't get auto-expanded the way `library(tidyverse)` does,
so a [small post-render script](https://github.com/tidymodels/tidymodels.org/pull/159) seeds the package list explicitly.
That is what makes `step_*`, `tune()`, and friends light up everywhere.

## Site content and UX

The most visible work this year was a steady stream of design polish.
We [rebuilt the landing page](https://github.com/tidymodels/tidymodels.org/pull/228) so it actually showcases what tidymodels is and where to start,
swapped in the [new Posit logo](https://github.com/tidymodels/tidymodels.org/pull/240),
and moved blog references from the old tidyverse blog to [opensource.posit.co](https://github.com/tidymodels/tidymodels.org/pull/241).
Hex stickers across the site were [converted from PNG to SVG](https://github.com/tidymodels/tidymodels.org/pull/212) so they stay crisp at any size,
and the dev articles [got hexes of their own](https://github.com/tidymodels/tidymodels.org/pull/213).

The team listing was [refreshed](https://github.com/tidymodels/tidymodels.org/pull/149) to reflect who is working on tidymodels today,
and we [reserved image dimensions on the About page](https://github.com/tidymodels/tidymodels.org/pull/250) to fix a layout shift where author photos popped in late.
The Learn, Books, and Resources pages picked up a batch of smaller fixes:
[updated Learn categories](https://github.com/tidymodels/tidymodels.org/pull/267)
and [more feedback UI](https://github.com/tidymodels/tidymodels.org/pull/253) such as hover states on article cards and sidebar links.
Edgar contributed a dedicated [cheatsheets page](https://github.com/tidymodels/tidymodels.org/pull/153),
and Julia's long-standing PR to publish the [priorities survey results](https://github.com/tidymodels/tidymodels.org/pull/239) finally landed.

## Behind the scenes

Plenty of repo hygiene rounded out the year.
The [Quarto config was split](https://github.com/tidymodels/tidymodels.org/pull/191) into local and production profiles,
fonts are now self-hosted (Lato and Source Code Pro) instead of pulled from Google,
and the README got a proper contributing section.

Head over to [tidymodels.org](https://www.tidymodels.org/) to see it all in action,
and if you spot something to improve,
contributions are very welcome over on [GitHub](https://github.com/tidymodels/tidymodels.org).
