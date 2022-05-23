from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Button creation")
root.configure(bg = "orange")
Scale1 = Scale(root , from_ = 0, to = 100, orient = HORIZONTAL)
Scale1.pack()
Scale2 = Scale(root , from_ = 0, to = 100, orient = VERTICAL)
Scale2.pack()
