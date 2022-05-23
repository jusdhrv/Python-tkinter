#GUI development in python using tkinter
#Grid function - puts widget in a 2d dimentional table
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Grid function")
button = Button(root,text= "Button")
button.grid(padx='0',pady='0')
root.mainloop()
