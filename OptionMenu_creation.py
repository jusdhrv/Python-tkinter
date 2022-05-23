#GUI development in python using tkinter
#Grid function - puts widget in a 2d dimentional table
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Grid function")
variable = StringVar(root)
variable.set("Num1")
Optionmenu = OptionMenu(root,variable,"Num1","Num2","Num3","Num4")
Optionmenu.pack(expand = True)
root.mainloop()
