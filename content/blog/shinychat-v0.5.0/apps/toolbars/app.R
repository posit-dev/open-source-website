source("../_mock-client.R")

ui <- page_chat(
  "Research assistant",
  id = "chat",
  toolbar = bslib::toolbar(
    bslib::toolbar_input_button(
      "clear_chat",
      "Clear conversation",
      icon = bsicons::bs_icon("arrow-counterclockwise")
    )
  ),
  toolbar_global = bslib::toolbar(
    bslib::toolbar_input_button(
      "help",
      "Help",
      icon = bsicons::bs_icon("question-circle")
    )
  ),
  toolbar_input = bslib::toolbar(
    shiny::selectInput(
      "response_style",
      label = NULL,
      choices = c("Concise", "Detailed"),
      width = "150px"
    )
  ),
  pages_navbar = list(
    chat_nav_panel(
      "Sources",
      tags$div(
        tags$p("Sources selected during this session appear here."),
        tags$ul(
          tags$li(tags$a(href = "#", "Survey observations (2026 season)")),
          tags$li(tags$a(href = "#", "Field notebook, May"))
        )
      ),
      toolbar = bslib::toolbar(
        bslib::toolbar_input_button(
          "refresh_sources",
          "Refresh",
          icon = bsicons::bs_icon("arrow-repeat")
        )
      )
    )
  ),
  greeting = paste0(
    "## Research assistant\n\n",
    "Ask about the study, or open the **Sources** page to see what I'm reading from."
  ),
  placeholder = "Ask about the study..."
)

server <- function(input, output, session) {
  chat_server("chat", mock_client(), history = FALSE)

  observeEvent(input$chat_user_input, {
    text <- if (is.list(input$chat_user_input)) {
      input$chat_user_input[[1]]
    } else {
      input$chat_user_input
    }
    mock_respond(
      "chat",
      paste0(
        "The study tracked monthly surveys across the 2026 season. ",
        "Open the **Sources** page to see the underlying documents."
      )
    )
  })
}

shinyApp(ui, server)
