from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Treeview window")
root.geometry("500x500")

my_tree = ttk.Treeview(root)

# Define columns
my_tree['columns'] = ("Name", "ID", "Favourite Pizza")

# Format columns
my_tree.column("#0", width=120, minwidth=25, stretch=NO)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favourite Pizza", anchor=W, width=120)

# Create headings
my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favourite Pizza", text="Favourite Pizza", anchor=W)

# Add data
my_tree.insert(parent='', index='end', iid=0, text="Parent", values=("John", 1, "Pepperoni"))
my_tree.insert(parent='', index='end', iid=1, text="Parent", values=("Mary", 2, "Cheese"))
my_tree.insert(parent='', index='end', iid=2, text="Parent", values=("Tina", 3, "Ham"))
my_tree.insert(parent='', index='end', iid=3, text="Parent", values=("Bob", 4, "Supreme"))
my_tree.insert(parent='', index='end', iid=4, text="Parent", values=("Erin", 5, "Cheese"))
my_tree.insert(parent='', index='end', iid=5, text="Parent", values=("Wes", 6, "Onion"))

my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", 1.2, "Peppers"))
my_tree.move('6', '0', '0')

# Pack to the screen
my_tree.pack(pady=20)

root.mainloop()
