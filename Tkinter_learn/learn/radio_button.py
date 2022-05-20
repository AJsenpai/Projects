from tkinter import *

"""
- radio buttons

"""
root = Tk()
root.title("new app")
root.geometry("400x400")


def radio():
    if v.get() == 1:
        my_label = Label(root, text="radio button 1 is chosen")
    else:
        my_label = Label(root, text="radio button 2 is chosen")
    my_label.pack(pady=30)


# radio buttons
v = IntVar()
# v= StringVar()
v.set(2)

r_button1 = Radiobutton(root, text="one", variable=v, value=1)
r_button2 = Radiobutton(root, text="two", variable=v, value=2)
r_button1.pack()
r_button2.pack()


my_button = Button(root, text="click", command=radio)
my_button.pack(pady=20)
root.mainloop()
