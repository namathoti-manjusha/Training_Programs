#check the student passed or not passed inthe Exam
'''
marks=eval(input('Enter Your Marks:'))
if marks>=0 and marks<=35:
    print('Failed')
elif marks>=35 and marks<=50: 
    print('Grade C')
elif marks>=50 and marks<=60:
    print('Grade B')
elif marks>=60 and marks<=75:
    print('Grade A')
elif marks>=75 and marks<=100:
    print('distintion')
else:
    print('Invalid marks')
'''
#given number is even or odd with sign
'''
n=eval(input('Enter Any Number:'))
if n>0 and n%2==0:
    print('{} is positive and even number.'.format(n))
elif n>0 and n%2!=0:
    print('{} is positive and odd number.'.format(n))
elif n<0 and n%2==0:
    print('{} is negative and even number.'.format(n))
elif n<0 and n%2!=0:
    print('{} is negative and odd number.'.format(n))
elif n==0:
    print('it is Zero')
else:
    print('invalid number')
'''
#course learning
'''
course=input('Which Course Are You Learning?:')
course=course.lower()
if course=='python':
    print('It is a Simple and Easy Course')
elif course=='java':
    print('It is a Lenghty Course')
elif course=='.Net':
    print('It is also Simple Course')
elif course in ['devops','ai','aws','azure']:
    print('it is for Exp Candidates')
else:
    print('Learn Proper Course')
'''
#given number is even or odd with sign
'''  
n=eval(input('Enter Any Number:'))
if n>0 and n%2==0:
    print('it is positive and even number' )
elif n>0 and n%2!=0:
    print('it is positive and odd number')
elif n<0 and n%2==0:
    print('it is negative and even number')
elif n<0 and n%2!=0:
    print('it is negative and odd number')
else:
    print('invalid number')

'''

