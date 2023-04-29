#Multi-Threading

import threading
class Threading1(threading.Thread):
    def run(self):
        i=1
        while i<=10:
            print(i)
            i=i+1
class Threading2(threading.Thread):
    def run(self):
        i=11
        while i<=20:
            print(i)
            i=i+1
class Threading3(threading.Thread):
    def run(self):
        i=21
        while i<=30:
            print(i)
            i=i+1
t1=Threading1()
t2=Threading2()
t3=Threading3()
t1.start()
t2.start()
t3.start()


