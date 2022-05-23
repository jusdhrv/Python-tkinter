#GUI development in python using tkinter
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Frames")
bottomframe = Frame(root)
bottomframe.pack(side = 'bottom')
red_button1 = Button(bottomframe,text = 'red1')
red_button1.pack(side = 'top')
red_button2 = Button(bottomframe,text = 'red2')
red_button2.pack(side = 'top')
red_button3 = Button(bottomframe,text = 'red3')
red_button3.pack(side = 'top')
root.mainloop()
