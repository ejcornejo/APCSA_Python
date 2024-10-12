def main():
    print('Hello!')
    print()
    x = int(input("Please enter 1st number you want to multiply by: "))
    y = int(input("Please enter 2nd number you want to multiply by: "))
    print()
    print("Your answer using recursion is",multiply(x, y))
    print()
    print("Your answer using multiplication is", x * y)

def multiply(x, y):
    if x == 0:
        return 0
    return y + multiply(x - 1, y)
    
   
main()
