from tkinter import *

""" about buttons """

root = Tk()
root.title("main window")
root.geometry("500x500")

# created a clicked function for button
def clicked():
    mylabel = Label(root, text="stop pushing my buttons")
    # if you don't specify row and col it keeps picking the
    # next row and same col, when you keep clicking the button
    mylabel.grid()


def clicked2(n):
    mylabel = Label(root, text="stop" * n)
    mylabel.grid()


# creating labels
my_label = Label(
    root, text="first label", fg="orange", bg="black", font=("Helvtica", 32)
)
my_label.grid(row=0, column=0)

# created a button

# when you call a function it doesnt require parenthesis for function
# without parameters, if you want to pass parameters you need to use lambda
mybutton = Button(root, text="click me!", bg="red", command=clicked)
mybutton.grid(row=1, pady=20)

# input entry
# can change the height by changing font and its size
e = Entry(root, width=10, font=("Helvetica", 20))
e.grid(pady=20)

mybutton2 = Button(root, text="don't click me!", bg="red", command=lambda: clicked2(3))
mybutton2.grid(row=3, pady=20)


root.mainloop()
