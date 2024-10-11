def main():
    print("Hey there!")
    x = int(input("Please enter a number less than 100: "))
    print(x)
    
    if x < 100:
        
        product = x
        
        while product < 100:
            product = product * 10
            
            print(product)
        
    else:
        print("Not a valid number.")
       
main()

# If you enter a value <= 0 the program will keep running.

# If you let it do so for longer it will eventually crash because
# you are using too much system memory.

# This happens because the while loop never terminates because "x" will never
# be greater than 100 because 0 * 10 = 0 but it keeps trying to do it because
# it is in a loop that only breaks once the number is over 100
# (which as I said, never happens).

# It also happens with number < 0 because it is a negative number times a postive number
# will always be negative and not greater than 100.
