# write a program to display a table as per user requirement
'''
n=eval(input('Enter Any Number:'))
i=1
while i<11:
    print(n,'*',i,'=',n*i)
    i=i+1
'''

#write a program to display the odd numbers from 1 to 15
'''
i=1
while i%2!=0 and i<16:
    print(i)
    i=i+2
##
i=1
while i<16:
    if i%2!=0:
        print(i)
        i=i+2
        
###
i=1
while i<16:
    if i%2==1:
        print(i)
    i=i+1
'''


#simple login operation
'''
while True:
        user=input('Enter username:')
        if user!='manjusha':
                print('{} is invalid username enter try again...'.format(user))
                continue
        else:
                pwd=input('Enter Password:')
                if pwd!='123@sha':
                         print('*'*len(pwd),'invalid password try again...')
                         continue
                else:
                        print('Welcome to NTH Homepge')
                break
        break
'''







    
