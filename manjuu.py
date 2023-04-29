'''
def sum(n):
    if n==0:
        return 0
    else:
        return(n%10)+(sum(int(n/10)))
print(sum(123456))

def sum1(n):
    if n==0:
        return 0
    else:
        return n+sum1(n-1)
print(sum1(6))
'''

st='12345'
