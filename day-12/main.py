# guessing number game
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty to play, 'easy' or 'hard': ")
number = random.randint(1, 100)
lives = 0
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
else:
    print('Choose a valid difficulty to play')


while lives > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You got it right!")
        lives = 0
    elif guess > number:
        print("Too high.")
        print("guess again")
        lives -= 1
    elif guess < number:
        print("Too low.")
        print("guess again")
        lives -= 1
    if lives == 0 and guess != number:
        print("You've run out of guesses, you lose.")
    elif lives > 0:
        print(f"You have {lives} guesses left.")
