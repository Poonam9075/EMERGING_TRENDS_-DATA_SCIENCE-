#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Exp No: 1


# In[3]:


#Aim: To perform Data Acquisition of given Data set using Python


# In[4]:


#Name: Poonam Manohar Khandagale
#Roll No: 34
#Sec: B
#Subject: Emerging Trends
#Date: 26-07-2023


# In[5]:


#importing the basic library
import pandas as pd


# In[6]:


import os 


# In[7]:


os.getcwd()


# In[9]:


os.chdir('C:\\Users\\HP\\Desktop')


# In[10]:


data=pd.read_csv("diabetes.csv")


# In[11]:


data.head()


# In[13]:


data.tail()


# In[14]:


data.head(50)


# In[ ]:




