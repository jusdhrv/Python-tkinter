#GUI development in python using tkinter
#Grid function - puts widget in a 2d dimentional table
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Grid function")
spinbox1 = Spinbox(root , from_ = 1900 , to = 2020)
spinbox1.pack(expand = True)
root.mainloop()
