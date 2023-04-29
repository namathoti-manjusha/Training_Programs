#1. Write a program to generate all 5 divisibles from 10 to 50?
'''
for i in range(10,51):
    if i%5==0:
        print(i)
'''
#2. Write a program to generate all 10 divisibles from 100 to 10?
'''
for i in range(100,9,-1):
    if i%10==0:
        print(i)
'''
#3. Write a program to generate all odd numbers from 11 to 25?
'''
for i in range(11,26):
    if i%2!=0:
        print(i)
'''
#4. Write a program to generate all even numbers from -2 to -22?
'''
for i in range(-2,-23,-1):
    if i%2==0:
        print(i)
'''

#5. Write a program to generate all numbers from -3 to 5?
'''
for i in range(-3,6):
    print(i)
'''

#6. Write a program to generate all 7 divisibles from -21 to 21?
'''
for i in range(-21,21):
    if i%7==0:
        print(i)
'''

#7. Write a program to generate all numbers from 1 to 10 except 2 and 6?
'''
for i in range(1,11):
    if i%2!=0 and i%6!=0:
        print(i)

'''

#8. Write a program to generate all numbers from 15 to 1 except 3,6,9 and 12?
'''
for i in range(15,1,-1):
    if i%3!=0 and i%6!=0 and i%9!=0 and i%12!=0:
        print(i)
'''
#9. Write a program to generate all numbers from -2 to 2 except -1 and 1?
'''
for i in range(-2,3):
    if i!=-1 and i!=1:
        print(i)

'''


#10. Write a program to generate all 3 divisibles from 15 to -15 except even numbers?
'''
for i in range(15,-16,-1):
    if i%3==0 and i%2!=0:
        print(i)

'''

