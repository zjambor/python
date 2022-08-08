class Person:
    """ Ez az osztaly egy személy adatait tárolja """

    def __init__(self, lastname, firstname, age, address):
        self._lastname = lastname
        self._firstname = firstname
        self._age = age
        self._address = address

    def getName(self):
        return f'{self._firstname} {self._lastname}'

    def __str__(self):
        """ toString() """
        return f"Person: {self.getName()}, age: {self._age}, address: {self._address}"

class Employee(Person):
    def __init__(self, lastname, firstname, age, address, salary, job, manager=None):
        super().__init__(lastname, firstname, age, address)
        self.__salary = salary
        self.__job = job
        self.__manager = manager

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    salary = property(get_salary, set_salary)

    def get_job(self):
        return self.__job

    def set_job(self, job):
        self.__job = job

    job = property(get_job, set_job)

    def get_manager(self):
        return self.__manager
    
    def set_manager(self, manager):
        self.__manager = manager

    manager = property(get_manager, set_manager)
    
    def __str__(self):
        return f"{self.getName()}, salary: {self.salary}, job: {self.job}, manager: {self.get_manager()}"

class Manager(Person):
    def __init__(self, lastname, firstname, age, address, employees):
        super().__init__(lastname, firstname, age, address)
        self.__employees = employees

    def __str__(self):
        return f"{self.getName()} (number of employees: {len(self.__employees)})"

    def print_employees(self):
        for emp in self.__employees:
            print(f"\t{emp.getName()}")

    def add_employee(self, employee):
        self.__employees.append(employee)
    
    def remove_employee(self, employee):
        self.__employees.remove(employee)

king = Manager("King", "Stephenson", 50, "Boul 1 CA", [])
peter = Employee("Peter", "Jones", 40, "Boul 2 CA", 2500, "Accountant", king)
jones = Employee("Jones", "Smith", 38, "Boul 3 CA", 3000, "Accountant", king)

king.add_employee(peter)
king.add_employee(jones)

print(king)
print(peter)
print(jones)

print(f"{king.getName()}'s employees:")
king.print_employees()

parker = Employee("Parker", "Smith", 38, "Boul 3 CA", 3000, "Accountant", king)
king.remove_employee(jones)
king.add_employee(parker)

print(king)
print(peter)
print(parker)

print(f"{king.getName()}'s employees:")
king.print_employees()
