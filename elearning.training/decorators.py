import time

def logged(fn):
    def wrapper(*args):
        print(f'you called: {fn.__name__}({args})')
        results = fn(*args)
        print(f'result was: {results}')
        return results
    return wrapper

@logged
def hello(*args):
    print(*args)
    return True

hello('Tamas', 'big', 'world')

def timeit_decorator(fn):
    def wrapper(*args):
        start = time.time()
        result = fn(*args)
        end = time.time()
        print(f'{fn.__name__} took {(end - start)*1000} ms.')
        return result
    return wrapper

@timeit_decorator
def comprehension():
    return [x**2 for x in range(3000000)]

@timeit_decorator
def generator():
    return (x**2 for x in range(3000000))

@timeit_decorator
def iter_over(iter):
    for _ in iter:
        pass

alist = comprehension()
iter_over(alist)
agenerator = generator()
iter_over(agenerator)
