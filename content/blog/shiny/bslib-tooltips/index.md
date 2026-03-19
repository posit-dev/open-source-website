---
title: 'Shiny for R updates: tooltips, popovers, a new theme, and more'
description: >
  An overview of recent Shiny for R updates, including tooltips, popovers, a new
  theme, and more.
people:
  - Carson Sievert
  - Garrick Aden-Buie
date: '2023-08-16'
image: feature.png
ported_from: shiny
port_status: in-progress
software: ["bslib", "shiny-r"]
languages: ["R"]
---


<script src="index_files/libs/bslib-component-js-0.10.0/components.min.js"></script>
<script src="index_files/libs/bslib-component-js-0.10.0/web-components.min.js" type="module"></script>
<link href="index_files/libs/bslib-component-css-0.10.0/components.css" rel="stylesheet" />
<script src="index_files/libs/bslib-tag-require-0.10.0/tag-require.js"></script>


<style>
.quarto-video> div {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
}
.cell-output-display {
  padding-left: 1rem;
}
</style>

The Shiny team is delighted to share that we've just released updates for 12 different R packages that contribute to the Shiny experience.
These updates include many improvements and bug fixes that aren't explicitly covered here, but the [release notes section](#release-notes) of this post provides links to the full list of changes for each package.
That said, there are a few new features in `bslib` that we're particularly excited to highlight for you!

## bslib

In [the last release of `bslib` (0.5.0)](../../../blog/shiny/bslib-dashboards/), we made significant strides towards `bslib` being our recommended way to [build modern Shiny dashboards](https://rstudio.github.io/bslib/articles/dashboards/index.html).
In this release, we've added more features to help you make even better dashboards.

### Tooltips and popovers

One essential quality of any great website is that it provides the user with the right amount of information at the right time.
In technically-oriented apps, you might want to provide a definition for a term, a description of a model parameter, or an input that updates a specific plot, but you don't want these details to overwhelm the user when they're not needed.

In this release, we've added `bslib::tooltip()` and `bslib::popover()` to help you do just that.
By putting this additional information in a tooltip or these additional controls in a popover, you can provide the detail your users need on demand, right where they need it.

Here's a quick demo.
In this example, we have a [card](https://rstudio.github.io/bslib/articles/cards/index.html) containing a plot that compares the body mass of our favorite [penguins](https://allisonhorst.github.io/palmerpenguins/) across species.
We've leveraged `bslib`'s new tooltip and popover features in a few ways:

1.  An info icon next to the card title includes a [tooltip](https://rstudio.github.io/bslib/reference/tooltip.html) that describes how the penguin body mass is measured.

2.  A gear icon in the upper left corner of the card includes a [popover](https://rstudio.github.io/bslib/reference/popover.html) with a few controls for customizing the plot.

3.  In the footer, a "Learn more" link opens a [popover](https://rstudio.github.io/bslib/reference/popover.html) with the full citation for the data used in the plot.

{{< video src="tooltips-popovers.mp4" title="Using bslib's tooltip and popover functionality to provide more detail on demand" >}}

<p>
<a  href="https://posit.cloud/content/6298796" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="01-tooltips-popovers.R"> <i class="me-1" style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i> Try on Posit Cloud </a> <a class="ms-1" href="https://gist.github.com/cpsievert/7a93ff167aebf474873493d566ab9e07#file-01-tooltips-popovers-r" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" title="View Source Code"> <i  style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i> <span>Source</span></a>
</p>

<p>
<i></i>
Learn more in the new
<a href="https://rstudio.github.io/bslib/articles/tooltips-popovers/index.html">Tooltips & Popovers article</a>.
</p>

### Towards a new Shiny theme

This release of `bslib` introduces a new theme that we intend on making the default experience for `bslib`-powered apps.
Since this theme is still a work-in-progress, you must currently must be opt-in to use it by providing `bs_theme(preset = "shiny")` to the `theme` argument of the relevant page function, for example:

``` r
library(shiny)
library(bslib)

ui <- page_sidebar(
  theme = bs_theme(preset = "shiny"),
  # ...
)
```

The screen recording below gives you a preview of the new Shiny preset theme.
One exciting difference between the Shiny preset and other [Bootswatch themes](https://bootswatch.com/), is that we've taken this opportunity to re-think the appearance of Shiny-specific widgets, like `sliderInput()` and `selectInput()`.

Want to see this theme in action? Just install the updated `bslib` package and run `bslib::bs_theme_preview()` in your R console!

{{< video src="shiny-theme.mp4" title="Changing from the current default theme to the new theme" >}}

<p>
<a  href="https://posit.cloud/content/6298796" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="02-new-theme.R">  <i class="me-1" style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i> Try on Posit Cloud </a> <a class="ms-1" href="https://gist.github.com/cpsievert/7a93ff167aebf474873493d566ab9e07#file-02-new-theme-r" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" title="View Source Code"> <i  style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i> <span>Source</span></a>
</p>

<p>
<i></i>
Learn more about
<a href="https://rstudio.github.io/bslib/articles/theming/index.html">real-time theming with bslib</a>.
</p>

### Improved Quarto integration

Since `bslib` components are designed to both work with Shiny and to render statically they can be added to [any Bootstrap-compatible page](https://rstudio.github.io/bslib/articles/any-project/index.html).

In practice, however, due to nuances in how Quarto provides Boostrap, some `bslib` components weren't quite working as expected in Quarto documents.
But this release fixes that issue!

To demonstrate, here's an example of a fullscreen-capable [`bslib::card()`](https://rstudio.github.io/bslib/articles/cards/index.html) in a Quarto document.

{{< video src="quarto-bslib.mp4" title="Putting a fullscreen-capable bslib card in a Quarto document" >}}

<p>
<a  href="https://posit.cloud/content/6298796" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="03-quarto-bslib.qmd"> <i class="me-1" style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i> Try on Posit Cloud </a> <a class="ms-1" href="https://gist.github.com/cpsievert/7a93ff167aebf474873493d566ab9e07#file-03-quarto-bslib-qmd" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" title="View Source Code"> <i  style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i> <span>Source</span></a>
</p>

<p>
<i></i>
You can also
<a href="https://rstudio.github.io/bslib/articles/any-project/index.html#r-markdown">use bslib components in R Markdown</a>.
</p>

### New `input_switch()`

Turning a feature on or off is a common action in many Shiny apps.
With Shiny's default UI, this is typically done with a [`checkboxInput()`](https://shiny.rstudio.com/reference/shiny/latest/checkboxInput.html).
But checkboxes don't always give an obvious visual cue of turning an option on or off.

In this release, we've added a new `input_switch()` with a modern appearance.
Here's a quick live preview of how it looks and feels:

``` r
bslib::input_switch("switch", "Turn Up Awesomeness", FALSE)
```

<div class="form-group shiny-input-container" data-require-bs-version="5" data-require-bs-caller="input_switch()">
<div class="bslib-input-switch form-switch form-check">
<input id="switch" class="form-check-input" type="checkbox" role="switch"/>
<label class="form-check-label" for="switch">
<span>Turn Up Awesomeness</span>
</label>
</div>
</div>

> **None**
>
> The new `bslib` is <span id="extra">**extra, extra**</span> awesome!

<script>
document.getElementById("switch").addEventListener("click", (ev) => {
  const extra = document.getElementById("extra");
  extra.classList.toggle("d-none", !ev.target.checked);
});
</script>

## Looking forward

We're excited to continue improving Shiny for R, and in the near-term we plan to focus on making `bslib` a more complete UI framework with great looking defaults.
Here are a few things currently towards the top of our roadmap:

- Make the new Shiny preset theme the default for `bslib`-powered apps.
  - We have refreshed style updates in the works for `card()`s, `sidebar()`, and much more.
  - And we'd love to get your feedback on the new theme!
- More UI components, such as [offcanvas](https://getbootstrap.com/docs/5.3/components/offcanvas/), [button groups](https://getbootstrap.com/docs/5.3/components/button-group/), etc.
- More incorporation of `bslib` as part of the [Getting Started experience](https://shiny.posit.co/r/getstarted/shiny-basics/lesson1/index.html) on [shiny.posit.co](https://shiny.posit.co/).
- More `bslib`-focused example galleries, starter templates, and articles.

> **Join us at posit::conf(2023)!**
>
> We're also excited to see you at [posit::conf(2023)](https://posit.co/conference/) this September! Currently, there are [35 sessions](https://reg.conf.posit.co/flow/posit/positconf23/attendee-portal/page/sessioncatalog?mkt_tok=NzA5LU5YTi03MDYAAAGMOwicGCTQ0Fdw5xeRt2ICgRdWcmS5wjLMqYn9lIzlZxV_RurIIbKDnx8O9POcnDuz7Fu5IGLG_FegVO8iDE08HrjnqmwQs5JKRs9qk2sS7Ac&search=shiny) on the schedule that mention Shiny, including a handful of UI-focused [workshops](https://reg.conf.posit.co/flow/posit/positconf23/attendee-portal/page/sessioncatalog?mkt_tok=NzA5LU5YTi03MDYAAAGMOwicGCTQ0Fdw5xeRt2ICgRdWcmS5wjLMqYn9lIzlZxV_RurIIbKDnx8O9POcnDuz7Fu5IGLG_FegVO8iDE08HrjnqmwQs5JKRs9qk2sS7Ac&search=shiny&search.sessiontype=1675316728702001wr6r) and [talks](https://reg.conf.posit.co/flow/posit/positconf23/attendee-portal/page/sessioncatalog?mkt_tok=NzA5LU5YTi03MDYAAAGMOwicGCTQ0Fdw5xeRt2ICgRdWcmS5wjLMqYn9lIzlZxV_RurIIbKDnx8O9POcnDuz7Fu5IGLG_FegVO8iDE08HrjnqmwQs5JKRs9qk2sS7Ac&search=bslib&search.sessiontype=1684338401751002OADN&search.sessiontopics=1684779688709001hs5K).

## Release notes

There are a lot of changes and updates in the Shiny universe that we haven't covered in this post.
Dive into the release notes linked below to learn more about changes in each package.

**Thank you, everyone!** 💙
We'd like to thank everyone who contributed to all of the packages released in this cycle.
Your contributions are what make Shiny great!

### bslib [v0.5.1](https://rstudio.github.io/bslib/news/index.html#bslib-051)

[@ariebh](https://github.com/ariebh), [@asadow](https://github.com/asadow), [@chrisbrownlie](https://github.com/chrisbrownlie), [@cpsievert](https://github.com/cpsievert), [@ctrlxctrlc](https://github.com/ctrlxctrlc), [@daattali](https://github.com/daattali), [@gadenbuie](https://github.com/gadenbuie), [@ideusoes](https://github.com/ideusoes), [@Liripo](https://github.com/Liripo), [@michael-dewar](https://github.com/michael-dewar), [@nteetor](https://github.com/nteetor), [@PaulC91](https://github.com/PaulC91), [@philiph99](https://github.com/philiph99), [@riskcede](https://github.com/riskcede), [@schloerke](https://github.com/schloerke), [@Teebusch](https://github.com/Teebusch), [@tillea](https://github.com/tillea), and [@wch](https://github.com/wch).

### shiny [v1.7.5](https://shiny.posit.co/r/reference/shiny/1.7.5/upgrade.html)

[@AlexWaterboyBezzina](https://github.com/AlexWaterboyBezzina), [@apalacio9502](https://github.com/apalacio9502), [@aronatkins](https://github.com/aronatkins), [@asadow](https://github.com/asadow), [@BajczA475](https://github.com/BajczA475), [@barracuda156](https://github.com/barracuda156), [@brooksambrose](https://github.com/brooksambrose), [@cpsievert](https://github.com/cpsievert), [@daattali](https://github.com/daattali), [@dipterix](https://github.com/dipterix), [@dkori](https://github.com/dkori), [@drag05](https://github.com/drag05), [@dvg-p4](https://github.com/dvg-p4), [@emillykkejensen](https://github.com/emillykkejensen), [@EricKrantz](https://github.com/EricKrantz), [@gadenbuie](https://github.com/gadenbuie), [@galachad](https://github.com/galachad), [@Gathuh](https://github.com/Gathuh), [@GShotwell](https://github.com/GShotwell), [@hadley](https://github.com/hadley), [@hcsun1](https://github.com/hcsun1), [@ifoxfoot](https://github.com/ifoxfoot), [@ismirsehregal](https://github.com/ismirsehregal), [@jcheng5](https://github.com/jcheng5), [@jessekps](https://github.com/jessekps), [@johnkarlen](https://github.com/johnkarlen), [@juwitt](https://github.com/juwitt), [@kathi-resan](https://github.com/kathi-resan), [@kennedymwavu](https://github.com/kennedymwavu), [@kevinushey](https://github.com/kevinushey), [@king-of-poppk](https://github.com/king-of-poppk), [@KRRLP-PL](https://github.com/KRRLP-PL), [@Liripo](https://github.com/Liripo), [@magarick](https://github.com/magarick), [@MalteSteinCytel](https://github.com/MalteSteinCytel), [@matt4815162342](https://github.com/matt4815162342), [@maxheld83](https://github.com/maxheld83), [@Mkranj](https://github.com/Mkranj), [@nolanjj](https://github.com/nolanjj), [@norahAlbarrak](https://github.com/norahAlbarrak), [@pawelru](https://github.com/pawelru), [@pbosetti](https://github.com/pbosetti), [@RaviSekha](https://github.com/RaviSekha), [@RosalynLP](https://github.com/RosalynLP), [@sanjmeh](https://github.com/sanjmeh), [@SarenT](https://github.com/SarenT), [@schloerke](https://github.com/schloerke), [@shahronak47](https://github.com/shahronak47), [@stefanedwards](https://github.com/stefanedwards), [@stla](https://github.com/stla), [@stuvet](https://github.com/stuvet), [@timbrock](https://github.com/timbrock), [@tomjemmett](https://github.com/tomjemmett), [@vivigirardin](https://github.com/vivigirardin), [@vnijs](https://github.com/vnijs), [@wch](https://github.com/wch), and [@Zhenglei-BCS](https://github.com/Zhenglei-BCS).

### htmltools [v0.5.6](https://rstudio.github.io/htmltools/news/index.html#htmltools-056)

[@ccamara](https://github.com/ccamara), [@cpsievert](https://github.com/cpsievert), [@daattali](https://github.com/daattali), [@gadenbuie](https://github.com/gadenbuie), [@PaulC91](https://github.com/PaulC91), [@schloerke](https://github.com/schloerke), [@ShixiangWang](https://github.com/ShixiangWang), and [@warnes](https://github.com/warnes).

### flexdashboard [v0.6.2](https://rstudio.github.io/flexdashboard/news/index.html#flexdashboard-062)

[@actuarial-lonewolf](https://github.com/actuarial-lonewolf), [@cpsievert](https://github.com/cpsievert), [@danielludolf](https://github.com/danielludolf), [@DataStrategist](https://github.com/DataStrategist), [@erm-eanway](https://github.com/erm-eanway), [@gadenbuie](https://github.com/gadenbuie), and [@nplatonov](https://github.com/nplatonov).

### leaflet [v2.1.3](https://github.com/rstudio/leaflet/blob/main/NEWS#leaflet-213)

[@antoine4ucsd](https://github.com/antoine4ucsd), [@daattali](https://github.com/daattali), [@gadenbuie](https://github.com/gadenbuie), [@Jakka](https://github.com/Jakka), [@jaseeverett](https://github.com/jaseeverett), [@johnbaums](https://github.com/johnbaums), [@JosephStewart](https://github.com/JosephStewart), [@Landon-Getting](https://github.com/Landon-Getting), [@lime-n](https://github.com/lime-n), [@Rafnuss](https://github.com/Rafnuss), [@ramyareddy161](https://github.com/ramyareddy161), [@rhijmans](https://github.com/rhijmans), [@rl-utility-man](https://github.com/rl-utility-man), and [@warnes](https://github.com/warnes).

### leaflet.providers [v1.13.0](https://rstudio.github.io/leaflet.providers/news/index.html#leafletproviders-1130)

[@gadenbuie](https://github.com/gadenbuie), [@jennybc](https://github.com/jennybc), [@joker234](https://github.com/joker234), [@kent37](https://github.com/kent37), [@mgzjys](https://github.com/mgzjys), and [@schloerke](https://github.com/schloerke).

### shinytest2 [v0.3.0](https://rstudio.github.io/shinytest2/news/index.html#shinytest2-030)

[@andrewbaxter439](https://github.com/andrewbaxter439), [@arepsz](https://github.com/arepsz), [@AskPascal](https://github.com/AskPascal), [@cpsievert](https://github.com/cpsievert), [@epruesse](https://github.com/epruesse), [@gadenbuie](https://github.com/gadenbuie), [@gladkia](https://github.com/gladkia), [@hugo-pH](https://github.com/hugo-pH), [@matt-sd-watson](https://github.com/matt-sd-watson), [@maxheld83](https://github.com/maxheld83), [@parmsam-pfizer](https://github.com/parmsam-pfizer), [@PaulinCharliquart](https://github.com/PaulinCharliquart), [@schloerke](https://github.com/schloerke), [@stla](https://github.com/stla), and [@sybrohee](https://github.com/sybrohee).

### chromote [v0.1.2](https://rstudio.github.io/chromote/news/index.html#chromote-012)

[@ashbythorpe](https://github.com/ashbythorpe), [@gadenbuie](https://github.com/gadenbuie), [@hadley](https://github.com/hadley), [@Ljupch0](https://github.com/Ljupch0), [@moladokun](https://github.com/moladokun), [@mrcaseb](https://github.com/mrcaseb), [@nick-youngblut](https://github.com/nick-youngblut), [@stla](https://github.com/stla), [@Waschoi](https://github.com/Waschoi), [@wch](https://github.com/wch), and [@yogat3ch](https://github.com/yogat3ch).

### webshot2 [v0.1.1](https://rstudio.github.io/webshot2/news/index.html#webshot2-011)

[@aengels-git](https://github.com/aengels-git), [@brunomioto](https://github.com/brunomioto), [@cderv](https://github.com/cderv), [@charleswidnall](https://github.com/charleswidnall), [@egehankinik](https://github.com/egehankinik), [@gadenbuie](https://github.com/gadenbuie), [@iMissile](https://github.com/iMissile), [@kangjf1943](https://github.com/kangjf1943), [@lijinbio](https://github.com/lijinbio), [@Liripo](https://github.com/Liripo), [@Minh-AnhHuynh](https://github.com/Minh-AnhHuynh), [@PatrickRWright](https://github.com/PatrickRWright), [@RKonstantinR](https://github.com/RKonstantinR), [@schloerke](https://github.com/schloerke), [@trafficonese](https://github.com/trafficonese), and [@tvqt](https://github.com/tvqt).

### promises [v1.2.1](https://rstudio.github.io/promises/news/index.html#promises-121)

[@bakaburg1](https://github.com/bakaburg1), [@bguillod](https://github.com/bguillod), [@can-taslicukur](https://github.com/can-taslicukur), [@CarlijnB](https://github.com/CarlijnB), [@chris31415926535](https://github.com/chris31415926535), [@cpsievert](https://github.com/cpsievert), [@CrossD](https://github.com/CrossD), [@gadenbuie](https://github.com/gadenbuie), [@gdeoli](https://github.com/gdeoli), [@HenrikBengtsson](https://github.com/HenrikBengtsson), [@hf778](https://github.com/hf778), [@jcheng5](https://github.com/jcheng5), [@jennybc](https://github.com/jennybc), [@king-of-poppk](https://github.com/king-of-poppk), [@lz100](https://github.com/lz100), [@maxheld83](https://github.com/maxheld83), [@mrkaye97](https://github.com/mrkaye97), [@pawelru](https://github.com/pawelru), [@schloerke](https://github.com/schloerke), [@tzakharko](https://github.com/tzakharko), and [@vspinu](https://github.com/vspinu).

### thematic [v0.1.3](https://rstudio.github.io/thematic/news/index.html#thematic-013)

[@biomystery](https://github.com/biomystery), [@boram1024](https://github.com/boram1024), [@cboettig](https://github.com/cboettig), [@cbrnr](https://github.com/cbrnr), [@cpsievert](https://github.com/cpsievert), [@dmenne](https://github.com/dmenne), [@Fluke95](https://github.com/Fluke95), [@gadenbuie](https://github.com/gadenbuie), [@gtritchie](https://github.com/gtritchie), [@jennybc](https://github.com/jennybc), [@kbzsl](https://github.com/kbzsl), [@mvwestendorp](https://github.com/mvwestendorp), [@PaulC91](https://github.com/PaulC91), [@r2evans](https://github.com/r2evans), [@rishabhshah-92](https://github.com/rishabhshah-92), [@schloerke](https://github.com/schloerke), [@stephan-koenig](https://github.com/stephan-koenig), [@uhkeller](https://github.com/uhkeller), and [@yixuan](https://github.com/yixuan).

### bsicons [v0.1.1](https://rstudio.github.io/bsicons/news/index.html#bsicons-011)

[@cpsievert](https://github.com/cpsievert), and [@sanjmeh](https://github.com/sanjmeh).

<script>
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
</script>
