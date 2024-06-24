from tkinter import *
from PIL import Image,ImageTk

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)
        self.create_widgets()
        self.window = window

        self.bg = ImageTk.PhotoImage(file="images\\WILL 2.jpg")
        bg = Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text= " You Are Welcome To our EmailApp", font=('Verdana', 30, 'bold italic'),
              fg="Black").place(x=280, y=280)

    def create_widgets(self):
        menubar = Menu(self)

        # file section
        filemenu = Menu(menubar)
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

        # Sent box section
        sentboxmenu = Menu(menubar)
        sentboxmenu.add_command(label="Open", command=self.open)
        menubar.add_cascade(label="Sent box", menu=sentboxmenu)


        window.config(menu=menubar)

    def new(self):
        window.destroy()
        from Compose import EmailApp

    def exit(self):
        window.destroy()
        #from Login_page import Login

    def close(self):
        window.destroy()
        from Login_page import Login

    def inbox(self):
        window.destroy()

    def sentbox(self):
        window.destroy()

    def open(self):
        window.destroy()


window = Tk()
window.title("User_Menu")
window.geometry("1350x750+0+0")
window.resizable(0, 0)
app = MainMenu(window)
app.mainloop()
