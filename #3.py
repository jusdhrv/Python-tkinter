#Button Usage
from tkinter import *

def custom() :
    print("custom command")

root = Tk()
root.geometry("500x500")
root.title("Button creation")
button = Button(root,text= "Button" , command=custom()) #creating and adding a function
button.pack()
root.mainloop()