# 1.Write a program to fetch all even numbers from list?
'''
lst = [10,11,13,14,9,8] #[10, 14, 8]
lst1=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
print(lst1)
##comprension

print([i for i in lst if i%2==0])
'''
#2.Write a program to fetch all string values from list? #['a', 'b']
'''
lst = [10,'a',True,'b',False] #['a', 'b']
lst1=[]
for i in lst:
    if type(i)==str:
        lst1.append(i)
print(lst1)

##comprention

print([i for i in lst if type(i)==str])
'''
#3.Write a program to fetch all 5 divisibles from list?
'''
lst = [12,15,27,20,5] #[15,20,5]
lst1=[]
for i in lst:
    if i%5==0:
        lst1.append(i)
print(lst1)
##comprention

print([i for i in lst if i%5==0])
'''
#4.Write a program to count total number of int values in the list
'''
lst = [10,'a',20,True,30,'b',40] #4
count=0
for i in lst:
    if type(i)==int:
        count=count+1
print(count)
'''
#5.Write a program to count total number of characters in the string(including space)?.
'''
st = 'Python language' #15
count=0
for i in st:
    if len(i):
        count=count+1
print(count)
'''
#6.Write a program to count total number of words in the string.
'''
st = 'python narayana tech house hyd' #5
st1=st.split(' ')
count=0
for i in st1:
    count=count+1
print(count)
'''
#7.Write a program to fetch all vowels from the string?
'''
st = 'Python language' #['o','a','u','a','e']
v='aeiou'
lst=[]
for i in st:
    if i in v:
        lst.append(i)
print(lst)
 ## comprention

print([i for i in st if i in v])
'''
#8.Write a program to count total number of vowels
'''
st = 'python narayana' #5
v='aeiou'
count=0
for i in st:
    if i in v:
        count=count+1
print(count)
'''
#9.Write a program to count total number of characters in the string(excluding space)?
'''
st = 'python is a simple language' #23
count=0
for i in st:
    if i!=' ':
        count=count+1
print(count)
'''
#10.Write a program to count total number of consonants in the string?
'''
st = 'python language' #9
v='aeiou'
count=0
for i in st:
    if i not in v:
        count=count+1
print(count)
'''
#11.Write a program to fetch all words which starts with vowel from given string?
'''
st = 'Python is simple and easy language' #['is', 'and', 'easy']
st1=st.split(' ')
v='aeiou'
lst=[]
for i in st1:
    if i[0] in v:
        lst.append(i)
print(lst)
##comprention

print([i for i in st.split(' ') if i[0] in v])
'''
#12. Write a program to fetch all words which ends with consonent in the given string?
'''
st = 'Python is simple and easy language' #['Python', 'is','and', 'easy']
st1=st.split(' ')
v='aeiou'
lst=[]
for i in st1:
    if i[-1] not in v:
        lst.append(i)
print(lst)
##comprention

print([i for i in st.split(' ') if i[-1] not in v])
'''
#13. Write a program to fetch all words which 'a' two or more then two times?
'''
st = 'Python is simple and easy language' #['language']

st1=st.split(' ')
lst=[]
for i in st1:
    if i.count('a')>=2:
        lst.append(i)
print(lst)
##comprention

print([i for i in st.split(' ') if i.count('a')>=2])
'''
#14. Write a program to count number of characters of each word in the string?
'''
st = 'Python is simple and easy language' #[6,2,6,3,4,8]
st1=st.split(' ')
lst=[]
for i in st1:
        lst.append(len(i))
print(lst)
##comprention

print([len(i) for i in st.split(' ')])
'''
#15. Write a program to fetch the first and last character from each word in the string?
'''
st = 'Python is simple and easy language' #['Pn', 'is', 'se', 'ad', 'ey', 'le']
st1=st.split(' ')
lst=[]
for i in st1:
    lst.append(i[0]+i[-1])
print(lst)
##comprention

print([i[0]+i[-1] for i in st.split(' ')])
'''
#16. Write a program to fetch all words which contains 'a' character in the string?
'''
st = 'Python is simple and easy language' #['and', 'easy', 'language']
st1=st.split(' ')
lst=[]
for i in st1:
    if i.count('a'):
        lst.append(i)
print(lst)
##comprention

print([i for i in st.split(' ') if i.count('a')])
'''
#17. Write a program to fetch all words which does not contain 'e' character in string?
'''
st = 'Python is simple and easy language' #['Python', 'is', 'and']
st1=st.split(' ')
lst=[]
for i in st1:
    if 'e' not in i:
        lst.append(i)
print(lst)
##comprention

print([i for i in st.split(' ') if 'e' not in i])
'''
#18. Write a program to fetch all words which contains only 4 or less than 4 characters?
'''
st = 'Python is simple and easy language' #['is', 'and', 'easy']
st1=st.split(' ')
lst=[]
for i in st1:
    if len(i)<=4:
        lst.append(i)
print(lst)
##compretion

print([i for i in st.split(' ') if len(i)<=4])
'''
#19. Write a program to fetch all words which contain odd number of characters in the string?
'''
st = 'Python is simple and easy language' #['and']
st1=st.split(' ')
lst=[]
for i in st1:
    if len(i)%2!=0:
        lst.append(i)
print(lst)
##compretion

print([i for i in st.split(' ') if len(i)%2!=0])
'''
#20. Write a program to fetch all words which starts and ends with vowel in the string?
'''
st = 'Python is number one language' #['one']
st1=st.split(' ')
v='aeiou'
lst=[]
for i in st1:
    if i[0] and i[-1] in v:
        lst.append(i)
print(lst)
##compretion

print([i for i in st.split(' ') if i[0] and i[-1] in v])
'''
#21. Write a program to fetch all palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam', 'dad', 'eye', 'malayalam']
lst=[]
for i in names:
    if i==i[::-1]:
        lst.append(i)
print(lst)
##comprention

print([i for i in names if i==i[::-1]])
'''
#22. Write a program to fetch all non palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['python','language']
lst=[]
for i in names:
    if i!=i[::-1]:
        lst.append(i)
print(lst)
##comprention

print([i for i in names if i!=i[::-1]])
'''
#23.Write a program to fetch all palindrom words which starts with 'm' character?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #['madam', 'malayalam']
lst=[]
for i in names:
    if i==i[::-1] and i[0]=='m':
        lst.append(i)
print(lst)
##comprention

print([i for i in names if i==i[::-1] and i[0]=='m'])
'''
#24. Write a program to fetch all palindrom words which more then 3 characters?
'''
names = ['madam', 'python','dad','language','eye','malayalam'] #[''madam','malayalam']
lst=[]
for i in names:
    if i==i[::-1] and len(i)>3:
        lst.append(i)
print(lst)
##comprention

print([i for i in names if i==i[::-1] and len(i)>3])
'''
#25.Write a program to longest palindrom word?

names = ['madam', 'python','dad','language','eye','malayalam'] #['malayalam']
lst=[]
'''
for i in names:
    if i==i[::-1]:
        lst.append(i)
for i in lst:
    if len(i) == max([len(i) for i in lst]):
        print(i)

##comprention
print(max([i for i in names if i==i[::-1]]))
'''

