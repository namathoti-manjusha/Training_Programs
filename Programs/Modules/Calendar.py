
##day_name

import calendar as c
print([i for i in c.day_name])

#WAP all The Days Which Starts With T Character
'''
import calendar as c
print([i for i in c.day_name if i[0].startswith('T')])
'''
#WAP to Display all the days which Contain i Character 
'''
import calendar as c
print([i for i in c.day_name if 'i'in i])
'''

#WAP display All The Days Which Contain 'u' as 2nd Character
'''
import calendar as c
print([i for i in c.day_name if i[1]=='u'])
'''
#WAP to Reverse Each day
'''
import calendar
print([i[::-1] for i in c.day_name])
'''
#WAP to display all the Names Except 'day'?
'''
import calendar as c
print([i.replace('day','') for i in c.day_name])
###
print([i[0:-3] for i in c.day_name])
'''
#WAP to Display the Day name as per user Requirement
'''
n=eval(input('Enter any month Number:'))

lst=[]
import calendar
for i in calendar.day_name:
    lst.append(i)
for i in lst:
    k=lst.index(i)
    if n==k:
        print('You Have Choosen',i)
    elif n<0 or n>7:
        print("You Entered Wrong Number")
        break
'''
##month_name
'''
import calendar as c
for i in c.month_name:
    print(i)
'''
##WAP to display Shortest Month Name
'''
import calendar as c
print([i for i in c.month_name if len(i)==min([len(i) for i in c.month_name if i!=''])])

'''

#WAP to Display the Month name as per user Requirement
'''
n=eval(input('Enter any month Number:'))

lst=[]
import calendar
for i in calendar.month_name:
    lst.append(i)
for i in lst:
    k=lst.index(i)
    if n==k:
        print('You Have Choosen',i)
    elif n<=0 or n>12:
        print("You Entered Wrong Number")
        break
'''
##month Abbrivation
'''
import calendar as c
for i in c.month_abbr:
    print(i)

'''
#leap year():
'''
import calendar as c
print(c.isleap(2006))
'''
#leapdays()
'''
import calendar as c
print(c.leapdays(2000,2006))
'''
#calendar
'''
import calendar as c
print(c.calendar(2025))
'''

















