import random

nums = [1, 2, 3, 4, 5]

squares = (x ** 2 for x in nums)
strings = (str(x) for x in squares)
lens = (len(s) for s in strings)
arbs = ((123 - x) * 2 - 15 for x in lens)
print(list(arbs))

nums_2 = [10,3,7,9,11,33,22,8,2]
power_3 = (x ** 3 for x in nums_2 if x % 2 == 0)
print(list(power_3))

random_numbers = (random.randint(1, 1000) for _ in range(1,100))
random_squares = (x ** 2 for x in random_numbers)
random_strings = (str(x) for x in random_squares)
print(set(random_strings))
