# Traditional way

def pascal_triangle(pascal, n):
    """Returns the Pascal triangle"""
    for i in range(1, n):
        newline = [1]
        for j in range(1, i):
            newline.append(add_num(pascal, i, j))
        newline.append(1)
        pascal.append(newline)
    return pascal

def add_num(pascal, i, j):
    """Returns the new value"""
    return pascal[i-1][j-1] + pascal[i-1][j]

# Functional way

def rec_pascal_triangle(pascal, n):
    """Returns the Pascal triangle"""
    addline(pascal, n, 1)
    return pascal

def addline(pascal, n, i):
    """auxiliary function"""
    if i < n:
        newline = [1]
        newline = addnum(newline, pascal, i, 1)
        newline.append(1)
        pascal.append(newline)
        addline(pascal, n, i + 1)
    return pascal

def addnum(line, pascal, i, j):
    """Returns the new line"""
    if j < i:
        line.append(pascal[i-1][j-1] + pascal[i-1][j])
        addnum(line, pascal, i, j + 1)
    return line

def walkthrough(triangle):
    """Prints the triangle"""
    if triangle != []:
        head, *tail = triangle
        print(head)
        walkthrough(tail)

pascal_tr = [[1]]
walkthrough(rec_pascal_triangle(pascal_tr, 10))
