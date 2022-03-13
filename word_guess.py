# I'm not sure what I was trying to do here.
# Adding it to the repository incase I want to come 
# back to it. 

import string
import random

def word_guess():
    alphabet = string.ascii_lowercase
    wordlist = ['-', '-', '-', '-']
    letters = 2
    
    while letters > 0:
        spot = random.randint(0, 3)
        if wordlist[spot] == '-':
            wordlist[spot] = alphabet[random.randint(1, 26)]
            letters -= 1
            
    word = wordlist[0] + wordlist[1] + wordlist[2] + wordlist[3]
    
    guesses = []
    
word_guess()