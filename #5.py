# Button positioning
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Button creation")
button1 = Button(root,text= "Button4" , command=root.destroy)
button1.pack(side = 'left') #left

button2 = Button(root,text= "Button2" , command=root.destroy)
button2.pack(side = 'right') #right

button3 = Button(root,text= "Button1" , command=root.destroy)
button3.pack(side = 'top') #top

button4 = Button(root,text= "Button3" , command=root.destroy)
button4.pack(side = 'bottom') #bottom

button5 = Button(root,text= "Button5" , command=root.destroy)
button5.pack(expand = 'True') #middle
root.mainloop()