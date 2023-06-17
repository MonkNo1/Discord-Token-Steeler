import os 
from tkinter import filedialog
import datetime
import hashlib


user = os.getlogin()
pdir = os.path.join("E:",os.sep,"programing","sh","bash","source")   
             


def hashk():
    current_time = datetime.datetime.now()
    hash1 = hashlib.md5(str(current_time).encode())
    name = hash1.hexdigest()[:14]
    name= name+".js"
    return name


def placeFile(content):
    try:
        os.chdir(pdir)
        fname = hashk()
        f = open(fname,"w")
        f.write(content)
        f.close()
    except:
        pass
        
    

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('javascript', '*.js')])
   if file:
      content = file.read()
      file.close()
      placeFile(content)
    #   print("%d characters in this file" % len(content))

# placeFile("hiiiii")