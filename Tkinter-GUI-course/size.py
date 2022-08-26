from tkinter import *

root = Tk()
root.title("Sizable window")
root.geometry("800x800")

def resize():
    w = width_entry.get()
    h = height_entry.get()
    root.geometry(f"{w}x{h}")
    # root.geometry("%ix%i" % (w,h))    # old method    

def get_size():
    dimension_label = Label(root, text="Geometry: " + str(root.winfo_geometry()) + " Width: " + str(root.winfo_width()) +" Height: " + str(root.winfo_height()))
    dimension_label.pack(pady=20)

width_label = Label(root, text="Width:")
width_label.pack(pady=20)
width_entry = Entry(root)
width_entry.pack()

height_label = Label(root, text="Height:")
height_label.pack(pady=20)
height_entry = Entry(root)
height_entry.pack()

my_button = Button(root, text="Resize", command=resize)
my_button.pack(pady=20)

get_size_button = Button(root, text="Get size", command=get_size)
get_size_button.pack(pady=20)

root.mainloop()
