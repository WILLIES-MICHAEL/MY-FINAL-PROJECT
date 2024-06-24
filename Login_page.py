from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3


class Login(Frame):
    def __init__(self, master):
        super(Login, self).__init__(master)
        self.create_widgets()


    def create_widgets(self):

        ############### Image Section ################
        self.bg = ImageTk.PhotoImage(Image.open("images\\StockSnap.jpg"))
        self.label = Label(image=self.bg).pack()

        self.user_icon = ImageTk.PhotoImage(Image.open("images\\Upload Photo 2.png"))
        self.label = Label(image=self.user_icon).place(x=300, y=80)

        self.name_icon = ImageTk.PhotoImage(Image.open("images\\img_401906.png"))
        self.label = Label(image=self.name_icon).place(x=100, y=220)

        self.psw_icon = ImageTk.PhotoImage(Image.open("images\\img_401905.png"))
        self.label = Label(image=self.psw_icon).place(x=100, y=280)

        Label(window, text="WELCOME TO INTERNAL EMAIL APPLICATION \nUSERS LOGIN ", font=("times new roman", 16, "bold"),bg="magenta4",fg="white").place(x=100, y=8)


        # Username section
        self.username = Label(text="Username:",bg= "magenta4", fg= "white",font=("Arial", 18))
        self.username.place(x=140, y=220)
        self.varusername = StringVar()
        self.usernameentry = Entry(textvariable=self.varusername, width=20, font=("Arial", 20)).place(x=270, y=220)

        # Password section
        self.password = Label(text="Password:", bg="magenta4",fg="white",font=("Arial", 18)).place(x=140, y=280)
        self.varpassword = StringVar()
        self.passwordentry = Entry(textvariable=self.varpassword,width=20, show= "****", font=("Arial", 20)).place(x=270, y=280)



        # Button creation
        self.login = Button(window,text="Login",height=2, width=42, command=self.login, font=("times new roman", 14),
                            cursor="hand2",bg="magenta4",fg="white").place(x=140, y=350)
        self.exit = Button(window, text="Exit", height=1, width=10, command=self.exit,
                            font=("times new roman", 14), cursor="hand2", bg="magenta4", fg="white").place(x=580,y=407)

    def login(self):
        strusername = self.varusername.get()
        strpassword = self.varpassword.get()

        if strusername == 'Micky01' and strpassword == 'Willies01':
            messagebox.showinfo("Confirmation", 'Welcome  {0}'.format(strusername))
            window.destroy()
            from Admin_Menu import AdminMenu

        elif strusername == 'Segun ' or strpassword == 'Bayus':
            messagebox.showinfo("Confirmation", 'Welcome  {0}'.format(strusername))
            window.destroy()
            from Menu_form import MainMenu
        else:
            messagebox.showerror("Error", "Access denied,")




        db = sqlite3.connect('email.db')
        insertstr = "insert into login(username,password) values (?,?);"

        try:
            cursor = db.cursor()
            cursor.execute(insertstr,(strusername, strpassword, ))
            db.commit()
            db.rollback()
            messagebox.showinfo("Confirmation", "Login Successful ")
        except:
            #messagebox.showerror("Error", "Registration Not Successful")
            db.rollback()
        db.close()




    def exit(self):
        result = messagebox.askyesno("Notification", "Do you want to exit?")
        if result:
            window.destroy()
        else:
            pass






window = Tk()
window.title("User_Login_Page")
window.geometry("700x450+340+100")
window.resizable(0,0)
app = Login(window)
app.mainloop()
