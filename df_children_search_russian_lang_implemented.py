
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np
import re


# In[45]:


df_minjust = pd.read_csv('data/Minjust2018.csv', 
                 header=None, 
                 usecols=[4, 27, 28, 33])
df_minjust.fillna('', inplace=True)
df_minjust.rename(columns={4: 'company_name', 
                           27: 'director', 
                           28: 'activity', 
                           33: 'founders'},
                  inplace = True)


# In[46]:


df_minjust


# In[47]:


df_decl = pd.read_csv('data/declaration.csv', 
                      header=None, 
                      usecols=[1, 2, 3, 4, 5])
df_decl.fillna('', inplace=True)
df_decl.rename(columns={1: 'surname', 
                        2: 'name', 
                        3: 'patronymic', 
                        4: 'workplace',
                        5: 'position'},
                  inplace = True)


# In[48]:


df_decl


# In[96]:


columns = ['company_name', 'director', 'activity', 'founders', 'surname', 'name', 'patronymic', 'workplace', 'position']
result = pd.DataFrame(columns=columns)


# In[101]:


for index, row in df_decl.loc[: 10].iterrows():
    search = search_df(df_minjust, 'founders', child_regex(row['surname'], row['name'])).copy()
    for column in df_decl.columns:
        search[column] = row[column]
    result = result.append(search, ignore_index=True)
    


# In[104]:


result


# In[ ]:


def search_df(df, column, pattern):
    return df.loc[df[column].str.contains(pattern)]
    
def child_regex(surname, name):
    pattern = re.compile(surname +
                         r'а?\s+\w+\s+' + # First name
                         remove_vowels(name) + # Patronymic
                         r'|' + 
                         r'\w+\s+' + # First name
                         remove_vowels(name) + r'\w+\s+' + # Patronymic
                         surname,
                         re.IGNORECASE)
    return pattern

def remove_vowels(name):
    while True:
        if name[-1] not in ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я', 'й']:
            break
        else:
            name = name[: -1]
    return name

