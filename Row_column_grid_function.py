#GUI development in python using tkinter
#Grid function - puts widget in a 2d dimentional table
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Grid function")
button = Button(root,text= "Button")
button.grid(row='0',column='0')
root.mainloop()
