class Person:
    """ Ez az osztaly egy személy adatait tárolja """

    def __init__(self, lastname, firstname, age, address):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.address = address

    def getName(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        """ toString() """
        return f"Person: {self.getName()}, age: {self.age}, address: {self.address}"

class Employee(Person):
    def __init__(self, lastname, firstname, age, address, salary, job, manager=None):
        super().__init__(lastname, firstname, age, address)
        self.salary = salary
        self.job = job
        self.manager = manager

    def set_manager(self, manager):
        self.manager = manager

    def __str__(self):
        return f"{self.getName()}, salary: {self.salary}, job: {self.job}, manager: {self.manager}"

class Manager(Person):
    def __init__(self, lastname, firstname, age, address, employees):
        super().__init__(lastname, firstname, age, address)
        self.employees = employees

    def __str__(self):
        return f"{self.getName()} (number of employees: {len(self.employees)})"

    def print_employees(self):
        for emp in self.employees:
            print(f"\t{emp.getName()}")

king = Manager("King", "Stephenson", 50, "Boul 1 CA", [])
peter = Employee("Peter", "Jones", 40, "Boul 2 CA", 2500, "Accountant", king)
jones = Employee("Jones", "Smith", 38, "Boul 3 CA", 3000, "Accountant", king)

king.employees = [peter, jones]

print(king)
print(peter)
print(jones)

print(f"{king.getName()}'s employees:")
king.print_employees()
