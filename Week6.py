#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=r'C:\Users\SKD\Downloads\births.csv'
# Load the dataset
df = pd.read_csv(data)

# Q.1: Add a new column "Decade"
df['Decade'] = (df['year'] // 10) * 10


# In[3]:


# Q.2: Show the descriptive statistics of the data
print("Descriptive statistics of the data:")
print(df.describe())


# In[4]:


# Q.3: Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values in the dataset:")
print(missing_values)


# In[5]:


# Q.4: Trend of male & female births every decade
trend = df.groupby(['Decade', 'gender'])['births'].sum().unstack()
trend.plot(kind='bar', stacked=True)
plt.title('Trend of Male & Female Births Every Decade')
plt.xlabel('Decade')
plt.ylabel('Total Births')
plt.xticks(rotation=45)
plt.show()


# In[6]:


# Q.5: Remove outliers using 5 standard deviations from the mean
df['z_score'] = np.abs((df['births'] - df['births'].mean()) / df['births'].std())
df = df[df['z_score'] <= 5]


# In[11]:


# Q.7: Group the data by month and day separately
births_by_month = df.groupby('month')['births'].sum()
births_by_day = df.groupby('day')['births'].sum()


# In[12]:


# Q.8: Plot the average number of births by date of the year
births_by_date = df.groupby(['month', 'day'])['births'].mean()
births_by_date.plot()
plt.title('Average Number of Births by Date of the Year')
plt.xlabel('Date of the Year')
plt.ylabel('Average Births')
plt.show()


# In[ ]:




