import sys
import time

a = sys.intern("the quick brown fox" * 200)
b = sys.intern("the quick brown fox" * 200)

print(a == b)   # slow
print(a is b)   # much faster

a = "a long string that is not interned" * 200
b = "a long string that is not interned" * 200

start = time.perf_counter()

for i in range(10000000):
    if a == b:
        pass

end = time.perf_counter()

print(end - start)

a = sys.intern("a long string that is not interned" * 200)
b = sys.intern("a long string that is not interned" * 200)

start = time.perf_counter()

for i in range(10000000):
    if a is b:
        pass

end = time.perf_counter()

print(end - start)
