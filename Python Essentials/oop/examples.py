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
