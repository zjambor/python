import itertools as it
import random

counter = it.count(start=10, step=1)
print(list(next(counter) for _ in range(5)))

num1 = [5,7,6,4,3]
num2 = [11,18,24,25,31]

# descartes-szorzat
# print(list(it.product(num1, num2)))

# shuffle
cart_prod = list(it.product(num1, num2))
random.shuffle(cart_prod)
print(cart_prod)
