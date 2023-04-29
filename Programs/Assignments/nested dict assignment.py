movies = {
    'actors':{
              'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remmunaration':100, 'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1,  'mStatus':'single','sRate':'35%'},
              'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remmunaration':50,'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},
              'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1},'remmunaration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'50%'},
              'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3},'remmunaration':70, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},
              'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5},'remmunaration':50, 'hits':{'industry':2, 'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%'},
             },
    'actress':{
               'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1},'remmunaration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':33, 'height':5.5,  'mStatus':'single','sRate':'40%'},
               'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},'remmunaration':12, 'hits':{'industry':0, 'super':4,'flops':2}, 'age':26, 'height':5.6,  'mStatus':'single','sRate':'30%'},
               'saipallavi':{'knownAs':'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},'remmunaration':8, 'hits':{'industry':0, 'super':3,'flops':0}, 'age':30, 'height':5.2,'mStatus':'married','sRate':'60%'},
               'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remmunaration':15, 'hits':{'industry':3, 'super':7,'flops':4}, 'age':35, 'height':5.5,  'mStatus':'single','sRate':'70%'},
               'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remmunaration':12, 'hits':{'industry':1, 'super':6,'flops':8}, 'age':37, 'height':5.5, 'mStatus':'married','sRate':'60%'},
              }
          }


#fetch all actors Nick names
'''
lst=[]
for i in movies:
    k=movies[i]
    for j in k:
        k1=movies[i][j]['knownAs']
        lst.append(k1)
print(lst)
'''   
#1. Write a program to display all actors names
'''
for i in movies:
    if i=='actors':
        for j in movies[i]:
            print(j)
'''
#2. Write a program to display all actress names
'''
for i in movies:
    if i=='actress':
        for j in movies[i]:
            print(j)
'''            
#3. Who is Darling?

'''
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Darling':
            print(j)
'''        

#4. What are the total number of Nandi Awards won by actors?
'''
lst=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            lst.append(movies[i][j]['awards']['nandi'])        
print(sum(lst))
''' 

#5. What is the name of Prince?
'''
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Prince':
            print(j)
'''        
    
#6. What are the total number of awards own by Ram Charan?

'''
for i in movies:
    for j in movies[i]:
        if j=='ramcharan':
            k=movies[i][j]['awards']       
            print(sum(k.values()))
'''
#7. Which actor won more number of Nandi Awards?
'''
lst=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            k=movies[i][j]['awards']['nandi']
            lst.append(k)
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if movies[i][j]['awards']['nandi']==max(lst):
                print(j)
            
'''

#8. What is the success rate of Prince?
'''
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Prince':
            print(movies[i][j]['sRate'],j)
'''
#9. Which actor and actress has more number of Hits?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(sum(list(movies[i][j]['hits'].values())))
for i in movies:
    for j in movies[i]:
        if sum(list(movies[i][j]['hits'].values())) == max(lst):
                print(j)

'''
#10. Who is Milky Beauty?
'''
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Milky Beauty':
            print(j)
'''
#11. What is the nick name of Rashmika?
'''
for i in movies:
    for j in movies[i]:
        if j=='rashmika':
            print(movies[i][j]['knownAs'])
'''       
#12. What are actress names who did not win at least one Nandi Award?
'''
for i in movies:
    for j in movies[i]:
        k1=movies[i][j]['awards']['nandi']
        if k1==0:
            print(j)

'''
#13. What are the total number of SIIMA awards won by both actors and actress?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['awards']['siima'])
print(sum(lst))
'''
#14. What are the actor and actress names who has more success rate?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if (movies[i][j]['sRate'])==max(lst):
            print(j)
'''
#15. What is the age of actor who has more super hit movies?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['hits']['super'])
for i in movies:
    for j in movies[i]:
        if (movies[i][j]['hits']['super'])==max(lst):
            print(movies[i][j]['age'])
        
'''        
#16. What is the actress name who is married?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            k=movies[i][j]['mStatus']
            if k=='married':
                print(j)
'''
#17. Who is the tallest actress?
''' lst=[] for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['height'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['height'])==max(lst):
                print(j)
        
'''
#18. Who is the Youngest actor and actress?
'''
lst=[]
lst1=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            k=movies[i][j]['age']
            lst.append(k)
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if movies[i][j]['age']==min(lst):
                print(j)
for i in movies:
    if i=='actress':
        for j in movies[i]:
            k=movies[i][j]['age']
            lst1.append(k)
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['age']==min(lst1):
                print(j)
'''
#19. Who are unmarried actress?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            k=movies[i][j]['mStatus']
            if k=='single':
                print(j)
 ''' 
#20. Who is smallest actress?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['age'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['age']==min(lst):
                print(j)
'''
#21. Which actress has more Flops?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['hits']['flops'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['hits']['flops']==max(lst):
                print(j)
'''
#22. What is the age of butter milky beauty?
'''
for i in movies:
    for j in movies[i]:
        k=movies[i][j]['knownAs']
        if k=='Butter Milky Beauty':
            print(movies[i][j]['age'])
'''
#23. What are the total number of flops of all actress?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['hits']['flops'])
print(sum(lst))        

'''
#24. What are the ages of Sam and Kaj?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        k=movies[i][j]['knownAs']
        if k=='Sam' or k=='Kaj':
           print(movies[i][j]['age'])
'''  
#25. Which actress own highest total number of Awards?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(sum(list(movies[i][j]['awards'].values())))
            
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (sum(list(movies[i][j]['awards'].values())))==max(lst):
                print(j)

            
