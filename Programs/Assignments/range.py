# 1.Write a program to count total number of characters
'''

st='Python Narayana Tech House@Hyd'
count=0
for i in st:
    if i!=' ':
        count=count+1
print(count)
'''

#by using range()
'''
st='Python Narayana Tech House@Hyd'
count=0
for i in range(0,len(st)):
    if st[i]!=' ':
        count=count+1
print(count)

'''

# 2.counting total number of words
 ##by using range()
'''

st='Python Narayana Tech House@Hyd'
st1=st.split()
import string
count=0
for i in range(0,len(st1)):
    if st1[i]!=string.punctuation:
        count=count+1
print(count)
'''
'''

st='Python Narayana Tech House@Hyd'
st1=st.split()
count=0
for i in st1:
        count=count+1
print(count)

'''

# 3.counting uppercase characters
'''

st='Python Narayana Tech House@Hyd'
st1=st.split()
count=0
for i in st1:
    count=count+1
    if i[0].isupper():
        count1=count+1
print(count1)


## by using Import

st='Python Narayana Tech House@Hyd'
import string
count=0
for i in st:
    if i in string.ascii_uppercase:
        count=count+1
print(count)
'''

# 4.counting total number of vowels
'''

st='Python Narayana Tech House@Hyd'
v='aeiou'
count=0
for i in st:
    if i in v:
        count=count+1
print(count)

'''
# 5.counting special characters
'''
st='Python Narayana Tech House@Hyd'
import string
count=0
for i in st:
    if i in string.punctuation:
        count=count+1
print(count)

'''

# 6.counting occurance of each vowel
'''

st='Python Narayana Tech House@Hyd'
v='aeiou'
d={}.fromkeys(v,0)
for i in st:
    if i in d:
        d[i]=d[i]+1
print(d)

'''

# 7.counting occurance of each character
'''

st='Python Narayana Tech House@Hyd'
d={}.fromkeys(st,0)
for i in st:
    if i in d:
        d[i]=d[i]+1
print(d)

'''
# 8.words which contain even number of characters
'''

st='Python indu manju Narayana Tech House@Hyd'
st1=st.split()
lst=[]
for i in st1:
    if len(i)%2==0:
        lst.append(i)
print(lst)
'''

#by using comprention
'''
print([i for i in st1 if len(i)%2==0])
 '''

# 9.words which starts with vowel
 #without vowel
'''
st='Python Narayana Tech House@Hyd'
st1=st.split()
v='aeiou'
lst=[]
for i in st1:
    if i[0] in v.upper():
        lst.append(i)
print(lst)
 '''
#by using comprention
'''
print([i for i in st1 if i[0] in v.upper()])
'''
##with vowel
'''
st='Python Narayana Indu Tech House@Hyd'
st1=st.split()
v='AEIOU'
lst=[]
for i in st1:
    if i[0] in v:
        lst.append(i)
print(lst)
'''

#by using comprention
'''
print([i for i in st1 if i[0] in v.upper()])

'''
# 10.word which starts and ends with consonent
'''
st='Python Narayana Tech House@Hyd'
st1=st.split()
v='AEIOU'
lst=[]
for i in st1:
    if i[0] not in v.lower() and i[-1] not in v.lower():
        lst.append(i)
print(lst)
'''

#by using comprention
'''
print([i for i in st1 if i[0] not in v.lower() and i[-1] not in v.lower()])
'''

# 11.word which starts and ends with vowel
 #without vowel
'''
st='Python Narayana Tech House@Hyd'
st1=st.split()
v='aeiou'
lst=[]
for i in st1:
    if i[0] in v.upper() and i[-1] in v:
        lst.append(i)
print(lst)
'''
#by using comprention
'''
print([i for i in st1 if i[0] in v.upper() and i[-1] in v])
'''
    
#with vowel
'''
st='Python Narayana Indu Tech House@Hyd'
st1=st.split()
v='aeiou'
lst=[]
for i in st1:
    if i[0] in v.upper() and i[-1] in v:
        lst.append(i)
print(lst)
'''

#by using comprention
'''
print([i for i in st1 if i[0] in v.upper() and i[-1] in v])
'''

# 12.starts with vowel and ends with consonent
#without vowel
'''
st='Python Narayana Tech House@Hyd'
st1=st.split()
v='aeiou'
lst=[]
for i in st1:
    if i[0] in v.upper() and i[-1] not in v:
        lst.append(i)
print(lst)
'''

 ##with vowel
'''
st='Python Narayana Amar Tech House@Hyd'
st1=st.split()
v='aeiou'
lst=[]
for i in st1:
    if i[0] in v.upper() and i[-1] not in v:
        lst.append(i)
print(lst)
'''
#by using comprention
'''
print([i for i in st1 if i[0] in v.upper() and i[-1] not in v])

'''

# 13.starts with consonent and end with vowel
'''
st='Python Narayana Tech House@Hyd'
st1=st.split()
v='aeiou'
lst=[]
for i in st1:
    if i[0] not in v.upper() and i[-1] in v:
        lst.append(i)
print(lst)
'''
#by using comprention
'''
print([i for i in st1 if i[0] not in v.upper() and i[-1] in v])

 '''

# 15.fetching all vowels from given string
'''
st='Python Narayana Tech House@Hyd'
v='aeiou'
print([i for i in st if i in v])
'''

# 16.fetching all consonent from the given string
'''
st='Python Narayana Tech House@Hyd'
v='aeiou'
print([i for i in st if i.lower() not in v and i!=' '])
'''

# 17.fetching first character from each word
'''
st='Python Narayana Tech House@Hyd'
st1=st.split()
print([i[0] for i in st1])

###
st='Python Narayana Tech House@Hyd'
print([i[0] for i in st.split()])
'''

# 18.fetching last character from each word
'''
st='Python Narayana Tech House@Hyd'
print([i[-1] for i in st.split()])
'''

# 19.fetching first and last character from each word
'''
st='Python Narayana Tech House@Hyd'
print([(i[0],i[-1]) for i in st.split()])
'''

# 20.fetching all special characters
'''
st='Python Narayana Tech House@Hyd'
import string
print([i for i in st if i in string.punctuation])
'''




























