#GUI development in python using tkinter
#Grid function - puts widget in a 2d dimentional table
import tkinter as tk
root = tk.Tk()
root.geometry("500x500")
root.title("Grid function")
text = tk.Text(root,height=15,width=15)
text.pack(expand = True)
text.insert(tk.END,"")
root.mainloop()
