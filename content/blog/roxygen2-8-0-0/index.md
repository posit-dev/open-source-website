---
title: roxygen2 8.0.0
date: 2026-05-01T00:00:00.000Z
people:
  - Hadley Wickham
description: >
  roxygen2 8.0.0 is now on CRAN, with first-class support for S7, a bunch of R6
  improvements, a new configuration style, and a slimmer dependency footprint.
image: balloons.jpg
image-alt: >-
  Dozens of small, brightly coloured balloons drifting upward against a clear
  blue sky.
photo:
  url: https://unsplash.com/photos/assorted-colored-balloons-mid-airs-yRjLihK35Yw
  author: Al Soot
topics:
  - Best Practices
software:
  - roxygen2
languages:
  - R
tags:
  - Packages
hidesubscription: false
---


I'm pleased to announce that [roxygen2 8.0.0](https://roxygen2.r-lib.org) is now on CRAN.
roxygen2 turns specially formatted comments in your R code into the `.Rd` files that power R's help system.
You can install it with:

``` r
install.packages("roxygen2")
```

This release has been a long time in the making and includes well over a hundred bug fixes and improvements.
This post covers the highlights: new support for S7, a raft of improvements to R6 documentation, a more natural way to configure roxygen2 in your `DESCRIPTION`, the changes to rendered `.Rd` files you're most likely to see, and some other minor improvements, and a bunch of new vignettes.
You can read the full list of changes in the [release notes](https://github.com/r-lib/roxygen2/releases/tag/v8.0.0).

``` r
library(roxygen2)
```

## Documenting S7

The headline feature is initial support for [S7](https://rconsortium.github.io/S7/).
S7 is a new object-oriented programming system built to be a successor to S3 and S4.
It's been designed and implemented collaboratively by the R Consortium Object-Oriented Programming Working Group, which includes representatives from R-Core, Bioconductor, tidyverse/Posit, and the wider R community.
S7 is still a work in progress, but it is useful today, and adding roxygen2 support makes it easier to use in packages.

roxygen2 now supports documenting S7 generics, classes, and methods:

- **Generics** are documented just like regular functions.
- **Classes** are documented like regular functions (because S7 constructors are functions), but you can also use `@prop` to document properties that aren't constructor parameters.
  If you document several related classes on the same page, `@prop ClassName@prop_name description` lets you group properties by class.
- **Methods** registered with `method(generic, class) <- fn` are picked up automatically, and roxygen2 generates the right usage and aliases for you.

Read `vignette("rd-S7")` for a full rundown, and please let us know if you discover any issues or have suggestions for improvement!

## More ways to document R6

R6 got the biggest pile of improvements in this release, driven by years (!!)
of accumulated feedback.
The most important change is that you no longer need to document all methods inside the class definition.
If you add methods with `$set()`, you can now document them directly:

``` r
Counter <- R6::R6Class(
  "Counter",
  public = list(
    count = 0
  )
)

#' Increment the counter by `by`.
#' @param by Number to add.
Counter$set("public", "increment", function(by = 1) {
  self$count <- self$count + by
  invisible(self)
})
```

For more exotic cases where methods get attached through code that roxygen2 can't follow, there's now `@R6method Class$method`, which lets you document a method from anywhere in your package.

You can also now opt *out* of documenting pieces of a class.
Writing `@noRd` above an R6 method excludes it from the docs, and `@field name NULL` does the same for fields and active bindings.

Finally, inheritance got a significant upgrade.
When a method overrides one from a superclass, it now automatically inherits that parameter documentation --- so common parameters only have to be documented once, on the base class.
The same is true for inherited fields and active bindings.
This should cut down on a lot of duplication if you have a deep class hierarchy,

## A cleaner home for configuration

roxygen2 has historically been configured through a `Roxygen:` field in `DESCRIPTION`, with a separate `RoxygenNote` field recording the version.
This release introduces a more natural home using the `Config/roxygen2/` namespace that packages like testthat and lifecycle have adopted:

``` yaml
# before
Roxygen: list(markdown = TRUE)
RoxygenNote: 7.3.2

# after
Config/roxygen2/markdown: TRUE
Config/roxygen2/version: 8.0.0
```

The old fields still work, and roxygen2 will quietly migrate `RoxygenNote` the next time you run `devtools::document()`.
Over time, devtools and usethis will switch to the new form by default.

## Rendering tweaks

When you re-document your package for the first time with roxygen2 8.0.0, you might notice some small differences in the rendered output.
The most commonly encountered changes are:

- All generated cross-reference links now go through the same code path and share a single style, e.g. `\code{\link[=compose]{compose()}}`.

- Links to external packages now use the topic alias rather than the `.Rd` filename.
  This brings roxygen2 into alignment with current CRAN best practices.

- Tags that typically expect a single line of input now warn if you spread them across multiple lines.
  This catches a common class of silent mistakes, e.g. a `@name` or `@rdname` with no content that quietly included the next line of the block.
  This will create warnings for some existing legitimate uses, but I think the payoff (eliminating problems that are otherwise very hard to spot) is worth it.

- People with both `"aut"` and `"cre"` roles now appear in both the Authors and Maintainer sections of package documentation.

## Other important changes

roxygen2 now requires R 4.1 and no longer depends on purrr, stringr, or stringi.
Those last two are the big win because it means that stringi is now gone from the complete devtools dependency graph, making it easier to install for folks on constrained Linux images.

There's a new helper, `needs_roxygenize()`, that tells you whether your `.Rd` files are out of date by comparing modification times against their sources.
It's much cheaper than running `roxygenize()` just to find out nothing has changed, which makes it a good fit for pre-commit hooks or CI checks.

Finally, parameter inheritance has gained a small but very useful feature: `@inheritParams` now supports filtering, just like `@inheritDotParams`.
If you only want to inherit a subset of arguments from another function, you can now list them explicitly:

``` r
#' @inheritParams other_fn x y
```

Or exclude the ones you don't want:

``` r
#' @inheritParams other_fn -z
```

Speaking of `@inheritDotParams`, it now also works more like `@inheritParams`: it inherits documented parameters rather than formal arguments.
This may introduce new false positives (replacing the old approach's false negatives), which you can prevent by explicitly listing the argument names to inherit.

## New vignettes

roxygen2's own documentation has had a significant tidy-up.
The old `vignette("rd-other")` has been broken into focused vignettes --- `vignette("rd-datasets")`, `vignette("rd-packages")`, `vignette("rd-S3")`, `vignette("rd-S4")`, and `vignette("rd-R6")` --- with the new `vignette("rd-S7")` joining them.
The main `vignette("rd")` has been renamed to `vignette("rd-functions")`, and the "getting started" content has moved to `vignette("roxygen2")`.

`vignette("rd-S3")` has also been rewritten with clearer guidance for documenting S3 generics, classes, and methods, including how to use the new [doclisting](https://doclisting.r-lib.org/) package to automatically list methods for a generic --- a long-standing pain point for generics with methods in multiple packages.
You can also use doclisting with S4 and S7 generics.

## Acknowledgements

A big thank you to everyone who has contributed issues, pull requests, and discussion since the last release!
[@achubaty](https://github.com/achubaty), [@adithya604](https://github.com/adithya604), [@akersting](https://github.com/akersting), [@alandipert](https://github.com/alandipert), [@alannearme](https://github.com/alannearme), [@alecw](https://github.com/alecw), [@alexgenin](https://github.com/alexgenin), [@AlexisDerumigny](https://github.com/AlexisDerumigny), [@AliSajid](https://github.com/AliSajid), [@alisonmosky](https://github.com/alisonmosky), [@aljabadi](https://github.com/aljabadi), [@allenzhuaz](https://github.com/allenzhuaz), [@andrew-schulman](https://github.com/andrew-schulman), [@andrewmarx](https://github.com/andrewmarx), [@aphalo](https://github.com/aphalo), [@apreshill](https://github.com/apreshill), [@arilamstein](https://github.com/arilamstein), [@arnaudgallou](https://github.com/arnaudgallou), [@ashbythorpe](https://github.com/ashbythorpe), [@ateucher](https://github.com/ateucher), [@b-niu](https://github.com/b-niu), [@bahadzie](https://github.com/bahadzie), [@balthasars](https://github.com/balthasars), [@BartJanvanRossum](https://github.com/BartJanvanRossum), [@bastistician](https://github.com/bastistician), [@batpigandme](https://github.com/batpigandme), [@beginb](https://github.com/beginb), [@BenEngbers](https://github.com/BenEngbers), [@BenWiseman](https://github.com/BenWiseman), [@bgctw](https://github.com/bgctw), [@BGWKlein](https://github.com/BGWKlein), [@bhagwataditya](https://github.com/bhagwataditya), [@billdenney](https://github.com/billdenney), [@Bisaloo](https://github.com/Bisaloo), [@bluewomble](https://github.com/bluewomble), [@bobjansen](https://github.com/bobjansen), [@boshek](https://github.com/boshek), [@brendanf](https://github.com/brendanf), [@brodieG](https://github.com/brodieG), [@BroVic](https://github.com/BroVic), [@brpetrucci](https://github.com/brpetrucci), [@brry](https://github.com/brry), [@bryanhanson](https://github.com/bryanhanson), [@bwiernik](https://github.com/bwiernik), [@cbielow](https://github.com/cbielow), [@cboettig](https://github.com/cboettig), [@cderv](https://github.com/cderv), [@CGMossa](https://github.com/CGMossa), [@chlebowa](https://github.com/chlebowa), [@chrarnold](https://github.com/chrarnold), [@ChristopherEeles](https://github.com/ChristopherEeles), [@chrk623](https://github.com/chrk623), [@chuxinyuan](https://github.com/chuxinyuan), [@cjyetman](https://github.com/cjyetman), [@coatless](https://github.com/coatless), [@ColinFay](https://github.com/ColinFay), [@courtiol](https://github.com/courtiol), [@cthombor](https://github.com/cthombor), [@d-morrison](https://github.com/d-morrison), [@d-sci](https://github.com/d-sci), [@daattali](https://github.com/daattali), [@DanChaltiel](https://github.com/DanChaltiel), [@DanielHermosilla](https://github.com/DanielHermosilla), [@danielvartan](https://github.com/danielvartan), [@DarioS](https://github.com/DarioS), [@davidrubinger](https://github.com/davidrubinger), [@DavisVaughan](https://github.com/DavisVaughan), [@daynefiler](https://github.com/daynefiler), [@dfrankow](https://github.com/dfrankow), [@dgkf](https://github.com/dgkf), [@dieghernan](https://github.com/dieghernan), [@dipterix](https://github.com/dipterix), [@dmurdoch](https://github.com/dmurdoch), [@dpprdan](https://github.com/dpprdan), [@drag05](https://github.com/drag05), [@dragosmg](https://github.com/dragosmg), [@dsweber2](https://github.com/dsweber2), [@dvg-p4](https://github.com/dvg-p4), [@dwachsmuth](https://github.com/dwachsmuth), [@eddelbuettel](https://github.com/eddelbuettel), [@eitsupi](https://github.com/eitsupi), [@ejosymart](https://github.com/ejosymart), [@elcortegano](https://github.com/elcortegano), [@ElsLommelen](https://github.com/ElsLommelen), [@espinielli](https://github.com/espinielli), [@FelixErnst](https://github.com/FelixErnst), [@florisvdh](https://github.com/florisvdh), [@flrd](https://github.com/flrd), [@gaborcsardi](https://github.com/gaborcsardi), [@GABurns](https://github.com/GABurns), [@galachad](https://github.com/galachad), [@gavinsimpson](https://github.com/gavinsimpson), [@genomaths](https://github.com/genomaths), [@ggrothendieck](https://github.com/ggrothendieck), [@ghost](https://github.com/ghost), [@goldingn](https://github.com/goldingn), [@gowerc](https://github.com/gowerc), [@gregorgorjanc](https://github.com/gregorgorjanc), [@gustavdelius](https://github.com/gustavdelius), [@gwd666](https://github.com/gwd666), [@hadley](https://github.com/hadley), [@harrelfe](https://github.com/harrelfe), [@hdarjus](https://github.com/hdarjus), [@HenningLorenzen-ext-bayer](https://github.com/HenningLorenzen-ext-bayer), [@HenrikBengtsson](https://github.com/HenrikBengtsson), [@hongooi73](https://github.com/hongooi73), [@hughjonesd](https://github.com/hughjonesd), [@iferres](https://github.com/iferres), [@IndrajeetPatil](https://github.com/IndrajeetPatil), [@J-Moravec](https://github.com/J-Moravec), [@jakubnowicki](https://github.com/jakubnowicki), [@jameslamb](https://github.com/jameslamb), [@jan-abel-inwt](https://github.com/jan-abel-inwt), [@JanaJarecki](https://github.com/JanaJarecki), [@JanMarvin](https://github.com/JanMarvin), [@JantekM](https://github.com/JantekM), [@jcubic](https://github.com/jcubic), [@JDenn0514](https://github.com/JDenn0514), [@jdprimus](https://github.com/jdprimus), [@jeffcraggy](https://github.com/jeffcraggy), [@jennybc](https://github.com/jennybc), [@jensmassberg](https://github.com/jensmassberg), [@jeroen](https://github.com/jeroen), [@jeroenjanssens](https://github.com/jeroenjanssens), [@JesseAlderliesten](https://github.com/JesseAlderliesten), [@jgellar](https://github.com/jgellar), [@jgutman](https://github.com/jgutman), [@JiaxiangBU](https://github.com/JiaxiangBU), [@Jiefei-Wang](https://github.com/Jiefei-Wang), [@jimhester](https://github.com/jimhester), [@jmbarbone](https://github.com/jmbarbone), [@jmpanfil](https://github.com/jmpanfil), [@johanneswerner](https://github.com/johanneswerner), [@johnbaums](https://github.com/johnbaums), [@JohnCoene](https://github.com/JohnCoene), [@JonathanUrbach](https://github.com/JonathanUrbach), [@jonkeane](https://github.com/jonkeane), [@jonocarroll](https://github.com/jonocarroll), [@jonthegeek](https://github.com/jonthegeek), [@JosiahParry](https://github.com/JosiahParry), [@jranke](https://github.com/jranke), [@JulieBlasquiz](https://github.com/JulieBlasquiz), [@jwijffels](https://github.com/jwijffels), [@kamapu](https://github.com/kamapu), [@karchjd](https://github.com/karchjd), [@karoliskoncevicius](https://github.com/karoliskoncevicius), [@kathi-munk](https://github.com/kathi-munk), [@kellijohnson-NOAA](https://github.com/kellijohnson-NOAA), [@kevinushey](https://github.com/kevinushey), [@kingaa](https://github.com/kingaa), [@klmr](https://github.com/klmr), [@Klorator](https://github.com/Klorator), [@kongdd](https://github.com/kongdd), [@kortschak](https://github.com/kortschak), [@kostrzewa](https://github.com/kostrzewa), [@kpagacz](https://github.com/kpagacz), [@krivit](https://github.com/krivit), [@krlmlr](https://github.com/krlmlr), [@kurt-o-sys](https://github.com/kurt-o-sys), [@kylebutts](https://github.com/kylebutts), [@lgatto](https://github.com/lgatto), [@lindeloev](https://github.com/lindeloev), [@LiNk-NY](https://github.com/LiNk-NY), [@lionel-](https://github.com/lionel-), [@llrs](https://github.com/llrs), [@llrs-roche](https://github.com/llrs-roche), [@lorenzwalthert](https://github.com/lorenzwalthert), [@LouisLeNezet](https://github.com/LouisLeNezet), [@LukasWallrich](https://github.com/LukasWallrich), [@lukasz-bednarz-reddeersystems](https://github.com/lukasz-bednarz-reddeersystems), [@m-muecke](https://github.com/m-muecke), [@maelle](https://github.com/maelle), [@malcolmbarrett](https://github.com/malcolmbarrett), [@mamueller](https://github.com/mamueller), [@math-mcshane](https://github.com/math-mcshane), [@maxheld83](https://github.com/maxheld83), [@MaximilianPi](https://github.com/MaximilianPi), [@mbojan](https://github.com/mbojan), [@mccarthy-m-g](https://github.com/mccarthy-m-g), [@mccroweyclinton-EPA](https://github.com/mccroweyclinton-EPA), [@mcol](https://github.com/mcol), [@mcsage](https://github.com/mcsage), [@MichaelChirico](https://github.com/MichaelChirico), [@michaelquinn32](https://github.com/michaelquinn32), [@mikemahoney218](https://github.com/mikemahoney218), [@mikkmart](https://github.com/mikkmart), [@mikmart](https://github.com/mikmart), [@MilesMcBain](https://github.com/MilesMcBain), [@mine-cetinkaya-rundel](https://github.com/mine-cetinkaya-rundel), [@MislavSag](https://github.com/MislavSag), [@mjsteinbaugh](https://github.com/mjsteinbaugh), [@mkoohafkan](https://github.com/mkoohafkan), [@MLopez-Ibanez](https://github.com/MLopez-Ibanez), [@mnazarov](https://github.com/mnazarov), [@mnneely](https://github.com/mnneely), [@monkeywithacupcake](https://github.com/monkeywithacupcake), [@moodymudskipper](https://github.com/moodymudskipper), [@mpadge](https://github.com/mpadge), [@mrchypark](https://github.com/mrchypark), [@ms609](https://github.com/ms609), [@msaltieri](https://github.com/msaltieri), [@msberends](https://github.com/msberends), [@mschilli87](https://github.com/mschilli87), [@multimeric](https://github.com/multimeric), [@muschellij2](https://github.com/muschellij2), [@musvaage](https://github.com/musvaage), [@naikymen](https://github.com/naikymen), [@nathaneastwood](https://github.com/nathaneastwood), [@nbenn](https://github.com/nbenn), [@nealrichardson](https://github.com/nealrichardson), [@Nelson-Gon](https://github.com/Nelson-Gon), [@neshvig10](https://github.com/neshvig10), [@netique](https://github.com/netique), [@ngreifer](https://github.com/ngreifer), [@nick-robo](https://github.com/nick-robo), [@NikNakk](https://github.com/NikNakk), [@nlneas1](https://github.com/nlneas1), [@nouvrita](https://github.com/nouvrita), [@nr0cinu](https://github.com/nr0cinu), [@nteetor](https://github.com/nteetor), [@ntguardian](https://github.com/ntguardian), [@oharar](https://github.com/oharar), [@okhoma](https://github.com/okhoma), [@olivroy](https://github.com/olivroy), [@orgadish](https://github.com/orgadish), [@p-carter](https://github.com/p-carter), [@p00ya](https://github.com/p00ya), [@pakjiddat](https://github.com/pakjiddat), [@pat-s](https://github.com/pat-s), [@PauloJhonny](https://github.com/PauloJhonny), [@PavelBal](https://github.com/PavelBal), [@pbreheny](https://github.com/pbreheny), [@phargarten2](https://github.com/phargarten2), [@pnacht](https://github.com/pnacht), [@pvanlaake](https://github.com/pvanlaake), [@ralmond](https://github.com/ralmond), [@ramiromagno](https://github.com/ramiromagno), [@RaphaelS1](https://github.com/RaphaelS1), [@retostauffer](https://github.com/retostauffer), [@RiboRings](https://github.com/RiboRings), [@richelbilderbeek](https://github.com/richelbilderbeek), [@rjake](https://github.com/rjake), [@RMHogervorst](https://github.com/RMHogervorst), [@robchallen](https://github.com/robchallen), [@Robinlovelace](https://github.com/Robinlovelace), [@romainfrancois](https://github.com/romainfrancois), [@rorynolan](https://github.com/rorynolan), [@rossellhayes](https://github.com/rossellhayes), [@rsbivand](https://github.com/rsbivand), [@russHyde](https://github.com/russHyde), [@rvernica](https://github.com/rvernica), [@s-fleck](https://github.com/s-fleck), [@saipenikalapati](https://github.com/saipenikalapati), [@Salatbesteck](https://github.com/Salatbesteck), [@salim-b](https://github.com/salim-b), [@sbgraves237](https://github.com/sbgraves237), [@sboehringer](https://github.com/sboehringer), [@schloerke](https://github.com/schloerke), [@schradj](https://github.com/schradj), [@sckott](https://github.com/sckott), [@sebffischer](https://github.com/sebffischer), [@setgree](https://github.com/setgree), [@ShixiangWang](https://github.com/ShixiangWang), [@simonpcouch](https://github.com/simonpcouch), [@simonsays1980](https://github.com/simonsays1980), [@simpar1471](https://github.com/simpar1471), [@slager](https://github.com/slager), [@smilberg](https://github.com/smilberg), [@stefanfritsch](https://github.com/stefanfritsch), [@stefanoborini](https://github.com/stefanoborini), [@stellathecat](https://github.com/stellathecat), [@stemangiola](https://github.com/stemangiola), [@stla](https://github.com/stla), [@strazto](https://github.com/strazto), [@strboul](https://github.com/strboul), [@sven-stodtmann](https://github.com/sven-stodtmann), [@swnydick](https://github.com/swnydick), [@t-kalinowski](https://github.com/t-kalinowski), [@TanguyBarthelemy](https://github.com/TanguyBarthelemy), [@tappek](https://github.com/tappek), [@tau31](https://github.com/tau31), [@tdhock](https://github.com/tdhock), [@ThierryO](https://github.com/ThierryO), [@tjebo](https://github.com/tjebo), [@TomKellyGenetics](https://github.com/TomKellyGenetics), [@tommarshall2](https://github.com/tommarshall2), [@trusch139](https://github.com/trusch139), [@turgeonmaxime](https://github.com/turgeonmaxime), [@tzakharko](https://github.com/tzakharko), [@uhkeller](https://github.com/uhkeller), [@unDocUMeantIt](https://github.com/unDocUMeantIt), [@vertesy](https://github.com/vertesy), [@VPetukhov](https://github.com/VPetukhov), [@wch](https://github.com/wch), [@wibeasley](https://github.com/wibeasley), [@wilcoxa](https://github.com/wilcoxa), [@wurli](https://github.com/wurli), [@wviechtb](https://github.com/wviechtb), [@yogat3ch](https://github.com/yogat3ch), [@Yunuuuu](https://github.com/Yunuuuu), [@yutannihilation](https://github.com/yutannihilation), [@zachary-foster](https://github.com/zachary-foster), [@zeehio](https://github.com/zeehio), [@zettlchen](https://github.com/zettlchen), and [@zkamvar](https://github.com/zkamvar).
