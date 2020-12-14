#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[12]:


marks = int(input("enter your marks out of 100 ::"))
if marks >= 95:
    print("Grade -> A+")
elif marks >=90 and marks <= 94:
    print("Grade -> A")
elif marks >=85 and marks <= 89:
    print("Grade -> B+")
elif marks >= 80 and marks <= 84:
    print("Grade -> B")
elif marks >=75 and marks <=79:
    print("Grade -> C+")
elif marks >= 70 and marks <= 74:
    print("Grade -> C")
elif marks >= 65 and marks <= 69:
    print("Grade -> D+")
elif marks >= 60 and marks <= 64:
    print("Grade -> D") 
elif marks >=33 and marks <= 59:
    print("Grade -> E")
elif marks < 33 and marks>=0:
    print("FAIL")


# # Question 2

# In[8]:



for item in range(1,1001):
   count = 0
   for i in range(2,(item//2+1)):
           if(item%i)==0:
               count =count+1
               break
   if item!=1 and count==0:
               print(item)
   


# # Question 3

# In[45]:


j=0
for item in range(1,11):
    print("TABLE OF ",item)
    for i in range(1,11):
        j=item*i
        print(j)
    item=item+1


# # Question 4

# In[1]:


X = int(input())
num=1
while(num<=X):
    count=0
    i=2
    
    while(i<=num//2):
        if(num%i==0):
            count=count+1
            break
        i=i+1
    if(count==0 and num!=1):
        print(num,end= ' ')
    num= num+1

