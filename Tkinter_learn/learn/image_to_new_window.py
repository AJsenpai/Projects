from tkinter import *
from PIL import ImageTk, Image

"""
- adding images to new window

"""
root = Tk()
root.title("new app")
root.geometry("400x400")


def newwindow():
    new = Toplevel()
    new.title("tiny window")
    new.geometry("500x700")

    my_label = Label(new, text="tiny widnow says hello", bg="blue", fg="white")
    my_label.pack()

    my_image = ImageTk.PhotoImage(
        Image.open(r"C:\Users\Jai\Desktop\Python\Projects\flashcards\learn\fruit.png")
    )
    my_image_lbl = Label(new, image=my_image, width=300, height=400)
    my_image_lbl.pack(pady=5)

    destroy_button = Button(new, text="kill window", command=new.destroy).pack()

    # minimize original window
    # hide_btn = Button(new, text="Hide main window", command=root.iconify)
    # show_btn = Button(new, text="show main window", command=root.deiconify)

    # withdraw original window
    hide_btn = Button(new, text="Hide main window", command=root.withdraw)
    show_btn = Button(new, text="show main window", command=root.deiconify)
    kill_original = Button(new, text="kill main window", command=root.destroy).pack()

    hide_btn.pack(pady=5)
    show_btn.pack(pady=5)

    # if you don't inclue this and close the main wiundow
    # tiny widnow will still ramain open
    new.mainloop()


popup_button = Button(root, text="click", command=newwindow)
popup_button.pack(pady=20)
root.mainloop()
