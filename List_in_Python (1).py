#!/usr/bin/env python
# coding: utf-8

# <h2>List in Python</h2>
# <b><ol> A list :
#     <li>Is denoted by [ ]. </li>
#     <li>Is mutable : Can be modify after created.</li>
#     <li>Is a collection of values with same or different types.</li>
#     <li>We can fetch the value of a list using indexing.</li>
#     <li>We can slice in a list for printing in between values.</li>
# </ol></b>

# In[79]:


#Declaring a list variable
l1 = [1,2,5,6,4,3,0,6,8,9]
l2 = [34,65,"MY Love", 5.6, True]
#Display the value 
print("List_1 = ", l1)
print("List_2 = ",l2)


# In[80]:


#add a number in a list
l1.append(12) #Expected the number 12 at the end of the list
#Display the new output of l1
l1


# In[81]:


#Add element in a list 2
l1.extend([15])
l1


# In[82]:


#Operation in a list
op_li = l1 +l2
op_li
l1 + [23]


# In[83]:


#Sort a list
sorted_list = sorted(l1)
#Display the output
sorted_list
#sorted_list_1


# In[84]:


#Remove element in a list
l2.remove(65)
#Display the new list
print(l2)


# In[85]:


#Pop a element in a list
l1.pop()


# In[86]:


l1


# In[89]:


#Operation in a list
op_l = l2 + [23]
print(op_l)


# In[90]:


#Reverse a list
l2.reverse()


# In[91]:


#Display new list
l2


# In[97]:


#Count how many time a number is appear in a list
l1_count = l1.count(1)
l1_count


# In[96]:


#Count the number 6 in a list 
l1.count(6)


# In[98]:


l3 = [2,2,2,3,3,4,5,0,3,4,6,7,5,6,7,5,6,7,8,9,9,6,4]


# In[99]:


#Sort a list using sort method
l3.sort()


# In[100]:


#Display the output
l3


# In[ ]:





# In[102]:





# In[111]:


#Count the number 3
l3.count(3)


# In[112]:


#Find a specific number using index
l3.index(3)


# In[122]:


#Copy a list using copy or ddeep copy

l3_1 = l3.copy()


# In[123]:


l3_1


# In[124]:


#FInd the sum of the value in a list 
som_val = sum(l3)


# In[125]:


#Display the output
som_val


# In[127]:


#Other way to create a list

l5 = list(["Love", 2,3,4,5])
l5


# In[132]:


#Verify the type of a variable
type(l1)


# In[135]:


type(l3_1)


# In[130]:





# In[ ]:





# In[ ]:




