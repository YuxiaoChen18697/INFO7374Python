
# coding: utf-8

# Q4_PART ONE
# • Use ‘movies_awards’ data set.
# • You are supposed to extract data from the awards column in this dataset and split it into several
# columns. An example is given below.
# • The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# • You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award.
# • If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated).
# • Create two separate columns for each award category (won and nominated).
# • Write your output to a csv file. (Sample output is given in next page)

# In[12]:

from pandas import Series, DataFrame
import pandas as pd


# In[13]:

# Read CSV
df = pd.read_csv('data/movies_awards.csv')


# In[14]:

df.dropna()
df = df[['imdbID', 'Awards']]
df.head()


# In[15]:

import re
def findWins(name, row):
    pattern = r'Won (\d+) '+name
    nums = re.findall(pattern, row)
    if len(nums)>0:
        return nums[0]
    else:
        return '0'
def findNoms(name, row):
    pattern = r'Nominated for (\d+) '+name
    nums = re.findall(pattern, row)
    if len(nums)>0:
        return nums[0]
    else:
        return '0'


# In[18]:

df['Prime_Won'] = df.apply(lambda row: findWins('Prime', row['Awards']), axis=1)
df.head(4)


# In[ ]:



