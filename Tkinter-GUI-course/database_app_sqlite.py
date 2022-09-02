from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Database window")
root.geometry("400x400")

# create a database or connect to one
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# create table
c.execute(""" 
    CREATE TABLE IF NOT EXISTS addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)
    """)

def submit():
    # insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }
    )
    conn.commit()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    c.execute("""
        SELECT *, oid FROM ADDRESSES
    """)
    records = c.fetchall()
    # c.fetchmany(50)
    # c.fetchone()

    print_records = "First_name Last_name   Address City    State   Zipcode ID\n"
    for record in records:
        for field in record:
            print_records += str(field) + "\t"
        print_records += "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=9, column=0, columnspan=2)

def delete():
    c.execute("DELETE FROM addresses where first_name=" + f_name.get())
    conn.commit()

def quit_program():
    # commit changes
    conn.commit()
    
    # close conn
    conn.close()

    root.quit()

# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# create buttons
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

quit_btn = Button(root, text="Exit", command=quit_program)
quit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=156)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

root.mainloop()
