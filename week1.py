#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[10]:


even_array = np.arange(30,71, 2)


# In[11]:


print(even_array)


# In[15]:


rand_array= np.random.randn(15)


# In[16]:


print(rand_array)


# In[19]:


matrix1=np.array([[10,20],[3,4]])
matrix2=np.array([[5,6],[1,2]])
cross_prod=np.cross(matrix1,matrix2)
print(cross_prod)


# In[22]:


array=np.array([[10,12],[3,4]])


# In[23]:


det=np.linalg.det(array)
print(det)


# In[24]:


rand_2d=np.random.rand(3,3,3)


# In[25]:


print(rand_2d)


# In[26]:


rand_5x5=np.random.rand(5,5)


# In[27]:


print(rand_5x5)


# In[29]:


print(np.min(rand_5x5))


# In[30]:


print(np.max(rand_5x5))


# In[43]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
mean=np.mean(arr,axis=1)
std_dev=np.std(arr,axis=1)
var=np.var(arr,axis=1)


# In[44]:


print(mean)
print(std_dev)
print(var)


# In[ ]:




