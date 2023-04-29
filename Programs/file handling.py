#Write data into the file
'''
file=open('newfile.txt','w')
file.write('Good Morning Students')
file.close()
'''
#Read all data from the file
'''
print(open('newfile.txt').read())
'''
#Append values into the file

file=open('newfile.txt','a')
file.write('NTH')
file.close()

#write multiple lines data
'''
file=open('newfile.txt','a')
file.write('\nNarayana Tech House\n+91-9010607010\nnarayanatechhouse@gmail.com\nAmmerpet\nHyd')
file.close()

'''
#write read the first line from the file
'''
print(open('myfile.txt').readlines()[0])
'''
#write read 3rd line from the file
'''
print(open('myfile.txt').readlines()[2])
'''
#write count total num of char the file(including and \n)
'''
print(len(open('myfile.txt').read()))
'''









#count total number of words in the file
'''
print(len(open('myfile.txt').read().replace('\n',',').split(',')))
'''
#Fetch first word from each line
'''
f=open('myfile.txt')
s=f.readlines()
for i in s:
    print(i.split(',')[0])
f.close()
'''
##
'''
lst=[]
a=open('myfile.txt')
b=a.readlines()
for i in b:
    c=i.split(',')
    d=c[0]
    lst.append(d)
print(lst)
'''

#fetch all words which starts with a charcter
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    if 'A' in i:
        lst.append(i)
print(lst)
'''
#fetch all words contain 4 charcters
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    if len(i)==4:
        lst.append(i)
print(lst)
'''         
#fetch all words ends with a character
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    if 'a' in i[-1]:
        lst.append(i)
print(lst)
'''
#fetch all uppercase words
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    if i.isupper():
        lst.append(i)
print(lst)
'''
#count all vowels in file
'''
data=open('myfile.txt').read()
v='aeiou'
d={}.fromkeys(v,0)
for i in data:
    if i in d:
        d[i]=d[i]+1
print(d)
'''

#To fetch character of first line
'''
print(open('myfile.txt').readline()[0])
'''
#to fetch first character of each word
'''
print([i[0]for i in open('myfile.txt').read().replace('/n',',').split(',')])
'''
#To fetch second word from third line
'''
print(open('myfile.txt').readlines()[2].split(',')[1])
'''
#fetch all words starts with vowel and ends with consonent
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
v='aeiou'
for i in b:
    if i[0].lower() in v and i[-1] not in v:
        lst.append(i)
print(lst)
'''
#fetch all words which are not starting with vowel
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
v='aeiou'
for i in b:
    if i[0].lower() not in v:
        lst.append(i)
print(lst)
'''
#count number of occurances of Sai
'''
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
count=0
for i in b:
    if i=='Sai':
        count=count+1
print(count)
'''
#fetch every alternative word from the file======
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    if b.index(i)%2 == 0 and i not in lst:
        lst.append(i)
print(lst)

'''
#find length of each word
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    lst.append(len(i))
print(lst)


print([[i,len(i)] for i in (open('myfile.txt').read().replace('\n',',').split(','))])
'''
#To fetch first word and last word from each line
'''
lst=[]
a=open('myfile.txt')
b=a.readlines()
for i in b:
    c=i.split(',')
    d=c[0],c[-1].replace('\n','')
    lst.append(d)
print(lst)

##

a=open('myfile.txt')
b=a.readlines()
for i in b:
    c=i.split(',')
    print(c[0],c[-1])
'''

#To fetch last word from each line
'''
a=open('myfile.txt')
b=a.readlines()
for i in b:
    c=i.split(',')
    print(c[-1])

##
lst=[]    
a=open('myfile.txt')
b=a.readlines()
for i in b:
    c=i.split(',')
    d=c[-1]
    lst.append(d)
print(lst)
'''

#fetch All words which contain a character more than 2 times
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    if i.lower().count('a')>=2:
        lst.append(i)
print(lst)
##comprention
print([i for i in b if i.lower().count('a')>=2])
'''
#Fetch all words which contain odd number of characters
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    if len(i)%2!=0:
        lst.append(i)
print(lst)
'''
#To count all characters in the file
'''
f=open('myfile.txt')
s=f.read()
count=0
for i in s:
    if i!=',' and '\n':
        count=count+1
print(count)
'''
#To count all uppercase characters in the file

'''
a=open('myfile.txt')
b=a.read().replace('\n',',')
count=0
for i in b:
    if i.isupper():
        count=count+1       
print(count)
'''
#To fetch all lower case words
'''
lst=[]
a=open('myfile.txt')
b=a.read().replace('\n',',').split(',')
for i in b:
    if i.islower():
        lst.append(i)
print(lst)
'''
#fetch duplicate names
'''
lst=[]
data=open('myfile.txt').read().replace('\n',',').split(',')
for i in data:
    if data.count(i)>=2:
        lst.append(i)
print(list(set(lst)))
'''           
#fetch unique names(without set)
'''
lst=[]
data=open('myfile.txt').read().replace('\n',',').split(',')
for i in data:
    if data.count(i)==1:
        lst.append(i)
print(lst)
'''
## fetch unique names(with set)
'''
lst=[]
data=open('myfile.txt').read().replace('\n',',').split(',')
for i in data:
    if data.count(i)<2:
        lst.append(i)
print(list(lst))
'''












