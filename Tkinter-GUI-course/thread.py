from tkinter import *
import time
from random import randint
import threading

root = Tk()
root.title("Run threads")
root.geometry("800x800")

def five_seconds():
    time.sleep(5)
    my_label.config(text="5 seconds is up!")

def rando():
    random_label.config(text=f'Random number: {randint(1,100)}')

my_label = Label(root, text="Hello there!")
my_label.pack(pady=20)

my_button1 = Button(root, text="5 seconds", command=threading.Thread(target=five_seconds).start())
my_button1.pack(pady=20)

my_button2 = Button(root, text="Pick random number", command=rando)
my_button2.pack(pady=20)

random_label = Label(root, text="")
random_label.pack()

root.mainloop()
