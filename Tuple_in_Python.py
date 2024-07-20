#!/usr/bin/env python
# coding: utf-8

# <h2>Tuples in Python</h2> <br>
# <b><ol> A tuple :
#     <li>Is denoted by ( ). </li>
#     <li>Is immutable : Cannot be modify after created.</li>
#     <li>Is a collection of values with same or different types.</li>
#     <li>We can fetch the value of a tuple using indexing.</li>
#     <li>We can slice in a tuple for printing in between values.</li>
# </ol></b>

# In[5]:


#Declaring a tuple variable
tupl_1 = 2,

tupl_2 = (1,2,3,4,5,6,7,"a","b", "c")

#Display the value 
print("Tuple_1 = ", tupl_1)
print("tuple_2 = ",tupl_2)


# In[7]:


#Print the type 
type(tupl_2)
#Display the new output of l1


# In[8]:


#Add element in a tuple 2
#We cannot add element to a tuple after created, because tuple is immutable.


# In[13]:


#Operation in a tuple
tupl_1 + (3,4,5)


# In[83]:





# In[15]:


#Remove element
#We cannot remove element in tuple
#Display the new list


# In[17]:


#Count how many time a number is appear in a tuple

t3 = (1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,45,5,5,5,5,5,6,6,7)


# In[19]:


#Count how many time a number is appear.
t3.count(2), t3.count(3)


# In[20]:


#Count the number 6 in a list 
t3.count(6)


# In[23]:


#Find element using index in a tuple
t3.index(3)


# In[24]:


t3


# In[26]:


#Create a list and then cnvert it to tuple

l = list(range(16))

#COnvert list to tuple

t = tuple(l)


# In[28]:


#Verify the type of each one
type(l),type(t)


# In[29]:


l


# In[30]:


t


# In[31]:


#FInd the length
len(l)


# In[32]:


len(t)


# In[ ]:




