#verify Mobile Number
'''
import re
mobile=input('Enter Any Mobile Number:')
m=re.fullmatch('[6-9]\d{9}',mobile)
if m==None:
    print('invalid Mobile Number')
else:
    print('valid Mobile Number')
'''
#verify PAN Number
'''
import re
PAN=input('Enter Any PAN Number:')
m=re.fullmatch('[A-Z]{5}\d{4}[A-Z]{1}',PAN)
if m==None:
    print('invalid PAN Number')
else:
    print('valid PAN Number')
'''
#verify Vehicle registration Number ##AP 31 CG 7277,HR26DQ5551,OR04 E 2900
'''
import re
Reg=input('Enter Any Reg Number:')
m=re.fullmatch('[A-Z]{2}[\s]?\d{2}[\s]?[A-Z]{1,2}[\s]?\d{4}',Reg)
if m==None:
    print('invalid Reg Number')
else:
    print('valid Reg Number')
'''
#write a pattern to verify email id  ##manjushanamathoti78@gmail.com
'''
import re
mail=input('Enter any mail id:')
m=re.fullmatch('[A-Za-z]{1,}[\w]+@[a-z]{5}[.][a-z]{2,3}',mail)
if m==None:
    print('Invalid id')
else:
    print('valid id')
'''
#write a pattern is fetch all company names from above data

data='This is Harish and I am working in TCS Company,recently i resigned from wipro company. I want join Infosys company next year'
import re

print([i.replace(' Company','') for i in (re.findall('[A-Za-z]{1,} Company',data))])



##from RFfile.txt
'''
#1.write a pattern to fetch all employees names from the file?

import re
m = open('RFfile.txt').read().replace('\n',',').split(',')
lst=[]
for i in m:
    if i in (re.findall('Mr[.][A-Za-z]{1,}',i)):
        lst.append(i)++20
print(lst)



#2.Write a pattern to fetch all mobile numbers

import re
m = open('RFfile.txt').read().replace('\n',',').split(',')
lst=[]
for i in m:
    if i in (re.findall('[6-9]\d{9}',i)):
        lst.append(i)
print(lst)


#3.fetch all company names

import re
lst = []
m = open('RFfile.txt').readlines()
for i in m:
    k = re.findall('[A-Za-z]{1,} Company',i)
    lst.append(k)
print(lst)



#4.fetch all email ids from the file

import re
m = open('RFfile.txt').read().replace('\n',',').split(',')
lst=[]
for i in m:
    if i in (re.findall('[A-Za-z]{1,}[\w]+@[a-z]{5}[.][a-z]{2,3}',i)):
        lst.append(i)
print(lst)

#5.fetch all vehicle reg numbers

import re
m = open('RFfile.txt').read().replace('\n',',').split(',')
lst=[]
for i in m:
    if i in (re.findall('[A-Z]{2}[\s]?\d{2}[\s]?[A-Z]{1,2}[\s]?\d{4}',i)):
        lst.append(i)
print(lst)
       

#6.fetch all PAN numbers


import re
m = open('RFfile.txt').read().replace('\n',',').split(',')
lst=[]
for i in m:
    if i in (re.findall('[A-Z]{5}\d{4}[A-Z]{1}',i)):
        lst.append(i)
print(lst)


#7.fetch all date-of-births from the file (1/1/1990)


import re
m = open('RFfile.txt').read().replace('\n',',').split(',')
lst=[]
for i in m:
    if i in (re.findall('\d{1,}[/]\d{1,}[/]\d{4}',i)):
        lst.append(i)
print(lst)



#8.fetch mobile number of Sai
import re
m = open('RFfile.txt').readlines()
for i in m:
    if 'Sai' in i:
        k=[i for i in re.findall('[6-9]\d{9}',i)]
        print(k)


#9.fetch company name of Nani
import re
m=open('RFfile.txt').readlines()
for i in m:
    if 'Nani' in i:
        k = [i.replace(' Company','') for i in re.findall('[a-zA-Z]{1,} Company',i)]
        print(k)

#10.fetch email id and PAN number of Rohan

import re
m=open('RFfile.txt').readlines()
for i in m:
    if 'Rohan' in i:
        k=[i for i in re.findall('[A-Za-z]{1,}[\w]+@[a-z]{5}[.][a-z]{2,3}',i)]+[i for i in re.findall('[A-Z]{5}\d{4}[A-Z]{1}',i)]
        print(k)

'''
#WAP to Display the company name of Sai
'''
import re
m=open('RFfile.txt').readlines()
for i in m:
    if 'Sai' in i:
        k = re.findall('[A-Za-z]{1,} Company',i)
        print(k)
'''       

## Write a pattern to display the date of birth of the employee of Wipro
'''
import re
m = open('RFfile.txt').readlines()
for i in m:
    if 'WIPRO' in i:
        k=re.findall('\d{1,}[/]\d{1,}[/]\d{4}',i)
        print(k)
'''

## Write a Pattern to display CTS company  employee Name
'''
import re
m = open('RFfile.txt').readlines()
for i in m:
    if 'CTS' in i:
        k=re.findall('Mr[.][A-za-z]{1,}',i)
        print(k)
'''
## WA pattern to display all employee Names and Mobile Numbers
'''
import re
m = open('RFfile.txt').read().replace('\n',',').split(',')
lst=[]
for i in m:
    if i in [i for i in re.findall('Mr[.][A-za-z]{1,}',i)]+[i for i in re.findall('[6-9]\d{9}',i)]:
        lst.append(i)
print(lst)
'''


##Write a  pattern to dispaly the employee name whose PAN number ends With D Character
'''
import re
m = open('RFfile.txt').readlines()
lst=[]
for i in m:
    k=re.findall('[A-Z]{5}\d{4}[A-Z]{1}',i)  #['---', '--']
    for j in k:
        if j.endswith('D'):
            lst.append(j)
print(lst)

'''


























'''

import re
m = open('RFfile.txt').readlines()
for i in m:
    print([re.findall('Mr[.][A-Za-z]{1,}',i)  for j in re.findall('[A-Z]{5}\d{4}[A-Z]' ,i.replace('\n','')) if j.endswith('D')])
'''


























