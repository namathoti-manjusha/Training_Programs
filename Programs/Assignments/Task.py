#Task-1   Python Nested list
'''
# 1.How to add 40 in first sub-list?
lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
lst[2].insert(3,40)
print(lst)
##OUTPUT===[100, 200, [10, 20, 30, 40], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]

## 2.How to find number of elements in second sublist?
lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
print(len(lst[4]))
#OUTPUT=====5

##3.How to add X between 'a' and 'b'
lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
x=lst[6].insert(1,'x')
print(x)
#OUTPUT====[100, 200, [10, 20, 30, 40], 300, [1, 2, 3, 4, 5], 400, ['a', 'x', 'b', 'c'], 500]

##4.How to remove/delete item 5 from the list?
lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
x=lst[4].remove(5)
print(x)
#OUTPUT===[100, 200, [10, 20, 30, 40], 300, [1, 2, 3, 4], 400, ['a', 'x', 'b', 'c'], 500]

##5.How to delete 400 from the list
lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
x=lst.remove(400)
print(x)
#OUTPUT====[100, 200, [10, 20, 30, 40], 300, [1, 2, 3, 4], ['a', 'x', 'b', 'c'], 500]

##6.How to clear all elements from third sub-list?
lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
x=lst.pop(6)
print(x)
#OUTPUT====['a', 'b', 'c']

##7.How to replace 40 with new item 400?
lst=[100, 200, [10, 20, 30, 40], 300, [1, 2, 3, 4, 5], 400, ['a', 'x', 'b', 'c'], 500]
lst[2][3]=400
lst
#OUTPUT===[100, 200, [10, 20, 30, 400], 300, [1, 2, 3, 4, 5], 400, ['a', 'x', 'b', 'c'], 500]

##8.How to count number of 200s in the list
lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
x=lst.count(200)
print(x)
#OUTPUT=== 1

##9.How to delete 2nd sublist from the main list?

lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
x=lst.pop(4)
print(x)
#OUTPUT====[1, 2, 3, 4, 5]

##10.How to find the index number of third sublist
lst = [100, 200, [10, 20, 30], 300, [1, 2, 3, 4, 5], 400, ['a', 'b', 'c'], 500]
x=lst.index(['a','b','c'])
print(x)
#OUTPUT===6
'''

##Task-2  (Python Nested Dict)
'''
employees = {
    'employee1':{'Name':'Sai', 'Salary':30000, 'Location':'Hyd', 'Colleagues':['Anil','Swetha','Rohan'], 'Company':'TCS' },
	'employee2':{'Name':'Nani', 'Salary':40000, 'Location':'Bang', 'Colleagues':['Satya','Varun','Sunil'], 'Company':'Wipro' },
	'employee3':{'Name':'Pallavi', 'Salary':50000, 'Location':'Chennai', 'Colleagues':['Ram','Renu','Jai'], 'Company':'TCS' },
	'employee4':{'Name':'Rohit', 'Salary':25000, 'Location':'Hyd', 'Colleagues':['Srinu','Roshan','Kumar'], 'Company':'CTS' }
}
#1.display First Employee Name
print(employees['employee1']['Name'])
Sai

#2.what is the Location of Second Employee
print(employees['employee2']['Location'])
Bang

#3.What are the Names of 1st Employee Colleagues
print(employees['employee1']['Colleagues'])      
['Anil', 'Swetha', 'Rohan']

#4.Who is the 2nd Colleague of Third Employee
print(employees['employee3']['Colleagues'][1])      
Renu

#5.What is the Salary of 4th Employee
print(employees['employee4']['Salary'])      
25000

#6.How many coleagues are there for Second Employee
print(len(employees['employe2']['Colleagues']))
3

#7.How to display the Third employee Name and Salary
print(employees['employee3']['Name'],'Salary is',(employees['employee3']['Salary']))     
Pallavi Salary is 50000

#8.How to Display 2nd Employee Data
print(employees['employee2']['Name'],'is working in',(employees['employee2']['Company']),(employees['employee2']['Location']),'and getting',(employees['employee2']['Salary']),'salary')      
Nani is working in Wipro Bang and getting 40000 salary
'''

#Task-3
'''
# WAP Whether the user given string or not

st=eval(input("Enter Anything:"))
if type(st) is str:
    print('User Entered String')
else:
    print('User did not Enter String')
'''

