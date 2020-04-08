#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
import pandas as pd 


# In[2]:


names = ['Bob','Jessica','Mary','John','Mel'] 
status = ['Senior','Freshman','Sophomore','Senior', 'Junior'] 
grades = [76,95,77,78,99] 
GradeList = zip(names,grades)

df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades']) 
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')

