# The same app as ../before-app, written the way the shiny-for-r skill points
# agents: a bslib page with a sidebar, value boxes, and real navigation.
library(shiny)
library(bslib)
library(ggplot2)

ui <- page_sidebar(
  title = "Fuel economy",
  sidebar = sidebar(
    checkboxGroupInput("cyl", "Cylinders", c(4, 6, 8), selected = c(4, 6, 8)),
    sliderInput("hp", "Horsepower", 50, 340, c(50, 340))
  ),
  layout_columns(
    fill = FALSE,
    value_box("Cars", textOutput("n")),
    value_box("Average mpg", textOutput("mpg")),
    value_box("Average weight", textOutput("wt"))
  ),
  navset_card_underline(
    nav_panel("Plot", plotOutput("plot")),
    nav_panel("Data", tableOutput("data"))
  )
)

server <- function(input, output, session) {
  cars <- reactive({
    mtcars[mtcars$cyl %in% input$cyl & mtcars$hp >= input$hp[1] & mtcars$hp <= input$hp[2], ]
  })
  output$n <- renderText(nrow(cars()))
  output$mpg <- renderText(round(mean(cars()$mpg), 1))
  output$wt <- renderText(paste(round(mean(cars()$wt) * 1000), "lb"))
  output$plot <- renderPlot({
    ggplot(cars(), aes(wt * 1000, mpg, colour = factor(cyl))) +
      geom_point(size = 3) +
      labs(x = "Weight (lb)", y = "Miles per gallon", colour = "Cylinders") +
      theme_minimal(base_size = 14)
  })
  output$data <- renderTable(cars(), rownames = TRUE)
}

shinyApp(ui, server)
