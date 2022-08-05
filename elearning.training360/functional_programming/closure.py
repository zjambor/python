def outer_fn(n):
    print('outer_fn')
    def inner_fn(x):
        print(f'inner_fn {n}')
    
    return inner_fn
    
fnx = outer_fn(5)
del outer_fn
fnx(3)

# factory pattern
def pow_make(n):
    """ calculates pow and returns function"""
    def pow(x):
        return x ** n

    return pow

pow_of_2 = pow_make(2)
pow_of_3 = pow_make(3)

print(pow_of_2(5))
print(pow_of_3(5))
