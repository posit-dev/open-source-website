---
title: Quarto 1.10
date: 2026-08-03T00:00:00.000Z
people:
  - Charlotte Wickham
description: >
  Quarto 1.10 is a maintenance release packed with fixes, plus a few
  improvements: accessibility checks that work offline and can target a WCAG
  conformance level, and localized strings for use in custom templates.
image: thumbnail.png
image-alt: >-
  The Quarto logo and the version number 1.10 in white on a steel blue
  background, with a hammer and wrench emoji above.
source: quarto
software:
  - quarto
languages:
  - R
  - Python
topics:
  - Publishing
tags:
  - Quarto 1.10
  - Releases
  - Accessibility
---


Quarto 1.10 is out! You can get the current release from the [download page](https://quarto.org/docs/download/index.html).

Quarto 1.10 is dominated by fixes, as much of our development effort is now going into [Quarto 2](../../blog/2026-04-06_whats-next-quarto-2/), but there are some improvements we wanted to point out: more refined HTML accessibility checks, and access to Quarto's localized strings for template authors.

You can read about these improvements and the most important fixes below. You can find all the changes in this version in the [Release Notes](https://quarto.org/docs/download/changelog/1.10/).

## Accessibility Checking Improvements

Since Quarto 1.8, setting the `axe` option on HTML documents runs [axe-core](https://github.com/dequelabs/axe-core) accessibility checks on your rendered document. Quarto 1.10 makes these checks easier to rely on.

**Checking works offline.** Quarto now bundles its own copy of axe-core instead of loading it from a CDN in the reader's browser. Accessibility checking works without a network connection, and viewing a rendered document no longer triggers a request to an external CDN. The axe-core version is unchanged, so results are identical.

**Check against a WCAG conformance level.** The new `standard` option scopes checks to a WCAG conformance level, including rules axe-core keeps off by default for that level. The `best-practice` option controls whether axe's best-practice rules, recommendations not required by any WCAG success criterion, are also checked:


``` yaml { filename="document.qmd" }
format:
  html:
    axe:
      standard: wcag21aa
      best-practice: true
```

**A clearer report.** When using `output: document`, violations are now listed first by impact, then WCAG conformance level. The report overlay also received its own accessibility and styling fixes: it can be scrolled with the keyboard, uses theme and brand independent colors, and no longer inherits page styling like text centering.

Learn more at [HTML Accessibility](https://quarto.org/docs/output-formats/html-accessibility.html).

## Localized Strings in Templates

If you write custom Pandoc templates or [template partials](https://quarto.org/docs/journals/templates.html#template-partials), you can now use Quarto's localized strings through the new `quarto.language` template variable namespace. Quarto resolves each string for the document's language and exposes it as a template variable:


``` default { filename="template.typ" }
$quarto.language.toc-title-document$
$quarto.language.crossref-fig-title$
```

This lets templates honor the document's `lang` option without hard-coding text. For example, the `orange-book` Typst book extension now uses these variables in its running headers, so a book with `lang: fr` gets *Chapitre* rather than *Chapter*.

Learn more at [Localized Strings in Templates](https://quarto.org/docs/authoring/language.html#localized-strings-in-templates).

## Other Important Fixes

- `quarto preview` reliability---a long-standing bug that showed stale HTML for non-index pages is fixed, changes to a document's `format:` are detected on the first render after the edit, a `_brand.yml` added or removed during preview is picked up, and transient `.quarto_ipynb` files no longer accumulate on disk.

- [Shortcodes](https://quarto.org/docs/extensions/shortcodes.html)---shortcodes are now resolved inside inline and display math expressions.

- [PDF font fallbacks](https://quarto.org/docs/output-formats/pdf-basics.html#fonts)---`mainfontfallback`, `sansfontfallback`, and `monofontfallback` no longer crash LuaLaTeX on TeX Live 2026, and a missing fallback font is now installed automatically.

- Typst fonts---fonts not installed locally are filtered from CSS `font-family` fallback lists before they reach Typst, suppressing `unknown font family` warnings, alongside a batch of fixes to Quarto's CSS-to-Typst translation.

- [Chrome Headless Shell](../../blog/2026-04-14_chrome-headless-shell/)---the `quarto install chromium` command, deprecated in 1.9, now transparently redirects to `chrome-headless-shell`, `quarto check install` warns about legacy Chromium installs, and arm64 Linux is now supported.

- [Output for LLMs](https://quarto.org/docs/websites/website-llms.html)---fixes for websites with `llms-txt` enabled: headings and shortcodes inside conditional content, and clean-URL rewriting of `index.html.md` links.

Dependency updates:

- `pandoc` updated to 3.10
- `typst` updated to 0.15.1
- `deno` updated to 2.7.14
- `dart-sass` updated to 1.101.0
- `esbuild` updated to 0.28.1

## Acknowledgements

We'd like to say a huge thank you to everyone who contributed to this release by opening issues and pull requests:

[AlexLietard](https://github.com/AlexLietard),
[ArthurRudolph](https://github.com/ArthurRudolph),
[Artmann](https://github.com/Artmann),
[C-Monaghan](https://github.com/C-Monaghan),
[ChrisJefferson](https://github.com/ChrisJefferson),
[CoryMcCartan](https://github.com/CoryMcCartan),
[DCEW](https://github.com/DCEW),
[DrFloLinke](https://github.com/DrFloLinke),
[Guest-1013](https://github.com/Guest-1013),
[MBe-iUS](https://github.com/MBe-iUS),
[MurzNN](https://github.com/MurzNN),
[ThierryO](https://github.com/ThierryO),
[ThomasFaria](https://github.com/ThomasFaria),
[TinasheMTapera](https://github.com/TinasheMTapera),
[Voorhoeve](https://github.com/Voorhoeve),
[alderete](https://github.com/alderete),
[andrewheiss](https://github.com/andrewheiss),
[barendgehrels](https://github.com/barendgehrels),
[basm92](https://github.com/basm92),
[blauzo](https://github.com/blauzo),
[chainsawriot](https://github.com/chainsawriot),
[crisbour](https://github.com/crisbour),
[cs-res-pub-ser-st](https://github.com/cs-res-pub-ser-st),
[dustinstoltz](https://github.com/dustinstoltz),
[eculler](https://github.com/eculler),
[eneveu](https://github.com/eneveu),
[github-actions\[bot\]](https://github.com/apps/github-actions),
[gregswinehart](https://github.com/gregswinehart),
[hwine](https://github.com/hwine),
[ianpittwood](https://github.com/ianpittwood),
[ihrke](https://github.com/ihrke),
[jdonaldson](https://github.com/jdonaldson),
[jiangyun-fun](https://github.com/jiangyun-fun),
[jidanni](https://github.com/jidanni),
[jkrumbiegel](https://github.com/jkrumbiegel),
[jnkatz](https://github.com/jnkatz),
[jph00](https://github.com/jph00),
[jtkulas](https://github.com/jtkulas),
[juleswg23](https://github.com/juleswg23),
[juliohm](https://github.com/juliohm),
[kazuyanagimoto](https://github.com/kazuyanagimoto),
[kelli-rstudio](https://github.com/kelli-rstudio),
[lsbjordao](https://github.com/lsbjordao),
[luismmontilla](https://github.com/luismmontilla),
[maelle](https://github.com/maelle),
[maucejo](https://github.com/maucejo),
[memeplex](https://github.com/memeplex),
[micedre](https://github.com/micedre),
[multimeric](https://github.com/multimeric),
[nathant181](https://github.com/nathant181),
[neilernst](https://github.com/neilernst),
[nessan](https://github.com/nessan),
[nickvigilante](https://github.com/nickvigilante),
[nrennie](https://github.com/nrennie),
[pbosetti](https://github.com/pbosetti),
[reckoner](https://github.com/reckoner),
[rgouveiamendes](https://github.com/rgouveiamendes),
[robjhyndman](https://github.com/robjhyndman),
[sbwiecko](https://github.com/sbwiecko),
[seandavi](https://github.com/seandavi),
[sebastiansauer](https://github.com/sebastiansauer),
[skyfroger](https://github.com/skyfroger),
[songwupei](https://github.com/songwupei),
[stefkuypers](https://github.com/stefkuypers),
[stragu](https://github.com/stragu),
[tiagojct](https://github.com/tiagojct),
[victorrssx](https://github.com/victorrssx),
[widlarizer](https://github.com/widlarizer),
[wlatendresse](https://github.com/wlatendresse),
[xuefeng-xu](https://github.com/xuefeng-xu),
[yasyf](https://github.com/yasyf),
[zinc75](https://github.com/zinc75).

The hammer and wrench emoji in the [listing and social card image](thumbnail.png) for this post comes from <a href="https://openmoji.org/" class="external">OpenMoji</a>-- the open-source emoji and icon project. License: <a href="https://creativecommons.org/licenses/by-sa/4.0/#" class="external">CC BY-SA 4.0</a>
