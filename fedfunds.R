library(ggplot2)
library(reshape2)
library(tidyr)


d <- read.csv("C:/Users/HMA03468/Documents/Econ_101/Econ_101/econ-rates.csv")

d$xDesc <- as.character(d$Desc)  

# long_d <- melt(d, X = (c(1)))
# 
d$cDate <- as.character(d$TIME_PERIOD)  

d$xDate <- as.Date(d$cDate,format = "%Y-%m-%d") 
d2<- subset(d, d$OBS_VALUE >=-50 & d$OBS_VALUE <= 50)

r <- ggplot(d2, aes(xDate, OBS_VALUE, group=xDesc, color=xDesc)) +
  geom_line(size=1) + theme(legend.position = "top", legend.text=element_text(size=8))
  
  

r
                  
