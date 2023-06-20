class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

class ExampleClass2:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass2()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass2, 'b'))
print(hasattr(ExampleClass2, 'a'))

class ExampleClass3:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass3(1)
print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)

class A:
    X = 0
    def __init__(self, v = 0):
        self.Y = v
        A.X += v


class B(A):
    def __init__(self):
        A.__init__(self)


a = A()
b = A(1)
c = A(2)
print(c.X)


class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x,end='')
