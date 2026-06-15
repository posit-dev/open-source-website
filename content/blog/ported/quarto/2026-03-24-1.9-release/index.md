---
title: Quarto 1.9
description: >
  Quarto 1.9 adds publishing to Posit Connect Cloud, LLM-friendly website
  output, major Typst improvements, experimental PDF accessibility standards,
  and list tables for complex table content.
people:
  - Charlotte Wickham
date: '2026-03-24'
image: thumbnail.png
image-alt: Quarto 1.9
ported_from: quarto
source: quarto
port_status: review
software:
  - quarto
languages:
  - R
  - Python
topics:
  - Publishing
tags:
  - Quarto
slug: 1.9-release
---


Quarto 1.9 is out! You can get the current release from the [download page](https://quarto.org/docs/download/index.html).

Sharing your work just got easier with integrated Posit Connect Cloud publishing. Typst users will appreciate book project support and article layouts, while experimental PDF accessibility standards bring PDF/A and PDF/UA compliance to both LaTeX and Typst. This release also introduces LLM-friendly output for websites, the `quarto use brand` command for keeping your brand assets in sync, and list tables for authoring complex tables with familiar bullet syntax.

You can read about these improvements and some other highlights below. You can find all the changes in this version in the [Release Notes](https://quarto.org/docs/download/changelog/1.9/).

## Publish to Posit Connect Cloud

You can now publish documents and websites to [Posit Connect Cloud](https://connect.posit.cloud) directly from the command line.
For example, publish your Quarto website project with:


``` bash { filename="Terminal" }
quarto publish posit-connect-cloud
```

Posit Connect Cloud is a hosted platform for sharing data applications and documents without managing your own infrastructure. It includes a free tier for unlimited static document publishing.
Read more in [Publishing \> Posit Connect Cloud](https://quarto.org/docs/publishing/posit-connect-cloud.html).

## Improvements to Typst Support

Quarto 1.9 brings substantial improvements to Typst output:

- [Book projects](https://quarto.org/docs/books/book-output.html#typst-output) can now render to Typst via the bundled `orange-book` extension, with chapter numbering, cross-references, and professional textbook styling.
- [Article layout](https://quarto.org/docs/authoring/article-layout.html) support lets you place content in the margins, create full-width figures, or add side notes.
- New options: `mathfont`, `codefont`, `linestretch`, `linkcolor`, `citecolor`, `filecolor`, `thanks`, and `abstract-title`.
- [Theorem styling](https://quarto.org/docs/output-formats/typst.html#theorems) with four appearance options: `simple`, `fancy`, `clouds`, or `rainbow`.

See [this blog post](/blog/2026-03-31_typst-books-and-more/) for details on all the Typst improvements.

## PDF Accessibility (Experimental)

We're rolling out experimental support for PDF accessibility standards in 1.9. The new `pdf-standard` option enables PDF/A archival formats and PDF/UA accessibility compliance for both LaTeX and Typst outputs. Alt text from `fig-alt` attributes now passes through to PDF for screen reader support, and Typst gains support for alt text on cross-referenced equations.

Read more in our [PDF Accessibility and Standards blog post](/blog/2026-03-05_pdf-accessibility-and-standards/) or the documentation for [LaTeX](https://quarto.org/docs/output-formats/pdf-basics.html#pdf-accessibility-standards) and [Typst](https://quarto.org/docs/output-formats/typst.html#pdf-accessibility-standards).

## Output for LLMs

Quarto can now generate [llms.txt](https://llmstxt.org/) format output for your website, making your content more accessible to large language models and AI-powered tools.

Enable it in your website configuration:


``` yaml { filename="_quarto.yml" }
website:
  title: "My Documentation"
  llms-txt: true
```

When you render your site, Quarto creates:

- An `llms.txt` index file at the root of your site listing all pages
- A `.llms.md` markdown file alongside each HTML page (e.g., `guide.html` gets `guide.llms.md`)

The markdown files contain clean versions of your content---navigation, sidebars, and scripts are stripped out; tables, code blocks, and callouts are converted to standard markdown.

Read more, including how to customize what appears in LLM output, in [Websites \> Output for LLMs](https://quarto.org/docs/websites/website-llms.html).

## `quarto use brand` Command

Keep your project's brand assets in sync with an external source using the new `quarto use brand` command:


``` bash { filename="Terminal" }
quarto use brand myorg/shared-brand
```

The command copies brand files from a GitHub repository, local directory, or zip archive into your project's `_brand/` directory. Quarto walks you through each step---confirming trust for remote sources, creating the directory if needed, and asking whether to overwrite or remove files.

See [Guide \> Brand](https://quarto.org/docs/authoring/brand.html#quarto-use-brand) for `--dry-run`, `--force`, and other options.

## List Tables

List tables provide a new syntax for creating tables with complex content---multiple paragraphs, code blocks, or nested lists---using familiar bullet syntax instead of grid table formatting:

<div class="grid gap-12 items-start md:grid-cols-2">
<div class="prose max-w-none">

```` markdown
::: {.list-table}
- - Function
  - Description

- - `sum()`
  - Add values:

    ```python
    sum([1, 2, 3])
    ```

- - `len()`
  - Count items:

    - Works on lists
    - Works on strings
:::
````

</div>
<div class="prose max-w-none">

<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>sum()</code></p></td>
<td><p>Add values:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode python"><code class="sourceCode python"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="bu">sum</span>([<span class="dv">1</span>, <span class="dv">2</span>, <span class="dv">3</span>])</span></code></pre></div></td>
</tr>
<tr>
<td><p><code>len()</code></p></td>
<td><p>Count items:</p>
<ul>
<li>Works on lists</li>
<li>Works on strings</li>
</ul></td>
</tr>
</tbody>
</table>

</div>
</div>

Each top-level bullet represents a row; nested bullets represent cells. This syntax is much easier to maintain than grid tables, especially when cells contain code or other block elements.

List tables support all the usual table features: captions, cross-references, column widths, and alignment. Thanks to Martin Fischer for the original development, with contributions from Albert Krewinkel and William Lupton.

Find all the details in [Guide \> Tables](https://quarto.org/docs/authoring/tables.html#list-tables).

## Other Highlights

- [Search Result Highlighting](https://quarto.org/docs/websites/website-search.html#search-result-highlighting): Improved highlighting of search terms on destination pages, with persistent marks, automatic tab activation for matches inside tabsets, and cross-element highlighting for multi-word searches.

- Privacy-focused features for websites:

  - [A privacy-first default for cookie consent](https://quarto.org/docs/websites/website-tools.html#cookie-consent): The default for cookie consent has changed to `type: express`, providing opt-in consent that blocks cookies until users explicitly agree. This privacy-conscious default is designed with modern privacy regulations in mind.

  - [Algolia Search Insights avoids cookies](https://quarto.org/docs/websites/website-search.html#cookie-consent-and-user-tracking): Use Algolia Insights now uses persistent cookies only if `cookie-consent` is active, and the user has opted-in.

  - [Use Plausible Analytics](https://quarto.org/docs/websites/website-tools.html#plausible-analytics): Add privacy-friendly Plausible Analytics to websites via the `plausible-analytics` configuration option.

- [`aria-label` for videos](https://quarto.org/docs/authoring/videos.html#accessibility-label): Improve accessibility of embedded videos by providing custom descriptive labels for screen readers instead of the default "Video Player" label.

- [New `syntax-highlighting` Option](https://quarto.org/docs/output-formats/pdf-basics.html#syntax-highlighting): Replaces the deprecated `highlight-style` (Pandoc 3.8). Supports style names, custom `.theme` files, `none`, or `idiomatic` for format-native highlighting.

- Metadata and brand extensions now work without a `_quarto.yml` project. A temporary default project is created in memory.

- [Engine extensions](https://quarto.org/docs/extensions/engine.html) allow replacement of the execution engine:

  - Julia is now a bundled extension instead of being built-in.
  - **quarto-marimo** will soon change from a filter extension to an engine extension.
  - New `quarto create extension engine` command.
  - New `quarto call build-ts-extension` command.
  - New **Quarto API** for engine extensions to use. (This is in flux and will not be documented for the next few releases, but [there is a dev blog post about it](https://quarto-dev.github.io/dev-notes/posts/2026-03-04/).)

Dependency updates:

- `pandoc` updated to 3.8.3
- `typst` updated to 0.14.2
- `esbuild` updated to 0.25.10
- `deno` updated to 2.4.5
- `mermaid` updated to 11.12.0

## Acknowledgements

One of the early proposals for PDF accessibility and alt text in the LaTeX ecosystem was provided to us by [Sam Schiano](https://github.com/Schiano-NOAA) and [Sophie Breitbart](https://github.com/sbreitbart-NOAA). We want to thank them for bringing into our attention the approach they used in their [`{asar}` R package](https://nmfs-ost.github.io/asar/), which influenced some of our design.

In addition, we'd like to say a huge thank you to everyone who contributed to this release by opening issues and pull requests:

[CoryMcCartan](https://github.com/CoryMcCartan),
[DanChaltiel](https://github.com/DanChaltiel),
[Data-Wise](https://github.com/Data-Wise),
[FrankwaP](https://github.com/FrankwaP),
[Joao-O-Santos](https://github.com/Joao-O-Santos),
[LukasDSauer](https://github.com/LukasDSauer),
[MBe-iUS](https://github.com/MBe-iUS),
[MarcoPortmann](https://github.com/MarcoPortmann),
[MariaBarrioSchez](https://github.com/MariaBarrioSchez),
[MateusMolina](https://github.com/MateusMolina),
[Selbosh](https://github.com/Selbosh),
[ThePurox](https://github.com/ThePurox),
[TucoFernandes](https://github.com/TucoFernandes),
[aecoleman](https://github.com/aecoleman),
[amirhome61](https://github.com/amirhome61),
[andrewheiss](https://github.com/andrewheiss),
[azankl](https://github.com/azankl),
[bensoltoff](https://github.com/bensoltoff),
[bruvellu](https://github.com/bruvellu),
[byzheng](https://github.com/byzheng),
[cbrnr](https://github.com/cbrnr),
[chendaniely](https://github.com/chendaniely),
[chi-raag](https://github.com/chi-raag),
[christopherkenny](https://github.com/christopherkenny),
[coatless](https://github.com/coatless),
[cynthiahqy](https://github.com/cynthiahqy),
[darwindarak](https://github.com/darwindarak),
[davidskalinder](https://github.com/davidskalinder),
[dmenne](https://github.com/dmenne),
[fconil](https://github.com/fconil),
[fkgruber](https://github.com/fkgruber),
[fkohrt](https://github.com/fkohrt),
[fredguth](https://github.com/fredguth),
[gadenbuie](https://github.com/gadenbuie),
[github-actions\[bot\]](https://github.com/apps/github-actions),
[gsathler-vi](https://github.com/gsathler-vi),
[hamgamb](https://github.com/hamgamb),
[herosi](https://github.com/herosi),
[icarusz](https://github.com/icarusz),
[idavydov](https://github.com/idavydov),
[jeremy886](https://github.com/jeremy886),
[jkrumbiegel](https://github.com/jkrumbiegel),
[jmcphers](https://github.com/jmcphers),
[jonas37](https://github.com/jonas37),
[jorherre](https://github.com/jorherre),
[jreades](https://github.com/jreades),
[jromanowska](https://github.com/jromanowska),
[jtbayly](https://github.com/jtbayly),
[juleswg23](https://github.com/juleswg23),
[juliasilge](https://github.com/juliasilge),
[kathsherratt](https://github.com/kathsherratt),
[kusnezoff-alexander](https://github.com/kusnezoff-alexander),
[lrrichter](https://github.com/lrrichter),
[lwjohnst86](https://github.com/lwjohnst86),
[maelle](https://github.com/maelle),
[matthiasbaitsch](https://github.com/matthiasbaitsch),
[mipmip](https://github.com/mipmip),
[mstrms2000](https://github.com/mstrms2000),
[multimeric](https://github.com/multimeric),
[mvuorre](https://github.com/mvuorre),
[mykolaskrynnyk](https://github.com/mykolaskrynnyk),
[nichtich](https://github.com/nichtich),
[nithinmkp](https://github.com/nithinmkp),
[nrichers](https://github.com/nrichers),
[orbsmiv](https://github.com/orbsmiv),
[paytonej](https://github.com/paytonej),
[petrelharp](https://github.com/petrelharp),
[phongphuhanam](https://github.com/phongphuhanam),
[pm-gusmano](https://github.com/pm-gusmano),
[posit-snyk-bot](https://github.com/posit-snyk-bot),
[prosoitos](https://github.com/prosoitos),
[rabyj](https://github.com/rabyj),
[sasja-san](https://github.com/sasja-san),
[sbwiecko](https://github.com/sbwiecko),
[serialc](https://github.com/serialc),
[spaette](https://github.com/spaette),
[spraetor](https://github.com/spraetor),
[stragu](https://github.com/stragu),
[szimmer](https://github.com/szimmer),
[the-solipsist](https://github.com/the-solipsist),
[thomasp85](https://github.com/thomasp85),
[yyzeng](https://github.com/yyzeng),
[zhe00a](https://github.com/zhe00a).

The airplane departure emoji in the [listing and social card image](thumbnail.png) for this post comes from <a href="https://openmoji.org/" class="external">OpenMoji</a>-- the open-source emoji and icon project. License: <a href="https://creativecommons.org/licenses/by-sa/4.0/#" class="external">CC BY-SA 4.0</a>
