import requests
import random
from hangman import *
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
word = str(random.choice(WORDS))
new_word = word.replace("'","")
final_word = new_word.replace("b","", 1)
display = []
for each_letter in final_word:
    display += "_"
print("Hello Friend! Welcome to a hangman!")
print("We are using the MIT ecprice word list, so good luck!")
print(f"Your word is:\n {display}")
# letter = input("Guess a letter: ").lower()
counter = 0
word_length = len(final_word)
# print(word_length)
# print(final_word)
guessed_letters = []
lives = 7
while word_length > 0:
    letter = input("Guess a letter: ").lower()
    if guessed_letters.count(letter) != 0:
        print("You have already guessed this letter! Guess a new letter!")
        print(f"Words you have guessed: {guessed_letters}")
    else:
        for each_letter in final_word:
            if letter == each_letter:
                # print("Right")
                display[counter] = letter
                counter += 1
                # print(display)
                word_length -= 1
            else:
                # print("Wrong")
                # print(display)
                counter += 1
        print(display)
        guessed_letters.append(letter)
        if display.count(letter) != 0:
            print(f"Words you have guessed: {guessed_letters}")
            print(f"The letter {letter} was found!")
        if display.count(letter) == 0:
            print(f"Words you have guessed: {guessed_letters}")
            print(f"The letter {letter} was not found!")
            lives -= 1
        if display.count("_") == 0:
            print("You Won! Congratulations")
            print(f"Your word was {final_word}")
            word_length = 0
        if lives == 7:
            print(full_hangman_headless)
        elif lives == 6:
            print(full_hangman_minus_six)
        elif lives == 5:
            print(full_hangman_minus_five)
        elif lives == 4:
            print(full_hangman_minus_four)
        elif lives == 3:
            print(full_hangman_minus_three)
        elif lives == 2:
            print(full_hangman_minus_two)
        elif lives == 1:
            print(full_hangman_minus_one)
            print("One guess left!!")
        elif lives == 0:
            print("You Lost!")
            print(full_hangman)
            print(f"Your word was {final_word}")
            word_length = 0
        counter = 0
