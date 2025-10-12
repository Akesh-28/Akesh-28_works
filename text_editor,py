import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def new():
    w.title("untitled")
    t_area.delete(1.0,END)

def change_color():
    color = colorchooser.askcolor(title="Pick a color...")
    if color[1]:
        t_area.config(fg=color[1])

def change_font(*args):
    t_area.config(font=(font_name.get(), font_size.get()))
    
def open() :
    
 file=askopenfilename(defaultextension=".txt",file=[("All Files","*.*"),("Text Documents","*.txt")])
 try:
  w.title(os.path.basename(file))
  t_area.delete(1.0,END)
  file=open(file,"r")
  t_area.insert(1.0,file.read())
 except Exception:
  print("file couldn't open")
 finally:
  file.close()
def cut() :
 t_area.event_generate("<<cut>>")
def copy() :
 t_area.event_generate("<<copy>>")
def paste() :
 t_area.event_generate("<<paste>>")
	
def save() :
 file=filedialog.asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents",".txt")])
 if file is None:
   return 
 else:
   try:
    w.title(os.path.basename(file))
    file=open(file,"w")
    file.write(t_area.get(1.0,END))
   except Exception as e:
    print("the file cant be save",e)
   
def exit() :
 w.destroy()
def about():
 showinfo("about this program","this is a program written by you ")
# Main window
w = Tk()
w.title("Text Editor Program")

file = None
w_width = 500
w_height = 500
s_width = w.winfo_screenwidth()
s_height = w.winfo_screenheight()
x = int((s_width / 2) - (w_width / 2))
y = int((s_height / 2) - (w_height / 2))
w.geometry(f"{w_width}x{w_height}+{x}+{y}")

# Font controls
font_name = StringVar(w)
font_name.set("Arial")
font_size = StringVar(w)
font_size.set("25")

# Text area and scrollbar
t_area = Text(w, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(w, command=t_area.yview)
t_area.config(yscrollcommand=scroll_bar.set)

w.grid_rowconfigure(0, weight=1)
w.grid_columnconfigure(0, weight=1)

t_area.grid(row=0, column=0, sticky=N+S+E+W)
scroll_bar.grid(row=0, column=1, sticky=N+S)

# Controls frame
frame = Frame(w)
frame.grid(row=1, column=0, columnspan=2)

c_button = Button(frame, text="Color", command=change_color)
c_button.grid(row=0, column=0)

f_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
f_box.grid(row=0, column=1)

f_size = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
f_size.grid(row=0, column=2)

menu_bar=Menu(w)
w.config(menu=menu_bar)

file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new)
file_menu.add_command(label="Open",command=open)
file_menu.add_command(label="Save",command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit)

edit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)

help_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About",command=about)
w.mainloop()


