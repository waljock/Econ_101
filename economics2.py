# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:26:07 2018

@author: Walter
"""

import xml.etree.ElementTree as ET

tree = ET.parse('G19_data.xml')
root = tree.getroot()

for obs in root.findall('{http://www.federalreserve.gov/structure/compact/common}Obs'):
    print(obs)
    #pass
#    for j in i:
#        #print(j)
#        pass
#        for w in j:
#            print (w)
#
