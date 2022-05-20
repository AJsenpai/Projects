from tkinter import *
from tkinter import ttk  # has better looking widgets

"""
- combo boxes

"""
root = Tk()
root.title("new app")
root.geometry("400x400")


def select():
    my_label = Label(root, text=my_como.get())
    my_label.pack(padx=10)


# combo boxes
options = ["jupiter", "mars", "earth", "mercury", "saturn", "uranus", "neptune" "sun"]
my_como = ttk.Combobox(root, value=options)
my_como.current(0)  # what to show up as predefined
my_como.pack(pady=5)

popup_button = Button(root, text="click", command=select)
popup_button.pack(pady=20)
root.mainloop()
