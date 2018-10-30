
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import re


# In[34]:


df = pd.read_csv('data/Minjust2018.csv', 
                 header=None, 
                 usecols=[4, 27, 28, 33])
df.fillna('', inplace=True)
df.rename(columns={4: 'name', 
                   27: 'director', 
                   28: 'activity', 
                   33: 'founders'},
              inplace = True)


# In[35]:


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


# In[36]:


df.loc[df['founders'].str.contains(child_regex('Тухватшин', 'Рустам'))]

