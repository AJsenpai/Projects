from tkinter import *
from tkinter import messagebox  # have to import it

"""
- pop up  boxes

"""
root = Tk()
root.title("new app")
root.geometry("400x400")


def popup():
    # messagebox.showinfo("Popup Title", "This is a  pop up message")
    # messagebox.showwarning("Popup Title", "wait stop right there") # returns ok
    # messagebox.showerror('Pop up Title', 'TF you are doing') # return ok
    # messagebox.askquestion('Pop up Title', 'are you mad') # return yes no
    # messagebox.askokcancel('Pop up Title', 'proceed')
    # messagebox.askyesno('Pop up Title', 'proceed') # return 0 and 1

    response = messagebox.askyesnocancel("Pop up Title", "proceed")
    my_label = Label(root, text=response).pack()


# pop up boxes
# shows info, showwarning, showerror, askquestion, askcancel, askyesno


popup_button = Button(root, text="click", command=popup)
popup_button.pack(pady=20)
root.mainloop()
