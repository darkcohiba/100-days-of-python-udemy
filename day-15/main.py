from drinks import MENU, resources


def add_money(money):
    resources["money"] += money


def report():
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: $ {resources['money']}"


in_shop = True
while in_shop:
    choice = input("What would you like? (espresso, cappuccino, latte): ")

    if choice == "report":
        print(report())
    elif choice == "quit":
        in_shop = False
