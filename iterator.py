
class Data:
    
    def __init__(self, limit, value):
        self.limit = limit
        self.value = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        x = self.value
        if x > self.limit:
            raise StopIteration
        else:
            self.value = x + 1
            return x 
        
        
num1 = int(input('Enter first value: '))
num2 =int(input('Enter second, higher value: '))


for i in Data(num2, num1):
    print(i)