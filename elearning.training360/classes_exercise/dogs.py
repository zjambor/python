class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class BullDog(Dog):
    def __init__(self, name, age, size=9) -> None:
        super(BullDog, self).__init__(name, age)
        self.size = size

d = Dog('Jerry', 4)
b = BullDog('Bob', 10)
print(f"{b.name}, age: {b.age} size: {b.size}")
