#0-D Array
'''
import numpy as np
a1=np.array(10)
print(a1)
'''

#1-D array
'''
import numpy as np
a1=np.array([10,20,30,40])
print(a1)
'''
#2-D Array
'''
import numpy as np
a1=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a1)
print(a1.ndim)
print(a1.shape)
print(a1.dtype)
'''

#3-D Array
'''
import numpy as np
a1=np.array([[[10,20,30],[20,30,40]],[[30,40,50],[40,50,60]],[[50,60,70],[60,70,80]]])
print(a1)
print(a1.ndim)
print(a1.shape)
print(a1.dtype)
'''

#indexing 1-D array
'''
import numpy as np
a1=np.array([10,20,30,40])
print(a1[0])
print(a1[-3])
print(a1[-True])
'''

#slicing 1-D Array
'''
import numpy as np
a1=np.array([10,20,30,40])
print(a1[0:4])
print(a1[-3:-1])
'''

#indexing 2-D Array
'''
import numpy as np
a1=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a1[0][2])
print(a1[2][-1])
print(a1[1][2])
'''

#slicing 2-D Array
'''
import numpy as np
a1=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a1[1][0:2])
print(a1[1][-3:-1])
print(a1[-2][0:2])
print(a1[-2][-3:-1])
'''

#3-D Array
''''
import numpy as np
a1=np.array([[[10,20,30],[20,30,40]],[[30,40,50],[40,50,60]],[[50,60,70],[60,70,80]]])
print(a1[0][0][0])
print(a1[0][1][2])
print(a1[-1][1][2])
print(a1[-2][-2][2])
print(a1[0][-2][0])
'''

#slicing 3-D array
'''
import numpy as np
a1=np.array([[[10,20,30],[20,30,40]],[[30,40,50],[40,50,60]],[[50,60,70],[60,70,80]]])
print(a1[1][1][0:2])
print(a1[2][0][0:2])
print(a1[-1][-1][-3:-1])
print(a1[-2][-2][0:-1])
print(a1[-2][0:3])
'''

#iterating 1-d  array
'''
import numpy as np
a1=np.array([10,20,30,40])
for i in a1:
    print(i)
'''

#iterating 2-D array
'''
import numpy as np
a1=np.array([[10,20,30],[40,50,60],[70,80,90]])
for i in a1:
    for j in i:
        print(j)
'''

#iterating 3-D Array
'''
import numpy as np
a1=np.array([[[10,20,30],[20,30,40]],[[30,40,50],[40,50,60]],[[50,60,70],[60,70,80]]])
for i in a1:
    for j in i:
        for k in j:
            print(k)
'''


#finding maximum ,minimum,sum on matrix
'''
import numpy as np
a1=np.array([[10,20,30],[40,50,60]])

print(a1)
print(np.max(a1))
print(np.max(a1,axis=0))
print(np.max(a1,axis=1))
'''
'''
print(a1)
print(np.min(a1))
print(np.min(a1,axis=0))
print(np.min(a1,axis=1))
'''
'''
print(a1)
print(np.sum(a1))
print(np.sum(a1,axis=0))
print(np.sum(a1,axis=1))
'''


#concatinating Numpy Array
'''
import numpy as np
a1=np.array([[10,20,30],[40,50,60]])
a2=np.array([[60,50,40],[30,20,10]])
print(a1)
print(a2)
x=np.concatenate((a1,a2),axis=0)
print(x)

y=np.concatenate((a1,a2),axis=1)
print(y)

'''

