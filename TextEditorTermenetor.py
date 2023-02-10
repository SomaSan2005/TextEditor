# include of tkinter and all

from tkinter import *
from tkinter import filedialog
from tkinter import font
import tkinter as tk

import bold as bold

#from TextEditor.texteditoprov01 import my_text


# definition for mause motions

def mouse_motion(event):
    x, y = event.x, event.y
    status_bar.config(text=F'Mouse at {x}, {y}        ')


# root
root = Tk()
root.title("Text Editor Classic")
root.geometry("1200x680")
# for mause motion
root.bind('<Motion>', mouse_motion)

# set variable  for open file name

global open_status_name
open_status_name = False


# Fanctions

# Create  new  file

def new_file():
    # Delate previus  text

    my_text.delete("1.0", END)
    # Update  status bars

    root.title("New File")
    status_bar.config(text="New File        ")

    global open_status_name
    open_status_name = False


# Open File

def open_file():
    # Delate previus  text

    my_text.delete("1.0", END)

    # Grab Filename

    text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(
        ("Text File", "*.txt"), ("Html File",
                                 "*.html"), ("Python File", "*.py"), ("C file", "*.c"),
        ("All File", "*.*")))
    # check  to see  if there  is a  file name

    if text_file:
        # make filename global so  we can  acess it later

        global open_status_name
        open_status_name = text_file

    # update status bars

    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("C:/gui/", "")
    root.title(f'{name} - new file')

    # Open the file

    text_file = open(text_file, 'r')
    stuff = text_file.read()

    # add file to texbox

    my_text.insert(END, stuff)

    # Close the  opend file

    text_file.close()


# save as file


def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/", title=" Save File",
                                             filetypes=(
                                                 ("Text File ",
                                                  "*.txt"), ("Html File", "*.html"),
                                                 ("Python File", "*.py"),
                                                 ("All File", "*.*")))
    if text_file:
        # update status  Bars

        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        name = name.replace("C:/gui/", "")
        root.title(f'{name} - new file')

        # save the file

        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))

        # close the file

        text_file.close()

    # save file


def save_file():
    global open_status_name
    if open_status_name:

        # save the file

        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))

        # close the file

        text_file.close()

        # put status update or popup code

        status_bar.config(text=f'Saved: {open_status_name}        ')
    else:
        save_as_file()


# Cut Text {none  01}


def cut_text(event=None):
    if my_text.tag_ranges("sel"):
        my_text.event_generate("<<Cut>>")


# Copy Text


def copy_text(e):
    global selected

    # chek to see if we used key board shortcuts

    if e:
        selected = root.clipboard_get()

    # ---------------------------------

    if my_text.selection_get():
        # grab selected text from box

        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


# pasteText


def paste_text(e):
    if selected:
        position = my_text.index(INSERT)
        my_text.insert(position, selected)


# Bold  Text
def bold_it():
    # Create our font

    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    # Configure  a tag
    my_text.tag_configure("bold", font=bold_font)

    #define current tags
    current_tags =  my_text.tag_names("sel.first")

    # if statamet to see if tag  has  been  set
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


# italics  text
def italic_it():
    # Create our font

    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    # Configure  a tag
    my_text.tag_configure("italic", font=italic_font)

    # define current tags
    current_tags = my_text.tag_names("sel.first")

    # if statamet to see if tag  has  been  set
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


# Create  a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)
# Create our  Scrollbar for  the text  box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal  Scrollbar

hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow",
               selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none",
               xscrollcommand=hor_scroll.set)
my_text.pack()
# Configure  our scrollbar

text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Create Menu

my_menu = Menu(root)
root.config(menu=my_menu)

# Add file menu

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add edit  menu

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=edit_menu)
edit_menu.add_command(label="Cut ", command=lambda: cut_text(
    False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy  ", command=lambda: copy_text(
    False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste ", command=lambda: paste_text(
    False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo ", command=my_text.edit_redo, accelerator="(Ctrl+y)")
# Add Status Bar  To Bottom  Of  App

status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

# Edit Bindings

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-c>', paste_text)

# Create Button

# Bold Button
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5)

# italics Button
italics_button = Button(toolbar_frame, text="Italic", command=italic_it)
italics_button.grid(row=0, column=1, padx=5)

# Undo/Redo Buttons
undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)
redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)
# Main loop

root.mainloop()

# the finish program
