def sales():
    n = int(input("Please enter the number of packages purchased: "))
    p = n * 99
    
    if n < 10:
        print("You unfortunately do not qualify for a discount, but thank you for your purchase.")
        print("Your total will be $",p,)
    
    elif n >= 10 and n <= 19:
        d = 0.1
        
        print("You get a 10% discount! Thank you for your purchase.")
        print("Your total will be $", p - (p * d))
    
    elif n >= 20 and n <= 49:
        d = 0.2
        
        print("You get a 20% discount! Thank you for your purchase.")
        print("Your total will be $",p - (p * d))
    
    elif n >= 50 and n <= 99:
        d = 0.3
        
        print("You get a 30% discount! Thank you for your purchase.")
        print("Your total will be $", p - (p * d))
        
    elif n >= 100:
        d = 0.4
        
        print("You get a 40% discount! Thank you for your purchase.")
        print("Your total will be $", p - (p * d))
    
    
    
    
sales()