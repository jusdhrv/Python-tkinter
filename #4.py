#Button other functions(background text colour)
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Button creation")
button5 = Button(root,text= "Button5" , font='CourierNew 50 italic' , background='blue' , foreground='black' , activebackground='yellow' , activeforeground='red')
button5.pack(expand = 'True')
root.mainloop()