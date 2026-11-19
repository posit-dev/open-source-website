from shiny import App, render, ui

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_text("query", "Search penguins"),
        ui.input_checkbox_group(
            "species", "Species", ["Adelie", "Chinstrap", "Gentoo"]
        ),
        title="Filters",
        role="search",
    ),
    ui.output_text("summary"),
    title="Penguins",
)


def server(input, output, session):
    @render.text
    def summary():
        return f"Searching for {input.query()!r} in {', '.join(input.species())}"


app = App(app_ui, server)
