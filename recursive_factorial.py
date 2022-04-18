def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def run_fact():
    num = int(input("Enter an integer: "))
    factorial(num)
    
run_fact()
