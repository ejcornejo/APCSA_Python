def main():
    
    rows = int(input("How many rows do you want to have?: "))
    print()
    
    for i in range(rows):
        print("#", end = "")
        
        for count in range(i):
            
            print(" ", end = "")
        
        print("#")
               
        
main()# To get the desired output, enter 6