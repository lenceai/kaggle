# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:03:11 2020

@author: RyanLence
"""
#%% pull in the data

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#df = pd.read_csv('us-counties.csv')
df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')

# focus on WA

wa = df[df.state == 'Washington']
wa = wa[wa.date >= '2020-03-01']

ut = df[df.state == 'Utah']
ut = ut[ut.date >= '2020-03-01']

# focus on US

us = df[df.date >= '2020-03-01']


del wa['fips']
del us['fips']
del ut['fips']

#%% add the last day's results

wa = wa.groupby('date').sum()
wa_last = wa.shift(periods=1)
wa['last_cases'] = wa_last.cases
wa['last_deaths'] = wa_last.deaths
wa['daily_cases'] = wa.cases - wa.last_cases
wa['daily_deaths'] = wa.deaths - wa.last_deaths
wa = wa.reset_index()

us = us.groupby('date').sum()
us_last = us.shift(periods=1)
us['last_cases'] = us_last.cases
us['last_deaths'] = us_last.deaths
us['daily_cases'] = us.cases - us.last_cases
us['daily_deaths'] = us.deaths - us.last_deaths
us = us.reset_index()

ut = ut.groupby('date').sum()
ut_last = ut.shift(periods=1)
ut['last_cases'] = ut_last.cases
ut['last_deaths'] = ut_last.deaths
ut['daily_cases'] = ut.cases - ut.last_cases
ut['daily_deaths'] = ut.deaths - ut.last_deaths
ut = ut.reset_index()



#%% Report on the data

wa.daily_cases.plot(kind='bar', label='Washington')
plt.show()

us.daily_cases.plot(kind='bar')
plt.show()

ut.daily_cases.plot(kind='bar')
plt.show()

wa.daily_deaths.plot(kind='bar')
plt.show()

us.daily_deaths.plot(kind='bar')
plt.show()

ut.daily_deaths.plot(kind='bar')
plt.show()

#%%


wa.to_csv('wa_daily.csv')

#sns.set_color_codes("pastel")
sns.barplot(x='daily_cases', y='date', data=wa)


