import tkinter.messagebox as messagebox
from tkinter import *

from contact_manager.conn import myconnection


def add_fu(right_display: Frame):
    label1 = Label(right_display, text='Name : ', width=20, bg='azure2', font='hadriel 13')
    label1.place(x=93, y=100)
    name = Entry(right_display, font='hadriel 13')
    name.place(x=250, y=100)
    label2 = Label(right_display, text='Contact 1 :', width=20, bg='azure2', font='hadriel 13')
    label2.place(x=100, y=150)
    num1 = Entry(right_display, font='hadriel 13')
    num1.place(x=250, y=150)
    label3 = Label(right_display, text='Contact 2 :', width=20, bg='azure2', font='hadriel 13')
    label3.place(x=100, y=200)
    num2 = Entry(right_display, font='hadriel 13')
    num2.place(x=250, y=200)
    label4 = Label(right_display, text='Email : ', width=20, bg='azure2', font='hadriel 13')
    label4.place(x=92, y=250)
    email = Entry(right_display, font='hadriel 13')
    email.place(x=250, y=250)
    save = Button(right_display, text='Save', width=10, font='hadriel 13',
                  relief='raised', borderwidth=3, bg='azure3',
                  command=lambda: save_fu(name, num1, num2, email))
    save.place(x=230, y=300)


def save_fu(name, num1, num2, email):
    mycursor = myconnection.cursor()
    nm = name.get()
    n1 = num1.get()
    n2 = num2.get()
    em = email.get()

    if nm == '' and n1 == '' and n2 == '':
        messagebox.showinfo('ERROR: Contact not saved', 'Contact Name and a phone number is required')
        return
    if nm == '':
        messagebox.showinfo('ERROR: Contact not saved', 'Contact Name is required')
        return
    if n1 == '' and n2 == '':
        messagebox.showinfo('ERROR: Contact not saved', 'Enter at least one phone number')
        return
    if (n1 != '' and len(n1) < 10) or (n2 != '' and len(n2) < 10):
        messagebox.showinfo('ERROR: Contact not saved', 'Enter a valid phone number')
        return
    if n1=='' and n2!='':
        qry = "insert into contacts values('{}','{}','{}','{}')"
        mycursor.execute((qry.format(nm, n2, n1, em)))
    else:
        qry = "insert into contacts values('{}','{}','{}','{}')"
        mycursor.execute((qry.format(nm, n1, n2, em)))

    myconnection.commit()


    name.delete(0, END)
    num1.delete(0, END)
    num2.delete(0, END)
    email.delete(0, END)
    messagebox.showinfo('Task complete', 'Contact saved successfully!!!')
    mycursor.close()
