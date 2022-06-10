from tkinter import Button, Entry, Label, Tk

def button_clicked():
    result = (1.609344 * float(input_entry.get())) if input_entry.get() != "" else 0
    result_label.config(text=f"{round(result)}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=30, pady=30)

input_entry = Entry(width=7)
input_entry.grid(column=1, row=0)

miles_label = Label(text=" Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2, row=0)
isequal_label = Label(text="is equal to", font=("Arial", 12, "normal"))
isequal_label.grid(column=0, row=1)
result_label = Label(text="0", font=("Arial", 12, "normal"))
result_label.grid(column=1, row=1)
km_label = Label(text="Km", font=("Arial", 12, "normal"))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
