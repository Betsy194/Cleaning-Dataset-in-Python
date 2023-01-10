#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_excel('sales_2017.xlsx')


# In[3]:


df


# In[9]:


df.rename({'Order': 'Order ID', 'Customer': 'Customer ID', 'Sales': 'Sales Person', 
           'Order.1':'Order date','Ship':'Ship date', 'Order.2':'Order Priority',
          'Order.3': 'Order Quantity', 'Unit Sell':'Unit SellPrice', 'Discount': 'Discount Percent',
          'Shipping': 'Shipping Amount', 'Ship Mode':'Ship Mode Container'},
          axis='columns', inplace=True)
df.head()


# In[12]:


df = df.drop(df.index[[0]])


# In[13]:


df


# In[17]:


df.loc [1, 'Order date']


# In[18]:


# To convert Date to Datetime
df['Order date'] = pd.to_datetime(df['Order date'])


# In[19]:


df['Ship date'] = pd.to_datetime(df['Ship date'])


# In[20]:


df.loc [1, 'Order Quantity']


# In[21]:


df.info()


# In[22]:


df['Order Quantity'] = df['Order Quantity'].astype(float)


# In[23]:


df['Unit SellPrice'] = df['Unit SellPrice'].astype(float)


# In[24]:


df['Discount Percent'] = df['Discount Percent'].astype(float)


# In[25]:


df['Shipping Amount'] = df['Shipping Amount'].astype(float)


# In[26]:


df.info()


# In[32]:


df.loc [1, 'Order date'].day_name()


# In[33]:


df['Order date'].dt.day_name()


# In[ ]:




