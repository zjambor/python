import logging

def hof_write_repeat(message, n, action):
    for i in range(n):
        action(message)

hof_write_repeat('Hello', 5, print)

hof_write_repeat('Hello', 5, logging.error)

items = [1, 2, 3, 4, 5]
newitems = list(map(lambda x: x**2, items))
print(newitems)

newitems = list(map(lambda x: x**x, items))
print(newitems)

def apply_string_list(fn, str_list):
    for item in str_list:
        print(fn(item))

apply_string_list(lambda s: s.upper(), ['hello', 'valaki'])

def make_is_div(n):
    def is_div_n(x):
        return x % n == 0
    return is_div_n

divisibles = [make_is_div(n) for n in range(1,10001)]

for i, div in enumerate(divisibles, start=1):
    if(div(23423453)):
        print(i, end=', ')
