# _protected
# __private

class Dog:
    def __init__(self, name, age):
        self._name = name   # protected
        self.__age = age    # private

    # getter, setter
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # property
    age = property(get_age,set_age)

d = Dog('Jerry', 11)

print(d.age)
d.age = 12
print(d.age)
