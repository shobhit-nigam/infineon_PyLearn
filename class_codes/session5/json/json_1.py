#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


with open("example_1.json", "r") as fj:
    data = json.load(fj)


# In[3]:


print(type(data))


# In[4]:


data


# In[5]:


data['fruit']


# In[6]:


with open("example_2.json", "r") as fj:
    datab = json.load(fj)


# In[7]:


datab


# In[10]:


datab['quiz']['sport']


# In[12]:


datab['quiz']['sport']['q1']['question']


# In[13]:


def read_dict(d):
    for k, v in d.items():
        if type(v) is dict:
            read_dict(v)
        else:
            print(v)
        print("------")


# In[14]:


read_dict(datab)


# In[15]:


dict_b = {'aa':100, 'bb':200, 'ff':70}


# In[16]:


with open("example_3.json", "w") as fj:
    json.dump(dict_b, fj)


# In[ ]:




