#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


print(np.__version__)


# In[3]:


print("Hello, World!")


# In[4]:


print("Nama saya (Edwin)")


# In[5]:


print("NIM saya (2020071002)")


# In[9]:


if 5 > 2:
    print("Five is greater than two!")


# In[10]:


x = 5
y = "John"
print(x)
print(y)


# In[11]:


x = 4
x = "Sally"
print(x)


# In[20]:


def getFirst(myList):
    return myList[0]


# In[21]:


getFirst([1,2,3])


# In[17]:


getFirst([1,2,3,4,5,6,7,8,9,10])


# In[22]:


def getSecond(myList):
    return myList[1]


# In[23]:


getSecond([1,2,3])


# In[24]:


getSecond([1,2,3,4,5,6,7,8,9,10])


# In[25]:


def getLast(myList):
    return myList[-1]


# In[26]:


getLast([1,2,3])


# In[27]:


getLast([1,2,3,4,5,6,7,8,9,10])


# In[35]:


def getSum(myList):
    sum = 0
    for item in myList:
        sum = sum+item
    return sum


# In[36]:


getSum([1,2,3])


# In[37]:


getSum([1,2,3,4])


# In[59]:


def getKali(myList):
    sum = 1
    for item in myList:
        sum = sum*item
    return sum


# In[60]:


getKali([1,2,3])


# In[61]:


getKali([1,2,3,4])


# In[62]:


def getBagi(myList):
    sum = 1
    for item in myList:
        sum = sum/item
    return sum


# In[63]:


getBagi([1,2,3])


# In[64]:


getBagi([1,2,3,4])


# In[69]:


def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum


# In[66]:


getSum([[1,2,5],[3,4,7]])


# In[67]:


getSum([[1,2],[3,4]])


# In[68]:


getSum([[1,2,3],[4,5,6]])


# In[91]:


def getSum(myList):
    sum = 100
    for row in myList:
        for item in row:
            sum /= item
    return sum


# In[92]:


getSum([[10,1],[5,2]])


# In[97]:


def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum -= item
    return sum


# In[99]:


getSum([[1,2,3],[4,5,6]])


# In[100]:


def searchBinary(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while( first<=last and not foundFlag):
        mid = (first + last)//2
        if myList[mid] == item:
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag


# In[101]:


searchBinary([8,9,10,100,1000,2000,3000], 10)


# In[105]:


searchBinary([8,9,10,100,1000,2000,3000], 5)


# In[ ]:




