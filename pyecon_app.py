# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:16:51 2019

@author: HMA03468
"""


import pandas as pd
import numpy as np
import os
import plotly.plotly as py
import plotly.graph_objs as go

import cufflinks as cf


#from bokeh.charts import Line

#py.plotly.tools.set_credentials_file(username='waljock', api_key='LtZNsahiHSoGfq2SEu9o')


path = os.getcwd()
file0 = os.path.join(path, "econ-rates.csv")
#outfile = os.path.join(path, "Lease Excelwriter.xlsx")
dg = pd.read_csv(file0)

#dg['date2'] = pd.to_datetime(dg['date'])

base = dg[(dg['OBS_VALUE'] >=-50) & (dg['OBS_VALUE'] <=50)]

b2 = base[['Desc', 'OBS_VALUE','date']]






base.iplot(kind='scatter', filename='cf-simple-line')
