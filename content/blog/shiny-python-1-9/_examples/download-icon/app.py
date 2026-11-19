import pandas as pd
from faicons import icon_svg

from shiny.express import render, ui

penguins = pd.DataFrame(
    {
        "species": ["Adelie", "Chinstrap", "Gentoo"],
        "island": ["Torgersen", "Dream", "Biscoe"],
        "bill_length_mm": [39.1, 46.5, 47.3],
    }
)

ui.page_opts(title="Penguins")


@render.download_button(
    label="Download CSV",
    icon=icon_svg("download"),
    class_="btn-success",
    filename="penguins.csv",
)
def download():
    yield penguins.to_csv(index=False)


@render.data_frame
def table():
    return penguins
