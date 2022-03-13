# Takes user entered length and generates a
# random password using uppercase letters, 
# lowercase letters, numbers, and special
# characters. 

import random
import string


def pass_gen(length):
    letters = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation
    full_set = letters + numbers + characters
    password = ''
    
    while length > 0:
        password += full_set[random.randint(0, len(full_set))]
        length -= 1
    return password

def run_gen():
    user_length = int(input('Enter passord length: '))
    new_pass = pass_gen(user_length)
    print(new_pass)
    
    again = input('Would you like to create another password (y/n): ')
    if again == 'y':
        run_gen()
    else:
        print('Stay Safe!')
        print('Goodbye')
    

run_gen()     