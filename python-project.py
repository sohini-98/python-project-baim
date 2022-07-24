# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline 

df=pd.read_csv("brfss2020.csv")

df.head()

df_relevant=df.loc[:,['_STATE',
'LADULT1',
'COLGSEX',
'PHYSHLTH',
'MENTHLTH',
'HLTHPLN1',
'EXERANY2',
'SLEPTIM1',
'CVDINFR4',
'CVDCRHD4',
'CVDSTRK3',
'DIABETE4',
'VETERAN3',
'INCOME2',
'PREGNANT',
'SMOKE100',
'DRNK3GE5',
'HIVRISK5',
'ECIGNOW',
'MARIJAN1',
'CNCRDIFF',
'CNCRTYP1',
'_URBSTAT',
'_IMPRACE',
'_AGEG5YR',
'_BMI5',
]]


df_relevant.head()

df_relevant.to_csv("dfff.csv")







