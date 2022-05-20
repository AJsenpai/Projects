from tkinter import *
from PIL import ImageTk, Image  # for image since tkinter has an outdated image system

"""
- creating a status bar using label
"""

root = Tk()
root.title("TEST FUN")
# root.geometry("500x500")


def fake_command():
    pass


def new_command():
    hide_menu_frames()
    current_status.set("new status")
    file_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)


def cut_command():
    hide_menu_frames()
    current_status.set("cut status")
    edit_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)


def show_menu_frames():
    file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def hide_menu_frames():
    file_frame.grid_forget()
    edit_frame.grid_forget()


# define a menu
my_menu = Menu(root)  # main menu
root.config(menu=my_menu)

# create menu items
file_menu = Menu(my_menu)  # sub menu
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create another menu
edit_menu = Menu(my_menu)  # sub menu
my_menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=cut_command)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=root.quit)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=root.quit)


# buttons
# show_button = Button(root, text="Show", command=show_menu_frames)
# hide_button = Button(root, text="Hide", command=hide_menu_frames)
# show_button.grid(row=0, column=0)
# hide_button.grid(row=0, column=1)

# File menu frame
file_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

# we can put different labels inside frame cuz frame is a different box inside main window
file_frame_label = Label(file_frame, text="File Frame", font=("Helvetica", 20))
file_frame_label.pack(padx=10, pady=10)

# Edit Menu Frame
edit_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")

# we can put different labels inside frame cuz frame is a different box inside main window
edit_frame_label = Label(edit_frame, text="Cut Frame", font=("Helvetica", 20))
edit_frame_label.pack(padx=10, pady=10)

# label for status bar

# we can create string variables and get and set them
current_status = StringVar()  # not python, Tkinter thing
current_status.set("waiting")

my_status = Label(
    root, textvariable=current_status, bd=2, relief="sunken", width=56, anchor="e"
)
my_status.grid(row=2, column=0)

root.mainloop()

