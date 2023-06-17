from tkinter import *
from tkinter import filedialog,ttk

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('javascript', '*.js')])
   if file:
      content = file.read()
      file.close()
      print("%d characters in this file" % len(content))

# this file used for UI frames for add plugins
def start():
    parent = Tk()        
    label = Label(parent, text="Click the Button to browse the Files", font=('Georgia 13'))
    label.pack(pady=10)        
    ttk.Button(parent, text="Browse", command=open_file).pack(pady=20)
    parent.mainloop()  
