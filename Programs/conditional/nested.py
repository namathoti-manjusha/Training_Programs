#check the given assignment written by student or not 
'''
ans=input('Did you write assignment-1?(yes/no):')
if ans=='yes':
    marks=eval(input('enter the marks:'))
    if marks>0 and marks<18:
        print('betterluck next time')
    elif marks>=18 and marks<30:
        print('ok good')
    elif marks>=30 and marks<=50:
        print('very Good')
    else:
        print('invalid marks')
elif ans=='no':
    print('you defnetly write next time' )
else:
    print('you tell yes or no only')
'''
#even or odd
'''
n=eval(input('enter any number:'))
if n>0:
    if n%2==0:
        print('{} is the positive and even number'.format(n))
    else:
        print('{} is the positive and odd number'.format(n))
elif n<0:
    if n%2==0:
        print('{} is the negative and even number'.format(n))
    else:
        print('{} is the negative and odd number'.format(n))
else:
    print('{} is Zero'.format(n))
'''
#mini project
#calculator

options='''
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.modulus
'''
print(10*'*',"NTH calculator",10*'*')
print(options)
option=eval(input('Enter Your Option:'))
if option>0 and option<=5:
    n1=eval(input('Enter First Number:'))
    n2=eval(input('Enter Second Number:'))
    if option==1:
        n=n1+n2
        print('The addition of {} and {} is {}'.format(n1,n2,n))
    elif option==2:
        n=n1-n2
        print('The Subtraction of {} and {} is {}'.format(n1,n2,n))
    elif option==3:
        n=n1*n2
        print('The Multiplication of {} and {} is {}'.format(n1,n2,n))
    elif option==4:
        n=n1/n2
        print('The division of {} and {} is {}'.format(n1,n2,n))
    elif option==5:
        n=n1%n2
        print('The modulus of {} and {} is {}'.format(n1,n2,n))
else:
    print('Please give Valid Option,1 or 2 or 3 or 4 or 5 only')

