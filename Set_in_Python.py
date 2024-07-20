#!/usr/bin/env python
# coding: utf-8

# <h2>Set in Python</h2> <br>
# <b><ol> A set :
#     <li>Is denoted by { }. </li>
#     <li>Is mutable : Can be modify after created.</li>
#     <li>Is a collection of unique values with same or different types.</li>
#     <li>never follows a sequence.</li>
#     <li>Doesn't permit duplicate values.</li>
#     <li>Values cannot be fletched using index.</li>
#     <li>Union, intersection, difference and symetric difference are supported.</li>
# </ol></b>

# In[5]:


#Declaring a set variable

s1 = {1,2,3,4,5,6,7,"a","b", "c"}
s2 = set((1,2,3,7,89,9))
#Display the value 
print("set_1 = ", s1)
print("set_2 = ",s2)


# In[6]:


#Print the type 
type(s1)
#Display the new output of l1


# In[10]:


#Add element in a set
s2.add(90)

#We can add element to a set after created, because tuple is mutable.
s2.add(99)
s2


# In[15]:


#Operation in a set

#Union

s1|s2


# In[16]:


#Union 2
s1.union(s2)


# In[18]:


#Intersection
s1&s2


# In[19]:


s1.intersection(s2)


# In[20]:


#Copy a set
s1.copy()
#Remove element
#We cannot remove element in tuple
#Display the new list


# In[21]:


#Remove element from a set
s1.remove("b")


# In[22]:


s1


# In[24]:


#Update a set
s1.update()


# In[25]:


s1


# In[27]:


#Pop in a set

s1.pop()


# In[29]:


#Symmetric difference in a set
s1.symmetric_difference(s2)


# In[31]:


#Create a list and then cnvert it to list

l = list(range(16))

#COnvert list to tuple

s4 = set(l)


# In[33]:


#Verify the type of each one
type(l),type(s4)


# In[34]:


l


# In[35]:


s4


# In[36]:


#FInd the length
len(l)


# In[37]:


len(s4)


# In[39]:


#Create a list
l1 = [1,1,1,1,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,"love","Darling", "Kerry"]
#FInd the length
len(l1)


# In[40]:


#Convert it to set
s6 = set(l1)


# In[44]:


#Find the length now
len(s6)


# Note : The lengths are different because set doesn't permit duplicate value

# In[45]:


s6


# In[46]:


#Is subset 
s1.issubset(s2)


# In[47]:


s2.issubset(s1)


# In[48]:


#Clear a set
s6.clear()


# In[49]:


s6


# In[ ]:




