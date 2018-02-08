library(readxl)
library(ggplot2)
library(dplyr)
library(data.table)
library(formattable)
library(tidyverse)
library(ggthemes)
library(ggrepel)

d <- read.csv('C:/Users/HMA03468/Documents/Econ_101/Econ_101/econ.csv')

d$ddate <- format(d$TIME_PERIOD, format="%Y%m%d")

s <-subset(d,(d$Series == 'DTCOLHE_N.M') & (d$OBS_VALUE != 'NA'))

j = ggplot(s,aes(OBS_VALUE),group=1)
j

