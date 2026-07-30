---
title: Quarto 1.10
date: 2026-08-03T00:00:00.000Z
people:
  - Charlotte Wickham
description: >
  Quarto 1.10 matures the built-in accessibility checks—they now work offline,
  report WCAG conformance levels, and can check against a specific conformance
  standard—and gives template authors access to Quarto's localized strings.
image: thumbnail.png
image-alt: Quarto 1.10
source: quarto
software:
  - quarto
languages:
  - R
  - Python
topics:
  - Publishing
---


Quarto 1.10 is out! You can get the current release from the [download page](https://quarto.org/docs/download/index.html).

This release concentrates on accessibility: the checks built into HTML output now work offline, report the WCAG conformance level of each violation, and can be scoped to a specific conformance standard. Template authors gain access to Quarto's localized strings, `quarto install chromium` gives way to `chrome-headless-shell`, and a long list of fixes improves `quarto preview`, Typst and PDF output, and tool installation.

You can read about these improvements and some other highlights below. You can find all the changes in this version in the [Release Notes](https://quarto.org/docs/download/changelog/1.10/).

## Accessibility Checking Improvements

Since Quarto 1.8, setting the `axe` option on HTML documents runs [axe-core](https://github.com/dequelabs/axe-core) accessibility checks on your rendered document and reports any violations right on the page. Quarto 1.10 makes these checks easier to rely on.

**Checking works offline.** Quarto now bundles its own copy of axe-core instead of loading it from a CDN in the reader's browser. Accessibility checking works without a network connection, and viewing a rendered document no longer triggers a request to an external CDN. The axe-core version is unchanged, so results are identical.

**Check against a WCAG conformance level.** The new `standard` option scopes checks to a WCAG conformance level, including rules axe-core keeps off by default for that level, such as AAA color contrast. The `best-practice` option controls whether axe's best-practice rules---recommendations not required by any WCAG success criterion---are also checked:


``` yaml { filename="document.qmd" }
format:
  html:
    axe:
      standard: wcag21aa
      best-practice: true
```

**A clearer report.** Violations are now listed most-important-first---by impact, then WCAG conformance level---and each violation is labeled with the level it belongs to (e.g. `WCAG 2.0 AA (1.4.3)`) or `Best Practice`. The report overlay also received its own accessibility and styling fixes: it can be scrolled with the keyboard, uses theme-independent colors so it stays readable and no longer clobbers colors set via `_brand.yml`, and no longer inherits page styling like text centering.

Beyond `axe`, 1.10 fixes two accessible-name gaps: code line-number links and the ORCID profile link in title blocks now have accessible names for screen readers---thanks to [Mickaël Canouil](https://github.com/mcanouil) for the ORCID fix.

Learn more at [HTML Accessibility](https://quarto.org/docs/output-formats/html-accessibility.html).

## Localized Strings in Templates

If you write custom Pandoc templates or [template partials](https://quarto.org/docs/journals/templates.html#template-partials), you can now use Quarto's localized strings through the new `quarto.language` template variable namespace. Quarto resolves each string for the document's language and exposes it as a template variable:


``` default { filename="template.typ" }
$quarto.language.toc-title-document$
$quarto.language.crossref-fig-title$
```

This lets templates honor the document's `lang` option without hard-coding text. For example, the `orange-book` Typst book extension now uses these variables in its running headers, so a book with `lang: fr` gets *Chapitre* rather than *Chapter*.

Learn more at [Localized Strings in Templates](https://quarto.org/docs/authoring/language.html#localized-strings-in-templates).

## `chrome-headless-shell` Replaces Chromium

Quarto uses a headless browser to render Mermaid and Graphviz diagrams in some formats. The recommended way to install one is:


``` bash { filename="Terminal" }
quarto install chrome-headless-shell
```

In 1.10, `quarto install chromium` is deprecated and transparently redirects to `chrome-headless-shell`. The legacy installer pins a Chromium build that can no longer receive security updates, while `chrome-headless-shell` always installs the latest stable Chrome. Installing `chrome-headless-shell` removes any legacy Chromium installation, and `quarto check install` warns if it detects one. `chrome-headless-shell` is now also available on arm64 Linux.

Learn more at [Diagrams \> Chrome Install](https://quarto.org/docs/authoring/diagrams.html#chrome-install).

## Other Highlights

- [Code annotations](https://quarto.org/docs/authoring/code-annotation.html)---code annotations and YAML cell options now work in Kotlin code cells. Thanks to [Barend Gehrels](https://github.com/barendgehrels) for the contribution!

- `quarto preview` reliability---a long-standing bug that showed stale HTML for non-index pages is fixed, changes to a document's `format:` are detected on the first render after the edit, a `_brand.yml` added or removed during preview is picked up, and transient `.quarto_ipynb` files no longer accumulate on disk.

- [Shortcodes](https://quarto.org/docs/extensions/shortcodes.html)---shortcodes are now resolved inside inline and display math expressions.

- [PDF font fallbacks](https://quarto.org/docs/output-formats/pdf-basics.html#fonts)---`mainfontfallback`, `sansfontfallback`, and `monofontfallback` no longer crash LuaLaTeX on TeX Live 2026, and a missing fallback font is now installed automatically.

- Typst fonts---fonts not installed locally are filtered from CSS `font-family` fallback lists before they reach Typst, suppressing `unknown font family` warnings, alongside a batch of fixes to Quarto's CSS-to-Typst translation.

- TinyTeX installation---`quarto install tinytex` now defaults to a [CDN-backed TeX Live mirror](https://yihui.org/en/2026/03/tinytex-ctan-mirror/), matching the R **tinytex** package, and all `quarto install` downloads retry on transient network failures.

- [Placeholder images](https://quarto.org/docs/authoring/placeholder.html)---the `placeholder` shortcode now generates images locally, with no network access, after the external image service it relied on was retired.

- [Output for LLMs](https://quarto.org/docs/websites/website-llms.html)---fixes for websites with `llms-txt` enabled: headings and shortcodes inside conditional content, and clean-URL rewriting of `index.html.md` links.

- Third-party Jupyter kernels---a kernel that returns an incomplete `execute_reply` (observed with Maple 2025) now records a cell error instead of aborting the render. Thanks to [Chris Jefferson](https://github.com/ChrisJefferson)!

Dependency updates:

- `pandoc` updated to 3.10
- `typst` updated to 0.15.1
- `deno` updated to 2.7.14
- `dart-sass` updated to 1.101.0
- `esbuild` updated to 0.28.1

## Acknowledgements

We'd like to say a huge thank you to everyone who contributed to this release by opening issues and pull requests:

[AlexLietard](https://github.com/AlexLietard),
[AlloriMD](https://github.com/AlloriMD),
[ArthurRudolph](https://github.com/ArthurRudolph),
[Artmann](https://github.com/Artmann),
[AshleyHenry15](https://github.com/AshleyHenry15),
[Benjamin-Lee](https://github.com/Benjamin-Lee),
[C-Monaghan](https://github.com/C-Monaghan),
[Ciyoku](https://github.com/Ciyoku),
[CoryMcCartan](https://github.com/CoryMcCartan),
[DCEW](https://github.com/DCEW),
[DmitriyLeybel](https://github.com/DmitriyLeybel),
[DrFloLinke](https://github.com/DrFloLinke),
[EinMaulwurf](https://github.com/EinMaulwurf),
[EllaKaye](https://github.com/EllaKaye),
[ErwinTATP](https://github.com/ErwinTATP),
[FelixBenning](https://github.com/FelixBenning),
[Huttsa](https://github.com/Huttsa),
[IndrajeetPatil](https://github.com/IndrajeetPatil),
[KipBalkcom-USDA](https://github.com/KipBalkcom-USDA),
[LBeaulaton](https://github.com/LBeaulaton),
[MBe-iUS](https://github.com/MBe-iUS),
[MurzNN](https://github.com/MurzNN),
[N1N74](https://github.com/N1N74),
[Optimus-Pine](https://github.com/Optimus-Pine),
[Robinlovelace](https://github.com/Robinlovelace),
[SrShelo](https://github.com/SrShelo),
[StephenB1289](https://github.com/StephenB1289),
[ThierryO](https://github.com/ThierryO),
[ThomasFaria](https://github.com/ThomasFaria),
[TinasheMTapera](https://github.com/TinasheMTapera),
[Voorhoeve](https://github.com/Voorhoeve),
[Younthing](https://github.com/Younthing),
[a-dna-n](https://github.com/a-dna-n),
[adityam](https://github.com/adityam),
[agerlach](https://github.com/agerlach),
[ahcombs](https://github.com/ahcombs),
[albertomercurio](https://github.com/albertomercurio),
[alderete](https://github.com/alderete),
[allefeld](https://github.com/allefeld),
[andjar](https://github.com/andjar),
[andrewheiss](https://github.com/andrewheiss),
[andrewpbray](https://github.com/andrewpbray),
[aronatkins](https://github.com/aronatkins),
[barendgehrels](https://github.com/barendgehrels),
[basm92](https://github.com/basm92),
[bblais](https://github.com/bblais),
[benibargera](https://github.com/benibargera),
[benlubas](https://github.com/benlubas),
[benz0li](https://github.com/benz0li),
[bergsmat](https://github.com/bergsmat),
[blauzo](https://github.com/blauzo),
[cbrnr](https://github.com/cbrnr),
[chainsawriot](https://github.com/chainsawriot),
[charliejhadley](https://github.com/charliejhadley),
[christopherkenny](https://github.com/christopherkenny),
[coatless](https://github.com/coatless),
[cod3licious](https://github.com/cod3licious),
[connorferster](https://github.com/connorferster),
[crisbour](https://github.com/crisbour),
[cs-res-pub-ser-st](https://github.com/cs-res-pub-ser-st),
[danielvartan](https://github.com/danielvartan),
[dmenne](https://github.com/dmenne),
[dustinstoltz](https://github.com/dustinstoltz),
[edavidaja](https://github.com/edavidaja),
[eheinzen](https://github.com/eheinzen),
[eitsupi](https://github.com/eitsupi),
[ekatko1](https://github.com/ekatko1),
[elenlefoll](https://github.com/elenlefoll),
[elharo](https://github.com/elharo),
[eneveu](https://github.com/eneveu),
[epamax](https://github.com/epamax),
[felixcremer](https://github.com/felixcremer),
[firai](https://github.com/firai),
[fkohrt](https://github.com/fkohrt),
[floholl](https://github.com/floholl),
[fmichonneau](https://github.com/fmichonneau),
[gadenbuie](https://github.com/gadenbuie),
[georgestagg](https://github.com/georgestagg),
[ghost](https://github.com/ghost),
[github-actions\[bot\]](https://github.com/apps/github-actions),
[gl-eb](https://github.com/gl-eb),
[glin](https://github.com/glin),
[gregswinehart](https://github.com/gregswinehart),
[gskorokhod](https://github.com/gskorokhod),
[gtritchie](https://github.com/gtritchie),
[gucio321](https://github.com/gucio321),
[hamelsmu](https://github.com/hamelsmu),
[hguturu](https://github.com/hguturu),
[hugetim](https://github.com/hugetim),
[ihrke](https://github.com/ihrke),
[ikolith](https://github.com/ikolith),
[jack-davison](https://github.com/jack-davison),
[jdonaldson](https://github.com/jdonaldson),
[jiangyun-fun](https://github.com/jiangyun-fun),
[jidanni](https://github.com/jidanni),
[jimjam-slam](https://github.com/jimjam-slam),
[jkrumbiegel](https://github.com/jkrumbiegel),
[jkub6](https://github.com/jkub6),
[jph00](https://github.com/jph00),
[jsquaredosquared](https://github.com/jsquaredosquared),
[jtbayly](https://github.com/jtbayly),
[jthomasmock](https://github.com/jthomasmock),
[jtkulas](https://github.com/jtkulas),
[juleswg23](https://github.com/juleswg23),
[juliasilge](https://github.com/juliasilge),
[juliohm](https://github.com/juliohm),
[kandolfp](https://github.com/kandolfp),
[kazuyanagimoto](https://github.com/kazuyanagimoto),
[kdheepak](https://github.com/kdheepak),
[kernie](https://github.com/kernie),
[kompre](https://github.com/kompre),
[kuon](https://github.com/kuon),
[lauren-obrien](https://github.com/lauren-obrien),
[lsbjordao](https://github.com/lsbjordao),
[luismmontilla](https://github.com/luismmontilla),
[lynn](https://github.com/lynn),
[machow](https://github.com/machow),
[maelle](https://github.com/maelle),
[maia-sh](https://github.com/maia-sh),
[malcolmbarrett](https://github.com/malcolmbarrett),
[maptv](https://github.com/maptv),
[matthew-brett](https://github.com/matthew-brett),
[matulad](https://github.com/matulad),
[maucejo](https://github.com/maucejo),
[mccarthy-m-g](https://github.com/mccarthy-m-g),
[mckabue](https://github.com/mckabue),
[memeplex](https://github.com/memeplex),
[micedre](https://github.com/micedre),
[mjdzr](https://github.com/mjdzr),
[mrheducation](https://github.com/mrheducation),
[multimeric](https://github.com/multimeric),
[mutlusun](https://github.com/mutlusun),
[natecostello](https://github.com/natecostello),
[nathant181](https://github.com/nathant181),
[neilernst](https://github.com/neilernst),
[nessan](https://github.com/nessan),
[nickvigilante](https://github.com/nickvigilante),
[nrennie](https://github.com/nrennie),
[odysseu](https://github.com/odysseu),
[paniterka](https://github.com/paniterka),
[papayoun](https://github.com/papayoun),
[pbosetti](https://github.com/pbosetti),
[pchtsp](https://github.com/pchtsp),
[petrelharp](https://github.com/petrelharp),
[petzi53](https://github.com/petzi53),
[posit-snyk-bot](https://github.com/posit-snyk-bot),
[py9mrg](https://github.com/py9mrg),
[rdimond](https://github.com/rdimond),
[remlapmot](https://github.com/remlapmot),
[rgaiacs](https://github.com/rgaiacs),
[rgouveiamendes](https://github.com/rgouveiamendes),
[richard-mevis](https://github.com/richard-mevis),
[rmflight](https://github.com/rmflight),
[robert-koetsier](https://github.com/robert-koetsier),
[robjhyndman](https://github.com/robjhyndman),
[ronblum](https://github.com/ronblum),
[rpruim](https://github.com/rpruim),
[rustyconover](https://github.com/rustyconover),
[ryjohnson09](https://github.com/ryjohnson09),
[s-andrews](https://github.com/s-andrews),
[s2t2](https://github.com/s2t2),
[sbwiecko](https://github.com/sbwiecko),
[schochastics](https://github.com/schochastics),
[seandavi](https://github.com/seandavi),
[sebastiansauer](https://github.com/sebastiansauer),
[sghng](https://github.com/sghng),
[siHopp-oowv](https://github.com/siHopp-oowv),
[sijow](https://github.com/sijow),
[skyfroger](https://github.com/skyfroger),
[songwupei](https://github.com/songwupei),
[stefkuypers](https://github.com/stefkuypers),
[stephan-koenig](https://github.com/stephan-koenig),
[stragu](https://github.com/stragu),
[sun123zxy](https://github.com/sun123zxy),
[thisisnic](https://github.com/thisisnic),
[tiagojct](https://github.com/tiagojct),
[timothoms](https://github.com/timothoms),
[tomicapretto](https://github.com/tomicapretto),
[venpopov](https://github.com/venpopov),
[victorrssx](https://github.com/victorrssx),
[visr](https://github.com/visr),
[vrbiki](https://github.com/vrbiki),
[widlarizer](https://github.com/widlarizer),
[winniehell](https://github.com/winniehell),
[wlatendresse](https://github.com/wlatendresse),
[wryfi](https://github.com/wryfi),
[xuefeng-xu](https://github.com/xuefeng-xu),
[yasyf](https://github.com/yasyf),
[yhkee0404](https://github.com/yhkee0404),
[zinc75](https://github.com/zinc75).
