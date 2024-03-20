#!/usr/bin/env python
# coding: utf-8

# In[26]:


import matplotlib.pyplot as plt
import pandas as pd
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('sample')
plt.show()


# In[14]:


y2=[4,0,3]
plt.plot(x,y,label='Line 1',color='red',linewidth=2)
plt.plot(x,y2,label='Line 2', color='blue',linewidth=2)
plt.legend()
plt.xlabel('X axis')
plt.ylabel('Y label')
plt.title('multiple lines')
plt.show()


# In[20]:


plt.plot(x,y,label='Line 1', marker='o',linestyle='--')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()


# In[23]:


languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']

# Popularity
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.barh(languages,popularity,color='skyblue')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.gca().invert_yaxis()
plt.show()


# In[27]:


data = {
    'a': [2, 4, 6, 8, 10],
    'b': [4, 2, 4, 2, 2],
    'c': [8, 3, 7, 6, 4],
    'd': [5, 4, 4, 4, 3],
    'e': [7, 2, 7, 8, 3]
}
df1=pd.DataFrame(data)
print(df1)


# In[31]:


df1.plot(kind='bar')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()


# In[37]:


countries = ['United States', 'Great Britain', 'China', 'Russia', 'Germany']
gold_medals = [46, 27, 26, 19, 17]

# Plot pie chart
plt.figure(figsize=(8, 6))
plt.pie(gold_medals, labels=countries, autopct='%1.1f%%', startangle=600)
plt.title('Gold Medal Achievements of Top 5 Countries in 2016 Summer Olympics')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()


# In[35]:


math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Plot scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(marks_range, math_marks, color='blue', label='Math Marks')
plt.scatter(marks_range, science_marks, color='red', label='Science Marks')
plt.title('Scatter Plot of Mathematics and Science Marks')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




