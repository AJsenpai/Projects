from tkinter import *
from PIL import ImageTk, Image  # for image since tkinter has an outdated image system
import requests
from tkinter import ttk
import re


#######################################################
# URL shortner Window code
#######################################################
def url_shorten_window():
    global url_window
    url_window = Toplevel()
    url_window.title("Tiny URL")
    url_window.geometry("900x500")
    url_window.configure(borderwidth="1")
    url_window.configure(background="black")
    url_window.configure(highlightbackground="green")
    url_window.configure(highlightcolor="black")
    url_window.configure(cursor="arrow")

    head_lbl_url = Label(
        url_window,
        text="Lesiure Box - Tiny URL",
        font=("Arial", 32, "bold"),
        bg="black",
        fg="#47e331",
        border=1,
        relief="sunken",
        justify="center",
        width=80,
    )

    head_lbl_url.pack(side=TOP)

    url_frame = Frame(url_window, bg="black")
    url_frame.pack(pady=30)

    url_entry_lbl = Label(
        url_frame, text="Enter URL", bg="black", fg="#47e331", font=("Helvetica", 20),
    )

    global url_entry
    url_entry = Entry(url_frame, width=40, font=("Helvetica", 20))

    # candidate_lbl.grid(row=1, column=0, stick="w")
    # cadidate_count.grid(row=1, column=1, stick="w")
    url_entry_lbl.pack(side=LEFT, padx=20)
    url_entry.pack(side=RIGHT)

    global url_lbl
    url_lbl = Label(url_window)

    bottom_frame = Frame(url_window, bg="black")
    bottom_frame.pack(side=BOTTOM)
    submit = Button(
        bottom_frame,
        text="submit",
        bg="black",
        fg="#47e331",
        width=20,
        command=lambda: clear_url_lbl(),
    )
    # more_jokes_btn.grid(row=4, column=0, pady="3")
    submit.pack(pady=3)

    kill_activity_window = Button(
        bottom_frame,
        text="kill window",
        command=url_window.destroy,
        bg="black",
        fg="red",
        width=20,
    )
    # kill_joke_window.grid(row=5, column=0)
    kill_activity_window.pack(pady=10)

    url_window.mainloop()


def url_api():
    global url_entry

    # if not candidate_count.get():
    #     candidate = 1
    # else:
    #     candidate = candidate_count.get()
    print(url_entry.get())
    url = f"https://api.shrtco.de/v2/shorten?url={url_entry.get()}"
    payload = {}
    headers = {}

    # response = requests.get(url, headers=headers, data=payload)
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        print(response.status_code)
    data = response.json()
    # print(data)

    global url_lbl
    global url_window

    # textvariable=self.labvar, wraplength=250
    information = f"""Link1: {data['result']['short_link']}
    Link2: {data['result']['full_short_link']}
    Link3: {data['result']['share_link']} """

    url_lbl = Label(
        url_window,
        text=information,
        bg="black",
        fg="#47e331",
        font=("Arial", 12, "bold"),
        wraplength=700,
        # justify='center'
    )

    url_lbl.pack(pady=10)


def clear_url_lbl():
    url_lbl.pack_forget()
    url_api()


#######################################################
# Tv Shows Information Window code
#######################################################
def tv_show_window():
    global tv_show
    tv_show = Toplevel()
    tv_show.title("TV Shows")
    tv_show.geometry("800x600")
    tv_show.configure(borderwidth="1")
    tv_show.configure(background="black")
    tv_show.configure(highlightbackground="green")
    tv_show.configure(highlightcolor="black")

    head_lbl_activity = Label(
        tv_show,
        text="Lesiure Box - TV Shows Information",
        font=("Arial", 32, "bold"),
        bg="black",
        fg="#47e331",
        border=1,
        relief="sunken",
        justify="center",
        width=80,
    )

    head_lbl_activity.pack(side=TOP)

    tv_show_frame = Frame(tv_show, bg="black")
    tv_show_frame.pack(pady=10)

    show_entry_lbl = Label(
        tv_show_frame,
        text="Search Show?",
        bg="black",
        fg="#47e331",
        font=("Helvetica", 20),
    )

    global show_entry
    show_entry = Entry(tv_show_frame, width=15, font=("Helvetica", 20))

    # candidate_lbl.grid(row=1, column=0, stick="w")
    # cadidate_count.grid(row=1, column=1, stick="w")
    show_entry_lbl.pack(side=LEFT, pady=20)
    show_entry.pack(side=RIGHT)

    global tv_show_lbl
    tv_show_lbl = Label(tv_show)

    bottom_frame = Frame(tv_show, bg="black")
    bottom_frame.pack(side=BOTTOM)
    submit = Button(
        bottom_frame,
        text="submit",
        bg="black",
        fg="#47e331",
        width=20,
        command=lambda: clear_tvshow_lbl(),
    )
    # more_jokes_btn.grid(row=4, column=0, pady="3")
    submit.pack(pady=3)

    kill_activity_window = Button(
        bottom_frame,
        text="kill window",
        command=tv_show.destroy,
        bg="black",
        fg="red",
        width=20,
    )
    # kill_joke_window.grid(row=5, column=0)
    kill_activity_window.pack(pady=10)

    tv_show.mainloop()


