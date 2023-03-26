from drinks import MENU, resources


def add_money(money):
    resources["money"] += money


def check_resources(drink_name):
    if resources["water"] < MENU[drink_name]["ingredients"]["water"] or resources["milk"] < MENU[drink_name]["ingredients"]["milk"] or resources["coffee"] < MENU[drink_name]["ingredients"]["coffee"]:
        return False
    else:
        return True


def remove_resources(drink_name):
    resources["water"] -= MENU[drink_name]["ingredients"]["water"]
    resources["milk"] -= MENU[drink_name]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink_name]["ingredients"]["coffee"]


def report():
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: $ {resources['money']}"


def ask_for_payment():
    pass
in_shop = True

while in_shop:
    if resources["water"] < 50:
        print("shop must close due to lack of water")
        in_shop = False

    choice = input("What would you like? (espresso, cappuccino, latte): ")

    if choice == "report":
        print(report())
    elif choice == "quit":
        in_shop = False
    else:
        resource_check = check_resources(choice)
        if resource_check:
            print("coming up")
            remove_resources(choice)
        else:
            print("Not enough resources sorry!")



