# !/usr/bin/python3
from tkinter import *
import os
cmdW = 'java -jar processing-py.jar mouse_follow.py'

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")
   os.system(cmdW)

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()
