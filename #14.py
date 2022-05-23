#GUI development in python via tkinter
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Label creation")
Label1 = Label(root , text = "Label1" , background = 'yellow' , foreground = 'red')
Label1.pack(expand = True)
root.mainloop()
