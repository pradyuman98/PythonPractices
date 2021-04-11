from tkinter import *
import json
from difflib import get_close_matches

window=Tk()
data=json.load(open("data.json"))

def Meaning():
    w=word.get()
    if w in data:
         output= data[w]
    else:
        w=w.lower()
        if w in data:
            output=data[w]

    if type(output)== list:
        for item in output:
            t1.insert(END, "-"+item+"\n")

    else:
         t1.insert(END, output)


word=StringVar()
e1=Entry(window, textvariable=word)
e1.grid(row=0, column=0)

b1=Button(window, text="Find", command=Meaning)
b1.grid(row=0,column=1)

t1=Text(window)
t1.grid(row=1,column=0)

window.mainloop()
