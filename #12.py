#GUI development in python using tkinter
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New File Ctrl+N')
filemenu.add_separator()
filemenu.add_command(label='Open File Ctrl+O')
filemenu.add_separator()
filemenu.add_command(label='Open Module Alt+M')
filemenu.add_separator()
filemenu.add_command(label='Quit Ctrl+Q')
root.geometry("500x500")
root.title("Grid function")
root.mainloop()
