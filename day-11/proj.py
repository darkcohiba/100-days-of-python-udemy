from art import *
import random

print(blackjack)
play = input("Do you want to play a game of Blackjack? (y/n): ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
user_total = 0
computer_hand = []
computer_total = 0
hit_me = True
playing = True

def deal(user_total, computer_total):
    for x in range(2):
        user_hand.append(random.choice(cards))
        user_total += int(user_hand[x])
        computer_hand.append(random.choice(cards))
        computer_total += int(computer_hand[x])
    check_if_over(user_total, computer_total)

def check_if_over(user_total, computer_total):
    if computer_total == 21:
        print("Computer has 21! User Lost")
        playing = False
    elif user_total == 21:
        print("User has 21! Computer Lost")
        playing = False
    else:
        print(user_hand)
        print([computer_hand[0]])
        print(computer_total)
        print(user_total)
        playing = False

def check_if_over_single(total, player):
    if total == 21:
        print(f"{player} has 21! User Lost")
        playing = False
    else:
        print(player)
        print(total)
        playing = False

def hit_me(total, player):
    player.append(random.choice(cards))
    total += int(player[-1])
    check_if_over_single(total, player)

while playing:
    deal(user_total, computer_total)    
    add_card_choice = input("Would you like to hit? (yes/no) ")
    if add_card_choice == 'yes':
        hit_me(user_total, user_hand)
    
    playing = False
    user_total = 0




    # while hit_me:
    #     hit_me_user(user_total)
    #     if user_total == 21: 
    #         print ("User has 21, User Wins, Computer Loses")
    #         hit_me = False
    #     if user_total > 21:
    #         print("User Bust, Computer Wins")
    #         hit_me = False
    #     again_input = input("Do you want to hit again? (yes/no): ")
    #     if again_input == "yes":
    #         hit_me_user(user_total)
    #         if user_total == 21: 
    #             print ("User has 21, User Wins, Computer Loses")
    #             hit_me = False
    #         if user_total > 21:
    #             print("User Bust, Computer Wins")
    #             hit_me = False
    #     else:
    #         hit_me = False
