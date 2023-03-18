import requests
import random
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
word = str(random.choice(WORDS))
new_word = word.replace("'","")
final_word = new_word.replace("b","", 1)

