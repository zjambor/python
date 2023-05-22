import sys
import ctypes

my_var = 10
print(hex(id(my_var)))

a = [1, 2, 3]

print(id(a))
print(sys.getrefcount(a))   # increase ref counter 

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

id_a = id(a)
a = None
print(ref_count(id_a))
print(ref_count(id_a))
print(ref_count(id_a))
