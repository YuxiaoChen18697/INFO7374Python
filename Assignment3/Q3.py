
# coding: utf-8

# Q3_PART ONE
# • Use ‘cricket_matches’ data set.
# • Calculate the average score for each team which host the game and win the game.
# • Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# • Display a few rows of the output use df.head()
# • Generate a csv output

# In[38]:

from pandas import Series, DataFrame
import pandas as pd


# In[39]:

# Read CSV
df = pd.read_csv('data/cricket_matches.csv')


# In[40]:

# Find team host the game and win
df1 = df[df['home']==df['winner']]


# In[41]:

# Dicide which row to select
def findScore(row):
    if row['home'] == row['innings1']:
        return row['innings1_runs']
    else:
        return row['innings2_runs']


# In[43]:

df1['Score'] = df1.apply(findScore,axis=1)
df1.head()


# In[48]:

# Select the columns
df1= df1[['home','Score']]
df1.head()


# In[51]:

# Calculate the means
grouped = df1.groupby(df1['home'],as_index=False).mean()
grouped.head()


# In[52]:

grouped.to_csv('ResultQ3P1.csv')


# In[ ]:



