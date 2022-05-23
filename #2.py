#Button creation
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Button creation")
button = Button(root,text= "Button") #creating button
button.pack() #anchoring it to window
root.mainloop()