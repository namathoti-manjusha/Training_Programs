import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Admin(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        border=tk.LabelFrame(self,text="Login",font=('cooper black', 30, 'bold'), bg='black',fg='white', relief=RAISED)
        border.pack(fill="both",expand="yes",padx=150,pady=150)
        
        
        L1=tk.Label(border,text="username",font=('cooper black', 30, 'bold'), bg='black',fg='white', relief=RAISED)
        L1.place(x=50,y=20)
        t1 =tk. Entry(border,width=30,bd=5,font=('HP Simplified Japan', 15, 'bold'))
        t1.place(x=180,y=20)

        L2=tk.Label(border,text="password",font=('cooper black', 30, 'bold'), bg='black',fg='white', relief=RAISED)
        L2.place(x=50,y=80)
        t2 = tk.Entry(border,width=30,bd=5,show="*",font=('HP Simplifie d Japan', 15, 'bold'))
        t2.place(x=180,y=80)
        
        def verify():
            try:
                with open("credential.text","r")as f:
                    info=f.readlines()
                    i=0
                for e in info:
                    u,p=e.split(",")
                    if u.strip()==t1.get() and p.strip()==t2.get():
                        controller.showframe(studentsinfodb)
                        i=1
                        break
                if i==0:
                   messagebox.showinfo("Error","Please Provide correct username and password!") 
            except:
                messagebox.showinfo("Error","Please Provide correct username and password!") 

        B1 = tk.Button(border,text="submit", bg='cyan', bd=5, relief='groove',command=verify)
        B1.place(x=320, y=115)

        

        def register():
            window=Tk()
            window.title("Register")
            window.configure("cyan")
            window.resizable(0,0)
            l1=label(window,text="Username",font=('HP Simplifie d Japan', 15, 'bold'))
            l1.place(x=10,y=10)
            t1 = Entry(window,width=30,bd=5,font=('HP Simplifie d Japan', 15, 'bold'))
            t1.place(x=200,y=10)

            l2=label(window,text="password",font=('HP Simplifie d Japan', 15, 'bold'))
            l2.place(x=10,y=60)
            t2 = Entry(border,width=30,bd=5,show="*",font=('HP Simplifie d Japan', 15, 'bold'))
            t2.place(x=200,y=60)

            l3=label(window,text="conformpassword",font=('HP Simplifie d Japan', 15, 'bold'))
            l3.place(x=10,y=110)
            t3 = Entry(border,width=30,bd=5,show="*",font=('HP Simplifie d Japan', 15, 'bold'))
            t3.place(x=200,y=110)

            def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("Credential.txt","a")as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are Registered Successfully!")
                    else:
                        messagebox.showinfo("Error","Your Password didn't match!")
                else:
                    messagebox.showinfo("Error","Please complete the field!!!")
            b1=Button(window,text="sign in",font=('HP Simplifie d Japan', 15, 'bold'),bg="#ffc22a",command=check)
            b1.place(x=170,y=150)
            
            window.geometry("470x220")
            window.mainloop()

        B2 = Button(border, bg='cyan',text="Register", bd=5, relief='groove',command=register)
        B2.place(x=650, y=20)


class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        window=tk.Frame(self)
        window.pack()



        self.frames={}
        for F in (Admin):
            frame=F(window,self)
            self.frame[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(Admin)

    def show_frame(self,page):
        frame=self.frames[page]
        frame.tkraise()
        
app=Application()

app.mainloop()



