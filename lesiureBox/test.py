import requests
import json
from pprint import pprint
from html.parser import HTMLParser
import re
from tkinter import *


def holidays():
    url_name = "https://stackoverflow.com/questions/61677440/putting-two-buttons-next-to-each-other-with-tkinter"
    url = f"https://api.shrtco.de/v2/shorten?url={url_name}"
    payload = {}
    headers = {}

    # response = requests.get(url, headers=headers, data=payload)
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        print(response.status_code)
    data = response.json()
    print(data)

    print(data["result"]["short_link"])
    print(data["result"]["full_short_link"])
    print(data["result"]["share_link"])


# holidays()

test = "<p><b>Breaking Bad</b> follows protagonist Walter White, a chemistry teacher who lives in New Mexico with his wife and teenage son who has cerebral palsy. White is diagnosed with Stage III cancer and given a prognosis of two years left to live. With a new sense of fearlessness based on his medical prognosis, and a desire to secure his family's financial security, White chooses to enter a dangerous world of drugs and crime and ascends to power in this world. The series explores how a fatal diagnosis such as White's releases a typical man from the daily concerns and constraints of normal society and follows his transformation from mild family man to a kingpin of the drug trade.</p>"
# print(re.sub('<.*?>', '', test))


# master = Tk()

# w = Text(master, height=1, borderwidth=0)
# w.insert(1.0, "Hello, world!")
# w.pack()

# w.configure(state="disabled")

# # if tkinter is 8.5 or above you'll want the selection background
# # to appear like it does when the widget is activated
# # comment this out for older versions of Tkinter
# w.configure(inactiveselectbackground=w.cget("selectbackground"))

# mainloop()

