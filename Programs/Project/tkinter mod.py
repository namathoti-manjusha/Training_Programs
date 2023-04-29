from tkinter import *
class studentsinfo:
    def __init__(self,root):
        self.root=root
        self.root.title('NTH')
        self.root.geometry('1300x650')
        title1=Label(self.root,text='Welcome To Students Information',bg='green',fg='white',font=('cooper black',30,'bold'),bd=5,relief=RAISED)
        title1.pack(fill='x')
        #======creating Data Entry Frame====
        dataEntryFrame=Frame(self.root,bg='green')
        dataEntryFrame.place(x=10,y=80,height=550,width=400)

        title2=Label(dataEntryFrame,text='Students Data Entry',bg='red',fg='white',font=('elephant',20,'bold'))
        title2.grid(row=0,columnspan=2,padx=50,pady=20)
        
        #======creating Data Display Frame====
        dataDisplayFrame=Frame(self.root,bg='green')
        dataDisplayFrame.place(x=420,y=80,height=550,width=870)

        title3=Label(dataDisplayFrame,text='Students Data Display Frame',bg='black',fg='white',font=('elephant',20,'bold'))
        title3.grid(row=0,columnspan=2,padx=50,pady=20 )
root=Tk()
obj=studentsinfo(root)
root.mainloop()
