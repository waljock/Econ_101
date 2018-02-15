library(readxl)
library(ggplot2)
library(dplyr)
library(data.table)
library(formattable)
library(tidyverse)
library(ggthemes)
library(ggrepel)

d <- read.csv('C:/Users/HMA03468/Documents/Econ_101/Econ_101/econ-rates.csv')
d$ddate <- as.Date(d$TIME_PERIOD, format="%Y-%m-%d")


#s <-subset(d,((d$Series == 'RIFSPPNAAD60_N.WF') | d$Series == 'RIFSPBLP_N.B')& (d$OBS_VALUE != '-9999'))
s <-subset(d,(d$OBS_VALUE != '-9999') & (d$OBS_VALUE != 'NA') & (d$ddate >= "2007-01-01"))

ggplot(s,aes(ddate, OBS_VALUE))+geom_line(aes(color=Series))+
  scale_x_date(date_labels = "%Y%m") + theme(legend.position="none")



