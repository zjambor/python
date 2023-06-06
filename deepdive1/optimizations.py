import time
import string

def my_func(container):
    e = 3
    start = time.perf_counter()
    for i in range(1000000):
        if e in container:
            pass
    end = time.perf_counter()
    print(end - start)

my_func(list(string.ascii_letters))
my_func(tuple(string.ascii_letters))
my_func(set(string.ascii_letters))
