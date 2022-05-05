filename = input("Please enter the file name you want to copy: ")
newfile = input("Please enter the file name of the new file: ")
listOfLines = []
with open(filename, "r") as file:
    for line in file:
        listOfLines.append(line)

with open(newfile, "w") as file:
    for line in listOfLines:
        file.write(line)