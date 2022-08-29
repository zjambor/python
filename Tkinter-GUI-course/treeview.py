from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Treeview window")
root.geometry("500x500")

my_tree = ttk.Treeview(root)

my_tree['columns'] = ("Name", "ID", "Favourite Pizza")

my_tree.column("#0", width=120)

root.mainloop()
