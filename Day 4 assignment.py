#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[2]:


f=open("Niyanshi.txt",'w')
f.write("I LOVE LETSUPGRADE")
f.close()


# In[4]:


f=open("Niyanshi.txt",'r+')
f.read()
f.write("\nGreat learning with letsupgrade")
f.close()


# # Question 2

# In[20]:


n= int(input("Enter the number to find factorial of it::"))
def fact(n):
    if n>=1:
        return n*fact(n-1)
    else:
        return 1
print("Factorial of ",n ,"is",fact(n))


# In[ ]:




