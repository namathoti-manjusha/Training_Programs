
'''
class myclass:
    name='Sai'
    loc='Hyd'
    com='NTH'
    def working(self):
        print('He is working since 10 years')
    def learning(self):
        print('He is learning since Childhood')
m=myclass()
print(m.name)
print(m.loc)
print(m.com)
m.working()
m.learning()
'''

#Getting data while object is creating
'''
class Empdata:
    company='TCS'
    location='Hyd'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('Emp Name:',self.name)
        print('salay:',self.salary)
        print('company:',Empdata.company)
        print('location:',Empdata.location)
emp1=Empdata('Sai',20000)
emp1.display()
emp2=Empdata('Nani',30000)
emp2.display()
emp3=Empdata('Satya',40000)
emp3.display()
'''

#Getting data from user
'''
class Empdata:
    company='TCS'
    location='Hyd'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('Emp Name:',self.name)
        print('salay:',self.salary)
        print('company:',Empdata.company)
        print('location:',Empdata.location)
n=eval(input('How many emps are there?:'))
for i in range(n):
    name=input('enter your Name:')
    salary=eval(input('Enter your Salary:'))
    e=Empdata(name,salary)
    e.display()
    print()
'''

# Getting Dta from file
'''
class Empdata:
    company='TCS'
    location='Hyd'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('Emp Name:',self.name)
        print('salay:',self.salary)
        print('company:',Empdata.company)
        print('location:',Empdata.location)
data=open('emps.txt').readlines()
for i in data:
    X=i.split(',')
    name=X[0]
    salary=X[1]
    e=Empdata(name,salary)
    e.display()
    print()

    
'''
'''
class Empdata:
    company='TCS'
    location='Hyd'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('Emp Name:',self.name)
        print('salay:',self.salary)
        print('company:',Empdata.company)
        print('location:',Empdata.location)
        
data=open('file.txt').readlines()
for i in data:
    X=i.split(',')
    name=X[0]
    salary=X[1]
    e=Empdata(name,salary)
    e.display()
    print()
'''
#Getting data from database

class Empdata:
    company='TCS'
    location='Hyd'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('Emp Name:',self.name)
        print('salay:',self.salary)
        print('company:',Empdata.company)
        print('location:',Empdata.location)
import pymysql
connection = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='manjudb')
c = connection.cursor()
c.execute('select * from emp;')
data = c.fetchmany(5)
# fetch one row ---> cursor.fetchone()
# fetch limited rows ----> cursor.fetchmany(size)
# fetch all rows -----> cursor.fetchall()
for i in data:
    name = i[0]
    salary = i[1]
    e = Empdata(name, salary)
    e.display()
    print()




























