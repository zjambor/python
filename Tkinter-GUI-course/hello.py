from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is valaki")
myLabel3 = Label(root, text="-------------")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)

myButton = Button(root, text="Click Me!", state=DISABLED)
myButton.grid(row=3, column=0)

root.mainloop()
