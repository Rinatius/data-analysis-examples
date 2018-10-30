
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('data/Minjust2018.csv', 
                 header=None, 
                 usecols=[4, 27, 28, 33])

df.fillna('', inplace=True)
df.rename(columns={4: 'name', 
                   27: 'director', 
                   28: 'activity', 
                   33: 'founders'},
              inplace = True)


# In[4]:


df


# In[7]:


def count_letters(words):
    return pd.Series([len(word) for word in words])


# In[8]:


df.loc[count_letters(df['director']) == count_letters(df['name'])]

