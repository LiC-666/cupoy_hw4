
# coding: utf-8

# 作業目標
# 
# 熟悉邏輯運算
# 
# 作業重點
# 
# 五大類邏輯函式與其對應的函式操作
# 
# 題目:
# 
# english_score = np.array([55,89,76,65,48,70])
# 
# math_score = np.array([60,85,60,68,55,60])
# 
# chinese_score = np.array([65,90,82,72,66,77])
# 
# 上3列共六位同學的英文、數學、國文成績，
# 第一個元素代表第一位同學，
# 舉例第一位同學英文55分、數學60分、國文65分，
# 運用上列數據回答下列問題。
# 
# 
# 
# 
# 

# In[20]:


#有多少學生英文成績比數學成績高?


# In[1]:


import numpy as np


# In[2]:


eng = np.array([55,89,76,65,48,70])
math = np.array([60,85,60,68,55,60])
ch = np.array([65,90,82,72,66,77])


# In[9]:


np.greater(eng, math)


# In[17]:


t = np.array([False,  True,  True, False, False,  True])


# In[28]:


print("有", np.sum(t != 0), "個人")


# In[30]:


#ANS : 3 個


# In[19]:


#2.是否全班同學最高分都是國文?


# In[22]:


c = np.greater_equal(ch, eng)
c


# In[23]:


d = np.greater_equal(ch, math)
d


# In[25]:


s = np.logical_and(c, d)
s


# In[29]:


np.sum(s != 0)


# In[31]:


#ANS : 是

