# Guess a number between 1 and 10.
# Get ten points for every correct guess.
# Game repeats until loop is stopped. 

import random

def guessing_game():
    play = True
    score = 0
    
    while play == True:
        num = input('Enter a number between 1 and 10. Enter "q" to quit: ')
        
        if num == 'q' or num == 'Q':
            print('Your final score is ', score)
            print('Game Over')
            play = False
        else:
            guess = int(num)
            check = random.randint(1,10)
            if guess == check:
                score += 10
                print('You guessed it!')
                print('Your score is ', score)
            else:
                print('Oops! Wrong answer!')
                print('Your score is ', score)
                
guessing_game()