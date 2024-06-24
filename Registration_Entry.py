from tkinter import *
from PIL import ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3


class Register(Frame):
    def __init__(self,window):
        super(Register, self).__init__()
        self.window = window

        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="Images/max-bender-1YHXFeOYpN0-unsplash.jpg")
        bg=Label(self.window,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # ===Left image===
        self.left = ImageTk.PhotoImage(file="images/w2.jpeg")
        left = Label(self.window, image=self.left).place(x=120, y=100, width=400, height=500)

        #=======Register Frame=====
        frame1=Frame(self.window,bg="white")
        frame1.place(x=520,y=100,width=700,height=500)

        title=Label(frame1,text= "REGISTER HERE",font=("times new roman",20,"bold"),
                    bg="white",fg="magenta4").place(x=50,y=30)

        self.vars_id= StringVar()
        self.vars_name=StringVar()
        self.varfirst_name=StringVar()
        self.varGender=StringVar()
        self.varemail = StringVar()
        self.varstate = StringVar()
        self.varposition=StringVar()


        #---------------
        lbstaff=Label(frame1,text="Staff ID",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=300,y=70)
        self.txt_staff=Entry(frame1,textvariable=self.vars_id,font=("times new roman",15),
                             bg="lightgray").place(x=230,y=115,width=250)

        lbfirstname = Label(frame1, text="First name", font=("times new roman", 15, "bold"),
                      bg="white", fg="gray").place(x=370, y=150)
        self.txt_sname = Entry(frame1,textvariable=self.varfirst_name, font=("times new roman", 15),
                               bg="lightgray").place(x=370, y=185, width=250)

        #--------------------
        lbsname = Label(frame1, text="Surname", font=("times new roman", 15, "bold"),
                          bg="white", fg="gray").place(x=50, y=150)
        self.txtsname = Entry(frame1,textvariable=self.vars_name, font=("times new roman", 15),
                                   bg="lightgray").place(x=50, y=185, width=250)

        lbGender = Label(frame1, text="Gender", font=("times new roman", 15, "bold"),bg="white",
                       fg="gray").place(x=370, y=220)
        self.txt_Gender = Entry(frame1,textvariable=self.varGender, font=("times new roman", 15),
                                bg="lightgray").place(x=370, y=250, width=250)

        # --------------------
        lbEmail = Label(frame1, text="Email", font=("times new roman", 15, "bold"),
                          bg="white", fg="gray").place(x=50, y=220)
        self.txt_email = Entry(frame1, textvariable=self.varemail, font=("times new roman", 15),
                                   bg="lightgray").place(x=50, y=250, width=250)

        lbState = Label(frame1, text="State", font=("times new roman", 15, "bold"), bg="white",
                       fg="gray").place(x=370, y=285)
        self.txt_state = Entry(frame1, textvariable=self.varstate, font=("times new roman", 15),
                                bg="lightgray").place(x=370, y=320, width=250)

        #------------------------
        lbquestion= Label(frame1, text="Position", font=("times new roman", 15, "bold"),bg="white",
                        fg="gray").place(x=50, y=285)

        self.cmb_quest=Combobox(frame1,textvariable=self.varposition,font=("times new roman", 13),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Admin","User 1","User 2")
        self.cmb_quest.place(x=50, y=320, width=250)
        self.cmb_quest.current(0)


        #------------- BUTTON SECTION

        self.btnSave = Button(window, text=" Save Data ", width="15", cursor="hand2",height="2",
                               bg="magenta4",command=self.save_data,
                               fg="white",font=("times new roman", 12, "bold")).place(x=600, y=480)

        self.btnClose = Button(window, text=" Close ", width="15", cursor="hand2", height="2",
                           bg="magenta4", command=self.close,
                           fg="white", font=("times new roman", 12, "bold")).place(x=970, y=480)

        self.btnClear = Button(window, text=" Clear ", width="15", cursor="hand2", height="2",
                               bg="magenta4", command=self.btnClear,
                               fg="white", font=("times new roman", 12, "bold")).place(x=790, y=480)

        ######### Buttom Label Section #################
        label = Label(window, text="Already a user ?", fg="magenta4", bg="white", font=("times new roman", 12))
        label.place(x=755, y=550)

        login = Button(window, width=6, text="Log in", border=0, bg="white", cursor="hand2", fg="magenta4", command=self.login)
        login.place(x=860, y=550)


    def login(self):
        result = messagebox.askyesno("Notification", "Do you want to login?")
        if result:
            window.destroy()
            from Login_page import Login
        else:
            pass


    def close(self):
        window.destroy()

    def btnClear(self):
        if self.vars_id.get() == "":
            messagebox.showerror("Error", "Fields Empty")
        else:
            self.vars_id.set("")
            self.vars_name.set("")
            self.varfirst_name.set("")
            self.varGender.set("")
            self.varemail.set("")
            self.varstate.set("")
            self.varposition.set("")

            #messagebox.showinfo("Confirmation", "Cleared Successfully")

        strs_id = self.vars_id.get()
        strs_name = self.vars_name.get()
        strfirst_name = self.varfirst_name.get()
        strGender = self.varGender.get()
        stremail = self.varemail.get()
        strstate = self.varstate.get()
        strposition = self.varposition.get()



    def save_data(self):
        if self.vars_id.get() == "":
            messagebox.showerror("Error", "Fields are Empty")


        strs_id = self.vars_id.get()
        strs_name = self.vars_name.get()
        strfirst_name = self.varfirst_name.get()
        strGender = self.varGender.get()
        stremail = self.varemail.get()
        strstate = self.varstate.get()
        strposition = self.varposition.get()

        db = sqlite3.connect('email.db')
        insertstr = "insert into register(staffid,surname,firstname,Gender,email,state,position) values (?,?,?,?,?,?,?);"

        try:
            cursor = db.cursor()
            cursor.execute(insertstr, (strs_id,strs_name, strfirst_name, strGender,stremail,strstate, strposition))
            db.commit()
            messagebox.showinfo("Confirmation", "Registration Successful, Thank You")
        except:
            db.rollback()
        db.close()





window=Tk()
window.title("Registration")
window.geometry("1350x750+0+0")
app = Register(window)
window.mainloop()