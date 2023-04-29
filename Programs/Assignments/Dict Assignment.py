players = {
        'player1':{'name':'Sachin','matches':{'test':200,'odi':463},'scores':{'test':248,'odi':200},'wickets':{'test':46,'odi':154},'age':49,'shirt':10, 'role':'top-order','loc':'Bombay'},
        'player2':{'name':'Kohli','matches':{'test':102,'odi':262},'scores':{'test':254,'odi':183},'wickets':{'test':0,'odi':4},'age':33,'shirt':18,'role':'top-order','loc':'Delhi'},
        'player3':{'name':'Rohit','matches':{'test':44,'odi':231},'scores':{'test':212,'odi':264},'wickets':{'test':2,'odi':8},'age':35,'shirt':45,'role':'opening','loc':'Nagpur'},
        'player4':{'name':'Sehwag','matches':{'test':104,'odi':251},'scores':{'test':319,'odi':219},'wickets':{'test':40,'odi':96},'age':43,'shirt':44,'role':'opening','loc':'Delhi'},
        'player5':{'name':'Zaheer Khan','matches':{'test':92,'odi':200},'scores':{'test':75,'odi':34},'wickets':{'test':311,'odi':282},'age':43,'shirt':41,'role':'Bowler','loc':'Bombay'},
        'player6':{'name':'Dhoni','matches':{'test':90,'odi':350},'scores':{'test':224,'odi':183},'wickets':{'test':0, 'odi':1},'age':41,'shirt':7,'role':'keeper','loc':'Ranchi'}
        }

#1.To display Player names
'''
for i in players:
    print(players[i]['name'])
    
'''

##2. Write a program to display ages of players?
'''
for i in players:
    print(players[i]['age'])
'''

##3.Write a program to display the youngest player name?
'''
lst=[]
for i in players:
    d=players[i]['age'],players[i]['name']
    lst.append(d)
    for i in lst:
        b=min(lst)
print(b)
'''   
##4.Write a program to display player name who played more test matches?
'''
lst=[]
for i in players:
    d=(players[i]['matches']['test'],players[i]['name'])
    lst.append(d)
    for i in lst:
        t=max(lst)
print(t)
 '''       

##5. Write a program to display player name and number of test matches who has taken 0 wickets in test matches?

'''
for id in players:
    d=players[i]['wickets']['test']
    if  d==0:
        print(players[i]['name'],players[i]['matches']['test'])
'''

##6. Write a program to display player name who has taken more wickets in ODI?
'''
lst=[]
for i in players:
    d=players[i]['wickets']['odi'],players[i]['name']
    lst.append(d)
    t=max(lst)
print(t)
'''

##7. Write a program to display the players’ names that played highest number of ODI matches?
'''
lst=[]
for i in players:
    d=players[i]['matches']['odi'],players[i]['name']
    lst.append(d)
    t=max(lst)
print(t)
'''
##8. Write a program to display the player name that has highest total score of both test and ODIs?
'''
lst=[]
for i in players:
    d=players[i]['scores']['test']+players[i]['scores']['odi'],players[i]['name']
    lst.append(d)
    t=max(lst)
print(t)
 '''  
##9.Write a program to display total number of matches of Kohli?
'''
for i in players:
    d=players[i]['name']
    if d=='Kohli':
        print(players[i]['matches']['test']+players[i]['matches']['odi'])
'''

##10. Write a program to display the age of Rohit?
'''
for i in players:
    k=players[i]['name']
    if k=='Rohit':
        print('Rohit age is',players[i]['age'])
'''
##11.Write a program to display the total ODI scores of all players?
'''
lst1=[]
for id in players:
    d=players[i]['scores']['odi']
    lst1.append(d)
print(sum(lst1))
'''
##12.Write a program to display total number of wickets of Zaheer Khan?
'''
for id in players:
    d=players[i]['name']
    if d=='Zaheer Khan':
        print(players[i]['wickets']['test']+players[i]['wickets']['odi'])
'''
##13. Write a program to display all opening batsman names?
'''
lst1=[]
for i in players:
    d=players[i]['role']
    if d=='opening':
        print(players[i]['name'])
'''
#14. Write a program to display player name that shirt number is highest number?
'''
lst=[]
for i in players:
    d=players[i]['shirt'],players[i]['name']
    lst.append(d)
    t=max(lst)
print(t)

'''
#15. Write a program to display all Bombay players?
'''
lst1=[]
for i in players:
    d=players[i]['loc']
    if d=='Bombay':
        print(players[i]['name'])
'''

