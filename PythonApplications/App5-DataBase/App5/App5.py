from tkinter import *
import Back

def get_selected(event):
    global selected_tuple
    index=list1.curselection()
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])

    e2.delete(0,END)
    e2.insert(END, selected_tuple[2])

    e3.delete(0,END)
    e3.insert(END, selected_tuple[3])

    e4.delete(0,END)
    e4.insert(END, selected_tuple[4])


def ViewAll():
    list1.delete(0, END)
    for row in Back.View():
       list1.insert(END, row)

def Search():
    list1.delete(0, END)
    for row in Back.Search(ent1.get(),ent2.get(),ent3.get(), ent4.get()):
       list1.insert(END, row)

def Insert():
    Back.Insert(ent1.get(),ent2.get(),ent3.get(), ent4.get())
    list1.delete(0, END)
    list1.insert(END, "ModelName:- "+ent1.get(),"Company:- "+ent2.get(),"Year:- "+ent3.get(),"ChasisNo:- "+ent4.get())

def Delete():
    Back.Delete(selected_tuple[0])

def Update():
    Back.Update(selected_tuple[0], ent1.get(), ent2.get(), ent3.get(), ent4.get())
    print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])

window=Tk()
window.wm_title("Cars24")

l1=Label(window, text="ModelName")
l1.grid(row=0, column=0)

l2=Label(window, text="Company")
l2.grid(row=0, column=2)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, text="ChasisNo.")
l4.grid(row=1, column=2)

ent1=StringVar()
e1=Entry(window, textvariable=ent1)
e1.grid(row=0, column=1)

ent2=StringVar()
e2=Entry(window, textvariable=ent2)
e2.grid(row=0, column=3)

ent3=StringVar()
e3=Entry(window, textvariable=ent3)
e3.grid(row=1, column=1)

ent4=StringVar()
e4=Entry(window, textvariable=ent4)
e4.grid(row=1, column=3)

sb=Scrollbar(window)
sb.grid(row=4, column=2)

list1=Listbox(window, height=10, width=40, yscrollcommand = sb.set )
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb.config(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected)

b1=Button(window, text="View All", width=12, command=ViewAll)
b1.grid(row=2, column=3)

b2=Button(window, text="Search", width=12, command=Search)
b2.grid(row=3, column=3)

b3=Button(window, text="Add", width=12, command=Insert)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12, command=Update)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12, command=Delete)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
