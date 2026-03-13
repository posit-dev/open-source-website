---
title: Quarto 1.8
description: >
  Quarto 1.8 improves brand support, introduces brand extensions, adds HTML
  accessibility checks, and gives access to execution context.
categories:
  - Quarto 1.8
  - Releases
people:
  - Charlotte Wickham
date: '2025-10-13'
draft: false
image: thumbnail.png
image-alt: Quarto 1.8 with a lightbulb emoji
css: /docs/output-formats/autodark.css
ported_from: quarto
port_status: raw
---


Quarto 1.8 is available! You can get the current release from the [download page](../docs/download/index.qmd).

Quarto 1.8 improves support for light and dark brand colors and logos, brand extensions for sharing brands across Quarto projects, HTML accessibility checks powered by Axe-core, and access to more information about execution context from your code cells.
You can read about these improvements and some other highlights below. You can find all the changes in this version in the [Release Notes](../docs/download/changelog/1.8/).

## Dark and light colors and logos in brand

You can now specify `light` and `dark` versions of any colors or logo in a brand specification:

**\_brand.yml**

``` yaml
color:
  foreground:
    light: "#333333"
    dark: "#EEEEEE"
  background:
    light: "#EEEEEE"
    dark: "#333333"
logos:
  medium:
    light: logo.png
    dark: logo-white.png         
```

This works in `_brand.yml` files as well as `brand` specified directly in document metadata.
You can also present in dark mode by specifying `brand-mode: dark` in your `format: revealjs` presentations.

Read more in the updated [Guide \> Brand](../docs/authoring/brand.qmd):

