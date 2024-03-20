#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

datapath=r'C:\Users\SKD\Downloads\menu.csv'
data=pd.read_csv(datapath)
print(data.head())


# In[9]:


stats=data.describe()
print(stats)


# In[14]:


maxvalue=data[['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein', 
                 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)', 
                 'Iron (% Daily Value)']].max()
print(maxvalue)


# In[17]:


numeric_columns = data.select_dtypes(include=['float64', 'int64'])
corre=numeric_columns.corr()
plt.figure(figsize=(20,20))
sns.heatmap(corre, annot=True, cmap='coolwarm', fmt=".2f",linewidths=0.5)
plt.show()


# In[25]:


plt.figure(figsize=(10, 8))
sns.boxplot(y='Category', x='Calories', data=data)
plt.xticks(rotation=70)  # Rotate x-axis labels for better readability
plt.title('Boxplot of Calories by Category')
plt.xlabel('Category')
plt.ylabel('Calories')
plt.show()


# In[31]:


# Create a dictionary to store the maximum values and corresponding items
max_items = {}

# Loop through each attribute and find the item with the highest quantity
for attribute in attributes:
    max_item_index = data[attribute].idxmax()
    max_item_name = data.loc[max_item_index, 'Item']
    max_value = data.loc[max_item_index, attribute]
    max_items[attribute] = {'item': max_item_name, 'value': max_value}

# Display the summary
for attribute, info in max_items.items():
    print(f"{attribute}: {info['item']} - {info['value']}")


# In[29]:


attributes = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 
              'Sugars', 'Protein', 'Vitamin A (% Daily Value)', 
              'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)', 
              'Iron (% Daily Value)']

# Loop through each attribute and draw the stripplot
for attribute in attributes:
    plt.figure(figsize=(6, 3))
    sns.stripplot(x='Category', y=attribute, data=data, jitter=True)
    plt.title(f'Stripplot of {attribute} for Each Category')
    plt.xlabel('Category')
    plt.ylabel(attribute)
    plt.xticks(rotation=45)  # Rotate category labels for better visibility
    plt.show()


# In[27]:


category = 'Beef & Pork'  # Replace 'Beef & Pork' with the desired category
filtered_df = data[data['Category'] == category].sort_values(by='Calories')

# Plot horizontal bar graph
plt.figure(figsize=(12, 8))
sns.barplot(x='Calories', y='Item', data=filtered_df, order=filtered_df['Item'])
plt.title(f'Calories in Items of {category} Category (Ascending Order)')
plt.xlabel('Calories')
plt.ylabel('Item')
plt.show()


# In[ ]:




