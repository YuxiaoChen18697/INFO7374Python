
# coding: utf-8

# Q2_PART ONE
# • Use 'employee_compensation' data set.
# • Find out the highest paid departments in each organization group by
# calculating mean of total compensation for every department.
# • Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# • Display a few rows of the output use df.head().
# • Generate a csv output.

# In[1]:

from pandas import Series, DataFrame
import pandas as pd


# In[2]:

# Read CSV
df = pd.read_csv('data/employee_compensation.csv')


# In[15]:

# Find all orgnization group
orgnization_group = df['Organization Group'].unique()


# In[45]:

result = pd.DataFrame(columns=['Organization','Department','Total compensation'])
for o in orgnization_group:
    og = df[df['Organization Group']==o]
    num=0
    subResult=pd.DataFrame(columns=['Organization','Department','Total compensation'])
    for d in og['Department'].unique():
        dnf = og[og['Department']==d]
        # Calculate mean
        compensation = dnf['Total Compensation'].mean()
        subResult.loc[num]=[o,d,compensation]
        num+=1
    # Sort by compensation
    result = pd.concat([result,subResult.sort_values(by='Total compensation',ascending=False)])


# In[47]:

result.head()


# In[48]:

result.to_csv('ResultQ2P1.csv',index=False)


# In[ ]:



