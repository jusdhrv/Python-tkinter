# Button other functions(background text colour )
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Button creation")
button5 = Button(root, text="Hello! Plz Click Me!" , font='Gabriola 50 italic' , background='blue' , foreground='black' , activebackground='yellow' , activeforeground='red' , command=root.destroy)
button5.pack(expand = 'True')
root.mainloop()
