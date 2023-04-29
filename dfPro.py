'''
import pandas as pd 
import numpy as np
import pymysql

#connecting db1
connection1 = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='db1')
c1 = connection1.cursor()
c1.execute('select * from studentsdata')
data1 = c1.fetchall()
names=[]
marks=[]
locations=[]
for i in data1:
    names.append(i[1])
    marks.append(i[2])
    locations.append(i[3])
sData = {'Names':names, 'Marks':marks, 'Locations':locations}
sDatadf = pd.DataFrame(sData)
print(sDatadf)

#connecting db2
connection2 = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='db2')
c2 = connection2.cursor()
c2.execute('select * from studentsinfo')
data2 = c2.fetchall()
names = []
marks=[]
locations=[]
for i in data2:
    names.append(i[1])
    marks.append(i[2])
    locations.append(i[3])

sInfo = {'Names':names, 'Marks':marks, 'Locations':locations}
sInfodf = pd.DataFrame(sInfo)
print(sInfodf)

#Connecting text file
data3 = open('C:\\Users\\manju\\AppData\\Local\\Programs\\Python\\Python310\\studentsdetails.txt','r').readlines()
names=[]
marks=[]
locations=[]
for i in data3:
    x = i.split(',')
    names.append(x[1])
    marks.append(int(x[2]))
    locations.append(x[3].replace('\n',''))
sDetails = {'Names':names, 'Marks':marks, 'Locations':locations}
sDetailsdf = pd.DataFrame(sDetails)
print(sDetailsdf)


#Connecting Excel File
data4 = pd.read_excel('D:\\data\\studentschats.xlsx', sheet_name='sdata', usecols="B,C,D")
schartsdf=pd.DataFrame(data4)

mainData = pd.concat([sDatadf,sInfodf,sDetailsdf,schartsdf])
print(mainData)

#Loading Data into Destination Database(Dataware house)
connection3 = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='destDb')
c3 = connection3.cursor()
for index, data in mainData.iterrows():
    c3.execute('insert into students(names, marks, location) values(%s, %s, %s)',
              (data.Names, data.Marks, data.Locations)
              )
connection3.commit()
connection3.close()
'''


import matplotlib.pyplot as plt
years = [2017, 2018, 2019, 2020, 2021, 2022]
percentages = [70, 80, 75, 90, 99, 90]

font1 = {'family':'CASTELLAR', 'color':'red', 'size':20}
font2 = {'family':'Berlin Sans FB', 'color':'blue', 'size':15}

plt.plot(years, percentages, marker="o", linestyle = 'solid', linewidth='2')
plt.xlabel('Years', fontdict=font2)
plt.ylabel('Percentages', fontdict=font2)
plt.title('Year wise Percentages', fontdict = font1)
plt.grid(color='red',linestyle = 'dashed',linewidth='0.5')
plt.show()


#Write a program to create a plot about 'Subject wise marks' by using matplotlib?



















































