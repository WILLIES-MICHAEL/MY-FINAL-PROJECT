from tkinter import *
from datetime import date
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
import sqlite3



class EmailApp(Frame):
    def __init__(self, master):
        super(EmailApp, self).__init__(master)
        self.create_widgets()


    def create_widgets(self):
        self.varsender = StringVar()
        self.var_receiver = StringVar()
        self.varsubject = StringVar()
        self.varmessage = StringVar()


        self.bg = ImageTk.PhotoImage(Image.open("images\\FLYER MATERRIAL 2.jpg"))
        self.label = Label(image=self.bg).pack()

        # Email Section
        self.lbsender = Label(window, text="Sender: ", bg="white", fg="Black", font=("times new roman", 18))
        self.lbsender.place(x=18, y=35)
        self.txtsender = Entry(textvariable=self.varsender, width=25, font=("times new roman", 20))
        self.txtsender.place(x=130, y=33)


        # To/position Section
        self.cmdreceiver = Label(window, text="Receiver: ",bg= "white",fg="Black", font=("times new roman", 18))
        self.cmdreceiver.place(x=18, y=80)
        self.cmdreceiver = Combobox(window,textvariable=self.var_receiver, font=("times new roman", 19), cursor="hand2",
                                    state="readonly", justify=CENTER)
        self.cmdreceiver['values'] = ("", "Admin", "User 1", "User 2")
        self.cmdreceiver.place(x=130, y=80, width=356)
        self.cmdreceiver.current(0)

        # Subject Section
        self.lbsubject = Label(window, text="Subject: ", bg="white", fg="Black", font=("times new roman", 18))
        self.lbsubject.place(x=18, y=130)
        self.txtsubject = Entry(textvariable=self.varsubject, width=25, font=("times new roman", 20))
        self.txtsubject.place(x=130, y=130)

        # Text box entry
        self.message = Text(window, width=64, height=15)
        self.message.place(x=18, y=200)

        # Button creation
        self.sendbtn = Button(window, width="9",height="1",text=" Send ", bg="magenta4",fg="white",cursor="hand2",command=self.sendmessage,font=("times new roman", 15))
        self.sendbtn.place(x=230, y=447)

        self.Btnclear = Button(window, width="9",height="1", text=" Clear ", bg="magenta4",fg="white", cursor="hand2", command=self.clearnow, font=("times new roman", 15))
        self.Btnclear.place(x=18, y=447)
        self.exitbtn = Button(window, width="9",height="1", text=" Exit ", bg="magenta4",fg="white", cursor="hand2",command=self.exitnow, font=("times new roman", 15))
        self.exitbtn.place(x=424, y=447)

        Date = StringVar()

        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        # date_entry = Entry(window, textvariable=Date, width=15, font="arial 15")
        # date_entry.place(x=650, y=150)
        Date.set(d1)

    def clearnow(self):
        if self.varsender.get() =="":
            messagebox.showerror("Error", "Fields Empty")
        else:
            self.varsender.set("")
            self.var_receiver.set("")
            self.varsubject.set("")
            self.varmessage.set("")

        strsender = self.varsender.get()
        str_receiver = self.var_receiver.get()
        strsubject = self.varsubject.get()
        strmessage = self.varmessage.get()

    def sendmessage(self):
        if self.varsender.get == '' or self.var_receiver.get == '' or self.varsubject.get == '' or self.varmessage.get == '':
            messagebox.showerror("Error", "All Fields Are Required")
#            window.destroy()

        strsender = self.varsender.get()
        str_receiver = self.var_receiver.get()
        strsubject = self.varsubject.get()
        strmessage = self.varmessage.get()
        strdate="25-04-2024"

        conn = sqlite3.connect("email.db")
        insertstr = "insert into message(sender, receiver, subject, message, messagedate) VALUES(?,?,?,?,?)"

        try:
            c = conn.cursor()
            c.execute(insertstr, (strsender, str_receiver, strsubject, strmessage,strdate))
            conn.commit()
            messagebox.showinfo("Confirmation", "Message sent ")
        except:
            messagebox.showerror("Error", "Message Not Sent")
            conn.rollback()
        conn.close()


    def exitnow(self):
        result = messagebox.askyesno("Notification", "Do you want to exit?")
        if result:
            window.destroy()
        else:
            pass



window = Tk()
window.title("Compose_Form")
window.geometry("550x500+400+50")
window.iconbitmap("App.ico")
window.resizable(0, 0)
app = EmailApp(window)
window.mainloop()