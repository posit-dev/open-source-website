# shinyswatch


<!-- DO NOT EDIT BY HAND: Edit docs/index.qmd and run `make docs-readme` to update -->

[Bootswatch](https://bootswatch.com/) + Bootstrap 5 themes for
[Shiny](https://shiny.rstudio.com/py/).

Here are just three of the **25 themes** in shinyswatch:

| Minty | Sketchy | Superhero |
|----|----|----|
| ![Minty](https://raw.githubusercontent.com/rstudio/py-shinyswatch/v0.2.2/readme_minty.png) | ![Sketchy](https://raw.githubusercontent.com/rstudio/py-shinyswatch/v0.2.2/readme_sketchy.png) | ![Superhero](https://raw.githubusercontent.com/rstudio/py-shinyswatch/v0.2.2/readme_superhero.png) |

## Installation

``` sh
pip install shinyswatch
```

To install the latest development version from this repository:

``` sh
pip install https://github.com/rstudio/py-shinyswatch/tarball/main
```

## Usage

To use a theme, add a `shinyswatch.theme` theme object to your App’s UI
definition.

``` python
# Minty theme
shinyswatch.theme.minty

# Sketchy theme
shinyswatch.theme.sketchy

# Superhero theme
shinyswatch.theme.superhero
```

Example Shiny application:

<table>

<thead>

<tr>

<th>

File: <code>app.py</code>
</th>

<th>

Screenshot
</th>

</tr>

</thead>

<tbody>

<tr>

<td>

``` python
from shiny import App, Inputs, Outputs, Session, render, ui

import shinyswatch

app_ui = ui.page_fluid(
    ui.input_slider("num", "Number:", min=10, max=100, value=30),
    ui.output_text_verbatim("slider_val"),
    theme=shinyswatch.theme.darkly,  # <- Use a shinyswatch theme here
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    def slider_val():
        return f"{input.num()}"


app = App(app_ui, server)
```

</td>

<td>

![darkly
theme](https://raw.githubusercontent.com/rstudio/py-shinyswatch/v0.2.2/readme_darkly.png)

</td>

</tr>

</tbody>

</table>

> Note: When writing [shiny apps that use shinyswatch on
> shinylive.io](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkAQUxEAkhHQBXCqyIB5eXIVEAynFatO5Ig2oATOAyKzOAHQjX+g4Wy49WAdygVi7a9YzoA+hbIALzIFjhQAOZwfnQANhZGABTWyKmhnFjcan6ssZwmDMmQsjCWhMhlAHIlAEamiGVEMNxBAIwADE1QAB5t7Z3IAG5Q8XBBAMztAJQEKWlhpKryflTdFH6DpjXu-EW5+aYbI2Uzc6kU7HDwQRzcuK7unlgXV3BYRlAMANaxuETIAGJkAAeAC0yAAqqw4MgoI47g8POxkC94MhLoZrFNvDYICY6GxTJtCll5ChpGpFMhFhQ1CgVLT5FToTo9BAUFpWeQpg0IGlkAABGlqM6Cwx40zPOBrUX4th5ApHWKJHmi-mGCiyBh8uhlECkihYCAlFUAXzKOJ8mGCYkwiV8AU4RGhDGJ2Ig5TAFFw6AQKC90ooYFNRHA0HgtDAhgAjhZDPBKKxnmtPWRKNQg-7bjxrNn7m4kdZPd7fZHVkHTQBdIA),
> remember to add `shinyswatch` to your `requirements.txt` file!

## Theme picker

To add a theme picker to your app, add the theme picker UI and server
functions to your app’s UI and server definitions.

[Demo **theme picker** app on
shinylive.io](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkAQUxEAkhHQBXCqyIB5eXIVEAynFatO5Ig2oATOAyKzOAHQjX+g4Wy49WAdygVi7a9YzoA+hbIALzIFjhQAOZwfnQANhZGABTWyKmO3Liu7p5YFOxw8H7onMQA1qYBnIkAlETIAMTIADwAtGJGRsh5cF358MjFZabIAKqSXaTIuKSyDMi+KWlh3Gp+rLGcJgzJkLIwloTIBwByewBGpogHRDDcQQCMAAw3UAAeD4-PyABuUPFwQQAzI9aotUmEZhRVlRXhQ-N9TGd3PwdutNhVfrEDqCIGlegUARwMlkPOxcn04FgAF5wdDsXBmVKNVrIADC7FIpFYPSguO4nAonD++P6iVI6EF5D+1WsMps8pMdDYpgR2xW8hQ0jUimQkLUKBUUPkOu5Oj0EBQWjN5GqV1xaUaAFkoOU2LMetNZsqGKrkHRZBBiJLccQ-rFWPiRT1BuU5tyfcN-YHg2D0s43KTyQSiiVY2sVaYat57akAAJ6+Sp0uGCBbXJwWGpxVsDZbeF-Gp2vF4wwUWa4ugHEDqihYCB7GoAXwOxZ8mGCYkwiV8lSI8dVcsOYAouHQCBQ24bFDAk6I4Gg8FoYEMAEcLIZ4JRWLlYVuyJRqMeD0SeNYf5kM08awtx3PcrxhY9JwAXSAA).

## Plot Theming

shinyswatch themes include a `.colors` attribute that can be used to
theme plots or other outputs and UI elements. In the example below, try
changing the theme and re-running the app to see how the plot changes.

[Demo **plot theming** app on
shinylive.io](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5GKC9AG1Iu7oAjHLh59kUAM7IeFADoQGTVsggBXRrgnSI6BQDNmpGMkkALOhC1KWbAIKYizagBM4zJ3ACORNXQUKAMTIACrMWsRmUBAA5pYxyBRmcInJ8MiGxuyWFFoUpMhqilQuBkYm5pa4kgDunJFYSXDpNiowOVpSphZWAPpN8AHQmL1+yAC8hXQ4UDFwvfrcfi4AFArIG1NYluhqFL2SAm7Ma5ByhMjnAHLnRO0Q4wAMd1AAHuMAjI-PyABuUEs4OMAEyPACUBHWmz8WGIUGYqxhpD2u32Ygop3R5zBEKhGwGQMqfQJkIgYKGCjc+lM7l+7hWOz2YMQeOQAAFnBBjjheBiARRxuc7MgLJJ8jFmLBsayqTJeStmazNqpsJKucYsJI4HBVh8AJwANgAHI8TR9yRBlcrXhNkF9HsgANR2gCsyAAVCqsGqXBqfRAVgAWADMAHYLUrNvo6DEiG9bbJNWpBOjJArIxs3lhRRjXkRGRQsAGIcg3BBJHRcuMwmo4EQyLxmOMibh+mk4LDSI3JDhmAx4bgI5arRtgiF26kUujEgUOBRIpPkMQ1MxOWwCRmMjGZvOzJq4Pt9FBiHAGyxThByHBpcOR1mtYfj6eu+fzpeINewEORxsz8wFgkkwtm2zQdn+PaCKQLitn+m5ZhQdDEAA1r06DwrAaZvHQkiCmAkFJLcS4vswOF-gBFo-hIryauglhwJIwDnPh+QwOcAC6+77H+KxkfoMQUT+960R+DHnPkehgBxD69NxvH8XB1GSMJ9GMWA3BwPo8iSZxMnETxxHkQpNF0aJYB9jEZhaVJB66Y2+mNoZECbs4FArpa0YxBSwzoLaDjoCsGDoKMdBEFqzB0swFoXGAuToAgKAxXArwUGAAC+RDgNA8C0GZ3h+M48CUD2FDJdFZCUNQKUJeomgKHO6ICIICgts1PTVHUu4KNFsXxagVClalbFAA).

## Development

If you want to do development on shinyswatch for Python:

``` sh
pip install -e ".[dev,test,docs]"
```

### Examples

There are multiple examples in the shinyswatch repo.

<!-- You can view them online at: [shinyswatch.theme.darkly](http://rstudio.github.io/py-shinyswatch/reference/theme.darkly.html) and [get_theme](http://rstudio.github.io/py-shinyswatch/reference/get_theme.html). -->

To run the demos locally, you can run the examples by calling:

``` sh
python3 -m shiny run examples/basic-darkly/app.py
python3 -m shiny run examples/big-sketchy/app.py
python3 -m shiny run examples/components/app.py
python3 -m shiny run examples/theme-picker/app.py
```
