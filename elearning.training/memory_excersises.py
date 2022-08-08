l = [300]
x = l
y = x
x.append(50)

print(l, x, y)

del x
print(l, y)
del y
print(l)
del l