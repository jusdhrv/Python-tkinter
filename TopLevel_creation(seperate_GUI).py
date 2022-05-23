#GUI development in python using tkinter
#Grid function - puts widget in a 2d dimentional table
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Grid function")
def new_screen():
    top1 = Toplevel()
    top1.title("New gui window")
    top1.geometry("500x500")
    top1.mainloop()
button = Button(root,text= "Create New Screen",command=new_screen)
button.pack(expand = True)
root.mainloop()
