library(readxl)
library(ggplot2)
library(dplyr)
library(data.table)
library(formattable)
library(tidyverse)
library(ggthemes)
library(ggrepel)

d <- read.csv('econ-rates.csv')
d$ddate <- as.Date(d$TIME_PERIOD, format="%Y-%m-%d")
d3 <- d[c(3,10)]
d4 <- unique(d3)

lst <- list("RIFSPPFAAD30_N.B","RIFSPPFAAD90_N.B","RIFSPBLP_N.A", "RIFLGFCY05_N.B")

#s <-subset(d,((d$Series == 'RIFSPPNAAD60_N.WF') | d$Series == 'RIFSPBLP_N.B')& (d$OBS_VALUE != '-9999'))
s <-subset(d,(d$OBS_VALUE != '-9999') &  (d$OBS_VALUE != 'NA') &
             (d$Series  %in% lst))

ggplot(s,aes(ddate, OBS_VALUE))+geom_line(aes(color=Instru))+
  scale_x_date(date_labels = "%Y%m") +  theme()

print(unique(s$Series))



