"""
There is a file secret.txt, which contains one character per line. 
There is a second file key.txt, which contains two lines with one number per line (the number could have several digits).
The first number col represents the number of columns of a grid, the second number row represents the number of rows of the grid. 
The characters of the first file should now be filled into this grid. 
Take the characters one by one and fill them into a string until the string contains col characters. Append the string to a list.
Then create a new string the same way. Continue, until the number of strings is equal to row. Now, write all the strings into a file public.txt.
Open the the file and check the content.
"""

with open("opensap-python-course\key.txt", "r") as file:
    key = []
    for line in file:
        key.append(line.strip())
    columns = int(key[0])
    rows = int(key[1])

print((columns, rows))

stringlist = []

with open("opensap-python-course\secret.txt", "r") as file:
    rowindex = 0
    columnindex = 1
    newstring = ""

    for line in file:
        newstring += line.strip()

        if columnindex == columns:
            stringlist.append(newstring)
            newstring = ""
            columnindex = 0
            rowindex += 1
        
        columnindex += 1
        if rowindex == rows:
            break

print(stringlist)

with open("public.txt", "w") as file:
    for stringline in stringlist:
        file.write(stringline + "\n")

with open("public.txt", "r") as file:
    for line in file:
        print(line.strip())

"""
.................................................
.................................................
...#####..#...#..#####..#...#..#####..#....#.....
...#...#..#...#....#....#...#..#...#..##...#.....
...#...#..#...#....#....#...#..#...#..#.#..#.....
...#####..#####....#....#####..#...#..#..#.#.....
...#........#......#....#...#..#...#..#..#.#.....
...#........#......#....#...#..#...#..#...##.....
...#........#......#....#...#..#####..#....#.....
.................................................
.................................................
...#..#####.....#####..#####..#####..#......#....
...#..#.........#......#...#..#...#..#......#....
...#..#.........#......#...#..#...#..#......#....
...#..#####.....#......#...#..#...#..#......#....
...#......#.....#......#...#..#...#..#......#....
...#......#.....#......#...#..#...#..#...........
...#..#####.....#####..#####..#####..#####..#....
.................................................
.................................................

with open("key.txt", "r") as key:
    columns = int(key.readline().strip())
    rows = int(key.readline().strip())
with open("secret.txt", "r") as file:
    sentence = []
    for i in range(rows):
        row = ""
        for j in range(columns - 1):
            symbol = file.readline().strip()
            row += symbol
        sentence.append(row)
with open("public.txt", "w") as output:
    for item in sentence:
        output.write("\n")
        output.write(item + "\n")
        print(item)
"""