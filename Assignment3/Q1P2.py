
# coding: utf-8

# Q1_PART TWO
# • Use ‘vehicle_collisions’ data set.
# • For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# • Display a few rows of the output use df.head().
# • Generate a csv output with five columns ('borough', 'one-vehicle', 'two- vehicles', 'three-vehicles', 'more-vehicles')

# In[1]:

from pandas import Series, DataFrame
import pandas as pd


# In[2]:

# Read CSV
df = pd.read_csv('data/vehicle_collisions.csv')


# In[21]:

# Convert date to datetime type
df['DATE'] = pd.to_datetime(df['DATE'])
# Find the records from 2015 to now
dfU = df[df['DATE'].dt.year>=2015]
# Remove the na in borough
dfU = dfU[dfU['BOROUGH'].notnull()]


# In[24]:

# Find borough names
bo = dfU.BOROUGH.unique()


# In[28]:

# Write header
result = pd.DataFrame(columns=['borough','one-vehicle','two-vehicles','three-vehicles','more-vehicles'])
num=0
for b in bo:
    dfB = dfU[dfU['BOROUGH']==b]
    # Find more vehicles involved by remove nan in both 4 type and 5 type column
    moreV = dfB[['VEHICLE 4 TYPE','VEHICLE 5 TYPE']].dropna(axis=0,how='all').shape[0]
    # Find 3 vehicles involved by remove nan in 3 type and all more vehicles rows
    threeV = dfB[['VEHICLE 3 TYPE']].dropna(axis=0,how='all').shape[0] - moreV
    # Find 2 vehicles involved by remove nan in 2 type and all more than 2 vehicles rows 
    twoV = dfB[['VEHICLE 2 TYPE']].dropna(axis=0,how='all').shape[0] - threeV - moreV
    # Find 1 vehicles involved by remove nan in 1 type and all more than 1 vehicles rows
    oneV = dfB[['VEHICLE 1 TYPE']].dropna(axis=0,how='all').shape[0] - threeV - moreV - twoV
    result.loc[num]=[b,oneV,twoV,threeV,moreV]
    num+=1


# In[29]:

result.head()


# In[30]:

result.to_csv('ResultQ1P2.csv',index=False)


# In[ ]:



