
# coding: utf-8

# Q1_PART ONE
# • Use ‘vehicle_collisions’ data set.
# • For each month in 2016, find out the percentage of collisions in
# Manhattan out of that year's total accidents in New York City.
# • Display a few rows of the output use df.head().
# • Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# In[83]:

from pandas import Series, DataFrame
import pandas as pd


# In[84]:

# Read CSV
df = pd.read_csv('data/vehicle_collisions.csv')


# In[85]:

# Convert date to datetime type
df['DATE'] = pd.to_datetime(df['DATE'])


# In[86]:

import datetime
result = pd.DataFrame(columns=["Month","Manhattan","NYC","Percentage"])
for i in range(1,12):
    month = datetime.date(1900, i, 1).strftime('%b') # Get month name
    dfM = df2016[df2016['DATE'].dt.month==i] # Get all records in each month
    count = dfM.shape[0] # Get the number of all records each month
    Mcount = dfM[dfM['BOROUGH']=='MANHATTAN'].shape[0] # Get the number of records happened in mantattan
    result.loc[i]=[month,Mcount,count,Mcount/count]


# In[87]:

result.head()


# In[88]:

result.to_csv('ResultQ1P1.csv',index=False)


# In[ ]:



