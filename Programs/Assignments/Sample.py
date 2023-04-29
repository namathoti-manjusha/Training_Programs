#check Student failed or not in Exam
'''
name=input('Enter Your Name:')
marks=eval(input('Enter Your Marks:'))
if marks>=35:
    print('Hello {},You Passed in the Exam'.format(name))
else:
    print('Hello {},You Failed in the Exam'.format(name))
''' 
#check citizen eligible to vote or not
'''
name=input('Enter Your Name:')
age=eval(input('Enter your age:'))
if age>=18:
    print('Hello {}, you are eligible to Vote'.format(name))
else:
    print('Hello {}, you are not eligible to Vote'.format(name))
'''
#check your ID card
'''
name=input('Enter Your Name:')
ans=input('Do You Have ID Card?:')
ans=ans.lower()
if ans=='yes':
    print('Hello {}, You are allowed to Class'.format(name))
else:
    print('Hello {}, You are Not Allowed to Class'.format(name))
'''
# compare the numbers
'''
num=eval(input('Enter Any Number:'))
if num<100:
    print('{}is smaller than 100'.format(num))
elif num==100:
    print('{}is equal to 100'.format(num))
else:
    print('{} is Graterthan 100'.format(num))
'''
# compare two numbers
'''
a=input('enter first number:')
b=input('enter second number:')
if a>b:
    print('{} is graterthan {}'.format(a,b))
elif a<b:
    print('{} is less than {}'.format(a,b))
else:
    print('{} Equal to {}'.format(a,b))
'''
#print decimals of the number     
'''
n=eval(input('Enter Any Number:'))
ans='%.6f'%n
print('thengiven numer is up to 6 decimels',ans)
'''
#checking for eligible for vote
'''
age=eval(input('enter a person age:'))
if age>=18:
    print('you are eligible to take Vote')
  
n=eval(input('Enter any Number:'))
if n%2==0:
    print('it is even Number')
else:
    print('it is odd number')

n=eval(input('enter a number:'))
if n%7==0:
    print('it is divisible')
else:
    print('not divisible')
 
n=eval(input('enter a number:'))
if n%5==0:
    print('Hello')
else:
    print('Bye')
 '''

#electricity bill
''''
nu=int(input('Enter number of electric unit:'))
if nu<=100:
     amt=0
     print('You do not Pay Any Amount')
elif nu>100 and nu<=200:
     amt=(nu-100)*5
     print('The Amount to pay is {}'.format(amt))
elif nu>200:
     amt=500+(nu-200)*10
     print('The Amount to pay is {}'.format(amt))
'''
#last number divisible by 3
'''
n=eval(input('enter any number:'))
num=n%10
if num%3==0:
     print('last number is Divisible By 3')
else:
     print(' last number is not Divisible By 3')
'''


'''
a=eval(input('Enter any number:'))
def oddnum(n):
    if n%2==0:
        print('it is even number')
    else:
        print('it is odd number')
oddnum(a)
'''




