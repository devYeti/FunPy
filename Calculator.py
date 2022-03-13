#a basic calculator capable of arithmatic on integers. 

def calculator():
    num1 = int(input("Enter first value: "))
    operator = input("Enter operator: ")
    num2 = int(input("Enter second value: "))
    
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Please enter a valid operator!")
        calculator()
    
    again = input("Would you like to try another problem? (y or n)")
    
    if again == "y":
        calculator()
    else:
        print("Goodbye!")
        
        
calculator()
    