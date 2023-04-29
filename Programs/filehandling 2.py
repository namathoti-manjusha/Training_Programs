#1.fetch all data from the file
'''
print(open('file.txt').read().split(','))

#2.read first line from the file
print(open('file.txt').readline().split(','))

#3.read last line from the file
print(open('file.txt').readlines()[-1])

#4.read third line from the file
print(open('file.txt').readlines()[1])

#5.count total number characters in the file
count=0
d=open('file.txt').read()
for i in d:
    c=i.split()
    count=count+1
print(count)

#6.count total number of comas in the file
count=0
d=open('file.txt').read()
for i in d:    
    if i==',':
        count=count+1
print(count)

#7.count total number of words in the first line

count=0
d=open('file.txt').readline()
c=d.split(',')
for i in c: 
    count=count+1
print(count)

#8.To count total number of lines in the file
print(len(open('file.txt').readlines()))


#9.count total numer of 'sai' name in the file

count=0
d=open('file.txt').readlines()
for i in d:
    c=i.replace('\n',',').split(',')
    for k in c:
        if k=='Satya':
            count=count+1
print(count)

              
#10.to fetch first word from each line
           
print([i.split(',')[0] for i in open('file.txt').readlines()])


#11.fetch lastword fro each line        

print([i.replace('\n','').split(',')[-1] for i in open('file.txt').readlines()])


#12.starts with 'a' character in the file

print([i for i in open('file.txt').read().replace('\n',',').split(',') if i[0].lower().startswith('a')])


#13.fetch all words which ends with Vowels

print([i for i in open('file.txt').read().replace('\n',',').split(',') if i[-1] in 'aeiou'])


#14.fetch all words has either 'a' or 'i' in the file
print([i for i in open('file.txt').read().replace('\n',',').split(',') if 'a' in i or 'i' in i])


#15.fetch all words which contains five characters in the file

print([i for i in open('file.txt').read().replace('\n',',').split(',') if len(i)==5])

#16.fetch all words which doesnot contain vowel except i in the file

print([i for i in open('file.txt').read().replace('\n',',').split(',') if 'i' in i and 'a' not in i.lower() and 'e' not in i and 'o' not in i and 'u' not in i ])

#17.fetch all words which ends with uppercase character

print([i for i in open('file.txt').read().replace('\n',',').split(',') if i[-1].isupper()])

#18.to count total number of characters in the file excluding comas

print(len([i for i in open('file.txt').read() if i!=',' and i!='\n']))

#19 count total number of words in the entire file

print(len([i for i in open('file.txt').read().replace('\n',',').split(',')]))

#20.Fech all even number words from every line

print([i for i in open('file.txt').read().replace('\n',',').split(',') if len(i)%2==0])

#21.fetch all words with endswith 'bha' in the file

print([i for i in open('file.txt').read().replace('\n',',').split(',') if i.endswith('bha')])

#22.WAP to display all TCS employees

print([i.replace('\n','').split(',')[1:] for i in open('file.txt').readlines()if 'TCS' in i.split(',') ])
'''
#23.WAP to display the company name of chinna employee
'''
print([i.replace('\n','').split(',') for i in open('file.txt').readlines() if 'Chinna' in i])
'''
#24.fetch the 2nd line 3rd line in the file
'''
print([i.replace('\n','').split(',') for i in open('file.txt').readlines()][2][1])
'''
#25.fetch first character from each word on 3rd line
'''
print([i[0]for i in [i for i in [i.replace('\n','').split(',') for i in open('file.txt').readlines()][2]]]) 

'''
    
#26.fetch first and last character of each word in the last line
'''
print([i[0]+i[-1] for i in [i for i in [i.replace('\n','').split(',') for i in open('file.txt').readlines()][-1]]])
'''
#27.fetch all characters (except 1st and last chars) of each word in second line
'''
print([i[1:-1] for i in[i for i in [i.replace('\n','').split(',') for i in open('file.txt').readlines()][1]]])
'''
#28.to count total 




