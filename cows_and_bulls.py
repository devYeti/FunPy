# To play cows and bulls the computer will generate a number
# between 1000 and 9999. The player will then guess a number 
# in that range. A bull is awarded for the correct digit in 
# the correct position. A cow is awarded for the correct 
# digit in an incorrect position. The score is shown and the
# player makes another guess. Fifteen attempts are allowed.


import random

def cows_and_bulls():
    secret = str(random.randint(1000,9999))
    attempts = 15
    herd = [0,1,2,3]
    
    if attempts > 0:
        guess = input("Guess a number between 1000 and 9999: ")
        bulls = 0
        cows = 0
        
        if guess == secret:
            print("You guessed it!")      
        else:
            for i in herd:
                if guess[i] == secret[i]:
                    bulls += 1
                    continue
                elif guess[i] in secret:
                    cows += 1
        
        print("bulls: ", bulls)
        print("cows: ", cows)
        attempts -= 1
        print("remaining attempts: ", attempts)
    
    else:
        print("You have died of dysentry!")
    
    
cows_and_bulls()