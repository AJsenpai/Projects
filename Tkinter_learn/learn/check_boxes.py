from tkinter import *

"""
- check boxex

"""
root = Tk()
root.title("new app")
root.geometry("400x400")


def addons():
    if v1.get():
        my_label1 = Label(root, text=v1.get())
    if v2.get():
        my_label2 = Label(root, text=v2.get())
    else:
        my_label1 = Label(root, text=v1.get())
        my_label2 = Label(root, text=v2.get())
    my_label1.pack()
    my_label2.pack()


# check boxes
v1 = StringVar()
v2 = StringVar()


check_box1 = Checkbutton(
    root, text="one", variable=v1, onvalue="mustard sauce", offvalue="no mustard sauce"
)
check_box2 = Checkbutton(
    root, text="two", variable=v2, onvalue="buns", offvalue="nobuns"
)
check_box1.deselect()
check_box2.deselect()
check_box1.pack()
check_box2.pack()


my_button = Button(root, text="click", command=addons)
my_button.pack(pady=20)
root.mainloop()
