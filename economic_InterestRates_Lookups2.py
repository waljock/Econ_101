# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:05:02 2018

@author: HMA03468
"""

import xml.etree.ElementTree as ET
import pandas as pd

#e = xml.etree.ElementTree.parse('G19_data.xml').getroot()

tree = ET.parse('H15_struct.xml')
root = tree.getroot()

#print(root.tag)
#print(root.attrib)

for dataset in root.findall('*'):
#    print(dataset)
    pass
    for y in dataset:
      #  print(y)
      pass
      for j in y:
          #print(j)
          pass
          for t in j:
          #    print(t)
              pass
              for h in t:
                 # pass
                 print(h.attrib)
       #           for o in h:
        #              print(o)
          
      
        
mydf2 = []   
 
for series in root.findall('.//{http://www.SDMX.org/resources/SDMXML/schemas/v1_0/structure}Attribute'):
    
   
    seriesobj2 = series.attrib
    #print(seriesobj2)
    
#    seriesName =  seriesobj['SERIES_NAME']
#    seriesInstrument =  seriesobj['INSTRUMENT']
#    seriesUnit = seriesobj['UNIT']
#    seriesMult = seriesobj['UNIT_MULT']
#    seriesMat = seriesobj['MATURITY']
#    seriesCurr = seriesobj['CURRENCY']
#    seriesFreq = seriesobj['FREQ']
#    
#    for obs in series:#.findall('{http://www.federalreserve.gov/structure/compact/G19_CCOUT}Obs'):
#       # print (obs.attrib)
#        obsobj = obs.attrib
#        obsobj['Series'] = seriesName
#        obsobj['Instru'] = seriesInstrument
#        obsobj['Unit'] = seriesUnit
#        obsobj['Mult'] = seriesMult
#        obsobj['Mat'] = seriesMat
#        obsobj['Curr'] = seriesCurr
#        obsobj['Freq'] = seriesFreq
#        
#        
#        
#    
#        mydf2.append(obsobj)
#    
#df = pd.DataFrame(mydf2)   
#df.to_csv('econ-rates.csv')  
#    
#
#    
    
    

#for child in root:
#    pass
#   # print(child.tag)#, child.attrib)
#    for child2 in child:
#        pass
#       # print(child2.tag)#, child2.attrib)
#        for child3 in child2:
#            #pass
#            print(child3.tag, child3.attrib)
##            for child4 in child3:
##                print(child4.tag, child4.attrib)
#for child in root:
#    print (child.tag)  
#    
#    for child2 in child:
#        print(child2.tag)
#        
#        for child3 in child2:
#            print(child3.tag)
#        
#            for child4 in child3:
#                print(child4.tag)
#      #  pass
#       # print(child2.tag)#, child2.attrib)
##    for Header in child.findall('{http://www.federalreserve.gov/structure/compact/common}DataSet'):
##        print(Header)
##    
#            
# 