#GUI development in python using tkinter
#Grid function - puts widget in a 2d dimentional table
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
root = Tk()
root.geometry("500x500")
root.title("Grid function")
style = ttk.Style()
style.theme_use('default')
style.configure("black.horizontal.TProgressbar",background = 'green')
bar = Progressbar(root,lenght=220,style='black.horizontal.TProgressbar')

bar['value'] = 20
bar.pack()
root.mainloop()
