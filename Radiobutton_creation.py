#GUI development in python via tkinter
# button other functions(background text colour )
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Button creation")
Radiobutton1 = Radiobutton(root,text="Hello",value=0)
Radiobutton1.pack(expand=True)
root.mainloop()
