from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print(Menu().get_items())


robust = CoffeeMaker()
register = MoneyMachine()
in_shop = True
while in_shop:

    choice = input("What would you like? (espresso, cappuccino, latte): ")
    drink = Menu().find_drink(choice)

    if choice == "report":
        robust.report()
        register.report()
    elif choice == "quit":
        in_shop = False
    elif drink:
        if robust.is_resource_sufficient(drink) and register.make_payment(drink.cost):
            robust.make_coffee(drink)
