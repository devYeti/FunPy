#A function that counts the vowels in user entered text


def count_vowels():
    text = input("Enter text: ")
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    print(count)
    again = input("Would you like to try again (y/n)? ")
    
    if again == 'y':
        count_vowels()
    else:
        print("Goodbye!")
        
count_vowels()

    