from tkinter import *
from contact_manager.conn import close
from contact_manager.add import add_fu
from contact_manager.all_conatcts import all_contacts_fu
from contact_manager.edit import find_fu
from contact_manager.delete import delete_fu
from contact_manager.search import search_fu

left_display_width = 200
right_display_width = 650
total_height = 550
button_width = 20
last_call = None
old_frame = None

# Main tkinter window
root = Tk()
root.geometry("850x550")
root.resizable(False, False)
root.title('Contacts Manager')

# Left display
left_display = Frame(root, width=left_display_width, height=total_height, bg="azure3")
left_display.pack(expand=False, fill="both", side="left", anchor=NW)


# Function which manage root
def display(root, current_call: str):
    global last_call
    global old_frame
    if last_call == current_call:
        return
    if old_frame is not None:
        old_frame.destroy()
    new_frame = Frame(root, width=right_display_width, height=total_height, bg="azure2")
    new_frame.pack(expand=False, fill="both", side="right")
    old_frame = new_frame
    if current_call == 'add':
        last_call = 'add'
        add_fu(new_frame)
    if current_call == 'all_contacts':
        last_call = 'all_contacts'
        all_contacts_fu(new_frame)
    if current_call == 'delete':
        last_call = 'delete'
        delete_fu(new_frame)
    if current_call == 'edit':
        last_call = 'edit'
        find_fu(new_frame)
    if current_call == 'search':
        last_call = 'search'
        search_fu(new_frame)


# Buttons in left display

options = StringVar(value='all_contacts')
display(root, 'all_contacts')
all_contacts = Radiobutton(left_display, text='All Contacts', width=button_width, font='hadriel 13',
                           relief='raised', borderwidth=3, activebackground="azure4",
                           variable=options, value='all_contacts', indicatoron=False,
                           command=lambda: display(root, 'all_contacts'))
all_contacts.grid(row=0)
search = Radiobutton(left_display, text='Search', width=button_width, font='hadriel 13',
                     relief='raised', borderwidth=3, activebackground="azure4",
                     variable=options, value='search', indicatoron=False,
                     command=lambda: display(root, 'search'))
search.grid(row=1)
add = Radiobutton(left_display, text='Add', width=button_width, font='hadriel 13',
                  relief='raised', borderwidth=3, activebackground="azure4",
                  variable=options, value='add', indicatoron=False,
                  command=lambda: display(root, 'add'))
add.grid(row=2)
edit = Radiobutton(left_display, text='Edit', width=button_width, font='hadriel 13',
                   relief='raised', borderwidth=3, activebackground="azure4",
                   variable=options, value='edit', indicatoron=False,
                   command=lambda: display(root, 'edit'))
edit.grid(row=3)
delete = Radiobutton(left_display, text='Delete', width=button_width, font='hadriel 13',
                     relief='raised', borderwidth=3, activebackground="azure4",
                     variable=options, value='delete', indicatoron=False,
                     command=lambda: display(root, 'delete'))
delete.grid(row=4)

root.mainloop()
close()
