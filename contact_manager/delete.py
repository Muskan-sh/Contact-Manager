import tkinter.messagebox as messagebox
from tkinter import *

from contact_manager.conn import myconnection

def delete_fu(right_display: Frame):
    label1 = Label(right_display, text='Name : ', width=20, bg='azure2', font='hadriel 14')
    label1.place(x=90, y=160)
    name = Entry(right_display, font='hadriel 13')
    name.place(x=250, y=160)
    delete = Button(right_display, text='Delete Contact', width=15, font='hadriel 13',
                  relief='raised', borderwidth=3, bg='azure3',
                  command=lambda: del_fu(name))
    delete.place(x=228, y=240)


def del_fu(name):
    mycursor = myconnection.cursor()
    nm = name.get()
    if nm=='' :
        messagebox.showinfo('ERROR: ', 'Contact name is required!!!')
        return
    qry = "DELETE from contacts where Name='{}'"
    mycursor.execute((qry.format(nm)))
    myconnection.commit()

    name.delete(0, END)
    messagebox.showinfo('Task complete', 'Contact Deleted!!!')
    mycursor.close()