- [Light and dark colors](../docs/authoring/brand.qmd#light-and-dark-colors)
- [Light and dark logos](../docs/authoring/brand.qmd#light-and-dark-logos)
- [Brand mode](../docs/authoring/brand.qmd#brand-mode)

## Brand extensions

Share brand definitions and assets across Quarto projects with a brand extension.

Get started with:

**Terminal**

``` default
quarto create extension brand
```

Read more in [Extensions \> Brand](../docs/extensions/brand.qmd), and keep an eye out for other ways to reuse and share your brand in future releases.

## Accessibility checks for HTML

You can add accessibility checks using the [Axe-core engine](https://github.com/dequelabs/axe-core) to HTML documents (`format`: `html`, `revealjs` and `dashboard`) with the new `axe` option.

For example, you can get a summary of violations right in your document preview:

<figure>
<img src="../docs/output-formats/images/axe-violation.png" class="border" data-fig-alt="A webpage with a box in the bottom left that warns &#39;Serious: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds&#39;." alt="A rendered webpage with an accessibility violation warning" />
<figcaption aria-hidden="true">A rendered webpage with an accessibility violation warning</figcaption>
</figure>

<figure>
<img src="../docs/output-formats/images/axe-violation.png" class="border autodark" data-fig-alt="A webpage with a box in the bottom left that warns &#39;Serious: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds&#39;." alt="A rendered webpage with an accessibility violation warning" />
<figcaption aria-hidden="true">A rendered webpage with an accessibility violation warning</figcaption>
</figure>

Read about your options in [HTML Accessibility Checks](../docs/output-formats/html-accessibility.qmd)

We know accessability is a big concern for many of our users, and more improvements will be coming in future releases.

## Accessing execution information

Quarto sets the `QUARTO_EXECUTE_INFO` environment variable, which allows you to access information about execution context from code cells.

Read the JSON file located at `QUARTO_EXECUTE_INFO` and access properties such as `document-path`, `format`, `metadata` and more:

## R

``` r
library(jsonlite)
execute_info <- read_json(Sys.getenv("QUARTO_EXECUTE_INFO"))
execute_info$`document-path`
```

## Python

``` python
import json
import os

with open(os.getenv("QUARTO_EXECUTE_INFO")) as f:
    execute_info = json.load(f)
execute_info["document-path"]
```

## Julia

``` julia
using JSON

execute_info = JSON.parsefile(ENV["QUARTO_EXECUTE_INFO"])
execute_info["document-path"]
```

Read more in [Access execution settings from code cells](../docs/advanced/quarto-execute-info.qmd).

## Other Highlights

- Access [metadata](../docs/extensions/lua-api.qmd#metadata-access) and [variables](../docs/extensions/lua-api.qmd#variables-access) in filters and shortcodes: Use the new `quarto.variables.get()` and `quarto.metadata.get()` APIs.

- The default LaTeX engine is now `lualatex`.

Dependency updates:

- `mermaidjs` updated to 11.6.0.
- Bootstrap icons updated to v1.13.1
- `QuartoNotebookRunner` in `julia` engine updated to 0.17.3

## Acknowledgements

We'd like to say a huge thank you to everyone who contributed to this release by opening issues and pull requests:

[Aariq](https://github.com/Aariq),
[AndreasThinks](https://github.com/AndreasThinks),
[ArthurData](https://github.com/ArthurData),
[Blake-Madden](https://github.com/Blake-Madden),
[ColinFay](https://github.com/ColinFay),
[DCEW](https://github.com/DCEW),
[DanStuder](https://github.com/DanStuder),
[Data-Wise](https://github.com/Data-Wise),
[EllaKaye](https://github.com/EllaKaye),
[EmilHvitfeldt](https://github.com/EmilHvitfeldt),
[FrankwaP](https://github.com/FrankwaP),
[GabrielCoffee9](https://github.com/GabrielCoffee9),
[GeorgRamer](https://github.com/GeorgRamer),
[Gewerd-Strauss](https://github.com/Gewerd-Strauss),
[GuillaumeDehaene](https://github.com/GuillaumeDehaene),
[HarunCelikOtto](https://github.com/HarunCelikOtto),
[HayesJohnD](https://github.com/HayesJohnD),
[Joao-O-Santos](https://github.com/Joao-O-Santos),
[MateusMolina](https://github.com/MateusMolina),
[MichaelHatherly](https://github.com/MichaelHatherly),
[PeteArm](https://github.com/PeteArm),
[Selbosh](https://github.com/Selbosh),
[SergeCroise](https://github.com/SergeCroise),
[SrShelo](https://github.com/SrShelo),
[VisruthSK](https://github.com/VisruthSK),
[Vistales](https://github.com/Vistales),
[abhiaagarwal](https://github.com/abhiaagarwal),
[aborruso](https://github.com/aborruso),
[adamblake](https://github.com/adamblake),
[adamiturabi](https://github.com/adamiturabi),
[alastairrushworth](https://github.com/alastairrushworth),
[albertomercurio](https://github.com/albertomercurio),
[alecloudenback](https://github.com/alecloudenback),
[alex-r-bigelow](https://github.com/alex-r-bigelow),
[allefeld](https://github.com/allefeld),
[alyst](https://github.com/alyst),
[andrewheiss](https://github.com/andrewheiss),
[andrewpbray](https://github.com/andrewpbray),
[austin-hoover](https://github.com/austin-hoover),
[batpigandme](https://github.com/batpigandme),
[bauerj](https://github.com/bauerj),
[benkeks](https://github.com/benkeks),
[benz0li](https://github.com/benz0li),
[bkowshik](https://github.com/bkowshik),
[blackerby](https://github.com/blackerby),
[boshek](https://github.com/boshek),
[brandonmontez](https://github.com/brandonmontez),
[bryce-carson](https://github.com/bryce-carson),
[carschandler](https://github.com/carschandler),
[christopherkenny](https://github.com/christopherkenny),
[cl-roberts](https://github.com/cl-roberts),
[cmadland](https://github.com/cmadland),
[co1emi11er2](https://github.com/co1emi11er2),
[coatless](https://github.com/coatless),
[cpcloud](https://github.com/cpcloud),
[daxkellie](https://github.com/daxkellie),
[dixslyf](https://github.com/dixslyf),
[dkapitan](https://github.com/dkapitan),
[econmaett](https://github.com/econmaett),
[edavidaja](https://github.com/edavidaja),
[edvinsyk](https://github.com/edvinsyk),
[ethanwhite](https://github.com/ethanwhite),
[fermarsan](https://github.com/fermarsan),
[fredguth](https://github.com/fredguth),
[fuhrmanator](https://github.com/fuhrmanator),
[gadenbuie](https://github.com/gadenbuie),
[georgestagg](https://github.com/georgestagg),
[ghisvail](https://github.com/ghisvail),
[ghost](https://github.com/ghost),
[github-actions\[bot\]](https://github.com/apps/github-actions),
[glin](https://github.com/glin),
[gregswinehart](https://github.com/gregswinehart),
[gwbrck](https://github.com/gwbrck),
[halleysfifthinc](https://github.com/halleysfifthinc),
[hansfn](https://github.com/hansfn),
[hchulkim](https://github.com/hchulkim),
[holtzy](https://github.com/holtzy),
[htbunn](https://github.com/htbunn),
[hturner](https://github.com/hturner),
[hugetim](https://github.com/hugetim),
[hutch3232](https://github.com/hutch3232),
[iagopinal](https://github.com/iagopinal),
[ihrke](https://github.com/ihrke),
[jameslairdsmith](https://github.com/jameslairdsmith),
[jdfoote](https://github.com/jdfoote),
[jeremy9959](https://github.com/jeremy9959),
[jfy133](https://github.com/jfy133),
[jkrumbiegel](https://github.com/jkrumbiegel),
[jmgirard](https://github.com/jmgirard),
[jonpeake](https://github.com/jonpeake),
[jvcarli](https://github.com/jvcarli),
[jxpeng98](https://github.com/jxpeng98),
[kandolfp](https://github.com/kandolfp),
[kapsner](https://github.com/kapsner),
[kathsherratt](https://github.com/kathsherratt),
[kazuyanagimoto](https://github.com/kazuyanagimoto),
[kevinah95](https://github.com/kevinah95),
[kippandrew](https://github.com/kippandrew),
[koldle](https://github.com/koldle),
[lachlansimpson](https://github.com/lachlansimpson),
[lbm364dl](https://github.com/lbm364dl),
[leovuong](https://github.com/leovuong),
[lostmygithubaccount](https://github.com/lostmygithubaccount),
[lu-kas](https://github.com/lu-kas),
[lukmanaj](https://github.com/lukmanaj),
[lwjohnst86](https://github.com/lwjohnst86),
[maelle](https://github.com/maelle),
[mahmudstat](https://github.com/mahmudstat),
[masud90](https://github.com/masud90),
[melaniewalsh](https://github.com/melaniewalsh),
[mfisher87](https://github.com/mfisher87),
[mipmip](https://github.com/mipmip),
[mpr1255](https://github.com/mpr1255),
[multimeric](https://github.com/multimeric),
[musvaage](https://github.com/musvaage),
[mvuorre](https://github.com/mvuorre),
[nathanj3](https://github.com/nathanj3),
[nessan](https://github.com/nessan),
[nichtich](https://github.com/nichtich),
[odysseu](https://github.com/odysseu),
[ofkoru](https://github.com/ofkoru),
[olivroy](https://github.com/olivroy),
[oyvindbso](https://github.com/oyvindbso),
[pagiraud](https://github.com/pagiraud),
[parmsam](https://github.com/parmsam),
[peter-gy](https://github.com/peter-gy),
[pm-gusmano](https://github.com/pm-gusmano),
[produnis](https://github.com/produnis),
[rabyj](https://github.com/rabyj),
[raffaem](https://github.com/raffaem),
[randyzwitch](https://github.com/randyzwitch),
[rben01](https://github.com/rben01),
[rossbowen](https://github.com/rossbowen),
[rundel](https://github.com/rundel),
[ryanzomorrodi](https://github.com/ryanzomorrodi),
[ryjohnson09](https://github.com/ryjohnson09),
[s2t2](https://github.com/s2t2),
[salim-b](https://github.com/salim-b),
[samcarter](https://github.com/samcarter),
[serialc](https://github.com/serialc),
[sgelzenleuchter](https://github.com/sgelzenleuchter),
[skriptum](https://github.com/skriptum),
[spaette](https://github.com/spaette),
[stragu](https://github.com/stragu),
[sun123zxy](https://github.com/sun123zxy),
[sverrirarnors](https://github.com/sverrirarnors),
[tecosaur](https://github.com/tecosaur),
[temospena](https://github.com/temospena),
[thatchermo](https://github.com/thatchermo),
[topepo](https://github.com/topepo),
[tylere](https://github.com/tylere),
[winniehell](https://github.com/winniehell),
[wklimowicz](https://github.com/wklimowicz),
[yogabonito](https://github.com/yogabonito),
[youcc](https://github.com/youcc),
[yves-amevoin](https://github.com/yves-amevoin),
[yyzeng](https://github.com/yyzeng).

The lightbulb emoji in the [listing and social card image](thumbnail.png) for this post comes from <a href="https://openmoji.org/" class="external">OpenMoji</a>-- the open-source emoji and icon project. License: <a href="https://creativecommons.org/licenses/by-sa/4.0/#" class="external">CC BY-SA 4.0</a>
