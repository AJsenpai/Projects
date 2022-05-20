from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

"""
- creating open file dialog box

"""
root = Tk()
root.title("new app")
root.geometry("400x400")


def open_file():
    # file dialog box
    root.filename = filedialog.askopenfilename(
        initialdir=r"C:\Users\Jai\Desktop\Python",
        title="open file bruh",
        filetypes=(("PNG FILES", "*.png"), ("ALL FIles", "*.*")),
    )

    # my_label = Label(root, text=root.filename).pack(pady=10)
    global my_image
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_lbl = Label(root, image=my_image, height=100, width=200).pack(pady=10)


my_btn = Button(root, text="open file", command=open_file)
my_btn.pack(pady=5)


root.mainloop()
