from tkinter import *
from PIL import ImageTk, Image  # for image since tkinter has an outdated image system

"""
- menus, Frame(box) in tkinter
"""

root = Tk()
root.title("TEST FUN")
root.geometry("500x500")


def fake_command():
    pass


def show():
    my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def hide():
    my_frame.grid_forget()


# define a menu
my_menu = Menu(root)  # main menu
root.config(menu=my_menu)

# create menu items
file_menu = Menu(my_menu)  # sub menu
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=fake_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create another menu
edit_menu = Menu(my_menu)  # sub menu
my_menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="New", command=fake_command)
edit_menu.add_separator()
edit_menu.add_command(label="Exit", command=root.quit)


# buttons
show_button = Button(root, text="Show", command=show)
hide_button = Button(root, text="Hide", command=hide)

show_button.grid(row=0, column=0)
hide_button.grid(row=0, column=1)

# creating a frame
my_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

# we can put different labels inside frame cuz frame is a different box inside main window
frame_label = Label(my_frame, text="Hellu world!", font=("Helvetica", 20))
frame_label.pack(padx=10, pady=10)


root.mainloop()

