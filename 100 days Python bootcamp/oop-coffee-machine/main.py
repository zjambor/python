from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True

my_coffeeMaker = CoffeeMaker()
my_MoneyMachine = MoneyMachine()
my_menu = Menu()


while is_on:
    drinks = my_menu.get_items()
    answer = input(f"What would you like? ({drinks}): ").lower()
    if answer == "off":
        is_on = False
    elif answer == "report":
        my_coffeeMaker.report()
        my_MoneyMachine.report()
    else:
        drink = my_menu.find_drink(answer)
        if my_coffeeMaker.is_resource_sufficient(drink) and my_MoneyMachine.make_payment(drink.cost):
            my_coffeeMaker.make_coffee(drink)
