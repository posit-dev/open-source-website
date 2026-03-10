---
title: "Card Test Page"
layout: single
---

## Single Cards

### Person
{{< insert-card item="people/hadley-wickham" >}}

### Software
{{< insert-card item="software/ggplot2" >}}

### Event
{{< insert-card item="events/pydata-boston-2025" >}}

### Blog Post
{{< insert-card item="blog/air" >}}

### Resource (Cheatsheet — shorthand)
{{< insert-card item="cheatsheets/data-visualization" >}}

### Resource (Video — shorthand)
{{< insert-card item="videos/2014-12-09_r-markdown" >}}

### Software (no badge)
{{< insert-card item="software/ggplot2" show-badge=false >}}

### Event (no badge)
{{< insert-card item="events/pydata-boston-2025" show-badge=false >}}

## Grids

### 2 Columns
{{< insert-cards cols=2 >}}
- people/hadley-wickham
- software/ggplot2
- events/pydata-boston-2025
- blog/air
{{< /insert-cards >}}

### 3 Columns
{{< insert-cards cols=3 >}}
- software/ggplot2
- software/shiny-r
- software/dplyr
- cheatsheets/data-visualization
- cheatsheets/data-transformation
- videos/2014-12-09_r-markdown
{{< /insert-cards >}}

### 4 Columns
{{< insert-cards cols=4 >}}
- people/hadley-wickham
- people/carson-sievert
- people/barret-schloerke
- people/carlos-scheidegger
- software/ggplot2
- software/shiny-r
- software/dplyr
- software/quarto
{{< /insert-cards >}}

### 3 Columns (no badges)
{{< insert-cards cols=3 badge="jeroen" >}}
- people/hadley-wickham
- software/ggplot2
- blog/air
{{< /insert-cards >}}

### 5 Columns
{{< insert-cards cols=5 >}}
- software/ggplot2
- software/shiny-r
- software/dplyr
- software/air
- software/quarto
- software/gt
- software/pointblank
- software/vetiver-r
- software/pins-r
- software/htmltools
{{< /insert-cards >}}