#Task-4  (by using If condition)

#Write a Python Program to check Player Name in WTC Final 2021?
'''
players_names = ['Kohli', 'Rohit', 'Shubman ', 'Pujara', 'Rahane', 'Pant', 'Jadeja', 'Ashwin', 'Shami', 'Bumrah', 'Ishant', 'Siraj', 'Vihari', 'Saha', 'Umesh']
names=input('Enter Player Name:')
if names in players_names:
  print('yes,{} is playing WTC Final 2021'.format(names))
else:
  print('No,{} is not  playing WTC Final 2021'.format(names))
'''
    
# Task-5    by using elif statement
'''
##WAP To take name and age from person na display the following as per the age
age=eval(input('Enter Your Age:'))
if age>=1 and age<=5:
    print('Learn talking,walking,eting....')
elif age>=6 and age<16:
    print('Enjoy Your School Days')
elif age>=16 and age<22:
    print('College Days teaches Life style.')
elif age>=22 and age<30:
    print('Get Job and Settle Well And Good Package')
elif age>=30 and age<45:
    print('Family Responsibilities')
elif age>=45 and age<60:
    print('Plan for own Business')
elif age>=60 and age<80:
    print('Dont take more stress at this age')
elif age>=80 and age<=100:
    print('You are luckey person because you still Alive after 80')
else:
    print('please check your age, i think you entered wrong age.')
'''

#Task-6
'''
# WAP to find BMI
Height=eval(input('Enter your height in centimeters:'))
Weight=eval(input('Enter Your Weight in kgs:'))
meter=Height/100
BMI=Weight/(meter*meter)
print('BMI is {}'.format(BMI))
if BMI>=0 and BMI<18.5:
    print('Underweight.')
elif BMI>=18.5 and BMI<=24.9:
    print('Normal Weight.')
elif BMI>=25.0 and BMI<=29.9:
    print('Pre-Obesity.')
elif BMI>=30.0 and BMI<40.0:
    print('Obesity.')
else:
    print('Extremly Obesity.')
'''

#Task-7  (by using nested-if statement)
'''
##WAP To take away one number from user,that number must be in between 1 and 10
n=eval(input('Enter Any Number:'))
if n>=1 and n<=10:
    if n%2==0:
        print('You Have Entered Even Number.')
    else:
        print('You Have Entered Odd Number.')
else:
    print('Please enter Any Number Between 1 and 10')
'''

##Task-8


students = {
  'student1':{'Name':'Sai', 'Loc':'Hyd', 'Courses':'Full Stack', 'Fee': 3000},
  'student2':{'Name':'Nani', 'Loc':'Bang', 'Courses':'Full Stack', 'Fee': 3000},
  'student3':{'Name':'Satya', 'Loc':'Chennai', 'Courses':['Python','Django', 'Flask'], 'Fee': 3000},
  'student4':{'Name':'Renu', 'Loc':'Bang', 'Courses':['MSBI','PowerBI','SQL'], 'Fee': 4000},
  'student5':{'Name':'Ramya', 'Loc':'Hyd', 'Courses':['Python','MSBI','Full Stack'], 'Fee': 5000},
  }

##8.Display all Students names who are learning 'Python' Course?

lst=[]
lst1=[]
for i in students:
    if type(students[i]['Courses']) is list:
        if 'Python' in students[i]['Courses']:
            print(students[i]['Name'])
        

    
'''
#1.Display Student1 Data
print(students['student1'])

#2.Display Course name of Student2
print(students['student2']['Courses'])
'''

#3.Display Total number of courses of student4
'''
s=(students['student4']['Courses']) 
print(len(s))
'''
##4.Display all students names
'''
for i in students:
    s=students[i]['Name']
    print(s)
'''
##5. Display all Students names who is spending 5000 or above to learn course?

'''
for i in students:
    s=students[i]['Fee']
    if s>=5000:
        print(students[i]['Name'])
'''

##6.Display all courses which fee is 3000?
'''
for i in students:
    s=students[i]['Fee']
    if s==3000:
        print(students[i]['Courses'])
'''

##7.Display all unique locations?
'''
lst=[]
for i in students:
    s=students[i]['Loc']
    lst.append(s)
print(list(set(lst)))

'''




