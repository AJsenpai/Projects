from tkinter import *

""" about labels """

root = Tk()
root.title("first project")
root.geometry("400x400")


# creating a label
# two types to add label - 1. Pack it , 2. Grid system (more meaningful)
# pack will change shapes according to things you put inside of it
# can also use hexcode to change color
"""
my_label = Label(root, text="label it", fg="orange", bg="black", font=("Helvtica", 32))
my_label.pack()
"""
# relief = flat (default), groove, raised, ridge, solid, or sunken
# state = disabled/ normal
# height=200, width=300
"""
my_label2 = Label(
    root,
    text="this comes below the first label",
    relief="ridge",
    font=("ariel", 15),
    state="disabled",
    height=5,
)
my_label2.pack(pady=50)  # pad-y
"""


# grid system - think in terms of rows and columns for each widget or label
my_label = Label(
    root, text="first label", fg="orange", bg="black", font=("Helvtica", 32)
)
my_label.grid(row=0, column=0, columnspan=3)  # rowspan, columnspan

my_label2 = Label(root, text="Second", font=("ariel", 15), state="disabled")
# sticky - think in terms of East, West, North, South
my_label2.grid(row=1, column=1, sticky=E)

my_label3 = Label(root, text="Third", font=("ariel", 15), state="disabled")
# sticky - think in terms of East, West, North, South
my_label3.grid(row=2, column=2)

root.mainloop()  # root window or our first main window

