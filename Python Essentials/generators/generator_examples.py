the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

powers_of_2 = (2 ** x for x in range(8))
print(list(powers_of_2))

l_powers_of_2 = lambda n: (2 ** x for x in range(n))
print(list(l_powers_of_2(9)))
