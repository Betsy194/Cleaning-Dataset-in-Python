#!/usr/bin/env python
# coding: utf-8

# ## Cleaning Dataset

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('MavenMarket_Products.csv')


# In[3]:


df


# #### Calling a Column

# In[4]:


df['recyclable']. head(50)


# #### To drop the Nan values on this [recyclable] column

# In[4]:


df['recyclable']. dropna()


# In[5]:


df['recyclable']. isna()


# #### To Fill the column with a number. remember nan is a float in python

# In[6]:


df['recyclable']. fillna(0)


# In[7]:


df['low_fat']. fillna(0, inplace = True)


# In[8]:


df['recyclable']. fillna(0, inplace = True)


# In[9]:


df


# In[10]:


df.dtypes


# #### This helps get the distinct value in a column

# In[11]:


df['product_brand'].value_counts().head(50)


# #### Group by function helps group column and form a new table.

# In[15]:


df.groupby(['product_brand'])['product_name']


# In[16]:


new = df.groupby(['product_brand','product_name'], as_index=False)[['product_weight', 
                                                                    'product_cost','product_retail_price']].sum()


# In[20]:


new_product = df.groupby(['product_brand','product_name'], as_index=False)[['product_weight', 
                                                                    'product_cost','product_retail_price']].agg(['sum','mean'])


# In[18]:


new


# In[21]:


new_product


# In[22]:


df.groupby(['product_brand'])['product_cost'].sum()


# In[26]:


product_brandgrp = df.groupby(['product_brand'])['product_weight'].sum


# In[27]:


product_brandgrp.get_group('Ebony')


# In[ ]:


product_brandgrp.get_group('Ebony')

