#GUI development in python using tkinter
#Grid function - puts widget in a 2d dimentional table
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Grid function")
message = Message(root,text = "Test")
message.config(bg = 'orange')
message.pack(expand = True)
root.mainloop()
