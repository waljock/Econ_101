library(readxl)
library(ggplot2)
library(dplyr)
library(data.table)
library(formattable)
library(tidyverse)
library(ggthemes)
library(ggrepel)

d <- read.csv('C:/Users/HMA03468/Documents/Econ_101/Econ_101/econ.csv')



s <-subset(d,(d$Series == 'DTCOLHE_N.M') & (d$OBS_VALUE != 'NA'))
s$ddate <- as.Date(s$TIME_PERIOD, format="%Y-%m-%d")

ggplot(s,aes(ddate, OBS_VALUE))+geom_point()+
  scale_x_date(date_labels = "%Y")


