from tkinter import *
import tkinter as tk
from datetime import date
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
import sqlite3




class Read(Frame):
    def __init__(self,master):
        super(Read, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):

        self.bg = ImageTk.PhotoImage(Image.open("images\\FLYER MATERRIAL 5.jpg"))
        self.label = Label(image=self.bg).place(x=50,y=50)

# def delete_message():
def delete_message():
    # my_message_table = self.varsender.get()

        ## connecting to database
    connection = sqlite3.connect('email.db')
    try:
        cursor = connection.cursor()
        delete_qry = "delete from message where staffid ='" + str(my_message_table) + "'"

        cursor.execute(delete_qry)
        connection.commit()

        messagebox.showinfo("Confirmation", "Customer Data Deleted Successful")
        #self.clearnow()
    except:
        messagebox.showerror("Error", "Customer Data Not Deleted")
        connection.rollback()
        connection.close()




def read_message():
    conn = sqlite3.connect('email.db')
    c = conn.cursor()
    c.execute("select * from message")
    message = c.fetchall()
    conn.close()


    message_text =""
    for message in message:
        text_entry.insert(END, message[1] + "\n")
        text_entry.insert(END, message[2] + "\n")
        text_entry.insert(END, message[3] + "\n")
        text_entry.insert(END, message[4] + "\n")
        text_entry.insert(END, message[5] + "\n")
        


window =Tk()
window.title("Message Display")
window.resizable(0,0)
window.geometry("650x400+350+100")

text_entry = Text(window, height=20, width=45)
text_entry.place(x=250, y=30)

delete_button =Button(window, width="10",height="1",text="Delete", bg="magenta4",fg="white",cursor="hand2",command=delete_message,font=("times new roman", 15))
delete_button.place(x=100, y=200)
read_button =Button(window,width="10",height="1", text="Read",bg="magenta4",fg="white",cursor="hand2",command=read_message,font=("times new roman", 15))
read_button.place(x=100, y=150)



window.mainloop()
