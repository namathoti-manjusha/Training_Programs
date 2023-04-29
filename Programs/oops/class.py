'''
class Studentsdata:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def displayGrade(self):
        print('{} got {} marks'.format(self.name,self.marks))
name='Nani'
marks=600
s1 = Studentsdata(name,marks)
s1.displayGrade()
'''

#using class Method
'''
class Studentsdata: 
    def __init__(self,name,percentage):
        self.name=name
        self.percentage=percentage
    def displayGrade(self):
        print('{} got {} percentage'.format(self.name,round(self.percentage)))
    @classmethod
    def findingpercentage(cls,name,marks):
        return cls(name,(marks|600)*100)
name='Nani'
marks=500
s1=Studentsdata.findingpercentage(name,marks)
s1.displayGrade()
name='Rohit'
marks=600
s2=Studentsdata.findingpercentage(name,marks)
s2.displayGrade()
'''

#Static Method
'''
class Calculations:
    @staticmethod
    def Addition(a,b):
        c=a+b
        print(c)
    @staticmethod
    def Subtraction(a,b):
        c=a-b
        print(c)
Calculations().Addition(10,20)
Calculations().Subtraction(20,10)
'''

#Dataabstraction
'''
class EmpData:
    name='Sai'
    __Salary=30000
    __Age=25
    comp='TCS'
    def working(self):
        print('Emp is working in IT')
e1=EmpData()
print(e1.name)
print(e1.comp)
print(e1.__Salary)
print(e1.__Age)
'''
#by using Private Attributes in Method
'''
class EmpData:
    name='Sai'
    __Salary=30000
    __Age=25
    comp='TCS'
    def working(self):
        print('Name:',EmpData.name)
        print('Salary:',EmpData.__Salary)
        print('Age:',EmpData.__Age)
        print('comp:',EmpData.comp)
e1=EmpData()
e1.working()
'''

#Encapsulation
'''
class studentsData:
    standard='Fifth'
    subject='English'
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('student name:',self.name)
        print('marks:',self.marks)
        print('standard:',studentsData.standard)
        print('subject:',studentsData.subject)
n=eval(input('How many Students are there?:'))
for i in range(n):
    name=input('Enter Your Name:')
    marks=eval(input('Enter your Marks:'))
    s=studentsData(name,marks)
    s.display()
    print()
 '''  
        
####
'''
class studentsData:
    standard='Fifth'
    subject='English'
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('{} got {}'.format(self.name,self.marks))
name='Manju'
marks=80
s1=studentsData(name,marks)
s1.display()
name='Nitya'
marks=90
s2=studentsData(name,marks)
s2.display()
'''





















    






































