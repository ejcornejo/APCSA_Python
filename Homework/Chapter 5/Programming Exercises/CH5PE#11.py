import random

def test():
    
    for i in range(1, 6):
    
        print("Question", i)
        
        num1 = random.randint (1, 10)
        
        num2 = random.randint (1, 10)
        
        print(num1, "+", num2, "= _____")
        print()
        
    
test()