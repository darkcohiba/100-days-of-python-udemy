import random

print("Welcome to Rock, Paper, Scissors!")

computer_score = 0
user_score = 0
game = 0
while game == 0:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")
    computer_choice = random.randint(0,2)
    choice = int(choice)
    print(f"player choice {choice}")
    print(f"computer choice {computer_choice}")
    if choice == 0:
        print("Rock Art")
    elif choice == 1:
        print("paper art")
    elif choice == 2:
        print("scissors art")
    else: 
        print("please choose 0, 1 or 2")

    if computer_choice == 0:
        print("Computer chose: \n Rock Art")
    elif computer_choice == 1:
        print("Computer chose: \n paper art")
    elif computer_choice == 2:
        print("Computer chose: \n scissors art")
    else:
        print("techical error")


    if choice == 0 and computer_choice == 0:
        print("Tie game")
    elif choice == 1 and computer_choice == 1:
        print("Tie game")
    elif choice == 2 and computer_choice == 2:
        print("Tie game")
    elif choice == 0 and computer_choice == 1:
        print("Paper beats Rock, you lose.")
        computer_score += 1
    elif choice == 0 and computer_choice == 2:
        print("Rock beats Scissors, you win.")
        user_score += 1
    elif choice == 1 and computer_choice == 0:
        print("Paper beats Rock, you win.")
        user_score += 1
    elif choice == 1 and computer_choice == 2:
        print("Scissors beats Paper, you lost.")
        computer_score += 1
    elif choice == 2 and computer_choice == 0:
        print("Rock beats Scissors, you lost.")
        computer_score += 1
    elif choice == 2 and computer_choice == 1:
        print("Scissors beats Paper, you win.")
        user_score += 1
    else:
        print(f"You didn't put in a valid number so the computer wins")

    
    print(f"score is user: {user_score}, computer {computer_score}")

    play_again = int(input("Would you like to play again, 1 to play again, 2 to quit?: "))

    if (play_again == 2):
        game += 1

