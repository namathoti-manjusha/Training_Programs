#Match
'''
import re
name=input('Enter Any Name:')
m=re.match('Python',name)
if m==None:
    print('Not matched')
else:
    print('Matched')
'''
    
# Full match
'''
import re
name=input('Enter Any Name:')
m=re.fullmatch('Python',name)
if m==None:
    print('Not Matched')
else:
    print('Matched')

'''    
# Search
'''
import re
name=input('Enter Any Name:')
m=re.search('Python',name)
if m==None:
    print('Not Matched')
else:
    print('Matched')
'''
#Find all
'''
import re
m=re.findall('\W','Na1@ to5%_ HX9*_')
print(m)
'''
# sub()
'''
import re
m=re.sub('a','_','Narayana')
print(m)
'''
#subn()
'''
import re
m=re.subn('a','_','Narayana')
print(m)
'''
#split()
'''
import re
m=re.split(' ','Narayana Tech House')
print(m)
'''











    
