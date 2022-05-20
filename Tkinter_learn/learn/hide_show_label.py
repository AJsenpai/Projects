from tkinter import *
from PIL import ImageTk, Image  # for image since tkinter has an outdated image system

"""
- hide or show somthing on the window
"""

root = Tk()
root.title("TEST FUN")
root.geometry("500x500")


def clicked():
    # e.get() - to get the input entered into the box
    global label_clicked
    label_clicked = Label(root, text=e.get() * 3)  # can do string manipulation
    label_clicked.pack()


my_label = Label(root, text="SuperMario", fg="red", bg="black", font=("Helvetica", 20))
my_label.pack()

# hide funtion
# 2 ways to do this
# 1. we can remove it temporary - label_name.pack_forget()
# 2. we can remove it permanently = label_name.destroy()
# we can use label_name.grid_forget (if we are using grid instead of pack)


def hide():
    label_clicked.pack_forget()
    # label_clicked.destroy()


# show funtion
def show():
    label_clicked.pack()


# taking input
e = Entry(root, font=("Helvetica", 20))
e.pack(pady=20)

button = Button(root, text="Push", command=clicked)
button.pack(pady=20)

# hide and show
hide_button = Button(root, text="hide", command=hide)
hide_button.pack(pady=20)

show_button = Button(root, text="show", command=show)
show_button.pack(pady=20)


root.mainloop()

