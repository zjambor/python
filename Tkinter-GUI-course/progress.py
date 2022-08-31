import time
from tkinter import *
from tkinter import ttk
import threading

root = Tk()
root.title("Progress window")
root.geometry("500x600")

global stop
stop = False

my_label = Label(root, text="")

def step():
    #my_progress['value'] += 20
    #my_progress.start(10)
    my_progress['value'] = 0
    my_label.config(text=my_progress['value'])
    for _ in range(5):
        global stop
        if not stop:
            my_progress['value'] += 20
            my_label.config(text=my_progress['value'])
            root.update_idletasks()
            time.sleep(1)
    my_label.config(text=my_progress['value'])

def stop_progress():
    global stop
    stop = True
    my_progress.stop()
    my_label.config(text=0)

def start_progress():
    global stop
    stop = False
    threading.Thread(target=step, daemon=False).start()

my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
my_progress.pack(pady=20)

my_button = Button(root, text="Progress", command=start_progress)
my_button.pack(pady=20)

my_button2 = Button(root, text="Stop", command=stop_progress)
my_button2.pack(pady=20)

my_label.pack()


root.mainloop()
