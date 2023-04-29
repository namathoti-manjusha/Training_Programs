##system-Defined Exceptions

#developement time exception(DTE)
'''
a=10
b=20
c=a+b: ##invalid syntax
    print(c)
 '''
'''
a=10
b=20
c=a+b
print(c)
'''
#Runtime Exception
'''
a=10
b=0
c=a/b
print(c)  #ZerodivisionError
'''
'''
a=10
b=0
try:
    c=a/b
    print(c)
except:
    print('Error Raised')
'''
#
'''
a=eval(input('Enter First value:'))
b=eval(input('Enter Second Value:'))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print('please Enter Non-Zero value')
except NameError:
    print('please use Defined Names only')
except TypeError:
    print('please use proper types only')
except:
    print('Error Raised')
'''
##Finally block
'''
a=eval(input('Enter First value:'))
b=eval(input('Enter Second Value:'))
try:
    c=a/b
    print(c)
except:
    print('Error Raised')
else:
    print('Try Executed')
finally:
    print('Thank you')
'''
##user-Defined Exceptions
'''
class LessThenZeroMarksError(Exception):
    pass
class MoreThenHundredMarksError(Exception):
    pass
marks=eval(input('Enter Your Marks:'))
if marks>0 and marks<35:
    print('you are Failed')
elif marks>=35 and marks<=100:
    print('you are Passed')
elif marks<0:
    raise LessThenZeroMarksError('You Have Given Lessthen 0 marks')
else:
    raise MoreThenHundredMarksError('You Have Given Morethen 100 marks')

'''
####
'''
class PositiveEvenError(Exception):
    pass
class PositiveOddError(Exception):
    pass
class NegativeEvenError(Exception):
    pass
class NegativeOddError(Exception):
    pass
marks=eval(input('Enter Your Marks:'))
if marks>0 and marks%2==0:
    raise PositiveEvenError('You Entered Positive Even Number')
elif marks>0 and marks%2!=0:
    raise PositiveOddError('You Entered Positive odd Number')
elif marks<0 and marks%2==0:
    raise NegativeEvenError('You Entered Negative Even Number')
elif marks<0 and marks%2!=0:
    raise NegativeOddError('You Entered Negative odd Number')
else:
    print('You Entered Zero Value')
'''
























    
