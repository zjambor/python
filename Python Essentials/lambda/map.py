list_1 = [x for x in range(5)]                  # lista generátor, 1-5-ig

# map(function, list)   a map a megadott függvényt alkalmazza a 2. paraméterben átadott lista elmeire

list_2 = list(map(lambda x: 2 ** x, list_1))    # a map a list_1 elemeire alkamazza a lambdát, amit a list fv. listává alakít

print(list_2)

# másik megoldás: a map objecten végig lehet iterálni
for x in map(lambda x: 2 ** x, list_1):
    print(x, end=' ')
print()
