from tkinter import*
from tkinter import messagebox
root=Tk()
root.minsize(height=200,width=400)
def tab1():
    def login():
        username=entry1.get()
        password=entry2.get()
        if (username=="" and password==""):
            messagebox.showinfo("","Blank Not Allowed")
        elif (username=="manju" and password=='admin'):
            messagebox.showinfo("", "Login Success")
        else:
            messagebox.showinfo("", "incorrect Username and Password")
    global entry1
    global entrt2
    Label(root, text='User Name').place(x=30, y=30)
    Label(root, text='Password').place(x=30, y=70)
    entry1 = Entry(root, bd=5)
    entry1.place(x=140, y=30)
    entry2 = Entry(root, bd=5)
    entry2.place(x=140, y=70)

    def tab2():
        label1.destroy()
        label2=Label(root,text='Student Registration',font=('Times_New_Roman',25))
        label2.pack()
        Button(root,text='Register',font=('Times_New_Roman',15)).place(x=200, y=100)
        Button(root, text='login', font=('Times_New_Roman', 10), command=login, height=1, width=5, bd=6).place(x=140,y=120)
    label1 = Label(root, text='Admin', font=('Times_New_Roman',15))
    label1.pack()
    Button(root, text='Next', font=('Times_New_Roman', 15), command=tab2, height=1, width=5, bd=6).place(x=250, y=100)

tab1()
root.mainloop()