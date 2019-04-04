# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:05:02 2018

@author: HMA03468
"""

import xml.etree.ElementTree as ET
import pandas as pd

#e = xml.etree.ElementTree.parse('G19_data.xml').getroot()

tree = ET.parse('FRB_H15.xml')
root = tree.getroot()

#print(root.tag)
#print(root.attrib)

#for dataset in root.findall('*'):
#    print(dataset)
mydf2 = []   
 
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
    
           
    
    
    
   
#    for attr in root.findall('.//{http://www.federalreserve.gov/structure/compact/common}Annotations'): 
#        print (attr.attrib)
        
    #<frb:Annotations xmlns:frb="http://www.federalreserve.gov/structure/compact/common"><common:Annotation xmlns:common="http://www.SDMX.org/resources/SDMXML/schemas/v1_0/common"><common:AnnotationType>Short Description</common:AnnotationType><common:AnnotationText>3-month financial commercial paper</common:AnnotationText></common:Annotation><common:Annotation xmlns:common="http://www.SDMX.org/resources/SDMXML/schemas/v1_0/common"><common:AnnotationType>Long Description</common:AnnotationType><common:AnnotationText>90-Day AA Financial Commercial Paper Interest Rate</common:AnnotationText></common:Annotation></frb:Annotations>
    
    
    for obs in series:#.findall('{http://www.federalreserve.gov/structure/compact/G19_CCOUT}Obs'):
       # print (obs.attrib)
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
    
df = pd.DataFrame(mydf2)  
df['date']= pd.to_datetime(df['TIME_PERIOD'])

df2 = df[(df['date'] > '2012-01-01')]
df2.to_csv('econ-rates.csv')  
    

    
    
    

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
