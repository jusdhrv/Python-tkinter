import tkinter as tk
from tkinter import ttk

root = tk.Tk()
scheduleimage = tk.PhotoImage("...")
note = ttk.Notebook(root)

tab1 = ttk.Frame(note)
tab2 = ttk.Frame(note)
tab3 = ttk.Frame(note)

button = ttk.Button(tab1,text = "b1")
button.pack()
button2 = ttk.Button(tab2,text = "b2")
button2.pack()
button3 = ttk.Button(tab3,text = "b3")
button3.pack()

note.add(tab1,text = "Tab1" , image=scheduleimage,compound='top')
note.add(tab2,text = "Tab2" , image=scheduleimage,compound='top')
note.add(tab3,text = "Tab3" , image=scheduleimage,compound='top')
note.pack()

root.mainloop()
