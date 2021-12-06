import sys
import traceback
import queue
from datetime import datetime
import time

msg = "hello world"
print(msg)

print(5+6 - 1)
print(msg.capitalize())
print(msg.split())

def addition(a, b):
    return a+b, "a+b:"

a, b = addition(5, 6)
print(b, a)

def print_all(*args):
    for arg in args:
        print(arg)

print_all('a', 'b', 'c')

def fibonacci(upper_limit):
    a, b = 0, 1
    while a < upper_limit:
        yield a
        a, b = b, a + b

for value in fibonacci(30):
    print(value, end =" ")

print()
generator_fib = fibonacci(10000)

for val in range(0,15):
    print(generator_fib.__next__(), end =" ")

print()

class C1:
    def __init__(self):
        self.name = "Constr"
        self._name = "Protected"
        self.__name = "Private"

    @property           # getter  
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def divide(self, a, b):
        try:
            c = a // b
            return c
        except ZeroDivisionError as identifier:
            print(identifier)
            return sys.exc_info()

a = C1()
print(a.name)
print(a._name)
a.name = "valami mas"
print(a.name)

# inheritence
class C2(C1):
    def __init__(self, name, email):
        C1.name = name
        self.email = email

g = C2("My name", "My email")
print(g.name, " | ", g.email)

# print(a.divide(5, 0))

type_d, value, traceback_obj = a.divide(5,0)
print(type_d, value, traceback.print_tb(traceback_obj))

def even_numbers(n):
    for x in range(n):
       if (x % 2 == 0): 
           yield x       

num = even_numbers(10)
print(list(num))

def getFibonnaciSeries(num):
    c1, c2 = 0, 1
    count = 0
    while count < num:
        yield c1
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1

fin = getFibonnaciSeries(7)

for i in fin:
    print(i, end =" ")

print()

q1 = queue.Queue()

for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue

while not q1.empty():
    print("The value is ", q1.get()) # get() will remove the item from the queue.

q1.put(11)
q1.put(5)
q1.put(4)
q1.put(21)
q1.put(3)
q1.put(10)

#using bubble sort on the queue
n =  q1.qsize()
for i in range(n):
    x = q1.get() # the element is removed
    for j in range(n-1):
        y = q1.get() # the element is removed
        if x > y :  
            q1.put(y)   #the smaller one is put at the start of the queue
        else:
            q1.put(x)  # the smaller one is put at the start of the queue
            x = y     # the greater one is replaced with x and compared again with nextelement
    q1.put(x)

while not q1.empty(): 
    print(q1.queue[0], end = " ")  
    q1.get()

def fakt(n):
    if n == 1 :
        return 1
    else:
        return n * fakt(n-1)

t1 = time.time()
print()
print(fakt(500))

t2 = time.time()
lasted = t2 - t1
print("Computation lasted", lasted*pow(10,9), "nanoseconds.")
