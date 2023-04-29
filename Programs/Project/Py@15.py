from tkinter import *
import pymysql
from tkinter import ttk

class StudentsInfo:
    def __init__(self, root):
        self.root = root
        self.root.title('NTH')
        self.root.geometry('1350x690')
        title1 = Label(self.root, text='Welcome to NTH Students Information', font=('Elephant',30,'bold'),
                       bd=5, relief = RAISED, bg='green', fg='white')
        title1.pack(fill=X)

        self.rollnoVar = StringVar()
        self.fnameVar = StringVar()
        self.lnameVar = StringVar()
        self.cnameVar = StringVar()
        self.emailidVar = StringVar()
        self.inameVar = StringVar()
        self.locVar = StringVar()
        self.contactVar = StringVar()

        #=====Creating Frames======
        dataEntryFrame = Frame(self.root, bg='green')
        dataEntryFrame.place(x=10, y=70, width=400, height=600)

        dataDisplayFrame = Frame(self.root, bg='green')
        dataDisplayFrame.place(x=420, y=70, width=920, height=600)
        

        #=====Working with Data Entry Frame====
        title2 = Label(dataEntryFrame, text='Data Entry Here',font=('Forte',20,'bold'),bd=5, relief = RAISED, bg='green', fg='white')
        title2.grid(row=0, columnspan=2, padx=80, pady=20)

        title3 = Label(dataDisplayFrame, text='Data Display Here',font=('Forte',20,'bold'),bd=5, relief = RAISED, bg='green', fg='white')
        title3.grid(row=0, columnspan=2, padx=300, pady=20)

    
        #----Roll No----
        rollnoLabel = Label(dataEntryFrame, text='Roll No:',font=('Book Antique',17,'bold'), bg='green', fg='white')
        rollnoLabel.grid(row=1, column=0, sticky='W', padx=5)

        rollNoEntry = Entry(dataEntryFrame,textvariable = self.rollnoVar,font=('Book Antique',15,'bold'))
        rollNoEntry.grid(row=1, column=1,sticky='E', pady=10)

        #----First Name----
        fnameLabel = Label(dataEntryFrame, text='First Name:',font=('Book Antique',17,'bold'), bg='green', fg='white')
        fnameLabel.grid(row=2, column=0, sticky='W', padx=5)

        fnameEntry = Entry(dataEntryFrame,textvariable = self.fnameVar, font=('Book Antique',15,'bold'))
        fnameEntry.grid(row=2, column=1,sticky='E')

        #----Last Name----
        lnameLabel = Label(dataEntryFrame, text='Last Name:',font=('Book Antique',17,'bold'), bg='green', fg='white')
        lnameLabel.grid(row=3, column=0, sticky='W', padx=5)

        lnameEntry = Entry(dataEntryFrame,textvariable = self.lnameVar, font=('Book Antique',15,'bold'))
        lnameEntry.grid(row=3, column=1,sticky='E', pady=10)

        #----Course Name
        cnameLabel = Label(dataEntryFrame, text='Course Name:',font=('Book Antique',17,'bold'), bg='green', fg='white')
        cnameLabel.grid(row=4, column=0, sticky='W', padx=5)

        cnameEntry = Entry(dataEntryFrame,textvariable = self.cnameVar, font=('Book Antique',15,'bold'))
        cnameEntry.grid(row=4, column=1,sticky='E')
        #---- Email Id
        emailLabel = Label(dataEntryFrame, text='Email ID:',font=('Book Antique',17,'bold'), bg='green', fg='white')
        emailLabel.grid(row=5, column=0, sticky='W', padx=5)

        emailEntry = Entry(dataEntryFrame,textvariable = self.emailidVar, font=('Book Antique',15,'bold'))
        emailEntry.grid(row=5, column=1,sticky='E', pady=10)

        #---- Institute Name-----
        inameLabel = Label(dataEntryFrame, text='Institute:',font=('Book Antique',17,'bold'), bg='green', fg='white')
        inameLabel.grid(row=6, column=0, sticky='W', padx=5)

        inameEntry = Entry(dataEntryFrame,textvariable = self.inameVar, font=('Book Antique',15,'bold'))
        inameEntry.grid(row=6, column=1,sticky='E')

        #----- Location----
        locLabel = Label(dataEntryFrame, text='Location:',font=('Book Antique',17,'bold'), bg='green', fg='white')
        locLabel.grid(row=7, column=0, sticky='W', padx=5)

        locEntry = Entry(dataEntryFrame,textvariable = self.locVar, font=('Book Antique',15,'bold'))
        locEntry.grid(row=7, column=1,sticky='E', pady=10)

        #---- Contact-----
        contactLabel = Label(dataEntryFrame, text='Contact:',font=('Book Antique',17,'bold'), bg='green', fg='white')
        contactLabel.grid(row=8, column=0, sticky='W', padx=5)

        contactEntry = Entry(dataEntryFrame,textvariable = self.contactVar, font=('Book Antique',15,'bold'))
        contactEntry.grid(row=8, column=1,sticky='E')

        #======Creating button Frame=========
        btnFrame = Frame(dataEntryFrame, bg='green', bd=5, relief=RAISED)
        btnFrame.place(x=10, y=450, width=380, height=100)

        #Creating buttons------
        addBtn = Button(btnFrame,text='Add',command = self.addingData, font=('Book Antique',15,'bold'), bg='red', fg='white')
        addBtn.grid(row=0, column=0, padx=10, pady=20)

        updateBtn = Button(btnFrame, text='Update',command = self.updatingData, font=('Book Antique',15,'bold'), bg='yellow', fg='red')
        updateBtn.grid(row=0, column=1, padx=10, pady=20)

        deleteBtn = Button(btnFrame, text='Delete',command = self.deletingData,font=('Book Antique',15,'bold'), bg='black', fg='yellow')
        deleteBtn.grid(row=0, column=2, padx=10, pady=20)

        clearBtn = Button(btnFrame,command = self.clearingData, text='Clear',font=('Book Antique',15,'bold'))
        clearBtn.grid(row=0, column=3, padx=10, pady=20)


        tableFrame = Frame(dataDisplayFrame)
        tableFrame.place(x = 20, y=70, width=870, height=400)

        self.StudentTable = ttk.Treeview(tableFrame,columns=('roll_no', 'fname', 'lname', 'cname', 'email_id', 'institute', 'location', 'contact'))

        self.StudentTable.heading('roll_no', text='Roll No')
        self.StudentTable.heading('fname', text='First Name')
        self.StudentTable.heading('lname', text='Last Name')
        self.StudentTable.heading('cname', text='Course')
        self.StudentTable.heading('email_id', text='Email ID')
        self.StudentTable.heading('institute', text='Institute')
        self.StudentTable.heading('location', text='Location')
        self.StudentTable.heading('contact', text='Contact')

        self.StudentTable['show']='headings'
        self.StudentTable.column('roll_no', width=70, anchor='center')
        self.StudentTable.column('fname', width=120, anchor='center')
        self.StudentTable.column('lname', width=120, anchor='center')
        self.StudentTable.column('cname', width=100, anchor='center')
        self.StudentTable.column('email_id', width=150, anchor='center')
        self.StudentTable.column('institute', width=100, anchor='center')
        self.StudentTable.column('location', width=100, anchor='center')
        self.StudentTable.column('contact', width=100, anchor='center')
        
        self.StudentTable.pack()
        self.fetchingData()

        self.StudentTable.bind('<ButtonRelease-1>', self.getCursor)
         

    def addingData(self):
        connection = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='studentsdb')
        c = connection.cursor()
        c.execute('insert into studentsdata values(%s, %s, %s, %s, %s, %s, %s, %s)',
                    (
                        self.rollnoVar.get(),
                        self.fnameVar.get(),
                        self.lnameVar.get(),
                        self.cnameVar.get(),
                        self.emailidVar.get(),
                        self.inameVar.get(),
                        self.locVar.get(),
                        self.contactVar.get()
                        )
                  )
        connection.commit()
        self.clearingData()
        self.fetchingData()
        connection.close()

        
    def clearingData(self):
        self.rollnoVar.set('')
        self.fnameVar.set('')
        self.lnameVar.set('')
        self.cnameVar.set('')
        self.emailidVar.set('')
        self.inameVar.set('')
        self.locVar.set('')
        self.contactVar.set('')
        
    def clear(self):
        for item in self.StudentTable.get_children():
            self.StudentTable.delete(item)
            
    def fetchingData(self):
        connection = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='studentsdb')
        c2 = connection.cursor()
        c2.execute('select * from studentsdata')
        data = c2.fetchall()
        self.clear()
        for i in data:
            self.StudentTable.insert('', END, value=i)
        connection.close()
        
    def getCursor(self,var):
        cursor_row = self.StudentTable.focus()
        content = self.StudentTable.item(cursor_row)
        row  = content['values']
        self.rollnoVar.set(row[0])
        self.fnameVar.set(row[1])
        self.lnameVar.set(row[2])
        self.cnameVar.set(row[3])
        self.emailidVar.set(row[4])
        self.inameVar.set(row[5])
        self.locVar.set(row[6])
        self.contactVar.set(row[7])
        

    def updatingData(self):
        connection  = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='studentsdb')
        c3 = connection.cursor()
        c3.execute('update studentsdata set fname=%s, lname=%s, cname=%s, email_id=%s, institute=%s, location=%s, contact=%s where roll_no=%s',
                   (
                       self.fnameVar.get(),
                       self.lnameVar.get(),
                       self.cnameVar.get(),
                       self.emailidVar.get(),
                       self.inameVar.get(),
                       self.locVar.get(),
                       self.contactVar.get(),
                       self.rollnoVar.get()
                       ))
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()

    def deletingData(self):
        connection  = pymysql.connect(host='localhost', user='root', password='Manjusha@17', db='studentsdb')
        c3 = connection.cursor()
        c3.execute('delete from studentsdata where roll_no=%s', self.rollnoVar.get())
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()
        
        
root = Tk()
obj = StudentsInfo(root)
mainloop()























