#single-level inheritance
'''
class A:
    a1=10
    def am1(self):
        print('am1 is {}'.format(A.a1))
class B(A):
    b1=20
    def bm1(self):
        print('bm1 is {}'.format(B.b1))
b=B()
print(b.b1)
b.bm1()
print(b.a1)
b.am1()
'''

#Multi-level inheritance
'''
class A:
    a1=10
    def am1(self):
        print('am1 is {}'.format(A.a1))
class B(A):
    b1=20
    def bm1(self):
        print('bm1 is {}'.format(B.b1))
class C(B):
    c1=30
    def cm1(self):
        print('cm1 is {}'.format(C.c1))
c=C()
print(c.c1)
c.cm1()
print(c.b1)
c.bm1()
print(c.a1)
c.am1()
'''

#Multiple inheritance
'''
class A:
    a1=10
    def am1(self):
        print('am1 is {}'.format(A.a1))
class B:
    b1=20
    def bm1(self):
        print('bm1 is {}'.format(B.b1))
class C(A,B):
    c1=30
    def cm1(self):
        print('cm1 is {}'.format(C.c1))
c=C()
print(c.c1)
c.cm1()
print(c.a1)
c.am1()
print(c.b1)
c.bm1()
'''

#Hierarichical Inheritance

class A:
    a1=10
    def am1(self):
        print('am1 is {}'.format(A.a1))
class B(A):
    b1=20
    def bm1(self):
        print('bm1 is {}'.format(B.b1))
class C(A):
    c1=30
    def cm1(self):
        print('cm1 is {}'.format(C.c1))
c=C()
print(c.c1)
c.cm1()
print(c.a1)
c.am1()
b=B()
print(b.b1)
b.bm1()
print(b.a1)
b.am1()


































