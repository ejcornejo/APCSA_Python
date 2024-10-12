def factorial():
    print("Hi there, I'm here to calculate factorials for you!")
    num = int(input("Please enter a nonnegative integer: "))
    result = 1 
    for i in range (2, num+1):
        result *= i

        
    print(num,"! =", result)

factorial()