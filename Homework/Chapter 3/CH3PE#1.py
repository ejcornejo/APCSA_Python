def number_analyser():
    x = int(input("Please enter any integer you want: "))
    
    if x > 0:
        print("Your number is positive and ")
        
        if x % 2 == 0:
            print("even.")
            
        else:
            print("odd.")
            
    elif x == 0:
        print("Brother eww, why are you trying to be different")
        print("(you're just being weird) and pick 0?")
        
    else:
        print("You number is negatve! and ")
        
        if x % 2 == 0:
            print("even.")
            
        else:
            print("odd.")
        
    
        
number_analyser()