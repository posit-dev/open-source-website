from faicons import icon_svg

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

app_ui = ui.page_fluid(
    ui.h2("Example App"),
    ui.layout_columns(
        ui.card(
            ui.card_header(
                "Toolbar in header & label",
            ),
            ui.card_body(ui.p("Placeholder text.")),
        ),
        ui.card(
            ui.card_header(
                "Toolbar in header, footer, label",
            ),
            ui.card_body(ui.p("More placeholder text.")),
            ui.card_footer(ui.p("Footer content here.")),
        ),
        col_widths=[6, 6],
    ),
    ui.card(
        ui.card_header(
            "Toolbar in Text Input Submit Area: Message Composer",
        ),
        ui.card_body(
            ui.layout_columns(
                ui.p("Placeholder for an input"),
                ui.div(ui.p("Placeholder for outputs")),
                col_widths=[6, 6],
            ),
        ),
    ),
)


def server(input: Inputs, output: Outputs, session: Session) -> None:
    pass


app = App(app_ui, server)
