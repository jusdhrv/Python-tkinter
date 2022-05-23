#GUI development in python via tkinter
# button other functions(background text colour )
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Button creation")
menubutton = Menubutton(root,text="Choose A,B or C")
menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
menubutton.menu.add_checkbutton(label="A",variable=var1)
menubutton.menu.add_checkbutton(label="B",variable=var2)
menubutton.menu.add_checkbutton(label="C",variable=var3)
menubutton.pack(expand=True)
root.mainloop()
