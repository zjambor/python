from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Treeview window")
root.geometry("500x600")

style = ttk.Style()

style.theme_use("clam")

style.configure("Treeview", 
    background="silver",
    foreground="black",
    rowheight=25,
    fieldbackground="silver"
    )

style.map('Treeview',
    background=[('selected', 'green')])

tree_frame = Frame(root)
tree_frame.pack(pady=20)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# selectmode= "none", "browse", "extended"
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="none")
# Pack to the screen
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

# Define columns
my_tree['columns'] = ("Name", "ID", "Favourite Pizza")

# Format columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favourite Pizza", anchor=W, width=140)

# Create headings
my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favourite Pizza", text="Favourite Pizza", anchor=W)

# Add data
data = [
    ["John", 1, "Pepperoni"],
    ["Mary", 2, "Cheese"],
    ["Tina", 3, "Ham"],
    ["Bob", 4, "Supreme"],
    ["Erin", 5, "Cheese"],
    ["Wes", 6, "Onion"],
    ["John", 1, "Pepperoni"],
    ["Mary", 2, "Cheese"],
    ["Tina", 3, "Ham"],
    ["Bob", 4, "Supreme"],
    ["Erin", 5, "Cheese"],
    ["Wes", 6, "Onion"]
]

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count = 0
for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="Parent", values=(record[0], record[1], record[2]), tags='evenrow',)
    else:
        my_tree.insert(parent='', index='end', iid=count, text="Parent", values=(record[0], record[1], record[2]), tags='oddrow',)

    count += 1

add_frame = Frame(root)
add_frame.pack(pady=20)

nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

def add_record_fn():
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    global count
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags='evenrow',)
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags='oddrow',)
    count += 1

    # Clear the boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

def remove_all_fn():
    for record in my_tree.get_children():
        my_tree.delete(record)

def remove_one_fn():
    x = my_tree.selection()[0]
    my_tree.delete(x)

def remove_many_fn():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

add_record = Button(root, text="Add Record", command=add_record_fn)
add_record.pack(pady=20)

remove_all = Button(root, text="Remove All Records", command=remove_all_fn)
remove_all.pack(pady=10)

remove_one = Button(root, text="Remove One Selected", command=remove_one_fn)
remove_one.pack(pady=10)

remove_many = Button(root, text="Remove Many Selected", command=remove_many_fn)
remove_many.pack(pady=10)

root.mainloop()
