
# coding: utf-8

# In[19]:


import pandas as pd


# In[5]:


spisok = ['a', 'b', 'c', 'd', 'e']
result = []

for x in spisok:
    result.append(x + 'k')


# In[6]:


result


# In[7]:


spisok = [1, 2, 3, 4, 5]
result = []

for x in spisok:
    result.append(x * 2)


# In[9]:


print(result)


# In[10]:


spisok = ['a', 'b', 'c', 'd', 'e']

result = [x + 'k' for x in spisok]


# In[11]:


result


# In[13]:


def complicated_function(letter):
    return letter + 'k'


# In[14]:


spisok = ['a', 'b', 'c', 'd', 'e']


result = [complicated_function(x) for x in spisok]


# In[15]:


result


# In[16]:


def square(x):
    return x**2


# In[17]:


spisok = [1, 2, 3, 4, 5]
result = [square(x) for x in spisok]


# In[18]:


result


# In[20]:


pd.Series(result)

