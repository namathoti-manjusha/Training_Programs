
##1.How to fetch an alternative elements from the given list
'''
lst=[1,10,2,20,3,30,4,40,5,50,6,60]
lst1=[]
for i in lst:
    if lst.index(i)%2!=0:
        lst1.append(i)
print(lst1)
'''

##2. Write a python program which accepts a sequence of comma-separated numbers from console and generate a list which contains every number.
'''
l = input('Enter any number:')
li = l.split(',')
li = list(li)
print(li)
'''

##3.Write a python program which will find all such numbers which are divisible by 7 but are not a multiple of 5, and those numbers are between 100 and 200 (both included).
'''
lst=[]
for i in range(100,200):
    if i%7==0 and i%5!=0:
        lst.append(i)
print(lst)
'''

##4.Write a python program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
'''
n=int(input("Enter a number:"))
lst=[]
for i in range(1,n+1):
    lst.append(i)
    d={}.fromkeys(lst,0)
    for i in lst:
        d[i]=i*i
print(d)

'''
#5.our organization contains 1000 employees.all the names are stored in the list now i want to check wheather my name is stored or not in the list? what should i do?
'''
st=['manju','prathyu','likhitha','swetha','divya','asha']
if 'manju' in st:
    print('yes')
'''

##6.How can we create a new dictionary by using existing tuple object?
'''
T1=(10,20,4,3,5)
d={}.fromkeys(T1,0)
print(d)
'''
##7.Define a python function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
'''
a=str(input("enter a string:"))
b=str(input("enter a string:"))
if len(a)>len(b):
    print(a)
elif len(a)==len(b):
        print("",a,'\n',b)
else:
    print(b)
'''

##8.Define a python function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
'''
n=eval(input('Enter Any Number:'))
def evenorodd(n):
    if n%2==0:
        print('It is Even Number')
    else:
        print('It is Odd Number')
evenorodd(n)
'''
##9.Define a python function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
'''
lst=[]
def squares(n):
    for i in range(1,4):
        lst.append(i)
    d={}.fromkeys(lst,0)
    for i in lst:
        d[i]=i*i
    print(d)
squares(4)

'''
##10.Define a python function which can print a dictionary where the keys are numbers between 1 and 20(both included) and the values are square of keys.

'''
lst=[]
def squares(n):
    for i in range(1,21):
        lst.append(i)
    d={}.fromkeys(lst,0)
    for i in lst:
        d[i]=i*i
    print(d)
squares(21)
###
print({i:i*i for i in range(1,21)})
'''
##11.Define a python function which can generate a dictionary where the keys are numbers between 1 and 20(both included) and the values are square of keys.The function should just print the keys only.

'''
lst=[]
def squares(n):
    for i in range(1,21):
        lst.append(i)
    d={}.fromkeys(lst,0)
    for i in lst:
        d[i]=i*i
        k=d.keys()
    print(k)
squares(21)

###
k={i:i*i for i in range(1,21)}
d=k.keys()
print(d)
'''

##12.Define a python function which can generate and print a list where the values are square of the numbers between 1 and 20(both included).
'''
lst=[]
lst1=[]
def squares(n):
    for i in range(1,21):
        lst.append(i)
    d={}.fromkeys(lst,0)
    for i in lst:
        d[i]=i*i
    for key,val in d.items():
        lst1.append([key,val])
    print(lst1)
squares(21)

'''
##13.Define a python function which can generate a list where the values are squares of numbers between 1to 20 (both included).Then the function needs to print the first five elements in the list.
'''
lst=[]
lst1=[]
def squares(n):
    lst=[]
    for i in range(1,21):
        lst.append(i)
        d={}.fromkeys(lst,0)
    for i in lst:
        d[i]=i*i
    for key,val in d.items():
        lst1.append([key,val])
        d1=lst1[:5]
    print(d1)
squares(21)
'''

#14.with the given tuple(1,2,3,4,5,6,7,8,9,10),write a program to print the first half values in one line and last half values in one line
'''
lst=[]
t=(1,2,3,4,5,6,7,8,9,10)
t1=t[:5]
t2=t[5:]
print(t1,'\n',t2)
'''

#15.Write a Python program to generate and print another tuple whose values are even numbers in the given tuple
'''
t1=[]
tup=(1,2,3,4,5,6,7,8,9,10)
for t in tup:
    if (t%2==0):
        t1.append(t)
print(t1)
    
'''
##16.write a program which accepts string a string as input to print 'Yes' if the string 'yes' or 'YES' or 'Yes',otherwise print 'NO'
'''
st=input('Enter any String:')
if st.upper()=='YES':
    print('YES')
else:
    print('NO')
'''
##17.WAP which can map() to make a list whose elements are squares of elements
'''
lst=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda i:i*i,lst)))

'''
##18.write a program which can filter() to make list whose elements are even Number between 1 to 20(Both Included)
'''

lst=[]
for i in range(1,21):
    lst.append(i)
print(list(filter(lambda i:i%2==0,lst)))


'''
##19.write a program which can map() to make list whose elements are square of Numbers between 1 to 20(Both Included)
'''
lst=[]
for i in range(1,21):
    lst.append(i)
print(list(map(lambda i:i*i,lst)))

'''




