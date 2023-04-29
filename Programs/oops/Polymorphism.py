#Method overloading

'''
class myclass:
    def display(self,a):
        print('its first method')
    def display(self,a,b):
        print('its second method')
    def display(self,a,b,c):
        print('its third method')
c=myclass()
c.display(10,20,30)
'''
    
#Method overriding
'''

class A:
    def display(self):
        print('its A class method')
class B(A):
    def display(self):
        print('its B class method')
        super().display()
b=B()
b.display()
'''

























