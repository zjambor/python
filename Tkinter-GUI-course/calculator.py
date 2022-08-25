from tkinter import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def add(fst, snd):
    return fst + snd

def multiply(fst, snd):
    return fst * snd

def subtract(fst, snd):
    return fst - snd

def divide(fst, snd):
    return fst / snd

def calculate(op_1, op_2, fn):
    return fn(op_1, op_2)

operations = [add, multiply, subtract, divide]
operation = []
nums = []

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear_fn():
    e.delete(0, END)
    nums.clear()
    operation.clear()

def button_add_fn():
    first_number = e.get()
    operation.append(0)
    nums.append(int(first_number))
    e.delete(0, END)

def button_mult_fn():
    first_number = e.get()
    operation.append(1)
    nums.append(int(first_number))
    e.delete(0, END)

def button_subt_fn():
    first_number = e.get()
    operation.append(2)
    nums.append(int(first_number))
    e.delete(0, END)

def button_div_fn():
    first_number = e.get()
    operation.append(3)
    nums.append(int(first_number))
    e.delete(0, END)

def button_equal_fn():
    second_number = int(e.get())
    e.delete(0, END)
    result = calculate(nums[0], second_number, operations[operation[0]])
    e.insert(0, result)

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=40, pady=20, command=button_add_fn)
button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal_fn)
button_clear = Button(root, text="Clear", padx=78, pady=20, command=button_clear_fn)

button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subt_fn)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_mult_fn)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_div_fn)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
