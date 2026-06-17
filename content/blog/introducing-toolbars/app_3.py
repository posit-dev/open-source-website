import pandas as pd
from faicons import icon_svg

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

app_ui = ui.page_fluid(
    ui.h2("Example App"),
    ui.layout_columns(
        ui.card(
            ui.card_header(
                "Sales Data",
                ui.toolbar(
                    ui.toolbar_input_select(
                        id="region_filter",
                        label="Region",
                        choices=["All", "North", "South", "East", "West"],
                        icon=icon_svg("filter"),
                    ),
                    ui.toolbar_divider(),
                    ui.toolbar_input_button(
                        id="save_btn",
                        label="Save",
                        icon=icon_svg("floppy-disk"),
                    ),
                    align="right",
                ),
            ),
            ui.card_body(ui.output_table("sales_table")),
        ),
        ui.card(
            ui.card_header(
                "Toolbar in header, footer, label",
            ),
            ui.card_body(ui.p("More placeholder text.")),
            ui.card_footer(
                ui.toolbar(
                    ui.toolbar_input_button(
                        id="share_btn",
                        label="Share",
                        icon=icon_svg("share-nodes"),
                        show_label=True,
                    ),
                    ui.toolbar_input_button(
                        id="export_btn",
                        label="Export",
                        icon=icon_svg("download")
                    ),
                    align="right",
                ),
            ),
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
    # Sample sales data
    @reactive.calc
    def sales_data():
        return pd.DataFrame(
            {
                "Product": ["Widget A", "Widget B", "Widget C", "Widget D"],
                "Region": ["North", "South", "East", "West"],
                "Sales": [1200, 850, 1450, 920],
            }
        )

    # Filtered sales data based on region filter
    @reactive.calc
    def filtered_data():
        data = sales_data()

        if input.region_filter() != "All":
            data = data[data["Region"] == input.region_filter()]

        return data

    # Render the table
    @render.table
    def sales_table():
        return (
            filtered_data()
            .style.hide(axis="index")
            .format({"Sales": "${:,.0f}"})
            .set_table_styles([
                {"selector": "th", "props": [
                    ("border-bottom", "1px solid black"),
                    ("padding", "8px 6px"),
                    ("text-align", "left"),
                ]},
                {"selector": "td", "props": [
                    ("padding", "6px"),
                ]},
            ])
        )


app = App(app_ui, server)
