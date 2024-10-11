def main():
    print("What's up!")
    i = 1
    while i != 0:
        x = int(input("Please enter any number: "))
        y = int(input("Please enter another number: "))
        
        print()
        print("Your numbers", x, "+", y, "is equal to:", x + y)
        print()
        
        i = int(input("Do you want to add more? Press any number to continue. Press '0' if no: "))
        print()
main()