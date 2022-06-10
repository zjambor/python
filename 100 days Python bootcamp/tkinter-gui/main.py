import playground
from tkinter import *

window = Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label1 = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label1.pack()
# my_label.place(x=0, y=10)
my_label.grid(column=0, row=0)
# my_label1.grid(column=1, row=1)
my_label.config(padx=50, pady=50)

def button_clicked():
    my_label["text"] = input.get() if input.get() != "" else "Button Got Clicked"
    my_label1["text"] = str(playground.add(1,2,3,4,5,6,7,8,9,10,))

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=3, row=2)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

window.mainloop()
