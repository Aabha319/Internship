#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11. finding factorial of a given number
number = int(input("enter a number to find factorial"))
factorial = 1
if number<0:
    print("cannot find factorial for negative numbers")
elif number==0:
    print("factorialof 0 is 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("factorial of ",number," is ",factorial)


# In[4]:


#12.finding whether a given number is a prime or composite number
number = int(input("Enter any number : "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is a composite number")
            break
    else:
        print(number, "is a prime number")
elif number == 0 or 1:
    print(number, "is a neither prime nor composite number")
else:
    pass


# In[7]:


#13.to check whether given string is palindrome or not
s=input("enter a string")
if (s==s[::-1]):
    print("the given string is a palindrome")
else:
    print("the given string is not a palindrome")


# In[8]:


#14.to find out third side of right angke traingle if two sides are given
def side(a,b,hypo):
        if a == str("x"):
            return ("a = " + str(((hypo**2) - (b**2))**0.5))
        elif b == str("x"):
            return ("b = " + str(((hypo**2) - (a**2))**0.5))
        elif hypo == str("x"):
            return ("Hypo = " + str(((a**2) + (b**2))**0.5))
        else:
            return "Pass"
    
print(side(3,4,'x'))
print(side(3,'x',5))
print(side('x',4,5))


# In[3]:


#15. to print the frequency of each of the characters present in a given string
def frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
str1=input("enter a string ")
print(frequency(str1))


# In[ ]:




