from tkinter import *
import time
from datetime import datetime as dt

window=Tk()
hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
def list_making_blocking():
    website_list=link.get().split(" ")
    print(website_list)

    while True:
       if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
           print("Working hrs. ")
           with open(hosts_path, 'r+') as f:
                content= f.read()
                for i in website_list:
                   if i in content:
                       pass
                   else: f.write("\n"+redirect+" "+ i+"\n")

       else:
           print("Be in working hrs. ")
           with open(hosts_path,'r+') as f:
                 content=f.readlines()
                 f.seek(0)
                 for i in content:
                     if not any(j in i for j in website_list):
                        f.write(i)
                 f.truncate()


       time.sleep(5)

link=StringVar()
e1=Entry(window, textvariable=link)
e1.grid(row=0, column=0)

b1=Button(window, text="Block", command=list_making_blocking)
b1.grid(row=0,column=1)

window.mainloop()
