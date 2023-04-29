##WAP a function to find a highest number of 2 given numbers by user
'''
a=eval(input('Enter first Number:'))
b=eval(input('Enter second Number:'))
def highestoftwo(n1,n2):
    if n1>n2:
        print('{} is grater than {}'.format(n1,n2))
    else:
        print('{} is grater than {}'.format(n2,n1))
highestoftwo(a,b)
'''

##WAP to check wheather by user is given even or odd number
'''
a=eval(input('Enter Any Number:'))
def evenorodd(n):
    if n%2==0:
        print('{} is Even Number'.format(n))
    else:
        print('{} is Odd Number'.format(n))
evenorodd(a)

'''

#count total number of vowels
'''
st='python developer'
def countvowels(st):
    v='aeiou'
    count=0
    for i in st:
        if i in v:
            count=count+1
    print(count)
countvowels(st)
'''
#count total number of special characters
'''
import string
st='Ab@#c_&D'
def splchar(n):
    count=0
    for i in n:
        if i in string.punctuation:
            count=count+1
    print(count)
splchar(st)
'''
#count total number of upper case
'''
import string
st='pyTHON nArAyANA'
def countofuppercase(n):
    count=0
    for i in n:
        if i in string.ascii_uppercase:
            count=count+1
    print(count)
countofuppercase(st)
'''
##Write a function to fetch all 10 divisibles from list
'''
lst=[15,20,25,30,35,40]
def filtertens(lst):
    lst1=[]
    for i in lst:
        if i%10==0:
            lst1.append(i)
    print(lst1)
filtertens(lst)
'''
#filter all words with contain 'y' character
'''
st='python narayana tech house hyd'
st1=st.split()
st2=[]
for i in st1:
    if 'y' in i:
        st2.append(i)
print(st2)
'''
#filter all which starts with consonent
'''
st='python narayana tech house hyd'
st1=st.split()
v='aeiou'
st2=[]
for i in st1:
    if i[0] not in v and i[-1] in v:
        st2.append(i)
print(st2)
'''
                

#passinfo
'''
m=input('Enter Your Name:')
m1=eval(input('Enter your marks:'))
def passinfo(n,n1):
    if n<30:
        print('{} you are failed with {} marks'.format(n1,n))
    elif n>=30 and n<=50:
        print('{} you are Passed with {} marks'.format(n1,n))
    else:
        print('Invalid marks')
passinfo(m1,m)
'''




        
