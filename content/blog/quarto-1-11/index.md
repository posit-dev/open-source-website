---
title: Quarto 1.11
date: 2026-10-30T00:00:00.000Z
people:
  - Christophe Dervieux
description: >
  Quarto 1.11 is coming early with a Deno security update, keyboard and screen
  reader fixes, and improvements to Typst, Julia, and shared metadata.
image: thumbnail.png
image-alt: >-
  The Quarto logo and version number 1.11 in white on a steel blue background,
  with a shield and check mark above.
source: quarto
topics:
  - Publishing
software:
  - quarto
languages:
  - Julia
tags:
  - Quarto 1.11
  - Releases
  - Accessibility
hidesubscription: false
---


Quarto 1.11 is coming early to deliver an important security update. You can try it from the [pre-release download page](https://quarto.org/docs/download/prerelease.html), and find the complete changes in the [Release Notes](https://quarto.org/docs/download/changelog/1.11/).

Alongside the security update, this release includes improvements to keyboard and screen reader access, Typst documents, the Julia engine, and shared metadata.

## Security Update

Quarto 1.11 bundles Deno 2.9.8, which rejects certificate chains containing the compromised eMudhra and emSign keys. This protects HTTPS requests made by Quarto commands, including publishing, downloading extensions and templates, and installing tools.

We are releasing 1.11 early because this update will not be backported to Quarto 1.10. Changing the certificate store setting does not address the problem. Once 1.11 is released, upgrading is the way to get the fix; see [quarto-dev/quarto-cli#15152](https://github.com/quarto-dev/quarto-cli/issues/15152) for the details.

The updated Deno has a minimum macOS version of 12 (Monterey).

## Keyboard and Screen Reader Access

Bootstrap-themed HTML documents, websites, books, and dashboards now include a **Skip to main content** link. Keyboard focus uses a consistent, high-contrast ring that remains visible in forced-colors mode, and website sidebar sections can be expanded with the keyboard.

Presentations also receive a set of fixes: keyboard focus stays on the current slide in the normal presentation view, tabsets follow the slide's reading order, and the closed slide menu is hidden from screen readers.

Alternative text is now preserved for Mermaid and Graphviz diagrams in HTML, Revealjs, Word, and Typst output. Word figures also honor `fig-alt`, including figures produced by code, while keeping their visible captions. In this example, `fig-cap` is the caption readers see, while `fig-alt` describes the diagram for readers using assistive technology.


```` markdown { filename="document.qmd" }
```{mermaid}
%%| label: fig-workflow
%%| fig-cap: "The report workflow."
%%| fig-alt: "Data flows through analysis to a report."
flowchart LR
  Data --> Analysis --> Report
```
````

Learn more about [figure alternative text](https://quarto.org/docs/authoring/figures.html#alt-text) and [diagrams](https://quarto.org/docs/authoring/diagrams.html). The [HTML Accessibility](https://quarto.org/docs/output-formats/html-accessibility.html) page explains the checks you can run on your own content.

## Typst Documents

Typst documents now support lists of figures and tables with `lof` and `lot`. Their titles follow the document language and can be customized with `crossref`.


``` yaml { filename="document.qmd" }
---
format: typst
lof: true
lot: true
crossref:
  lof-title: "Figures"
  lot-title: "Tables"
---
```

Proof, remark, and solution blocks now receive theorem-style frames instead of appearing as plain text. Cross-references to blocks with a registered cross-reference label work in Typst too; an ordinary `.proof` block remains unnumbered.

CSS generic font families such as `serif`, `sans-serif`, and `monospace` now resolve to available fonts, avoiding the warnings caused by passing those names directly to Typst.

Learn more at [Lists of Figures and Tables](https://quarto.org/docs/output-formats/typst.html#lists-of-figures-and-tables) and [Theorems and Proofs](https://quarto.org/docs/authoring/cross-references.html#theorems-and-proofs).

## Julia Engine Improvements

The Julia engine now supports `execute-dir`, exporting an executed notebook with `keep-ipynb: true`, and shared worker processes for notebooks with matching configurations. It also includes fixes for renders that hang on long error stack traces or cells that leave a process running.

The bundled engine uses QuartoNotebookRunner 0.18.5. Changes to document or project metadata now invalidate cached cell output.

Learn more about [using the Julia engine](https://quarto.org/docs/computations/julia.html#using-the-julia-engine).

## Shared Metadata and Upgrade Notes

Metadata shared through projects, directories, and `metadata-files` now reaches Pandoc templates and Lua filters correctly when the document defines the same key. Document values still take precedence for single values, while inherited list entries are retained. If you previously used document-level `keywords` to replace an inherited list, check the combined result after upgrading.

Learn more at [Metadata Merging](https://quarto.org/docs/projects/quarto-projects.html#metadata-merging).

Website metadata also receives stricter validation. Misspelled page-level `open-graph` and `twitter-card` options now fail the render with an error instead of being ignored. Put declared preview-image dimensions under `open-graph`; Twitter Cards do not use `image-width` or `image-height`. When a page provides its own image, declare its dimensions in the page's `open-graph` options or shared directory metadata, rather than relying on the site's image dimensions.

Learn more at [Social Metadata](https://quarto.org/docs/websites/website-tools.html#social-metadata).

If you customize HTML themes, the keyboard focus ring now uses `$focus-ring-outer-color`, `$focus-ring-inner-color`, `$focus-ring-outline-width`, and `$focus-ring-outline-offset`. Quarto no longer uses Bootstrap's `$focus-ring-color`, `$focus-ring-box-shadow`, `$btn-focus-width`, or `$btn-focus-box-shadow` for this styling. See [Focus Ring](https://quarto.org/docs/output-formats/html-themes.html#focus-ring) for customization.

## Other Highlights

- [Definition Lists](https://quarto.org/docs/authoring/markdown-basics.html#definition-lists)---You can use a `.definition-list` div containing nested bullet lists, the syntax used by Quarto 2. Existing definition-list syntax continues to work in Quarto 1.11.
- [Website Tools](https://quarto.org/docs/websites/website-tools.html#disabling-on-a-page)---A page can now disable Open Graph or Twitter Card metadata with `open-graph: false` or `twitter-card: false`, even when the website enables it.
- [Google Scholar Metadata](https://quarto.org/docs/authoring/create-citeable-articles.html#google-scholar)---Fixes improve the citation metadata for HTML articles and books, including shared and CSL JSON bibliographies.

Dependency updates include Deno 2.9.8 and the Observable JavaScript runtime's parser, inspector, and inputs. Pandoc 3.10 and Typst 0.15.1 were already bundled with Quarto 1.10.

## Acknowledgements

Thank you to everyone who reported issues, tested pre-releases, and contributed fixes.

[abdanar](https://github.com/abdanar), [adam-na-qureshi](https://github.com/adam-na-qureshi), [AJBogo9](https://github.com/AJBogo9), [andrewheiss](https://github.com/andrewheiss), [asyntai](https://github.com/asyntai), [batpigandme](https://github.com/batpigandme), [beck-chan](https://github.com/beck-chan), [benz0li](https://github.com/benz0li), [cenmir](https://github.com/cenmir), [chanellebingham](https://github.com/chanellebingham), [chendaniely](https://github.com/chendaniely), [colinorourke](https://github.com/colinorourke), [cynthiahqy](https://github.com/cynthiahqy), [D3ller](https://github.com/D3ller), [danmackinlay](https://github.com/danmackinlay), [dasayan05](https://github.com/dasayan05), [drpawelo](https://github.com/drpawelo), [edavidaja](https://github.com/edavidaja), [ferenci-tamas](https://github.com/ferenci-tamas), [gavinsimpson](https://github.com/gavinsimpson), [glin](https://github.com/glin), [gregswinehart](https://github.com/gregswinehart), [Guest-1013](https://github.com/Guest-1013), [guslipkin](https://github.com/guslipkin), [gvegayon](https://github.com/gvegayon), [hvizzolini](https://github.com/hvizzolini), [jfsalzmann](https://github.com/jfsalzmann), [jimjam-slam](https://github.com/jimjam-slam), [jkrumbiegel](https://github.com/jkrumbiegel), [jmcphers](https://github.com/jmcphers), [jmgirard](https://github.com/jmgirard), [jmguzmanc](https://github.com/jmguzmanc), [JoFrhwld](https://github.com/JoFrhwld), [jolars](https://github.com/jolars), [kasbah](https://github.com/kasbah), [kv9898](https://github.com/kv9898), [larcherMTT](https://github.com/larcherMTT), [Lightbridge-KS](https://github.com/Lightbridge-KS), [lsbjordao](https://github.com/lsbjordao), [luifrancgom](https://github.com/luifrancgom), [lwjohnst86](https://github.com/lwjohnst86), [Masad791](https://github.com/Masad791), [melissa-barca](https://github.com/melissa-barca), [merlinschumacher](https://github.com/merlinschumacher), [nealrichardson](https://github.com/nealrichardson), [nickriches](https://github.com/nickriches), [pbosetti](https://github.com/pbosetti), [pinin4fjords](https://github.com/pinin4fjords), [plessl](https://github.com/plessl), [presnick](https://github.com/presnick), [ravila4](https://github.com/ravila4), [ravimakhijapi](https://github.com/ravimakhijapi), [resulumit](https://github.com/resulumit), [rkskmt](https://github.com/rkskmt), [rodrigo-j-goncalves](https://github.com/rodrigo-j-goncalves), [schochastics](https://github.com/schochastics), [seandavi](https://github.com/seandavi), [sogav21](https://github.com/sogav21), [supertj](https://github.com/supertj), [visr](https://github.com/visr), [VisruthSK](https://github.com/VisruthSK), [xtimbeau](https://github.com/xtimbeau), [xuefeng-xu](https://github.com/xuefeng-xu).
