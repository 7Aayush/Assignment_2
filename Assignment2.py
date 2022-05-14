#!/usr/bin/env python
# coding: utf-8

# In[ ]:


txt = "Python is a case sensitive language"
print(txt)

a= len(txt)
print(a)

b="Python is a case sensitive language"[::-1]
print(b)

c=txt[10:26]
print(c)

d=txt.replace("a case sensitive","object oriented")
print(d)

e=txt.find('a')
print(e)

f=txt.replace(' ','')
print(f)


# In[ ]:


a= "Aayush Bhalla"
b= "21102050"
c= "Civil"
d= "8.5"

print("Hey, "+ a + " here!\n")
print("My SID is "+ b +"\n")
print("I am from "+ c + " department and my CGPA is "+ d)


# In[ ]:


a=56
b=10

x=a&b
print("a&b = "+ str(x))

y=a|b
print("a|b = "+ str(y))

z=a^b
print("a^b = "+ str(z))

l_shift1=a<<2 #left shift a with 2 bits
l_shift2=b<<2 #left shift b with 2 bits
print("left shifting a with 2 bits = "+ str(l_shift1) + "\nleft shifting b with 2 bits = "+ str(l_shift2))

r_shift1=a>>2 #right shift a with 2 bits
r_shift2=b>>2 #right shift b with 2 bits
print("right shifting a with 2 bits = "+ str(r_shift1) + "\nright shifting b with 2 bits = "+ str(r_shift2))


# In[ ]:


txt=str(input())

x='name' in txt

if x==1:
    print("Yes")
else:
    print("No")


# In[ ]:


a=int(input())
b=int(input())
c=int(input())

while a<b+c and b<a+c and c<a+b:
    print("Yes")
    break

while a>b+c or b>a+c or c>a+b:
    print("No")
    break


# In[ ]:


print("enter 1st number")
number_1=int(input())

print("enter 2nd number")
number_2=int(input())

ex_or=number_1^number_2 #to know which bits are different as they will give output 1
bin_exor=bin(ex_or)
check_string=str(bin_exor)

a=check_string.count('1')
print(a)

