"""
The file invoice_data.txt contains raw data for an invoice. More precisely, each line contains
    the name of an item
    how many items are bought
    the unit price of the item
The three values are separated by a single whitespace. Prepare a beautified output of the file which contains
    the name of the item formatted with 15 characters
    the number of units with 3 digits
    the price per item with 7 digits, 3 digits after the decimal point
    the total price (number of items * price per item) with 8 digits in total, 2 digits after the decimal point
If there are two lines with the following content “Apple 5 0.99” and “Cherry 2 11.99”, then the beautified output should look as follows:
Apple           15   0.99   14.85
Cherry           2  11.99   23.98
"""

items = []

with open("invoice_data.txt", "r") as file:
    for line in file:
        item = line.strip().split(" ")
        name = item[0]
        numberofitems = int(item[1])
        price = float(item[2])
        items.append((name, numberofitems, price))

for item in items:
    print(f"{item[0]:15s}{item[1]:3}{item[2]:7.2f}{item[1] * item[2]:8.2f}")