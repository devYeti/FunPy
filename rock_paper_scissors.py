# Prepare yourself for nonstop excitement and
# edge of your seat thrills as you play
# the classic Rock, Paper, Scissors game
# against the Python RNG!!


import random

def rock_paper_scissors():
    play = True
    options = ['rock', 'paper', 'scissors']
    play_score = 0
    comp_score = 0
    
    while play == True:
        pick = input('Choose rock, paper, or scissors ("q" to quit): ')
        game = options[random.randint(0,2)]
        if pick in options:
            print('You chose: ' + pick)
            print('The computer picks: ' + game)
        
        if pick == 'q' or pick == 'Q':
            print('Thanks for playing!')
            print('Final Score:')
            print('Player: ', play_score)
            print('Computer: ', comp_score)
            play = False
        
        elif pick == 'rock':
            
            if game == 'rock':
                print("It's a tie!")
            elif game == 'paper':
                print('Sorry, you lose.')
                comp_score +=1
            else:
                print('You Win!')
                play_score += 1
            
            print('Player Score: ', play_score)
            print('Computer Score: ', comp_score)
        
        elif pick == 'paper':
            
            if game == 'paper':
                print("It's a tie!")
            elif game == 'scissors':
                print('Sorry, you lose.')
                comp_score += 1
            else:
                print('You Win!')
                play_score += 1
            
            print('Player Score: ', play_score)
            print('Computer Score: ', comp_score)
        
        elif pick == 'scissors':
            
            if game == 'scissors':
                print("It's a tie!")
            elif game == 'rock':
                print('Sorry, you lose.')
                comp_score += 1
            else:
                print('You Win!')
                play_score += 1
            
            print('Player Score: ', play_score)
            print('Computer Score: ', comp_score)
        
        else:
            print('Please enter a valid choice.')



rock_paper_scissors()      
            
