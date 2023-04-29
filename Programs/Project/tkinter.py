from tkinter import *
from tkinter import ttk
import pymysql

class NTHStudentsInfo:
    def __init__(self,root):
        self.root=root
        self.root.title('NTH')
        self.root.geometry('1300x650')
        label1=Label(self.root,text='NTH Students Management System',font=('cooper black',40,'bold'),bg='green',fg='white',relief=RAISED)
        label1.pack(fill='x')

        formFrame=Frame(self.root,bg='green')
        formFrame.place(x=10,y=80,width=400,height=550)
        
        dataFrame=Frame(self.root,bg='green')
        dataFrame.place(x=420,y=80,width=870,height=550)

        self.roll_no_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.emailid_var = StringVar()
        self.contact_var = StringVar()
        self.course_var = StringVar()
        self.location_var = StringVar()

        label3=Label(dataFrame,text='Students Information Display',bg='green',fg='white',font=('elephant',15,'bold'),bd=5,relief=RAISED)
        label3.grid(row=0,columnspan=5,padx=250,pady=15)

        tableFrame = Frame(dataFrame, bg='green',bd=5,relief='groove')
        tableFrame.place(x=30,y=60, width=800, height=420)

        self.Student_Table = ttk.Treeview(tableFrame, column=('roll_no', 'first_name', 'last_name', 'emailid', 'contact', 'course', 'location'))


        self.Student_Table.heading('roll_no', text='Roll No')
        self.Student_Table.heading('first_name', text='First Name')
        self.Student_Table.heading('last_name', text='Last Name')
        self.Student_Table.heading('emailid', text='Email ID'),
        self.Student_Table.heading('contact', text='Contact No')
        self.Student_Table.heading('course', text='Course')
        self.Student_Table.heading('location', text='Location')

        self.Student_Table['show'] = 'headings'

        self.Student_Table.column('roll_no', width=100, anchor=CENTER)
        self.Student_Table.column('first_name', width=100, anchor=CENTER)
        self.Student_Table.column('last_name', width=100, anchor=CENTER)
        self.Student_Table.column('emailid', width=150, anchor=CENTER)
        self.Student_Table.column('contact', width=100, anchor=CENTER)
        self.Student_Table.column('course', width=100, anchor=CENTER)
        self.Student_Table.column('location', width=150, anchor=CENTER)
        
        self.Student_Table.pack()
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetching_data()
            
#working with frame
        label2=Label(formFrame,text='Students Information Entry',bg='green',fg='white',font=('elephant',15,'bold'),bd=5,relief=RAISED)
        label2.grid(row=0,columnspan=5,padx=50,pady=15)

#roll number
        lbl_rollno=Label(formFrame,text='Roll Number',font=('HP Simplified Japan',15,'bold'),bg='green',fg='white')
        lbl_rollno.grid(row=1,column=0,sticky='W')

        entry_rollno=Entry(formFrame, textvariable = self.roll_no_var, font=('HP Simplified Japan',15,'bold'))
        entry_rollno.grid(row=1,column=1,pady=10)

#first name
        lbl_fname=Label(formFrame,text='First Name',font=('HP Simplified Japan',15,'bold'),bg='green',fg='white')
        lbl_fname.grid(row=2,column=0,sticky='W')

        entry_fname=Entry(formFrame, textvariable = self.first_name_var,font=('HP Simplified Japan',15,'bold'))
        entry_fname.grid(row=2,column=1)
#last name
        lbl_lname=Label(formFrame,text='Last name',font=('HP Simplified Japan',15,'bold'),bg='green',fg='white')
        lbl_lname.grid(row=3,column=0,sticky='W')

        entry_lname=Entry(formFrame, textvariable = self.last_name_var,font=('HP Simplified Japan',15,'bold'))
        entry_lname.grid(row=3,column=1,pady=10)

#emaild
        lbl_email=Label(formFrame,text='Email ID',font=('HP Simplified Japan',15,'bold'),bg='green',fg='white')
        lbl_email.grid(row=4,column=0,sticky='W')

        entry_email=Entry(formFrame, textvariable = self.emailid_var,font=('HP Simplified Japan',15,'bold'))
        entry_email.grid(row=4,column=1)

#contact no
        lbl_cno=Label(formFrame,text='Contact No',font=('HP Simplified Japan',15,'bold'),bg='green',fg='white')
        lbl_cno.grid(row=5,column=0,sticky='W')

        entry_cno=Entry(formFrame, textvariable = self.contact_var,font=('HP Simplified Japan',15,'bold'))
        entry_cno.grid(row=5,column=1,pady=10)

