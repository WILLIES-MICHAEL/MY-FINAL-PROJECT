from tkinter import *
from PIL import Image,ImageTk

class AdminMenu(Frame):
    def __init__(self, master):
        super(AdminMenu, self).__init__(master)
        self.create_widgets()
        self.window = window

        self.bg = ImageTk.PhotoImage(file="images\\WILL 1.jpg")
        bg = Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text= "You are Welcome Back", font=('Verdana', 40, 'bold italic'),
              fg="Black").place(x=360, y=300)

    def create_widgets(self):
        menubar = Menu(self)

        # file section
        filemenu = Menu(menubar)
        filemenu.add_command(label="Create", command=self.create)
        filemenu.add_command(label="Close", command=self.close)
        filemenu.add_command(label="Exit",command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Inbox section
        Inboxmenu = Menu(menubar)
        Inboxmenu.add_command(label="Open", command=self.open)
        menubar.add_cascade(label="Inbox", menu=Inboxmenu)

        # message section
        compmenu = Menu(menubar)
        compmenu.add_command(label="New", command=self.new)
        menubar.add_cascade(label="Compose", menu=compmenu)

        # Sentbox section
        sentmenu = Menu(menubar)
        sentmenu.add_command(label="Open", command=self.sent)
        menubar.add_cascade(label="Sent ", menu=sentmenu)

        # Others section
        othersmenu = Menu(menubar)
        othersmenu.add_command(label="Staff details", command=self.staff_details)
        menubar.add_cascade(label="Others", menu=othersmenu)


        window.config(menu=menubar)

    def new(self):
        window.destroy()
        from Compose import EmailApp

    def exit(self):
        window.destroy()

    def create(self):
        window.destroy()
        from Registration_Entry import Register

    def staff_details(self):
        window.destroy()
        from view_staff_records import View

        # import sqlite31
        #
        # connection = sqlite3.connect('USERS REGISTER.db')
        #
        # view_record0 = "select * from register;"
        #
        # cursor = connection.cursor()
        # cursor.execute(view_record0)
        #
        # while True:
        #     record = cursor.fetchone()
        #
        #     if record == None:
        #         break
        #     print(record)
        # connection.close()
        # window.destroy()

    def close(self):
        window.destroy()
        from Login_page import Login

    def inbox(self):
        window.destroy()

    def sent(self):
        window.destroy()

    def open(self):
        window.destroy()



window = Tk()
window.title("Admin_Menu")
window.geometry("1350x750+0+0")
window.resizable(0, 0)
window.iconbitmap("App.ico")
app = AdminMenu(window)
app.mainloop()
