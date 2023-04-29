## Pickling
'''
import pickle
lst=['Sai','Nani','Python','Django','UI']
with open('pypickle.txt','wb') as file:
    pickle.dump(lst,file)
'''
## Unpickling

import pickle
file=open('pypickle.txt','rb')
lst1=pickle.load(file)
print(lst1)
