#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xlwt


# In[2]:


book_a = xlwt.Workbook()


# In[3]:


sheet_a = book_a.add_sheet("monday")


# In[4]:


font_a = xlwt.Font()


# In[5]:


font_a.name = 'Arial'
font_a.italic = True
font_a.underline = False
font_a.bold = True

style = xlwt.XFStyle()
style.font = font_a


# In[6]:


sheet_a.write(0, 0, "hey", style)
sheet_a.write(0, 1, "hello", style)

book_a.save("five.xls")


# In[ ]:




