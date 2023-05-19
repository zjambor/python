EMPTY = ""
ROOK = "rook"
board = [[EMPTY for i in range(8)] for j in range(8)]

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Average temperature at noon:", average)

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

var = 1
while var < 10:
    print("#")
    var = var << 1

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
 
print(c + d + e)

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

nums = [1, 2, 3]
vals = nums[-1:-2]
print(vals)

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals)

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

my_list = [i for i in range(-1, 2)]
print(my_list)

t = [[3-i for i in range (3)] for j in range (3)]
print(t)
