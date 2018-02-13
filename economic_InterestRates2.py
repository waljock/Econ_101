# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:05:02 2018

@author: HMA03468
"""

import xml.etree.ElementTree as ET
import pandas as pd

#e = xml.etree.ElementTree.parse('G19_data.xml').getroot()

tree = ET.parse('H15_data.xml')
root = tree.getroot()

#print(root.tag)
#print(root.attrib)

#for dataset in root.findall('*'):
#    print(dataset)
mydf = []   
 
for series in root.findall('{http://www.federalreserve.gov/structure/compact/common/DataSet}Series'):
    print(series.attrib)
   

    

    
    
    

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