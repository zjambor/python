two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y


for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

any_list = [1, 2, 3, 4]
even_list = list(map(lambda n: n | 1, any_list))
print(even_list)
