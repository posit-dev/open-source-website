from faithful import histogram, waiting
from shiny.express import input
from shinyreact import reactive_output, set_react_page

set_react_page()


# py-shiny#2497: `Jsonifiable`'s `dict`/`list` arms are invariant, so a
# `dict` return is not assignable to it. Drop the ignore when that lands.
@reactive_output  # pyright: ignore[reportArgumentType]
def dist_data():
    return histogram(waiting, input.bins())


@reactive_output
def dist_caption():
    n = input.bins()
    return f"{len(waiting)} eruptions in {n} bin{'' if n == 1 else 's'}"
