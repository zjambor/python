"""
The file numbers.txt contains numbers. (Actually, the same numbers from the last exercise.) 
There is exactly one number per line. Read the numbers from the file and write only the 
even numbers into a new file named even_numbers.txt. Again, there should be one number per line. 
The order of the numbers shall be unchanged. To indicate that the program is finished, 
print the following output: “List of even numbers created!”
"""

listOfNumbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        listOfNumbers.append(int(line.strip()))

print(listOfNumbers)

with open("even_numbers.txt", "w") as wfile:
    for i in listOfNumbers:
        if i % 2 == 0:
            wfile.write(str(i) + "\n")

with open("even_numbers.txt", "r") as file:
    for line in file:
        print(line.strip())

print("List of even numbers created!")