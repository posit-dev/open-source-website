---
title: "Palmer Penguins"
format: dashboard
server: shiny
---

```{{python}}
#| context: setup
import seaborn as sns
from shiny.express import render, ui, input
penguins = sns.load_dataset("penguins")
```

# {.sidebar}

```{{python}}
species = list(penguins["species"].value_counts().index)
ui.input_checkbox_group(
    "species", "Species:",
    species, selected = species
)
```

# Plots

```{{python}}
@render.plot
def depth():
    data = penguins[penguins["species"].isin(input.species())]
    return sns.displot(
        data, x = "bill_depth_mm",
        hue = "species", kind = "kde",
        fill = True
    )
```
