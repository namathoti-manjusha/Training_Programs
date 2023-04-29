'''
def squares(lst):
    lst1=[]
    for i in lst:
        lst1.append(i*i)
    print(lst1)
def cubes(lst):
    lst1=[]
    for i in lst:
        lst1.append(i*i*i)
    print(lst1)
lst=range(1000)
squares(lst)
cubes(lst)
'''
###
'''
import time
def squares(lst):
    lst1=[]
    start=time.time()
    for i in lst:
        lst1.append(i*i)
    end=time.time()
    print('The squares function duration is:',end-start)
    #print(lst1)
def cubes(lst):
    lst1=[]
    start=time.time()
    for i in lst:
        lst1.append(i*i*i)
    end=time.time()
    print('The cubes function duration is:',end-start)
    #print(lst1)
lst=range(10000000)
squares(lst)
cubes(lst)
'''
###

import time
def dec_fun(fun):
    def wrap_fun(*arg):
        start=time.time()
        result=fun(*arg)
        end=time.time()
        print('The',fun.__name__,'function duration is:',end-start)
        return result
    return wrap_fun
@dec_fun
def squares(lst):
    lst1=[]
    for i in lst:
        lst1.append(i*i)
    #print(lst1)
@dec_fun        
def cubes(lst):
    lst1=[]
    for i in lst:
        lst1.append(i*i*i)
    #print(lst1)
lst=range(100000000)
squares(lst)
cubes(lst)



























