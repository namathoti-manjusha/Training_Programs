from tkinter import*
from tkinter import messagebox
import os

def login():
    user = username.get()
    code = password.get()

    if (user == "manju" and code == 'admin'):

        def register():

            root = Toplevel(screen)
            root.title("Registration")
            root.geometry("800x1100+200+100")
            root.resizable(False, False)

            Label(root,text="Student Registration Form", font=("arial",50,'bold'),fg="black").pack(pady=50)




            f=Frame(width=600,height=600)
            f.place(x=50,y=50)

            Label(f,text="Name", font=20).place(x=100, y=150)
            Label(f,text="Phone", font=20).place(x=100, y=200)
            Label(f,text="Gender", font=20).place(x=100, y=250)
            Label(f,text="Email", font=20).place(x=100, y=300)

            nameValue = StringVar()
            phoneValue = StringVar()
            genderValue = StringVar()
            emailValue = StringVar()

            nameEntry = Entry(f, textvariable=nameValue, width=30, bd=2, font=20)
            phoneEntry = Entry(f, textvariable=phoneValue, width=30, bd=2, font=20)
            genderEntry = Entry(f, textvariable=genderValue, width=30, bd=2, font=20)
            emailEntry = Entry(f, textvariable=emailValue, width=30, bd=2, font=20)

            nameEntry.place(x=200, y=150)
            phoneEntry.place(x=200, y=200)
            genderEntry.place(x=200, y=250)
            emailEntry.place(x=200, y=300)

            checkValue = IntVar
            checkbtn = Checkbutton(f,text="remember me?", variable=checkValue)
            checkbtn.place(x=200, y=340)

            Button(f,text="Register", font=10, width=11, height=2).place(x=250, y=380)

        register()


    elif (user == "" and code == ""):
        messagebox.showinfo("", "Blank Not Allowed")

    else:
        messagebox.showinfo("", "incorrect Username and Password")

def main_screen():

    global screen
    global username
    global password

    screen=Tk()
    screen.configure(bg='#d7dae2')

    label1 = Label(text='Admin', font=("arial",50,'bold'),fg="black",bg="#d7dae2")
    label1.pack(pady=50)

    bordercolor=Frame(screen,bg="black",width=800,height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg="#d7dae2",width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe, text='User Name',font=("arial",30,'bold'),bg="#d7dae2").place(x=100,y=50)
    Label(mainframe, text='Password', font=("arial", 30,'bold'), bg="#d7dae2").place(x=100, y=150)

    username=StringVar()
    password=StringVar()


    entry_username = Entry(mainframe, textvariable=username,width=12,bd=2,font=("arial",30))
    entry_username.place(x=400, y=50)
    entry_password = Entry(mainframe, textvariable=password,width=12,bd=2,font=("arial",30),show="*")
    entry_password.place(x=400, y=150)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    Button(mainframe, text='login', height="2", width=23, bg="#ed3833", fg="white", bd=0,command=login).place(x=100, y=250)
    Button(mainframe, text='signup', height="2", width=23, bg="#1089ff", fg="white", bd=0).place(x=300, y=250)
    Button(mainframe, text='reset', height="2", width=23, bg="#00bd56", fg="white", bd=0,command=reset).place(x=500, y=250)

    screen.mainloop()

main_screen()
