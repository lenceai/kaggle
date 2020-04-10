# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('D:\\code\\OneDrive - Lence.AI\\kaggle\\us-counties.csv')
print(data.tail())

#%%
print(data.sort_values('cases'))

#%%

wa = data[data.state == 'Washington'].groupby('date')