#16. Write a program to display the shirt number of Sachin?
'''
lst=[]
for i in players:
    d=players[id]['name']
    if d=='Sachin':
        print(players[i]['shirt'])
'''


#17. Write a program to display the role of Rohit in match?
'''
lst=[]
for i in players:
    d=players[i]['name']
    if d=='Sachin':
        print(players[i]['shirt'])

'''


#18. What is the location of the player whose shirt number is 45?
'''
lst=[]
for i in players:
    d=players[i]['shirt']
    if d==45:
        print(players[i]['loc'])

'''
#19. Write a program to display all wickets of a player whose role is bowler?

''''
lst=[]
for i in players:
    d=players[i]['role']
    if d=='Bowler':
        print(players[i]['wickets'])
'''

#20. Write a program to count total number opening players?

'''
count=0
for i in players:
    d=players[i]['role']
    if d=='opening':
        count=count+1
print(count)
'''

#21. Write a program to display Bombay opening player name?
'''
lst=[]
for i in players:
    d=players[i]['role']
    d1=players[i]['loc']
    if d=='opening' or d1=='Bombay':
        print(players[i]['name'])
'''
#22. Write a program to display the roles of Delhi players?
'''
lst=[]
for i in players:
    d=players[i]['loc']
    if d=='Delhi':
        print(players[i]['role'])
'''

#23. Write a program to display the role and location of Rohit?

'''
for id in players:
    d=players[i]['name']
    if d=='Rohit':
        print(players[i]['role'],'\n',players[i]['loc'])

'''
#24. Write a program to display total score of Bombay top-order player?
'''
lst=[]
for i in players:
    d=players[i]['role']
    d1=players[i]['loc']
    if d=='top-order' and d1=='Bombay':
        k=players[i]['scores']['test']+players[i]['scores']['odi']
        lst.append(k)
print(lst)
'''
#25. Write a program to display all unique roles of players?
'''
lst=[]
for i in players:
    d=players[i]['role']
    lst.append(d)       
print(list(set(lst)))
 '''       
        
#26 Write a program to display shirt number of Delhi top-order player?
'''

for id in players:
    d=players[i]['role']
    d1=players[i]['loc']
    if d=='top-order' and d1=='Delhi':
        print(players[i]['shirt'])
'''

#27. Write a program to display keeper name?
'''

for id in players:
    d=players[i]['role']
    if d=='keeper':
        print(players[i]['name'])

'''
        
#28. Write a program to display the shirt number of Dhoni?
'''

for id in players:
    d=players[i]['name']
    if d=='Dhoni':
        print(players[i]['shirt'])

'''

#29. Write a program to display players names who played less than 100 test matches?
'''
lst=[]
for id in players:
    d=players[i]['matches']['test']
    if d<=100:
        print(players[i]['name'])
'''

#30. Write a program to display total wickets of Ranchi player?
'''
for id in players:
    d=players[i]['loc']
    if d=='Ranchi':
        print(players[i]['wickets']['test']+players[i]['wickets']['odi'])
       
'''

employees ={
        'emp1':{'name':'Sai','salary':20000,'company':['TCS','Capegimini','Infosys'],'hTown':'Hyd'},
        'emp2':{'name':'Nani','salary':30000,'company':['Wipro','NTH'],'hTown':'Bangalore'},
        'emp3':{'name':'Satya','salary':40000,'company':['NTH','Infosys','CTS'],'hTown':'Chennai'},
        'emp4':{'name':'Rohit','salary':25000,'company':['Infosys','TCS','Defteam'],'hTown':'Pune'},
        'emp5':{'name':'Mohan','salary':22000,'company':['NTH','HCL','DeepCompute'],'hTown':'Hyd'},
        'emp6':{'name':'Sanjay','salary':45000,'company':['Wipro','Infosys','Defteam'],'hTown':'Mumbai'}
}
'''
for i in employees:
     k=employees[i]['company']
     if 'Infosys'not in k:
         print(employees[i]['name'])
         
         
'''
'''
lst=[]
for i in employees:
    k=employees[i]['name']
    if k=='Rohit':
       l=employees[i]['company']
       print(l[-1])
   
'''
'''
for i in employees:
    k=employees[i]['company']
    if 'DeepCompute' in k:
        print(employees[i]['name'])

'''
'''
for i in employees:
    k=employees[i]['company']
    k1=len(k)
    if k1==2:
        print(employees[i]['name'])
'''
