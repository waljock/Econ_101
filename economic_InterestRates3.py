# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:05:02 2018

@author: HMA03468
"""

import xml.etree.ElementTree as ET
import pandas as pd
import os
import bokeh as bk
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import wget

site = "https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=42196c5860f0cc408e8603dd4791139c&lastobs=1000&from=&to=&filetype=sdmx&label=include&layout=seriescolumn"
filename = 'C:\\Users\\HMA03468\\Documents\\Econ_101\\Econ_101\\FRB_H15.xml'
#"/home/waljock/Projects/python_proj/pyEcon/"

try:
    os.remove(filename)
    print ("TxtFileRemoved")
except:
    print ("FILE DOES NOT EXIST OR OTHER ERROR")
    pass

wget.download(site, filename)

tree = ET.parse(filename)
root = tree.getroot()

mydf2 = []   

ctr = 0
 
for series in root.findall('.//{http://www.federalreserve.gov/structure/compact/H15_H15}Series'):
  
    seriesobj = series.attrib
    
    seriesName =  seriesobj['SERIES_NAME']
    seriesInstrument =  seriesobj['INSTRUMENT']
    seriesUnit = seriesobj['UNIT']
    seriesMult = seriesobj['UNIT_MULT']
    seriesMat = seriesobj['MATURITY']
    seriesCurr = seriesobj['CURRENCY']
    seriesFreq = seriesobj['FREQ']
    
    seriesType = series[0][0][1].text
    
    
    for obs in series:
        
        obsobj = obs.attrib
        obsobj['Series'] = seriesName
        obsobj['Instru'] = seriesInstrument
        obsobj['Unit'] = seriesUnit
        obsobj['Mult'] = seriesMult
        obsobj['Mat'] = seriesMat
        obsobj['Curr'] = seriesCurr
        obsobj['Freq'] = seriesFreq
        obsobj['Desc'] =seriesType
         
        mydf2.append(obsobj)
        
        ctr = ctr + 1
    
df = pd.DataFrame(mydf2)  
df['date']= pd.to_datetime(df['TIME_PERIOD'])

print("Line Count is:  " + str(ctr))

df2 = df[(df['date'] > '2012-01-01')]
df2.to_csv('econ-rates.csv')