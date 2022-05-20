from tkinter import *

""" grid forget """

root = Tk()
root.title("main window")
root.geometry("500x500")


submit_lbl = Label(root)
# created a clicked function for button
def submit():
    global submit_lbl
    clear()
    submit_lbl = Label(root, text="Hello " + e.get())
    submit_lbl.grid(row=3, column=0)


def clear():
    submit_lbl.grid_forget()
    # submit_lbl.destory()


# creating labels
my_label = Label(root, text="Enter your name")
my_label.grid(row=0, column=0)

# input entry
e = Entry(root)
e.grid(row=1, column=0)

mybutton = Button(root, text="Submit", command=submit)
mybutton.grid(row=2, column=0)

clear_btn = Button(root, text="Clear", command=clear)
clear_btn.grid(row=2, column=1)

root.mainloop()
