def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

f = select_function(1)
print(f is square)
print(f(2))

f = select_function(2)
print(f is cube)
print(f(2))

print(select_function(2)(3))    # = cube(3)

def exec_function(fn, n):
    return fn(n)

print("cube(3): ", exec_function(cube, 3))
print("square(3): ", exec_function(square, 3))
