#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


index=['a','x','c',2,'e']
array=[1,4,9,6,7]
ser=pd.Series(array,index)
print(ser)


# In[7]:


dic_arr={'bilal':42,'Ayesha':38,'Hadia':39}
ser2=pd.Series(dic_arr)
print(ser2)


# In[10]:


data={ 'date':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/1/2017'],
    'Temperament':[32,35,28,24,32,31],    
    'windspeed':[6,7,2,7,4,2],
      'event':['snow','sunny','snow','snow','rain','sunny']
}
datafr=pd.DataFrame(data)
print(datafr)


# In[12]:


data2={ 'date':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/1/2017'],
    'Temperament':[32,35,28,24,32,31],    
    'windspeed':[6,7,2,7,4,2],
      'event':['snow','sunny','snow','snow','rain','sunny']
}
datafr=pd.DataFrame(data)
datafr.index=['a','b','c','d','e','f']
print(datafr)


# In[13]:


mean_temp=datafr['Temperament'].mean()
min_temp=datafr['Temperament'].min()
max_temp=datafr['Temperament'].max()


# In[14]:


print(mean_temp," ", min_temp," ", max_temp)


# In[16]:


path=r'C:\Users\SKD\Downloads\people.csv'


# In[24]:


df=pd.read_csv(path,usecols=["First Name","Sex","Email","Phone","Job Title"], skiprows=[1,5])
df.set_index(["Sex","Job Title"], inplace=True)
new=df.to_csv('NewPeople.csv')


# In[26]:


newdata=pd.read_csv('NewPeople.csv')


# In[27]:


print(newdata)


# In[35]:


file_path = r'C:\Users\SKD\Downloads\SampleWork.xlsx'
sampleWork=pd.read_excel(file_path,sheet_name=0,skiprows=[1],usecols=[0,-1],header=[1])
newsheet=sampleWork.to_excel('NewSampleWork.xlsx',index=False)


# In[38]:


df3=pd.read_excel('NewSampleWork.xlsx')
print(df3)


# In[55]:


dataQ8 = {
    'Name': ['Sonia', 'Bilal', 'Hifza', 'Kabir', 'Jazim'],
    'Age': [27, 24, 22, 32, 23],
    'Address': ['Karachi', 'Lahore', 'Sialkot', 'Peshawar', 'lhr'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd', 'bsc']
}

AICP_DF = pd.DataFrame(dataQ8)


# In[56]:


print(AICP_DF)


# In[57]:


df1 = AICP_DF[['Name', 'Qualification']]


# In[58]:


# Add a new column 'Height' with the given values
AICP_DF['Height'] = [5.1, 6.2, 5.1, 5.2, 5.1]

# Set column 'Name' as the index column
AICP_DF.set_index('Name', inplace=True)

# Retrieve row with index "Hifza"
row_hifza = AICP_DF.loc['Hifza']
print("Row with index 'Hifza':\n", row_hifza)

# Retrieve row with index 3
row_3 = AICP_DF.iloc[2]
print("\nRow with index 3:\n", row_3)

# Drop row with index 'Bilal'
AICP_DF.drop(index='Bilal', inplace=True)
print("\nDataFrame after dropping row with index 'Bilal':\n", AICP_DF)


# In[ ]:




