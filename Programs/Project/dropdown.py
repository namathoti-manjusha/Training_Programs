import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import pymysql

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width = 30, bd = 5)
        T1.place(x=180, y=20)
        
        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width = 30, show='*', bd = 5)
        T2.place(x=180, y=80)
        
        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
         
        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)
        
        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial",15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x = 200, y=10)
            
            l2 = tk.Label(window, text="Password:", font=("Arial",15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x = 200, y=60)
            
            l3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x = 200, y=110)
            
            def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("credential.txt", "a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            b1 = tk.Button(window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)
            
            window.geometry("470x220")
            window.mainloop()
            
        B2 = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        B2.place(x=650, y=20)
        
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

               
        
        label1 = tk.Label(self, text='Students Course Enrollment System', font=('cooper black', 30, 'bold'), bg='black',
                       fg='white')
        label1.place(x=230,y=230)

        button=tk.Button(self,text="Home",font=('cooper black', 30, 'bold'), bg='black',fg='white', command=lambda:controller.show_frame(FirstPage))
        button.place(x=650,y=450)
        
        formFrame = tk.Frame(self, bg='cyan')
        formFrame.place(x=10, y=80, width=400, height=550)

        dataFrame = tk.Frame(self, bg='cyan')
        dataFrame.place(x=420, y=80, width=870, height=550)

        self.rool_no_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.emailid_var = StringVar()
        self.contact_var = StringVar()
        self.course_var = StringVar()
        self.location_var = StringVar()

        label3 = tk.Label(dataFrame, text='Students Information Display', bg='black', fg='white',
                       font=('elephant', 15, 'bold'), bd=5, relief=RAISED)
        label3.grid(row=0, columnspan=5, padx=250, pady=15)

        tableFrame = tk.Frame(dataFrame, bg='cyan', bd=5, relief=GROOVE)
        tableFrame.place(x=30, y=60, width=800, height=420)

        self.Student_Table = ttk.Treeview(tableFrame, column=('rool_no', 'first_name', 'last_name', 'emailid', 'contact', 'course', 'location'))

        self.Student_Table.heading('rool_no', text='Roll No')
        self.Student_Table.heading('first_name', text='First Name')
        self.Student_Table.heading('last_name', text='Last Name')
        self.Student_Table.heading('contact', text='Contact No')
        self.Student_Table.heading('course', text='Course')
        self.Student_Table.heading('location', text='Location')
        self.Student_Table.heading('emailid', text='Email ID')

        self.Student_Table['show'] = 'headings'

        self.Student_Table.column('rool_no', width=100, anchor=CENTER)
        self.Student_Table.column('first_name', width=100, anchor=CENTER)
        self.Student_Table.column('last_name', width=100, anchor=CENTER)
        self.Student_Table.column('contact', width=100, anchor=CENTER)
        self.Student_Table.column('course', width=100, anchor=CENTER)
        self.Student_Table.column('location', width=150, anchor=CENTER)
        self.Student_Table.column('emailid', width=150, anchor=CENTER)

        self.Student_Table.pack()
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetching_data()

        # working with frame
        label2 = tk.Label(formFrame, text='Students Enrollment', bg='black', fg='white',
                       font=('elephant', 15, 'bold'), bd=5, relief=RAISED)
        label2.grid(row=0, columnspan=5, padx=50, pady=15)

        # roll number
        lbl_roolno = tk.Label(formFrame, text='Roll Number', font=('HP Simplified Japan', 15, 'bold'), bg='cyan',
                           fg='black')
        lbl_roolno.grid(row=1, column=0, sticky='W')

        entry_roolno = tk.Entry(formFrame, textvariable=self.rool_no_var, font=('HP Simplified Japan', 15, 'bold'))
        entry_roolno.grid(row=1, column=1, pady=10)

        # first name
        lbl_fname = tk.Label(formFrame, text='First Name', font=('HP Simplified Japan', 15, 'bold'), bg='cyan',
                          fg='black')
        lbl_fname.grid(row=2, column=0, sticky='W')

        entry_fname = tk.Entry(formFrame, textvariable=self.first_name_var, font=('HP Simplified Japan', 15, 'bold'))
        entry_fname.grid(row=2, column=1)
        # last name
        lbl_lname = tk.Label(formFrame, text='Last name', font=('HP Simplified Japan', 15, 'bold'), bg='cyan', fg='black')
        lbl_lname.grid(row=3, column=0, sticky='W')

        entry_lname = tk.Entry(formFrame, textvariable=self.last_name_var, font=('HP Simplified Japan', 15, 'bold'))
        entry_lname.grid(row=3, column=1, pady=10)

        # emaild
        lbl_email = tk.Label(formFrame, text='Email ID', font=('HP Simplified Japan', 15, 'bold'), bg='cyan', fg='black')
        lbl_email.grid(row=4, column=0, sticky='W')

        entry_email = tk.Entry(formFrame, textvariable=self.emailid_var, font=('HP Simplified Japan', 15, 'bold'))
        entry_email.grid(row=4, column=1)

        # contact no
        lbl_cno = tk.Label(formFrame, text='Contact No', font=('HP Simplified Japan', 15, 'bold'), bg='cyan', fg='black')
        lbl_cno.grid(row=5, column=0, sticky='W')

        entry_cno = tk.Entry(formFrame, textvariable=self.contact_var, font=('HP Simplified Japan', 15, 'bold'))
        entry_cno.grid(row=5, column=1, pady=10)

        # course name
        lbl_cname = tk.Label(formFrame, text='Course Name', font=('HP Simplified Japan', 15, 'bold'), bg='cyan',
                          fg='black')
        lbl_cname.grid(row=6, column=0, sticky='W')

        course=["Python","Java","C","C++","Ruby","LISP","UI","SQL"]
        courseroom=StringVar(self)
        courseroom.set("Select Perticular Course")
        menu=OptionMenu(formFrame,courseroom,*course)
        menu.grid(row=6,column=1,padx=30,pady=10)
        
        
        # location
        lbl_loc = tk.Label(formFrame, text='location', font=('HP Simplified Japan', 15, 'bold'), bg='cyan', fg='black')
        lbl_loc.grid(row=7, column=0, sticky='W')

        entry_loc = tk.Entry(formFrame, textvariable=self.location_var, font=('HP Simplified Japan', 15, 'bold'))
        entry_loc.grid(row=7, column=1, pady=10)

        # Cteating btnFrame

        btnFrame = tk.Frame(formFrame, bg='cyan', bd=5, relief='groove')
        btnFrame.place(x=10, y=380, height=100, width=370)

        # Add Button
        btnAdd = tk.Button(btnFrame, text='Add', command=self.adding_data, font=('HP Simplified Japan', 15, 'bold'),
                        bg='black', fg='white')
        btnAdd.grid(row=0, column=0, padx=10, pady=20)

        # Update Button
        btnUpdate = tk.Button(btnFrame, text='Update', command=self.update_data, font=('HP Simplified Japan', 15, 'bold'),
                           bg='black', fg='white')
        btnUpdate.grid(row=0, column=1, padx=10, pady=20)

        # Delete Button
        btnDelete = tk.Button(btnFrame, text='Delete', command=self.delete_data, font=('HP Simplified Japan', 15, 'bold'),
                           bg='black', fg='white')
        btnDelete.grid(row=0, column=2, padx=10, pady=20)

        # clear
        btnClear = tk.Button(btnFrame, command=self.clearing_data, text='Clear', font=('HP Simplified Japan', 15, 'bold'),bg='black', fg='white')
        btnClear.grid(row=0, column=3, padx=10, pady=20)

    def adding_data(self):
        mydb = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='sem')
        cur =mydb.cursor()
        cur.execute('insert into student values(%s, %s, %s, %s, %s, %s, %s)',
                  (
                      self.rool_no_var.get(),
                      self.first_name_var.get(),
                      self.last_name_var.get(),
                      self.emailid_var.get(),
                      self.contact_var.get(),
                      self.course_var.get(),
                      self.location_var.get()
                  ))
        mydb.commit()
        self.fetching_data()
        self.clearing_data()
        mydb.close()

    def clearing_data(self):
        self.rool_no_var.set('')
        self.first_name_var.set('')
        self.last_name_var.set('')
        self.emailid_var.set('')
        self.contact_var.set('')
        self.course_var.set('')
        self.location_var.set('')


    def fetching_data(self):
        mydb = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='sem')
        cur = mydb.cursor()
        cur.execute('select * from student')
        data = cur.fetchall()  # ((----),(-----),(-----))
        if len(data) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for i in data:
                self.Student_Table.insert('', END, value=i)
        mydb.commit()
        mydb.close()

    def get_cursor(self, var):
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.rool_no_var.set(row[0])
        self.first_name_var.set(row[1])
        self.last_name_var.set(row[2])
        self.emailid_var.set(row[3])
        self.contact_var.set(row[4])
        self.course_var.set(row[5])
        self.location_var.set(row[6])

    def update_data(self):
        mydb =pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='sem')
        cur = mydb.cursor()
        cur.execute('update student set first_name=%s, last_name=%s, emailid=%s, contact=%s, course=%s, location=%s where rool_no=%s',
            (
             self.first_name_var.get(),
             self.last_name_var.get(),
             self.emailid_var.get(),
             self.contact_var.get(),
             self.course_var.get(),
             self.location_var.get(),
             self.rool_no_var.get()
             ))
        mydb.commit()
        self.fetching_data()
        self.clearing_data()
        mydb.close()

    def delete_data(self):
        mydb = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='sem')
        cur = mydb.cursor()
        cur.execute('delete from student where rool_no=%s', self.rool_no_var.get())
        mydb.commit()
        self.fetching_data()
        self.clearing_data()
        mydb.close()

        
        
        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)
        
        
                
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage,SecondPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")
            
app=Application()
app.mainloop()
    
