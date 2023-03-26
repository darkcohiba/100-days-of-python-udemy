from drinks import MENU, resources


def add_money(money):
    resources["money"] += money


def check_resources(drink_name):
    if resources["water"] < MENU[drink_name]["ingredients"]["water"] or \
            resources["milk"] < MENU[drink_name]["ingredients"]["milk"] or \
            resources["coffee"] < MENU[drink_name]["ingredients"]["coffee"]:
        return False
    else:
        return True


def remove_resources(drink_name):
    resources["water"] -= MENU[drink_name]["ingredients"]["water"]
    resources["milk"] -= MENU[drink_name]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink_name]["ingredients"]["coffee"]


def report():
    return f"Water: {resources['water']}ml \n" \
           f"Milk: {resources['milk']}ml\n" \
           f"Coffee: {resources['coffee']}g\n" \
           f"Money: ${resources['money']}"


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def give_change(total, drink_name):
    if total == MENU[drink_name]["cost"]:
        resources["money"] += MENU[drink_name]["cost"]
        remove_resources(drink_name)
        print(f"Here is your {drink_name} ☕️. Enjoy!")
    elif total > MENU[drink_name]["cost"]:
        resources["money"] += MENU[drink_name]["cost"]
        change = total - MENU[drink_name]["cost"]
        remove_resources(drink_name)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink_name} ☕️. Enjoy!")
    elif total < MENU[drink_name]["cost"]:
        print("Sorry that's not enough money. Money refunded.")


in_shop = True
start = True


def check_system():
    if resources["water"] < 50:
        global in_shop
        in_shop = False
        global start
        start = False
        print("shop must close due to lack of water")
        print(report())


while in_shop:

    while start:
        choice = input("What would you like? (espresso, cappuccino, latte): ")

        if choice == "report":
            print(report())
        elif choice == "quit":
            in_shop = False
        else:
            resource_check = check_resources(choice)
            if resource_check:
                profit = int(process_coins())
                give_change(profit, choice)
            else:
                print("Not enough resources sorry!")

        check_system()
