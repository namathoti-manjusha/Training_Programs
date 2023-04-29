##1.WAP to find the Highest values from given list(without using predefined function)
'''
num=[3,4,96,20,38,5,100,99]
high=num[0]
for a in num:
    if a> high:
        high=a
print(high)

'''

##2.WAP to display the given number into characters
##Enter any Number=253
##Two hundred fifty three
'''
names={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Ninteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninty',100:'Hundred'}
num=eval(input('Enter a Number:'))
if num<=100:
    if num in names:
        k=names.get(num)
        print(num,"in words is ", k)
    else:
        b=num%10
        b=names.get(b)
        c=num // 10
        c=c*10
        c=names.get(c)
        result=c+b
        print(num, "in words is ",result)
else:
    print("Error! Enter A Number From 1 to 100")

'''

##3.WAP function indexnum(n,m)
# n is Occurance of element
# m is element
#eg:
##lst=[10,20,30,10,40,50,10,60]
##lst.indexnum(2,10)-----3
'''
lst=[10,20,30,10,40,50,10,60]
x=10
count=0
for i in lst:
    if i==x:
        count=count+1
print("{} has occured {} time".format(x,count))        
'''
#Assending order of list(2nd Highest number)
'''
lst=[10,100,60,70,50,30,5]

lst.sort()
print(lst[-1])
print(lst[-2])
print(lst[-3])

lst1 = []
while lst:
    small= lst[0]
    for x in lst:
        if x < small:
            small = x
    lst1.append(small)
    lst.remove(small)
print(lst1[-2])
print(lst1[-3])

'''
#Descending order of list(2nd Samallest Number)
'''
lst=[10,100,60,70,50,30,5]

lst.sort(reverse=True)
print(lst[-1])
print(lst[-2])
print(lst[-3])
'''

'''
lst1 = []
while lst:
    high= lst[0]
    for x in lst:
        if x >high:
            high = x
    lst1.append(high)
    lst.remove(high)
print(lst1[-2])
print(lst1[-3])
'''
##swap first and last element
'''
lst1=[]
lst=[10,23,54,96,5,95,76]
for i in lst:
    lst1.append(i)
    temp=lst1[0]
    lst1[0]=lst1[lst-1]
    lst1[lst-1]=temp
print(lst1)
'''

##Print Calender
'''
import calendar
year=eval(input('Enter the year:'))
month=eval(input('Enter the month number:'))
print(calendar.month(year,month))
'''
#Python program to Print Natural number 1 to N
'''
n=eval(input('Enter any number:'))
for i in range(1,n+1):
    print(i)
'''

#Python program for Leap Year
'''
yr=eval(input('Enter the year:'))
if  (( yr%400 == 0)or (( yr%4 == 0 ) and ( yr%100 != 0))):
    print('{} is leap year'.format(yr))
else:
    print('{} is not leap year'.format(yr))
'''

#Python program to find Odd or Even
'''
n=eval(input('Enter first number:'))
if n%2==0:
    print('{} is even number'.format(n))
else:
    print('{} is odd number'.format(n))
'''
#Python program to print Even Numbers from 1 to 100
'''
n=eval(input('Enter first number:'))
for i in range(1,n):
    if i%2==0:
        print('{}'.format(i))
'''
#Python program to print Odd Numbers from 1 to 100
#Python Program to Print Negative Numbers in a Range
#Python Program to Print Positive Numbers in a Range

###
'''
n=input('Enter Any Day:')
if n=='Monday' and 'Tuesday' and 'Wednesday' and 'Thursday':
    print('You can Wear School Uniform')
elif n=='Friday':
    print('You can wear Civil dress')
elif n=='Saturday':
    print('You can Wear White and White')
elif n=='Sunday':
    print('Its Your Choice')
'''
'''
n=input('Enter Your Name:')
g=input('Enter Your Gender:')
if g=='Male':
    k=eval(input('Enter Your Age:'))
    if k>=30:
        print('Please Marry me')
else:
    k=eval(input('Enter Your Age:'))
    if k>=25:
        print('Marry me')
'''

'''
student=input('which Language are you Learning:')
gender=input('Enter your Gender:')
if student=='Python':
    print(gender,'is learning Updated Skills')
else:
    print(gender,'have to learn Python')

'''
'''
n=eval(input('Enter Your Age:'))
if n>=0 and n<=5:
    print('Your Are An Infant')
elif n>=6 and n<=16:
    print('You Are School Going Kid')
elif n>=17 and n<=22:
    print('You Are College Going Kid')
elif n>=23 and n<=30:
    print('You Need to Settle in Life And Get Marry')
elif n>=31 and n<=45:
    print('You Need to Work And Earn Money')
elif n>=46 and n<=60:
    print('You need to Do Business')
elif n>=61 and n<=70:
    print('You need to take retirement from your work')
else:
    print('you no need to take rest')

'''