'''        
#26. Who is tallest Actor and Actress?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['height'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['height'])==max(lst):
                print(j)

'''
#27. What are the total number of Industry hits of who has more Success Rate?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if (movies[i][j]['sRate'])==max(lst):
            k=movies[i][j]['hits']['industry']
            print(j,k)
'''
#28. What is the success rate of youngest actress?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['age'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['age'])==min(lst):
                k=movies[i][j]['sRate']
                print(j,k)

'''      
#29. Who is youngest married actress?
'''
lst=[]
lst1=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            k=(movies[i][j]['mStatus'])
            if k=='married':
                lst.append(movies[i][j]['age'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if(movies[i][j]['age'])==min(lst):
                    print(j)
            
'''       

#30. Who is oldest unmarried actor?
'''
lst=[]
lst1=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            k=(movies[i][j]['mStatus'])
            if k=='single':
                lst.append(movies[i][j]['age'])
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if(movies[i][j]['age'])==max(lst):
                    print(j)
            
 '''      
    
#31. Who are the high successful actor and actress?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if(movies[i][j]['sRate'])==max(lst) :
            print(j)
        
'''
#32. Totally How many unmarried actors and actress are acting in movies?
'''
lst=[]
count=0
for i in movies:
    for j in movies[i]:
        k=movies[i][j]['mStatus']
        if k=='single':
            lst.append(k)
            count=count+1
print(count)
'''
#33. Which actress is having more industry hit movies?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['hits']['industry'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['hits']['industry'])==max(lst):
                print(j)
            
'''
#34. Which actress does not have atleast one industry hit also?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            k=movies[i][j]['hits']['industry']
            if k!=0:
                print(j)

'''
#35. What are the total number of industry and super hits of tallest actress?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['height'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['height'])==max(lst):
                k=movies[i][j]['hits']['industry']+movies[i][j]['hits']['super']
                print(j,k)

'''
#36. Which actress is having lengthiest nick name?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['knownAs'])
max1=len(lst[0])
temp=lst[0]
for word in lst:
    if(len(word)>max1):
        max1=len(word)
        temp=word
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if(movies[i][j]['knownAs'])==temp:
                print(j)

'''
#37. Who are the youngest unmarried actor and actress?
'''
lst=[]
for i in movies:
        for j in movies[i]:
            lst.append(movies[i][j]['age'])
for i in movies:
    for j in movies[i]:
        if (movies[i][j]['age'])==min(lst):
            k=movies[i][j]['mStatus']
            if k=='single':
                print(j)

'''
#38. What are the total number of Industry hits and Super Hits of the actress who got more SIIMA awards?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['awards']['siima'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['awards']['siima'])==max(lst):
                k=movies[i][j]['hits']['industry']+movies[i][j]['hits']['super']
                print(j,k)

'''
#39.What are the ages of Darling and Milky Beauty?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        k=movies[i][j]['knownAs']
        if k in'Darling'or k in 'Milky Beauty':
            k1=movies[i][j]['age']
            print(j,k1)

'''
#40. What are names of actors whose nick name contains star?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        k=movies[i][j]['knownAs']
        if 'Star' in k:
            print(j)

'''
#41. What is the total remuneration of all actors?
'''
lst=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            lst.append(movies[i][j]['remmunaration'])
print(sum(lst))
'''       
#42. What is the remuneration of an actor who has more flops?
'''
lst=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            lst.append(movies[i][j]['hits']['flops'])
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if (movies[i][j]['hits']['flops'])==max(lst):
                k=movies[i][j]['remmunaration']
                print(j,k)

'''
#43. What is the highest remuneration of an unmarried actress?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['remmunaration'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['remmunaration'])==max(lst):
                k=movies[i][j]['mStatus']
                if k=='single':
                    print(j)
'''                
#44. What are the names of actor and actress who has more remuneration?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['remmunaration'])
for i in movies:
    for j in movies[i]:
        if (movies[i][j]['remmunaration'])==max(lst):
           print(j)
'''
#45. What is the remuneration of high successful Actress?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['sRate'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['sRate'])==max(lst):
                k=movies[i][j]['remmunaration']
                print(j)
'''
#46. What is the remuneration of actress who has more industry hits?
'''
lst=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            lst.append(movies[i][j]['hits']['industry'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if (movies[i][j]['hits']['industry'])==max(lst):
                k=movies[i][j]['remmunaration']
                print(j)

'''
#47. What are the ages of an actors whose remuneration is more then 90 crores?
'''
lst=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            k=movies[i][j]['remmunaration']
            if k >= 90:
                print(j)

'''
#48. What are the total number of industry hits of both Prince and Butter Milky Beauty?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        k=movies[i][j]['knownAs']
        if k=='Prince'or k=='Butter Milky Beauty':
            lst.append(movies[i][j]['remmunaration'])
            k1=sum(lst)
            print(k1,j)
'''
#49. What is the age of Laughing Queen?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        k=movies[i][j]['knownAs']
        if k=='Laughing Queen':
            k1=movies[i][j]['age']
            print(j,k1)
'''
#50. What are the total number of awards won by an actor who has less successful rate?
'''
lst=[]
lst1=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if (movies[i][j]['sRate'])==min(lst):
            k=(list(movies[i][j]['awards'].values()))
            k1=sum(k)
            print(k1,j)
    
'''
