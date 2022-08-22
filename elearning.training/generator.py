def my_gen(n):
    for i in range(1, n):
        yield i

gen = my_gen(20)

for i in range(10):
    print(next(gen))

def fibonacci(limit):
    a, b = 0, 1
    i = 0

    while i < limit:
        yield a
        a, b = b, a + b
        i += 1

fib = fibonacci(100)

# first 8 fibonacci numbers

nex_fib = next(fib)
ind = 1
try:
    while True:
        print(ind, ": ", nex_fib)
        nex_fib = next(fib)
        ind += 1
except StopIteration:
    print("End of Fibonacci sequence")
