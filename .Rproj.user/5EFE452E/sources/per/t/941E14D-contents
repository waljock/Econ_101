library(ggplot2)
library(reshape2)
library(tidyr)


d <- read.csv("C:/Users/HMA03468/Documents/Econ_101/Econ_101/econ-rates.csv")



# long_d <- melt(d, X = (c(1)))
# 
d$cDate <- as.character(d$date)  
d$xDate <- as.Date(d$cDate,format = "%Y-%m-%d") 
d$Date2 <- format(d$xDate, format="%Y-%m")
# long_d$variable <- as.character(long_d$variable)
d2<- subset(d, d$Date2 >= "2018-01")


r <- ggplot(d2, aes(Date2, OBS_VALUE, group=Desc, color=Desc)) +
  geom_line(size=2)
  

r
                  
