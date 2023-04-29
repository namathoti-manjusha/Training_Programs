#lambda function
'''

x=lambda a,b:a+b
print(x(12,8))
'''
#highest
'''
def highest(a,b):
    lst1=[]
    if a>b:
        print(a)
    else:
        print(b)
highest(20,30)

#By using filter()

print(list(lambda a,b:a if a>b else b))
'''
##=====FILTER()======

##1.write a function to fetch only even numbers
'''
lst=[2,3,5,6,8]
#By using Def
def filteringEvens(lst):
     lst1=[]
     for i in lst:
          if i%2==0:
               lst1.append(i)
     print(lst1)
filteringEvens(lst)

#By using filter()

print(list(filter(lambda i:i%2==0,lst)))
'''

#2.Fetch all words which contain 4 characters
'''
#By using Def
lst=['nani','sai','syam','kholi','koti']
def fourchar(lst):
    lst1=[]
    for i in lst:
        if len(i)==4:
            lst1.append(i)
    print(lst1)
fourchar(lst)

#By using filter

print(list(lambda i:len(i)==4,lst))
'''
#3.fetch all words  which starts with k
'''
#By using Def
lst=['nani','sai','syam','kholi','koti']
def startk(lst):
    lst1=[]
    for i in lst:
        if i.startswith('k'):
            lst1.append(i)
    print(lst1)
startk(lst)

#By using filter()

print(list(lambda i:i.startswith('k'),lst))
'''
#4.fetch all words which contain n char 2 or morethen 2 times
'''
#By using Def

lst=['nani','sai','syam','kholi','koti']
def nchar(lst):
    lst1=[]
    for i in lst:
        if i.count('n')==2:
            lst1.append(i)
    print(lst1)
nchar(lst)

#By using filter()

print(list(filter(lambda i:i.count('n')==2,lst)))
'''
#fetch all words which contain o character
'''
#By using Def

lst=['nani','sai','syam','kholi','koti']
def ochar(lst):
    lst1=[]
    for i in lst:
        if 'o' in i:
            lst1.append(i)
    print(lst1)
ochar(lst)

#By using filter()

print(list(filter(lambda i:'o' in i,lst)))
'''
#fetch all words which contain not contain a character

'''
#By using Def

lst=['nani','sai','syam','kholi','koti']
def notconta(lst):
    lst1=[]
    for i in lst:
        if 'a' not in i:
            lst1.append(i)
    print(lst1)
notconta(lst)

#By using filter()

print(list(filter(lambda i:'a' not in i,lst)))
'''

##======MAP()========








