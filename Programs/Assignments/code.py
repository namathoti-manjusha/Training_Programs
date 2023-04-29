##Coding Questions on Numbers

#1.Write a to reverse an Integer
'''
n=input('Enter Any Number:')
num=n[::-1]
rev=int(num)
print(rev)
'''
#Palendrome number
'''
n=input('Enter Any Number:')
num=n[::-1]
if n==num:
    print(n,'is Palendrome Number')
else:
    print(n,'it is not a Palendrome Number')
'''

#2.WAP to check whether the intiger is Armsteong are not
'''
n=eval(input('Enter Any Number:'))
result=0
t=n
while t>0:
    digit=t%10
    result+=digit**3
    t=t//10
if n==result:
    print(n,'is an Armstrong Number')
else:
    print(n,'is not Armstrong Number')
'''

##3.WAP to check whwather the Given Number is Prime are not
'''
n=eval(input('Enter Any Number:'))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,'it is not a Prime Number')
            break
    else:
        print(n,'it is Prime Number')
       
'''
#4.WAP to find greatest among three integers

'''
n1=int(input('Enter First Number:'))
n2=int(input("Enter second Number:"))
n3=int(input("Enter third number:"))
print("Maximum is ",end='')
if n2<=n1>=n3:
    print(n1)
elif n1<=n2>=n3:
    print(n2)
elif n1<=n3>=n2:
    print(n3)

'''

#5.WAP  to find sum of digits of number using recrsion
'''
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(6))
'''

##6.swap two Numbers without using Third variable
'''
num1 = eval(input('Enter first number:'))
num2 = eval(input('Enter second number:'))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1)
print(num2)
'''
##7.swap two numbers using third number
'''
num1 = input('Enter first number:')
num2 = input('Enter second number:')
temp=num1
num1=num2
num2=temp
print('After swapping',num1)
print('After swapping',num2)
'''

##8.WAP to find Prime Factor of Given integers
'''
a=eval(input('Enter Any Number:'))
fact=[]
divisor=2
while divisor<=a:
    if a%divisor==0:
        fact.append(divisor)
        a=a/divisor
    else:
        divisor+=1
print('factors are',fact) 
'''

##9.WAP to add two integers without using arthmetic operator
'''
def add(x,y):
    for i in range(1,y+1):
        x=x+1
    return x
x=add(10,22)
print(x)
''' 

#10.WAP in python to find given number is perfect or not
'''
num=eval(input('Enter Any Number:'))
result=0
for i in range(1,num):
    if (num%i==0):
        result=result+i
if num==result:
    print(num,'is perfect Number')
else:
    print(num,'is not a perfect Number')

'''
## Coding Questions on String

#1.WAP in python which will remove any given character in a string 
'''
n=input('Enter Any thing:')
for i in n:
    k=i.split(' ')
    for j in k:
        if j!='a':
            print(j)

'''
#2.WAP in python to count occurances of given character in a string
'''
n=input('Enter Any thing:')
k=n.count('a')
print(k)

n=input('Enter Any thing:')
count=0
for i in n:
    if i=='a':
        count=count+1
print(count)
'''

#3. WAP to check if two strings are Anagram
'''
s1=input('Enter First Word:')
s2=input('Enter Second Word:')
s1=sorted(s1)
print(s1)
s2=sorted(s2)
print(s2)
if s1==s2:
    print(s1,'is Anagram')
else:
    print(s2,'is not anagram')

'''
#4.WAP to check a string is palendrome or not
'''
n=input('Enter Anything:')
k=n[::-1]
if n==k:
    print('it is Palendrome')
else:
    print('it is not palendrome')

'''
##python programming code questions on list

#1. in list 1-100 numbers are stored,one number is missing how do you find it
'''
lst=[1,2,3,5,6,8]
print([i for i in range(1,11) if i not in lst])
'''
#2.in list 1-100 multiple numbers are duplicates,how do you find it
'''
lst=[3,5,2,6,7,2,5,2,4,3,6,8,6]
print(list(set([i for i in lst if lst.count(i) >= 2])))
'''
#3.how to find all pairs in list of integers whose sum is equal to given number
'''
n=eval(input('enter any number:'))
for i in range(1,11):
    for j in range(i,11):
        if i+j==n:
            print(i,j)
'''

#4.how to compare two lists is equal in size or not
'''
lst=[1,2,3,4,4,5,6,5,8,7,9]
lst2=[2,4,8,6,4,7,8,3,7,2]
if len(lst)==len(lst2):
    print('it is equal')
else:
    print('not equal')
'''
#5.find largest and smallest numbers in the list
'''
lst=[2,4,5,7,8,9,1,3,9,5,7,20,54,60]

li=sorted(lst)
print(li[-1],li[0])


lst1=[]
while lst:
    small=lst[0]
    for x in lst:
        if x < small:
            small=x
    lst1.append(small)
print(lst1[-1])
'''
#6.second highest number in an integer list
'''
lst=[2,4,5,7,8,9,1,3,9,5,7,20,54,60]
li=sorted(lst)
print(li[-2])
'''
#7.find top two maximum numbers in list
'''
lst=[2,4,5,7,8,9,1,3,9,5,7,20,54,60]
li=sorted(lst)
print(li[-1],li[-2])
'''

#remove duplicate elements from the list
'''
lst=[2,4,5,7,8,9,1,3,9,5,7,20,54,60]
print(set(lst))
'''

lst=[2,4,5,7,8,9,1,3,9,5,7,20,54,60]
lst1=[]
for i in lst:
    if lst.count(i)>=2:
        lst1.append(i)
print(set(lst1))
        
