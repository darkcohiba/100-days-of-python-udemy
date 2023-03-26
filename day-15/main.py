from drinks import MENU, resources


def add_money(money):
    resources["money"] += money
def report():
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: $ {resources['money']}"


