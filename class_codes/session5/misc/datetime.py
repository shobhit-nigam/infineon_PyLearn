#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[3]:


print("hey")
time.sleep(5)
print("hello")


# In[4]:


import datetime


# In[5]:


obja = datetime.date.today()


# In[6]:


print(obja)


# In[7]:


print(obja.year)


# In[8]:


objb = datetime.date.today()


# In[10]:


print(objb.strftime("%d and %m"))


# In[11]:


print(objb.strftime("%d %B"))


# In[12]:


print(objb.strftime("%d %b"))


# In[13]:


objb = datetime.datetime.now()

print(objb.strftime("%H hours and %M minutes"))


# In[15]:


obj_covid = datetime.date(year=2020, month=3, day=27)


# In[17]:


delta = obj_covid - obja


# In[18]:


print(delta)


# In[ ]:




