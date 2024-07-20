#!/usr/bin/env python
# coding: utf-8

# <h2>Dictionnary in Python</h2> <br>
# <b><ol> A dictionnary :
#     <li>Are represented with { } having <b>key</b> and <b>value</b> pair. </li>
#     <li>Indexing is done by keys.</li>
#     <li>Keys can be numbers as well as strings.</li>
#     <li>Keys are unique and hence immutable whereas dictionnary are mutable.</li>
#    
# </ol></b>

# In[73]:


#Declaring a dictionnary variable
d1 = {"Name " : "Wedson", "Age" : 22, "Country " : "Haiti"}
#Display the value 
print(d1)


# In[74]:


#Print the type 
type(d1)
#Display the new output of l1


# In[75]:


#Find all keys
d1.keys()

#We can add element to a dict after created, because tuple is mutable.


# In[76]:


#VAlues in a dict
d1.values()


# In[77]:


#Items in a dict
d1.items()


# In[42]:


#Remove item from a dictionnary using pop method
d1.popitem()


# In[43]:


d1


# In[44]:


#Copy a dict
dc = d1.copy()
dc


# In[45]:


#Verify
dc == d1


# In[ ]:





# In[46]:


#Update a dict

d1.update()



# In[47]:


d1


# In[48]:


#Length of a dict
len(d1)


# In[49]:


d1


# In[53]:


#Add element to a dict
d1["Name"] = "Jimmy"


# In[55]:


d1["Age"] = 23
d1["Tail"] = 34


# In[56]:


d1


# In[71]:


d1.setdefault(1)


# In[72]:


d1


# In[ ]:




