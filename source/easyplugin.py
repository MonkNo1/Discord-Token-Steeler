from tkinter import *
from tkinter import ttk
from . import core

# this file used for UI frames for add plugins

def start():
    parent = Tk()        
    label = Label(parent, text="Click the Button to browse the Files", font=('Georgia 13'))
    label.pack(pady=10)        
    ttk.Button(parent, text="Browse", command=core.open_file).pack(pady=20)
    parent.mainloop()  
