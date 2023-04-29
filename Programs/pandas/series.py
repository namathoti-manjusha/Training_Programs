#creating a series by using list or tuple

import pandas as pd
names=['sai','dhoni','kohli','sachin']
num=(10,20,30,40)
s1=pd.Series(data=names,index=num)
print(s1)


#creating series by using set
'''
import pandas as pd
names=['sai','dhoni','satya','kohli','sachin']
k=list(names)
num=(10,20,30,40,50)
s1=pd.Series(data=names,index=num)
print(s1)
'''
#creating set by using dict
'''
import pandas as pd
emps={'name':'sai','salary':90000,'comp':'WIPRO','loc':'Hyd'}
ks=emps.keys()
vs=emps.values()
k=pd.Series(data=ks)
v=pd.Series(data=vs)
print(k)
print(v)

'''

#Creating Series By Using arange()
'''
import pandas as pd
import numpy as np
x=np.arange(3,10,2)
s1=pd.Series(data=x)
print(s1)

'''

#Creating Series By Using File Data
'''
import pandas as pd
x=open('C:/Users/manju/AppData/Local/Programs/Python/Python310/Programs/myfile.txt').readlines()[0].replace('\n','').split(',')
n=(10,20,30,40,10)
d=pd.Series(x,n)
print(d)

'''
#