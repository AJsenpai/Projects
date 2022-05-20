from tkinter import *
from PIL import ImageTk, Image  # for image since tkinter has an outdated image system

""" 
- adding an image 
- changing top icon in menu bas
- taking input from user
"""

root = Tk()
root.title("TEST FUN")
root.geometry("500x500")

# adding a new icon - icontbitmap
root.iconbitmap(r"C:\Users\Jai\Desktop\Python\Projects\flashcards\icons\ic1.ico")


def clicked():
    # e.get() - to get the input entered into the box
    label = Label(root, text=e.get() * 3)  # can do string manipulation
    label.pack()


my_label = Label(root, text="SuperMario", fg="red", bg="black", font=("Helvetica", 20))
my_label.pack()

# add Images
my_image = ImageTk.PhotoImage(
    Image.open(r"C:\Users\Jai\Desktop\Python\Projects\flashcards\images\fruit.png")
)
image_label = Label(image=my_image, width=200, height=200)
image_label.pack()


# taking input
e = Entry(root, font=("Helvetica", 20))
e.pack(pady=20)

button = Button(root, text="Push", command=clicked)
button.pack(pady=20)


root.mainloop()

