from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


class View(Frame):
    def __init__(self,master):
        super(View, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.staffid = IntVar()
        self.sname = StringVar()
        self.fname = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.state = StringVar()

        # self.bg = ImageTk.PhotoImage(Image.open("images\\FLYER pics.jpg"))
        # self.label = Label(image=self.bg).pack()


        ######## Title Label ############
        Label(window, text="STAFFS RECORDS", width=10, height=2, bg="magenta4",fg="#fff", font="arial, 20 bold").pack(side=TOP, fill=X)
        obj = LabelFrame(window, text="Staff's Details", font=20, bd=2, width=500,height=600, relief=GROOVE)
        obj.place(x=30, y=100)

        # ------------- LABELS
        self.lbstaffid = Label(window, text=" STAFF ID", font=("times new roman", 15, "bold"))
        self.lbstaffid.place(x=50, y=150)

        # ------------- ENTRY BOX
        self.txtstaffid = Entry(window, textvariable=self.staffid, width="12", bg="white",
                                font=("times new roman", 18))
        self.txtstaffid.place(x=190, y=150)

        self.btnSearch = Button(window, command=self.Searchnow, text=" Search ", cursor="hand2", width="15",
                              font=("times new roman", 12, "bold"),
                              bg="magenta4", fg="white")
        self.btnSearch.place(x=340, y=150)

        # ------------- SURNAME SECTION ##
        self.lbsurname = Label(window, text="Surname", font=("times new roman", 18, "bold"))
        self.lbsurname.place(x=50, y=210)

        self.txtsurname = Entry(window, textvariable=self.sname, width="25", bg="white",
                                font=("times new roman", 18))
        self.txtsurname.place(x=190, y=210)

        # ------------ FIRSTNAME SECTION ##
        self.lbfirstname = Label(window, text="Firstname", font=("times new roman", 18, "bold"))
        self.lbfirstname.place(x=50, y=260)

        self.txtfirstname = Entry(window, textvariable=self.fname, width="25", bg="white",
                                  font=("times new roman", 18))
        self.txtfirstname.place(x=190, y=260)

        # ----------- EMAIL SECTION ##
        self.lbemail = Label(window, text="Email", font=("times new roman", 18, "bold"))
        self.lbemail.place(x=50, y=320)

        self.txtemail = Entry(window, textvariable=self.email, width="25", bg="white", font=("times new roman", 18))
        self.txtemail.place(x=190, y=320)

        # ------------ GENDER SECTION ##
        self.lbsex = Label(window, text="Sex", font=("times new roman", 18, "bold"))
        self.lbsex.place(x=50, y=380)

        self.txtsex = Entry(window, textvariable=self.gender, width="25", bg="white", font=("times new roman", 18))
        self.txtsex.place(x=190, y=380)

        ## STATE SECTION ##
        self.lbstate = Label(window, text="State", font=("times new roman", 18, "bold"))
        self.lbstate.place(x=50, y=450)

        self.txtstate = Entry(window, textvariable=self.state, width="25", bg="white", font=("times new roman", 18))
        self.txtstate.place(x=190, y=450)

        ## BUTTONS SECTION ##
        self.btnClear = Button(window, height="2", text=" Clear ", cursor="hand2", command=self.clearnow, width="13",
                               font=("times new roman", 12, "bold"), bg="magenta4", fg="white")
        self.btnClear.place(x=52, y=560)

        self.btnClose = Button(window, height="3", text=" Close ", cursor="hand2", command=self.closenow, width="13",
                               font=("times new roman", 12, "bold"),
                               bg="magenta4", fg="white")
        self.btnClose.place(x=378, y=560)

        self.btnDelete = Button(window, height="2", text=" Delete ", cursor="hand2", command=self.deletenow, width="21",
                                font=("times new roman", 12, "bold"), bg="magenta4", fg="white")
        self.btnDelete.place(x=179, y=585)

        self.btnUpdate = Button(window, height="1", text=" Update ", cursor="hand2", command=self.updatenow, width="21",
                                font=("times new roman", 12, "bold"), bg="magenta4", fg="white")
        self.btnUpdate.place(x=179, y=551)

        self.view_all = Button(window, height="1", text=" View ", cursor="hand2", command=self.View_all, width="13",
                                font=("times new roman", 12, "bold"), bg="magenta4", fg="white")
        self.view_all.place(x=52, y=600)

        tree = ttk.Treeview(window)
        tree.place(x=550, y=101, width=770, height=600)
        #
        tree["columns"] = ('one', 'two', 'three', 'four', 'five')
        tree.column('#0', width=29, )
        tree.column('one', anchor='c', width=120)
        tree.column('two', anchor='c', width=120)
        tree.column('three',anchor='c', width=200, minwidth=200)
        tree.column('four',anchor='c', width=50, minwidth=100)
       # tree.column('5', width=50, minwidth=50)

        tree.heading('#0', text='ID' )
        tree.heading('one', text="Surname",)
        tree.heading('two', text="Firstname", )
        tree.heading('three',text="Email", )
        tree.heading('four', text="Sex", )
        tree.heading('five', text="State", )

        scrollbar = Scrollbar(window, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar = Scrollbar(window, orient=HORIZONTAL)
        scrollbar.pack(side=BOTTOM, fill=X)
        # textarea = Text(window, height=35, width=95, yscrollcommand=scrollbar.set)
        # textarea.pack()
        scrollbar.config(command=tree.yview)


    def View_all(self):

        # Getting Total Staff record from database
        connection = sqlite3.connect('email.db')

        view_record0 = "select * from register;"

        cursor = connection.cursor()
        cursor.execute(view_record0)

        while True:
            record = cursor.fetchone()

            if record == None:
                break
            print(record)
        connection.close()

    def Searchnow(self):
        self.clearnow()
        ## Getting Staff number from m gui form
        my_registration_table = self.staffid.get()

        ## connecting to database
        connection = sqlite3.connect('email.db')
        cursor = connection.cursor()

        count = 0
        find_qry = "select surname, firstname, gender, email, state from register where Staffid='" + str(
            my_registration_table) + "'"
        result = cursor.execute(find_qry)

        for record in result:
            self.txtsurname.insert(END, record[0])
            self.txtfirstname.insert(END, record[1])
            self.txtsex.insert(END, record[2])
            self.txtemail.insert(END, record[3])
            self.txtstate.insert(END, record[4])
            count = count + 1

        if count == 0:
            messagebox.showerror("Confirmation", "Record Does Not Exist")
        connection.close()

    def clearnow(self):
        if self.staffid.get() == "":
            messagebox.showerror("Error", "Fields Empty")
        self.txtsurname.delete(0, END)
        self.txtfirstname.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtstate.delete(0, END)
        self.txtsex.delete(0, END)

    def deletenow(self):
        ## Getting Staff number from m gui form
        my_registration_table = self.staffid.get()

        ## connecting to database
        connection = sqlite3.connect('email.db')
        try:
            cursor = connection.cursor()
            delete_qry = "delete from register where staffid ='" + str(my_registration_table) + "'"

            cursor.execute(delete_qry)
            connection.commit()

            messagebox.showinfo("Confirmation", "Customer Data Deleted Successful")
            self.clearnow()
        except:
            messagebox.showerror("Error", "Customer Data Not Deleted")
            connection.rollback()
        connection.close()

    def updatenow(self):
        ## Getting Staff number from m gui form
        staffid = self.staffid.get()
        sname = self.sname.get()
        fname = self.fname.get()
        email = self.email.get()
        sex = self.gender.get()
        state = self.state.get()

        ## connecting to database
        connection = sqlite3.connect('email.db')
        try:
            cursor = connection.cursor()
            ## Update from database table
            update_qry = "update register set surname='%s', firstname='%s', gender='%s',email='%s',state='%s' where staffid= '%s'" % (
                sname, fname, sex, email, state, staffid)

            cursor.execute(update_qry)
            connection.commit()

            messagebox.showinfo("Confirmation", "Staff Data \nUpdate Successful")
        except:
            messagebox.showerror("Error", "Data Update Not Successful")
            connection.rollback()
        connection.close()

    def closenow(self):
        result = messagebox.askyesno("Notification", "Do you want to close \n this page?")
        if result:
            window.destroy()
    #


window = Tk()
window.title("View Staff Details")
window.geometry("1350x750+0+0")
window.resizable(0, 0)
window.iconbitmap("App.ico")
#window.configure(bg="white")
app = View(window)
app.mainloop()