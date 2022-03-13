# A function which finds the greatest common denominator for two user entered integers. 

def find_gcd(num1, num2):
    numbers = []
    common = []
    numbers.append(num1)
    numbers.append(num2)
    small = min(numbers) + 1
    
    for i in range(1, small):
        if num1 % i == 0 and num2 % i == 0:
            common.append(i)
        else:
            continue
    
    gcd = max(common)
    return gcd

def run_gcd():
    user_num1 = int(input('Enter first integer: '))
    user_num2 = int(input('Enter second integer: '))
    
    answer = find_gcd(user_num1, user_num2)
    print(answer)
    
    again = input('Would you like to try again (y/n)? ')
    
    if again = 'y':
        run_gcd()
    else:
        print('Goodbye!')
        
run_gcd()