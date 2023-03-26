import random
from game_data import data
from art import logo, vs


def get_randomizer():
    return random.choice(data)

def format_data(data):
    name = data["name"]
    description = data["description"]
    country = data["country"]
    # print(f'{name}: {data["follower_count"]}')
    return f"{name}, a {description}, from {country}"

def compare_account_followers(guess, follower_one, follower_two):
    # print(f'{guess} {follower_one} {follower_two}')

    if follower_one > follower_two:
        return guess == "a"
    elif follower_two > follower_one:
        return guess == "b"



def game():
    print(logo)
    score = 0
    game_over = False
    choice_1 = get_randomizer()
    choice_2 = get_randomizer()
    while not game_over:
        choice_1 = choice_2
        choice_2 = get_randomizer()

        while choice_1 == choice_2:
            choice_2 = get_randomizer()

        print(f"Compare A: {format_data(choice_1)}")
        print(vs)
        print(f"Compare B: {format_data(choice_2)}")

        guess = input("Who has more followers, A or B: \n").lower()
        choice_1_followers = choice_1["follower_count"]
        choice_2_followers = choice_2["follower_count"]
        is_correct = compare_account_followers(guess, choice_1_followers, choice_2_followers)
        

        # print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")


game()