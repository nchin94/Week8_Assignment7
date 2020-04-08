#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt 
import pandas as pd 


# In[11]:


names = ['Bob','Jessica','Mary','John','Mel'] 
status = ['Senior','Freshman','Sophomore','Senior', 'Junior'] 
grades = [76,95,77,78,99] 
GradeList = zip(names,grades,status)

df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades','Status']) 
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[12]:


df2 = df.set_index(df['Names']) 


# In[13]:


df2


# In[18]:


df2.plot(kind="bar", x = "Status")

