library(ggplot2)
library(tidyverse)
library(readxl)
library(leaflet)
library(htmlwidgets)
library(shiny)
library(shinythemes)



d <- read.csv("C:/Users/HMA03468/Documents/Econ_101/Econ_101/econ-rates.csv")

d$xDesc <- as.character(d$Desc)  

# long_d <- melt(d, X = (c(1)))
# 
d$cDate <- as.character(d$TIME_PERIOD)  

d$xDate <- as.Date(d$cDate,format = "%Y-%m-%d") 
d2<- subset(d, d$OBS_VALUE >=-50 & d$OBS_VALUE <= 50)

r <- ggplot(d2, aes(xDate, OBS_VALUE, group=xDesc, color=xDesc)) +
  geom_line(size=1) + theme(legend.position = "top", legend.text=element_text(size=8))






# This is the Shiny UI
ui <- bootstrapPage(
  
  tags$style(type = "text/css", "html, body {width:100%;height:100%}"),
  
  absolutePanel(top = 10, right = 10,
                selectInput(inputId = "year", label = strong("MY"),
                            choices = grouped_MY$MODEL_YEAR,
                            selected = "2019"),
                selectInput(inputId = "series", label = strong("Series"),
                            choices = grouped_Series$SERIES_CD,
                            selected = "1")),
  leafletOutput("map", width = "100%", height = "100%")
  
)

# Define server function

server <- function(input, output, session) {
  #reactive here allow pulldowns to update the map
  
  filteredData <- reactive(data.frame((subset(r,(SERIES_CD==input$series) & (MODEL_YEAR == input$year)))))
  
  
  
  
  output$map <- renderLeaflet({
    # Use leaflet() here, and only include aspects of the map that
    # won't need to change dynamically (at least, not unless the
    # entire map is being torn down and recreated).
    leaflet(map) %>% addTiles() %>%
      addMarkers(data=filteredData(), label =~ DEALER_CD, clusterOptions = markerClusterOptions())
    
  })
}




#Run the app 

shinyApp(ui = ui, server = server)               