#course name
        lbl_cname=Label(formFrame,text='Course Name',font=('HP Simplified Japan',15,'bold'),bg='green',fg='white')
        lbl_cname.grid(row=6,column=0,sticky='W')

        entry_cname=Entry(formFrame, textvariable = self.course_var,font=('HP Simplified Japan',15,'bold'))
        entry_cname.grid(row=6,column=1)

#location
        lbl_loc=Label(formFrame,text='location',font=('HP Simplified Japan',15,'bold'),bg='green',fg='white')
        lbl_loc.grid(row=7,column=0,sticky='W')

        entry_loc=Entry(formFrame, textvariable = self.location_var,font=('HP Simplified Japan',15,'bold'))
        entry_loc.grid(row=7,column=1,pady=10)

#Cteating btnFrame

        btnFrame=Frame(formFrame,bg='green',bd=5,relief='groove')
        btnFrame.place(x=10,y=380,height=100,width=370)

        #Add Button
        btnAdd=Button(btnFrame,text='Add',command = self.adding_data, font=('HP Simplified Japan',15,'bold'),bg='red',fg='yellow')
        btnAdd.grid(row=0,column=0,padx=10,pady=20)

        #Update Button
        btnUpdate=Button(btnFrame,text='Update',command = self.update_data, font=('HP Simplified Japan',15,'bold'),bg='yellow',fg='red')
        btnUpdate.grid(row=0,column=1,padx=10,pady=20)

        #Delete Button
        btnDelete=Button(btnFrame,text='Delete',command=self.delete_data, font=('HP Simplified Japan',15,'bold'),bg='black',fg='white')
        btnDelete.grid(row=0,column=2,padx=10,pady=20)

        #clear
        btnClear=Button(btnFrame,command = self.clearing_data, text='Clear',font=('HP Simplified Japan',15,'bold'))
        btnClear.grid(row=0,column=3,padx=10,pady=20)

    def adding_data(self):
        connection = pymysql.connect(host = 'localhost', user='root', password='Manjusha@17', db='studentsinfodb')
        c = connection.cursor()
        c.execute('insert into studentsdata values(%s, %s, %s, %s, %s, %s, %s)',
                  (
                    self.roll_no_var.get(),
                    self.first_name_var.get(),
                    self.last_name_var.get(),
                    self.emailid_var.get(),
                    self.contact_var.get(),
                    self.course_var.get(),
                    self.location_var.get()
                      )
                  )
        connection.commit()
        self.fetching_data()
        self.clearing_data()
        connection.close()

    def clearing_data(self):
        self.roll_no_var.set('')
        self.first_name_var.set('')
        self.last_name_var.set('')
        self.emailid_var.set('')
        self.contact_var.set('')
        self.course_var.set('')
        self.location_var.set('')

    def fetching_data(self):
        connection = pymysql.connect(host = 'localhost', user='root', password='Manjusha@17', db='studentsinfodb')
        c = connection.cursor()
        c.execute('select * from studentsdata')
        data = c.fetchall()   #((----),(-----),(-----))
        if len(data) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for i in data:
                self.Student_Table.insert('', END, value=i)
        connection.commit()
        connection.close()

    def get_cursor(self,var):
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.roll_no_var.set(row[0])
        self.first_name_var.set(row[1])
        self.last_name_var.set(row[2])
        self.emailid_var.set(row[3])
        self.contact_var.set(row[4])
        self.course_var.set(row[5])
        self.location_var.set(row[6])

    def update_data(self):
        connection = pymysql.connect(host = 'localhost', user='root', password='Manjusha@17', db='studentsinfodb')
        c = connection.cursor()
        c.execute('update studentsdata set first_name=%s, last_name=%s, emailid=%s, contact=%s, course=%s, location=%s where roll_no=%s',
                  (self.first_name_var.get(),
                   self.last_name_var.get(),
                   self.emailid_var.get(),
                   self.contact_var.get(),
                   self.course_var.get(),
                   self.location_var.get(),
                   self.roll_no_var.get()
                   ))
        connection.commit()
        self.fetching_data()
        self.clearing_data()
        connection.close()

    def delete_data(self):
        connection = pymysql.connect(host = 'localhost', user='root', password='Manjusha@17', db='studentsinfodb')
        c = connection.cursor()
        c.execute('delete from studentsdata where roll_no=%s', self.roll_no_var.get())
        connection.commit()
        self.fetching_data()
        self.clearing_data()
        connection.close()
        
root=Tk()
obj=NTHStudentsInfo(root)
root.mainloop()
