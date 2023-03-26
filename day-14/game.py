import random
from game_data import data
from art import logo, vs


def get_random():
    return random.choice(data)
def game():
    print(logo)
    score = 0
    choice_1 = get_random()
    choice_2 = get_random()
    print(choice_1)


game()