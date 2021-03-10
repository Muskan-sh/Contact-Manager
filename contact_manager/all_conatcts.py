import pymysql as connector
from tkinter import *
from tkinter import ttk

from contact_manager.conn import myconnection


def all_contacts_fu(right_display: Frame):
    mycursor = myconnection.cursor()
    mycursor.execute('SELECT * FROM contacts ORDER BY Name ')
    data = mycursor.fetchall()

    tree = ttk.Treeview(right_display, height=400, columns=(1, 2, 3, 4), show="headings")
    tree.pack(side='left', fill='x')
    style = ttk.Style()
    # Modify the font of the body
    style.configure("Treeview", highlightthickness=5, font=('Calibri', 13))
    # Modify the font of the headings
    style.configure("Treeview.Heading", font=('Calibri', 15, 'bold'))

    tree.heading(1, text="Name", anchor=W)
    tree.heading(2, text="Number 1", anchor=W)
    tree.heading(3, text="Number 2", anchor=W)
    tree.heading(4, text="Email", anchor=W)

    tree.column(1, width=170)
    tree.column(2, width=120)
    tree.column(3, width=120)
    tree.column(4, width=220)

    scroll1 = ttk.Scrollbar(right_display, orient="vertical", command=tree.yview)
    scroll1.pack(side='right', fill='y')
    # scroll2 = ttk.Scrollbar(right_display, orient="horizontal", command=tree.xview)
    # scroll2.pack(side='bottom', fill='x')

    tree.configure(yscrollcommand=scroll1.set)
    #tree.configure(xscrollcommand=scroll2.set)
    for val in data:
        tree.insert('', 'end', values=(val[0], val[1], val[2],val[3]))

    mycursor.close()
