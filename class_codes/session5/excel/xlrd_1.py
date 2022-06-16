#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xlrd


# In[2]:


book_a = xlrd.open_workbook("one.xlsx")


# In[3]:


print(book_a.nsheets)


# In[4]:


print(book_a.sheet_names())


# In[5]:


sheet_a = book_a.sheet_by_index(0)


# In[6]:


print(sheet_a.name)


# In[8]:


print(sheet_a.nrows)


# In[9]:


sheet_a.cell_value(rowx=4, colx=2)     #C5


# In[ ]:




