from tkinter import *

#buttons function
def button_press(num):
	
 global et 
 et=et+str(num)
 el.set(et)
 #equal function 
def equals():
 global et
 try:
  total=str(eval(et))
  el.set(total)
  et=total
 except ZeroDivisionError:
  el.set("arithmetic error")
  et=""
 except SyntaxError:
  el.set("syntax error")
  et=""
#delete function
def clear():
 global et
 el.set("")
 et=""


         #TKinter part 
w=Tk()
w.title("calculator")
w.geometry("800x1000")

et=""
el=StringVar()
label=Label(w,bg="white",width=24,height=1,textvariable=el,font=("Arial",50))
label.pack()

frame=Frame(w)#creating frame
frame.pack()
#creatin buttons and assigning to the function
b1=Button(frame,text="1",width=20,height=10,command=lambda : button_press(1))
b1.grid(row=0,column=0)

b2=Button(frame,text="2",width=20,height=10,command=lambda :button_press(2))
b2.grid(row=0,column=1)

b3=Button(frame,text="3",width=20,height=10,command=lambda:button_press(3))
b3.grid(row=0,column=2)

b4=Button(frame,text="4",width=20,height=10,command=lambda:button_press(4))
b4.grid(row=1,column=0)

b5=Button(frame,text="5",width=20,height=10,command=lambda:button_press(5))
b5.grid(row=1,column=1)

b6=Button(frame,text="6",width=20,height=10,command=lambda:button_press(6))
b6.grid(row=1,column=2)

b7=Button(frame,text="7",width=20,height=10,command=lambda:button_press(7))
b7.grid(row=2,column=0)

b8=Button(frame,text="8",width=20,height=10,command=lambda:button_press(8))
b8.grid(row=2,column=1)

b9=Button(frame,text="9",width=20,height=10,command=lambda:button_press(9))
b9.grid(row=2,column=2)

b0=Button(frame,text="0",width=20,height=10,command=lambda:button_press(0))
b0.grid(row=3,column=0)

plus=Button(frame,text="+",width=20,height=10,command=lambda:button_press("+"))
plus.grid(row=0,column=3)

minus=Button(frame,text="-",width=20,height=10,command=lambda:button_press("-"))
minus.grid(row=1,column=3)

multiply=Button(frame,text="*",width=20,height=10,command=lambda:button_press("*"))
multiply.grid(row=2,column=3)

division=Button(frame,text="/",width=20,height=10,command=lambda:button_press("/"))
division.grid(row=3,column=3)

equal=Button(frame,text="=",width=20,height=10,command=lambda:equals())
equal.grid(row=3,column=1)

decimal=Button(frame,text=".",width=20,height=10,command=lambda:button_press("."))
decimal.grid(row=3,column=2)

clears=Button(w,text="Clear",width=20,height=10,command=lambda:clear())
clears.pack()
#finally
w.mainloop()