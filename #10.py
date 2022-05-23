import tkinter as tk
from tkinter import ttk

window = tk.Tk()
ttk.Label(window,text="Choose a month").grid()
n = tk.StringVar()
monthchoosen = ttk.Combobox(window,width=20,textvariable=n)
monthchoosen['values'] = ('1','2','3','4','5')
monthchoosen.grid()
monthchoosen.current(1)
window.mainloop()
