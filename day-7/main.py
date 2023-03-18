import requests
import random
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
from hangman import *



response = requests.get(word_site)
WORDS = response.content.splitlines()
word = str(random.choice(WORDS))
new_word = word.replace("'","")
final_word = new_word.replace("b","", 1)
# final_word = list(final_word)
letter = input("Guess a letter: ").lower()
print(full_hangman_headless)
print( full_hangman)
print(final_word)

for each_letter in final_word:
    if letter == each_letter:
        print("Right")
    else:
        print("Wrong")