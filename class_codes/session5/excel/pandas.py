#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dfa = pd.read_excel("one.xlsx")    # dataframe


# In[3]:


dfa


# In[6]:


dfa.at[2, 'val_a']


# In[7]:


dfa.loc[2, 'val_a']


# In[11]:


dfa.iloc[2, 0]


# In[12]:


dfa.loc[2:6, 'val_b']


# In[14]:


dfa.loc[:, 'val_a']


# In[15]:


list(dfa.loc[:, 'val_a'])


# In[16]:


dfa


# In[17]:


dfa.sort_values('val_b')


# In[18]:


dfa


# In[19]:


dfa = pd.read_excel("one.xlsx")


# In[20]:


dfa


# In[21]:


dfa.sort_values('val_b')


# In[22]:


dfa


# In[23]:


dfb = pd.read_csv('annual-enterprise-survey-2020-financial-year-provisional-csv.csv')


# In[24]:


dfb.shape


# In[25]:


dfb


# In[26]:


dfa


# In[27]:


dfb.columns


# In[28]:


print(list(dfb.columns))


# In[31]:


dfb.info()


# In[32]:


dfb


# In[33]:


dfb['Units'].nunique()


# In[34]:


dfb['Units'].unique()


# In[36]:


print(dict(dfb["Units"].value_counts()))


# In[37]:


dfa


# In[39]:


# condition 
# dfa['val_b'] > 100

dfa [ dfa['val_b'] > 100 ]


# In[40]:


dfa.loc [ dfa['val_b'] == 189.5, 'val_c'] = 100


# In[41]:


dfa


# In[42]:


dfa.to_excel("three.xlsx", index=False)


# In[44]:


dfa = pd.read_excel("one.xlsx")
dfa.to_csv("one.csv", index=False)


# In[47]:


dfa.plot(x='val_c', y='val_b')


# In[48]:


import os


# In[49]:


os.listdir()


# In[ ]:




