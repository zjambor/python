class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    """ The function named incIntsI() gets an object of any class, scans its contents in order to find all integer attributes with names starting with i, and increments them by one. """
    for name in obj.__dict__.keys():    # scan the __dict__ attribute, looking for all attribute names;
        if name.startswith('i'):
            val = getattr(obj, name)    # use the getattr() function to get its current value; note: getattr() takes two arguments: an object, and its property name (as a string), and returns the current attribute's value;
            if isinstance(val, int):    # check if the value is of type integer, and use the function isinstance() for this purpose;
                setattr(obj, name, val + 1)     # if the check goes well, increment the property's value by making use of the setattr() function; 
                                                # the function takes three arguments: an object, the property name (as a string), and the property's new value.


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
