library(readxl)
library(ggplot2)
library(dplyr)
library(data.table)
library(formattable)
library(tidyverse)
library(ggthemes)
library(ggrepel)

d <- read.csv('econ-rates.csv')
g <- read.csv('hmf-rates.csv')


d$ddate <- as.Date(d$TIME_PERIOD, format="%Y-%m-%d")
d3 <- d[c(3,10)]
d4 <- unique(d3)

g$ddate <- as.Date(g$CALENDAR_DATE, format="%d%b%Y:%H:%M:%S")
g <- subset(g, ddate >= '2012-01-01')
#u <- merge(d,g, by.x='ddate', by.y='ddate')

lst <- list("RIFSPPFAAD90_N.B", "RIFLGFCY05_N.B","RIFLGFCY03_N.B")

#s <-subset(d,((d$Series == 'RIFSPPNAAD60_N.WF') | d$Series == 'RIFSPBLP_N.B')& (d$OBS_VALUE != '-9999'))
s <-subset(d,(d$OBS_VALUE != '-9999') &  (d$OBS_VALUE != 'NA') &
             (d$Series  %in% lst))

ggplot(s,aes(ddate, OBS_VALUE))+geom_line(aes(color=Desc) )+
  scale_x_date(date_labels = "%Y%m") +   
  geom_line(data=g,aes(x=ddate, y=AVG_of_SETTLEMENT_RATE))+theme(legend.position = 'top') 

print(unique(s$Series))




