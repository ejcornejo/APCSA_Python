def average_rain():
    print("A program to collect data and calculate the average rainfall over a certain period of years.")
    print()
    year = int(input("Please enter the number of years: "))
    print()
    
    count = 0
    
    inch = 0
    
    while count < year:
        
        count += 1
        
        for i in range(1, 13):
            
            print("For month", i,)
            
            inch = inch + float(input("please enter inches of rainfall: "))
            print()
            
    print()       
    print("Over", (year * 12), "Months, there was a total of", inch, "inches of rain.")
    print()
    print("Overall, there was an average rainfall of", (inch / (year * 12)), "per month.")
    
    
    
    
average_rain()