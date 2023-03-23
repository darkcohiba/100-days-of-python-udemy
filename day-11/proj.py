from art import *
import random

# play = input("Do you want to play a game of Blackjack? (y/n): ")

# user_total = 0
# computer_total = 0
# hit_me = True
# playing = True

def deal_cards():
    """Returns a card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    """Calculates scores for a given array of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Its a draw"
    elif computer_score == 0 or computer_score == 21:
        return "User lost, Computer has a blackjack"
    elif user_score == 0 or user_score == 21:
        return "User won, you have a blackjack"
    elif user_score > 21:
        return "You bust! The computer wins!"
    elif computer_score > 21:
        return "The computer bust! User Wins!"
    elif user_score > computer_score:
        return "The user cards are closer to 21 than the computer, User wins!"
    else:
        return "You lose!"



def play_game():
    print(blackjack)
    user_hand = []
    computer_hand = []
    is_game_over = False
    for _ in range(2):
        # newCard = deal_cards()
        user_hand.append(deal_cards())
        computer_hand.append(deal_cards())

    while not is_game_over:
        user_score = calculate_scores(user_hand)
        # print(user_score)
        computer_score = calculate_scores(computer_hand)
        print(f"The user score is {user_score}, and the user hand is {user_hand}")
        print(f"The computer first card is {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit = input("Do you want to hit? (y/n): ")
            if hit == 'y':
                user_hand.append(deal_cards())
                # print(user_hand)
            else:
                is_game_over = True
        
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_cards())
        computer_score = calculate_scores(computer_hand)

    print(compare(user_score, computer_score))
    print(f"The user final hand is {user_hand}, the computer final hand is {computer_hand}")

while input("Do you want to play a game of blackjack? (y/n): ") == "y":
    play_game()



# def deal(user_total, computer_total):
#     for x in range(2):
#         user_hand.append(random.choice(cards))
#         user_total += int(user_hand[x])
#         computer_hand.append(random.choice(cards))
#         computer_total += int(computer_hand[x])
#     check_if_over(user_total, computer_total)

# def check_if_over(user_total, computer_total):
#     if computer_total == 21:
#         print("Computer has 21! User Lost")
#         playing = False
#     elif user_total == 21:
#         print("User has 21! Computer Lost")
#         playing = False
#     else:
#         print(user_hand)
#         print([computer_hand[0]])
#         print(computer_total)
#         print(user_total)
#         playing = False

# def check_if_over_single(total, player):
#     if total == 21:
#         print(f"{player} has 21! User Lost")
#         playing = False
#     else:
#         print(player)
#         print(total)
#         playing = False

# def hit_me(total, player):
#     player.append(random.choice(cards))
#     total += int(player[-1])
#     check_if_over_single(total, player)

# while playing:
#     deal(user_total, computer_total)    
#     add_card_choice = input("Would you like to hit? (yes/no) ")
#     if add_card_choice == 'yes':
#         hit_me(user_total, user_hand)
    
#     playing = False
#     user_total = 0





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
