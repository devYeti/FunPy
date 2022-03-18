# A simple function that counts the number of words
# in a given string by counting spaces.

def word_count(text):
    count = 1
    for i in text:
        if i == ' ':
            count += 1
    return count

def run_count():
    user_text = input('Enter text: ')
    total = word_count(user_text)
    print(total)
    
    again = input('Would you like to try again (y/n)? ')
    if again == 'y':
        run_count()
    else:
        print:('Goodbye!')
    
    
run_count() 

