# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:16:51 2019

@author: HMA03468
"""


import pandas as pd
import numpy as np
import os
from bokeh.plotting import figure, output_file, show
from bokeh.models.ranges import Range1d
#from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20, Inferno
from bokeh.models import HoverTool
#from bokeh.charts import Line




path = os.getcwd()
file0 = os.path.join(path, "econ-rates.csv")
#outfile = os.path.join(path, "Lease Excelwriter.xlsx")
dg = pd.read_csv(file0)

#dg['date2'] = pd.to_datetime(dg['date'])

base = dg[(dg['OBS_VALUE'] >=-50) & (dg['OBS_VALUE'] <=50)]

group = base['Desc'].unique().tolist()
group.sort()

datelst = base['date'].unique().tolist()
datelst.sort()






lstx = []
lsty= []
lstg = []
lstz = []

#for i in range(len(group)):
#    
#    source = ColumnDataSource(data = {'x':base.loc[base.date == datelst[i]],
#                                      'group':base.loc[base.Desc == group[i]],
#                                      'y':base.loc[base.Desc == group[i]].OBS_VALUE})


xs = 
ys = [base.loc[base.Desc == i]['OBS_VALUE'] for i in group]
p2 = figure(plot_width=600, plot_height=300)

p2.multi_line(
     xs=xs['date'],
     ys=ys['OBS_VALUE'],
     legend='group',
     
     line_color=Category20[20][0:len(group)])


show(p2)
#for i in range(len(group)):
#    
#    print( i)
#    
#    for j in range(len(datelst)):
#        
#        obsval = np.array(base[(base['Desc'] == group[i]) & (base['date'] == datelst[j])].OBS_VALUE).item()
#        
#        lstx.append(str(datelst[j]))
#        lstg.append(group[i])
#        lsty.append(obsval)
#        
#        
#print(len(lstx))      
#print(len(lsty))
#print(len(lstg))  
#
#
#lstz.append(lstx)
#lstz.append(lsty)
#lstz.append(lstg)
#
#print(len(lstz))
#source = ColumnDataSource(data = {'x':lstx,
#                                      'group':lstg,
#                                      'y':lsty})
#
#



    

#        legend = grp_list[i],
#        color = (Category10[3])[i])      
#        
#        
#source = ColumnDataSource(lstz)      
#
#p2.line(x=lstz[0],
#        y=lstz[1],
#        source=source,
#        legend = lstz[2]) 
        
        
        
        
#        
#        
#        
#        source = ColumnDataSource(
#                
#                data={'x':base.loc[base.date == datelst[j]],
#                     'group':base.loc[base.Desc == desclst[i]],
#                     'y':base.loc[(base.date == datelst[j]) & ( base.Desc == desclst[i])].OBS_VALUE})
#    
#    p2.line(x='x',
#        y='y',
#        source=source)
#        #legend = desclst[i])
#                     
#                
#                
#                
#                
#    
#    
#    
##    source = ColumnDataSource(
#     data={'x':base.loc[base.date == base[i]].date,
#           'group':base.loc[base.Desc == desclst[i]].Desc,
#           'y':base.loc[base.OBS_VALUE == base.Desc[i]]})

        #color = (Inferno)[i])
#add tool tips
#hover = HoverTool(tooltips =[
#     ('group','@group'),('x','@x'),('y','@y')])
#p2.add_tools(hover)

