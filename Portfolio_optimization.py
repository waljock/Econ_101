#!/usr/bin/env python
# coding: utf-8

# # Basic portfolio optimization problem using `CVXPY`
# 
# ### Dr. Tirthajyoti Sarkar 
# ### Fremont, CA, May 2019

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cvxpy import *


# ### Read the data (please make sure that the CSV data file is in the same directory as this Notebook)

# In[2]:


mp = pd.read_excel("costs.xlsx")

mr0 = pd.DataFrame(mp)

mr1 = mr0[(mr0['REGION_CD'] == 'EA') & (mr0['SaleMo'] <= 201905) & (mr0['SaleMo'] >= 201810)].dropna()
reg = set(mr1['REGION_CD'])
label = reg.pop()

cnum = mr1.columns

vv = len(mr1.columns)

mr = mr1.iloc[:,2:-1]


# get symbol names
symbols = mr.columns


# ### Convert monthly return data frame to a numpy matrix

# In[8]:


return_data = mr.as_matrix().T



# In[10]:


r = np.asarray(np.mean(return_data, axis=1))


# ### Covariance matrix

# In[11]:


C = np.asmatrix(np.cov(return_data))


# In[12]:

C

# ### Print expected returns and risk

# In[13]:
for j in range(len(symbols)):
    print ('%s: Exp ret = %f, Risk = %f' %(symbols[j],r[j], C[j,j]**0.5))

# ### Set up the optimization model
    


# Number of variables
n = len(symbols)

# The variables vector
x = Variable(n)

# The minimum return
req_return = .2

# The return
ret = r.T*x

# The risk in xT.Q.x format
risk = quad_form(x, C)

constraints = [sum(x)==1, ret >= req_return, x >= 0
                  , x[0] <= .10   , x[0] >= .07 
                  , x[1] <= .30   , x[1] >= .17
                  , x[2] <= .12   , x[2] >= .05
                  , x[3] <= .10   , x[3] >= .05
                  , x[4] <= .10   , x[4] >= .05
                  , x[5] <= .25   , x[5] >= .15
                  , x[6] <= .07   , x[6] >= .02
#                  , x[7] >= .02
#                  , x[7] <= .07
#                  , x[8] <= .06
#                  , x[8] >= .02
#                  , x[9] <= .03
#                  , x[9] >= .01
#                  , x[10] <= .03
#                  , x[10] >= .01
#                  , x[11] <= .03
#                  , x[11] >= .01
#                  , x[12] >= .03
#                  , x[12] <= .01
                  ]
#                  
#                        
#                
#                ]

# The core problem definition with the Problem class from CVXPY
prob = Problem(Maximize(ret), constraints)

# In[15]:


try:
    prob.solve()
    print ("Optimal portfolio for Region " + label)
    print ("----------------------")
    for s in range(len(symbols)):
       print (" Investment in {} : {}% of the portfolio".format(symbols[s],round(100*x.value[s],2)))
    print ("----------------------")
    print ("Exp ret = {}%".format(round(100*ret.value,2)))
    print ("Expected risk    = {}%".format(round(100*risk.value**0.5,2)))
except:
    print ("Error")

# In[16]:


prob.status


# In[17]:


x.value


# In[ ]:



