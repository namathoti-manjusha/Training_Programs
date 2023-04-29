# Write a program to display the below patterns
##pattern 1
'''
print(5 * '*')
'''
#pattern 2
'''
print(5 * '*''\n')
'''
#pattern 3(Square Pattern)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(0,n):
    for j in range(0,n):
        print("* ",end="")
    print()
'''

##Pattern 4(Triangle)

n=eval(input('Enter Number of Rows:'))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,i+2):
        print("* ",end="")
    print()


##Pattern 5(Down Triangle)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n,i,-1):
        print("* ",end="")
    print()  
'''


#pattern 6(Left triangle)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()

'''
##pattern 7(Right Triangle)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(1,i+2):
        print("*",end=" ")
    print()
'''
    
##Pattern 8(Left Down Triangle)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
'''

##Pattern 9(Right Down triangle)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n,i,-1):
        print("*",end=" ")
    print()
'''

##pattern 10(Pyramid)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()

'''
##Pattern 11(Down Pyramid)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(n-i)-1):
        print('*', end='')
    print()
'''

##pattern 12(Diamond)
'''
n=eval(input('Enter Number of Rows:'))
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(n-i)-1):
        print('*', end='')
    print()
'''







