from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python GUI")
ttk.Label(root,text = "Treeview").pack()

treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('','0',"item1",text = 'Parent tree')
treeview.insert('','1',"item2",text = '1st child')
treeview.insert('','end',"item3",text = '2nd child')
