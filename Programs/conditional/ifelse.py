#Write a program to check student passed or not in the Exam
'''
name=input('Enter Your name:')
marks=eval(input('Enter Your Marks:'))
if marks>=35:
    print('Hello')
    print('You are Passed in the Exam')
    print('congrats')
else: 
    print('Hello')
    print('You Failed in the Exam')

'''
#using Format function
'''
name=input('Enter Your name:')
marks=eval(input('Enter Your Marks:'))
if marks>=35:
    print('Hello {},You got {} marks.'.format(name,marks))
    print('You are Passed in the Exam')
    print('congrats')
else: 
    print('Hello {},You got {}marks.'.format(name,marks))
    print('You Failed in the Exam')
'''
#To find Highest number of two given numbers by user
'''
n1=eval(input('Enter First Number:'))
n2=eval(input('Enter Second Number:'))
if n1>n2:
    print('{}is Highest number between {} and {}'.format(n1,n1,n2))
else:
    print('{} is highest number between {} and{}'.format(n2,n1,n2))
'''
#wheather the user is given Even or Odd number
'''
n=eval(input('Enter Any Number:'))
if n%2==0:
    print(n,'is even number')
else:
    print(n,'is odd number')
'''
#using format function
'''
n=eval(input('Enter Any Number:'))
if n%2==0:
    print('{} is even number'.format(n))
else:
    print('{} is odd number'.format(n))
'''
#Given character is Vowel are not
'''
char=input('Enter Any Character:')
vowel=['a','e','i','o','u','A','E','I','O','U']
if char in vowel:
    print('{} is vowel'.format(char))
else:
    print('{} is Consonent'.format(char))
'''    




