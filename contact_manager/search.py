import tkinter.messagebox as messagebox
from tkinter import *

from contact_manager.conn import myconnection

name_s = None
num1_s = None
num2_s = None
email_s = None


def search_fu(right_display: Frame):
    label1 = Label(right_display, text='Name : ', width=20, bg='azure2', font='hadriel 14')
    label1.place(x=90, y=140)
    name = Entry(right_display, font='hadriel 13')
    name.place(x=250, y=140)
    search = Button(right_display, text='Search Contact', width=15, font='hadriel 13',
                    relief='raised', borderwidth=3, bg='azure3',
                    command=lambda: search_func(name, right_display))
    search.place(x=228, y=220)


def search_func(name, right_display):
    global num2_s
    global num1_s
    global email_s
    global name_s
    if name_s is not None:
        name_s.destroy()
    if num1_s is not None:
        num1_s.destroy()
    if num2_s is not None:
        num2_s.destroy()
    if email_s is not None:
        email_s.destroy()
    mycursor = myconnection.cursor()
    nm = name.get()
    if nm == '':
        messagebox.showinfo('ERROR: ', 'Contact name is required!!!')
        return
    # to check if contact exists in list or not
    mycursor.execute("SELECT name from contacts")
    data = mycursor.fetchall()
    name_list = [j.lower() for i in data for j in i]
    if nm.lower() not in name_list:
        messagebox.showinfo('ERROR: ', 'This contact does not exist!!!')
        return
    qry = "SELECT * from contacts where name='{}'"
    mycursor.execute((qry.format(nm)))
    contact = mycursor.fetchone()
    myconnection.commit()
    name_s = Label(right_display, text=contact[0], font='hadriel 13')
    name_s.place(x=240, y=330)
    num1_s = Label(right_display, text=contact[1], font='hadriel 13')
    num1_s.place(x=240, y=380)
    if contact[2] != '':
        num2_s = Label(right_display, text=contact[2], font='hadriel 13')
        num2_s.place(x=240, y=430)
        if contact[3] != '':
            email_s = Label(right_display, text=contact[3], font='hadriel 13')
            email_s.place(x=240, y=480)
    elif contact[3] != '':
        email_s = Label(right_display, text=contact[3], font='hadriel 13')
        email_s.place(x=240, y=430)

    name.delete(0, END)

    mycursor.close()
