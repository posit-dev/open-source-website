library(shiny)
library(bslib)

ui <- page_fluid(
  h2("Example App"),
  layout_columns(
    card(
      card_header(
        "Toolbar in header & label"
      ),
      card_body(
        p("Placeholder text.")
      )
    ),
    card(
      card_header(
        "Toolbar in header, footer, label"
      ),
      card_body(
        p("More placeholder text.")
      ),
      card_footer(
        p("Footer content here.")
      )
    ),
    col_widths = c(6, 6)
  ),
  card(
    card_header(
      "Toolbar in Text Input Submit Area: Message Composer"
    ),
    card_body(
      layout_columns(
        p("Placeholder for an input"),
        div(
          p("Placeholder for outputs")
        ),
        col_widths = c(6, 6)
      )
    )
  )
)

server <- function(input, output, session) {
  # Placeholder
}

shinyApp(ui, server)
