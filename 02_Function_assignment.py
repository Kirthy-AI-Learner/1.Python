#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create Function


# In[2]:


# Sub-fields in AI are:
#  Machine Learning
#  Neural Networks
#  Vision
#  Robotics
#  Speech Processing
#  Natural Language Processing


# In[3]:


subfields = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']


# In[4]:


def listFunction():
    print("Sub-fields in AI are: ")
    for fields in subfields:
        print(fields)


# In[5]:


listFunction()


# In[6]:


def OddEven():
    num = int(input("Enter the number: "))
    if(num%2==0):
        print(num," is Even number")
    else:
        print(num," is Odd number")


# In[7]:


#Create a function that checks whether the given number is Odd or Even


# In[ ]:


OddEven()


# In[9]:


# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female


# In[10]:


def Eligible():
    Gender = input("Your Gender: ")
    Age = int(input("Your Age: "))
    if(Gender == 'Male' and Age >21):
        print("ELIGIBLE")
    elif(Gender == 'Female' and
         Age >18):
        print("ELIGIBLE")
    else:
        print('NOT ELIGIBLE')


# In[11]:


Eligible()


# In[1]:


def percentage():
    subject1 = int(input("Subject1 = "))
    subject2 = int(input("Subject2 = "))
    subject3 = int(input("Subject3 = "))
    subject4 = int(input("Subject4 = "))
    subject5 = int(input("Subject5 = "))
    total = subject1+subject2+subject3+subject4+subject5
    percentage = total/5
    print('Total: ',total)
    print('Percentage: ',percentage)


# In[2]:


percentage()


# In[3]:


def triangle():
    Height = int(input("Height : "))
    Breadth = int(input("Breadth : "))
    print('Area formula: (Height*Breadth)/2')
    area=(Height*Breadth)/2
    print('Area of Triangle:',area)
    Height1 = int(input("Height1 : "))
    Height2 = int(input("Height2 : "))
    Breadth = int(input("Breadth : "))  
    print('Perimeter formula: Height1+Height2+Breadth')
    perimeter = Height1+Height2+Breadth
    print('Perimeter of Triangle: ',perimeter)


# In[4]:


triangle()


# In[ ]:




