#a function which will find the least common multiple of two user entered integers.

def find_lcm(num1, num2):
    mult1 = []
    mult2 = []
    multiples = []
    
    for i in range(1, 50):
        mult1.append(num1 * i)
    for j in range(1, 50):
        mult2.append(num2 * j)
        
    for n in mult1:
        if n in mult2:
            multiples.append(n)
            
    lcm = min(multiples)
    return(lcm)

def run_lcm():
    user_num1 = int(input('Enter first integer: '))
    user_num2 = int(input('Enter second integer: '))
    
    answer = find_lcm(user_num1, user_num2)
    print(answer)
    
    again = input('Would you like to try again (y/n)? ')
    
    if again = 'y':
        run_lcm()
    else:
        print('Goodbye!')

run_lcm()