#GUI development in python via tkinter
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Checkbutton creation")
state = BooleanVar()
state.set(True)
Checkbutton = Checkbutton(root, text="Hello! Plz Click Me!" , var=state)
Checkbutton.pack(expand = 'True')
root.mainloop()