def tvshow_api():
    global show_entry

    # if not candidate_count.get():
    #     candidate = 1
    # else:
    #     candidate = candidate_count.get()
    print(show_entry.get())
    url = f"https://api.tvmaze.com/search/shows?q={show_entry.get()}"
    payload = {}
    headers = {}

    # response = requests.get(url, headers=headers, data=payload)
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        print(response.status_code)
    data = response.json()
    # print(data)

    global tv_show_lbl
    global tv_show

    # textvariable=self.labvar, wraplength=250
    information = f"""Name: {data[0]["show"]["name"]}
    Genere: {','.join(data[0]["show"]["genres"]) or "NA"}
    Status:{data[0]["show"]["status"]}
    Type: {data[0]["show"]["type"]}\n        
    Summary:  {re.sub('<.*?>', '', data[0]["show"]["summary"])}"""

    tv_show_lbl = Label(
        tv_show,
        text=information,
        bg="black",
        fg="#47e331",
        font=("Arial", 12, "bold"),
        wraplength=700,
        # justify='center'
    )

    tv_show_lbl.pack(pady=10)


def clear_tvshow_lbl():
    tv_show_lbl.pack_forget()
    tvshow_api()


#######################################################
# Activity Suggestions Window code
#######################################################
def activity_window():
    global activity
    activity = Toplevel()
    activity.title("What To Do")
    activity.geometry("800x400")
    activity.configure(borderwidth="1")
    activity.configure(background="black")
    activity.configure(highlightbackground="green")
    activity.configure(highlightcolor="black")

    head_lbl_activity = Label(
        activity,
        text="Lesiure Box - Activity Suggestion",
        font=("Arial", 36, "bold"),
        bg="black",
        fg="#47e331",
        border=1,
        relief="sunken",
        justify="center",
        width=80,
    )

    head_lbl_activity.pack(side=TOP)

    candidate_frame = Frame(activity, bg="black")
    candidate_frame.pack(pady=20)

    candidate_lbl = Label(
        candidate_frame,
        text="how many people?",
        fg="#47e331",
        bg="black",
        font=("Helvetica", 20),
    )
    global candidate_count
    # candidate_count = Entry(candidate_frame, width=10, font=("Helvetica", 20))

    options = [1, 2, 3, 4, 5]
    candidate_count = ttk.Combobox(candidate_frame, value=options)
    candidate_count.current(0)  # what to show up as predefined
    candidate_count.pack(pady=5)

    # candidate_lbl.grid(row=1, column=0, stick="w")
    # cadidate_count.grid(row=1, column=1, stick="w")
    candidate_lbl.pack(side=LEFT, padx=10)
    candidate_count.pack(side=RIGHT)

    global activity_lbl
    activity_lbl = Label(activity)

    bottom_frame = Frame(activity, bg="black")
    bottom_frame.pack(side=BOTTOM)
    submit = Button(
        bottom_frame,
        text="Suggest",
        bg="black",
        fg="#47e331",
        width=20,
        command=lambda: clear_activity_lbl(),
    )
    # more_jokes_btn.grid(row=4, column=0, pady="3")
    submit.pack(pady=3)

    kill_activity_window = Button(
        bottom_frame,
        text="kill window",
        command=activity.destroy,
        bg="black",
        fg="red",
        width=20,
    )
    # kill_joke_window.grid(row=5, column=0)
    kill_activity_window.pack(pady=10)

    activity.mainloop()


def activity_api():
    global candidate_count

    if not candidate_count.get():
        candidate = 1
    else:
        candidate = candidate_count.get()

    url = f"http://www.boredapi.com/api/activity?participants={candidate}"
    payload = {}
    headers = {}

    # response = requests.get(url, headers=headers, data=payload)
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        print(response.status_code)
    data = response.json()

    global activity_lbl
    global acitivity

    activity_lbl = Label(
        activity,
        text=f'Activity :{data["activity"].strip()}\nType: {data["type"]}',
        bg="black",
        fg="#47e331",
        font=("Arial", 10, "bold"),
        wraplength=700,
    )

    activity_lbl.pack(pady=30)


def clear_activity_lbl():
    activity_lbl.pack_forget()
    activity_api()


#######################################################
# Joke Window code
#######################################################
def joke_window():
    global joke
    joke = Toplevel()
    joke.title("LMAO")
    joke.geometry("600x300")
    joke.configure(borderwidth="1")
    joke.configure(background="black")
    joke.configure(highlightbackground="green")
    joke.configure(highlightcolor="black")

    head_lbl_joke = Label(
        joke,
        text="Lesiure Box - Jokes :D",
        font=("Arial", 36, "bold"),
        bg="black",
        fg="#47e331",
        border=1,
        relief="sunken",
        justify="center",
        width=80,
    )

    head_lbl_joke.pack()
    # head_lbl_joke.grid(row=0, column=0)
    joke_lbl = Label(joke)

    jokes_api()

    bottom_frame = Frame(joke, bg="black")
    bottom_frame.pack(side=BOTTOM)
    more_jokes_btn = Button(
        bottom_frame,
        text="more jokes",
        bg="black",
        fg="#47e331",
        width=20,
        command=lambda: clear_joke_lbl(),
    )
    # more_jokes_btn.grid(row=4, column=0, pady="3")
    more_jokes_btn.pack(pady=3)

    kill_joke_window = Button(
        bottom_frame,
        text="kill window",
        command=joke.destroy,
        bg="black",
        fg="red",
        width=20,
    )
    # kill_joke_window.grid(row=5, column=0)
    kill_joke_window.pack(pady=10)

    joke.mainloop()


def jokes_api():
    url = "https://v2.jokeapi.dev/joke/Any"
    payload = {}
    headers = {}

    # response = requests.get(url, headers=headers, data=payload)
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        print(response.status_code)
    data = response.json()
    # data = jokes_api()

    global joke_lbl
    global joke

    if data["type"] == "twopart":
        joke_lbl = Label(
            joke,
            text=f'{data["setup"].strip()}\n{data["delivery"]}',
            bg="black",
            fg="#47e331",
            font=("Arial", 10, "bold"),
            wraplength=800,
        )

    else:
        joke_lbl = Label(
            joke,
            text=f'{data["joke"]}',
            bg="black",
            fg="#47e331",
            font=("Arial", 10, "bold"),
            wraplength=800,
        )
    # joke_lbl.grid(row=2, column=0, sticky="s", pady=10)
    joke_lbl.pack(pady=20)


def clear_joke_lbl():
    joke_lbl.pack_forget()
    jokes_api()
    # jokes_api(window)
    # lbl_name.destroy()


#######################################################
# Main Window code - Radio buttons & Submit buttons
#######################################################
root = Tk()
root.title("Lesiure Box")
root.geometry("700x400")
root.configure(borderwidth="1")
root.configure(relief="sunken")
root.configure(background="#333355")
# root.configure(highlightbackground="black")
# root.configure(highlightcolor="black")
root.configure(cursor="arrow")
root.grid_columnconfigure((0, 1), weight=1)
# adding a new icon - icontbitmap
# root.iconbitmap(r"C:\Users\Jai\Desktop\Python\Projects\flashcards\icons\ic1.ico")


def radio_action():
    if ip.get() == 1:
        activity_window()
    elif ip.get() == 2:
        url_shorten_window()
    elif ip.get() == 3:
        joke_window()
    elif ip.get() == 4:
        tv_show_window()


head_lbl = Label(
    root,
    text="Welcome to Lesiure Box",
    font=("Arial", 32, "bold"),
    bg="#681ccc",
    border=1,
    relief="sunken",
    justify="center",
    width=80,
)
head_lbl.grid(row=0, column=0)

ip = IntVar()
# v= StringVar()
ip.set(1)

# r_button1 = Radiobutton(root, text="one", variable=v, value=1)

weathr_btn = Radiobutton(
    root,
    text="Activity Suggestion",
    font=("Arial", 15, "bold"),
    variable=ip,
    value=1,
    bg="#47e331",
    width=80,
)
weathr_btn.grid(row=2, column=0, sticky="s", pady=5)

url_btn = Radiobutton(
    root,
    text="Url Shortner",
    font=("Arial", 15, "bold"),
    variable=ip,
    value=2,
    bg="#11eecc",
    width=80,
)

url_btn.grid(row=3, column=0, sticky="s", pady=5)


joke_btn = Radiobutton(
    root,
    text="Jokes",
    font=("Arial", 15, "bold"),
    variable=ip,
    value=3,
    bg="#47e331",
    width=80,
)
joke_btn.grid(row=4, column=0, sticky="s", pady=5)

exit_btn = Radiobutton(
    root,
    text="Tv Shows",
    font=("Arial", 15, "bold"),
    variable=ip,
    value=4,
    bg="#11eecc",
    width=80,
)

exit_btn.grid(row=5, column=0, sticky="s", pady=5)


# taking input
# entry = Entry(root, font=("Helvetica", 20)).grid(row=6, column=0, pady=10)


submit_btn = Button(
    root,
    text="let's Go",
    font=("Helvetica", 10),
    bg="black",
    fg="#47e331",
    width=20,
    command=radio_action,
)

kill_root_window = Button(
    root, text="kill window", command=root.destroy, bg="black", fg="red", width=22
)

submit_btn.grid(row=10, column=0, pady=10)
kill_root_window.grid(row=21, column=0)

global joke
global joke_lbl

global activity
global activity_lbl

global tv_show
global tv_show_lbl

global url_window
global url_lbl
root.mainloop()

