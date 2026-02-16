# Supported By Posit Badge <img src="https://posit-dev.github.io/supported-by-posit/img/supported-by-posit-hex-small.png" style="margin-left: 20px; height: 150px" align="right" height="150" alt="supported-by-posit website" />

The "Supported by Posit" badge is a clickable element that can be added to Quarto and pkgdown websites to indicate that Posit, PBC supports the project.
It appears on the far right of the top navigation bar or at the bottom of the hamburger menu.
It links to [Posit's main website](https://posit.co).


## Featured Websites

The following websites have the "Supported by Posit" badge:
[dplyr](https://dplyr.tidyverse.org),
[ggplot2](https://ggplot2.tidyverse.org),
[Great Tables](https://posit-dev.github.io/great-tables/articles/intro.html),
[gt](https://gt.rstudio.com),
[lubridate](https://lubridate.tidyverse.org),
[mirai](https://mirai.r-lib.org),
[nanonext](nanonext.r-lib.org),
[pkgdown](https://pkgdown.r-lib.org)
[Plotnine](https://plotnine.org),
[Pointblank](https://posit-dev.github.io/pointblank/),
[pointblank](https://rstudio.github.io/pointblank/),
[purrr](https://purrr.tidyverse.org),
[Quarto](https://quarto.org),
[Shiny](https://shiny.posit.co),
and many others.


## Installation

The badge is implemented as a single JavaScript file that can be easily added to any Quarto or pkgdown website. To add the badge, include the following in your `_quarto.yml` or `_pkgdown.yml` file:

::: {.panel-tabset group="language"}

## _quarto.yml

```yaml
format:
  html:
    include-in-header:
      - text: |
          <script src="https://cdn.jsdelivr.net/gh/posit-dev/supported-by-posit/js/badge.min.js"></script>
```

## _pkgdown.yml

```yaml
template:
  includes:
    in_header: |
      <script src="https://cdn.jsdelivr.net/gh/posit-dev/supported-by-posit/js/badge.min.js"></script>
```
:::


## Customization

If the default colors or settings don't match your website's design, you can customize the badge. The badge supports customization of the background color, foreground color, whether it should be hidden below a certain width to accommodate crowded navigation headers, the left margin, and the maximum height.

**Note:** Dark mode colors are ignored if your website only supports light mode.

::: {.panel-tabset group="language"}

## _quarto.yml

```yaml
format:
  html:
    include-in-header:
      - text: |
          <script src="https://cdn.jsdelivr.net/gh/posit-dev/supported-by-posit/js/badge.min.js"
                  data-light-bg="#ffffff"
                  data-light-fg="#404041"
                  data-dark-bg="#404041"
                  data-dark-fg="#ffffff"
                  data-hide-below="992"
                  data-margin-left="10"
                  data-max-height="54"></script>
```

## _pkgdown.yml

```yaml
template:
  includes:
    in_header: |
      <script src="https://cdn.jsdelivr.net/gh/posit-dev/supported-by-posit/js/badge.min.js"
              data-light-bg="#ffffff"
              data-light-fg="#404041"
              data-dark-bg="#404041"
              data-dark-fg="#ffffff"
              data-hide-below="992"
              data-margin-left="10"
              data-max-height="54"></script>
```
:::

**Best Practice:** Only include the `data-*` attributes for colors and settings you want to override from the defaults.

To comply with Posit's brand guide, please choose from the following colors:

* Background color (`data-*-bg`): Any color that provides adequate contrast with the text and the logo
* Foreground color (`data-*-fg`): Either `#404041` or `#ffffff`

For questions, message the `#supported-by-posit` channel on Slack.


## Testing

You can test how the badge will look on your website before making permanent changes by using your browser's JavaScript Console.

```javascript
// Step 1: Load the Badge Script
script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/gh/posit-dev/supported-by-posit/js/badge.min.js';
document.head.appendChild(script);

// Step 2: Test Different Settings
addSupportedByPositBadge({
  'lightBg': '#ffffff',
  'lightFg': '#404041',
  'darkBg': '#404041',
  'darkFg': '#ffffff',
  'hideBelow': 992,
  'marginLeft': 10,
  'maxHeight': 54
});
```

**Important:** All parameters must be provided when calling the `addSupportedByPositBadge()` function. Once you're satisfied, add only the non-default ones to your `<script>` tag using the `data-*` attributes shown in the customization section.


## Deploying

When the script itself is updated on GitHub, purge the CDN cache to ensure users receive the latest version.
To purge the script, visit: [purge.jsdelivr.net/gh/posit-dev/supported-by-posit/js/badge.min.js](https://purge.jsdelivr.net/gh/posit-dev/supported-by-posit/js/badge.min.js).
