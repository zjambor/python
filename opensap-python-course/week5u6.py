items = []

with open("opensap-python-course\students.csv", "r") as file:
    for line in file:
        item = line.strip().split(";")
        items.append(item)

print(items)