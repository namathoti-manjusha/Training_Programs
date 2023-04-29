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

#4. getting data from database
import pymysql
connection = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='python7amdb')

c = connection.cursor()

c.execute('select * from empdata;')

data = c.fetchall()

for i in data:
    name = i[0]
    salary = i[1]
    e = Empdata(name, salary)
    e.display()
    print()

'''


