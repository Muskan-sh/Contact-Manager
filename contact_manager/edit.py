from tkinter import *
import tkinter.messagebox as messagebox

from contact_manager.conn import myconnection

name_s = None
num1_s = None
num2_s = None
email_s = None


def find_fu(right_display: Frame):
    label1 = Label(right_display, text='Name : ', width=20, bg='azure2', font='hadriel 14')
    label1.place(x=90, y=100)
    name = Entry(right_display, font='hadriel 13')
    name.place(x=250, y=100)
    search = Button(right_display, text='Search Contact', width=15, font='hadriel 13',
                    relief='raised', borderwidth=3, bg='azure3',
                    command=lambda: find_func(name, right_display))
    search.place(x=228, y=150)


def find_func(name, right_display):
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
    name_s.place(x=50, y=250)
    num1_s = Label(right_display, text=contact[1], font='hadriel 13')
    num1_s.place(x=50, y=300)
    if contact[2] != '':
        num2_s = Label(right_display, text=contact[2], font='hadriel 13')
        num2_s.place(x=50, y=350)
        if contact[3] != '':
            email_s = Label(right_display, text=contact[3], font='hadriel 13')
            email_s.place(x=50, y=400)
    elif contact[3] != '':
        email_s = Label(right_display, text=contact[3], font='hadriel 13')
        email_s.place(x=50, y=350)
    edit_fu(right_display, name, contact[2])


def edit_fu(right_display: Frame, name_old, n2: str):
    label1 = Label(right_display, text='Name : ', width=20, bg='azure2', font='hadriel 13')
    label1.place(x=250, y=250)
    name = Entry(right_display, font='hadriel 13')
    name.place(x=400, y=250)
    label2 = Label(right_display, text='Contact 1 :', width=20, bg='azure2', font='hadriel 13')
    label2.place(x=250, y=300)
    num1 = Entry(right_display, font='hadriel 13')
    num1.place(x=400, y=300)
    label3 = Label(right_display, text='Contact 2 :', width=20, bg='azure2', font='hadriel 13')
    label3.place(x=250, y=350)
    num2 = Entry(right_display, font='hadriel 13')
    num2.place(x=400, y=350)
    label4 = Label(right_display, text='Email : ', width=20, bg='azure2', font='hadriel 13')
    label4.place(x=250, y=400)
    email = Entry(right_display, font='hadriel 13')
    email.place(x=400, y=400)
    Edit = Button(right_display, text='Save Changes', width=15, font='hadriel 13',
                  relief='raised', borderwidth=3, bg='azure3',
                  command=lambda: save_fu(name, num1, num2, email, name_old, n2))
    Edit.place(x=350, y=450)


def save_fu(name, num1, num2, email, name_old, n2: str):

    mycursor = myconnection.cursor()
    new_nm = name.get()
    new_n1 = num1.get()
    new_n2 = num2.get()
    em = email.get()

    if new_nm == '' and new_n1 == '' and new_n2 == '' and em == '':
        messagebox.showinfo('Message : ', 'No changes made!!!')
        return
    if em != '':
        qry = "UPDATE contacts SET Email='{}' WHERE Name='{}'"
        mycursor.execute((qry.format(em, name_old.get())))
        myconnection.commit()
    if new_n1 != '' and new_n2 != '':
        if len(new_n1) < 10 or len(new_n2) < 10:
            messagebox.showinfo('ERROR: Contact not saved', 'Enter a valid phone number')
            return
        else:
            qry = "UPDATE contacts SET Number_1='{}',Number_2='{}' WHERE Name='{}'"
            mycursor.execute((qry.format(new_n1, new_n2, name_old.get())))
            myconnection.commit()
    if new_n1 != '' and new_n2 == '':
        if len(new_n1) < 10:
            messagebox.showinfo('ERROR: Contact not saved', 'Enter a valid phone number')
            return
        else:
            if n2 == '':
                qry = "UPDATE contacts SET Number_2='{}' WHERE Name='{}'"
                mycursor.execute((qry.format(new_n1, name_old.get())))
                myconnection.commit()
            else:
                qry = "UPDATE contacts SET Number_1='{}' WHERE Name='{}'"
                mycursor.execute((qry.format(new_n1, name_old.get())))
                myconnection.commit()
    if new_n2 != '' and new_n1 == '':
        if len(new_n2) < 10:
            messagebox.showinfo('ERROR: Contact not saved', 'Enter a valid phone number')
            return
        else:
            qry = "UPDATE contacts SET Number_2='{}' WHERE Name='{}'"
            mycursor.execute((qry.format(new_n2, name_old.get())))
            myconnection.commit()
    if new_nm != '':
        qry = "UPDATE contacts SET Name='{}' WHERE Name='{}'"
        mycursor.execute((qry.format(new_nm, name_old.get())))
        myconnection.commit()

    name_old.delete(0, END)
    name.delete(0, END)
    num1.delete(0, END)
    num2.delete(0, END)
    email.delete(0, END)
    messagebox.showinfo('Task complete', 'Changes saved successfully!!!')
    mycursor.close()
