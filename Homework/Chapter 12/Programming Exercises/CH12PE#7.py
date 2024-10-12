def main():
    
    x = int(input("Please enter the number will be the base: "))
    y = int(input("Please enter the power you want the base to be raised to: "))
    print()
    raised_num = 1
    
    for i in range(0, y):
        
        raised_num *= power(x,y)
        
    print(x, "to the power of", y, "is:" ,raised_num)
    
    
def power(x,y):
    total = 1
    if y == 1:
        return x
    
    elif y == 0:
        return 1
    
    else:
        y -= 1
        total *= power(x,y)
        return total
        
main()