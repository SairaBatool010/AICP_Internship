#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Importing necessary libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Setting plotly default template
pio.templates.default = "plotly_white"

data=r'C:\Users\SKD\Downloads\Instagram data.csv'
# Load the dataset
df = pd.read_csv(data, encoding='latin1')


# In[4]:


print("Column names and their info:")
print(df.info())


# In[5]:


print("\nDescriptive statistics of the data:")
print(df.describe())


# In[6]:


# Q.3: Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values in the dataset:")
print(missing_values)


# In[7]:


# Q.4: Exploring the main feature of the data - Impressions column
# Visualizing the distribution of Impressions
fig = px.histogram(df, x='Impressions', title='Distribution of Impressions')
fig.show()


#  right skewed

# In[ ]:





# In[24]:


# Calculate the total count or sum of each engagement type
engagement_distribution = df[['Likes', 'Saves', 'Shares', 'Comments']].sum()

# Plot the distribution of engagement sources using a pie chart
plt.figure(figsize=(8, 8))
plt.pie(engagement_distribution, labels=engagement_distribution.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'orange', 'pink'])
plt.title('Distribution of Engagement Sources')
plt.show()


# In[15]:


# Q.9: Relationship between profile visits and follows
profile_follow_relationship = px.scatter(df, x='Profile Visits', y='Follows', title='Profile Visits vs Follows')
profile_follow_relationship.show()


# In[16]:


# Q.10: Type of hashtags used in the posts using a wordcloud
hashtags_text = ' '.join(df['Hashtags'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(hashtags_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Wordcloud of Hashtags Used in Posts')
plt.show()


# In[22]:


# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include='number')

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Visualize correlation matrix
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numeric Features')
plt.show()


# In[21]:


# Count the occurrences of each hashtag
hashtag_counts = df['Hashtags'].value_counts()

# Plot the distribution of hashtags
plt.figure(figsize=(10, 6))
ax = hashtag_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Used Hashtags')
plt.xlabel('Hashtag')
plt.ylabel('Count')
plt.xticks(rotation=45)

# Label only the first two hashtags on the x-axis
tick_labels = [text.get_text()[:20] for text in ax.get_xticklabels()]  # Truncate to first 20 characters
ax.set_xticklabels(tick_labels)

plt.show()


# In[20]:


# Group data by hashtag and calculate mean likes and impressions
hashtag_stats = df.groupby('Hashtags')[['Likes', 'Impressions']].mean().sort_values(by='Impressions', ascending=False)

# Plot the distribution of likes and impressions for each hashtag
plt.figure(figsize=(12, 6))
ax = hashtag_stats.head(10).plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Top 10 Hashtags by Likes and Impressions')
plt.xlabel('Hashtag')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(['Likes', 'Impressions'])

# Label only the first two hashtags on the x-axis
tick_labels = [text.get_text()[:20] for text in ax.get_xticklabels()]  # Truncate to first 20 characters
ax.set_xticklabels(tick_labels)

plt.show()


# Q.14: Summary of observations:
# 
# The correlation matrix reveals the relationships between different features in the dataset. Positive correlations indicate that as one feature increases, the other also tends to increase, while negative correlations indicate the opposite.
# The distribution of hashtags shows which hashtags are used the most in the posts. This information can be valuable for understanding popular trends or topics among the audience.
# Analyzing the distribution of likes and impressions received from each hashtag provides insights into the effectiveness of hashtags in engaging the audience. Hashtags with higher average likes and impressions may indicate higher relevance or appeal to the audience.
