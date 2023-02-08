import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import font


def mouse_motion(event):
    x, y = event.x, event.y
    status_bar.config(text=F'Mouse at {x}, {y}        ')

# Add Status BAr To Bottom App
status_bar = Label(root, text='', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root = Tk()
root.title("text editor pro in python")
root.geometry("1200x650")
root.bind('<Motion>', mouse_motion)

# Functions

# Grabe FileName
def open_file():
    my_text.delete("1.0", END)

def new_file():
    # Delete  previus text
    my_text.delete("1.0", END)
    # upadete  status  bars
    root.title(" new file ")
    status_bar.config(test="New File")
# Create New File
def open_file():
    # Delete  previus text
    my_text.delete("1.0", END)

    # Grabe file name
text_file = filedialog.askopenfilename(initialdir="C:/gui/", title=" Open  File ",  filetypes=(
    ("Text  files ", "*.txt"), ("HTML Files", "*.html"), ("Python  Files ", "*.py"), ("All File", "*.*")))
name = text_file
status_bar.config(text=name)

# Create mian Frame

my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scrollbar  fro  the text bax
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create  Text Box
my_text = Text(my_frame, width=97, height=25, font=("Arial", 16), selectbackground="yellow", selectforeground="black",
               undo=True, yscrollcommand=text_scroll.set)
my_text.pack()
# Configure our Scroball
text_scroll.configure(command=my_text.yview())
# Create Menu
my_menu = Menu(root)
root.configure(menu=my_menu)
# add file  menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", commadn=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Rendo")

root.mainloop()
