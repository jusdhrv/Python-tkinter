#GUI development in python via tkinter
# button other functions(background text colour )
from tkinter import *
def fun1():
    print("Button pressed")
root = Tk()
root.geometry("500x500")
root.title("Button creation")
button5 = Button(root, text="Hello" , font='CourierNew 50 italic' , background='blue' , foreground='black' , activebackground='yellow' , activeforeground='red' , command=fun1)
button5.pack(expand = 'True')
root.mainloop()
