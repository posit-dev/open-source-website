library(shiny)
library(bslib)

ui <- page_fillable(
  h2("Old Faithful"),
  card(plotOutput("plot"))
)

server <- function(input, output, session) {
  output$plot <- renderPlot({
    hist(faithful$waiting, col = "steelblue", border = "white")
  })
}

shinyApp(ui, server)
