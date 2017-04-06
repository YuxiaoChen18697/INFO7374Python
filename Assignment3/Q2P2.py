
# coding: utf-8

# Q2_PART TWO
# • Use 'employee_compensation' data set.
# • Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# • Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# • For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# • Display the top 5 Job Families according to this percentage value using df.head().
# • Write the output (jobs and percentage value) to a csv.

# In[20]:

from pandas import Series, DataFrame
import pandas as pd


# In[21]:

# Read CSV
df = pd.read_csv('data/employee_compensation.csv')


# In[22]:

df = df[df['Year Type']=='Calendar']
df = df[['Job Family', 'Employee Identifier' , 'Salaries', 'Overtime', 'Total Benefits', 'Total Compensation']]
df.head()


# In[24]:

average_salary = df.groupby(['Job Family', 'Employee Identifier'], as_index=False).mean()
average_salary.head()


# In[25]:

overtime = average_salary[average_salary['Overtime'] > average_salary['Salaries']*0.05]
overtime.head()


# In[26]:

final = overtime[['Job Family', 'Total Benefits', 'Total Compensation']]
result = final.groupby(['Job Family'], as_index=False).mean()


# In[27]:

result['Percentage_Total_Benefit'] = result['Total Benefits'] / result['Total Compensation']*100


# In[28]:

result = result.sort_values(by='Percentage_Total_Benefit', ascending=False)


# In[29]:

result.head()


# In[30]:

result.to_csv('ResultQ2P2.csv',index=False)


# In[ ]:



