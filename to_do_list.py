from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
wd=19
ht=3
def add():
    box.insert(END,me.get())
    me.delete(0,END)
def delete1():
    box.delete(ANCHOR)
def cross():
    box.itemconfig(box.curselection(),fg="white")
    box.selection_clear(0,END)
def uncross():
    box.itemconfig(box.curselection(),fg="black")
    box.selection_clear(0,END)
def dcross():
    count=0
    while count<box.size():
        if box.itemcget(count,"fg")=="white":
            box.delete(box.index(count))
        count+=1

w=Tk()
w.title("To_Do_List")
w.geometry("800x800")
f=Frame(w,bg="light blue")
f.pack(padx=10)
box=Listbox(f,height=20,width=100,bg="SystemButtonFace",font=("italic",15),activestyle="none",selectbackground="grey")
box.pack(side=LEFT)
scroller=Scrollbar(f)
scroller.pack(side=RIGHT,fill=Y)
box.config(yscrollcommand=scroller)
scroller.config(command=box.yview)
la=["runing","work out","break fast","python","nap","lunch","ground","gym","dinner","sleep"]
for x in la:
    box.insert(END,x)
me=Entry(w,font=("cosolas",15))
me.pack(pady=20)
fr=Frame(w)#another frame
fr.pack(pady=20)
b1=Button(fr,text="Add A Task",command=add,font=('arial',10),bg="black",fg="white",width=wd,height=ht)
b1.grid(row=0,column=1)
b2=Button(fr,text="Delete A Task",command=delete1,font=('arial',10),bg="black",fg="white",width=wd,height=ht)
b2.grid(row=0,column=2,padx=20)
b3=Button(fr,text="Cross A Task",command=cross,font=('arial',10),bg="black",fg="white",width=wd,height=ht)
b3.grid(row=0,column=3)
b4=Button(fr,text="UnCross A Task",command=uncross,font=('arial',10),bg="black",fg="white",width=wd,height=ht)
b4.grid(row=0,column=4,padx=20)
b5=Button(fr,text="Delete Crossed Task",command=dcross,font=('arial',10),bg="black",fg="white",width=wd,height=ht)
b5.grid(row=0,column=5)



w.mainloop()

